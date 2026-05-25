#!/usr/bin/env python3
"""Normalise typography in the manuscript prose.

Pandoc's ``smart`` extension (enabled by default with ``--from=markdown``)
converts ASCII straight quotes, ellipses, and en/em-dashes to their
typographic equivalents at render time, so those don't need source edits.

What pandoc does *not* touch:

* ASCII arrows ``-->`` — often meant as "→" in biochemical pathways.
* ASCII ``...`` in code-free prose — harmless, but becomes ``\\ldots``.

This script targets only the ASCII arrow conversion, because it genuinely
improves PDF output. It skips mermaid blocks, code fences, and LaTeX
equation environments (where ``-->`` has its own meaning).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"


_ARROW_RE = re.compile(r"(?<![=\-])-->(?![>\-])")


def _strip_code_and_math(text: str) -> list[tuple[int, int]]:
    """Return list of (start, end) spans that must NOT be touched."""
    spans: list[tuple[int, int]] = []
    # Fenced code / mermaid blocks
    fence_re = re.compile(r"```[a-zA-Z0-9_-]*\n.*?\n```", re.DOTALL)
    for m in fence_re.finditer(text):
        spans.append(m.span())
    # Display equations $$…$$
    for m in re.finditer(r"\$\$.*?\$\$", text, re.DOTALL):
        spans.append(m.span())
    # LaTeX equation / figure / table environments
    for env in ("equation", "align", "gather", "multline", "figure", "table"):
        for m in re.finditer(
            rf"\\begin\{{{env}\*?\}}.*?\\end\{{{env}\*?\}}", text, re.DOTALL
        ):
            spans.append(m.span())
    # Inline math $…$
    for m in re.finditer(r"(?<!\$)\$[^$\n]+\$", text):
        spans.append(m.span())
    # Literal code spans `…`
    for m in re.finditer(r"`[^`\n]+`", text):
        spans.append(m.span())
    # HTML comments — contain ``-->`` as their own terminator; never touch.
    for m in re.finditer(r"<!--.*?-->", text, re.DOTALL):
        spans.append(m.span())
    # YAML front-matter block at top of file (``---\n…\n---``)
    fm = re.match(r"\A---\n.*?\n---\n", text, re.DOTALL)
    if fm:
        spans.append(fm.span())
    return sorted(spans)


def _is_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    for s, e in spans:
        if s <= pos < e:
            return True
        if s > pos:
            return False
    return False


def normalise_file(path: Path, dry_run: bool = False) -> int:
    text = path.read_text(encoding="utf-8")
    protected = _strip_code_and_math(text)
    # Walk matches in reverse so substitutions don't invalidate spans.
    matches = list(_ARROW_RE.finditer(text))
    out = text
    converted = 0
    for m in reversed(matches):
        if _is_protected(m.start(), protected):
            continue
        out = out[: m.start()] + "→" + out[m.end():]
        converted += 1
    if converted and not dry_run:
        write_text_atomic(path, out)
    return converted


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total = 0
    files = 0
    for md in MANUSCRIPT.rglob("*.md"):
        if md.name in {"README.md", "AGENTS.md", "preamble.md"}:
            continue
        n = normalise_file(md, dry_run=dry_run)
        if n:
            files += 1
            total += n
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] arrows_converted={total} files_touched={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
