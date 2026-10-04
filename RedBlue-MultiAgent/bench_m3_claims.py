"""Automatic claim-pair benchmark for the Evaluator in isolation (paper gap
M3), replacing author-written cases with claims generated from NVD ground
truth for every CVE in g4_cves.json (the held-out set plus the m3_only extras).

For each CVE the evidence excerpt is exactly what the agent would capture:
str(lookup_cve output)[:800]. Claims generated per CVE:

  true_score_sev     the real score and severity. EXPECTED VERIFIED only if both
                     appear in the 800-character excerpt; when the long description
                     pushes the score past the cut, the claim is true but unsupported.
  wrong_score        a different score with its matching severity
  wrong_severity     the real score with a wrong severity label
  wrong_cve          the real score and severity attributed to a different CVE id
  kev_membership     "is in the CISA KEV catalogue" (true for KEV CVEs, false
                     otherwise); supported only when the excerpt still contains NVD's
                     link to the CISA KEV catalogue page (first run of this benchmark
                     wrongly assumed it never does; see rescore_m3.py)
  description_quote  the first sentence of the description, verbatim

The expected verdict is a deterministic rule (are all stated facts literally
present in the excerpt?), not a judgment. It tests the PROVENANCE check, not
factual truth: a true claim missing from the excerpt is expected to be rejected.
Each claim goes through the real evaluator_node (substring check + LLM judgment).

    ./run_agent.sh bench_m3_claims.py      (needs llama-server on localhost:5500)

Options: M3_CVES (g4_cves.json), M3_LIMIT_CVES (all), M3_OUT (m3_results.jsonl),
M3_WORKERS (concurrent judge calls, default 1; llama-server has 4 slots).
"""

import asyncio
import json
import os
import random
import time
from collections import defaultdict
from pathlib import Path

from langchain_core.messages import ToolMessage

import g4_common as g
from agents.evaluator import evaluator_node
from state import Finding, new_state

CVES_PATH = Path(os.getenv("M3_CVES", "g4_cves.json"))
LIMIT = int(os.getenv("M3_LIMIT_CVES", "0")) or None
OUT = Path(os.getenv("M3_OUT", "m3_results.jsonl"))
SEED = 7
WORKERS = int(os.getenv("M3_WORKERS", "1"))  # llama-server has 4 slots; the claim judge needs no browser


def kev_link_in(excerpt):
    return "known-exploited-vulnerabilities" in excerpt.lower()


def make_pairs(cves):
    rng = random.Random(SEED)
    pairs = []
    for i, t in enumerate(cves):
        cve = t["cve_id"]
        excerpt = t["tool_excerpt"]
        S, SEV = t["scores"][0]["score"], t["scores"][0]["severity"]
        other = cves[(i + 1) % len(cves)]["cve_id"]
        score_in = f"'base_score': {S}" in excerpt
        # no closing quote: the 800-char cut can land right after the label text
        sev_in = f"'severity': '{SEV}" in excerpt

        wrong = S
        while any(abs(wrong - s["score"]) < 0.05 for s in t["scores"]):
            wrong = round(min(10.0, max(0.1, S + rng.choice([-3.1, -2.4, -1.7, -0.9, 0.9, 1.2, 1.8]))), 1)
            if wrong == S:
                wrong = round((S + 2.3) % 10, 1) or 0.5
        sev_wrong = rng.choice([x for x in g.SEVERITIES if x != SEV])
        sentence = t["description"].split(". ")[0].strip()
        sentence = sentence if sentence.endswith(".") else sentence + "."

        def add(cat, claim, expected, truth):
            pairs.append({"cve": cve, "category": cat, "claim": claim, "excerpt": excerpt,
                          "expected": expected, "claim_true": truth})

        add("true_score_sev", f"{cve} has a CVSS base score of {S} and severity {SEV}.",
            "verified" if (score_in and sev_in) else "rejected", True)
        add("wrong_score", f"{cve} has a CVSS base score of {wrong} and severity {g.severity_of(wrong)}.", "rejected", False)
        add("wrong_severity", f"{cve} has a CVSS base score of {S} and severity {sev_wrong}.", "rejected", False)
        add("wrong_cve", f"{other} has a CVSS base score of {S} and severity {SEV}.", "rejected", False)
        # NVD lists a link to the CISA KEV catalogue page among the references of KEV CVEs; when that
        # link survives the 800-char cut, a KEV-membership claim IS supported by the excerpt.
        kev_supported = bool(t["in_kev"]) and kev_link_in(excerpt)
        add("kev_membership", f"{cve} is in the CISA Known Exploited Vulnerabilities catalog.",
            "verified" if kev_supported else "rejected", bool(t["in_kev"]))
        if sentence in excerpt:
            add("description_quote", f"{cve}: {sentence}", "verified", True)
    return pairs


async def judge(pair, idx):
    msg_id = f"m3_msg_{idx}"
    tool_msg = ToolMessage(content=pair["excerpt"], tool_call_id=f"call_{idx}", name="lookup_cve", id=msg_id)
    finding = Finding(source_agent="recon", confidence="unverified", evidence_ref=msg_id,
                      evidence_excerpt=pair["excerpt"], claim=pair["claim"])
    state = new_state("m3 evaluator test", mode="red")
    state["messages"] = [tool_msg]
    state["findings"] = [finding]
    t0 = time.time()
    res = await evaluator_node(state)
    reason = res["trace"][-1]["message"] if res["trace"] else ""
    return {**pair, "verdict": res["findings"][0]["confidence"], "reason": reason[:300],
            "latency_s": round(time.time() - t0, 2)}


def summarize(results):
    ev = [r for r in results if r["expected"] == "verified"]
    er = [r for r in results if r["expected"] == "rejected"]
    verified = [r for r in results if r["verdict"] == "verified"]
    print("\n=== M3 summary (", len(results), "claims ) ===")
    print("recall on expected-verified :", g.fmt_rate(sum(r["verdict"] == "verified" for r in ev), len(ev)))
    print("reject rate on expected-rejected:", g.fmt_rate(sum(r["verdict"] == "rejected" for r in er), len(er)))
    print("precision of verified       :", g.fmt_rate(sum(r["expected"] == "verified" for r in verified), len(verified)))
    fa = [r for r in er if not r["claim_true"]]
    tu = [r for r in er if r["claim_true"]]
    print("false claims rejected       :", g.fmt_rate(sum(r["verdict"] == "rejected" for r in fa), len(fa)))
    print("true-but-unsupported rejected:", g.fmt_rate(sum(r["verdict"] == "rejected" for r in tu), len(tu)),
          "(rejection is the intended provenance behaviour)")
    by = defaultdict(list)
    for r in results:
        by[r["category"]].append(r)
    print("\nby category (verdict agrees with expected):")
    for cat, rs in sorted(by.items()):
        print(f"  {cat:18s}", g.fmt_rate(sum(r['verdict'] == r['expected'] for r in rs), len(rs)))


async def main():
    doc = json.loads(CVES_PATH.read_text(encoding="utf-8"))
    cves = doc["cves"][:LIMIT] if LIMIT else doc["cves"]
    pairs = make_pairs(cves)
    print(f"{len(cves)} CVEs -> {len(pairs)} claim pairs")
    sem = asyncio.Semaphore(WORKERS)
    finished = 0
    t_start = time.time()

    async def one(i, p):
        nonlocal finished
        async with sem:
            try:
                r = await judge(p, i)
            except Exception as e:  # noqa: BLE001
                r = {**p, "verdict": "error", "reason": f"{type(e).__name__}: {e}"[:300], "latency_s": 0}
        finished += 1
        if finished % 25 == 0:
            print(f"  {finished}/{len(pairs)} ({time.time() - t_start:.0f}s)", flush=True)
        return r

    results = await asyncio.gather(*(one(i, p) for i, p in enumerate(pairs)))
    print(f"wall time {time.time() - t_start:.0f}s with {WORKERS} worker(s)")
    with OUT.open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    summarize([r for r in results if r["verdict"] != "error"])
    print("errors:", sum(r["verdict"] == "error" for r in results), "| wrote", OUT)


if __name__ == "__main__":
    asyncio.run(main())
