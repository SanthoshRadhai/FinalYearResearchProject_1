"""
Interactive LangChain <-> MCP client for the stealth-browser-mcp server: a
general-purpose multi-site web research agent (not security/CVE-specific).

Given a user query, the agent is instructed to search using advanced Google
dorking operators, visit multiple distinct sites (up to --max-sites), and
finish with a synthesized conclusion. The script itself (not just the prompt)
tracks every site actually navigated to and every search query actually
issued, and prints a script-generated "[Sites visited]" / "[Search queries
used]" block after every answer — the same "don't just trust the model to
self-report" philosophy used for the malformed-tool-call and premature-call
safeguards below, applied to citation accuracy instead of tool-call safety.

Shares its resilience infrastructure (Harmony-token sanitization, malformed-
tool-call circuit breaker, premature-tool-call auto-recovery, context-window
compaction) with 4_langchain_stealth_llamacpp_CVE_Agent.py, since it targets
the same model/backend (gpt-oss-20b via llama.cpp, --jinja, port 5500).

Install:
    pip install langchain langchain-mcp-adapters langgraph langchain-openai mcp httpx

Run:
    python 5_langchain_stealth_browser_agent.py
    python 5_langchain_stealth_browser_agent.py --max-sites 8
"""

import argparse
import asyncio
import functools
import os
import re
import uuid
from urllib.parse import urlparse, parse_qs

import httpx

# Force every print() in this module to flush immediately. When stdout is
# redirected to a file/pipe (not a TTY) Python fully block-buffers it, which
# can hide real diagnostic output (our [auto-recover]/[circuit-breaker]/
# [compact]/[tool call] lines) for minutes at a time — indistinguishable from
# an actual hang when watching a redirected log during a long-running,
# multi-site browsing turn. Unbuffered output costs nothing here.
print = functools.partial(print, flush=True)

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
DEBUG_HARMONY = os.environ.get("DEBUG_HARMONY", "0") == "1"

# Matches leaked gpt-oss/Harmony control tokens like <|channel|>, <|end|>,
# <|start|>, <|constrain|>, <|call|>, <|message|>, etc.
HARMONY_TOKEN_RE = re.compile(r"<\|[a-z_]+\|>")

# Tracks consecutive malformed tool calls (empty required args, or garbage
# repeated-character args) across a single agent turn.
_malformed_call_streak = {"count": 0}
MALFORMED_CALL_LIMIT = 2  # abort after this many consecutive bad calls in a row


def _is_valid_uuid(value):
    if not isinstance(value, str):
        return False
    try:
        uuid.UUID(value.strip())
        return True
    except (ValueError, AttributeError):
        return False


def _looks_malformed(call):
    """Every real instance_id in this system is a UUID minted by
    spawn_browser's own output, so validating against that directly is far
    more robust than trying to pattern-match every possible shape of leaked
    Harmony-token garbage (empirically, garbled values don't reliably match
    any single 'repeats' heuristic — some are period-aligned, most aren't)."""
    args = call.get("args", {})
    if "instance_id" in args and not _is_valid_uuid(args.get("instance_id")):
        return True
    # Still worth catching gross repeated-character garbage in any other
    # long string argument (e.g. a corrupted URL or script body).
    for k, v in args.items():
        if k == "instance_id":
            continue
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
def _instance_id_looks_bad(value):
    return not _is_valid_uuid(value)


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
    call instead of letting it dispatch a guaranteed-failing call."""
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
        return None

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


# --- Multi-site tracking and cap enforcement --------------------------------
# Rather than trust the model to correctly self-report every source it used
# (it may forget one, or cite a site it never actually fetched), the script
# derives the real list from the actual `navigate` tool calls in history, and
# separately enforces a hard cap on distinct non-search-engine sites so a
# search task can't run away visiting dozens of pages.
SEARCH_ENGINE_HOSTS = ("google.", "bing.", "duckduckgo.")


def _is_search_engine_url(url):
    netloc = urlparse(url).netloc.lower()
    return any(engine in netloc for engine in SEARCH_ENGINE_HOSTS)


def _extract_search_query(url):
    qs = parse_qs(urlparse(url).query)
    for key in ("q", "query", "p"):
        if key in qs and qs[key]:
            return qs[key][0]
    return None


def _extract_navigate_urls(messages):
    urls = []
    for m in messages:
        if isinstance(m, AIMessage) and m.tool_calls:
            for call in m.tool_calls:
                if call.get("name") == "navigate":
                    url = call.get("args", {}).get("url")
                    if url:
                        urls.append(url)
    return urls


def _distinct_visited_sites(messages):
    """Distinct non-search-engine URLs actually navigated to, in first-visit
    order."""
    seen = []
    for url in _extract_navigate_urls(messages):
        if _is_search_engine_url(url):
            continue
        if url not in seen:
            seen.append(url)
    return seen


def _search_queries_used(messages):
    seen = []
    for url in _extract_navigate_urls(messages):
        if _is_search_engine_url(url):
            q = _extract_search_query(url)
            if q and q not in seen:
                seen.append(q)
    return seen


def _maybe_block_over_cap(last, messages, max_sites):
    """If the model is about to navigate to a brand-new (not yet visited)
    non-search-engine site after already reaching max_sites distinct sites,
    block the call and nudge it to conclude with what it already has."""
    if not last.tool_calls:
        return None
    call = last.tool_calls[0]
    if call.get("name") != "navigate":
        return None
    url = call.get("args", {}).get("url")
    if not url or _is_search_engine_url(url):
        return None  # searching itself never counts against the cap

    already_visited = _distinct_visited_sites(messages)
    if url in already_visited:
        return None  # revisiting a known site is fine
    if len(already_visited) < max_sites:
        return None

    print(f"[site-cap] already visited {len(already_visited)} distinct site(s) "
          f"(max {max_sites}) — blocking a new site visit and asking the "
          f"agent to conclude with what it has.")
    return AIMessage(
        content=(
            f"I've already visited {len(already_visited)} different sites for "
            f"this query, which is the configured limit for this session. "
            f"I'll give my conclusion now based on what I've gathered so far "
            f"rather than visiting further sites."
        ),
        id=last.id,
    )


# --- Context-window compaction ---------------------------------------------
LLAMA_SERVER_HOST = "http://localhost:5500"
MAX_CONTEXT_TOKENS = 131072
COMPACT_TOKEN_THRESHOLD = int(MAX_CONTEXT_TOKENS * 0.75)
KEEP_RECENT_MESSAGES = 10


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
    start = max(0, len(messages) - keep_last_n)
    while start > 0 and isinstance(messages[start], ToolMessage):
        start -= 1
    return start


async def _compact_if_needed(messages):
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
        return None

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


def make_sanitize_hook(max_sites):
    """Returns a post_model_hook closed over the configured max_sites cap."""

    async def sanitize_ai_message(state):
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
            kwargs_preview = repr(last.additional_kwargs)
            if len(kwargs_preview) > 1000:
                kwargs_preview = kwargs_preview[:1000] + "...[truncated]"
            print(f"[debug] raw AIMessage.additional_kwargs: {kwargs_preview}")
            print(f"[debug] response_metadata finish_reason: "
                  f"{last.response_metadata.get('finish_reason', '<not present>')}\n")

        # --- Auto-recover from a premature tool call ---
        redirected = _maybe_redirect_to_spawn_browser(last, messages)
        if redirected is not None:
            return {"messages": [redirected]}

        # --- Enforce the multi-site visit cap ---
        capped = _maybe_block_over_cap(last, messages, max_sites)
        if capped is not None:
            return {"messages": [capped]}

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
            updates.append(AIMessage(content=new_content, tool_calls=new_tool_calls, id=last.id))

        compaction_updates = await _compact_if_needed(messages)
        if compaction_updates:
            updates.extend(compaction_updates)

        if not updates:
            return {}
        return {"messages": updates}

    return sanitize_ai_message


SYSTEM_PROMPT_TEMPLATE = (
    "You are a web research agent with access to browser automation tools via "
    "MCP (navigate, get_page_content, query_elements, execute_script, etc.). "
    "The browser you control is undetectable by anti-bot systems, so if a "
    "site appears blocked or shows a CAPTCHA/challenge page, retry the "
    "navigation or wait for the page to finish rendering before giving up on "
    "that source — do not fabricate an answer instead.\n\n"
    "GOAL: given the user's question, search the web and gather information "
    "from MULTIPLE distinct sites (up to {max_sites} for this session) before "
    "answering. Never answer from your own memory alone for anything that "
    "could be time-sensitive, niche, or that you are not fully certain of — "
    "use the tools to check.\n\n"
    "HOW TO SEARCH: navigate to Google search URLs "
    "(https://www.google.com/search?q=<query>) and use advanced Google "
    "dorking operators to get sharper, more targeted results instead of one "
    "generic query. Use as many of these as are relevant to the question, "
    "and run at least 2-3 differently-dorked searches, not just one plain "
    "query:\n"
    '  - "exact phrase"        force exact phrase matching\n'
    "  - site:example.com      restrict results to one domain\n"
    "  - -site:example.com     exclude a domain from results\n"
    "  - filetype:pdf          find a specific file type (pdf, doc, csv, ...)\n"
    "  - intitle:word          require a word in the page title\n"
    "  - inurl:word            require a word in the URL\n"
    "  - termA OR termB        match either term\n"
    "  - related:example.com   find sites similar to a known good source\n"
    "  - before:2026-01-01 / after:2025-01-01   restrict by date, useful for "
    "\"latest\"/\"recent\" questions\n\n"
    "After running a search, open several of the actual result links (not "
    "just the Google results page itself) with navigate + get_page_content "
    "to read their real content. Visit sites that look independent of each "
    "other, not several near-duplicates of the same source, so you can "
    "actually cross-check facts rather than just re-reading one source "
    "multiple times.\n\n"
    "WHEN YOU HAVE ENOUGH INFORMATION: write a final answer with this "
    "structure:\n"
    "1. A direct answer to the user's question.\n"
    "2. A short synthesis noting where sources agreed, and explicitly "
    "flagging anywhere they disagreed or you were only able to confirm "
    "something from a single source.\n"
    "3. Do not fabricate a citation for a site you did not actually "
    "navigate to in this conversation — only reference sites you actually "
    "opened with a tool call.\n\n"
    "(Note: this script also independently tracks and prints every site you "
    "actually navigated to after your answer, so your own citations will be "
    "cross-checked against that regardless.)"
)


# --- Point this at your MCP server's entrypoint ---
SERVER_PARAMS = StdioServerParameters(
    command="/home/johndoe/miniconda3/envs/hexstrike/bin/python",
    args=["server.py"],
    cwd="/mnt/s/FinalYear-Project/stealth-browser-mcp/src",
)

# --- Point this at your local OpenAI-compatible endpoint ---
# llama.cpp (llama-server) on port 5500, launched with --jinja so it applies
# gpt-oss's real Harmony chat template (tool-call support requires this flag
# plus a GGUF with Harmony-compatible chat-template metadata baked in).
# temperature=1.0 / top_p=1.0 match gpt-oss's own recommended sampling
# settings; the resilience hooks above are what make temp=1.0's occasional
# instability (malformed args, premature tool calls) safe to run with.
llm = ChatOpenAI(
    base_url="http://localhost:5500/v1",
    api_key="EMPTY",
    model="/home/vishnudharanb.23it/Santhosh/gpt-oss-20b/gpt-oss-20b-F16.gguf",
    temperature=1.0,
    top_p=1.0,
    max_tokens=16000,
    streaming=False,
)


async def main(max_sites):
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            print(f"Loaded {len(tools)} tools from MCP server:")
            for t in tools:
                print(f"  - {t.name}")
            print()
            print(f"Max distinct sites per query: {max_sites}\n")

            system_prompt = SystemMessage(content=SYSTEM_PROMPT_TEMPLATE.format(max_sites=max_sites))
            agent = create_react_agent(llm, tools, post_model_hook=make_sanitize_hook(max_sites))

            history = [system_prompt]
            print("Interactive session started. Type 'exit' or 'quit' to stop.\n")

            while True:
                user_input = input("You: ").strip()
                if user_input.lower() in ("exit", "quit"):
                    break
                if not user_input:
                    continue

                history.append(HumanMessage(content=user_input))
                prev_len = len(history)

                # A request-level failure here (llama-server's own tool-call
                # parser hard-failing with a 500 "does not match the expected
                # peg-native format" error) happens *before* post_model_hook
                # ever sees a message — it's a raw HTTP/parse failure, not a
                # malformed-but-parseable tool call, so none of the hooks
                # above can catch it. It's pure generation-level randomness
                # (gpt-oss/Harmony occasionally degrading badly enough within
                # one generation that llama.cpp can't extract any tool call
                # structure at all), so a plain retry of the same turn is a
                # reasonable, low-cost mitigation.
                RETRY_LIMIT = 2
                result = None
                for attempt in range(1, RETRY_LIMIT + 1):
                    try:
                        result = await agent.ainvoke({"messages": history})
                        break
                    except Exception as e:
                        if attempt < RETRY_LIMIT:
                            print(f"[error] {e}\n[retry] request-level failure "
                                  f"(attempt {attempt}/{RETRY_LIMIT}) — retrying "
                                  f"the same turn once before giving up.")
                        else:
                            print(f"[error] {e}\n[retry] gave up after {RETRY_LIMIT} attempts.\n")

                if result is None:
                    continue

                messages = result["messages"]
                history = messages

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

                last_ai = messages[-1]
                print(f"\nAgent: {last_ai.content}\n")

                # --- Script-generated (not model-self-reported) source list ---
                turn_messages = messages[prev_len:]
                queries = _search_queries_used(turn_messages)
                sites = _distinct_visited_sites(turn_messages)
                if queries:
                    print("[Search queries used]")
                    for q in queries:
                        print(f"  - {q}")
                if sites:
                    print("[Sites visited (references)]")
                    for s in sites:
                        print(f"  - {s}")
                print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-sites", type=int, default=5,
        help="Maximum number of distinct non-search-engine sites to visit per query (default: 5)",
    )
    args = parser.parse_args()
    asyncio.run(main(args.max_sites))
