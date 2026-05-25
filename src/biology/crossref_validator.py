"""Backward-compatible re-export of :mod:`biology.crossref`."""

from biology.crossref import (
    CrossRefIssue,
    CrossRefReport,
    scan_directory,
    scan_file,
    suggest_id,
    validate,
)

__all__ = [
    "CrossRefIssue",
    "CrossRefReport",
    "scan_directory",
    "scan_file",
    "suggest_id",
    "validate",
]
