"""Recon / OSINT Web-Search Agent — the one node in this graph that touches a
browser. Ports the working pattern from Langchain/6_langchain_cloakbrowser_lama_cpp.py
(cloakbrowser-mcp / @playwright/mcp tool surface) rather than reinventing it.

Per Research-Paper resources/07-...ARCHITECTURE.md §5.1 and
08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md §1.1: this is the ONLY MCP subprocess in
the whole system. main.py is responsible for spawning it once and reusing the
same session across every graph turn — never spawn a second one per call.
"""

from langgraph.prebuilt import create_react_agent

import events
from llm import TOOL_AGENT_LLM
from reliability import make_sanitize_hook
from tools import lookup_cve, search_knowledge_base
from state import GraphState
from .common import run_tool_agent

REF_REQUIRING_TOOLS = frozenset({
    "browser_click", "browser_hover", "browser_type",
    "browser_select_option", "browser_drag", "browser_fill_form",
})

SYSTEM_PROMPT = (
    "You are the Recon/OSINT agent in a red-team pipeline. You have a "
    "Playwright-based browser (cloakbrowser-mcp), a direct NVD CVE lookup "
    "tool, and a local offline knowledge base covering MITRE ATT&CK, CWE, "
    "CAPEC, D3FEND, CISA KEV, OWASP Cheat Sheets, and this project's own "
    "reference papers/results.\n\n"
    "WORKFLOW:\n"
    "1. If the objective names a specific CVE ID, call lookup_cve first — it "
    "is faster and more reliable than browsing NVD's website.\n"
    "2. ALSO check search_knowledge_base for anything that might already be "
    "covered locally — a known ATT&CK technique/campaign, a CWE weakness "
    "class, a CAPEC attack pattern, a D3FEND mitigation, or whether a CVE is "
    "in the CISA KEV (actively-exploited) catalog. It's instant and free — "
    "check it before reaching for the browser, not as a last resort.\n"
    "3. Only use browser_navigate for things NOT covered by the tools above "
    "or that require live/current information the local knowledge base "
    "can't have. Use browser_snapshot to get element refs before any "
    "click/type action.\n"
    "4. Never invent a `ref` value or claim a page said something a tool "
    "result in THIS conversation doesn't show.\n"
    "5. Only cite sources you actually navigated to, queried via lookup_cve, "
    "or retrieved via search_knowledge_base — never a search-result snippet "
    "you didn't open.\n\n"
    "End with a concise factual summary of what you found, citing your "
    "source(s) explicitly."
)


def build_recon_node(browser_tools: list):
    tools = [lookup_cve, search_knowledge_base, *browser_tools]
    agent = create_react_agent(
        TOOL_AGENT_LLM, tools,
        post_model_hook=make_sanitize_hook(ref_requiring_tools=REF_REQUIRING_TOOLS, node_name="recon"),
    )

    async def recon_node(state: GraphState) -> dict:
        start_entry = events.emit("recon", "node_start", "starting")
        finding, run_messages = await run_tool_agent(
            agent,
            system_prompt=SYSTEM_PROMPT,
            objective=state["objective"],
            target_scope=state["target_scope"],
            source_agent="recon",
        )
        end_entry = events.emit("recon", "node_end", finding["claim"][:200])
        return {
            "messages": run_messages,
            "findings": [*state["findings"], finding],
            "last_agent": "recon",
            "trace": [start_entry, end_entry],
        }

    return recon_node
