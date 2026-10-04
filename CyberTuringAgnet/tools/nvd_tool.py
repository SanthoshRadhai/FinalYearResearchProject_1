"""NVD REST API lookup — plain HTTP call, no MCP server, no browser needed.

This is the "CVE-ID-known fast path" from Research-Paper resources/
07-...ARCHITECTURE.md §5.1 — already proven working in Langchain/
4_langchain_stealth_llamacpp_CVE_Agent.py. Ported here unchanged in spirit: a
direct httpx call, not a browse-and-scrape task.
"""

import httpx
from langchain_core.tools import tool

NVD_CVE_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"


@tool
def lookup_cve(cve_id: str) -> dict:
    """Look up a CVE by ID directly against the NVD REST API (ground truth,
    not a search engine snippet). Use this whenever the CVE ID is already
    known — it is faster and more reliable than browsing nvd.nist.gov.

    Args:
        cve_id: e.g. "CVE-2026-9862".

    Returns:
        dict with keys: cve_id, description, cvss_vector, cvss_version,
        base_score, severity, references (list of URLs), or
        {"error": "..."} if the lookup failed or the ID doesn't exist.
    """
    cve_id = cve_id.strip().upper()
    try:
        resp = httpx.get(NVD_CVE_API, params={"cveId": cve_id}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return {"error": f"NVD API request failed for {cve_id}: {e}"}

    vulns = data.get("vulnerabilities", [])
    if not vulns:
        return {"error": f"{cve_id} not found in NVD"}

    cve = vulns[0]["cve"]
    description = next(
        (d["value"] for d in cve.get("descriptions", []) if d.get("lang") == "en"),
        "(no English description)",
    )

    metrics = cve.get("metrics", {})
    cvss_vector, cvss_version, base_score, severity = None, None, None, None
    for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        if key in metrics and metrics[key]:
            m = metrics[key][0]["cvssData"]
            cvss_vector = m.get("vectorString")
            cvss_version = m.get("version")
            base_score = m.get("baseScore")
            severity = m.get("baseSeverity", metrics[key][0].get("baseSeverity"))
            break

    references = [r["url"] for r in cve.get("references", [])]

    return {
        "cve_id": cve_id,
        "description": description,
        "cvss_vector": cvss_vector,
        "cvss_version": cvss_version,
        "base_score": base_score,
        "severity": severity,
        "references": references,
    }
