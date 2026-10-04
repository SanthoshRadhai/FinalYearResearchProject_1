"""Shared helper for every tool-using specialist node (Recon, Vulnerability
Analysis, and future ones): run its inner ReAct sub-agent to completion for
the current objective, then package the result as a Finding.

Design simplification, stated explicitly (see Research-Paper resources/
07-...ARCHITECTURE.md §3's Finding schema): rather than asking the small model
to self-report a structured evidence_ref/evidence_excerpt pair (risky given
the malformed-output history in this project), evidence_excerpt is always a
*direct copy* of the actual last tool result's text. That makes the
Evaluator's step-1 substring check trivially satisfiable by construction, so
the check that actually carries weight is step 2 (does the claim follow from
that excerpt) — a deliberate, documented trade-off for the time budget, not an
oversight. Revisit if the paper's RQ3 numbers need the stronger self-reported
version.
"""

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage

import events
from state import Finding

MAX_EXCERPT_CHARS = 800


def build_task_text(objective: str, target_scope: dict) -> str:
    scope_line = f"\nTarget scope: {target_scope}" if target_scope else ""
    return f"{objective}{scope_line}"


async def run_tool_agent(agent, *, system_prompt: str, objective: str, target_scope: dict,
                          source_agent: str) -> tuple[Finding, list]:
    """Runs `agent` (a compiled create_react_agent) on the objective and returns
    (finding, messages_from_this_run).

    Streams the inner ReAct loop (`astream(..., stream_mode="values")`)
    instead of a single blocking `ainvoke()` purely so tool calls and their
    results can be pushed to events.py AS THEY HAPPEN, not batched together
    at the end -- this is what makes the web UI's live trace feed show real
    "thinking" mid-run rather than a wall of events all at once when the
    node finishes. The final yielded value is exactly what `ainvoke` would
    have returned, so this is a behavior-preserving change for every
    existing caller (bench scripts, main.py) that doesn't care about live
    events at all.
    """
    history = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=build_task_text(objective, target_scope)),
    ]

    seen_ids = set()
    final_state = None
    async for step_state in agent.astream({"messages": history}, stream_mode="values"):
        final_state = step_state
        for m in step_state["messages"]:
            mid = getattr(m, "id", None)
            if mid is None or mid in seen_ids:
                continue
            seen_ids.add(mid)
            if isinstance(m, AIMessage) and m.tool_calls:
                for call in m.tool_calls:
                    events.emit(source_agent, "tool_call", f"{call['name']}({call.get('args', {})})")
            elif isinstance(m, ToolMessage):
                preview = str(m.content)[:200]
                events.emit(source_agent, "tool_result", preview, tool_name=getattr(m, "name", ""))

    messages = final_state["messages"]
    tool_messages = [m for m in messages if isinstance(m, ToolMessage)]
    final = messages[-1]

    if tool_messages:
        last_tool = tool_messages[-1]
        excerpt = str(last_tool.content)[:MAX_EXCERPT_CHARS]
        evidence_ref = last_tool.id or ""
    else:
        excerpt = ""
        evidence_ref = ""

    finding = Finding(
        source_agent=source_agent,
        claim=str(final.content),
        evidence_ref=evidence_ref,
        evidence_excerpt=excerpt,
        confidence="unverified",
    )
    return finding, messages
