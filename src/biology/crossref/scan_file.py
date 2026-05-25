"""Single-file manuscript cross-reference scanning."""

from __future__ import annotations

import re
from pathlib import Path

from biology.crossref.helpers import generated_block_lines, suggest_id
from biology.crossref.models import CrossRefIssue
from biology.crossref.patterns import (
    RE_DISPLAY_EQ_OPEN,
    RE_EQ_ID,
    RE_EQ_TAG,
    RE_FENCE,
    RE_FIG_ID,
    RE_HEADING,
    RE_IMG,
    RE_INLINE_DISPLAY_EQ,
    RE_LATEX_EQ_END,
    RE_LATEX_EQ_OPEN,
    RE_LATEX_FIG_END,
    RE_LATEX_FIG_OPEN,
    RE_LATEX_INCLUDE,
    RE_LATEX_LABEL,
    RE_LATEX_TBL_END,
    RE_LATEX_TBL_OPEN,
    RE_PROSE_XREF,
    RE_RAW_LATEX_REF,
    RE_REF_USE,
    RE_SEC_ID,
    RE_TBL_CAPTION,
    RE_TBL_ID,
)


def scan_file(path: Path) -> tuple[dict[tuple[str, str], int], list[tuple[str, str, int]], list[CrossRefIssue]]:
    """Scan a single markdown file for cross-reference definitions and uses."""
    defined: dict[tuple[str, str], int] = {}
    references: list[tuple[str, str, int]] = []
    issues: list[CrossRefIssue] = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:  # pragma: no cover - unreadable file is a hard error
        issues.append(
            CrossRefIssue(file=path, line=0, kind="file", problem="missing_id", context=f"could not read file: {exc}")
        )
        return defined, references, issues

    lines = text.splitlines()
    generated_lines = generated_block_lines(text)

    in_display_eq = False
    in_latex_eq = False
    in_latex_fig = False
    in_latex_tbl = False
    eq_buffer: list[str] = []
    fig_buffer: list[str] = []
    tbl_buffer: list[str] = []
    eq_start_line = 0
    fig_start_line = 0
    tbl_start_line = 0
    eq_ordinal = 0
    fig_ordinal = 0
    tbl_ordinal = 0
    in_code_fence = False
    code_fence_lang = ""

    def _record_latex_equation_block(block: str, start_line: int) -> None:
        nonlocal eq_ordinal
        eq_ordinal += 1
        label_match = RE_LATEX_LABEL.search(block)
        if label_match and label_match.group("kind") == "eq":
            defined[("eq", label_match.group("id"))] = start_line
        else:
            issues.append(
                CrossRefIssue(
                    file=path,
                    line=start_line,
                    kind="equation",
                    problem="missing_id",
                    suggested_id=suggest_id("eq", path, "", eq_ordinal),
                    context=block.splitlines()[0],
                )
            )

    for i, line in enumerate(lines, start=1):
        fence_match = RE_FENCE.match(line)
        if fence_match:
            if in_code_fence:
                in_code_fence = False
                code_fence_lang = ""
            else:
                in_code_fence = True
                code_fence_lang = fence_match.group("lang").lower()
            continue

        visible_for_xref_check = not in_code_fence or code_fence_lang == "mermaid"
        if visible_for_xref_check and i not in generated_lines and RE_EQ_TAG.search(line):
            issues.append(
                CrossRefIssue(
                    file=path,
                    line=i,
                    kind="equation",
                    problem="hardcoded_equation_tag",
                    context=line.strip()[:120],
                )
            )

        if RE_LATEX_FIG_OPEN.search(line):
            in_latex_fig = True
            fig_buffer = [line]
            fig_start_line = i
            continue
        if in_latex_fig:
            fig_buffer.append(line)
            if RE_LATEX_FIG_END.search(line):
                fig_ordinal += 1
                block = "\n".join(fig_buffer)
                label_match = RE_LATEX_LABEL.search(block)
                if label_match and label_match.group("kind") == "fig":
                    defined[("fig", label_match.group("id"))] = fig_start_line
                else:
                    inc_match = RE_LATEX_INCLUDE.search(block)
                    desc = Path(inc_match.group("path")).stem if inc_match else f"fig-{fig_ordinal}"
                    issues.append(
                        CrossRefIssue(
                            file=path,
                            line=fig_start_line,
                            kind="figure",
                            problem="missing_id",
                            suggested_id=suggest_id("fig", path, desc, fig_ordinal),
                            context=block.splitlines()[0],
                        )
                    )
                in_latex_fig = False
                fig_buffer = []
            continue

        if RE_LATEX_TBL_OPEN.search(line):
            in_latex_tbl = True
            tbl_buffer = [line]
            tbl_start_line = i
            continue
        if in_latex_tbl:
            tbl_buffer.append(line)
            if RE_LATEX_TBL_END.search(line):
                tbl_ordinal += 1
                block = "\n".join(tbl_buffer)
                label_match = RE_LATEX_LABEL.search(block)
                if label_match and label_match.group("kind") == "tbl":
                    defined[("tbl", label_match.group("id"))] = tbl_start_line
                    if r"\caption{" not in block:
                        issues.append(
                            CrossRefIssue(
                                file=path,
                                line=tbl_start_line,
                                kind="table",
                                problem="missing_caption",
                                suggested_id=label_match.group("id"),
                                context=block.splitlines()[0],
                            )
                        )
                else:
                    issues.append(
                        CrossRefIssue(
                            file=path,
                            line=tbl_start_line,
                            kind="table",
                            problem="missing_id",
                            suggested_id=suggest_id("tbl", path, "", tbl_ordinal),
                            context=block.splitlines()[0],
                        )
                    )
                in_latex_tbl = False
                tbl_buffer = []
            continue

        inline_eq = RE_INLINE_DISPLAY_EQ.match(line)
        if inline_eq and not in_display_eq and not in_latex_eq:
            eq_ordinal += 1
            body = inline_eq.group("body")
            label_match = RE_LATEX_LABEL.search(body)
            eq_attr = RE_EQ_ID.search(body)
            tag_match = RE_EQ_TAG.search(body)
            if tag_match and label_match:
                issues.append(
                    CrossRefIssue(
                        file=path,
                        line=i,
                        kind="equation",
                        problem="tag_label_dollar_equation",
                        suggested_id=label_match.group("id"),
                        context=line.strip()[:120],
                    )
                )
            if eq_attr:
                defined[("eq", eq_attr.group("id"))] = i
            elif label_match and label_match.group("kind") == "eq":
                defined[("eq", label_match.group("id"))] = i
            else:
                issues.append(
                    CrossRefIssue(
                        file=path,
                        line=i,
                        kind="equation",
                        problem="missing_id",
                        suggested_id=suggest_id("eq", path, "", eq_ordinal),
                        context=line.strip()[:120],
                    )
                )
            continue

        heading_match = RE_HEADING.match(line)
        if heading_match and not in_display_eq and not in_latex_eq:
            attrs = heading_match.group("attrs") or ""
            sec_match = RE_SEC_ID.search(attrs)
            if sec_match:
                sid = sec_match.group("id")
                if ("sec", sid) in defined:
                    issues.append(
                        CrossRefIssue(
                            file=path, line=i, kind="section", problem="duplicate", suggested_id=sid, context=line
                        )
                    )
                defined[("sec", sid)] = i

        for fig_match in RE_IMG.finditer(line):
            fig_ordinal += 1
            attrs = fig_match.group("attrs") or ""
            fid_match = RE_FIG_ID.search(attrs)
            if fid_match:
                fid = fid_match.group("id")
                if ("fig", fid) in defined:
                    issues.append(
                        CrossRefIssue(
                            file=path, line=i, kind="figure", problem="duplicate", suggested_id=fid, context=line
                        )
                    )
                defined[("fig", fid)] = i
            else:
                desc = fig_match.group("alt") or Path(fig_match.group("path")).stem
                issues.append(
                    CrossRefIssue(
                        file=path,
                        line=i,
                        kind="figure",
                        problem="missing_id",
                        suggested_id=suggest_id("fig", path, desc, fig_ordinal),
                        context=line,
                    )
                )

        if RE_DISPLAY_EQ_OPEN.match(line):
            if not in_display_eq:
                in_display_eq = True
                eq_buffer = [line]
                eq_start_line = i
            else:
                eq_buffer.append(line)
                eq_ordinal += 1
                block = "\n".join(eq_buffer)
                eq_match = RE_EQ_ID.search(block)
                label_match = RE_LATEX_LABEL.search(block)
                if eq_match:
                    defined[("eq", eq_match.group("id"))] = eq_start_line
                elif label_match and label_match.group("kind") == "eq":
                    defined[("eq", label_match.group("id"))] = eq_start_line
                else:
                    nxt = lines[i] if i < len(lines) else ""
                    nxt_match = RE_EQ_ID.search(nxt)
                    if nxt_match:
                        defined[("eq", nxt_match.group("id"))] = eq_start_line
                    else:
                        issues.append(
                            CrossRefIssue(
                                file=path,
                                line=eq_start_line,
                                kind="equation",
                                problem="missing_id",
                                suggested_id=suggest_id("eq", path, "", eq_ordinal),
                                context=eq_buffer[1] if len(eq_buffer) > 1 else block,
                            )
                        )
                in_display_eq = False
                eq_buffer = []
            continue

        if in_display_eq:
            eq_buffer.append(line)
            continue

        if RE_LATEX_EQ_OPEN.search(line):
            eq_buffer = [line]
            eq_start_line = i
            if RE_LATEX_EQ_END.search(line):
                _record_latex_equation_block(line, eq_start_line)
                eq_buffer = []
            else:
                in_latex_eq = True
            continue
        if in_latex_eq:
            eq_buffer.append(line)
            if RE_LATEX_EQ_END.search(line):
                _record_latex_equation_block("\n".join(eq_buffer), eq_start_line)
                in_latex_eq = False
                eq_buffer = []
            continue

        if line.lstrip().startswith("Table:") or line.lstrip().startswith(": "):
            table_match = RE_TBL_CAPTION.match(line.strip())
            if table_match:
                tbl_ordinal += 1
                attrs = table_match.group("attrs") or ""
                tid_match = RE_TBL_ID.search(attrs)
                if tid_match:
                    defined[("tbl", tid_match.group("id"))] = i
                else:
                    caption = table_match.group("caption").strip()
                    issues.append(
                        CrossRefIssue(
                            file=path,
                            line=i,
                            kind="table",
                            problem="missing_id",
                            suggested_id=suggest_id("tbl", path, caption, tbl_ordinal),
                            context=line,
                        )
                    )

        for ref_match in RE_REF_USE.finditer(line):
            references.append((ref_match.group("kind"), ref_match.group("id"), i))

        if (
            visible_for_xref_check
            and i not in generated_lines
            and not line.startswith("#")
            and not line.lstrip().startswith("%")
            and not re.match(r"^>\s*\*\*(?:Ch|Appendix)\s+[A-Za-z0-9.]+", line.strip())
            and (RE_PROSE_XREF.search(line) or RE_RAW_LATEX_REF.search(line))
        ):
            issues.append(CrossRefIssue(file=path, line=i, kind="ref", problem="prose_xref", context=line.strip()))

    return defined, references, issues


__all__ = ["scan_file"]
