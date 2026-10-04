# Project RAG Index

A BM25 (keyword) retrieval index over everything this project has produced
or collected: the 6 offline domain knowledge bases, the 4 reference papers,
and this project's own results/architecture docs. Built to support "compare
our benchmark results against the reference papers" and similar
cross-document questions.

## Why BM25, not embeddings

See `Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md` and the
web research behind it: for a corpus this size, BM25 is the recommended
default — no embedding step, no vector DB, no GPU, fast and deterministic.
It also sidesteps a real, documented problem general embedding models have
with this domain: subword tokenization fragments identifiers like
`CVE-2021-44228` or `T1059.001`. `query.py`'s tokenizer keeps `.`, `_`, `-`
inside tokens specifically so these identifiers survive as exact matches —
see Q4 in the "proof it works" section below for what this buys you in
practice.

## Structure

```
rag/
  ingest.py          # Builds rag_corpus.jsonl from every source below
  query.py           # BM25Okapi retriever + CLI
  rag_corpus.jsonl   # One JSON object per chunk: {id, source, doc_type, text}
```

## Corpus composition (6,713 chunks total)

| doc_type | Chunks | Source |
|---|---|---|
| `mitre-attack-kb` | 2,317 | `../mitre-attack-kb/` — one chunk per object, no splitting |
| `cisa-kev-kb` | 1,721 | `../cisa-kev-kb/` |
| `cwe-kb` | 969 | `../cwe-kb/` |
| `capec-kb` | 615 | `../capec-kb/` |
| `d3fend-kb` | 278 | `../d3fend-kb/` |
| `owasp-cheatsheets-kb` | 122 | `../owasp-cheatsheets-kb/` |
| `paper` | 466 | The 4 PDFs in `../papaers/`, parsed with **Docling** (structure-aware — headings/tables/reading order, not a raw text dump), then split with LangChain's `RecursiveCharacterTextSplitter` (1500 chars, 200 overlap) |
| `project-doc` | 225 | `../RedBlue-MultiAgent/README.md` + `RESULTS.md`, all of `../Research-Paper resources/01-08*.md`, `../findings/ornith-...md` — same splitter as papers |

The 6 KB folders are NOT split further — each entry is already a short,
self-contained document (per each KB's own `build_kb.py`), so one KB entry
= one retrievable chunk.

## Docling: CPU-only, and why that took extra work

Docling's default `pip install docling` pulls a **CUDA-enabled torch
build** (~2GB+ of nvidia_cublas/cudnn/nccl/etc.) even though this project
only needs CPU-based PDF parsing for 4 papers. Fix: install CPU-only torch
FIRST from PyTorch's own CPU wheel index
(`pip install torch --index-url https://download.pytorch.org/whl/cpu`),
then `pip install docling` — it sees torch already satisfied and skips the
CUDA variant entirely.

**A second, less obvious issue this surfaced**: docling's own dependency
resolution then installed a `torchvision` build from plain PyPI (not the
CPU wheel index), which has a different native-ops ABI than the CPU `torch`
build already installed — Docling's layout model failed with
`RuntimeError: operator torchvision::nms does not exist`. Fixed by
force-reinstalling `torchvision` from the **same** CPU wheel index as
`torch`:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install docling
pip install --force-reinstall --no-deps torchvision --index-url https://download.pytorch.org/whl/cpu
```
Both torch and torchvision must come from the same index/build variant —
mixing a CPU-index torch with a PyPI-default torchvision (or vice versa)
breaks at the native-extension level, not at import time, so this only
surfaces once you actually run a model that calls the mismatched op.

## Usage

```bash
python ingest.py     # rebuild rag_corpus.jsonl from scratch (run after any KB/paper/doc changes)
python query.py "your question here"
python query.py "CVE-2024-3400" --k 5
python query.py "PentestGPT ablation study" --doc-type paper
python query.py "stall count design limitation" --doc-type project-doc --full-text
```

As a library:
```python
from query import RagIndex
idx = RagIndex()
hits = idx.query("tool-calling success rate comparison", k=5)
```

## Proof it works (4 sample queries, real output)

- **Q1** ("tool calling success rate reliability evaluation", no filter) —
  top hits mixed our own `RESULTS.md` §2 with a third-party paper's
  evaluation-methodology section (Vulnerability Detection Rate, Exploitation
  Success Rate) — exactly the side-by-side material a paper-comparison
  question needs.
- **Q2** ("PentestGPT reasoning generation parsing module architecture",
  `--doc-type paper`) — top 3 hits were PentestGPT's own tripartite
  architecture description and its ablation study (§6.4) — precise,
  relevant, paper-only retrieval.
- **Q3** ("evaluator caught hallucination CVSS score rejected",
  `--doc-type project-doc`) — top hits were `RESULTS.md`'s own RQ3
  narrative (Trial 3, the Evaluator catching a real hallucination) —
  confirms project-only filtering works.
- **Q4** ("CVE-2024-3400", no filter) — surfaced the CISA KEV entry, our own
  `RESULTS.md` benchmark mention, **and** (unprompted) a MITRE ATT&CK
  campaign record: this exact CVE was used in a real 2024 attack campaign
  ("Operation MidnightEclipse", the UPSTYLE backdoor). Nobody curated that
  cross-reference by hand — it fell out of BM25 matching the same
  identifier across three independently-built knowledge bases, which is
  the whole point of keeping identifiers intact as single tokens.

## Updating

Re-run `python ingest.py` any time a `*-kb/` folder, a paper, or a project
doc changes — it rebuilds `rag_corpus.jsonl` from scratch (a few seconds
for the KBs, a few minutes for the 4 PDFs via Docling on CPU).
