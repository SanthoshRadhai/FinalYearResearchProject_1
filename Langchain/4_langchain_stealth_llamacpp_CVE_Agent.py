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

import httpx

from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp import ClientSession

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.graph.message import RemoveMessage
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

# Tracks consecutive malformed tool calls (empty required args, or garbage
# repeated-character args) across a single agent turn. llama.cpp's grammar-
# constrained tool calling can fight gpt-oss's native Harmony output format,
# and once the model gets stuck it tends to spiral into worse and worse
# garbage rather than recovering — better to cut it off cleanly than let it
# grind toward a 500 "peg-native format" error.
_malformed_call_streak = {"count": 0}
MALFORMED_CALL_LIMIT = 2  # abort after this many consecutive bad calls in a row


def _looks_malformed(call):
    args = call.get("args", {})
    # Empty string for what's almost always a required identifier
    if args.get("instance_id", "__unset__") == "":
        return True
    # Degenerate repeated-character garbage (seen as e.g. "??..??..??..")
    for v in args.values():
        if isinstance(v, str) and len(v) > 40:
            prefix = v[:4]
            if prefix and v.count(prefix) > 5:
                return True
    return False


def _strip_harmony_tokens(text):
    if not isinstance(text, str):
        return text
    return HARMONY_TOKEN_RE.sub("", text)


# --- Early auto-recovery: tool call before any browser exists ---------------
# Observed failure mode: on the very first turn (before spawn_browser has ever
# been called), the model sometimes reaches straight for a tool that needs an
# existing browser instance (execute_cdp_command, get_page_content, navigate,
# ...) with an empty or garbage instance_id. Left alone, this either wastes a
# guaranteed-failing round trip or — if it happens twice in a row — trips the
# circuit breaker before the agent ever gets a real chance to do the task. It's
# a much cheaper, more targeted fix than the circuit breaker: since we already
# know the fix (call spawn_browser first), just redirect the call there
# instead of dispatching it or waiting for a second failure.
def _instance_id_looks_bad(value):
    if not isinstance(value, str) or value == "":
        return True
    if len(value) > 40:
        prefix = value[:4]
        if prefix and value.count(prefix) > 5:
            return True
    return False


def _has_live_browser_instance(messages):
    for m in messages:
        if isinstance(m, ToolMessage) and m.name == "spawn_browser":
            content = str(m.content)
            if '"success":false' not in content and '"instance_id"' in content:
                return True
    return False


def _maybe_redirect_to_spawn_browser(last, messages):
    """If the model's first tool call needs a live instance_id but none has
    ever been spawned in this conversation, replace it with a spawn_browser
    call instead of letting it dispatch (or counting toward the circuit
    breaker). Returns a replacement AIMessage, or None if no redirect is
    needed."""
    if not last.tool_calls:
        return None
    first_call = last.tool_calls[0]
    if first_call.get("name") == "spawn_browser":
        return None
    args = first_call.get("args", {})
    if "instance_id" not in args:
        return None
    if not _instance_id_looks_bad(args["instance_id"]):
        return None
    if _has_live_browser_instance(messages):
        return None  # a real instance exists — this is a different bug, let the circuit breaker handle it

    print(f"[auto-recover] '{first_call.get('name')}' was called with no live "
          f"browser instance yet — redirecting to spawn_browser first instead "
          f"of dispatching a guaranteed-failing call.")
    return AIMessage(
        content="",
        tool_calls=[{
            "name": "spawn_browser",
            "args": {"headless": True},
            "id": first_call["id"],
            "type": "tool_call",
        }],
        id=last.id,
    )


# --- Context-window compaction ---------------------------------------------
# The ReAct loop can accumulate a lot of tool-call/tool-result round trips
# within a single turn (e.g. several failed execute_script retries before the
# model lands on the right approach). Once the running history gets close to
# the server's context limit, the *next* request hard-fails with llama.cpp's
# "request exceeds the available context size" 400 error and the whole turn
# is lost. Rather than wait for that, we check the exact token count (via
# llama-server's own /tokenize endpoint, not a rough char-based guess) after
# every model response, and if it's getting close to the limit, drop the
# middle of the conversation — keeping the system prompt, the original
# request, and the most recent exchanges — before it ever hits the wall.
LLAMA_SERVER_HOST = "http://localhost:5500"
MAX_CONTEXT_TOKENS = 131072
COMPACT_TOKEN_THRESHOLD = int(MAX_CONTEXT_TOKENS * 0.75)
KEEP_RECENT_MESSAGES = 10  # always keep at least this many trailing messages intact


async def _count_tokens(client, text):
    if not text:
        return 0
    resp = await client.post(f"{LLAMA_SERVER_HOST}/tokenize", json={"content": text})
    resp.raise_for_status()
    return len(resp.json().get("tokens", []))


def _message_text(msg):
    parts = []
    if isinstance(msg.content, str):
        parts.append(msg.content)
    elif isinstance(msg.content, list):
        for item in msg.content:
            if isinstance(item, dict):
                parts.append(str(item.get("text", item)))
            else:
                parts.append(str(item))
    if isinstance(msg, AIMessage) and msg.tool_calls:
        for call in msg.tool_calls:
            parts.append(f"{call.get('name', '')}({call.get('args', {})})")
    return " ".join(parts)


async def _total_tokens(messages):
    async with httpx.AsyncClient(timeout=30) as client:
        total = 0
        for m in messages:
            total += await _count_tokens(client, _message_text(m))
        return total


def _find_clean_tail_start(messages, keep_last_n):
    """Index to slice the kept tail from, adjusted so it never starts with an
    orphaned ToolMessage — both llama.cpp and OpenAI-style APIs reject a tool
    result message whose originating AIMessage tool_call isn't present."""
    start = max(0, len(messages) - keep_last_n)
    while start > 0 and isinstance(messages[start], ToolMessage):
        start -= 1
    return start


async def _compact_if_needed(messages):
    """Returns a list of updates (RemoveMessage markers plus a short summary
    note) to shrink the history, or None if compaction isn't needed / wasn't
    possible right now."""
    try:
        total = await _total_tokens(messages)
    except Exception as e:
        print(f"[compact] token count check failed ({e}), skipping compaction")
        return None

    if total <= COMPACT_TOKEN_THRESHOLD:
        return None

    system_msgs = [m for m in messages if isinstance(m, SystemMessage)]
    non_system = [m for m in messages if not isinstance(m, SystemMessage)]

    tail_start = _find_clean_tail_start(non_system, KEEP_RECENT_MESSAGES)
    head = non_system[:tail_start]
    tail = non_system[tail_start:]

    if not head:
        return None  # nothing meaningful left to drop

    first_human = next((m for m in head if isinstance(m, HumanMessage)), None)
    to_remove = [m for m in head if m is not first_human]
    if not to_remove:
        return None

    print(f"[compact] history at ~{total} tokens (over {COMPACT_TOKEN_THRESHOLD}) — "
          f"dropping {len(to_remove)} older message(s), keeping the original "
          f"request and the last {len(tail)} message(s)")

    summary_note = SystemMessage(content=(
        f"[{len(to_remove)} earlier tool call/result messages were removed "
        f"from history to stay within the model's context window. The "
        f"original request and the most recent exchanges below are "
        f"unaffected.]"
    ))

    updates = [RemoveMessage(id=m.id) for m in to_remove]
    updates.append(summary_note)
    return updates


async def sanitize_ai_message(state):
    """post_model_hook: runs right after the LLM produces an AIMessage and
    right before LangGraph decides whether to dispatch tool calls. Strips
    leaked Harmony control tokens from the tool call names and from the
    message content, so corrupted tokens never reach the tool dispatcher
    and never get written into history for the next turn. Also checks the
    running token count and compacts history if it's approaching the
    context-window limit (see _compact_if_needed above)."""
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

    # --- Auto-recover from a premature tool call (see helper above) ---
    redirected = _maybe_redirect_to_spawn_browser(last, messages)
    if redirected is not None:
        return {"messages": [redirected]}

    # --- Circuit breaker for degenerate/malformed tool-call loops ---
    if last.tool_calls and any(_looks_malformed(c) for c in last.tool_calls):
        _malformed_call_streak["count"] += 1
        if _malformed_call_streak["count"] >= MALFORMED_CALL_LIMIT:
            print(f"[circuit-breaker] {_malformed_call_streak['count']} consecutive "
                  f"malformed tool calls detected — aborting this turn instead of "
                  f"letting it spiral toward a server error.")
            _malformed_call_streak["count"] = 0
            return {"messages": [AIMessage(
                content=(
                    "I ran into repeated malformed tool calls (likely a mismatch "
                    "between this backend's tool-calling grammar and the model's "
                    "native output format) and stopped rather than continuing to "
                    "retry. Try rephrasing the request, or check the backend's "
                    "tool-calling configuration."
                ),
                id=last.id,
            )]}
    else:
        _malformed_call_streak["count"] = 0

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

    updates = []
    if changed:
        print(f"[sanitized] removed leaked Harmony token(s) from assistant message")
        # Reuse the same message id so LangGraph's message reducer replaces
        # the original message in place instead of appending a duplicate.
        updates.append(AIMessage(content=new_content, tool_calls=new_tool_calls, id=last.id))

    # --- Context-window compaction check (runs on every turn, regardless of
    # whether the sanitization step above changed anything) ---
    compaction_updates = await _compact_if_needed(messages)
    if compaction_updates:
        updates.extend(compaction_updates)

    if not updates:
        return {}
    return {"messages": updates}

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
# --- Point this at your local OpenAI-compatible endpoint ---
# Currently pointed at localhost:5500, which is a llama.cpp server
# (llama-server) based on the /v1/models response ("owned_by": "llamacpp").
# llama.cpp requires the exact model PATH as the "model" field, not a short
# name/tag like Ollama uses — copy this verbatim from `curl .../v1/models`
# if it ever changes (e.g. after moving the GGUF file).
#
# IMPORTANT — tool calling caveat: the /v1/models response here only lists
# "capabilities": ["completion"], with no "tools" entry. llama-server only
# exposes OpenAI-style tool/function calling when started with the --jinja
# flag (so it can apply the GGUF's embedded chat template, which is what
# actually defines the tool-call format) AND the GGUF's template supports
# it. If you get malformed tool calls or a "tools not supported"-style
# error here, check that the server was launched with --jinja and that
# gpt-oss-20b-F16.gguf has Harmony-compatible chat template metadata baked
# in (recent gpt-oss GGUF conversions do; older ones may not).
#
# max_tokens is the per-request generation budget (llama.cpp has no
# server-side cap equivalent — it's set by the client on each call).
# stream=False avoids the class of gpt-oss/Harmony channel-token leaks seen
# in streaming tool-call paths across multiple backends. Non-streaming
# responses go through the full parser output rather than incremental
# chunk-by-chunk parsing.
llm = ChatOpenAI(
    base_url="http://localhost:5500/v1",
    api_key="EMPTY",
    model="/home/vishnudharanb.23it/Santhosh/gpt-oss-20b/gpt-oss-20b-F16.gguf",
    temperature=0.2,
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