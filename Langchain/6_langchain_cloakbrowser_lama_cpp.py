"""
Interactive LangChain <-> MCP client for the cloakbrowser-mcp server
(https://github.com/swimmwatch/cloakbrowser-mcp), talking to a local
OpenAI-compatible endpoint (llama.cpp / SGLang / Ollama).

cloakbrowser-mcp is a Node/TypeScript server that runs the upstream
`@playwright/mcp` tool surface unchanged, pointed at CloakBrowser Chromium.
That means:
  * it is launched over stdio with `npx -y cloakbrowser-mcp@latest`
    (NOT a Python `server.py`), so you need Node.js 22.13+ (22.x) or 24+;
  * the tools are the standard Playwright MCP tools — browser_navigate,
    browser_snapshot, browser_click, browser_type, browser_take_screenshot,
    browser_evaluate, browser_wait_for, ... — plus two local introspection
    tools, cloakbrowser_binary_info and cloakbrowser_bridge_info;
  * there is NO spawn_browser / instance_id concept. Playwright MCP manages
    a single browser context implicitly and hands you element `ref`s via
    accessibility snapshots. The correct workflow is: navigate -> snapshot
    to get refs -> act on those refs.

This script spawns the MCP server over stdio, loads its tools into LangChain,
wires them into a ReAct agent, and gives you a REPL to chat with it while it
drives the browser tools on your behalf.

Install (Python side):
    pip install langchain langchain-mcp-adapters langgraph langchain-openai mcp httpx

Install (server side) — nothing to pre-install; npx fetches it on first run.
On the very first launch Playwright/CloakBrowser may download a browser build,
so the first tool call can take a while.

Run:
    python mcp_cloakbrowser_chat.py
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
# next tool call that the backend's parser is failing to extract (raw Harmony
# markup ends up in `content` with `tool_calls` empty), versus the model
# genuinely stopping on its own.
DEBUG_HARMONY = os.environ.get("DEBUG_HARMONY", "0") == "1"

# Matches leaked gpt-oss/Harmony control tokens like <|channel|>, <|end|>,
# <|start|>, <|constrain|>, <|call|>, <|message|>, etc.
#
# This defense is backend-agnostic and worth keeping regardless of whether you
# run llama.cpp, SGLang, or Ollama behind the OpenAI-compatible endpoint. All
# of them have had recurring Harmony-parsing bugs where channel markers leak
# into "content" during commentary-channel messages or truncated/streamed tool
# calls. Keep the sanitizer as a safety net.
HARMONY_TOKEN_RE = re.compile(r"<\|[a-z_]+\|>")

# Tracks consecutive malformed tool calls (empty required args, or garbage
# repeated-character args) across a single agent turn. Grammar-constrained
# tool calling can fight gpt-oss's native Harmony output format, and once the
# model gets stuck it tends to spiral into worse and worse garbage rather than
# recovering — better to cut it off cleanly than let it grind toward a server
# error.
_malformed_call_streak = {"count": 0}
MALFORMED_CALL_LIMIT = 2  # abort after this many consecutive bad calls in a row

# Playwright MCP tools whose primary job needs an element `ref` obtained from a
# prior accessibility snapshot. If the model calls one of these with a bad/empty
# ref before any snapshot has ever produced refs, redirect it to browser_snapshot.
REF_REQUIRING_TOOLS = {
    "browser_click",
    "browser_hover",
    "browser_type",
    "browser_select_option",
    "browser_drag",
    "browser_fill_form",
}

# Common "required identifier"-style keys across Playwright MCP tool schemas.
# Empty values for these almost always mean the model failed to produce a real
# argument rather than legitimately passing "".
REQUIRED_ISH_KEYS = ("ref", "url", "element", "selector", "text")


def _looks_degenerate(value):
    """True for garbage repeated-character strings, e.g. '??..??..??..'."""
    if not isinstance(value, str) or len(value) <= 40:
        return False
    prefix = value[:4]
    return bool(prefix) and value.count(prefix) > 5


def _looks_malformed(call):
    args = call.get("args", {}) or {}
    # Empty string for what's almost always a required identifier.
    for key in REQUIRED_ISH_KEYS:
        if args.get(key, "__unset__") == "":
            return True
    # Degenerate repeated-character garbage in any string arg.
    for v in args.values():
        if _looks_degenerate(v):
            return True
    return False


def _strip_harmony_tokens(text):
    if not isinstance(text, str):
        return text
    return HARMONY_TOKEN_RE.sub("", text)


# --- Early auto-recovery: interaction before any snapshot exists -------------
# Observed failure mode (the Playwright-MCP analog of "tool call before any
# browser exists"): the model reaches straight for browser_click / browser_type
# with a made-up or empty `ref` before ever taking a browser_snapshot, so it has
# no valid element references. Left alone this wastes a guaranteed-failing round
# trip or — twice in a row — trips the circuit breaker before the agent gets a
# real chance. Since we already know the fix (snapshot first to get refs), just
# redirect the call to browser_snapshot instead of dispatching it.
def _ref_looks_bad(value):
    if not isinstance(value, str) or value == "":
        return True
    return _looks_degenerate(value)


def _page_refs_available(messages):
    """Have any prior tool results actually surfaced element refs? Playwright MCP
    emits accessibility snapshots containing `[ref=eNN]` markers from
    browser_snapshot AND as a side effect of navigate/click/etc. If none of that
    has appeared yet, the model has nothing valid to reference."""
    for m in messages:
        if isinstance(m, ToolMessage) and "ref=" in str(m.content):
            return True
    return False


def _maybe_redirect_to_snapshot(last, messages):
    """If the model's tool call needs a live element ref but no snapshot has ever
    produced any refs in this conversation, replace it with a browser_snapshot
    call instead of letting it dispatch (or counting toward the circuit breaker).
    Returns a replacement AIMessage, or None if no redirect is needed."""
    if not last.tool_calls:
        return None
    first_call = last.tool_calls[0]
    name = first_call.get("name")
    if name not in REF_REQUIRING_TOOLS:
        return None
    args = first_call.get("args", {}) or {}
    ref = args.get("ref", "")
    if not _ref_looks_bad(ref):
        return None
    if _page_refs_available(messages):
        return None  # refs already exist — different bug, let the circuit breaker handle it

    print(f"[auto-recover] '{name}' was called with no valid element ref and no "
          f"snapshot has produced any yet — redirecting to browser_snapshot "
          f"first instead of dispatching a guaranteed-failing call.")
    return AIMessage(
        content="",
        tool_calls=[{
            "name": "browser_snapshot",
            "args": {},
            "id": first_call["id"],
            "type": "tool_call",
        }],
        id=last.id,
    )


# --- Context-window compaction ---------------------------------------------
# The ReAct loop can accumulate a lot of tool-call/tool-result round trips
# within a single turn (e.g. several snapshots, each of which can be large, plus
# failed action retries). Once the running history gets close to the server's
# context limit, the *next* request hard-fails with a "request exceeds the
# available context size" error and the whole turn is lost. Rather than wait for
# that, we check the exact token count (via the server's own /tokenize endpoint,
# not a rough char-based guess) after every model response, and if it's getting
# close to the limit, drop the middle of the conversation — keeping the system
# prompt, the original request, and the most recent exchanges — before it ever
# hits the wall.
#
# NOTE: /tokenize is a llama.cpp (llama-server) endpoint. SGLang and Ollama do
# not expose the identical route, so if you switch backends either point
# TOKENIZE_HOST at a llama-server you keep around just for counting, or replace
# _count_tokens with a tokenizer-based / char-heuristic estimate.
TOKENIZE_HOST = "http://localhost:5500"
MAX_CONTEXT_TOKENS = 131072
COMPACT_TOKEN_THRESHOLD = int(MAX_CONTEXT_TOKENS * 0.75)
KEEP_RECENT_MESSAGES = 10  # always keep at least this many trailing messages intact


async def _count_tokens(client, text):
    if not text:
        return 0
    resp = await client.post(f"{TOKENIZE_HOST}/tokenize", json={"content": text})
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
        f"[{len(to_remove)} earlier tool call/result messages (mostly large "
        f"page snapshots) were removed from history to stay within the model's "
        f"context window. The original request and the most recent exchanges "
        f"below are unaffected.]"
    ))

    updates = [RemoveMessage(id=m.id) for m in to_remove]
    updates.append(summary_note)
    return updates


async def sanitize_ai_message(state):
    """post_model_hook: runs right after the LLM produces an AIMessage and
    right before LangGraph decides whether to dispatch tool calls. Strips
    leaked Harmony control tokens from the tool call names and from the
    message content, so corrupted tokens never reach the tool dispatcher
    and never get written into history for the next turn. Also handles the
    early snapshot redirect, the malformed-call circuit breaker, and context
    compaction."""
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
        # Some backends put the model's actual final text into additional_kwargs
        # (e.g. reasoning_content) instead of .content due to a Harmony
        # content/reasoning field mix-up. Check both.
        kwargs_preview = repr(last.additional_kwargs)
        if len(kwargs_preview) > 1000:
            kwargs_preview = kwargs_preview[:1000] + "...[truncated]"
        print(f"[debug] raw AIMessage.additional_kwargs: {kwargs_preview}")
        print(f"[debug] response_metadata finish_reason: "
              f"{last.response_metadata.get('finish_reason', '<not present>')}\n")

    # --- Auto-recover from a premature interaction call (see helper above) ---
    redirected = _maybe_redirect_to_snapshot(last, messages)
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
    "You are a web automation agent with access to a Playwright-based browser "
    "via MCP (the cloakbrowser-mcp server, which exposes the standard "
    "@playwright/mcp tool surface).\n\n"
    "WORKFLOW — this browser is driven through accessibility snapshots, not "
    "raw CSS selectors:\n"
    "1. Use browser_navigate to open a URL.\n"
    "2. Use browser_snapshot to get the page's accessibility tree. Each "
    "interactive element is listed with a stable `ref` (e.g. ref=e12). These "
    "refs are the ONLY valid way to target elements.\n"
    "3. Use browser_click, browser_type, browser_hover, browser_select_option, "
    "browser_fill_form, etc. with the `ref` (and the human-readable `element` "
    "description) taken from the most recent snapshot.\n"
    "4. After an action that changes the page, take a fresh browser_snapshot — "
    "refs from an old snapshot may be stale after navigation or DOM updates.\n\n"
    "Never invent a `ref` value. If you don't have a current snapshot for the "
    "page you're acting on, call browser_snapshot first. Use "
    "browser_take_screenshot when you need to visually confirm state, and "
    "browser_evaluate for reading values or running small JS in page context.\n\n"
    "Do not claim a page said something, or that an action succeeded, unless a "
    "tool result in THIS conversation shows it. If a tool call fails or returns "
    "nothing relevant, say so explicitly rather than guessing.\n\n"
    "The tools cloakbrowser_binary_info and cloakbrowser_bridge_info report "
    "the CloakBrowser build and bridge metadata — use them only if asked about "
    "the environment itself."
))

# --- Point this at the cloakbrowser-mcp server entrypoint --------------------
# cloakbrowser-mcp is a Node package launched over stdio via npx. This requires
# Node.js 22.13+ (in the 22.x line) or 24+ on PATH. On the first run npx will
# download the package (and CloakBrowser/Playwright may fetch a browser build),
# so the first tool call can be slow.
#
# Flags after the package name are forwarded to the underlying Playwright MCP
# runtime. `--headless` runs without a visible window; drop it to watch the
# browser. Cloak-specific behavior is controlled via CLOAK_PLAYWRIGHT_MCP_*
# environment variables and upstream behavior via PLAYWRIGHT_MCP_* — pass those
# through `env=` below if you need them.
#
# On Windows, npx is a shell script; if StdioServerParameters can't find it,
# use command="npx.cmd" (or the absolute path to it) instead.
SERVER_PARAMS = StdioServerParameters(
    command="npx",
    args=["-y", "cloakbrowser-mcp@latest"],
    # cwd=".",  # artifacts (screenshots, downloads) are written relative to here
    # env={"CLOAK_PLAYWRIGHT_MCP_NO_SANDBOX": "true"},  # e.g. in containers
)

# --- Point this at your local OpenAI-compatible endpoint --------------------
# Configured below for a llama.cpp server (llama-server) on localhost:5500.
# Notes that carry over from the original stealth-browser client:
#
#  * MODEL FIELD: llama.cpp requires the exact model PATH as the "model" field,
#    not a short name/tag. Copy it verbatim from `curl .../v1/models` if it
#    changes (e.g. after moving the GGUF). Ollama instead wants the exact tag
#    string it reports (including any ":latest" suffix) or requests 404.
#
#  * TOOL CALLING (llama.cpp): OpenAI-style tool/function calling is only
#    exposed when llama-server is started with --jinja (so it applies the GGUF's
#    embedded chat template, which defines the tool-call format) AND the GGUF's
#    template supports it. If you get malformed tool calls or a "tools not
#    supported" error, verify the server was launched with --jinja and that the
#    gpt-oss GGUF has Harmony-compatible chat-template metadata baked in.
#
#  * max_tokens is the per-request generation budget (llama.cpp / Ollama /
#    SGLang have no server-side cap equivalent — the client sets it per call).
#
#  * stream=False avoids the class of gpt-oss/Harmony channel-token leaks seen
#    in streaming tool-call paths across multiple backends. Non-streaming
#    responses go through the full parser output rather than incremental
#    chunk-by-chunk parsing. (The sanitizer above is still kept as a net.)
#
# If TOKENIZE_HOST above no longer points at a llama-server, adjust the
# compaction token counter accordingly (see the note there).
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
            print(f"Loaded {len(tools)} tools from cloakbrowser-mcp:")
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