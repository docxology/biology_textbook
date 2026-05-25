"""Manuscript tree validation orchestration."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from biology.crossref.models import CrossRefIssue, CrossRefReport
from biology.crossref.scan_file import scan_file


def scan_directory(root: Path, patterns: Iterable[str] = ("**/*.md",)) -> CrossRefReport:
    """Walk ``root`` and aggregate a :class:`CrossRefReport`."""
    report = CrossRefReport()
    for pat in patterns:
        for path in sorted(root.glob(pat)):
            if not path.is_file():
                continue
            if path.name in {"AGENTS.md", "README.md"}:
                continue
            defined, refs, issues = scan_file(path)
            for kind, crossref_id in defined:
                key = (kind, crossref_id)
                if key in report.defined:
                    report.issues.append(
                        CrossRefIssue(
                            file=path,
                            line=0,
                            kind=kind,
                            problem="duplicate",
                            suggested_id=crossref_id,
                            context=f"also defined in {report.defined[key]}",
                        )
                    )
                else:
                    report.defined[key] = path
            for kind, crossref_id, line_no in refs:
                report.references.append((kind, crossref_id, path, line_no))
            report.issues.extend(issues)

    for kind, crossref_id, path, line_no in report.references:
        if (kind, crossref_id) not in report.defined:
            report.issues.append(
                CrossRefIssue(
                    file=path,
                    line=line_no,
                    kind=kind,
                    problem="unresolved",
                    suggested_id=crossref_id,
                    context=f"@{kind}:{crossref_id}",
                )
            )

    return report


def validate(manuscript_root: Path | str) -> CrossRefReport:
    """Validate an entire manuscript tree and return the aggregate report."""
    return scan_directory(Path(manuscript_root))


__all__ = ["scan_directory", "validate"]
