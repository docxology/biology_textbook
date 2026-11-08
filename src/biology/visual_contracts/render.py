"""Render inline Mermaid assets for visual contract review."""

from __future__ import annotations

import shutil
from pathlib import Path

from biology.visual_contracts.helpers import ensure_import_paths
from biology.visual_contracts.scan import inline_mermaid_sources, inline_stem
from biology.visual_contracts_paths import OUTPUT_FIGURES, PROJECT_ROOT
from textbook_paths import require_project_output_directory


def render_inline_mermaid_assets(figures_root: Path = OUTPUT_FIGURES) -> list[Path]:
    """Render every inline Mermaid fence to ``figures_root/mermaid_inline``."""
    output_dir = require_project_output_directory(PROJECT_ROOT, figures_root / "mermaid_inline")
    if shutil.which("mmdc") is None:
        raise RuntimeError("Mermaid CLI 'mmdc' is required to render inline Mermaid assets")
    ensure_import_paths()
    from mermaid import MermaidRenderer

    sources = list(inline_mermaid_sources())
    expected = {
        inline_stem(index, source) + suffix
        for index, _path, _line, source in sources
        for suffix in (".mmd", ".png")
    }
    renderer = MermaidRenderer(output_dir=output_dir, strict_png=True)
    for pattern in ("inline_mermaid_*.mmd", "inline_mermaid_*.png"):
        for path in output_dir.glob(pattern):
            if path.name not in expected:
                path.unlink()
    paths: list[Path] = []
    for index, _path, _line, source in sources:
        paths.append(renderer.render(inline_stem(index, source), source, size=1200))
    return paths


__all__ = ["render_inline_mermaid_assets"]
