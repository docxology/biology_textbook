"""Generate and check the biology textbook visual contract manifest."""

from __future__ import annotations

from biology.visual_contracts.audit import check_records, contrast_ratio as _contrast_ratio
from biology.visual_contracts.helpers import (
    dimensions as _dimensions,
    first_alt_after as _first_alt_after,
    first_caption_after_mermaid as _first_caption_after_mermaid,
)
from biology.visual_contracts.manifest import (
    build_manifest,
    review_action as _review_action,
    write_manifest,
    write_review_matrix,
)
from biology.visual_contracts.models import Finding, VisualRecord
from biology.visual_contracts.render import render_inline_mermaid_assets
from biology.visual_contracts.scan import (
    inline_mermaid_records,
    normalise_inline_mermaid_source as _normalise_inline_mermaid_source,
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
    "_contrast_ratio",
    "_dimensions",
    "_first_alt_after",
    "_first_caption_after_mermaid",
    "_normalise_inline_mermaid_source",
    "_review_action",
]
