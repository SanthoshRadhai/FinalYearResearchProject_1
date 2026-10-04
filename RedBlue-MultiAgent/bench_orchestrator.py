"""Scaled-up (N=8) Orchestrator benchmark — bumps RESULTS.md §6 from n=4 to
n=8, adding the halted-short-circuit path, an edge-case empty objective, an
unimplemented-specialist robustness check, and (most importantly) a case that
exposes a real limitation in the stall-count logic: `agents/orchestrator.py`
increments `stall_count` whenever the SAME specialist is picked twice in a
row, regardless of whether new verified findings were actually produced in
between. A legitimately productive multi-CVE session that calls `recon`
twice in a row (once per CVE) would be indistinguishable, by this counter,
from a genuinely stuck loop. Case F below demonstrates this concretely rather
than just asserting it from reading the code.
"""

import asyncio
import json
import time

from agents.orchestrator import orchestrator_node, STALL_LIMIT
from state import new_state, Finding

CASES = []


async def case_A_no_findings():
    s = new_state("Investigate CVE-2024-3400 and tell me if we should be worried.")
    t0 = time.time()
    out = await orchestrator_node(s)
    return {"case": "A_no_findings_yet", "expected": "recon", "got": out["next_agent"],
            "correct": out["next_agent"] == "recon", "latency_s": round(time.time() - t0, 2)}


async def case_B_recon_done_has_cvss():
    s = new_state("Investigate CVE-2024-3400 and tell me if we should be worried.")
    s["verified_findings"] = [Finding(source_agent="recon", confidence="verified", evidence_ref="m1",
        evidence_excerpt="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
        claim="CVE-2024-3400 has CVSS vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H")]
    s["last_agent"] = "recon"
    t0 = time.time()
    out = await orchestrator_node(s)
    return {"case": "B_recon_done_has_cvss", "expected": "vuln_analysis", "got": out["next_agent"],
            "correct": out["next_agent"] == "vuln_analysis", "latency_s": round(time.time() - t0, 2)}


async def case_C_recon_and_vuln_done():
    s = new_state("Investigate CVE-2024-3400 and tell me if we should be worried.")
    s["verified_findings"] = [
        Finding(source_agent="recon", confidence="verified", evidence_ref="m1",
                evidence_excerpt="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
                claim="CVE-2024-3400 has CVSS vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H"),
        Finding(source_agent="vuln_analysis", confidence="verified", evidence_ref="m2",
                evidence_excerpt="base_score': 10.0, 'severity': 'Critical'",
                claim="CVE-2024-3400 is Critical severity, base score 10.0, high priority for escalation."),
    ]
    s["last_agent"] = "vuln_analysis"
    t0 = time.time()
    out = await orchestrator_node(s)
    return {"case": "C_recon_and_vuln_done", "expected": "end", "got": out["next_agent"],
            "correct": out["next_agent"] == "end",
            "note": "known over-verification bias (see RESULTS.md §6) -- not a crash",
            "latency_s": round(time.time() - t0, 2)}


async def case_D_stall_limit_forces_end():
    s = new_state("Investigate CVE-2024-3400 and tell me if we should be worried.")
    s["last_agent"] = "recon"
    s["stall_count"] = STALL_LIMIT - 1
    t0 = time.time()
    out = await orchestrator_node(s)
    tripped = out["next_agent"] == "end"
    return {"case": "D_stall_limit_forces_end", "expected": "end (if router repeats recon)",
            "got": out["next_agent"], "stall_count_after": out.get("stall_count"),
            "correct": tripped, "latency_s": round(time.time() - t0, 2)}


async def case_E_halted_short_circuits():
    s = new_state("anything")
    s["halted"] = True
    t0 = time.time()
    out = await orchestrator_node(s)
    dt = time.time() - t0
    return {"case": "E_halted_short_circuits_no_llm_call", "expected": "end", "got": out["next_agent"],
            "correct": out["next_agent"] == "end" and dt < 0.5,
            "note": "should return instantly without an LLM call when halted=True",
            "latency_s": round(dt, 3)}


async def case_F1_progress_resets_stall_count():
    """FIXED (was the documented limitation): a repeated pick of the SAME
    specialist that actually produced a new verified finding since the last
    dispatch must NOT increment stall_count. `verified_count_at_last_dispatch`
    is set to 0 (as if 1 verified finding was produced since a dispatch that
    started at 0), so if the router picks 'recon' again, progress was made
    and stall_count must stay 0."""
    s = new_state("Investigate both CVE-2024-3400 and CVE-2026-9862 and summarize each.")
    s["verified_findings"] = [Finding(source_agent="recon", confidence="verified", evidence_ref="m1",
        evidence_excerpt="CVE-2024-3400 details", claim="CVE-2024-3400 is a critical PAN-OS vulnerability.")]
    s["last_agent"] = "recon"
    s["stall_count"] = 0
    s["verified_count_at_last_dispatch"] = 0  # 0 verified findings before recon's last run, now 1 -> progress
    t0 = time.time()
    out = await orchestrator_node(s)
    correct = out.get("stall_count", -1) == 0  # must NOT increment, regardless of which agent is picked next
    return {"case": "F1_progress_resets_stall_count", "got_next_agent": out["next_agent"],
            "stall_count_after": out.get("stall_count"), "correct": correct,
            "note": "verified_findings grew since last dispatch -> stall_count must stay 0 even if 'recon' is picked again",
            "latency_s": round(time.time() - t0, 2)}


async def case_F2_no_progress_still_increments():
    """The other half of the fix: if the SAME specialist is picked again and
    verified_findings did NOT grow since the last dispatch, stall_count must
    still increment -- the fix must not accidentally disable the loop guard
    entirely."""
    s = new_state("Investigate CVE-2024-3400 and tell me if we should be worried.")
    s["verified_findings"] = [Finding(source_agent="recon", confidence="verified", evidence_ref="m1",
        evidence_excerpt="CVE-2024-3400 details", claim="CVE-2024-3400 is a critical PAN-OS vulnerability.")]
    s["last_agent"] = "recon"
    s["stall_count"] = 0
    s["verified_count_at_last_dispatch"] = 1  # already had this 1 finding before the last dispatch -> no growth
    t0 = time.time()
    out = await orchestrator_node(s)
    # Only scorable when the router actually repeats 'recon' (can't force the LLM's choice deterministically).
    scorable = out["next_agent"] == "recon"
    correct = (out.get("stall_count", -1) == 1) if scorable else None
    return {"case": "F2_no_progress_still_increments", "got_next_agent": out["next_agent"],
            "stall_count_after": out.get("stall_count"), "scorable": scorable, "correct": correct,
            "note": "verified_findings did NOT grow since last dispatch -> stall_count must still increment if 'recon' repeats",
            "latency_s": round(time.time() - t0, 2)}


async def case_G_empty_objective_edge_case():
    s = new_state("")
    t0 = time.time()
    try:
        out = await orchestrator_node(s)
        return {"case": "G_empty_objective", "crashed": False, "got": out["next_agent"],
                "latency_s": round(time.time() - t0, 2)}
    except Exception as e:
        return {"case": "G_empty_objective", "crashed": True, "error": str(e)[:300],
                "latency_s": round(time.time() - t0, 2)}


async def case_H_unimplemented_specialist_pick_is_handled():
    """The Orchestrator's schema lists Phase-2/3 specialists it doesn't yet
    have code for. This doesn't test the Orchestrator forcing a specific
    pick (it can't be forced without mocking the LLM) -- it confirms that
    WHATEVER it picks is a valid literal the graph can route on, i.e. no
    crash/undefined value, for a blue-team-flavored objective that might
    tempt it toward an unimplemented specialist."""
    s = new_state("We're seeing repeated failed login attempts in our logs -- correlate against known threats.")
    t0 = time.time()
    out = await orchestrator_node(s)
    valid_values = {"recon", "vuln_analysis", "exploit_poc", "attack_planning", "threat_intel",
                     "log_triage", "detection_mitigation", "incident_response", "end"}
    return {"case": "H_blue_objective_valid_literal", "got": out["next_agent"],
            "is_valid_literal": out["next_agent"] in valid_values,
            "note": "graph.py routes any not-yet-built pick to a safe no-op node, not a crash",
            "latency_s": round(time.time() - t0, 2)}


async def main():
    results = []
    for fn in [case_A_no_findings, case_B_recon_done_has_cvss, case_C_recon_and_vuln_done,
               case_D_stall_limit_forces_end, case_E_halted_short_circuits,
               case_F1_progress_resets_stall_count, case_F2_no_progress_still_increments,
               case_G_empty_objective_edge_case, case_H_unimplemented_specialist_pick_is_handled]:
        r = await fn()
        print(json.dumps(r, indent=2))
        results.append(r)

    scored = [r for r in results if r.get("correct") is not None]
    n_correct = sum(1 for r in scored if r["correct"])
    print(f"\n=== ORCHESTRATOR SUMMARY (N={len(results)}, {len(scored)} scorable) === "
          f"{n_correct}/{len(scored)} as expected")
    with open("bench_orchestrator_n8_results.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
