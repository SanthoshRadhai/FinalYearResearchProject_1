"""Re-scores m3_results.jsonl with the corrected expected-verdict rule for
KEV-membership claims (the first run assumed the KEV link never survives the
800-character excerpt; in 13 of 30 true-KEV cases it does). Verdicts are the
original Evaluator outputs; only the expected labels are recomputed. The raw
file is left untouched. Needs no LLM.
"""
import json
import sys

from bench_m3_claims import kev_link_in, summarize

src = sys.argv[1] if len(sys.argv) > 1 else "m3_results.jsonl"
rows = [json.loads(line) for line in open(src, encoding="utf-8") if line.strip()]
for r in rows:
    if r["category"] == "kev_membership":
        r["expected"] = "verified" if (r["claim_true"] and kev_link_in(r["excerpt"])) else "rejected"
with open("m3_results_rescored.jsonl", "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")
summarize([r for r in rows if r["verdict"] != "error"])
print("\nremaining mismatches:")
for r in rows:
    if r["verdict"] != r["expected"]:
        print(" -", r["category"], r["cve"], "expected", r["expected"], "got", r["verdict"], "|", r["reason"][:150])
