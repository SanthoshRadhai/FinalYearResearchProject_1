"""Evaluator / Judge Agent — the mechanism that makes RQ3 (evidence-grounding)
real. See Research-Paper resources/07-...ARCHITECTURE.md §7.1.

Two-tier check, run for every `unverified` Finding in state["findings"]:
  1. Deterministic: is evidence_excerpt a literal substring of the real
     message (by id) referenced by evidence_ref? No LLM call — pure string
     matching. Fails => confidence "rejected" immediately.
  2. LLM judgment (only for excerpts that pass step 1): does the claim
     actually follow from the excerpt? This is the only place an LLM is asked
     to judge rather than retrieve.

Never edits claim/evidence_excerpt — only sets confidence. That is what makes
this node incapable of introducing a new hallucination into the record.
"""

from pydantic import BaseModel, Field

from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage

import events
from llm import JUDGMENT_LLM
from state import GraphState


class JudgmentVerdict(BaseModel):
    claim_follows_from_excerpt: bool = Field(
        description="True only if the claim is a fair, non-exaggerated reading of the excerpt."
    )
    reason: str = Field(description="One sentence explaining the verdict.")


_judge = JUDGMENT_LLM.with_structured_output(JudgmentVerdict)


def _message_text(msg: BaseMessage) -> str:
    if isinstance(msg.content, str):
        return msg.content
    return str(msg.content)


def _find_message_by_id(messages: list[BaseMessage], message_id: str):
    for m in messages:
        if getattr(m, "id", None) == message_id:
            return m
    return None


async def _evaluate(state: GraphState, all_evidence: bool) -> dict:
    messages = state["messages"]
    findings = list(state["findings"])
    verified = list(state["verified_findings"])
    trace_entries = []

    for i, finding in enumerate(findings):
        if finding["confidence"] != "unverified":
            continue

        # --- Step 1: deterministic substring check ---
        source_msg = _find_message_by_id(messages, finding["evidence_ref"])
        if source_msg is None or not finding["evidence_excerpt"]:
            findings[i] = {**finding, "confidence": "rejected"}
            msg = f"REJECTED ({finding['source_agent']}): evidence_ref did not resolve to a real message"
            print(f"[evaluator] {msg}")
            trace_entries.append(events.emit("evaluator", "rejected", msg, source_agent=finding["source_agent"]))
            continue
        if finding["evidence_excerpt"] not in _message_text(source_msg):
            findings[i] = {**finding, "confidence": "rejected"}
            msg = f"REJECTED ({finding['source_agent']}): evidence_excerpt is not a substring of the referenced message"
            print(f"[evaluator] {msg}")
            trace_entries.append(events.emit("evaluator", "rejected", msg, source_agent=finding["source_agent"]))
            continue

        # --- Step 2: LLM judgment (only reached if step 1 passed) ---
        try:
            verdict = await _judge.ainvoke([
                SystemMessage(content=(
                    "You are a strict fact-checker. You will be given a CLAIM and an "
                    "EXCERPT of real tool output. Decide only whether the claim is a "
                    "fair, non-exaggerated reading of the excerpt — not whether it is "
                    "true in general."
                )),
                HumanMessage(content=f"CLAIM: {finding['claim']}\n\nEXCERPT:\n"
                                     f"{_all_tool_evidence(messages, finding['evidence_ref']) if all_evidence else finding['evidence_excerpt']}"),
            ])
        except Exception as e:
            print(f"[evaluator] judgment call failed ({e}) — treating as rejected")
            findings[i] = {**finding, "confidence": "rejected"}
            trace_entries.append(events.emit("evaluator", "rejected", f"judgment call failed: {e}",
                                              source_agent=finding["source_agent"]))
            continue

        if verdict.claim_follows_from_excerpt:
            findings[i] = {**finding, "confidence": "verified"}
            verified.append(findings[i])
            print(f"[evaluator] VERIFIED ({finding['source_agent']}): {verdict.reason}")
            trace_entries.append(events.emit("evaluator", "verified", verdict.reason,
                                              source_agent=finding["source_agent"], claim=finding["claim"][:200]))
        else:
            findings[i] = {**finding, "confidence": "rejected"}
            print(f"[evaluator] REJECTED ({finding['source_agent']}) at judgment step: {verdict.reason}")
            trace_entries.append(events.emit("evaluator", "rejected", verdict.reason,
                                              source_agent=finding["source_agent"], claim=finding["claim"][:200]))

    return {"findings": findings, "verified_findings": verified, "trace": trace_entries}


async def evaluator_accept_all_node(state: GraphState) -> dict:
    """Baseline for the Evaluator on/off comparison (paper gap G4): promotes
    every unverified finding to verified with no check at all, i.e. trusts the
    model's self-report. Only used when graph.build_graph(evaluator_mode="off")."""
    findings = list(state["findings"])
    verified = list(state["verified_findings"])
    trace_entries = []
    for i, finding in enumerate(findings):
        if finding["confidence"] != "unverified":
            continue
        findings[i] = {**finding, "confidence": "verified"}
        verified.append(findings[i])
        trace_entries.append(events.emit("evaluator", "verified", "accept-all baseline (no check)",
                                          source_agent=finding["source_agent"], claim=finding["claim"][:200]))
    return {"findings": findings, "verified_findings": verified, "trace": trace_entries}


# --- Evidence for the all-tool-results variant (paper study G4) -------------
# The normal Evaluator judges a claim against ONE excerpt: the last tool result,
# cut to 800 characters (agents/common.py). A claim that summarises several tool
# results (e.g. a CVSS score from lookup_cve plus KEV status from the knowledge
# base) then looks unsupported. This variant lets the step-2 judgment see every
# tool result up to the one the finding cites. Step 1 and the stored
# evidence_excerpt are unchanged, and the Evaluator still never edits a claim.
MAX_TOOL_CHARS = 3000      # per tool result
MAX_BROWSER_CHARS = 1000   # browser snapshots are large and rarely hold the cited fact
MAX_TOTAL_CHARS = 15000


def _all_tool_evidence(messages: list[BaseMessage], upto_id: str) -> str:
    plain, browser = [], []
    for m in messages:
        if isinstance(m, ToolMessage):
            name = getattr(m, "name", "") or "tool"
            cap = MAX_BROWSER_CHARS if name.startswith("browser_") else MAX_TOOL_CHARS
            part = f"[tool result: {name}]\n{_message_text(m)[:cap]}"
            (browser if name.startswith("browser_") else plain).append(part)
        if getattr(m, "id", None) == upto_id:
            break
    return "\n\n".join(plain + browser)[:MAX_TOTAL_CHARS]


async def evaluator_node(state: GraphState) -> dict:
    return await _evaluate(state, all_evidence=False)


async def evaluator_all_evidence_node(state: GraphState) -> dict:
    return await _evaluate(state, all_evidence=True)
