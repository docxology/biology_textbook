"""Cross-reference validation models."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

CrossRefProblem = Literal[
    "missing_id",
    "missing_caption",
    "unresolved",
    "duplicate",
    "prose_xref",
    "hardcoded_equation_tag",
    "tag_label_dollar_equation",
]


@dataclass(frozen=True)
class CrossRefIssue:
    """A single validation finding."""

    file: Path
    line: int
    kind: str  # "figure" | "equation" | "table" | "section" | "ref" | "file"
    problem: CrossRefProblem | str
    suggested_id: str = ""
    context: str = ""

    def as_row(self) -> dict[str, str]:
        return {
            "file": str(self.file),
            "line": str(self.line),
            "kind": self.kind,
            "problem": str(self.problem),
            "suggested_id": self.suggested_id,
            "context": self.context.replace("\n", " ").strip()[:120],
        }


@dataclass
class CrossRefReport:
    """Aggregate results of a manuscript scan."""

    defined: dict[tuple[str, str], Path] = field(default_factory=dict)
    references: list[tuple[str, str, Path, int]] = field(default_factory=list)
    issues: list[CrossRefIssue] = field(default_factory=list)

    @property
    def missing(self) -> list[CrossRefIssue]:
        return [issue for issue in self.issues if issue.problem == "missing_id"]

    @property
    def missing_captions(self) -> list[CrossRefIssue]:
        return [issue for issue in self.issues if issue.problem == "missing_caption"]

    @property
    def unresolved(self) -> list[CrossRefIssue]:
        return [issue for issue in self.issues if issue.problem == "unresolved"]

    @property
    def duplicates(self) -> list[CrossRefIssue]:
        return [issue for issue in self.issues if issue.problem == "duplicate"]

    @property
    def prose(self) -> list[CrossRefIssue]:
        return [issue for issue in self.issues if issue.problem == "prose_xref"]

    def summary(self) -> str:
        parts = [
            f"defined={len(self.defined)}",
            f"references={len(self.references)}",
            f"missing={len(self.missing)}",
            f"unresolved={len(self.unresolved)}",
            f"duplicates={len(self.duplicates)}",
            f"prose_xrefs={len(self.prose)}",
        ]
        return " ".join(parts)


__all__ = ["CrossRefIssue", "CrossRefProblem", "CrossRefReport"]
