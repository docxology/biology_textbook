"""CLI for visual contract manifest auditing."""

from __future__ import annotations

import argparse
from pathlib import Path

from biology.visual_contracts import (
    build_manifest,
    check_records,
    render_inline_mermaid_assets,
    write_manifest,
    write_review_matrix,
)
from biology.visual_contracts_paths import DEFAULT_MANIFEST


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate and check the biology visual manifest")
    parser.add_argument("--output", type=Path, default=DEFAULT_MANIFEST, help="Manifest JSON output path")
    parser.add_argument(
        "--figures-root",
        type=Path,
        default=DEFAULT_MANIFEST.parent,
        help="Root containing generated figures, mermaid/, and mermaid_inline/ assets",
    )
    parser.add_argument(
        "--review-matrix",
        type=Path,
        default=None,
        help="Optional Markdown review matrix path",
    )
    parser.add_argument(
        "--render-inline",
        action="store_true",
        help="Render all inline Mermaid fences into figures-root/mermaid_inline before auditing",
    )
    parser.add_argument("--check", action="store_true", help="Fail if visual contract findings are present")
    args = parser.parse_args(argv)

    if args.render_inline:
        render_inline_mermaid_assets(args.figures_root)

    records = build_manifest(args.figures_root)
    manifest_path = write_manifest(records, args.output)
    matrix_path = write_review_matrix(
        records,
        args.review_matrix or args.output.with_name("visual_review_matrix.md"),
    )
    findings = check_records(records)

    print(f"[audit_visual_contracts] manifest: {manifest_path}")
    print(f"[audit_visual_contracts] review_matrix: {matrix_path}")
    print(f"[audit_visual_contracts] records: {len(records)}")
    if findings:
        for finding in findings:
            print(f"{finding.code}: {finding.source_path}:{finding.line}: {finding.detail}")
    else:
        print("[audit_visual_contracts] visual contracts clean")
    return 1 if args.check and findings else 0


__all__ = ["main"]
