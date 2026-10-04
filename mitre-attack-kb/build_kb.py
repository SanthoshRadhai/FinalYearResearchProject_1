"""
Build an offline, LLM-readable MITRE ATT&CK knowledge base from the official
STIX 2.1 bundles published at https://github.com/mitre/cti.

For each domain (enterprise / mobile / ics) this produces, under
mitre-attack-kb/<domain>/:
    tactics/<TAxxxx>__<name>.md
    techniques/<Txxxx[.xxx]>__<name>.md
    mitigations/<Mxxxx>__<name>.md
    groups/<Gxxxx>__<name>.md
    software/<Sxxxx>__<name>.md
    campaigns/<Cxxxx>__<name>.md
    data_sources/<DSxxxx>__<name>.md
    _index.json                (machine-readable index of every object)
    _full_corpus.md            (single concatenated file, for simple RAG/context stuffing)

Run inside the `mitre-kb` conda env:
    conda run -n mitre-kb python build_kb.py
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw")

DOMAINS = {
    "enterprise": "enterprise-attack.json",
    "mobile": "mobile-attack.json",
    "ics": "ics-attack.json",
}

TYPE_DIR = {
    "x-mitre-tactic": "tactics",
    "attack-pattern": "techniques",
    "course-of-action": "mitigations",
    "intrusion-set": "groups",
    "malware": "software",
    "tool": "software",
    "campaign": "campaigns",
    "x-mitre-data-source": "data_sources",
}

def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_")
    return s[:80]


def get_attack_id(obj) -> str | None:
    for ref in obj.get("external_references", []):
        if ref.get("source_name") in ("mitre-attack", "mitre-mobile-attack", "mitre-ics-attack"):
            return ref.get("external_id")
    return None


def get_url(obj) -> str | None:
    for ref in obj.get("external_references", []):
        if ref.get("source_name") in ("mitre-attack", "mitre-mobile-attack", "mitre-ics-attack"):
            return ref.get("url")
    return None


def load_bundle(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)["objects"]


def index_by_id(objects):
    return {o["id"]: o for o in objects if "id" in o}


def relationships_for(objects):
    rels = [o for o in objects if o.get("type") == "relationship"]
    by_source = {}
    by_target = {}
    for r in rels:
        by_source.setdefault(r["source_ref"], []).append(r)
        by_target.setdefault(r["target_ref"], []).append(r)
    return by_source, by_target


def name_of(obj):
    if not obj:
        return "Unknown"
    return obj.get("name", obj.get("id", "Unknown"))


def build_technique_md(obj, by_id, by_source, by_target, kill_chain_name):
    attack_id = get_attack_id(obj)
    name = obj["name"]
    url = get_url(obj)
    is_sub = "." in (attack_id or "")
    parent_line = ""
    if is_sub:
        parent_id = attack_id.split(".")[0]
        parent_line = f"**Parent technique:** {parent_id}\n\n"

    tactics = [kc["phase_name"] for kc in obj.get("kill_chain_phases", []) if kc.get("kill_chain_name") == kill_chain_name]
    platforms = obj.get("x_mitre_platforms", [])
    data_sources = obj.get("x_mitre_data_sources", [])
    detection = obj.get("x_mitre_detection", "")
    deprecated = obj.get("x_mitre_deprecated", False)
    revoked = obj.get("revoked", False)

    mitigations = []
    groups_using = []
    software_using = []
    sub_techniques = []

    for r in by_target.get(obj["id"], []):
        src = by_id.get(r["source_ref"])
        if not src:
            continue
        if r["relationship_type"] == "mitigates" and src.get("type") == "course-of-action":
            mitigations.append(src)
        elif r["relationship_type"] == "uses":
            if src.get("type") == "intrusion-set":
                groups_using.append(src)
            elif src.get("type") in ("malware", "tool"):
                software_using.append(src)
        elif r["relationship_type"] == "subtechnique-of":
            pass

    for r in by_source.get(obj["id"], []):
        tgt = by_id.get(r["target_ref"])
        if tgt and r["relationship_type"] == "subtechnique-of":
            pass

    if not is_sub:
        for other in by_id.values():
            if other.get("type") == "attack-pattern":
                for r in by_source.get(other["id"], []):
                    if r["relationship_type"] == "subtechnique-of" and r["target_ref"] == obj["id"]:
                        sub_techniques.append(other)

    lines = [f"# {attack_id}: {name}", ""]
    if deprecated or revoked:
        lines.append("> **Status:** " + ("Deprecated" if deprecated else "Revoked") + "\n")
    lines.append(parent_line.strip())
    lines.append(f"**ATT&CK ID:** {attack_id}  ")
    lines.append(f"**Domain:** {kill_chain_name.replace('-', ' ').title()}  ")
    if tactics:
        lines.append(f"**Tactic(s):** {', '.join(t.replace('-', ' ').title() for t in tactics)}  ")
    if platforms:
        lines.append(f"**Platforms:** {', '.join(platforms)}  ")
    if url:
        lines.append(f"**Reference:** {url}  ")
    lines.append("")
    lines.append("## Description")
    lines.append(obj.get("description", "").strip())
    lines.append("")

    if sub_techniques:
        lines.append("## Sub-techniques")
        for st in sorted(sub_techniques, key=lambda x: get_attack_id(x) or ""):
            lines.append(f"- {get_attack_id(st)}: {st['name']}")
        lines.append("")

    if data_sources:
        lines.append("## Data Sources")
        for ds in data_sources:
            lines.append(f"- {ds}")
        lines.append("")

    if detection:
        lines.append("## Detection")
        lines.append(detection.strip())
        lines.append("")

    if mitigations:
        lines.append("## Mitigations")
        for m in sorted(mitigations, key=lambda x: get_attack_id(x) or ""):
            lines.append(f"- {get_attack_id(m)}: {m['name']}")
        lines.append("")

    if groups_using:
        lines.append("## Known Threat Groups Using This Technique")
        for g in sorted(groups_using, key=lambda x: x["name"]):
            lines.append(f"- {get_attack_id(g)}: {g['name']}")
        lines.append("")

    if software_using:
        lines.append("## Known Software Using This Technique")
        for s in sorted(software_using, key=lambda x: x["name"]):
            lines.append(f"- {get_attack_id(s)}: {s['name']}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_generic_md(obj, by_id, by_source, by_target):
    attack_id = get_attack_id(obj) or obj.get("id")
    name = obj["name"]
    url = get_url(obj)
    otype = obj["type"]

    lines = [f"# {attack_id}: {name}", ""]
    lines.append(f"**Type:** {otype}  ")
    if url:
        lines.append(f"**Reference:** {url}  ")
    aliases = obj.get("aliases") or obj.get("x_mitre_aliases")
    if aliases:
        lines.append(f"**Aliases:** {', '.join(aliases)}  ")
    platforms = obj.get("x_mitre_platforms")
    if platforms:
        lines.append(f"**Platforms:** {', '.join(platforms)}  ")
    lines.append("")
    lines.append("## Description")
    lines.append((obj.get("description") or "").strip())
    lines.append("")

    if otype == "course-of-action":
        used_for = []
        for r in by_target.get(obj["id"], []):
            pass
        mitigates = []
        for r in by_source.get(obj["id"], []):
            if r["relationship_type"] == "mitigates":
                tgt = by_id.get(r["target_ref"])
                if tgt:
                    mitigates.append(tgt)
        if mitigates:
            lines.append("## Techniques Mitigated")
            for t in sorted(mitigates, key=lambda x: get_attack_id(x) or ""):
                lines.append(f"- {get_attack_id(t)}: {t['name']}")
            lines.append("")

    if otype == "intrusion-set":
        used = []
        for r in by_source.get(obj["id"], []):
            if r["relationship_type"] == "uses":
                tgt = by_id.get(r["target_ref"])
                if tgt and tgt.get("type") == "attack-pattern":
                    used.append(tgt)
        if used:
            lines.append("## Techniques Used")
            for t in sorted(used, key=lambda x: get_attack_id(x) or ""):
                lines.append(f"- {get_attack_id(t)}: {t['name']}")
            lines.append("")

    if otype in ("malware", "tool"):
        used = []
        for r in by_source.get(obj["id"], []):
            if r["relationship_type"] == "uses":
                tgt = by_id.get(r["target_ref"])
                if tgt and tgt.get("type") == "attack-pattern":
                    used.append(tgt)
        if used:
            lines.append("## Techniques Used")
            for t in sorted(used, key=lambda x: get_attack_id(x) or ""):
                lines.append(f"- {get_attack_id(t)}: {t['name']}")
            lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_tactic_md(obj, by_id, objects, kill_chain_name):
    attack_id = get_attack_id(obj)
    name = obj["name"]
    shortname = obj.get("x_mitre_shortname")
    lines = [f"# {attack_id}: {name}", ""]
    lines.append(f"**Type:** Tactic  ")
    url = get_url(obj)
    if url:
        lines.append(f"**Reference:** {url}  ")
    lines.append("")
    lines.append("## Description")
    lines.append((obj.get("description") or "").strip())
    lines.append("")

    techniques = []
    for o in objects:
        if o.get("type") != "attack-pattern" or o.get("revoked") or o.get("x_mitre_deprecated"):
            continue
        for kc in o.get("kill_chain_phases", []):
            if kc.get("kill_chain_name") == kill_chain_name and kc.get("phase_name") == shortname:
                techniques.append(o)
                break

    if techniques:
        lines.append("## Techniques in This Tactic")
        for t in sorted(techniques, key=lambda x: get_attack_id(x) or ""):
            lines.append(f"- {get_attack_id(t)}: {t['name']}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main():
    domain_kc = {
        "enterprise": "mitre-attack",
        "mobile": "mitre-mobile-attack",
        "ics": "mitre-ics-attack",
    }

    global_index = {}

    for domain, fname in DOMAINS.items():
        path = os.path.join(RAW, fname)
        if not os.path.exists(path):
            print(f"skip {domain}: {fname} not found")
            continue
        print(f"Processing {domain} ...")
        objects = load_bundle(path)
        by_id = index_by_id(objects)
        by_source, by_target = relationships_for(objects)
        kc_name = domain_kc[domain]

        domain_root = os.path.join(BASE, domain)
        for sub in TYPE_DIR.values():
            os.makedirs(os.path.join(domain_root, sub), exist_ok=True)

        domain_index = []
        corpus_parts = [f"# MITRE ATT&CK — {domain.upper()} domain\n"]

        for obj in objects:
            otype = obj.get("type")
            if otype not in TYPE_DIR:
                continue
            if obj.get("revoked") or obj.get("x_mitre_deprecated"):
                continue

            attack_id = get_attack_id(obj)
            if not attack_id:
                continue
            name = obj.get("name", "unnamed")
            subdir = TYPE_DIR[otype]
            fname_out = f"{attack_id}__{slugify(name)}.md"
            out_path = os.path.join(domain_root, subdir, fname_out)

            if otype == "x-mitre-tactic":
                md = build_tactic_md(obj, by_id, objects, kc_name)
            elif otype == "attack-pattern":
                md = build_technique_md(obj, by_id, by_source, by_target, kc_name)
            else:
                md = build_generic_md(obj, by_id, by_source, by_target)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)

            entry = {
                "id": attack_id,
                "stix_id": obj["id"],
                "type": otype,
                "name": name,
                "path": os.path.relpath(out_path, BASE).replace("\\", "/"),
            }
            domain_index.append(entry)
            corpus_parts.append(md)

        with open(os.path.join(domain_root, "_index.json"), "w", encoding="utf-8") as f:
            json.dump(domain_index, f, indent=2)

        with open(os.path.join(domain_root, "_full_corpus.md"), "w", encoding="utf-8") as f:
            f.write("\n\n---\n\n".join(corpus_parts))

        global_index[domain] = {
            "counts": {
                t: sum(1 for e in domain_index if e["type"] == t) for t in TYPE_DIR
            },
            "total": len(domain_index),
        }
        print(f"  {domain}: {len(domain_index)} objects written")

    with open(os.path.join(BASE, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump(global_index, f, indent=2)

    print("Done. Summary:")
    print(json.dumps(global_index, indent=2))


if __name__ == "__main__":
    main()
