# MITRE CAPEC Offline Knowledge Base

Built from the official CAPEC XML catalog (`capec.mitre.org/data/xml/capec_latest.xml`,
version 3.9, dated 2023-01-24). Fully offline after generation.

## Structure

```
capec-kb/
  patterns/         # One file per attack pattern, e.g. CAPEC-66__SQL_Injection.md
  raw/              # Original XML (safe to delete once you trust the build)
  build_kb.py       # Regenerates everything from raw/ (re-run after updating raw/*.xml)
  _index.json       # id, type, name, abstraction, path -- for every pattern
  _full_corpus.md   # All patterns concatenated into one document
  _summary.json     # Object count
```

Each pattern file includes: description, likelihood of attack, typical
severity, related attack patterns (ChildOf/ParentOf), prerequisites, skills
required, resources required, consequences, mitigations, and related CWE
weaknesses (cross-referencing `../cwe-kb/`).

## Object count

615 attack patterns.

## How this fits the RedBlue-MultiAgent project

CAPEC sits between MITRE ATT&CK's techniques (`../mitre-attack-kb/`, tactical
"how" at the enterprise-technique level) and CWE's weaknesses (`../cwe-kb/`,
the underlying code/design flaw): CAPEC describes the *attack pattern* an
adversary follows to exploit a given weakness class. Useful for the Exploit/
PoC Discovery and Attack Planning agents from
`Research-Paper resources/07-MULTI-AGENT-ARCHITECTURE.md` §5.3/§5.4 when a
recon finding names a weakness type but not yet a specific technique.

## Updating later

```bash
curl -sL -o raw/capec_latest.xml https://capec.mitre.org/data/xml/capec_latest.xml
python build_kb.py
```

## Notes

Licensed by MITRE under the CAPEC Terms of Use (free for use with attribution).
