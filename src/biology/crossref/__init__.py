"""Cross-reference validation and label insertion for the biology textbook manuscript."""

from biology.crossref.helpers import suggest_id
from biology.crossref.label_insertion import (
    ChapterInfo,
    RewriteReport,
    apply_crossref_labels,
    load_chapters,
)
from biology.crossref.models import CrossRefIssue, CrossRefProblem, CrossRefReport
from biology.crossref.scan_file import scan_file
from biology.crossref.validator import scan_directory, validate

__all__ = [
    "ChapterInfo",
    "CrossRefIssue",
    "CrossRefProblem",
    "CrossRefReport",
    "RewriteReport",
    "apply_crossref_labels",
    "load_chapters",
    "scan_directory",
    "scan_file",
    "suggest_id",
    "validate",
]
