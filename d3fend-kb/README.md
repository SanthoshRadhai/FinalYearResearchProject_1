# MITRE D3FEND Offline Knowledge Base

Built from the official D3FEND ontology JSON-LD
(`d3fend.mitre.org/ontologies/d3fend.json`). Fully offline after generation.

## Structure

```
d3fend-kb/
  techniques/       # One file per defensive technique, e.g. D3-AMED__Access_Mediation.md
  tactics/          # One file per D3FEND tactic (Harden, Detect, Isolate, Deceive, Evict, Restore)
  raw/              # Original JSON-LD ontology (safe to delete once you trust the build)
  build_kb.py       # Regenerates everything from raw/d3fend.json
  _index.json       # id, type, name, path -- for every tactic and technique
  _full_corpus.md   # Everything concatenated into one document
  _summary.json     # Object counts
```

Each technique file includes: definition, synonym(s), parent class(es), and
every direct ontology relationship on that technique (e.g. `enables:
Isolate`, `maps: Digital Identity`, `kb-reference: ...`) plus any knowledge
base article text the ontology includes.

## Object count

6 tactics + 272 defensive techniques.

## Two honest limitations of this build (read before treating it as complete)

1. **This is fundamentally different from `../mitre-attack-kb/`,
   `../cwe-kb/`, and `../capec-kb/`: D3FEND is an OWL ontology (a graph),
   not a flat XML catalog.** `build_kb.py` resolves each technique's direct
   properties and `owl:Restriction` blank nodes (onProperty +
   someValuesFrom) into a "Relationships" section — this is real ontology
   content, not a summary or approximation of it.
2. **Tactic groupings are partial, not comprehensive**: only techniques that
   carry a *direct* `d3f:enables` relationship to one of the 6 tactics are
   listed on that tactic's page (28 of 272 techniques, ~10%, at build time).
   The other ~90% of techniques are almost certainly still conceptually
   under a tactic via a longer parent-class chain (D3FEND's own website
   computes this via a SPARQL query over additional mapping data not present
   in the single ontology JSON fetched here) — this build does not attempt
   that multi-hop resolution. **Every individual technique's own page is
   still complete** (definition, relationships, references); it's only the
   top-down "which techniques fall under tactic X" grouping that's partial.
   Browse `_index.json` directly for the full technique list regardless of
   tactic.
3. **This build does NOT reconstruct "D3FEND technique X counters ATT&CK
   technique Y"** mappings — same reason as above (that mapping isn't in
   this ontology file). If you need that specific cross-reference, it would
   require either a different D3FEND data export or scraping the live site's
   per-technique "Counters" section.

## How this fits the RedBlue-MultiAgent project

This is the row `Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md`
§1.5 flagged as the one real MCP/dataset-ecosystem gap (offense-focused
tooling like ATT&CK/CVE/KEV is mature; defense-focused D3FEND coverage
wasn't) — this build closes that gap for the Detection & Mitigation Agent
(`07-MULTI-AGENT-ARCHITECTURE.md` §6.3) with a real, local, offline corpus
rather than leaving it as a documented limitation.

## Updating later

```bash
curl -sL -o raw/d3fend.json https://d3fend.mitre.org/ontologies/d3fend.json
python build_kb.py
```

## Notes

Licensed by MITRE under the D3FEND Terms of Use (free for use with attribution).
