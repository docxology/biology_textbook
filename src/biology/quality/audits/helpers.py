"""Shared helper functions for quality audit modules."""

from __future__ import annotations

import re
from pathlib import Path

from biology.maintenance.manuscript_walker import configured_chapter_title_by_path
from biology.quality.models import Finding
from biology.crossref.helpers import generated_block_lines
from biology.quality.patterns import (
    COMPANION_SOURCE_MODULE_HEADING_RE,
    PAPER_EVIDENCE_UPGRADE_HEADING_RE,
)


def _first_occurrence_line(text: str, needle: str) -> int:
    for line_no, line in enumerate(text.splitlines(), start=1):
        if needle in line:
            return line_no
    raise ValueError(f"needle not found: {needle}")


def _paper_evidence_upgrade_body(text: str) -> str | None:
    match = PAPER_EVIDENCE_UPGRADE_HEADING_RE.search(text)
    if match is None:
        return None
    body_start = match.end()
    if text[body_start:body_start + 2] == "\r\n":
        body_start += 2
    elif text[body_start:body_start + 1] in {"\r", "\n"}:
        body_start += 1
    next_heading = re.search(r"^## ", text[body_start:], flags=re.MULTILINE)
    if next_heading is None:
        return text[body_start:]
    body_end = body_start + next_heading.start()
    return text[body_start:body_end]


def _companion_source_module_body(text: str) -> str | None:
    match = COMPANION_SOURCE_MODULE_HEADING_RE.search(text)
    if match is None:
        return None
    body_start = match.end()
    if text[body_start:body_start + 2] == "\r\n":
        body_start += 2
    elif text[body_start:body_start + 1] in {"\r", "\n"}:
        body_start += 1
    next_heading = re.search(r"^#{1,3} ", text[body_start:], flags=re.MULTILINE)
    if next_heading is None:
        return text[body_start:]
    body_end = body_start + next_heading.start()
    return text[body_start:body_end]


def _generated_block_line_numbers(path: Path) -> set[int]:
    """Return line numbers owned by approved generated manuscript blocks."""
    text = path.read_text(encoding="utf-8")
    return generated_block_lines(text)


def add_line_findings(
    findings: list[Finding],
    *,
    path: Path,
    line_no: int,
    line: str,
    patterns: tuple[tuple[str, re.Pattern[str]], ...],
    severity: str = "error",
) -> None:
    for code, pattern in patterns:
        if pattern.search(line):
            findings.append(Finding(severity, code, path, line_no, line.strip()))


__all__ = [
    "_companion_source_module_body",
    "_first_occurrence_line",
    "_generated_block_line_numbers",
    "_paper_evidence_upgrade_body",
    "add_line_findings",
    "configured_chapter_title_by_path",
]
