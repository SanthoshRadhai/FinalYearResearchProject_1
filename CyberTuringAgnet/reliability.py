"""Reliability harness shared by every tool-using specialist's inner ReAct loop.
Ported unchanged from ../RedBlue-MultiAgent/reliability.py -- see that file's
docstring (and Research-Paper resources/06-GPT-OSS-LLAMACPP-TOOLCALLING-FINDINGS.md)
for the root-cause history behind these fixes.
"""

import re

from langchain_core.messages import AIMessage, ToolMessage

import events

HARMONY_TOKEN_RE = re.compile(r"<\|[a-z_]+\|>")

REQUIRED_ISH_KEYS = ("ref", "url", "element", "selector", "text", "cve_id", "technique_id", "vector")


def _looks_degenerate(value):
    if not isinstance(value, str) or len(value) <= 40:
        return False
    prefix = value[:4]
    return bool(prefix) and value.count(prefix) > 5


def _looks_malformed(call):
    args = call.get("args", {}) or {}
    for key in REQUIRED_ISH_KEYS:
        if args.get(key, "__unset__") == "":
            return True
    for v in args.values():
        if _looks_degenerate(v):
            return True
    return False


def _strip_harmony_tokens(text):
    if not isinstance(text, str):
        return text
    return HARMONY_TOKEN_RE.sub("", text)


def _ref_looks_bad(value):
    if not isinstance(value, str) or value == "":
        return True
    return _looks_degenerate(value)


def _page_refs_available(messages):
    for m in messages:
        if isinstance(m, ToolMessage) and "ref=" in str(m.content):
            return True
    return False


def make_sanitize_hook(*, ref_requiring_tools: frozenset = frozenset(), malformed_call_limit: int = 2,
                        node_name: str = "specialist"):
    """Build a post_model_hook for create_react_agent. See the ported docstring
    in ../RedBlue-MultiAgent/reliability.py for full parameter documentation."""
    streak = {"count": 0}

    def _maybe_redirect_to_snapshot(last, messages):
        if not ref_requiring_tools or not last.tool_calls:
            return None
        first_call = last.tool_calls[0]
        if first_call.get("name") not in ref_requiring_tools:
            return None
        args = first_call.get("args", {}) or {}
        if not _ref_looks_bad(args.get("ref", "")):
            return None
        if _page_refs_available(messages):
            return None
        msg = f"'{first_call.get('name')}' called with no valid ref — redirecting to browser_snapshot"
        print(f"[auto-recover] {msg}.")
        events.emit(node_name, "auto_recover", msg)
        return AIMessage(
            content="",
            tool_calls=[{"name": "browser_snapshot", "args": {}, "id": first_call["id"], "type": "tool_call"}],
            id=last.id,
        )

    async def sanitize_ai_message(state):
        messages = state["messages"]
        last = messages[-1]
        if not isinstance(last, AIMessage):
            return {}

        redirected = _maybe_redirect_to_snapshot(last, messages)
        if redirected is not None:
            return {"messages": [redirected]}

        if last.tool_calls and any(_looks_malformed(c) for c in last.tool_calls):
            streak["count"] += 1
            if streak["count"] >= malformed_call_limit:
                msg = f"{streak['count']} consecutive malformed tool calls — aborting this turn"
                print(f"[circuit-breaker] {msg}.")
                events.emit(node_name, "circuit_breaker", msg)
                streak["count"] = 0
                return {"messages": [AIMessage(
                    content=("I ran into repeated malformed tool calls and stopped rather than "
                              "continuing to retry. This likely needs a rephrased request."),
                    id=last.id,
                )]}
        else:
            streak["count"] = 0

        new_content = _strip_harmony_tokens(last.content)
        new_tool_calls = [
            {**c, "name": _strip_harmony_tokens(c["name"])} for c in (last.tool_calls or [])
        ]
        if new_content != last.content or any(
            c["name"] != orig["name"] for c, orig in zip(new_tool_calls, last.tool_calls or [])
        ):
            print("[sanitized] removed leaked Harmony token(s) from assistant message")
            events.emit(node_name, "sanitized", "removed leaked Harmony token(s) from assistant message")
            return {"messages": [AIMessage(content=new_content, tool_calls=new_tool_calls, id=last.id)]}

        return {}

    return sanitize_ai_message
