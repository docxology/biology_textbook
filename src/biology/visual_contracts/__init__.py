"""Generate and check the biology textbook visual contract manifest."""

from __future__ import annotations

from biology.visual_contracts.audit import check_records
from biology.visual_contracts.manifest import build_manifest, write_manifest, write_review_matrix
from biology.visual_contracts.models import Finding, VisualRecord
from biology.visual_contracts.render import render_inline_mermaid_assets
from biology.visual_contracts.scan import (
    inline_mermaid_records,
    raw_figure_records,
    registered_mermaid_records,
)

__all__ = [
    "Finding",
    "VisualRecord",
    "build_manifest",
    "check_records",
    "inline_mermaid_records",
    "raw_figure_records",
    "registered_mermaid_records",
    "render_inline_mermaid_assets",
    "write_manifest",
    "write_review_matrix",
]
