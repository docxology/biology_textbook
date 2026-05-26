"""Build and write visual contract manifests."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from biology.visual_contracts.scan import (
    inline_mermaid_records,
    raw_figure_records,
    registered_mermaid_records,
)
from biology.visual_contracts.models import VisualRecord
from biology.visual_contracts_paths import DEFAULT_MANIFEST, OUTPUT_FIGURES
from textbook_io import write_text_atomic


def build_manifest(figures_root: Path = OUTPUT_FIGURES) -> list[VisualRecord]:
    """Return all visual records in a stable order."""
    records = raw_figure_records(figures_root)
    records.extend(registered_mermaid_records(figures_root))
    records.extend(inline_mermaid_records(figures_root))
    return sorted(records, key=lambda r: (r.kind, r.source_path, r.line, r.label))


def write_manifest(records: list[VisualRecord], path: Path = DEFAULT_MANIFEST) -> Path:
    """Write manifest JSON atomically."""
    payload = [asdict(record) for record in records]
    write_text_atomic(path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return path


def aspect_ratio(record: VisualRecord) -> float:
    if not record.width_px or not record.height_px:
        return 0.0
    return record.width_px / record.height_px


def review_action(record: VisualRecord) -> str:
    if record.kind == "raw_figure":
        if record.aspect_policy == "figure-landscape":
            return "landscape matplotlib save helper"
        return "square-padded by matplotlib save helper"
    if record.kind == "registered_mermaid":
        return "square viewport plus PNG padding"
    if record.kind == "inline_mermaid":
        return "rendered through inline Mermaid review path"
    return "measured"


def write_review_matrix(records: list[VisualRecord], path: Path) -> Path:
    """Write a Markdown matrix summarizing every visual record."""
    rows = [
        "# Visual Review Matrix",
        "",
        "| Kind | Label | Source | Asset | Size | Ratio | Policy | Action Taken | Exception |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        ratio = aspect_ratio(record)
        size = f"{record.width_px}x{record.height_px}" if ratio else ""
        ratio_text = f"{ratio:.2f}" if ratio else ""
        action = review_action(record) if ratio else "asset missing"
        exception = record.aspect_exception or ""
        rows.append(
            "| "
            + " | ".join(
                (
                    record.kind,
                    record.label,
                    f"{record.source_path}:{record.line}",
                    record.asset_path,
                    size,
                    ratio_text,
                    record.aspect_policy,
                    action,
                    exception,
                )
            )
            + " |"
        )
    write_text_atomic(path, "\n".join(rows) + "\n")
    return path


__all__ = [
    "aspect_ratio",
    "build_manifest",
    "review_action",
    "write_manifest",
    "write_review_matrix",
]
