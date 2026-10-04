"""Scaled-up (N=10) Evaluator benchmark — bumps RESULTS.md §5 from n=4 to
n=10 controlled cases, adding more diverse claim/excerpt combinations on top
of the original 4 (correct-grounded, fabricated-excerpt, unsupported-claim,
dangling-ref). No browser/MCP subprocess involved.
"""

import asyncio
import json
import time

from langchain_core.messages import ToolMessage
from agents.evaluator import evaluator_node
from state import new_state, Finding

REAL_TOOL_OUTPUT = (
    "{'cve_id': 'CVE-2024-3400', 'description': 'A command injection as a result of "
    "arbitrary file creation vulnerability in the GlobalProtect feature of Palo Alto "
    "Networks PAN-OS software for specific PAN-OS versions and distinct feature "
    "configurations may enable an unauthenticated attacker to execute arbitrary code "
    "with root privileges on the firewall.', 'cvss_vector': "
    "'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H', 'base_score': 10.0, 'severity': 'CRITICAL'}"
)
TOOL_MSG = ToolMessage(content=REAL_TOOL_OUTPUT, tool_call_id="call_1", name="lookup_cve", id="msg_1")

CASES = [
    {
        "name": "A_correct_grounded_claim_full_quote",
        "expected": {"verified"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt=REAL_TOOL_OUTPUT,
            claim="CVE-2024-3400 has CVSS vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, base score 10.0, severity CRITICAL."),
    },
    {
        "name": "B_fabricated_evidence_substring",
        "expected": {"rejected"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt="base_score': 11.5, 'severity': 'APOCALYPTIC'",
            claim="CVE-2024-3400 has an unprecedented CVSS score of 11.5, rated APOCALYPTIC."),
    },
    {
        "name": "C_real_excerpt_unsupported_claim",
        "expected": {"rejected"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt="execute arbitrary code with root privileges on the firewall",
            claim="This vulnerability has already been patched by Palo Alto and no longer affects any customers."),
    },
    {
        "name": "D_dangling_evidence_ref",
        "expected": {"rejected"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_DOES_NOT_EXIST",
            evidence_excerpt="anything", claim="Some claim citing a message that isn't in history."),
    },
    {
        "name": "E_narrow_excerpt_narrow_claim_should_verify",
        "expected": {"verified"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
            claim="CVE-2024-3400's CVSS vector is CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H."),
    },
    {
        "name": "F_empty_excerpt",
        "expected": {"rejected"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt="", claim="CVE-2024-3400 is critical."),
    },
    {
        "name": "G_near_miss_substring_typo",
        "expected": {"rejected"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt="base_score': 10.1",  # real text has 10.0, not 10.1 -- must NOT match
            claim="CVE-2024-3400 has a base score of 10.1."),
    },
    {
        "name": "H_claim_understates_severity_still_grounded",
        "expected": {"verified"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt=REAL_TOOL_OUTPUT,
            claim="CVE-2024-3400 is a command injection vulnerability in PAN-OS GlobalProtect."),
    },
    {
        "name": "I_claim_about_wrong_cve_same_excerpt",
        "expected": {"rejected"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt=REAL_TOOL_OUTPUT,
            claim="CVE-2025-99999 is a command injection vulnerability affecting PAN-OS."),
    },
    {
        "name": "J_verbatim_quote_of_description_only",
        "expected": {"verified"},
        "finding": Finding(source_agent="recon", confidence="unverified", evidence_ref="msg_1",
            evidence_excerpt="enable an unauthenticated attacker to execute arbitrary code with root privileges on the firewall",
            claim="An unauthenticated attacker can execute arbitrary code with root privileges on the firewall for this CVE."),
    },
]


async def main():
    results = []
    for case in CASES:
        state = new_state("test objective")
        state["messages"] = [TOOL_MSG]
        state["findings"] = [case["finding"]]
        t0 = time.time()
        out = await evaluator_node(state)
        dt = time.time() - t0
        got = out["findings"][0]["confidence"]
        correct = got in case["expected"]
        results.append({"case": case["name"], "expected": sorted(case["expected"]),
                         "got": got, "correct": correct, "latency_s": round(dt, 2)})
        print(json.dumps(results[-1], indent=2))

    n_correct = sum(1 for r in results if r["correct"])
    print(f"\n=== EVALUATOR SUMMARY (N={len(results)}) === {n_correct}/{len(results)} as expected "
          f"({n_correct/len(results)*100:.1f}%)")
    with open("bench_evaluator_n10_results.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
