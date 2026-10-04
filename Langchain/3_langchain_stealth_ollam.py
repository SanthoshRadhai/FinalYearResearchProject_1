"""
Interactive LangChain <-> MCP client for the stealth-browser-mcp server,
targeting a local SGLang server instead of vLLM.

Spawns the MCP server over stdio, loads its tools into LangChain, wires them
into a ReAct agent, and gives you a simple REPL to chat with it while it
drives the browser tools on your behalf.

Install:
    pip install langchain langchain-mcp-adapters langgraph langchain-openai mcp

Run:
    python mcp_browser_chat_sglang.py
"""

import asyncio
import os
import re

from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp import ClientSession

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, SystemMessage

# Set DEBUG_HARMONY=1 in the environment to print the model's raw output
# (content + tool_calls) on every turn, BEFORE any Harmony-token stripping.
# This is the fastest way to see whether the model is actually producing a
# next tool call that SGLang's parser is failing to extract (raw Harmony
# markup ends up in `content` with `tool_calls` empty), versus the model
# genuinely stopping on its own.
DEBUG_HARMONY = os.environ.get("DEBUG_HARMONY", "0") == "1"

# Matches leaked gpt-oss/Harmony control tokens like <|channel|>, <|end|>,
# <|start|>, <|constrain|>, <|call|>, <|message|>, etc.
#
# NOTE: this defense is backend-agnostic and worth keeping even on SGLang.
# SGLang's own --reasoning-parser/--tool-call-parser (gpt-oss) is supposed to
# separate reasoning/tool-call content from the visible response, but SGLang
# has had its own recurring Harmony-parsing bugs (channel markers leaking
# into "content" during commentary-channel messages or truncated/streamed
# tool calls, tracked across several sglang issues over 2025-2026). Keep the
# sanitizer as a safety net regardless of backend.
HARMONY_TOKEN_RE = re.compile(r"<\|[a-z_]+\|>")


def _strip_harmony_tokens(text):
    if not isinstance(text, str):
        return text
    return HARMONY_TOKEN_RE.sub("", text)


def sanitize_ai_message(state):
    """post_model_hook: runs right after the LLM produces an AIMessage and
    right before LangGraph decides whether to dispatch tool calls. Strips
    leaked Harmony control tokens from the tool call names and from the
    message content, so corrupted tokens never reach the tool dispatcher
    and never get written into history for the next turn."""
    messages = state["messages"]
    last = messages[-1]
    if not isinstance(last, AIMessage):
        return {}

    if DEBUG_HARMONY:
        raw_preview = repr(last.content)
        if len(raw_preview) > 1000:
            raw_preview = raw_preview[:1000] + "...[truncated]"
        print(f"\n[debug] raw AIMessage.content BEFORE sanitization: {raw_preview}")
        print(f"[debug] raw AIMessage.tool_calls BEFORE sanitization: {last.tool_calls}")
        # Some SGLang versions have put the model's actual final text into
        # additional_kwargs (e.g. reasoning_content) instead of .content due
        # to a Harmony content/reasoning field mix-up. Check both.
        kwargs_preview = repr(last.additional_kwargs)
        if len(kwargs_preview) > 1000:
            kwargs_preview = kwargs_preview[:1000] + "...[truncated]"
        print(f"[debug] raw AIMessage.additional_kwargs: {kwargs_preview}")
        print(f"[debug] response_metadata finish_reason: "
              f"{last.response_metadata.get('finish_reason', '<not present>')}\n")

    changed = False

    new_content = _strip_harmony_tokens(last.content)
    if new_content != last.content:
        changed = True

    new_tool_calls = []
    for call in (last.tool_calls or []):
        cleaned_name = _strip_harmony_tokens(call["name"])
        if cleaned_name != call["name"]:
            changed = True
        new_tool_calls.append({**call, "name": cleaned_name})

    if not changed:
        return {}

    print(f"[sanitized] removed leaked Harmony token(s) from assistant message")

    # Reuse the same message id so LangGraph's message reducer replaces the
    # original message in place instead of appending a duplicate.
    sanitized = AIMessage(content=new_content, tool_calls=new_tool_calls, id=last.id)
    return {"messages": [sanitized]}

SYSTEM_PROMPT = SystemMessage(content=(
    "You are a security research agent with access to browser automation "
    "tools via MCP (navigate, get_page_content, query_elements, etc.).\n\n"
    "You do NOT have reliable knowledge of CVEs, vulnerabilities, exploits, "
    "or any security advisory information — your training data may be "
    "outdated or you may simply be pattern-matching a plausible-sounding "
    "but fabricated answer. For ANY question that names a CVE ID, asks "
    "about a vulnerability, or asks about current security advisories, "
    "you MUST use the available tools to look up real information on the "
    "web BEFORE answering.\n\n"
    "IMPORTANT: NVD's and MITRE's human-facing websites are JavaScript "
    "single-page apps — fetching their raw HTML often returns just an "
    "empty app shell with no actual vulnerability data. Prefer "
    "machine-readable sources instead: NVD's REST API at "
    "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=<CVE-ID> "
    "returns the full record as plain JSON with no rendering required. "
    "If that returns no result, fall back to https://www.cve.org/CVERecord?id=<CVE-ID> "
    "and, if needed, wait for the page to fully render before reading it.\n\n"
    "Never state a CVSS score, affected product, affected version, or "
    "advisory URL unless you retrieved it via a tool call in this "
    "conversation. If a tool call fails or returns nothing relevant, say "
    "so explicitly rather than filling in plausible-sounding details."
))

# --- Point this at your MCP server's entrypoint ---
# Using the hexstrike conda env's interpreter directly (absolute path) avoids
# relying on `conda activate` having been run in this process's shell.
SERVER_PARAMS = StdioServerParameters(
    command="/home/johndoe/miniconda3/envs/hexstrike/bin/python",
    args=["server.py"],
    cwd="/mnt/s/FinalYear-Project/stealth-browser-mcp/src",
)

# --- Point this at your local OpenAI-compatible endpoint ---
# Currently pointed at localhost:1337 (looks like Ollama's OpenAI-compatible
# API based on the /v1/models response format — "id": "model:tag",
# "owned_by": "library"). Model name must match the exact tag string Ollama
# reports, including the ":latest" suffix, or requests will 404.
#
# max_tokens is the per-request generation budget (set by the client on each
# call, since neither Ollama nor SGLang expose a server-side cap for this).
# stream=False avoids the class of gpt-oss/Harmony channel-token leaks seen
# in streaming tool-call paths across multiple backends (SGLang issues
# #8976, #9139, #30480, #37187; similar reports exist for Ollama's own
# gpt-oss template). Non-streaming responses go through the full parser
# output rather than incremental chunk-by-chunk parsing.
llm = ChatOpenAI(
    base_url="http://localhost:1338/v1",
    api_key="EMPTY",
    model="gpt-oss-20b:latest",
    temperature=0,
    max_tokens=16000,
    streaming=False,
)


async def main():
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            print(f"Loaded {len(tools)} tools from MCP server:")
            for t in tools:
                print(f"  - {t.name}")
            print()

            agent = create_react_agent(llm, tools, post_model_hook=sanitize_ai_message)

            history = [SYSTEM_PROMPT]
            print("Interactive session started. Type 'exit' or 'quit' to stop.\n")

            while True:
                user_input = input("You: ").strip()
                if user_input.lower() in ("exit", "quit"):
                    break
                if not user_input:
                    continue

                history.append(HumanMessage(content=user_input))
                prev_len = len(history)

                try:
                    result = await agent.ainvoke({"messages": history})
                except Exception as e:
                    print(f"[error] {e}\n")
                    continue

                messages = result["messages"]
                history = messages  # keep full updated history for next turn

                # Print every tool call + tool result generated during this turn,
                # in order, before the final answer.
                tool_call_count = 0
                for msg in messages[prev_len:]:
                    if isinstance(msg, AIMessage) and msg.tool_calls:
                        for call in msg.tool_calls:
                            tool_call_count += 1
                            print(f"[tool call] {call['name']}({call['args']})")
                    elif isinstance(msg, ToolMessage):
                        preview = str(msg.content)
                        if len(preview) > 300:
                            preview = preview[:300] + "... [truncated]"
                        print(f"[tool result] {msg.name}: {preview}")

                if tool_call_count == 0:
                    print("[warning] agent answered without calling any tool")

                # Print the final AI message content
                last_ai = messages[-1]
                print(f"\nAgent: {last_ai.content}\n")


if __name__ == "__main__":
    asyncio.run(main())