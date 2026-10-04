"""
Query the RAG corpus built by ingest.py (rag_corpus.jsonl) using BM25
(keyword) retrieval -- no embeddings, no vector DB, no GPU. See
Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md and the
web research behind it for why this is the right default for a corpus this
size: no embedding step to manage, fast, deterministic, and avoids the
documented subword-tokenization problem general embedding models have with
identifiers like "CVE-2021-44228" or "T1059.001" that this corpus is full of.

Usage:
    python query.py "how does our tool-calling success rate compare to PentestGPT"
    python query.py "CVE-2024-3400" --k 3
    python query.py "stall count design limitation" --doc-type project-doc

As a library:
    from query import RagIndex
    idx = RagIndex()
    for hit in idx.query("SQL injection mitigation", k=5):
        print(hit["source"], hit["score"])
"""
import argparse
import json
import os
import re

from rank_bm25 import BM25Okapi

BASE = os.path.dirname(os.path.abspath(__file__))
CORPUS_PATH = os.path.join(BASE, "rag_corpus.jsonl")

TOKEN_RE = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9._-]*")


def tokenize(text: str) -> list[str]:
    """Lowercased word tokens, keeping internal '.', '_', '-' so identifiers
    like 'CVE-2021-44228' and 'T1059.001' survive as single tokens instead
    of being fragmented -- the exact problem general subword tokenizers have
    with this domain (see rag/README.md)."""
    return [t.lower() for t in TOKEN_RE.findall(text)]


class RagIndex:
    def __init__(self, corpus_path: str = CORPUS_PATH):
        self.records = []
        with open(corpus_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    self.records.append(json.loads(line))
        if not self.records:
            raise RuntimeError(f"{corpus_path} is empty -- run ingest.py first")

        self._tokenized = [tokenize(r["text"]) for r in self.records]
        self._bm25 = BM25Okapi(self._tokenized)

    def query(self, text: str, k: int = 5, doc_type: str | None = None) -> list[dict]:
        scores = self._bm25.get_scores(tokenize(text))
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

        results = []
        for i in ranked:
            if doc_type and self.records[i]["doc_type"] != doc_type:
                continue
            if scores[i] <= 0:
                break
            rec = self.records[i]
            results.append({
                "id": rec["id"],
                "source": rec["source"],
                "doc_type": rec["doc_type"],
                "score": round(float(scores[i]), 3),
                "text": rec["text"],
            })
            if len(results) >= k:
                break
        return results

    def stats(self) -> dict:
        by_type = {}
        for r in self.records:
            by_type[r["doc_type"]] = by_type.get(r["doc_type"], 0) + 1
        return {"total_chunks": len(self.records), "by_doc_type": by_type}


def main():
    parser = argparse.ArgumentParser(description="Query the project's RAG corpus (BM25).")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--k", type=int, default=5, help="Number of results (default 5)")
    parser.add_argument("--doc-type", default=None, help="Restrict to one doc_type (e.g. paper, project-doc, cwe-kb)")
    parser.add_argument("--full-text", action="store_true", help="Print full chunk text instead of a preview")
    args = parser.parse_args()

    idx = RagIndex()
    print(f"[corpus] {idx.stats()}\n")

    results = idx.query(args.query, k=args.k, doc_type=args.doc_type)
    if not results:
        print("No matches.")
        return

    for rank, hit in enumerate(results, 1):
        preview = hit["text"] if args.full_text else hit["text"][:400].replace("\n", " ")
        print(f"[{rank}] score={hit['score']}  {hit['source']}")
        print(f"    {preview}{'...' if not args.full_text and len(hit['text']) > 400 else ''}")
        print()


if __name__ == "__main__":
    main()
