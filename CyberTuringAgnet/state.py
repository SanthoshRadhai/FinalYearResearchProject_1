from __future__ import annotations

import operator
from typing import Annotated, Literal, Optional, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


# --- RedBlue multi-agent state, ported from ../RedBlue-MultiAgent/state.py ---
# See that file's docstring: the Evaluator node is the only place that
# promotes a Finding from `findings` to `verified_findings`, by literal
# substring-checking `evidence_excerpt` against the real message referenced
# by `evidence_ref`. Never add a code path that writes directly into
# `verified_findings`.


class Finding(TypedDict):
    source_agent: str
    claim: str
    evidence_ref: str
    evidence_excerpt: str
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
    stall_count: int
    last_agent: Optional[str]
    verified_count_at_last_dispatch: int
    trace: Annotated[list[dict], operator.add]


def new_redblue_state(objective: str, mode: Literal["red", "blue", "auto"] = "auto",
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
