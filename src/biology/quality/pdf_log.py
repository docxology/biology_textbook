"""XeLaTeX/PDF log parsing for render regression gates."""

from __future__ import annotations

import re
from dataclasses import dataclass

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
_DOUBLE_SUPERSCRIPT_RE = re.compile(r"^! Double superscript\.")


@dataclass(frozen=True)
class PdfLogIssue:
    """One PDF log issue found by the checker."""

    line_no: int
    message: str


def find_pdf_log_issues(
    log_text: str,
    *,
    max_overfull_pt: float = 50.0,
    max_overfull_vbox_pt: float | None = None,
    allow_missing_glyphs: bool = False,
) -> list[PdfLogIssue]:
    """Return undefined-reference, missing-glyph, double-superscript, and severe-overfull-box issues."""
    issues: list[PdfLogIssue] = []
    effective_vbox_pt = max_overfull_vbox_pt if max_overfull_vbox_pt is not None else max_overfull_pt
    for line_no, line in enumerate(log_text.splitlines(), start=1):
        if _UNDEFINED_RE.search(line):
            issues.append(PdfLogIssue(line_no, line.strip()))
            continue
        if _MISSING_CHARACTER_RE.search(line):
            if allow_missing_glyphs:
                continue
            issues.append(PdfLogIssue(line_no, line.strip()))
            continue
        if _DOUBLE_SUPERSCRIPT_RE.search(line):
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


def run_pdf_log_check(
    log_path: Path,
    *,
    max_overfull_pt: float = 50.0,
    max_overfull_vbox_pt: float = 350.0,
    allow_missing_glyphs: bool = False,
) -> int:
    """Check one log file; return process exit code."""
    import sys

    if not log_path.is_file():
        print(f"PDF log not found: {log_path}", file=sys.stderr)
        return 2
    issues = find_pdf_log_issues(
        log_path.read_text(encoding="utf-8", errors="replace"),
        max_overfull_pt=max_overfull_pt,
        max_overfull_vbox_pt=max_overfull_vbox_pt,
        allow_missing_glyphs=allow_missing_glyphs,
    )
    if not issues:
        print(
            "[PASS] no undefined references, missing glyphs, double superscripts, "
            f"or overfull boxes (hbox > {max_overfull_pt:g}pt, "
            f"vbox > {max_overfull_vbox_pt:g}pt)"
        )
        return 0
    print(f"[FAIL] PDF log issues found: {len(issues)}", file=sys.stderr)
    for issue in issues[:40]:
        print(f"  line {issue.line_no}: {issue.message}", file=sys.stderr)
    if len(issues) > 40:
        print(f"  ... {len(issues) - 40} additional issue(s)", file=sys.stderr)
    return 1


__all__ = ["PdfLogIssue", "find_pdf_log_issues", "run_pdf_log_check"]
