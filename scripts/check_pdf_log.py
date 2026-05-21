#!/usr/bin/env python3
"""Check XeLaTeX/PDF logs for render regressions."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


_UNDEFINED_RE = re.compile(
    r"(undefined references|Reference [`'][^`']+[''] on page \d+ undefined|"
    r"Hyper reference [`'][^`']+[''] on page \d+ undefined)",
    re.IGNORECASE,
)
_OVERFULL_RE = re.compile(
    r"Overfull \\(?P<box>[hv])box \((?P<points>\d+(?:\.\d+)?)pt too "
    r"(?P<direction>wide|high)\)",
)
_MISSING_CHARACTER_RE = re.compile(r"Missing character:")


@dataclass(frozen=True)
class PdfLogIssue:
    """One PDF log issue found by the checker."""

    line_no: int
    message: str


def find_pdf_log_issues(
    log_text: str, *, max_overfull_pt: float = 50.0, max_overfull_vbox_pt: float | None = None
) -> list[PdfLogIssue]:
    """Return undefined-reference, missing-glyph, and severe-overfull-box issues."""
    issues: list[PdfLogIssue] = []
    effective_vbox_pt = max_overfull_vbox_pt if max_overfull_vbox_pt is not None else max_overfull_pt
    for line_no, line in enumerate(log_text.splitlines(), start=1):
        if _UNDEFINED_RE.search(line):
            issues.append(PdfLogIssue(line_no, line.strip()))
            continue
        if _MISSING_CHARACTER_RE.search(line):
            issues.append(PdfLogIssue(line_no, line.strip()))
            continue
        match = _OVERFULL_RE.search(line)
        if match is None:
            continue
        points = float(match.group("points"))
        box_type = match.group("box")
        limit = effective_vbox_pt if box_type == "v" else max_overfull_pt
        if points > limit:
            issues.append(PdfLogIssue(line_no, line.strip()))
    return issues


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path, help="Path to a XeLaTeX or combined manuscript log")
    parser.add_argument("--max-overfull-pt", type=float, default=50.0)
    parser.add_argument("--max-overfull-vbox-pt", type=float, default=350.0)
    args = parser.parse_args(argv)

    if not args.log.is_file():
        print(f"PDF log not found: {args.log}", file=sys.stderr)
        return 2
    issues = find_pdf_log_issues(
        args.log.read_text(encoding="utf-8", errors="replace"),
        max_overfull_pt=args.max_overfull_pt,
        max_overfull_vbox_pt=args.max_overfull_vbox_pt,
    )
    if not issues:
        print(
            "[PASS] no undefined references, missing glyphs, "
            f"or overfull boxes (hbox > {args.max_overfull_pt:g}pt, "
            f"vbox > {args.max_overfull_vbox_pt:g}pt)"
        )
        return 0
    print(f"[FAIL] PDF log issues found: {len(issues)}", file=sys.stderr)
    for issue in issues[:40]:
        print(f"  line {issue.line_no}: {issue.message}", file=sys.stderr)
    if len(issues) > 40:
        print(f"  ... {len(issues) - 40} additional issue(s)", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(run())
