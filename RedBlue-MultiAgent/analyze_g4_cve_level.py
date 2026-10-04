"""CVE-level view of the Evaluator on/off/all study. Each CVE is run three times
per condition, so run-level intervals (analyze_g4.py) treat repeats as
independent and are too narrow. Here the unit is the CVE (n=50): a CVE counts
as "answered" if a majority (>=2 of 3) of its repeats ended with an accepted
claim, and as having a "false accept" if ANY repeat accepted an incorrect claim.
Also splits by CVE pool (KEV / non-KEV) and lists every incorrect claim.

    python analyze_g4_cve_level.py [g4_onoff.jsonl] [g4_cves.json]
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import g4_common as g

runs = Path(sys.argv[1] if len(sys.argv) > 1 else "g4_onoff.jsonl")
cves = Path(sys.argv[2] if len(sys.argv) > 2 else "g4_cves.json")
truth = {c["cve_id"]: c for c in json.loads(cves.read_text(encoding="utf-8"))["cves"]}
rows = [json.loads(line) for line in runs.read_text(encoding="utf-8").splitlines() if line.strip()]


def status(text, cve):
    return g.check_claim(text, truth[cve], truth[cve]["in_kev"])["status"]


by = defaultdict(lambda: defaultdict(list))  # cond -> cve -> runs
for r in rows:
    by[r["condition"]][r["cve"]].append(r)

for cond in sorted(by):
    per = by[cond]
    n = len(per)
    answered_maj = correct_maj = any_false_accept = any_displayed_wrong = 0
    for cve, rs in per.items():
        ok = [r for r in rs if r["ok"]]
        ans = [r for r in ok if r["verified_claims"]]
        if len(ans) * 2 >= len(ok) and ok:
            answered_maj += 1
        good = [r for r in ans if status("\n".join(r["verified_claims"]), cve) == "correct"]
        if ans and len(good) * 2 > len(ans):
            correct_maj += 1
        if any(status("\n".join(r["verified_claims"]), cve) == "incorrect" for r in ans):
            any_false_accept += 1
        if any(status(r["final_answer"], cve) == "incorrect" for r in ok):
            any_displayed_wrong += 1
    print(f"\n=== {cond}: {n} CVEs ===")
    print("CVE answered in a majority of repeats :", g.fmt_rate(answered_maj, n))
    print("CVE answered AND mostly correct       :", g.fmt_rate(correct_maj, n))
    print("CVE with any false-accepted claim     :", g.fmt_rate(any_false_accept, n))
    print("CVE with any wrong displayed answer   :", g.fmt_rate(any_displayed_wrong, n))
    for pool in ("kev", "nonkev"):
        sub = [c for c in per if truth[c]["pool"] == pool]
        a = sum(1 for c in sub if sum(1 for r in per[c] if r["ok"] and r["verified_claims"]) * 2 >= max(1, sum(1 for r in per[c] if r["ok"])))
        print(f"  pool {pool:7s}: answered (majority)", g.fmt_rate(a, len(sub)))

print("\n=== every INCORRECT claim (accepted or rejected) ===")
for r in rows:
    if not r["ok"]:
        continue
    for f in r["findings"]:
        if status(f["claim"], r["cve"]) == "incorrect":
            t = truth[r["cve"]]
            p = g.parse_claim(f["claim"])
            print(f"- {r['cve']} [{r['condition']} rep{r['repeat']}] decision={f['confidence']} stated={p} "
                  f"truth scores={[s['score'] for s in t['scores']]} kev={t['in_kev']}")

print("\n=== errors ===")
for r in rows:
    if not r["ok"]:
        print("-", r["cve"], r["condition"], r["repeat"], r.get("error", "")[:90])
