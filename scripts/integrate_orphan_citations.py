#!/usr/bin/env python3
"""Weave orphan BibTeX entries into the manuscript narrative.

The bibliography (``manuscript/references.bib``) is kept closed by tests:
every entry must be cited and every citekey must resolve. This script maps
orphaned entries to a natural home — the chapter that already names the concept
the paper is famous for — and inserts a single ``\\citep{key}`` or
``\\citet{key}`` after an anchor phrase in the prose.

The script is idempotent: a citation already present in the target file
is left alone. A run that inserts zero citations means the goal has been
reached (bibliography closure).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from biology.citations import (
        citation_keys,
        orphan_citation_insertions,
    )
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from biology.citations import (
        citation_keys,
        orphan_citation_insertions,
    )
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT_ROOT / "manuscript"
INSERTIONS = orphan_citation_insertions(PROJECT_ROOT)


def _is_skippable_context(text: str, pos: int) -> bool:
    """Return True if ``pos`` falls inside:

    * a markdown heading line (``# …``)
    * a fenced code / mermaid block (between ``\\`\\`\\``` pairs)
    * a LaTeX macro argument (``\\label{…}``, ``\\cref{…}``, ``\\citep{…}``, …)
    """
    line_start = text.rfind("\n", 0, pos) + 1
    line_end = text.find("\n", pos)
    if line_end == -1:
        line_end = len(text)
    line = text[line_start:line_end]
    stripped = line.lstrip()
    if stripped.startswith("#"):
        return True
    if stripped.startswith("\\label") or stripped.startswith("\\cref") or stripped.startswith("\\Cref"):
        return True
    before = text[:pos]
    fences = before.count("```")
    if fences % 2 == 1:
        return True
    line_up_to_pos = text[line_start:pos]
    depth = 0
    i = len(line_up_to_pos) - 1
    while i >= 0:
        c = line_up_to_pos[i]
        if c == "}":
            depth += 1
        elif c == "{":
            if depth == 0:
                j = i - 1
                while j >= 0 and (line_up_to_pos[j].isalpha() or line_up_to_pos[j] == "*"):
                    j -= 1
                if j >= 0 and line_up_to_pos[j] == "\\":
                    return True
                break
            depth -= 1
        i -= 1
    return False


def _inject_citation(text: str, anchor: str, citekey: str) -> tuple[str, bool]:
    """Find first safe occurrence of ``anchor`` and inject ``\\citep{key}``."""
    pattern = re.compile(re.escape(anchor) + r"\w*", re.IGNORECASE)
    for match in pattern.finditer(text):
        if _is_skippable_context(text, match.start()):
            continue
        end = match.end()
        return text[:end] + f" \\citep{{{citekey}}}" + text[end:], True
    return text, False


def run(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    inserted = 0
    skipped_already_cited = 0
    skipped_no_anchor = 0

    for ins in INSERTIONS:
        if not ins.target.exists():
            print(f"WARN: target missing {ins.target}", file=sys.stderr)
            continue
        text = ins.target.read_text(encoding="utf-8")
        if ins.citekey in citation_keys(text):
            skipped_already_cited += 1
            continue
        new_text, ok = _inject_citation(text, ins.anchor, ins.citekey)
        if not ok:
            skipped_no_anchor += 1
            print(f"  skip {ins.citekey}: no safe anchor '{ins.anchor}' in {ins.target.name}")
            continue
        if not dry_run:
            write_text_atomic(ins.target, new_text)
        inserted += 1
        print(f"  [{'D' if dry_run else '+'}] {ins.citekey:18s}  {ins.target.relative_to(MANUSCRIPT)}")

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(
        f"\n[{mode}] inserted={inserted} already_cited={skipped_already_cited} "
        f"no_anchor={skipped_no_anchor} total={len(INSERTIONS)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
