"""Safety / Guardrail Agent — deterministic scope check, no LLM call for the
common case. See Research-Paper resources/07-...ARCHITECTURE.md §7.2.

Phase-1 scope (see Langchain conversation on the time-boxed build plan): this
enforces the two hard rules from Research-Paper resources/01-SCOPE.md §4 —
no live third-party targets, no exploit execution — as a plain Python
allow/deny check against target_scope. It is intentionally NOT a general
content filter on model output prose; that is a separate, harder problem
out of scope for this pass.
"""

import events
from state import GraphState

DENY_KEYWORDS = ("execute_exploit", "live_target", "run_poc", "metasploit", "reverse_shell")


def safety_node(state: GraphState) -> dict:
    scope_text = " ".join(str(v).lower() for v in state["target_scope"].values())
    objective_text = state["objective"].lower()

    for kw in DENY_KEYWORDS:
        if kw in scope_text or kw in objective_text:
            reason = (
                f"objective/target_scope references '{kw}', which is out of scope "
                f"per Research-Paper resources/01-SCOPE.md §4 (no live-target "
                f"execution). Passive OSINT/planning/analysis only."
            )
            entry = events.emit("safety", "halted", reason)
            return {"halted": True, "halt_reason": reason, "trace": [entry]}

    entry = events.emit("safety", "cleared", "scope check passed")
    return {"halted": False, "halt_reason": None, "trace": [entry]}
