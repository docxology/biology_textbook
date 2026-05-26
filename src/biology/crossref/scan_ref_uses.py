"""Reference-use and prose cross-reference handlers for ``scan_file``."""

from __future__ import annotations

import re

from biology.crossref.helpers import strip_canonical_plain_refs
from biology.crossref.models import CrossRefIssue
from biology.crossref.patterns import RE_EQ_TAG, RE_PROSE_XREF, RE_RAW_LATEX_REF, RE_REF_USE

from .scan_context import ScanContext


def process_hardcoded_equation_tag(ctx: ScanContext, line_no: int, line: str) -> None:
    if (
        ctx.visible_for_xref_check
        and line_no not in ctx.generated_lines
        and RE_EQ_TAG.search(line)
    ):
        ctx.issues.append(
            CrossRefIssue(
                file=ctx.path,
                line=line_no,
                kind="equation",
                problem="hardcoded_equation_tag",
                context=line.strip()[:120],
            )
        )


def process_ref_uses(ctx: ScanContext, line_no: int, line: str) -> None:
    for ref_match in RE_REF_USE.finditer(line):
        ctx.references.append((ref_match.group("kind"), ref_match.group("id"), line_no))


def process_prose_xrefs(ctx: ScanContext, line_no: int, line: str) -> None:
    if (
        ctx.visible_for_xref_check
        and line_no not in ctx.generated_lines
        and not line.startswith("#")
        and not line.lstrip().startswith("%")
        and not re.match(r"^>\s*\*\*(?:Ch|Appendix)\s+[A-Za-z0-9.]+", line.strip())
        and (
            RE_PROSE_XREF.search(strip_canonical_plain_refs(line))
            or RE_RAW_LATEX_REF.search(line)
        )
    ):
        ctx.issues.append(
            CrossRefIssue(file=ctx.path, line=line_no, kind="ref", problem="prose_xref", context=line.strip())
        )
