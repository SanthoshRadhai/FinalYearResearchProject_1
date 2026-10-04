"""RedBlue Investigate tab logic -- runs the full Safety -> Orchestrator ->
{Recon, Vulnerability Analysis} -> Evaluator -> ... -> END pipeline (ported
from ../RedBlue-MultiAgent) for one objective at a time, streaming every
agent's live "thinking" (the events.py bus) into the Gradio UI the same way
../RedBlue-MultiAgent/webui streamed it over a WebSocket.

Single-run-at-a-time by design -- same shared-cloakbrowser-mcp-subprocess
constraint as the original project (see browser_tools.py).
"""

import asyncio
import time

import events
from browser_tools import get_browser_tools
from graph import build_redblue_graph
from state import new_redblue_state

RECURSION_LIMIT = 30

_graph = None
_busy = False


async def get_redblue_graph():
    global _graph
    if _graph is None:
        tools = await get_browser_tools()
        _graph = build_redblue_graph(tools)
    return _graph


def _format_trace(entries: list[dict]) -> str:
    lines = []
    for e in entries:
        ts = time.strftime("%H:%M:%S", time.localtime(e.get("ts", time.time())))
        line = f"[{ts}] [{e['node']}] {e['event']}: {e['message']}"
        if e.get("reason"):
            line += f" (reason: {e['reason']})"
        lines.append(line)
    return "\n".join(lines)


def _format_findings(verified: list[dict], rejected: list[dict]) -> str:
    if not verified and not rejected:
        return "_No findings yet._"
    parts = []
    if verified:
        parts.append("### Verified")
        for f in verified:
            parts.append(f"- **[{f['source_agent']}]** {f['claim']}")
    if rejected:
        parts.append("### Rejected")
        for f in rejected:
            parts.append(f"- **[{f['source_agent']}]** {f['claim']}")
    return "\n".join(parts)


async def run_investigation(objective: str):
    """Async generator: yields (trace_text, findings_md, answer_md) tuples as
    the run progresses, for a Gradio streaming output binding."""
    global _busy

    if not objective or not objective.strip():
        yield "", "_No findings yet._", "_Enter an objective first._"
        return

    if _busy:
        yield "", "_No findings yet._", "**A run is already in progress** -- only one investigation runs at a time (shared browser subprocess)."
        return

    _busy = True
    trace_entries: list[dict] = []
    try:
        graph = await get_redblue_graph()
        events.start_run()
        state = new_redblue_state(objective, mode="red")
        result_holder = {}

        async def _run():
            try:
                result_holder["result"] = await graph.ainvoke(state, config={"recursion_limit": RECURSION_LIMIT})
                events.emit("graph", "run_complete", "run finished")
            except Exception as e:
                result_holder["error"] = str(e)
                events.emit("graph", "run_error", str(e))

        task = asyncio.create_task(_run())

        async for entry in events.subscribe():
            trace_entries.append(entry)
            yield _format_trace(trace_entries), "_Running..._", "_Running..._"

        await task

        if "error" in result_holder:
            yield _format_trace(trace_entries), "_No findings yet._", f"**Error:** {result_holder['error']}"
            return

        result = result_holder.get("result", {})
        verified = [
            {"source_agent": f["source_agent"], "claim": f["claim"]}
            for f in result.get("verified_findings", [])
        ]
        rejected = [
            {"source_agent": f["source_agent"], "claim": f["claim"]}
            for f in result.get("findings", []) if f["confidence"] == "rejected"
        ]
        findings_md = _format_findings(verified, rejected)

        if result.get("halted"):
            answer_md = f"**Halted:** {result.get('halt_reason')}"
        else:
            answer = result["messages"][-1].content if result.get("messages") else "(no answer produced)"
            if not verified:
                answer_md = (
                    "> No verified findings support this answer (see Findings panel — "
                    "the Evaluator rejected every claim). Treat the text below with caution.\n\n"
                    + answer
                )
            else:
                answer_md = answer

        yield _format_trace(trace_entries), findings_md, answer_md
    finally:
        _busy = False
