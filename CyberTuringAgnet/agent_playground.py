"""Agent Playground tab logic -- lets each RedBlue agent be exercised on its
own, outside the full pipeline, for demoing/debugging a single node in
isolation. Every function here builds just enough GraphState by hand to
satisfy that one node's contract (see state.py's GraphState) and returns a
Markdown string summarizing what the node did.
"""

import json

from langchain_core.messages import HumanMessage

from browser_tools import get_browser_tools
from agents.safety import safety_node
from agents.orchestrator import orchestrator_node
from agents.evaluator import evaluator_node
from agents.recon import build_recon_node
from agents.vuln_analysis import build_vuln_analysis_node
from state import Finding, new_redblue_state

_recon_node = None
_vuln_node = None


async def _get_recon_node():
    global _recon_node
    if _recon_node is None:
        tools = await get_browser_tools()
        _recon_node = build_recon_node(tools)
    return _recon_node


def _get_vuln_node():
    global _vuln_node
    if _vuln_node is None:
        _vuln_node = build_vuln_analysis_node()
    return _vuln_node


def _parse_scope(target_scope_text: str) -> dict:
    if not target_scope_text or not target_scope_text.strip():
        return {}
    return json.loads(target_scope_text)


async def test_safety(objective: str, target_scope_text: str) -> str:
    try:
        target_scope = _parse_scope(target_scope_text)
    except json.JSONDecodeError as e:
        return f"**Invalid target_scope JSON:** {e}"
    state = new_redblue_state(objective, target_scope=target_scope)
    result = safety_node(state)
    if result["halted"]:
        return f"**HALTED**\n\n{result['halt_reason']}"
    return "**Cleared** — scope check passed, nothing in `DENY_KEYWORDS` matched."


async def test_recon(objective: str, target_scope_text: str) -> str:
    try:
        target_scope = _parse_scope(target_scope_text)
    except json.JSONDecodeError as e:
        return f"**Invalid target_scope JSON:** {e}"
    node = await _get_recon_node()
    state = new_redblue_state(objective, target_scope=target_scope)
    result = await node(state)
    finding = result["findings"][-1]
    return (
        f"**Claim:**\n\n{finding['claim']}\n\n"
        f"**Evidence excerpt** (last tool result, truncated):\n```\n{finding['evidence_excerpt'][:800]}\n```"
    )


async def test_vuln_analysis(objective: str, prior_findings_text: str) -> str:
    node = _get_vuln_node()
    state = new_redblue_state(objective)
    if prior_findings_text and prior_findings_text.strip():
        state["findings"] = [Finding(
            source_agent="manual", claim=prior_findings_text.strip(),
            evidence_ref="", evidence_excerpt="", confidence="unverified",
        )]
    result = await node(state)
    finding = result["findings"][-1]
    return (
        f"**Claim:**\n\n{finding['claim']}\n\n"
        f"**Evidence excerpt** (last tool result, truncated):\n```\n{finding['evidence_excerpt'][:800]}\n```"
    )


async def test_evaluator(claim: str, excerpt: str) -> str:
    if not claim.strip() or not excerpt.strip():
        return "Provide both a claim and an excerpt."
    fake_message = HumanMessage(content=excerpt, id="manual-evidence")
    finding = Finding(
        source_agent="manual", claim=claim, evidence_ref="manual-evidence",
        evidence_excerpt=excerpt, confidence="unverified",
    )
    state = new_redblue_state("manual evaluator test")
    state["messages"] = [fake_message]
    state["findings"] = [finding]
    result = await evaluator_node(state)
    verdict_finding = result["findings"][0]
    verdict = "✅ VERIFIED" if verdict_finding["confidence"] == "verified" else "❌ REJECTED"
    return f"**{verdict}**\n\n(step 1's substring check always passes here by construction — this tests step 2, the LLM judgment, in isolation)"


async def test_orchestrator(objective: str, verified_claims_text: str, last_agent: str, stall_count: float) -> str:
    verified = []
    for line in (verified_claims_text or "").splitlines():
        line = line.strip()
        if line:
            verified.append(Finding(
                source_agent="manual", claim=line,
                evidence_ref="", evidence_excerpt="", confidence="verified",
            ))
    state = new_redblue_state(objective)
    state["verified_findings"] = verified
    state["last_agent"] = last_agent.strip() or None
    state["stall_count"] = int(stall_count)
    result = await orchestrator_node(state)
    return (
        f"**Next agent:** `{result['next_agent']}`\n\n"
        f"**Stall count:** {result.get('stall_count', state['stall_count'])}"
    )
