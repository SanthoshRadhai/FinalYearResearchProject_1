# MITRE ATT&CK Offline Knowledge Base

Built from the official MITRE STIX 2.1 data (`github.com/mitre/cti`) on 2026-09-11.
Fully offline after generation — no network access needed to read or query it.

## Structure

```
mitre-attack-kb/
  enterprise/          # Enterprise ATT&CK domain (Windows/macOS/Linux/Cloud/Network/Containers/SaaS/IdP)
  mobile/               # Mobile ATT&CK domain (Android/iOS)
  ics/                  # ICS ATT&CK domain (industrial control systems)
  raw/                  # Original STIX JSON bundles (safe to delete once you trust the build)
  build_kb.py           # Regenerates everything from raw/ (re-run after updating raw/*.json)
  _summary.json         # Object counts per domain
```

Each domain folder contains:

| Folder | Content |
|---|---|
| `tactics/` | The high-level "why" — e.g. `TA0002__Execution.md`, listing every technique in that tactic |
| `techniques/` | One file per technique/sub-technique (e.g. `T1059__Command_and_Scripting_Interpreter.md`, `T1059.001__PowerShell.md`) — description, platforms, detection guidance, mitigations, and known groups/software observed using it |
| `mitigations/` | Defensive controls (e.g. `M1038__Execution_Prevention.md`) and which techniques each one addresses |
| `groups/` | Named threat actors/APTs (e.g. `G0016__APT29.md`) and the techniques attributed to them |
| `software/` | Malware and tools (e.g. `S0002__Mimikatz.md`) and the techniques they implement |
| `campaigns/` | Named intrusion campaigns and their associated techniques |
| `_index.json` | Machine-readable index: id, type, name, file path — for every object in that domain |
| `_full_corpus.md` | All of the above domain's files concatenated into one document (useful for simple context-stuffing into an LLM prompt) |

## Object counts

| Domain | Tactics | Techniques (incl. sub) | Mitigations | Groups | Software | Campaigns |
|---|---|---|---|---|---|---|
| Enterprise | 15 | 697 | 44 | 176 | 825 | 56 |
| Mobile | 12 | 124 | 13 | 20 | 126 | 3 |
| ICS | 12 | 97 | 52 | 14 | 23 | 8 |

## How to feed this to an LLM

- **Full-context models / small KB subset:** hand it a domain's `_full_corpus.md` directly, or a handful of individual technique files — they're plain Markdown, self-contained, and cross-reference IDs (e.g. "T1059") rather than fragile links.
- **RAG pipeline:** chunk by file (each Markdown file is already one coherent unit — a technique, a group, a mitigation, etc.), embed each chunk, and keep `_index.json` around to map an ATT&CK ID back to its file/type instantly without re-parsing STIX.
- **Fine-tuning / instruction data:** the consistent `# <ID>: <Name>` + `## Description` / `## Mitigations` / etc. structure makes it easy to script Q&A pair generation per object.

## Updating later

MITRE ATT&CK releases new versions ~2x/year. To refresh:

```bash
curl -sL -o raw/enterprise-attack.json https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json
curl -sL -o raw/mobile-attack.json https://raw.githubusercontent.com/mitre/cti/master/mobile-attack/mobile-attack.json
curl -sL -o raw/ics-attack.json https://raw.githubusercontent.com/mitre/cti/master/ics-attack/ics-attack.json
conda run -n mitre-kb python build_kb.py
```

## Notes

- Deprecated and revoked ATT&CK objects are excluded.
- `x-mitre-data-source` objects (the newer detection data-source catalog) show 0 counts here because the STIX relationship model links techniques to data sources by name string (`x_mitre_data_sources` field on the technique) rather than by relationship object in this bundle version — the data source *names* are still listed under each technique's "Data Sources" section.
- Everything is licensed by MITRE under the ATT&CK Terms of Use (free for use with attribution) — see `raw/*.json` bundle metadata for the exact license reference.
