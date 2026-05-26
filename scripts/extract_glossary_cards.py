#!/usr/bin/env python3
"""Extract glossary terms from manuscript/glossary.md and produce Anki/Quizlet CSV."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.maintenance.glossary_cards import parse_glossary_cards, write_glossary_cards


def main() -> int:
    parser = argparse.ArgumentParser(description="Glossary → flashcards")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=PROJECT / "output" / "glossary_cards.tsv",
    )
    parser.add_argument("--format", choices=["anki", "quizlet"], default="anki")
    args = parser.parse_args()
    entries = parse_glossary_cards(PROJECT / "manuscript" / "glossary.md")
    if not entries:
        print("No entries parsed", file=sys.stderr)
        return 1
    write_glossary_cards(entries, args.output, card_format=args.format)
    label = "Anki" if args.format == "anki" else "Quizlet"
    print(f"Wrote {len(entries)} {label} cards -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
