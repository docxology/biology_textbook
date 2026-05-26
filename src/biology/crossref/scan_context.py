"""Mutable per-file scan state for cross-reference parsing."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from biology.crossref.helpers import suggest_id
from biology.crossref.models import CrossRefIssue
from biology.crossref.patterns import RE_LATEX_LABEL


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
    in_code_fence: bool = False
    code_fence_lang: str = ""

    def record_latex_equation_block(self, block: str, start_line: int) -> None:
        self.eq_ordinal += 1
        label_match = RE_LATEX_LABEL.search(block)
        if label_match and label_match.group("kind") == "eq":
            self.defined[("eq", label_match.group("id"))] = start_line
        else:
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

    @property
    def visible_for_xref_check(self) -> bool:
        return not self.in_code_fence or self.code_fence_lang == "mermaid"
