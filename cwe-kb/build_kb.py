"""
Build an offline, LLM-readable MITRE CWE (Common Weakness Enumeration)
knowledge base from the official XML catalog at
https://cwe.mitre.org/data/xml/cwec_latest.xml.zip

Mirrors the layout/conventions of ../mitre-attack-kb/build_kb.py:
    weaknesses/CWE-<id>__<slug>.md
    _index.json
    _full_corpus.md

Run inside the `hexstrike` (or any) conda env with the stdlib only
(xml.etree.ElementTree) -- no extra dependencies:
    python build_kb.py
"""
import json
import os
import re
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")
NS = {"cwe": "http://cwe.mitre.org/cwe-7"}


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_")
    return s[:80]


def text_of(elem) -> str:
    """Flattened text of an element and all its children (handles the mixed
    xhtml: markup CWE uses for formatted description/mitigation text)."""
    if elem is None:
        return ""
    return " ".join("".join(elem.itertext()).split())


def find_xml_file():
    for fname in os.listdir(RAW):
        if fname.startswith("cwec_") and fname.endswith(".xml"):
            return os.path.join(RAW, fname)
    raise FileNotFoundError("No cwec_*.xml found in raw/ -- download cwec_latest.xml.zip first")


def build_weakness_md(w) -> str:
    cwe_id = w.get("ID")
    name = w.get("Name")
    abstraction = w.get("Abstraction", "")
    status = w.get("Status", "")

    lines = [f"# CWE-{cwe_id}: {name}", ""]
    lines.append(f"**Abstraction:** {abstraction}  ")
    lines.append(f"**Status:** {status}  ")
    lines.append(f"**Reference:** https://cwe.mitre.org/data/definitions/{cwe_id}.html  ")
    lines.append("")

    desc = text_of(w.find("cwe:Description", NS))
    if desc:
        lines.append("## Description")
        lines.append(desc)
        lines.append("")

    ext_desc = text_of(w.find("cwe:Extended_Description", NS))
    if ext_desc:
        lines.append("## Extended Description")
        lines.append(ext_desc)
        lines.append("")

    related = w.find("cwe:Related_Weaknesses", NS)
    if related is not None:
        rels = []
        for r in related.findall("cwe:Related_Weakness", NS):
            rels.append(f"- {r.get('Nature')}: CWE-{r.get('CWE_ID')}")
        if rels:
            lines.append("## Related Weaknesses")
            lines.extend(rels)
            lines.append("")

    consequences = w.find("cwe:Common_Consequences", NS)
    if consequences is not None:
        items = []
        for c in consequences.findall("cwe:Consequence", NS):
            scopes = [s.text for s in c.findall("cwe:Scope", NS) if s.text]
            impacts = [i.text for i in c.findall("cwe:Impact", NS) if i.text]
            note = text_of(c.find("cwe:Note", NS))
            line = f"- Scope: {', '.join(scopes) or '(unspecified)'}; Impact: {', '.join(impacts) or '(unspecified)'}"
            if note:
                line += f" — {note}"
            items.append(line)
        if items:
            lines.append("## Common Consequences")
            lines.extend(items)
            lines.append("")

    mitigations = w.find("cwe:Potential_Mitigations", NS)
    if mitigations is not None:
        items = []
        for m in mitigations.findall("cwe:Mitigation", NS):
            phases = [p.text for p in m.findall("cwe:Phase", NS) if p.text]
            desc_m = text_of(m.find("cwe:Description", NS))
            if desc_m:
                prefix = f"[{', '.join(phases)}] " if phases else ""
                items.append(f"- {prefix}{desc_m}")
        if items:
            lines.append("## Potential Mitigations")
            lines.extend(items)
            lines.append("")

    detection = w.find("cwe:Detection_Methods", NS)
    if detection is not None:
        items = []
        for d in detection.findall("cwe:Detection_Method", NS):
            method = d.find("cwe:Method", NS)
            desc_d = text_of(d.find("cwe:Description", NS))
            if desc_d:
                prefix = f"[{method.text}] " if method is not None and method.text else ""
                items.append(f"- {prefix}{desc_d}")
        if items:
            lines.append("## Detection Methods")
            lines.extend(items)
            lines.append("")

    examples = w.find("cwe:Demonstrative_Examples", NS)
    if examples is not None:
        intros = []
        for ex in examples.findall("cwe:Demonstrative_Example", NS):
            intro = text_of(ex.find("cwe:Intro_Text", NS))
            if intro:
                intros.append(f"- {intro}")
        if intros:
            lines.append("## Demonstrative Examples (summary)")
            lines.extend(intros)
            lines.append("")

    return "\n".join(lines).strip() + "\n"


def main():
    xml_path = find_xml_file()
    print(f"Parsing {xml_path} ...")
    tree = ET.parse(xml_path)
    root = tree.getroot()

    weaknesses_dir = os.path.join(BASE, "weaknesses")
    os.makedirs(weaknesses_dir, exist_ok=True)

    index = []
    corpus_parts = ["# MITRE CWE (Common Weakness Enumeration)\n"]

    weaknesses = root.find("cwe:Weaknesses", NS)
    for w in weaknesses.findall("cwe:Weakness", NS):
        cwe_id = w.get("ID")
        name = w.get("Name")
        md = build_weakness_md(w)
        fname = f"CWE-{cwe_id}__{slugify(name)}.md"
        out_path = os.path.join(weaknesses_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)

        index.append({
            "id": f"CWE-{cwe_id}",
            "type": "weakness",
            "name": name,
            "abstraction": w.get("Abstraction"),
            "path": os.path.relpath(out_path, BASE).replace("\\", "/"),
        })
        corpus_parts.append(md)

    with open(os.path.join(BASE, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    with open(os.path.join(BASE, "_full_corpus.md"), "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(corpus_parts))

    summary = {"weaknesses": len(index)}
    with open(os.path.join(BASE, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Done. {len(index)} weaknesses written to {weaknesses_dir}")


if __name__ == "__main__":
    main()
