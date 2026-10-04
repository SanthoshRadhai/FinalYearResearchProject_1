"""Builds the Phase-1 StateGraph: Safety -> Orchestrator -> {Recon, Vulnerability
Analysis} -> Evaluator -> back to Orchestrator -> END.

Matches Research-Paper resources/09-multi-agent-stategraph.drawio, restricted
to the Phase-1 subset called out in 07-...ARCHITECTURE.md §11. Extending to
Phase 2/3 (Attack Planning, Threat Intel, Log Triage, Detection & Mitigation,
Incident Response) means: write agents/<new>.py following recon.py/
vuln_analysis.py's shape, add one add_node call and one entry in
SPECIALIST_NODE_NAMES below, and one line in the conditional-edge map — the
graph topology already accounts for them via orchestrator.py's RoutingDecision
Literal.
"""

from langgraph.graph import StateGraph, END

import events
from state import GraphState
from agents.safety import safety_node
from agents.orchestrator import orchestrator_node, route_from_orchestrator
from agents.evaluator import evaluator_node, evaluator_accept_all_node, evaluator_all_evidence_node
from agents.recon import build_recon_node
from agents.vuln_analysis import build_vuln_analysis_node

# Specialists not yet built (Phase 2/3) — if the Orchestrator's structured
# output ever names one of these (it shouldn't, per its prompt, but small
# models drift), route to this instead of crashing the graph on a missing node.
NOT_YET_IMPLEMENTED = {
    "exploit_poc", "attack_planning", "threat_intel",
    "log_triage", "detection_mitigation", "incident_response",
}


def _not_implemented_node(state: GraphState) -> dict:
    msg = (f"orchestrator picked an unimplemented specialist ({state['next_agent']}) "
           f"— ending turn instead of crashing")
    print(f"[graph] {msg}. See 07-...ARCHITECTURE.md §11 phased build order.")
    entry = events.emit("graph", "not_implemented", msg)
    return {"next_agent": "end", "trace": [entry]}


def build_graph(browser_tools: list, evaluator_mode: str = "on"):
    builder = StateGraph(GraphState)

    builder.add_node("safety", safety_node)
    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("recon", build_recon_node(browser_tools))
    builder.add_node("vuln_analysis", build_vuln_analysis_node())
    # evaluator_mode: "on" normal, "off" accept-all baseline, "all" judge sees all tool results (bench_g4_onoff.py).
    evaluator_by_mode = {"on": evaluator_node, "off": evaluator_accept_all_node, "all": evaluator_all_evidence_node}
    builder.add_node("evaluator", evaluator_by_mode[evaluator_mode])
    builder.add_node("not_implemented", _not_implemented_node)

    builder.set_entry_point("safety")
    builder.add_edge("safety", "orchestrator")

    route_map = {name: "not_implemented" for name in NOT_YET_IMPLEMENTED}
    route_map.update({"recon": "recon", "vuln_analysis": "vuln_analysis", "end": END})
    builder.add_conditional_edges("orchestrator", route_from_orchestrator, route_map)

    builder.add_edge("recon", "evaluator")
    builder.add_edge("vuln_analysis", "evaluator")
    builder.add_edge("not_implemented", END)
    builder.add_edge("evaluator", "orchestrator")

    return builder.compile()
