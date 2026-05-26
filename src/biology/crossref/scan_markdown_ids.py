"""Markdown identity handlers for ``scan_file``."""

from __future__ import annotations

from pathlib import Path

from biology.crossref.helpers import suggest_id
from biology.crossref.models import CrossRefIssue
from biology.crossref.patterns import (
    RE_DISPLAY_EQ_OPEN,
    RE_EQ_ID,
    RE_FENCE,
    RE_FIG_ID,
    RE_HEADING,
    RE_IMG,
    RE_LATEX_LABEL,
    RE_SEC_ID,
    RE_TBL_CAPTION,
    RE_TBL_ID,
)

from .scan_context import ScanContext


def process_code_fence(ctx: ScanContext, line: str) -> bool:
    fence_match = RE_FENCE.match(line)
    if not fence_match:
        return False
    if ctx.in_code_fence:
        ctx.in_code_fence = False
        ctx.code_fence_lang = ""
    else:
        ctx.in_code_fence = True
        ctx.code_fence_lang = fence_match.group("lang").lower()
    return True


def process_heading(ctx: ScanContext, line_no: int, line: str) -> None:
    heading_match = RE_HEADING.match(line)
    if not heading_match or ctx.in_display_eq or ctx.in_latex_eq:
        return
    attrs = heading_match.group("attrs") or ""
    sec_match = RE_SEC_ID.search(attrs)
    if not sec_match:
        return
    sid = sec_match.group("id")
    if ("sec", sid) in ctx.defined:
        ctx.issues.append(
            CrossRefIssue(
                file=ctx.path,
                line=line_no,
                kind="section",
                problem="duplicate",
                suggested_id=sid,
                context=line,
            )
        )
    ctx.defined[("sec", sid)] = line_no


def process_markdown_images(ctx: ScanContext, line_no: int, line: str) -> None:
    for fig_match in RE_IMG.finditer(line):
        ctx.fig_ordinal += 1
        attrs = fig_match.group("attrs") or ""
        fid_match = RE_FIG_ID.search(attrs)
        if fid_match:
            fid = fid_match.group("id")
            if ("fig", fid) in ctx.defined:
                ctx.issues.append(
                    CrossRefIssue(
                        file=ctx.path,
                        line=line_no,
                        kind="figure",
                        problem="duplicate",
                        suggested_id=fid,
                        context=line,
                    )
                )
            ctx.defined[("fig", fid)] = line_no
        else:
            desc = fig_match.group("alt") or Path(fig_match.group("path")).stem
            ctx.issues.append(
                CrossRefIssue(
                    file=ctx.path,
                    line=line_no,
                    kind="figure",
                    problem="missing_id",
                    suggested_id=suggest_id("fig", ctx.path, desc, ctx.fig_ordinal),
                    context=line,
                )
            )


def process_block_display_equation(ctx: ScanContext, line_no: int, line: str) -> bool:
    if not RE_DISPLAY_EQ_OPEN.match(line):
        if ctx.in_display_eq:
            ctx.eq_buffer.append(line)
            return True
        return False
    if not ctx.in_display_eq:
        ctx.in_display_eq = True
        ctx.eq_buffer = [line]
        ctx.eq_start_line = line_no
        return True
    ctx.eq_buffer.append(line)
    ctx.eq_ordinal += 1
    block = "\n".join(ctx.eq_buffer)
    eq_match = RE_EQ_ID.search(block)
    label_match = RE_LATEX_LABEL.search(block)
    if eq_match:
        ctx.defined[("eq", eq_match.group("id"))] = ctx.eq_start_line
    elif label_match and label_match.group("kind") == "eq":
        ctx.defined[("eq", label_match.group("id"))] = ctx.eq_start_line
    else:
        nxt = ctx.lines[line_no] if line_no < len(ctx.lines) else ""
        nxt_match = RE_EQ_ID.search(nxt)
        if nxt_match:
            ctx.defined[("eq", nxt_match.group("id"))] = ctx.eq_start_line
        else:
            ctx.issues.append(
                CrossRefIssue(
                    file=ctx.path,
                    line=ctx.eq_start_line,
                    kind="equation",
                    problem="missing_id",
                    suggested_id=suggest_id("eq", ctx.path, "", ctx.eq_ordinal),
                    context=ctx.eq_buffer[1] if len(ctx.eq_buffer) > 1 else block,
                )
            )
    ctx.in_display_eq = False
    ctx.eq_buffer = []
    return True


def process_pipe_table_caption(ctx: ScanContext, line_no: int, line: str) -> None:
    if not (line.lstrip().startswith("Table:") or line.lstrip().startswith(": ")):
        return
    table_match = RE_TBL_CAPTION.match(line.strip())
    if not table_match:
        return
    ctx.tbl_ordinal += 1
    attrs = table_match.group("attrs") or ""
    tid_match = RE_TBL_ID.search(attrs)
    if tid_match:
        ctx.defined[("tbl", tid_match.group("id"))] = line_no
        return
    caption = table_match.group("caption").strip()
    ctx.issues.append(
        CrossRefIssue(
            file=ctx.path,
            line=line_no,
            kind="table",
            problem="missing_id",
            suggested_id=suggest_id("tbl", ctx.path, caption, ctx.tbl_ordinal),
            context=line,
        )
    )
