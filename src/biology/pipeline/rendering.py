"""Render the live textbook using read-only, externally supplied template code."""

from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

from biology.pipeline.collection import collect_ordered_chapters, load_config
from biology.pipeline.injection import inject_chapters_for_rendering
from biology.pipeline.paths import OUTPUT_DIR, PROJECT_ROOT
from biology.visual_contracts.render import render_inline_mermaid_assets
from biology.visual_contracts.scan import inline_stem, normalise_inline_mermaid_source
from textbook_io import write_text_atomic
from textbook_paths import discover_template_root, require_project_output_directory


def _inline_diagram_bounds(path: Path) -> tuple[int, int, int, int]:
    """Find visible PNG content plus two pixels, excluding white/transparent padding."""
    from PIL import Image, ImageChops

    with Image.open(path) as image:
        canvas = Image.new("RGBA", image.size, "white")
        canvas.alpha_composite(image.convert("RGBA"))
        background = Image.new("RGB", image.size, "white")
        bounds = ImageChops.difference(canvas.convert("RGB"), background).getbbox()
        if bounds is None:
            raise ValueError(f"Inline Mermaid PNG contains no visible diagram: {path}")
        left, top, right, bottom = bounds
        return max(0, left - 2), max(0, top - 2), min(image.width, right + 2), min(image.height, bottom + 2)


def _prepare_inline_diagrams(sources: list[Path], assets: list[Path]) -> None:
    """Bind hydrated fences to audited PNGs and fit visible content, not square padding."""
    from infrastructure.rendering._pdf_mermaid import (  # type: ignore[import-not-found]
        _MERMAID_BLOCK_RE,
        inline_mermaid_figure_markdown,
    )
    from PIL import Image

    index = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal index
        source = normalise_inline_mermaid_source(match.group("source").strip())
        expected = inline_stem(index + 1, source)
        if index >= len(assets) or assets[index].stem != expected:
            raise RuntimeError(f"Hydrated Mermaid source does not match rendered asset {expected}")
        path = assets[index]
        index += 1
        markup = str(inline_mermaid_figure_markdown(match, path.name))
        image_start = markup.find(r"\includegraphics[")
        alt_start = markup.find("alt={", image_start)
        if markup.count(r"\includegraphics[") != 1 or image_start < 0 or alt_start < 0:
            raise RuntimeError("Installed renderer changed its inline image/alt emission contract")
        left, top, right, bottom = _inline_diagram_bounds(path)
        with Image.open(path) as image:
            dpi_x, dpi_y = image.info.get("dpi", (72.0, 72.0))
            if dpi_x <= 0 or dpi_y <= 0:
                raise ValueError(f"Inline Mermaid PNG has an invalid resolution: {path}")
            trim = (left * 72 / dpi_x, (image.height - bottom) * 72 / dpi_y,
                    (image.width - right) * 72 / dpi_x, top * 72 / dpi_y)
        # Print at 144 raster pixels per inch or denser; never enlarge a tiny graph
        # to fill a page. The original square PNG and its audited hash stay intact.
        width, height = (right - left) / 2, (bottom - top) / 2
        options = (
            "trim={" + " ".join(f"{value:.6f}bp" for value in trim) + "},clip,"
            rf"width={{\ifdim {width:.6f}bp<0.96\linewidth {width:.6f}bp\else0.96\linewidth\fi}},"
            rf"height={{\ifdim {height:.6f}bp<8.5in {height:.6f}bp\else8.5in\fi}},keepaspectratio,"
        )
        return markup[:image_start] + r"\includegraphics[" + options + markup[alt_start:]

    for path in sources:
        content = path.read_text(encoding="utf-8")
        replaced = _MERMAID_BLOCK_RE.sub(replace, content)
        if replaced != content:
            write_text_atomic(path, replaced)
    if index != len(assets):
        raise RuntimeError("Rendered Mermaid assets do not match the hydrated manuscript")


def render_textbook() -> Path:
    """Hydrate live sources and render exclusively into this project's output tree.

    The template is a library dependency, never a working directory or output
    destination. Publication requires real PNG diagrams, not verbatim fallbacks.
    """
    output = require_project_output_directory(PROJECT_ROOT, PROJECT_ROOT / "output")
    require_project_output_directory(PROJECT_ROOT, OUTPUT_DIR)
    figures = require_project_output_directory(PROJECT_ROOT, output / "figures")
    require_project_output_directory(PROJECT_ROOT, figures / "mermaid_inline")
    pdf_dir = require_project_output_directory(PROJECT_ROOT, output / "pdf")
    template = discover_template_root(PROJECT_ROOT)
    if template is None:
        raise RuntimeError("Set BIOLOGY_TEXTBOOK_TEMPLATE_ROOT to an installed template checkout")
    if shutil.which("mmdc") is None:
        raise RuntimeError("Mermaid CLI 'mmdc' is required for textbook PDF rendering")

    from infrastructure.rendering.config import RenderingConfig  # type: ignore[import-not-found]
    from infrastructure.rendering.pdf_renderer import PDFRenderer  # type: ignore[import-not-found]
    from PIL import Image

    config = load_config()
    chapters = collect_ordered_chapters(config)
    export = config.get("export", {})
    include_solutions = export.get("include_solutions", False) or os.environ.get("BIOLOGY_INCLUDE_SOLUTIONS") == "1"
    inject_chapters_for_rendering(
        chapters,
        include_solutions=include_solutions,
        watermark_instructor=export.get("watermark_instructor", False),
    )
    sources = sorted(path for path in OUTPUT_DIR.glob("*.md") if path.name != "preamble.md")
    inline_pngs = render_inline_mermaid_assets(figures)
    _prepare_inline_diagrams(sources, inline_pngs)
    renderer = PDFRenderer(RenderingConfig(
        manuscript_dir=str(OUTPUT_DIR),
        figures_dir=str(figures),
        output_dir=str(output),
        pdf_dir=str(pdf_dir),
        template_dir=str(template / "infrastructure" / "rendering" / "templates"),
    ))
    pdf = renderer.render_combined(sources, OUTPUT_DIR, project_name="biology_textbook")
    # The backend receives PNG figures, so a failed Mermaid render cannot
    # silently become verbatim source or change the audited asset identities.
    for path in inline_pngs:
        with Image.open(path) as image:
            if image.format != "PNG":
                raise RuntimeError(f"Not a PNG diagram: {path}")
            image.verify()
    return pdf
