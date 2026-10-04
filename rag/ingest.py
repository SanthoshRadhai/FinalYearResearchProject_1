"""
Build the RAG corpus for this project: one JSONL file with one chunk per
line, drawn from three kinds of sources:

  1. The 6 offline domain knowledge bases (mitre-attack-kb, cwe-kb,
     capec-kb, cisa-kev-kb, owasp-cheatsheets-kb, d3fend-kb) -- each entry
     is already a short, self-contained Markdown document (per their own
     build_kb.py scripts), so each becomes exactly ONE chunk, no splitting.
  2. The 4 reference papers in papaers/*.pdf -- parsed with Docling
     (structure-aware PDF extraction: headings, tables, reading order --
     not just a raw text dump), then split into overlapping chunks with
     LangChain's RecursiveCharacterTextSplitter since these are long,
     multi-page documents.
  3. This project's own long-form docs (RedBlue-MultiAgent/RESULTS.md,
     Research-Paper resources/*.md) -- same chunking treatment as the papers,
     since they're comparably long, prose-heavy documents.

Output: rag_corpus.jsonl in this directory, one record per line:
    {"id": "...", "source": "...", "doc_type": "...", "text": "..."}

Design choice (see Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md
and the web research behind it): retrieval itself is BM25 (query.py), not
embeddings -- no GPU, no vector DB, consistent with every other tool in this
project. Docling is used ONLY for high-quality PDF text extraction, not for
retrieval.

Run inside the `hexstrike` conda env (needs docling, pypdf, langchain_community
installed -- see ../RedBlue-MultiAgent/requirements.txt style):
    python ingest.py
"""
import json
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(BASE, "rag_corpus.jsonl")

KB_FOLDERS = [
    "mitre-attack-kb",   # note: this one has per-domain _index.json (enterprise/mobile/ics), handled specially
    "cwe-kb",
    "capec-kb",
    "cisa-kev-kb",
    "owasp-cheatsheets-kb",
    "d3fend-kb",
]

PAPER_FILES = [
    "papaers/usenixsecurity24-deng.pdf",
    "papaers/s10664-025-10758-3.pdf",
    "papaers/s10207-024-00835-x.pdf",
    "papaers/s11227-026-08439-z.pdf",
]

PROJECT_DOC_FILES = [
    "RedBlue-MultiAgent/README.md",
    "RedBlue-MultiAgent/RESULTS.md",
    "Research-Paper resources/01-SCOPE.md",
    "Research-Paper resources/02-APPROACHES.md",
    "Research-Paper resources/03-CONCLUSION.md",
    "Research-Paper resources/04-MODEL-SPECIALIZATION.md",
    "Research-Paper resources/05-QA-PREP.md",
    "Research-Paper resources/06-GPT-OSS-LLAMACPP-TOOLCALLING-FINDINGS.md",
    "Research-Paper resources/07-MULTI-AGENT-ARCHITECTURE.md",
    "Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md",
    "findings/ornith-1.0-35b-Q4_K_M-latest_2026-09-07_2317.md",
]

PROSE_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=1500, chunk_overlap=200,
    separators=["\n## ", "\n### ", "\n\n", "\n", ". ", " ", ""],
)


def ingest_kb_folder(kb_name: str) -> list[dict]:
    """Reads a KB's _index.json (or, for mitre-attack-kb, one per domain)
    and turns every entry into exactly one chunk. Every *-kb/'s entry["path"]
    is already relative to that KB's own root folder (confirmed against
    each build_kb.py: e.g. cwe-kb's is "weaknesses/CWE-79__....md" relative
    to cwe-kb/, mitre-attack-kb's domain entries are "enterprise/techniques/
    ....md" relative to mitre-attack-kb/ itself, NOT relative to the
    enterprise/ subfolder) -- so the join is uniform across every KB,
    mitre-attack-kb included, despite it having 3 separate _index.json files
    instead of 1."""
    records = []
    kb_path = os.path.join(PROJECT_ROOT, kb_name)

    index_paths = []
    if kb_name == "mitre-attack-kb":
        for domain in ("enterprise", "mobile", "ics"):
            p = os.path.join(kb_path, domain, "_index.json")
            if os.path.exists(p):
                index_paths.append(p)
    else:
        p = os.path.join(kb_path, "_index.json")
        if os.path.exists(p):
            index_paths.append(p)

    for index_path in index_paths:
        with open(index_path, encoding="utf-8") as f:
            entries = json.load(f)
        for entry in entries:
            file_path = os.path.join(kb_path, entry["path"])
            if not os.path.exists(file_path):
                continue
            with open(file_path, encoding="utf-8") as f:
                text = f.read()
            records.append({
                "id": f"{kb_name}/{entry['id']}",
                "source": f"{kb_name}: {entry.get('name', entry['id'])} ({entry['id']})",
                "doc_type": kb_name,
                "text": text,
            })
    return records


def ingest_paper_pdf(rel_path: str) -> list[dict]:
    from docling.document_converter import DocumentConverter

    abs_path = os.path.join(PROJECT_ROOT, rel_path)
    if not os.path.exists(abs_path):
        print(f"  [skip] {rel_path} not found")
        return []

    print(f"  parsing with docling: {rel_path} ...")
    converter = DocumentConverter()
    result = converter.convert(abs_path)
    markdown = result.document.export_to_markdown()

    stem = os.path.splitext(os.path.basename(rel_path))[0]
    chunks = PROSE_SPLITTER.split_text(markdown)
    return [
        {
            "id": f"paper/{stem}#chunk{i}",
            "source": f"paper: {stem} (chunk {i+1}/{len(chunks)})",
            "doc_type": "paper",
            "text": chunk,
        }
        for i, chunk in enumerate(chunks)
    ]


def ingest_project_doc(rel_path: str) -> list[dict]:
    abs_path = os.path.join(PROJECT_ROOT, rel_path)
    if not os.path.exists(abs_path):
        print(f"  [skip] {rel_path} not found")
        return []
    with open(abs_path, encoding="utf-8") as f:
        text = f.read()
    stem = rel_path.replace("/", "__")
    chunks = PROSE_SPLITTER.split_text(text)
    return [
        {
            "id": f"project-doc/{stem}#chunk{i}",
            "source": f"project doc: {rel_path} (chunk {i+1}/{len(chunks)})",
            "doc_type": "project-doc",
            "text": chunk,
        }
        for i, chunk in enumerate(chunks)
    ]


def main():
    all_records = []

    print("=== Domain knowledge bases ===")
    for kb_name in KB_FOLDERS:
        recs = ingest_kb_folder(kb_name)
        print(f"  {kb_name}: {len(recs)} chunks")
        all_records.extend(recs)

    print("=== Reference papers (via Docling) ===")
    for rel_path in PAPER_FILES:
        recs = ingest_paper_pdf(rel_path)
        print(f"  {rel_path}: {len(recs)} chunks")
        all_records.extend(recs)

    print("=== Project's own docs ===")
    for rel_path in PROJECT_DOC_FILES:
        recs = ingest_project_doc(rel_path)
        print(f"  {rel_path}: {len(recs)} chunks")
        all_records.extend(recs)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        for rec in all_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    by_type = {}
    for r in all_records:
        by_type[r["doc_type"]] = by_type.get(r["doc_type"], 0) + 1

    print(f"\nDone. {len(all_records)} total chunks written to {OUT_PATH}")
    print(json.dumps(by_type, indent=2))


if __name__ == "__main__":
    main()
