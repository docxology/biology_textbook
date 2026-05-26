#!/usr/bin/env python3
"""Add a ``\\cref`` link to each lab's and question bank's opening."""

from __future__ import annotations

import sys

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths()

from biology.crossref.parent_chapter_links import apply_parent_chapter_cref

MANUSCRIPT = PROJECT / "manuscript"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    n_labs = 0
    n_questions = 0
    for path in (MANUSCRIPT / "labs").rglob("lab_*.md"):
        if apply_parent_chapter_cref(path, write=not dry_run):
            n_labs += 1
    for path in (MANUSCRIPT / "questions").rglob("questions_*.md"):
        if apply_parent_chapter_cref(path, write=not dry_run):
            n_questions += 1
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] labs_linked={n_labs}  questions_linked={n_questions}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
