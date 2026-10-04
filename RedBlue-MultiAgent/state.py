"""Shared LangGraph state for the red/blue multi-agent system.

See ../Research-Paper resources/07-MULTI-AGENT-ARCHITECTURE.md §3 for the design
rationale. This is intentionally a thin, mechanical data model — the Evaluator
node (agents/evaluator.py) is the only place that promotes a Finding from
`findings` to `verified_findings`, and it does so by literal substring-checking
`evidence_excerpt` against the real message referenced by `evidence_ref`. Never
add a code path that writes directly into `verified_findings`.
"""

from __future__ import annotations

import operator
from typing import Annotated, Literal, Optional, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class Finding(TypedDict):
    source_agent: str
    claim: str
    evidence_ref: str          # id of the message in `messages` this claim is grounded in
    evidence_excerpt: str      # verbatim substring that must appear in that message's content
    confidence: Literal["unverified", "verified", "rejected"]


class GraphState(TypedDict):
    objective: str
    mode: Literal["red", "blue", "auto"]
    messages: Annotated[list[BaseMessage], add_messages]
    target_scope: dict
    findings: list[Finding]
    verified_findings: list[Finding]
    attack_plan: Optional[dict]
    mitigation_plan: Optional[dict]
    next_agent: Optional[str]
    halted: bool
    halt_reason: Optional[str]
    # Loop guard: counts consecutive dispatches to the same specialist that
    # produced NO new verified_findings, so the Orchestrator can bail instead
    # of looping forever (the multi-agent analogue of scripts 4-6's
    # MALFORMED_CALL_LIMIT). `verified_count_at_last_dispatch` is what makes
    # this progress-aware rather than pure repetition-counting — see
    # agents/orchestrator.py and RESULTS.md §6a Case F for the bug this fixes
    # (a naive "same agent twice = stall" check penalizes a legitimately
    # productive repeated specialist call identically to a genuinely stuck one).
    stall_count: int
    last_agent: Optional[str]
    verified_count_at_last_dispatch: int
    # Durable, append-only record of every "thinking" event a node emits
    # (routing decisions + reasons, Evaluator verdicts + reasons, circuit
    # breaker/sanitizer triggers, tool calls) -- see events.py for the live
    # push channel a web UI consumes; this field is what survives in the
    # final returned state for anything that isn't listening live (bench
    # scripts, main.py's REPL, tests). `operator.add` makes this an
    # append-only reducer, same idea as `messages`' add_messages.
    trace: Annotated[list[dict], operator.add]


def new_state(objective: str, mode: Literal["red", "blue", "auto"] = "auto",
              target_scope: Optional[dict] = None) -> GraphState:
    return GraphState(
        objective=objective,
        mode=mode,
        messages=[],
        target_scope=target_scope or {},
        findings=[],
        verified_findings=[],
        attack_plan=None,
        mitigation_plan=None,
        next_agent=None,
        halted=False,
        halt_reason=None,
        stall_count=0,
        last_agent=None,
        verified_count_at_last_dispatch=0,
        trace=[],
    )
