"""LaTeX environment handlers for ``scan_file``."""

from __future__ import annotations

from pathlib import Path

from biology.crossref.helpers import suggest_id
from biology.crossref.models import CrossRefIssue
from biology.crossref.patterns import (
    RE_EQ_ID,
    RE_EQ_TAG,
    RE_INLINE_DISPLAY_EQ,
    RE_LATEX_EQ_END,
    RE_LATEX_EQ_OPEN,
    RE_LATEX_FIG_END,
    RE_LATEX_FIG_OPEN,
    RE_LATEX_INCLUDE,
    RE_LATEX_LABEL,
    RE_LATEX_TBL_END,
    RE_LATEX_TBL_OPEN,
)

from .scan_context import ScanContext


def process_latex_figure(ctx: ScanContext, line_no: int, line: str) -> bool:
    if RE_LATEX_FIG_OPEN.search(line):
        ctx.in_latex_fig = True
        ctx.fig_buffer = [line]
        ctx.fig_start_line = line_no
        return True
    if ctx.in_latex_fig:
        ctx.fig_buffer.append(line)
        if RE_LATEX_FIG_END.search(line):
            ctx.fig_ordinal += 1
            block = "\n".join(ctx.fig_buffer)
            label_match = RE_LATEX_LABEL.search(block)
            if label_match and label_match.group("kind") == "fig":
                ctx.defined[("fig", label_match.group("id"))] = ctx.fig_start_line
            else:
                inc_match = RE_LATEX_INCLUDE.search(block)
                desc = Path(inc_match.group("path")).stem if inc_match else f"fig-{ctx.fig_ordinal}"
                ctx.issues.append(
                    CrossRefIssue(
                        file=ctx.path,
                        line=ctx.fig_start_line,
                        kind="figure",
                        problem="missing_id",
                        suggested_id=suggest_id("fig", ctx.path, desc, ctx.fig_ordinal),
                        context=block.splitlines()[0],
                    )
                )
            ctx.in_latex_fig = False
            ctx.fig_buffer = []
        return True
    return False


def process_latex_table(ctx: ScanContext, line_no: int, line: str) -> bool:
    if RE_LATEX_TBL_OPEN.search(line):
        ctx.in_latex_tbl = True
        ctx.tbl_buffer = [line]
        ctx.tbl_start_line = line_no
        return True
    if ctx.in_latex_tbl:
        ctx.tbl_buffer.append(line)
        if RE_LATEX_TBL_END.search(line):
            ctx.tbl_ordinal += 1
            block = "\n".join(ctx.tbl_buffer)
            label_match = RE_LATEX_LABEL.search(block)
            if label_match and label_match.group("kind") == "tbl":
                ctx.defined[("tbl", label_match.group("id"))] = ctx.tbl_start_line
                if r"\caption{" not in block:
                    ctx.issues.append(
                        CrossRefIssue(
                            file=ctx.path,
                            line=ctx.tbl_start_line,
                            kind="table",
                            problem="missing_caption",
                            suggested_id=label_match.group("id"),
                            context=block.splitlines()[0],
                        )
                    )
            else:
                ctx.issues.append(
                    CrossRefIssue(
                        file=ctx.path,
                        line=ctx.tbl_start_line,
                        kind="table",
                        problem="missing_id",
                        suggested_id=suggest_id("tbl", ctx.path, "", ctx.tbl_ordinal),
                        context=block.splitlines()[0],
                    )
                )
            ctx.in_latex_tbl = False
            ctx.tbl_buffer = []
        return True
    return False


def process_inline_display_equation(ctx: ScanContext, line_no: int, line: str) -> bool:
    inline_eq = RE_INLINE_DISPLAY_EQ.match(line)
    if not inline_eq or ctx.in_display_eq or ctx.in_latex_eq:
        return False
    ctx.eq_ordinal += 1
    body = inline_eq.group("body")
    label_match = RE_LATEX_LABEL.search(body)
    eq_attr = RE_EQ_ID.search(body)
    tag_match = RE_EQ_TAG.search(body)
    if tag_match and label_match:
        ctx.issues.append(
            CrossRefIssue(
                file=ctx.path,
                line=line_no,
                kind="equation",
                problem="tag_label_dollar_equation",
                suggested_id=label_match.group("id"),
                context=line.strip()[:120],
            )
        )
    if eq_attr:
        ctx.defined[("eq", eq_attr.group("id"))] = line_no
    elif label_match and label_match.group("kind") == "eq":
        ctx.defined[("eq", label_match.group("id"))] = line_no
    else:
        ctx.issues.append(
            CrossRefIssue(
                file=ctx.path,
                line=line_no,
                kind="equation",
                problem="missing_id",
                suggested_id=suggest_id("eq", ctx.path, "", ctx.eq_ordinal),
                context=line.strip()[:120],
            )
        )
    return True


def process_latex_equation_env(ctx: ScanContext, line_no: int, line: str) -> bool:
    if RE_LATEX_EQ_OPEN.search(line):
        ctx.eq_buffer = [line]
        ctx.eq_start_line = line_no
        if RE_LATEX_EQ_END.search(line):
            ctx.record_latex_equation_block(line, ctx.eq_start_line)
            ctx.eq_buffer = []
        else:
            ctx.in_latex_eq = True
        return True
    if ctx.in_latex_eq:
        ctx.eq_buffer.append(line)
        if RE_LATEX_EQ_END.search(line):
            ctx.record_latex_equation_block("\n".join(ctx.eq_buffer), ctx.eq_start_line)
            ctx.in_latex_eq = False
            ctx.eq_buffer = []
        return True
    return False
