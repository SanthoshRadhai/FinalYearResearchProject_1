"""
Build an offline, LLM-readable CISA Known Exploited Vulnerabilities (KEV)
knowledge base from the official feed at
https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

Mirrors the sibling *-kb/ conventions:
    entries/<CVE-ID>.md
    _index.json
    _full_corpus.md

Stdlib only:
    python build_kb.py

NOTE: unlike ATT&CK/CWE/CAPEC, this feed changes daily (new entries added
regularly). Re-run this after re-downloading raw/known_exploited_vulnerabilities.json
to refresh the KB -- there is no versioned "latest" snapshot to pin to.
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")


def build_entry_md(v: dict) -> str:
    cve = v["cveID"]
    lines = [f"# {cve}: {v.get('vulnerabilityName', '')}", ""]
    lines.append(f"**Vendor/Project:** {v.get('vendorProject', '')}  ")
    lines.append(f"**Product:** {v.get('product', '')}  ")
    lines.append(f"**Date Added to KEV:** {v.get('dateAdded', '')}  ")
    lines.append(f"**Remediation Due Date:** {v.get('dueDate', '')}  ")
    lines.append(f"**Known Ransomware Campaign Use:** {v.get('knownRansomwareCampaignUse', 'Unknown')}  ")
    cwes = v.get("cwes") or []
    if cwes:
        lines.append(f"**Related CWEs:** {', '.join(cwes)}  ")
    lines.append(f"**Reference:** https://nvd.nist.gov/vuln/detail/{cve}  ")
    lines.append("")
    lines.append("## Description")
    lines.append(v.get("shortDescription", ""))
    lines.append("")
    lines.append("## Required Action")
    lines.append(v.get("requiredAction", ""))
    lines.append("")
    if v.get("notes"):
        lines.append("## Notes / Additional References")
        lines.append(v["notes"])
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main():
    raw_path = os.path.join(RAW, "known_exploited_vulnerabilities.json")
    with open(raw_path, encoding="utf-8") as f:
        data = json.load(f)

    entries_dir = os.path.join(BASE, "entries")
    os.makedirs(entries_dir, exist_ok=True)

    index = []
    corpus_parts = [
        f"# CISA Known Exploited Vulnerabilities (KEV) Catalog\n"
        f"Catalog version: {data.get('catalogVersion')}, released {data.get('dateReleased')}, "
        f"{data.get('count')} entries.\n"
    ]

    for v in data["vulnerabilities"]:
        cve = v["cveID"]
        md = build_entry_md(v)
        out_path = os.path.join(entries_dir, f"{cve}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)

        index.append({
            "id": cve,
            "type": "kev-entry",
            "name": v.get("vulnerabilityName", ""),
            "date_added": v.get("dateAdded"),
            "ransomware_use": v.get("knownRansomwareCampaignUse"),
            "path": os.path.relpath(out_path, BASE).replace("\\", "/"),
        })
        corpus_parts.append(md)

    with open(os.path.join(BASE, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    with open(os.path.join(BASE, "_full_corpus.md"), "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(corpus_parts))

    with open(os.path.join(BASE, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump({
            "kev_entries": len(index),
            "catalog_version": data.get("catalogVersion"),
            "date_released": data.get("dateReleased"),
        }, f, indent=2)

    print(f"Done. {len(index)} KEV entries written to {entries_dir}")


if __name__ == "__main__":
    main()
