#!/usr/bin/env python3
"""Add a ``\\cref`` link to each lab's and question bank's opening, pointing
to the parent chapter.

Mapping rule: for a lab file named ``lab_<stem>.md`` in ``labs/unit_<X>/``,
the parent chapter is ``manuscript/unit_<X>/<stem>.md`` with label
``sec:unit_<X>_<stem>``. Question banks use the same rule against
``questions_<stem>.md``.

Idempotent: if the cross-reference is already present, the file is
skipped. Run ``--dry-run`` to preview.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"


def _derive_parent_label(path: Path) -> str | None:
    # labs/unit_X/lab_foo.md  OR  questions/unit_X/questions_foo.md
    try:
        idx_unit = [p.startswith("unit_") or p == "unit_0" for p in path.parts].index(True)
    except ValueError:
        return None
    unit = path.parts[idx_unit]
    stem = path.stem
    for prefix in ("lab_", "questions_"):
        if stem.startswith(prefix):
            stem = stem[len(prefix):]
            break
    return f"sec:{unit}_{stem}"


def process(path: Path, dry_run: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    label = _derive_parent_label(path)
    if label is None:
        return False
    # Already linked?
    if f"\\cref{{{label}}}" in text:
        return False
    # Inject after the first non-empty paragraph following the title label.
    lines = text.splitlines()
    label_marker = "\\label{sec:"
    inserted = False
    for i, line in enumerate(lines):
        if line.strip().startswith(label_marker):
            # Find next non-empty, non-H2 paragraph start
            j = i + 1
            while j < len(lines) and (lines[j].strip() == "" or lines[j].strip().startswith("##")
                                        or lines[j].strip().startswith("<!--")
                                        or lines[j].strip().startswith(">")):
                j += 1
            if j >= len(lines):
                break
            note = (f"*This activity accompanies \\cref{{{label}}} of the textbook — "
                    f"review that chapter before attempting the exercises below.*")
            new_lines = lines[:j] + [note, ""] + lines[j:]
            text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
            inserted = True
            break
    if inserted and not dry_run:
        write_text_atomic(path, text)
    return inserted


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    n_labs = 0
    n_qs = 0
    for f in (MANUSCRIPT / "labs").rglob("lab_*.md"):
        if process(f, dry_run=dry_run):
            n_labs += 1
    for f in (MANUSCRIPT / "questions").rglob("questions_*.md"):
        if process(f, dry_run=dry_run):
            n_qs += 1
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] labs_linked={n_labs}  questions_linked={n_qs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
