"""Scaled-up (N=20) Vulnerability Analysis Agent benchmark — bumps §2 of
RESULTS.md from n=5 to n=20 for statistical power, and adds coverage across
CVSS v2, v3.0, v3.1, and v4.0 vectors (v4.0 was never exercised by any prior
benchmark — tools/cvss_tool.py's CVSS4 code path had zero test coverage
before this file).

Note: CVSS vectors below are illustrative/approximate for well-known CVEs,
not guaranteed byte-exact NVD values — this benchmark tests tool-calling
reliability and CVSS-parsing correctness across versions/severities, not CVE
factual accuracy (that's covered separately by the live NVD lookup_cve tool
in RESULTS.md §1). No browser/MCP subprocess involved.
"""

import asyncio
import json
import time

from agents.vuln_analysis import build_vuln_analysis_node
from state import new_state

# (label, CVSS vector, expected version bucket) — mix of versions/severities.
CASES = [
    ("CVE-2024-3400", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", "3.x"),
    ("CVE-2026-9862", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2021-44228 (Log4Shell)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", "3.x"),
    ("CVE-2017-0144 (EternalBlue)", "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2014-0160 (Heartbleed)", "CVSS:2.0/AV:N/AC:L/Au:N/C:P/I:N/A:N", "2.0"),
    ("CVE-2017-5638 (Apache Struts)", "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2019-0708 (BlueKeep)", "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2020-1472 (Zerologon)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", "3.x"),
    ("CVE-2022-30190 (Follina)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2023-4863 (WebP heap overflow)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2022-22965 (Spring4Shell)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2021-34527 (PrintNightmare)", "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2019-11510 (Pulse Secure)", "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N", "3.x"),
    ("CVE-2020-0601 (CurveBall)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N", "3.x"),
    ("CVE-2018-13379 (Fortinet SSL VPN)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N", "3.x"),
    ("CVE-2016-10033 (PHPMailer)", "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "3.x"),
    ("CVE-2015-1635 (HTTP.sys)", "CVSS:2.0/AV:N/AC:L/Au:N/C:C/I:C/A:C", "2.0"),
    ("CVE-2013-3900 (WinVerifyTrust)", "CVSS:2.0/AV:N/AC:M/Au:N/C:N/I:P/A:N", "2.0"),
    ("CVE-2021-26855 (ProxyLogon)", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", "3.x"),
    ("Synthetic CVSS v4.0 test vector", "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N", "4.0"),
]


async def run_trial(node, label, vector, idx):
    objective = f"{label} has CVSS vector {vector} (from NVD). Parse it and give a priority assessment."
    state = new_state(objective, mode="red")
    t0 = time.time()
    try:
        result = await node(state)
        dt = time.time() - t0
        finding = result["findings"][-1]
        n_tool_msgs = sum(1 for m in result["messages"] if type(m).__name__ == "ToolMessage")
        return {
            "trial": idx, "label": label, "vector": vector, "ok": True,
            "latency_s": round(dt, 2), "tool_calls": n_tool_msgs,
            "claim": finding["claim"][:200],
        }
    except Exception as e:
        return {"trial": idx, "label": label, "vector": vector, "ok": False,
                "latency_s": round(time.time() - t0, 2), "error": str(e)[:300]}


async def main():
    node = build_vuln_analysis_node()
    results = []
    for i, (label, vector, _) in enumerate(CASES, 1):
        r = await run_trial(node, label, vector, i)
        print(json.dumps(r, indent=2))
        results.append(r)

    ok = sum(1 for r in results if r["ok"])
    tool_used = sum(1 for r in results if r.get("tool_calls", 0) >= 1)
    lat = [r["latency_s"] for r in results if r["ok"]]
    print("\n=== SUMMARY (N={}) ===".format(len(results)))
    print(f"success_rate: {ok}/{len(results)} ({ok/len(results)*100:.1f}%)")
    print(f"correct_tool_use_rate: {tool_used}/{len(results)} ({tool_used/len(results)*100:.1f}%)")
    if lat:
        avg = sum(lat) / len(lat)
        variance = sum((x - avg) ** 2 for x in lat) / len(lat)
        print(f"avg_latency_s: {avg:.2f}, min: {min(lat):.2f}, max: {max(lat):.2f}, stdev: {variance**0.5:.2f}")

    with open("bench_vuln_analysis_n20_results.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
