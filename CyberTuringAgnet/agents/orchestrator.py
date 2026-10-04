"""Orchestrator / Coordinator Agent — pure router, no tools. See
Research-Paper resources/07-...ARCHITECTURE.md §4.

Phase-1 roster (see 07-...ARCHITECTURE.md §11 phased build order): only
"recon", "vuln_analysis", and "end" are wired into graph.py so far. The
Literal below already lists the full Phase-2/3 roster so extending the graph
later is a matter of adding nodes + edges, not renegotiating this contract.
"""

from typing import Literal

from pydantic import BaseModel, Field

from langchain_core.messages import SystemMessage, HumanMessage

import events
from llm import JUDGMENT_LLM
from state import GraphState

STALL_LIMIT = 3  # abort if the same specialist is picked this many times with no new verified finding


class RoutingDecision(BaseModel):
    next_agent: Literal[
        "recon", "vuln_analysis", "exploit_poc", "attack_planning",
        "threat_intel", "log_triage", "detection_mitigation", "incident_response",
        "end",
    ] = Field(description="Which specialist should run next, or 'end' if the objective is answerable now.")
    reason: str = Field(description="One sentence justifying the choice.")


_router = JUDGMENT_LLM.with_structured_output(RoutingDecision)

ROUTING_PROMPT = (
    "You are the Orchestrator of a red/blue-team multi-agent pentesting-research "
    "pipeline. Given the objective and the VERIFIED findings gathered so far, "
    "decide which specialist should run next, or 'end' if the objective is "
    "already answerable from verified findings alone.\n\n"
    "Currently implemented specialists (Phase 1): 'recon' (OSINT/CVE lookup, "
    "has browser + NVD access) and 'vuln_analysis' (CVSS/ATT&CK analysis, no "
    "browser). Route to 'recon' first for anything requiring new information; "
    "route to 'vuln_analysis' once recon has produced at least one verified "
    "finding with a CVSS vector to parse. Route to 'end' once you have enough "
    "verified findings to answer the objective, or if no forward progress is "
    "being made.\n\n"
    "Never claim something is answered without at least one verified finding "
    "supporting it."
)


async def orchestrator_node(state: GraphState) -> dict:
    if state["halted"]:
        entry = events.emit("orchestrator", "route", "-> end (halted by Safety)")
        return {"next_agent": "end", "trace": [entry]}

    verified_text = "\n".join(
        f"- [{f['source_agent']}] {f['claim']}" for f in state["verified_findings"]
    ) or "(none yet)"

    try:
        decision = await _router.ainvoke([
            SystemMessage(content=ROUTING_PROMPT),
            HumanMessage(content=(
                f"Objective: {state['objective']}\n"
                f"Target scope: {state['target_scope']}\n\n"
                f"Verified findings so far:\n{verified_text}\n\n"
                f"Last agent run: {state['last_agent']}\n"
                f"Consecutive stalls (same agent, no new verified finding): {state['stall_count']}"
            )),
        ])
    except Exception as e:
        # Same resilience as the Evaluator's judgment call: a truncated/
        # unparsable structured-output response must not crash the whole run.
        # Fail safe to "end" rather than silently repeating the same agent.
        msg = f"routing call failed ({e}) -- forcing end"
        print(f"[orchestrator] {msg}")
        entry = events.emit("orchestrator", "route", "-> end (routing call failed)", reason=str(e)[:200])
        return {"next_agent": "end", "trace": [entry]}

    next_agent = decision.next_agent

    # Progress-aware stall check: `verified_count_at_last_dispatch` is the
    # verified-findings count as of the PREVIOUS time the Orchestrator ran
    # (i.e. right before whatever specialist just executed). Comparing it to
    # the CURRENT count tells us whether that specialist's run actually
    # produced new verified evidence, not just whether it's the same name as
    # last time. A repeated pick that keeps producing new verified findings
    # (e.g. recon called once per CVE in a multi-CVE objective) must NOT be
    # penalized the same as a repeated pick that produces nothing new.
    current_verified_count = len(state["verified_findings"])
    made_progress = current_verified_count > state["verified_count_at_last_dispatch"]

    stall_count = state["stall_count"]
    if next_agent == state["last_agent"] and not made_progress:
        stall_count += 1
    else:
        stall_count = 0

    trace_entries = []
    if stall_count >= STALL_LIMIT:
        msg = f"stall limit reached ({stall_count}) — forcing end"
        print(f"[orchestrator] {msg}")
        trace_entries.append(events.emit("orchestrator", "stall_limit", msg))
        next_agent = "end"

    print(f"[orchestrator] -> {next_agent} ({decision.reason})")
    trace_entries.append(events.emit("orchestrator", "route", f"-> {next_agent}", reason=decision.reason))
    return {
        "next_agent": next_agent,
        "stall_count": stall_count,
        "verified_count_at_last_dispatch": current_verified_count,
        "trace": trace_entries,
    }


def route_from_orchestrator(state: GraphState) -> str:
    return state["next_agent"] or "end"
