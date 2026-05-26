#!/usr/bin/env python3
"""Bold + link each glossary term on first use in every chapter."""

from __future__ import annotations

import sys

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.maintenance.glossary_first_use import apply_glossary_first_use, load_glossary_terms

MANUSCRIPT = PROJECT / "manuscript"
SKIP_NAMES = frozenset({"README.md", "AGENTS.md", "unit_intro.md"})


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    terms = load_glossary_terms()
    total = 0
    files = 0
    for unit_dir in sorted(MANUSCRIPT.glob("unit_*")):
        for chapter in sorted(unit_dir.glob("*.md")):
            if chapter.name in SKIP_NAMES:
                continue
            count = apply_glossary_first_use(chapter, terms, write=not dry_run)
            if count:
                files += 1
                total += count
                print(f"  [{'D' if dry_run else '+'}] {chapter.relative_to(MANUSCRIPT)}: {count} terms")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] linked_total={total} files_touched={files} terms={len(terms)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
