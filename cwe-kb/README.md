# MITRE CWE Offline Knowledge Base

Built from the official CWE XML catalog (`cwe.mitre.org/data/xml/cwec_latest.xml.zip`,
version 4.20, dated 2026-04-30). Fully offline after generation.

## Structure

```
cwe-kb/
  weaknesses/       # One file per weakness, e.g. CWE-79__Improper_Neutralization_..._XSS.md
  raw/              # Original XML (safe to delete once you trust the build)
  build_kb.py       # Regenerates everything from raw/ (re-run after updating raw/*.xml)
  _index.json       # id, type, name, abstraction, path -- for every weakness
  _full_corpus.md   # All weaknesses concatenated into one document
  _summary.json     # Object count
```

Each weakness file includes: description, extended description, related
weaknesses (ChildOf/ParentOf/etc. with CWE IDs), common consequences,
potential mitigations (tagged by phase), detection methods, and a summary of
demonstrative examples.

## Object count

969 weaknesses.

## How this fits the RedBlue-MultiAgent project

Row from `Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md`
§1.6 ("Local CWE dataset lookup, optional") — built the same way as
`../mitre-attack-kb/` rather than depending on a third-party MCP server.
CISA KEV entries (`../cisa-kev-kb/`) reference CWE IDs, so this is also the
natural cross-reference target from a KEV entry back to its root-cause
weakness class.

## Updating later

```bash
curl -sL -o raw/cwec_latest.xml.zip https://cwe.mitre.org/data/xml/cwec_latest.xml.zip
cd raw && unzip -o cwec_latest.xml.zip && cd ..
python build_kb.py
```

## Notes

Licensed by MITRE under the CWE Terms of Use (free for use with attribution).
