"""Shared helpers for the Evaluator on/off study (paper gaps G4, M1, M3):
NVD ground truth, deterministic claim checking, and Wilson intervals.

Everything here is deterministic -- no LLM judge decides whether a claim is
correct. A claim is checked only on facts that NVD / the CISA KEV catalogue
settle: the CVSS base score, the severity label, and KEV membership. Claims
that state none of these are reported separately as "no_checkable_fact".

Pure standard library so the CVE-set builder runs on any Python.
"""

import json
import math
import re
import time
import urllib.parse
import urllib.request

NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0"
NVD_SLEEP_S = 6.5  # public NVD API limit: 5 requests per rolling 30 s without a key
SEVERITIES = ("CRITICAL", "HIGH", "MEDIUM", "LOW")
MAX_EXCERPT_CHARS = 800  # same cut agents/common.py applies to the evidence excerpt

OBJECTIVE_TEMPLATE = (
    "Look up {cve}. State its CVSS base score and severity, and say whether it "
    "is in the CISA KEV catalog."
)


def nvd_get(params, retries=4):
    url = NVD + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "redblue-g4/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 - network flakiness, retry with backoff
            last = e
            time.sleep(10 * (attempt + 1))
    raise RuntimeError(f"NVD request failed: {last}")


def truth_from_record(cve):
    """Ground truth from one NVD `cve` object. `tool_dict` reproduces what
    tools/nvd_tool.py's lookup_cve returns (first metric of the first
    available version), which is what the agent actually sees."""
    metrics = cve.get("metrics", {})
    scores = []
    tool_dict = None
    for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        for i, m in enumerate(metrics.get(key, [])):
            d = m.get("cvssData", {})
            if d.get("baseScore") is None:
                continue
            sev = (d.get("baseSeverity") or m.get("baseSeverity") or "").upper()
            scores.append({"metric": key, "score": float(d["baseScore"]), "severity": sev,
                           "vector": d.get("vectorString"), "source": m.get("source"), "type": m.get("type")})
            if tool_dict is None and i == 0:
                tool_dict = {
                    "base_score": d.get("baseScore"), "severity": d.get("baseSeverity", m.get("baseSeverity")),
                    "cvss_vector": d.get("vectorString"), "cvss_version": d.get("version"),
                }
    desc = next((x["value"] for x in cve.get("descriptions", []) if x.get("lang") == "en"),
                "(no English description)")
    refs = [r["url"] for r in cve.get("references", [])]
    full_tool = {
        "cve_id": cve["id"], "description": desc,
        "cvss_vector": (tool_dict or {}).get("cvss_vector"), "cvss_version": (tool_dict or {}).get("cvss_version"),
        "base_score": (tool_dict or {}).get("base_score"), "severity": (tool_dict or {}).get("severity"),
        "references": refs,
    }
    return {
        "cve_id": cve["id"], "published": cve.get("published"), "vuln_status": cve.get("vulnStatus"),
        "description": desc, "scores": scores, "tool_excerpt": str(full_tool)[:MAX_EXCERPT_CHARS],
        "nvd_kev_date": cve.get("cisaExploitAdd"),
    }


# ----------------------------------------------------------------- claim parsing
_SCORE_RES = [
    re.compile(r"(?:base\s*score|cvss[^.\n]{0,25}?score|score)[^0-9]{0,40}?(10\.0|\d\.\d)", re.I),
    re.compile(r"(10\.0|\d\.\d)\s*/\s*10"),
    re.compile(r"(10\.0|\d\.\d)\s*\(?\s*(?:critical|high|medium|low)\b", re.I),
]
_SEV_RES = [
    re.compile(r"severity[^A-Za-z]{0,20}(critical|high|medium|low)\b", re.I),
    re.compile(r"\d\.\d\s*\(?\s*(critical|high|medium|low)\b", re.I),
    re.compile(r"\b(critical|high|medium|low)\s+severity\b", re.I),
]
_KEV_MENTION = re.compile(r"\bKEV\b|Known[\s\u2010-\u2015-]*Exploited Vulnerabilit", re.I)
# per-line cues; a line that mentions KEV is classified negative if ANY negative cue matches
_KEV_NEG_LINE = re.compile(
    r"[|:]\s*\*{0,2}\s*No\b"                                  # table cell / label answering "No"
    r"|\bno\s+(?:matches|results|entry|record|listing)\b"
    r"|\b(?:not|never|isn't|is not|wasn't)\s+(?:currently\s+)?(?:listed|included|present|found|in|a\s+member)\b"
    r"|\bnot\s+(?:in|on|part of)\b|\babsent\b|\bdoes\s+not\s+(?:list|include)\b|did\s+not\s+return",
    re.I,
)
_KEV_POS_LINE = re.compile(
    r"[|:]\s*\*{0,2}\s*Yes\b|\b(?:is|are|was)\s+(?:also\s+)?(?:listed|included|present|in)\b"
    r"|\blisted\b|\badded\b|\bincluded\b|\bappears?\b",
    re.I,
)


def _kev_stance(text):
    """None if KEV is not discussed; False/True for stated non-membership/membership."""
    pos = neg = False
    for line in text.split("\n"):
        if not _KEV_MENTION.search(line):
            continue
        if _KEV_NEG_LINE.search(line):
            neg = True
        elif _KEV_POS_LINE.search(line):
            pos = True
    if neg:
        return False
    return True if pos else None


def parse_claim(text):
    text = text or ""
    scores = []
    for rx in _SCORE_RES:
        for m in rx.finditer(text):
            v = float(m.group(1))
            before = text[max(0, m.start(1) - 9):m.start(1)].lower()
            if re.search(r"cvss\s*:?\s*(?:v|version)?\s*$|\bv\s*$|version\s*$", before):
                continue  # a CVSS version string such as "CVSS 3.1", not a score
            if 0.0 <= v <= 10.0 and v not in scores:
                scores.append(v)
    sevs = []
    for rx in _SEV_RES:
        for m in rx.finditer(text):
            v = m.group(1).upper()
            if v not in sevs:
                sevs.append(v)
    kev = _kev_stance(text)
    return {"scores": scores, "severities": sevs, "kev": kev}


def check_claim(text, truth, in_kev):
    """Check the facts a claim states against ground truth. Returns
    {status, n_checkable, n_wrong, parsed}; status is one of
    correct | incorrect | no_checkable_fact."""
    p = parse_claim(text)
    true_scores = [s["score"] for s in truth["scores"]]
    true_sevs = {s["severity"] for s in truth["scores"]}
    n_checkable = n_wrong = 0
    for v in p["scores"]:
        n_checkable += 1
        if not any(abs(v - t) < 0.05 for t in true_scores):
            n_wrong += 1
    for v in p["severities"]:
        n_checkable += 1
        if v not in true_sevs:
            n_wrong += 1
    if p["kev"] is not None:
        n_checkable += 1
        if p["kev"] != bool(in_kev):
            n_wrong += 1
    status = "incorrect" if n_wrong else ("correct" if n_checkable else "no_checkable_fact")
    return {"status": status, "n_checkable": n_checkable, "n_wrong": n_wrong, "parsed": p}


def severity_of(score):
    if score >= 9.0:
        return "CRITICAL"
    if score >= 7.0:
        return "HIGH"
    if score >= 4.0:
        return "MEDIUM"
    return "LOW"


def wilson(k, n, z=1.959964):
    """95% Wilson score interval for k successes out of n (returns (lo, hi) in [0,1])."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def fmt_rate(k, n):
    if n == 0:
        return "n/a (0 of 0)"
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {100*k/n:.1f}% [{100*lo:.1f}, {100*hi:.1f}]"
