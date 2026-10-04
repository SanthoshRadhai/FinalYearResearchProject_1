# OWASP Cheat Sheet Series Offline Knowledge Base

Built from a shallow clone of the official repository
(`github.com/OWASP/CheatSheetSeries`). Already Markdown at the source —
this build step copies the files into this project's `*-kb/` layout and
generates the same index/corpus files as the sibling knowledge bases,
without any format conversion.

## Structure

```
owasp-cheatsheets-kb/
  cheatsheets/      # One file per topic, copied as-is, e.g. SQL_Injection_Prevention_Cheat_Sheet.md
  raw/CheatSheetSeries/   # Shallow git clone (safe to delete once you trust the build)
  build_kb.py       # Regenerates everything from raw/CheatSheetSeries/cheatsheets/
  _index.json       # id, type, name, path -- for every cheat sheet
  _full_corpus.md   # All cheat sheets concatenated into one document
  _summary.json     # Object count
```

## Object count

122 cheat sheets, covering topics from SQL/NoSQL/XSS injection prevention to
authentication, session management, AI agent security, and cryptographic
storage.

## How this fits the RedBlue-MultiAgent project

This is the **defensive-guidance counterpart** to CAPEC/CWE's
vulnerability-description focus — where CWE says "this is the weakness class"
and CAPEC says "this is how an attacker exploits it," an OWASP Cheat Sheet
says "this is the concrete, actionable fix." It's also the exact corpus
`Research-Paper resources/01-SCOPE.md` cites the reference `docs-autopentestgpt`
implementation as RAGing over (alongside PortSwigger/HackTricks), so this
build closes that specific citation gap in your own project rather than
leaving it as a description of someone else's system.

## Updating later

```bash
rm -rf raw/CheatSheetSeries
git clone --depth 1 https://github.com/OWASP/CheatSheetSeries.git raw/CheatSheetSeries
python build_kb.py
```

## Notes

Licensed by OWASP under Creative Commons Attribution-ShareAlike 4.0.
