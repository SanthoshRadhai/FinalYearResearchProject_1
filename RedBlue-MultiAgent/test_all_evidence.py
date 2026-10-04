"""Sanity check for the all-tool-results Evaluator: a claim that combines a
fact from lookup_cve with a fact from a later knowledge-base result should be
rejected by the normal Evaluator (it only sees the last result) and verified
by the all-evidence variant. A claim with a wrong score must be rejected by both."""
import asyncio

from langchain_core.messages import ToolMessage

from agents.evaluator import evaluator_all_evidence_node, evaluator_node
from state import Finding, new_state

LOOKUP = ("{'cve_id': 'CVE-2024-3400', 'description': 'A command injection vulnerability in the "
          "GlobalProtect feature of Palo Alto Networks PAN-OS.', 'cvss_vector': "
          "'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H', 'cvss_version': '3.1', 'base_score': 10.0, "
          "'severity': 'CRITICAL'}")
KB = ("[{'source': 'cisa-kev-kb: CVE-2024-3400', 'excerpt': '# CVE-2024-3400 **Vendor/Project:** Palo Alto "
      "Networks **Date Added to KEV:** 2024-04-12'}]")


async def verdict(node, claim):
    m1 = ToolMessage(content=LOOKUP, tool_call_id="c1", name="lookup_cve", id="t1")
    m2 = ToolMessage(content=KB, tool_call_id="c2", name="search_knowledge_base", id="t2")
    st = new_state("test", mode="red")
    st["messages"] = [m1, m2]
    st["findings"] = [Finding(source_agent="recon", confidence="unverified", evidence_ref="t2",
                              evidence_excerpt=KB, claim=claim)]
    res = await node(st)
    return res["findings"][0]["confidence"]


async def main():
    good = "CVE-2024-3400 has a CVSS base score of 10.0 (CRITICAL) and is listed in the CISA KEV catalog."
    bad = "CVE-2024-3400 has a CVSS base score of 6.1 (MEDIUM) and is listed in the CISA KEV catalog."
    for name, node in (("normal", evaluator_node), ("all-evidence", evaluator_all_evidence_node)):
        print(f"{name:13s} multi-source true claim -> {await verdict(node, good)}   wrong-score claim -> {await verdict(node, bad)}")


asyncio.run(main())
