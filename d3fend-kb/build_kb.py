"""
Build an offline, LLM-readable MITRE D3FEND knowledge base from the official
JSON-LD ontology at https://d3fend.mitre.org/ontologies/d3fend.json

D3FEND is an OWL ontology, not a flat catalog like ATT&CK/CWE/CAPEC, so this
parser is a small graph resolver rather than a simple per-record loop:
  - every node (including OWL restriction blank nodes) lives in one flat
    "@graph" list, indexed here by "@id" for O(1) lookup;
  - a technique's semantic relationships (e.g. "enables: Isolate",
    "maps: Digital Identity") are expressed either directly as a property
    on the technique node, or indirectly via an `owl:Restriction` blank
    node referenced from `rdfs:subClassOf` (onProperty + someValuesFrom) --
    both forms are resolved into the same "Relationships" section below.

Produces, mirroring ../mitre-attack-kb/'s conventions:
    tactics/<Name>.md          (the 6 top-level D3FEND tactics)
    techniques/D3-<ID>__<slug>.md
    _index.json
    _full_corpus.md
    _summary.json

Stdlib only (plain json):
    python build_kb.py

Known simplification (stated plainly rather than glossed over): this build
does NOT attempt to reconstruct D3FEND's "counters ATT&CK technique X"
mapping, which the live d3fend.mitre.org site computes via a SPARQL query
over additional mapping files not present in the single ontology JSON
fetched here. What IS captured -- each technique's own definition, parent
class(es), and every direct semantic relationship the ontology encodes on
that technique's node (enables/hardens/isolates/detects/maps/etc.) -- is
real, complete ontology content, just not the specific ATT&CK cross-map.
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")

TACTIC_IDS = ["Harden", "Detect", "Isolate", "Deceive", "Evict", "Restore"]

# Keys on a technique node that are administrative/structural, not semantic
# relationships to another ontology node -- everything else matching
# "d3f:<verb>" is treated as a relation to resolve and report.
NON_RELATION_KEYS = {
    "@id", "@type", "d3f:d3fend-id", "d3f:definition", "d3f:synonym",
    "d3f:kb-article", "d3f:kb-comment", "d3f:d3fend-comment",
    "d3f:d3fend-annotation", "rdfs:label", "rdfs:comment", "rdfs:subClassOf",
    "rdfs:seeAlso", "skos:prefLabel", "d3f:contributor", "d3f:version",
    "d3f:published", "d3f:release-date", "d3f:cwe-id", "d3f:capec-id",
    "d3f:attack-id", "d3f:display-order", "d3f:display-priority",
    "d3f:display-baseurl",
}


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_")
    return s[:80]


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def label_of(node_or_ref, idx) -> str:
    """Best-effort human label for either a resolved node dict or a bare
    {"@id": ...} reference -- falls back to the bare id/value if nothing
    better is available (e.g. an external http:// @id with no local node)."""
    if not isinstance(node_or_ref, dict):
        return str(node_or_ref)
    if "@value" in node_or_ref:
        return str(node_or_ref["@value"])
    ref_id = node_or_ref.get("@id")
    if ref_id is None:
        return str(node_or_ref)
    node = idx.get(ref_id)
    if node and node.get("rdfs:label"):
        return node["rdfs:label"]
    return ref_id.split(":")[-1] if ":" in ref_id else ref_id


def relation_lines(node: dict, idx: dict) -> list[str]:
    """Collect (verb, target-label) pairs from BOTH direct properties on the
    node and owl:Restriction blank nodes referenced via rdfs:subClassOf."""
    seen = set()
    lines = []

    def add(verb: str, target_label: str):
        key = (verb, target_label)
        if key not in seen:
            seen.add(key)
            lines.append(f"- **{verb}:** {target_label}")

    for key, value in node.items():
        if key in NON_RELATION_KEYS or not key.startswith("d3f:"):
            continue
        verb = key.split(":", 1)[1]
        for ref in as_list(value):
            add(verb, label_of(ref, idx))

    for parent_ref in as_list(node.get("rdfs:subClassOf")):
        parent_id = parent_ref.get("@id") if isinstance(parent_ref, dict) else None
        if not parent_id:
            continue
        parent_node = idx.get(parent_id)
        if not parent_node:
            continue
        if parent_node.get("@type") == "owl:Restriction" or (
            isinstance(parent_node.get("@type"), list) and "owl:Restriction" in parent_node["@type"]
        ):
            prop = parent_node.get("owl:onProperty", {})
            verb = (prop.get("@id", "") if isinstance(prop, dict) else "").split(":")[-1]
            target = parent_node.get("owl:someValuesFrom", {})
            if verb and target:
                add(verb, label_of(target, idx))

    return lines


def parent_class_labels(node: dict, idx: dict) -> list[str]:
    labels = []
    for parent_ref in as_list(node.get("rdfs:subClassOf")):
        parent_id = parent_ref.get("@id") if isinstance(parent_ref, dict) else None
        if not parent_id or parent_id.startswith("_:"):
            continue
        parent_node = idx.get(parent_id)
        if parent_node and parent_node.get("rdfs:label"):
            labels.append(parent_node["rdfs:label"])
    return labels


def build_technique_md(node: dict, idx: dict) -> str:
    d3fend_id = node["d3f:d3fend-id"]
    name = node.get("rdfs:label", d3fend_id)

    lines = [f"# {d3fend_id}: {name}", ""]
    synonym = node.get("d3f:synonym")
    if synonym:
        syns = ", ".join(as_list(synonym)) if isinstance(synonym, list) else synonym
        lines.append(f"**Synonym(s):** {syns}  ")
    lines.append(f"**Reference:** https://d3fend.mitre.org/technique/{d3fend_id}/  ")
    lines.append("")

    definition = node.get("d3f:definition", "")
    if definition:
        lines.append("## Definition")
        lines.append(definition)
        lines.append("")

    parents = parent_class_labels(node, idx)
    if parents:
        lines.append("## Parent Class(es)")
        lines.extend(f"- {p}" for p in parents)
        lines.append("")

    rels = relation_lines(node, idx)
    if rels:
        lines.append("## Relationships")
        lines.extend(rels)
        lines.append("")

    kb_article = node.get("d3f:kb-article")
    if kb_article:
        lines.append("## Knowledge Base Article")
        lines.append(kb_article)
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_tactic_md(tactic_name: str, node: dict, techniques: list) -> str:
    lines = [f"# {tactic_name} (D3FEND Tactic)", ""]
    lines.append(f"**Reference:** https://d3fend.mitre.org/dao/artifact/d3f:{tactic_name}/  ")
    lines.append("")
    lines.append("## Definition")
    lines.append(node.get("d3f:definition", node.get("rdfs:comment", "")))
    lines.append("")
    if techniques:
        lines.append("## Techniques Related to This Tactic (via 'enables' relationship)")
        for t in sorted(techniques, key=lambda x: x["d3f:d3fend-id"]):
            lines.append(f"- {t['d3f:d3fend-id']}: {t.get('rdfs:label', '')}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main():
    with open(os.path.join(RAW, "d3fend.json"), encoding="utf-8") as f:
        data = json.load(f)
    graph = data["@graph"]
    idx = {n["@id"]: n for n in graph if isinstance(n, dict) and "@id" in n}
    print(f"Loaded {len(graph)} ontology nodes.")

    techniques = [
        n for n in graph
        if isinstance(n, dict) and str(n.get("d3f:d3fend-id", "")).startswith("D3-")
    ]
    print(f"Found {len(techniques)} defensive techniques (d3fend-id starting with 'D3-').")

    techniques_dir = os.path.join(BASE, "techniques")
    tactics_dir = os.path.join(BASE, "tactics")
    os.makedirs(techniques_dir, exist_ok=True)
    os.makedirs(tactics_dir, exist_ok=True)

    # Map each tactic -> techniques that have an "enables" relation to it
    # (the one direct, reliably-present per-node signal linking a technique
    # to a tactic in this ontology snapshot -- see module docstring's
    # "known simplification" note for what this does NOT capture).
    tactic_techniques = {t: [] for t in TACTIC_IDS}
    for t in techniques:
        for key in ("d3f:enables",):
            for ref in as_list(t.get(key)):
                ref_id = ref.get("@id", "") if isinstance(ref, dict) else ""
                short = ref_id.split(":")[-1]
                if short in tactic_techniques:
                    tactic_techniques[short].append(t)

    index = []
    corpus_parts = ["# MITRE D3FEND\n"]

    for tactic_name in TACTIC_IDS:
        node = idx.get(f"d3f:{tactic_name}", {})
        md = build_tactic_md(tactic_name, node, tactic_techniques[tactic_name])
        out_path = os.path.join(tactics_dir, f"{tactic_name}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
        index.append({
            "id": tactic_name, "type": "tactic", "name": tactic_name,
            "path": os.path.relpath(out_path, BASE).replace("\\", "/"),
        })
        corpus_parts.append(md)

    for t in techniques:
        d3fend_id = t["d3f:d3fend-id"]
        name = t.get("rdfs:label", d3fend_id)
        md = build_technique_md(t, idx)
        fname = f"{d3fend_id}__{slugify(name)}.md"
        out_path = os.path.join(techniques_dir, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)
        index.append({
            "id": d3fend_id, "type": "technique", "name": name,
            "path": os.path.relpath(out_path, BASE).replace("\\", "/"),
        })
        corpus_parts.append(md)

    with open(os.path.join(BASE, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    with open(os.path.join(BASE, "_full_corpus.md"), "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(corpus_parts))

    with open(os.path.join(BASE, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump({"tactics": len(TACTIC_IDS), "techniques": len(techniques)}, f, indent=2)

    print(f"Done. {len(TACTIC_IDS)} tactics + {len(techniques)} techniques written.")


if __name__ == "__main__":
    main()
