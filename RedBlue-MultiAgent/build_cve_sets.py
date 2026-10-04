"""Builds the held-out CVE set for the Evaluator on/off study (paper gaps G4,
M1, M3) with NVD ground truth. Reproducible (fixed seed), excludes the 8 CVEs
used while developing and debugging the agent, and deliberately samples
beyond famous CVEs:

  * KEV pool: random entries of the CISA KEV catalogue (local snapshot in
    ../cisa-kev-kb/raw/), which are mostly vendor-specific, not household names.
  * non-KEV pool: random NVD records drawn from random 119-day publication
    windows, 40% of them from 2025-07 onward so recent CVEs are covered.

Output: g4_cves.json. The first N_EVAL_KEV + N_EVAL_NONKEV entries are the
"eval" set used for the agent on/off runs; the rest ("m3_only") only feed the
claim-pair benchmark. Needs network access to NVD and ~15 minutes (public API
rate limit). Run on any Python 3: `python build_cve_sets.py`.
"""

import datetime as dt
import json
import random
import sys
import time
from pathlib import Path

import g4_common as g

SEED = 42
N_KEV = 30
N_NONKEV = 50
N_EVAL_KEV = 20
N_EVAL_NONKEV = 30
DEV_CVES = {
    "CVE-2024-3400", "CVE-2026-9862", "CVE-2021-44228", "CVE-2023-4863",
    "CVE-2020-1472", "CVE-2017-5638", "CVE-2019-0708", "CVE-2022-30190",
    "CVE-2017-0144", "CVE-2014-0160", "CVE-2026-90829",
}
KEV_PATH = Path(__file__).resolve().parent.parent / "cisa-kev-kb" / "raw" / "known_exploited_vulnerabilities.json"
OUT = Path(__file__).resolve().parent / "g4_cves.json"

rng = random.Random(SEED)
kev_doc = json.load(open(KEV_PATH, encoding="utf-8"))
kev_ids = {v["cveID"] for v in kev_doc["vulnerabilities"]}


def fetch_one(cve_id):
    d = g.nvd_get({"cveId": cve_id})
    time.sleep(g.NVD_SLEEP_S)
    vulns = d.get("vulnerabilities", [])
    return vulns[0]["cve"] if vulns else None


def usable(cve):
    t = g.truth_from_record(cve)
    return t if t["scores"] and t["vuln_status"] != "Rejected" else None


def sample_kev():
    pool = [c for c in sorted(kev_ids) if c not in DEV_CVES]
    rng.shuffle(pool)
    out = []
    for cid in pool:
        if len(out) >= N_KEV:
            break
        cve = fetch_one(cid)
        t = usable(cve) if cve else None
        if t:
            t["in_kev"] = True
            t["pool"] = "kev"
            out.append(t)
            print(f"  kev {len(out)}/{N_KEV}: {cid}", flush=True)
    return out


def random_window():
    if rng.random() < 0.4:
        lo, hi = dt.date(2025, 7, 1), dt.date(2026, 8, 25)
    else:
        lo, hi = dt.date(2019, 1, 1), dt.date(2025, 6, 30)
    start = lo + dt.timedelta(days=rng.randrange((hi - lo).days))
    end = start + dt.timedelta(days=119)
    return start, end


def sample_nonkev():
    out, seen = [], set()
    while len(out) < N_NONKEV:
        start, end = random_window()
        base = {"pubStartDate": f"{start}T00:00:00.000", "pubEndDate": f"{end}T23:59:59.999"}
        head = g.nvd_get({**base, "resultsPerPage": 1})
        time.sleep(g.NVD_SLEEP_S)
        total = head.get("totalResults", 0)
        if total < 1:
            continue
        idx = rng.randrange(total)
        d = g.nvd_get({**base, "resultsPerPage": 1, "startIndex": idx})
        time.sleep(g.NVD_SLEEP_S)
        vulns = d.get("vulnerabilities", [])
        if not vulns:
            continue
        cve = vulns[0]["cve"]
        cid = cve["id"]
        if cid in kev_ids or cid in DEV_CVES or cid in seen:
            continue
        t = usable(cve)
        if not t:
            continue
        seen.add(cid)
        t["in_kev"] = False
        t["pool"] = "nonkev"
        out.append(t)
        print(f"  nonkev {len(out)}/{N_NONKEV}: {cid} (published {t['published'][:10]})", flush=True)
    return out


def main():
    print(f"KEV catalogue {kev_doc['catalogVersion']} ({len(kev_ids)} entries), seed {SEED}")
    kev = sample_kev()
    nonkev = sample_nonkev()
    for i, t in enumerate(kev):
        t["set"] = "eval" if i < N_EVAL_KEV else "m3_only"
    for i, t in enumerate(nonkev):
        t["set"] = "eval" if i < N_EVAL_NONKEV else "m3_only"
    doc = {
        "seed": SEED, "built": dt.datetime.now().isoformat(timespec="seconds"),
        "kev_catalog_version": kev_doc["catalogVersion"], "excluded_dev_cves": sorted(DEV_CVES),
        "n_eval": N_EVAL_KEV + N_EVAL_NONKEV, "cves": kev + nonkev,
    }
    json.dump(doc, open(OUT, "w", encoding="utf-8"), indent=2)
    n_recent = sum(1 for t in doc["cves"] if t["published"] >= "2025-07-01")
    print(f"Wrote {OUT} with {len(doc['cves'])} CVEs ({sum(1 for t in doc['cves'] if t['set']=='eval')} eval, "
          f"{n_recent} published since 2025-07).")


if __name__ == "__main__":
    sys.exit(main())
