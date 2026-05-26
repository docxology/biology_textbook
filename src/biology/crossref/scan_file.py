"""Single-file manuscript cross-reference scanning."""

from __future__ import annotations

from pathlib import Path

from biology.crossref.helpers import generated_block_lines
from biology.crossref.models import CrossRefIssue
from biology.crossref.scan_latex_envs import (
    process_inline_display_equation,
    process_latex_equation_env,
    process_latex_figure,
    process_latex_table,
)
from biology.crossref.scan_markdown_ids import (
    process_block_display_equation,
    process_code_fence,
    process_heading,
    process_markdown_images,
    process_pipe_table_caption,
)
from biology.crossref.scan_ref_uses import (
    process_hardcoded_equation_tag,
    process_prose_xrefs,
    process_ref_uses,
)

from .scan_context import ScanContext


def scan_file(path: Path) -> tuple[dict[tuple[str, str], int], list[tuple[str, str, int]], list[CrossRefIssue]]:
    """Scan a single markdown file for cross-reference definitions and uses."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:  # pragma: no cover - unreadable file is a hard error
        return (
            {},
            [],
            [
                CrossRefIssue(
                    file=path,
                    line=0,
                    kind="file",
                    problem="missing_id",
                    context=f"could not read file: {exc}",
                )
            ],
        )

    lines = text.splitlines()
    ctx = ScanContext(path=path, lines=lines, generated_lines=generated_block_lines(text))

    for line_no, line in enumerate(lines, start=1):
        if process_code_fence(ctx, line):
            continue

        process_hardcoded_equation_tag(ctx, line_no, line)

        if process_latex_figure(ctx, line_no, line):
            continue
        if process_latex_table(ctx, line_no, line):
            continue
        if process_inline_display_equation(ctx, line_no, line):
            continue

        process_heading(ctx, line_no, line)
        process_markdown_images(ctx, line_no, line)

        if process_block_display_equation(ctx, line_no, line):
            continue
        if process_latex_equation_env(ctx, line_no, line):
            continue

        process_pipe_table_caption(ctx, line_no, line)
        process_ref_uses(ctx, line_no, line)
        process_prose_xrefs(ctx, line_no, line)

    return ctx.defined, ctx.references, ctx.issues


__all__ = ["scan_file"]
