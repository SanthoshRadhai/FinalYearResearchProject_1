"""Scaled-up (N=8) live test of the Recon agent's search_knowledge_base tool
-- the follow-up flagged in RESULTS.md §8d's scope note: does the RAG tool
actually get used when the objective is covered locally, AND does Recon
correctly avoid over-relying on it (falling back to lookup_cve/browser
instead) when the objective needs data the local KB snapshot doesn't have?

Objectives 1-5 are covered by the local KB (../rag/rag_corpus.jsonl) and
should resolve via search_knowledge_base alone, no browser. Objectives 6-8
are deliberately chosen to need something the KB can't provide -- either a
CVE too recent for the CISA KEV/CVE snapshots, a data field the KB entries
don't carry (CVSS score isn't in the CISA KEV schema -- see
cisa-kev-kb/build_kb.py), or live/current-events information no static KB
has -- testing whether Recon still falls back correctly rather than
confidently answering from an irrelevant KB hit.

Run via run_agent.sh (needs the one shared cloakbrowser-mcp subprocess).
"""
import asyncio
import json
import time

from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

from state import new_state
from agents.recon import build_recon_node

SERVER_PARAMS = StdioServerParameters(command="npx", args=["-y", "cloakbrowser-mcp@latest"])
RECURSION_LIMIT = 15

# (objective, expectation, note)
CASES = [
    ("What is CVE-2024-3400 and is it linked to any known threat actor campaign?",
     "kb_only", "Covered by cisa-kev-kb + mitre-attack-kb (campaign C0048)"),
    ("What is MITRE ATT&CK technique T1595.001 and how can it be detected or mitigated?",
     "kb_only", "Covered by mitre-attack-kb (technique detection/mitigation fields)"),
    ("What is CWE-79 and what's a standard mitigation for it?",
     "kb_only", "Covered by cwe-kb + owasp-cheatsheets-kb"),
    ("Is CVE-2021-44228 (Log4Shell) listed in the CISA Known Exploited Vulnerabilities catalog, and what's the remediation due date?",
     "kb_only", "Covered by cisa-kev-kb directly"),
    ("What is CAPEC-66 and which CWE weakness does it relate to?",
     "kb_only", "Covered by capec-kb (Related Weaknesses section)"),
    ("What is the current exploitation status of CVE-2026-90829 right now?",
     "needs_fallback", "Likely absent from the static KEV/KB snapshot (dated 2026-09-22) -- should fall back to lookup_cve or report not-found rather than guess"),
    ("What are today's top cybersecurity news headlines?",
     "needs_fallback", "No static KB has live/current-events data -- must use the browser or explicitly say it can't answer"),
    ("What is CVE-2024-3400's exact CVSS score according to NVD?",
     "needs_fallback", "cisa-kev-kb's schema has no CVSS score field (see cisa-kev-kb/build_kb.py) -- correct behavior is lookup_cve, not confidently citing a KB hit for a field it doesn't contain"),
]


async def run_trial(node, objective, expectation, note, idx):
    state = new_state(objective, mode="red")
    t0 = time.time()
    try:
        result = await node(state)
        dt = time.time() - t0
        tool_calls = []
        for m in result["messages"]:
            if type(m).__name__ == "AIMessage" and getattr(m, "tool_calls", None):
                tool_calls.extend(c["name"] for c in m.tool_calls)

        used_kb = "search_knowledge_base" in tool_calls
        used_browser = any(t.startswith("browser_") for t in tool_calls)
        used_lookup_cve = "lookup_cve" in tool_calls

        finding = result["findings"][-1]
        return {
            "trial": idx, "objective": objective, "expectation": expectation, "note": note,
            "ok": True, "latency_s": round(dt, 2), "tool_calls": tool_calls,
            "used_kb": used_kb, "used_browser": used_browser, "used_lookup_cve": used_lookup_cve,
            "claim": finding["claim"][:300],
        }
    except Exception as e:
        return {"trial": idx, "objective": objective, "expectation": expectation, "note": note,
                "ok": False, "latency_s": round(time.time() - t0, 2), "error": str(e)[:400]}


async def main():
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            browser_tools = await load_mcp_tools(session)
            print(f"Loaded {len(browser_tools)} browser tools.\n")

            node = build_recon_node(browser_tools)
            results = []
            for i, (objective, expectation, note) in enumerate(CASES, 1):
                print(f"=== Trial {i} ({expectation}): {objective} ===")
                r = await run_trial(node, objective, expectation, note, i)
                print(json.dumps(r, indent=2))
                print()
                results.append(r)

            ok = [r for r in results if r["ok"]]
            kb_only_cases = [r for r in ok if r["expectation"] == "kb_only"]
            fallback_cases = [r for r in ok if r["expectation"] == "needs_fallback"]

            kb_hit_rate = sum(1 for r in kb_only_cases if r["used_kb"] and not r["used_browser"]) / len(kb_only_cases) if kb_only_cases else 0
            fallback_correct_rate = sum(1 for r in fallback_cases if r["used_browser"] or r["used_lookup_cve"]) / len(fallback_cases) if fallback_cases else 0
            avg_latency_kb_only = sum(r["latency_s"] for r in kb_only_cases) / len(kb_only_cases) if kb_only_cases else 0
            avg_latency_fallback = sum(r["latency_s"] for r in fallback_cases) / len(fallback_cases) if fallback_cases else 0

            print("=== SUMMARY (N={}) ===".format(len(results)))
            print(f"success_rate: {len(ok)}/{len(results)}")
            print(f"kb_only cases resolved via KB alone (no browser): {sum(1 for r in kb_only_cases if r['used_kb'] and not r['used_browser'])}/{len(kb_only_cases)} ({kb_hit_rate*100:.0f}%)")
            print(f"needs_fallback cases that correctly used lookup_cve/browser: {sum(1 for r in fallback_cases if r['used_browser'] or r['used_lookup_cve'])}/{len(fallback_cases)} ({fallback_correct_rate*100:.0f}%)")
            print(f"avg_latency_kb_only_cases_s: {avg_latency_kb_only:.2f}")
            print(f"avg_latency_fallback_cases_s: {avg_latency_fallback:.2f}")

            with open("bench_recon_rag_n8_results.json", "w") as f:
                json.dump(results, f, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
