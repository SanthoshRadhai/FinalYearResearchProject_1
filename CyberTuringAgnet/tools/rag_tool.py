"""
Shared in-process RAG tool — BM25 keyword search over the project's combined
knowledge base: 6 offline domain KBs (MITRE ATT&CK/CWE/CAPEC/D3FEND, CISA
KEV, OWASP Cheat Sheets), the 4 reference papers, and this project's own
results/architecture docs. Built by ../../rag/ingest.py; see
../../rag/README.md for the full corpus breakdown (6,713 chunks) and why
BM25 (not embeddings) was chosen for this corpus.

This module deliberately does NOT import ../../rag/query.py across the
folder boundary -- it re-implements the same small (~20 line) BM25-loading
logic directly, following the same "reach up to a sibling *-kb/ folder via a
relative path" precedent already set by attack_kb_tool.py for
../../mitre-attack-kb/.

Requires: pip install rank_bm25 (already a dependency of ../../rag/).
"""
import json
import re
from functools import lru_cache
from pathlib import Path

from langchain_core.tools import tool

try:
    from rank_bm25 import BM25Okapi
except ImportError as e:  # pragma: no cover
    raise ImportError(
        "The 'rank_bm25' package is required (pip install rank_bm25). "
        "See Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md and ../../rag/README.md."
    ) from e

CORPUS_PATH = Path(__file__).resolve().parent.parent.parent / "rag" / "rag_corpus.jsonl"
MAX_EXCERPT_CHARS = 500

TOKEN_RE = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9._-]*")

VALID_DOC_TYPES = {
    "mitre-attack-kb", "cwe-kb", "capec-kb", "cisa-kev-kb",
    "owasp-cheatsheets-kb", "d3fend-kb", "paper", "project-doc",
}


def _tokenize(text: str) -> list[str]:
    """Lowercased tokens, keeping '.', '_', '-' inside a token so identifiers
    like 'CVE-2021-44228' or 'T1059.001' survive intact instead of being
    fragmented by a general-purpose tokenizer -- see ../../rag/query.py's
    docstring for why this matters for this specific corpus."""
    return [t.lower() for t in TOKEN_RE.findall(text)]


@lru_cache(maxsize=1)
def _load_corpus():
    if not CORPUS_PATH.exists():
        raise FileNotFoundError(
            f"{CORPUS_PATH} not found -- run 'python ingest.py' inside ../../rag/ first."
        )
    records = []
    with open(CORPUS_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    tokenized = [_tokenize(r["text"]) for r in records]
    bm25 = BM25Okapi(tokenized)
    return records, bm25


@tool
def search_knowledge_base(query: str, k: int = 5, doc_type: str = "") -> list[dict]:
    """Search the project's local, offline knowledge base: MITRE ATT&CK,
    CWE, CAPEC, D3FEND, CISA KEV, OWASP Cheat Sheets, the 4 reference papers
    this research is being compared against, and this project's own
    results/architecture docs. This is a keyword (BM25) search over ~6,700
    chunks -- fast, deterministic, no network call, no cost. Prefer this
    BEFORE browsing the web for anything that might already be covered
    locally: a known CVE, a MITRE ATT&CK technique or campaign, a CWE
    weakness class, a CAPEC attack pattern, a D3FEND defensive technique, an
    OWASP mitigation, or a claim from one of the reference papers.

    Args:
        query: Natural-language query or an exact identifier (e.g.
            "CVE-2024-3400", "T1595.001", "SQL injection mitigation").
        k: Max number of results to return (default 5).
        doc_type: Optional filter to restrict the search to one source type
            -- one of "mitre-attack-kb", "cwe-kb", "capec-kb",
            "cisa-kev-kb", "owasp-cheatsheets-kb", "d3fend-kb", "paper", or
            "project-doc". Leave empty ("") to search everything.

    Returns:
        Up to k results, each {"source", "doc_type", "score", "excerpt"}.
        Empty list if nothing matched. {"error": "..."} if doc_type is not
        one of the valid values above.
    """
    if doc_type and doc_type not in VALID_DOC_TYPES:
        return [{"error": f"'{doc_type}' is not a valid doc_type. Valid values: {sorted(VALID_DOC_TYPES)}"}]

    records, bm25 = _load_corpus()
    scores = bm25.get_scores(_tokenize(query))
    ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    results = []
    for i in ranked:
        if scores[i] <= 0:
            break
        rec = records[i]
        if doc_type and rec["doc_type"] != doc_type:
            continue
        excerpt = rec["text"][:MAX_EXCERPT_CHARS]
        if len(rec["text"]) > MAX_EXCERPT_CHARS:
            excerpt += "..."
        results.append({
            "source": rec["source"],
            "doc_type": rec["doc_type"],
            "score": round(float(scores[i]), 3),
            "excerpt": excerpt,
        })
        if len(results) >= k:
            break
    return results
