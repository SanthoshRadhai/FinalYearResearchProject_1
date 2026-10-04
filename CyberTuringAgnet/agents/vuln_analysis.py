"""Vulnerability Analysis Agent — no browser, no MCP subprocess at all.

Per Research-Paper resources/07-...ARCHITECTURE.md §5.2: reads the Recon
agent's verified findings, extracts/parses the published CVSS vector
deterministically (never re-scores from prose itself), and can cross-reference
ATT&CK technique names via the local offline KB.
"""

from langgraph.prebuilt import create_react_agent

import events
from llm import TOOL_AGENT_LLM
from reliability import make_sanitize_hook
from tools import parse_cvss_vector, lookup_attack_technique, search_attack_kb
from state import GraphState
from .common import run_tool_agent

SYSTEM_PROMPT = (
    "You are the Vulnerability Analysis agent in a red-team pipeline. You do "
    "NOT have browser access. You work only from findings already gathered by "
    "the Recon agent (given to you below as prior context) plus your tools.\n\n"
    "RULES:\n"
    "1. Never estimate or invent a CVSS score yourself. If a CVSS vector "
    "string is available (e.g. 'CVSS:3.1/AV:N/...'), call parse_cvss_vector "
    "on it verbatim to get the real base score and severity.\n"
    "2. If no CVSS vector is available, say so explicitly rather than "
    "guessing a severity.\n"
    "3. Use search_attack_kb / lookup_attack_technique only if a specific "
    "attack technique needs cross-referencing.\n\n"
    "End with a short priority assessment: is this worth escalating to "
    "exploit/attack-planning, and why, grounded in the parsed CVSS data."
)


def build_vuln_analysis_node():
    tools = [parse_cvss_vector, lookup_attack_technique, search_attack_kb]
    agent = create_react_agent(
        TOOL_AGENT_LLM, tools,
        post_model_hook=make_sanitize_hook(node_name="vuln_analysis"),  # no ref-redirect needed, no browser
    )

    async def vuln_analysis_node(state: GraphState) -> dict:
        start_entry = events.emit("vuln_analysis", "node_start", "starting")
        prior = "\n\n".join(
            f"[{f['source_agent']}] {f['claim']}" for f in state["findings"]
        )
        objective_with_context = (
            f"{state['objective']}\n\nPrior findings so far:\n{prior}"
            if prior else state["objective"]
        )
        finding, run_messages = await run_tool_agent(
            agent,
            system_prompt=SYSTEM_PROMPT,
            objective=objective_with_context,
            target_scope=state["target_scope"],
            source_agent="vuln_analysis",
        )
        end_entry = events.emit("vuln_analysis", "node_end", finding["claim"][:200])
        return {
            "messages": run_messages,
            "findings": [*state["findings"], finding],
            "last_agent": "vuln_analysis",
            "trace": [start_entry, end_entry],
        }

    return vuln_analysis_node
