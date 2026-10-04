# CISA Known Exploited Vulnerabilities (KEV) Offline Knowledge Base

Built from the official CISA KEV feed
(`cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`),
catalog snapshot dated 2026-09-22 (1,721 entries at build time).

**Unlike the other `*-kb/` folders, this catalog changes daily** — CISA adds
new confirmed-exploited CVEs on an ongoing basis. Re-download and rebuild
periodically rather than treating this as a fixed reference corpus.

## Structure

```
cisa-kev-kb/
  entries/          # One file per CVE, e.g. CVE-2024-3400.md
  raw/              # Original JSON feed (safe to delete once you trust the build)
  build_kb.py       # Regenerates everything from raw/*.json
  _index.json       # id (CVE), type, name, date_added, ransomware_use, path
  _full_corpus.md   # All entries concatenated into one document
  _summary.json     # Entry count, catalog version, release date
```

Each entry includes: vendor/product, date added to KEV, remediation due date
(per CISA's BOD 26-04), known ransomware campaign use, related CWE IDs
(cross-referencing `../cwe-kb/`), description, required action, and
additional reference notes/URLs.

## Object count

1,721 entries (as of catalog version dated 2026-09-22).

## How this fits the RedBlue-MultiAgent project

This is the row from `Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md`
§1.3 ("CISA KEV JSON feed"), built as a static local snapshot instead of a
live MCP server call — matches the "Local ATT&CK dataset" precedent in
`../mitre-attack-kb/`. Intended for the Threat Intel Correlation Agent
(`07-MULTI-AGENT-ARCHITECTURE.md` §6.1): given a CVE ID, check whether it's
confirmed actively exploited in the wild rather than only theoretically
severe.

## Updating later

```bash
curl -sL -o raw/known_exploited_vulnerabilities.json \
  https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
python build_kb.py
```

## Notes

Public domain (U.S. government work) per CISA's KEV catalog terms.
