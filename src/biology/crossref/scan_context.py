"""Mutable per-file scan state for cross-reference parsing."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from biology.crossref.helpers import suggest_id
from biology.crossref.models import CrossRefIssue
from biology.crossref.patterns import RE_LATEX_LABEL, reference_key


@dataclass
class ScanContext:
    """Accumulators and buffers for a single ``scan_file`` pass."""

    path: Path
    lines: list[str]
    generated_lines: set[int]
    defined: dict[tuple[str, str], int] = field(default_factory=dict)
    references: list[tuple[str, str, int]] = field(default_factory=list)
    issues: list[CrossRefIssue] = field(default_factory=list)
    in_display_eq: bool = False
    in_latex_eq: bool = False
    in_latex_fig: bool = False
    in_latex_tbl: bool = False
    eq_buffer: list[str] = field(default_factory=list)
    fig_buffer: list[str] = field(default_factory=list)
    tbl_buffer: list[str] = field(default_factory=list)
    eq_start_line: int = 0
    fig_start_line: int = 0
    tbl_start_line: int = 0
    eq_ordinal: int = 0
    fig_ordinal: int = 0
    tbl_ordinal: int = 0

    def record_definitions(self, text: str) -> None:
        """Index all rendered raw/Pandoc definitions, retaining duplicates."""
        cursor = 0
        line_no = 1
        for match in re.finditer(
            r"\\label\s*\{([^{}]*)\}|\{[^{}\n]*?#([^\s{}]+)[^{}\n]*\}", text,
        ):
            line_no += text.count("\n", cursor, match.start())
            cursor = match.start()
            line = self.lines[line_no - 1]
            raw = match.group(1) if match.group(1) is not None else match.group(2)
            target = raw.strip()
            if not target:
                self.issues.append(CrossRefIssue(
                    file=self.path, line=line_no, kind="ref", problem="missing_id", context=line,
                ))
                continue
            key = reference_key(target)
            if key in self.defined:
                self.issues.append(CrossRefIssue(
                    file=self.path, line=line_no,
                    kind={"sec": "section", "fig": "figure", "eq": "equation", "tbl": "table"}.get(key[0], key[0]),
                    problem="duplicate", suggested_id=target, context=line,
                ))
            else:
                self.defined[key] = line_no

    def record_latex_equation_block(self, block: str, start_line: int) -> None:
        self.eq_ordinal += 1
        label_match = RE_LATEX_LABEL.search(block)
        if not label_match or label_match.group("kind") != "eq":
            self.issues.append(
                CrossRefIssue(
                    file=self.path,
                    line=start_line,
                    kind="equation",
                    problem="missing_id",
                    suggested_id=suggest_id("eq", self.path, "", self.eq_ordinal),
                    context=block.splitlines()[0],
                )
            )

