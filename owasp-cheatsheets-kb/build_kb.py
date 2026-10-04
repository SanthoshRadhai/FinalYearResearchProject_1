"""
Build an offline, LLM-readable knowledge base from the official OWASP Cheat
Sheet Series repository (already Markdown -- no format conversion needed,
unlike the XML/JSON-sourced sibling *-kb/ folders):
https://github.com/OWASP/CheatSheetSeries

Mirrors the sibling *-kb/ conventions:
    cheatsheets/<Name>_Cheat_Sheet.md   (copied as-is from the repo)
    _index.json
    _full_corpus.md

Stdlib only:
    python build_kb.py

To refresh: re-clone/pull raw/CheatSheetSeries, then re-run this script.
"""
import json
import os
import re
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
RAW_CHEATSHEETS = os.path.join(BASE, "raw", "CheatSheetSeries", "cheatsheets")


def title_from_filename(fname: str) -> str:
    name = fname[:-3] if fname.endswith(".md") else fname
    return name.replace("_", " ")


def main():
    if not os.path.isdir(RAW_CHEATSHEETS):
        raise FileNotFoundError(
            f"{RAW_CHEATSHEETS} not found -- clone OWASP/CheatSheetSeries into raw/ first"
        )

    out_dir = os.path.join(BASE, "cheatsheets")
    os.makedirs(out_dir, exist_ok=True)

    index = []
    corpus_parts = ["# OWASP Cheat Sheet Series\n"]

    for fname in sorted(os.listdir(RAW_CHEATSHEETS)):
        if not fname.endswith(".md"):
            continue
        src_path = os.path.join(RAW_CHEATSHEETS, fname)
        dst_path = os.path.join(out_dir, fname)
        shutil.copyfile(src_path, dst_path)

        with open(src_path, encoding="utf-8") as f:
            content = f.read()

        title = title_from_filename(fname)
        index.append({
            "id": fname[:-3],
            "type": "cheatsheet",
            "name": title,
            "path": os.path.relpath(dst_path, BASE).replace("\\", "/"),
        })
        corpus_parts.append(f"# {title}\n\n{content}")

    with open(os.path.join(BASE, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    with open(os.path.join(BASE, "_full_corpus.md"), "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(corpus_parts))

    with open(os.path.join(BASE, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump({"cheatsheets": len(index)}, f, indent=2)

    print(f"Done. {len(index)} cheat sheets written to {out_dir}")


if __name__ == "__main__":
    main()
