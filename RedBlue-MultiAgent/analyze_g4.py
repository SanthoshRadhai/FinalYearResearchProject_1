"""Scores g4_onoff.jsonl (written by bench_g4_onoff.py) against NVD / CISA KEV
ground truth in g4_cves.json and prints the Evaluator on/off comparison with
Wilson 95% intervals. Deterministic: no LLM is involved in judging correctness.

    python analyze_g4.py [g4_onoff.jsonl] [g4_cves.json]

Definitions (per run, then per finding):
  answered         at least one finding was accepted (verified)
  accepted claim   the text of the accepted (verified) findings joined together
  status           correct | incorrect | no_checkable_fact, from g4_common.check_claim
                   (checks base score, severity label and KEV membership only)
  false accept     an answered run whose accepted claim states a wrong fact
  displayed answer the final message text the user would read
  false reject     (on condition) a finding whose claim is correct but was rejected
  provenance reject a false reject whose stated facts are NOT in the captured excerpt
"""

import json
import statistics
import sys
from collections import Counter
from pathlib import Path

import g4_common as g

runs_path = Path(sys.argv[1] if len(sys.argv) > 1 else "g4_onoff.jsonl")
cves_path = Path(sys.argv[2] if len(sys.argv) > 2 else "g4_cves.json")
doc = json.loads(cves_path.read_text(encoding="utf-8"))
truth = {c["cve_id"]: c for c in doc["cves"]}
rows = [json.loads(line) for line in runs_path.read_text(encoding="utf-8").splitlines() if line.strip()]


def status(text, cve):
    return g.check_claim(text, truth[cve], truth[cve]["in_kev"])["status"]


def supported_by_excerpt(text, excerpt):
    p = g.parse_claim(text)
    up = (excerpt or "").upper()
    for v in p["scores"]:
        if str(v) not in (excerpt or ""):
            return False
    for v in p["severities"]:
        if v not in up:
            return False
    if p["kev"] is not None and "KEV" not in up and "KNOWN EXPLOITED" not in up:
        return False
    return True


out = {}
for cond in sorted({r["condition"] for r in rows}):
    rs = [r for r in rows if r["condition"] == cond]
    ok = [r for r in rs if r["ok"]]
    answered = [r for r in ok if r["verified_claims"]]
    acc = Counter(status("\n".join(r["verified_claims"]), r["cve"]) for r in answered)
    disp = Counter(status(r["final_answer"], r["cve"]) for r in ok)
    lat = [r["latency_s"] for r in ok]
    print(f"\n===== condition: {cond}  ({len(ok)} completed of {len(rs)} runs, {len(rs)-len(ok)} errors) =====")
    print("answer rate (>=1 accepted claim)     :", g.fmt_rate(len(answered), len(ok)))
    print("accepted claims correct              :", g.fmt_rate(acc["correct"], len(answered)))
    print("accepted claims INCORRECT (false acc):", g.fmt_rate(acc["incorrect"], len(answered)))
    print("accepted claims no checkable fact    :", g.fmt_rate(acc["no_checkable_fact"], len(answered)))
    chk = acc["correct"] + acc["incorrect"]
    print("precision among checkable accepted   :", g.fmt_rate(acc["correct"], chk))
    print("displayed answer correct / incorrect :", g.fmt_rate(disp["correct"], len(ok)), "/",
          g.fmt_rate(disp["incorrect"], len(ok)))
    if lat:
        print(f"latency s: mean {statistics.mean(lat):.1f}, median {statistics.median(lat):.1f}, max {max(lat):.1f}")

    fnd = [(r, f) for r in ok for f in r["findings"]]
    tab = Counter((status(f["claim"], r["cve"]), f["confidence"]) for r, f in fnd)
    print("finding-level (claim status x decision):")
    for st in ("correct", "incorrect", "no_checkable_fact"):
        print(f"   {st:18s} verified {tab[(st,'verified')]:4d}   rejected {tab[(st,'rejected')]:4d}")
    fr = [(r, f) for r, f in fnd
          if status(f["claim"], r["cve"]) == "correct" and f["confidence"] == "rejected"]
    corr = tab[("correct", "verified")] + tab[("correct", "rejected")]
    inc = tab[("incorrect", "verified")] + tab[("incorrect", "rejected")]
    print("false reject rate (correct claims rejected):", g.fmt_rate(len(fr), corr))
    def evidence_for(r, f):
        # the "all" condition judges against every tool result, so check support the same way
        if cond == "all" and r.get("tool_results"):
            return " ".join(t["content"] for t in r["tool_results"])
        return f["evidence_excerpt"]
    prov = sum(1 for r, f in fr if not supported_by_excerpt(f["claim"], evidence_for(r, f)))
    print("  of which stated facts absent from the excerpt (provenance rejects):", f"{prov}/{len(fr)}")
    print("false accept rate (incorrect claims verified):", g.fmt_rate(tab[("incorrect", "verified")], inc))
    out[cond] = {"runs": len(rs), "completed": len(ok), "answered": len(answered), "accepted_status": dict(acc),
                 "displayed_status": dict(disp), "finding_table": {f"{a}|{b}": v for (a, b), v in tab.items()}}

json.dump(out, open("g4_summary.json", "w"), indent=2)
print("\nWrote g4_summary.json")
