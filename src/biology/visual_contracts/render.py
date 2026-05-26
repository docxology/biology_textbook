"""Render inline Mermaid assets for visual contract review."""

from __future__ import annotations

import shutil
from pathlib import Path

from biology.visual_contracts.helpers import ensure_import_paths
from biology.visual_contracts.scan import inline_mermaid_sources, inline_stem
from biology.visual_contracts_paths import OUTPUT_FIGURES


def render_inline_mermaid_assets(figures_root: Path = OUTPUT_FIGURES) -> list[Path]:
    """Render every inline Mermaid fence to ``figures_root/mermaid_inline``."""
    if shutil.which("mmdc") is None:
        raise RuntimeError("Mermaid CLI 'mmdc' is required to render inline Mermaid assets")
    ensure_import_paths()
    from mermaid import MermaidRenderer

    renderer = MermaidRenderer(output_dir=figures_root / "mermaid_inline", strict_png=True)
    paths: list[Path] = []
    for index, _path, _line, source in inline_mermaid_sources():
        paths.append(renderer.render(inline_stem(index, source), source, width=1200, height=1200))
    return paths


__all__ = ["render_inline_mermaid_assets"]
