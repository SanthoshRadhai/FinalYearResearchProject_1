"""
Build an offline, LLM-readable MITRE CAPEC (Common Attack Pattern Enumeration
and Classification) knowledge base from the official XML catalog at
https://capec.mitre.org/data/xml/capec_latest.xml

Mirrors ../mitre-attack-kb/build_kb.py and ../cwe-kb/build_kb.py's
conventions:
    patterns/CAPEC-<id>__<slug>.md
    _index.json
    _full_corpus.md

Stdlib only (xml.etree.ElementTree):
    python build_kb.py
"""
import json
import os
import re
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")
NS = {"c": "http://capec.mitre.org/capec-3"}


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_")
    return s[:80]


def text_of(elem) -> str:
    if elem is None:
        return ""
    return " ".join("".join(elem.itertext()).split())


def build_pattern_md(ap) -> str:
    capec_id = ap.get("ID")
    name = ap.get("Name")
    abstraction = ap.get("Abstraction", "")
    status = ap.get("Status", "")

    lines = [f"# CAPEC-{capec_id}: {name}", ""]
    lines.append(f"**Abstraction:** {abstraction}  ")
    lines.append(f"**Status:** {status}  ")
    likelihood = ap.find("c:Likelihood_Of_Attack", NS)
    severity = ap.find("c:Typical_Severity", NS)
    if likelihood is not None and likelihood.text:
        lines.append(f"**Likelihood of Attack:** {likelihood.text}  ")
    if severity is not None and severity.text:
        lines.append(f"**Typical Severity:** {severity.text}  ")
    lines.append(f"**Reference:** https://capec.mitre.org/data/definitions/{capec_id}.html  ")
    lines.append("")

    desc = text_of(ap.find("c:Description", NS))
    if desc:
        lines.append("## Description")
        lines.append(desc)
        lines.append("")

    related = ap.find("c:Related_Attack_Patterns", NS)
    if related is not None:
        rels = [f"- {r.get('Nature')}: CAPEC-{r.get('CAPEC_ID')}" for r in related.findall("c:Related_Attack_Pattern", NS)]
        if rels:
            lines.append("## Related Attack Patterns")
            lines.extend(rels)
            lines.append("")

    prereqs = ap.find("c:Prerequisites", NS)
    if prereqs is not None:
        items = [f"- {text_of(p)}" for p in prereqs.findall("c:Prerequisite", NS) if text_of(p)]
        if items:
            lines.append("## Prerequisites")
            lines.extend(items)
            lines.append("")

    skills = ap.find("c:Skills_Required", NS)
    if skills is not None:
        items = [f"- [{s.get('Level', '')}] {text_of(s)}" for s in skills.findall("c:Skill", NS) if text_of(s)]
        if items:
            lines.append("## Skills Required")
            lines.extend(items)
            lines.append("")

    resources = ap.find("c:Resources_Required", NS)
    if resources is not None:
        items = [f"- {text_of(r)}" for r in resources.findall("c:Resource", NS) if text_of(r)]
        if items:
            lines.append("## Resources Required")
            lines.extend(items)
            lines.append("")

    consequences = ap.find("c:Consequences", NS)
    if consequences is not None:
        items = []
        for c in consequences.findall("c:Consequence", NS):
            scopes = [s.text for s in c.findall("c:Scope", NS) if s.text]
            impacts = [i.text for i in c.findall("c:Impact", NS) if i.text]
            items.append(f"- Scope: {', '.join(scopes) or '(unspecified)'}; Impact: {', '.join(impacts) or '(unspecified)'}")
        if items:
            lines.append("## Consequences")
            lines.extend(items)
            lines.append("")

    mitigations = ap.find("c:Mitigations", NS)
    if mitigations is not None:
        items = [f"- {text_of(m)}" for m in mitigations.findall("c:Mitigation", NS) if text_of(m)]
        if items:
            lines.append("## Mitigations")
            lines.extend(items)
            lines.append("")

    related_cwe = ap.find("c:Related_Weaknesses", NS)
    if related_cwe is not None:
        items = [f"- CWE-{rw.get('CWE_ID')}" for rw in related_cwe.findall("c:Related_Weakness", NS)]
        if items:
            lines.append("## Related Weaknesses (CWE)")
            lines.extend(items)
            lines.append("")

    return "\n".join(lines).strip() + "\n"


def main():
    xml_path = os.path.join(RAW, "capec_latest.xml")
    print(f"Parsing {xml_path} ...")
    tree = ET.parse(xml_path)
    root = tree.getroot()

    patterns_dir = os.path.join(BASE, "patterns")
    os.makedirs(patterns_dir, exist_ok=True)

    index = []
    corpus_parts = ["# MITRE CAPEC (Common Attack Pattern Enumeration and Classification)\n"]

    patterns = root.find("c:Attack_Patterns", NS)
    for ap in patterns.findall("c:Attack_Pattern", NS):
        capec_id = ap.get("ID")
        name = ap.get("Name")
        md = build_pattern_md(ap)
        fname = f"CAPEC-{capec_id}__{slugify(name)}.md"
        out_path = os.path.join(patterns_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)

        index.append({
            "id": f"CAPEC-{capec_id}",
            "type": "attack-pattern",
            "name": name,
            "abstraction": ap.get("Abstraction"),
            "path": os.path.relpath(out_path, BASE).replace("\\", "/"),
        })
        corpus_parts.append(md)

    with open(os.path.join(BASE, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    with open(os.path.join(BASE, "_full_corpus.md"), "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(corpus_parts))

    with open(os.path.join(BASE, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump({"attack_patterns": len(index)}, f, indent=2)

    print(f"Done. {len(index)} attack patterns written to {patterns_dir}")


if __name__ == "__main__":
    main()
