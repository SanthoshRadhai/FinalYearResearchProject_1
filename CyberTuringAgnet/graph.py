"""Two graphs live here:

  * `build_chat_graph` -- single-node plain chat graph (Chat tab). All model
    parameters (temperature, max_tokens, top_p, system prompt) come from the
    per-call `config` instead of a module-level client, so the same compiled
    graph serves every session even though each one can run with different
    settings (see app.py's Settings panel).

  * `build_redblue_graph` -- the full Safety -> Orchestrator ->
    {Recon, Vulnerability Analysis} -> Evaluator -> back to Orchestrator ->
    END pipeline, ported unchanged from ../RedBlue-MultiAgent/graph.py (see
    that file's docstring and Research-Paper resources/
    09-multi-agent-stategraph.drawio for the topology).
"""

from langchain_core.messages import SystemMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.base import BaseCheckpointSaver

import events
from llm import make_llm, DEFAULT_SETTINGS
from state import ChatState, GraphState
from agents.safety import safety_node
from agents.orchestrator import orchestrator_node, route_from_orchestrator
from agents.evaluator import evaluator_node
from agents.recon import build_recon_node
from agents.vuln_analysis import build_vuln_analysis_node


async def chat_node(state: ChatState, config: RunnableConfig) -> dict:
    settings = {**DEFAULT_SETTINGS, **config.get("configurable", {})}

    llm = make_llm(
        temperature=settings["temperature"],
        max_tokens=settings["max_tokens"],
        top_p=settings["top_p"],
    )

    messages = list(state["messages"])
    if settings["system_prompt"].strip():
        messages = [SystemMessage(content=settings["system_prompt"])] + messages

    response = await llm.ainvoke(messages)
    return {"messages": [response]}


def build_chat_graph(checkpointer: BaseCheckpointSaver):
    graph = StateGraph(ChatState)
    graph.add_node("chat", chat_node)
    graph.add_edge(START, "chat")
    graph.add_edge("chat", END)
    return graph.compile(checkpointer=checkpointer)


# --- RedBlue multi-agent pipeline ---

NOT_YET_IMPLEMENTED = {
    "exploit_poc", "attack_planning", "threat_intel",
    "log_triage", "detection_mitigation", "incident_response",
}


def _not_implemented_node(state: GraphState) -> dict:
    msg = (f"orchestrator picked an unimplemented specialist ({state['next_agent']}) "
           f"— ending turn instead of crashing")
    print(f"[graph] {msg}.")
    entry = events.emit("graph", "not_implemented", msg)
    return {"next_agent": "end", "trace": [entry]}


def build_redblue_graph(browser_tools: list):
    builder = StateGraph(GraphState)

    builder.add_node("safety", safety_node)
    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("recon", build_recon_node(browser_tools))
    builder.add_node("vuln_analysis", build_vuln_analysis_node())
    builder.add_node("evaluator", evaluator_node)
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
