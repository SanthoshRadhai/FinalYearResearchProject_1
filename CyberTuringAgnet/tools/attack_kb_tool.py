"""Local, offline MITRE ATT&CK lookup — no network, no MCP server, no subprocess.

Wraps the already-built ../../mitre-attack-kb/ (see its README.md for how it was
generated from the official STIX 2.1 corpus). Used by Exploit/PoC Discovery,
Attack Planning, and Log/Alert Triage per Research-Paper resources/
07-...ARCHITECTURE.md §5.3/§5.4/§6.2 — this is the "local MITRE ATT&CK dataset +
lookup tool" row from that document's §8, now actually built.
"""

import json
from functools import lru_cache
from pathlib import Path

from langchain_core.tools import tool

KB_ROOT = Path(__file__).resolve().parent.parent.parent / "mitre-attack-kb"
DOMAINS = ("enterprise", "mobile", "ics")


@lru_cache(maxsize=1)
def _load_index() -> list[dict]:
    """Concatenated _index.json across all three domains, loaded once per process."""
    entries = []
    for domain in DOMAINS:
        index_path = KB_ROOT / domain / "_index.json"
        if not index_path.exists():
            continue
        with open(index_path, "r", encoding="utf-8") as f:
            for entry in json.load(f):
                entries.append({**entry, "domain": domain})
    return entries


@tool
def lookup_attack_technique(technique_id: str) -> dict:
    """Look up a MITRE ATT&CK technique or sub-technique by its exact ID
    (e.g. "T1595" or "T1595.001") and return its full Markdown writeup —
    description, platforms, detection guidance, mitigations, and known
    groups/software observed using it. This is a local, offline lookup; it
    never hits attack.mitre.org over the network.

    Args:
        technique_id: The ATT&CK technique ID, e.g. "T1595.001".

    Returns:
        dict with keys: id, name, domain, content (full Markdown text), or
        {"error": "..."} if the ID isn't found in the local KB.
    """
    technique_id = technique_id.strip().upper()
    for entry in _load_index():
        if entry["id"] == technique_id:
            # entry["path"] is already relative to KB_ROOT, e.g.
            # "enterprise/techniques/T1595.001__Scanning_IP_Blocks.md".
            real_path = KB_ROOT / entry["path"]
            if not real_path.exists():
                return {"error": f"index says {technique_id} is at {entry['path']} but the file is missing on disk"}
            return {
                "id": entry["id"],
                "name": entry["name"],
                "domain": entry["domain"],
                "content": real_path.read_text(encoding="utf-8"),
            }
    return {"error": f"technique '{technique_id}' not found in local ATT&CK KB (checked enterprise/mobile/ics)"}


@tool
def search_attack_kb(query: str, object_type: str = "") -> list[dict]:
    """Search the local ATT&CK KB index by name substring (case-insensitive).
    Use this when you have a technique/group/software NAME but not its ID.

    Args:
        query: Substring to match against object names, e.g. "scanning ip blocks".
        object_type: Optional filter — one of "attack-pattern" (techniques),
            "intrusion-set" (groups), "malware"/"tool" (software),
            "course-of-action" (mitigations), "x-mitre-tactic" (tactics),
            "campaign". Leave empty to search all types.

    Returns:
        Up to 20 matches as [{"id", "name", "type", "domain"}, ...].
    """
    query_lower = query.strip().lower()
    results = []
    for entry in _load_index():
        if object_type and entry.get("type") != object_type:
            continue
        if query_lower in entry["name"].lower():
            results.append({
                "id": entry["id"],
                "name": entry["name"],
                "type": entry.get("type"),
                "domain": entry["domain"],
            })
        if len(results) >= 20:
            break
    return results
