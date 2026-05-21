#!/usr/bin/env python3
"""Extract glossary terms from manuscript/glossary.md and produce Anki/Quizlet CSV."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_GLOSSARY = PROJECT_ROOT / "manuscript" / "glossary.md"
_GLOSSARY_ENTRY_RE = re.compile(
    r"^\[\*\*(?P<term>.+?)\*\*\]\{#gl:(?P<slug>[^}]+)\}"
    r"(?:\s+\[[^\]]+\])?\s+—\s+(?P<definition>.+)$"
)
_TRAILING_CREF_RE = re.compile(r"\s*→\s*\\cref\{[^}]+\}\s*$")


def parse_glossary(path: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            m = _GLOSSARY_ENTRY_RE.match(line.rstrip("\n"))
            if m:
                term = m.group("term").strip()
                slug = m.group("slug").strip()
                definition = _TRAILING_CREF_RE.sub("", m.group("definition").strip())
                entries.append({"term": term, "slug": slug, "definition": definition})
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description="Glossary → flashcards")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=PROJECT_ROOT / "output" / "glossary_cards.tsv",
    )
    parser.add_argument("--format", choices=["anki", "quizlet"], default="anki")
    args = parser.parse_args()
    entries = parse_glossary(MANUSCRIPT_GLOSSARY)
    if not entries:
        print("No entries parsed", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.format == "anki":
        with args.output.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter="\t")
            for e in entries:
                writer.writerow([e["term"], e["definition"]])
        print(f"Wrote {len(entries)} Anki cards -> {args.output}")
    else:
        with args.output.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["Term", "Definition"])
            w.writeheader()
            for e in entries:
                w.writerow({"Term": e["term"], "Definition": e["definition"]})
        print(f"Wrote {len(entries)} Quizlet cards -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
