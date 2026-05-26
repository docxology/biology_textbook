"""Scan manuscript and factory sources for visual contract records."""

from __future__ import annotations

import hashlib
import inspect
from collections.abc import Callable, Iterable
from importlib import import_module
from pathlib import Path
from typing import Any

from biology.visual_contracts.helpers import (
    aspect_policy_for_stem,
    dimensions,
    ensure_import_paths,
    first_alt_after,
    first_caption_after_mermaid,
    line_for_offset,
    normalise_space,
    raw_generator_for_asset,
    relative,
)
from biology.visual_contracts.models import (
    VisualRecord,
    _CAPTION_RE,
    _INCLUDE_RE,
    _LABEL_RE,
    _LATEX_FIGURE_RE,
    _MERMAID_RE,
)
from biology.visual_contracts_paths import MANUSCRIPT_DIR, OUTPUT_FIGURES


def raw_figure_records(figures_root: Path = OUTPUT_FIGURES) -> list[VisualRecord]:
    """Extract raw LaTeX figure records from manuscript Markdown."""
    records: list[VisualRecord] = []
    for path in sorted(MANUSCRIPT_DIR.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _LATEX_FIGURE_RE.finditer(text):
            block = match.group(0)
            include = _INCLUDE_RE.search(block)
            caption = _CAPTION_RE.search(block)
            label = _LABEL_RE.search(block)
            if not include and not caption and not label:
                continue
            asset_path = include.group("path") if include else ""
            width, height = dimensions(asset_path, figures_root=figures_root)
            stem = Path(asset_path).stem if asset_path else ""
            records.append(
                VisualRecord(
                    kind="raw_figure",
                    source_path=relative(path),
                    line=line_for_offset(text, match.start()),
                    label=label.group("label") if label else "",
                    caption=normalise_space(caption.group("caption")) if caption else "",
                    alt=first_alt_after(text, match.end()),
                    asset_path=asset_path,
                    generator=raw_generator_for_asset(asset_path) if asset_path else "",
                    width_px=width,
                    height_px=height,
                    aspect_policy=aspect_policy_for_stem(stem),
                )
            )
    return records


def registered_mermaid_factories() -> Iterable[tuple[str, Callable[[], Any], int]]:
    ensure_import_paths()
    import mermaid.biology_diagrams as biology_diagrams
    from mermaid import MermaidDiagram

    for name, factory in inspect.getmembers(biology_diagrams, inspect.isfunction):
        if factory.__module__ != biology_diagrams.__name__:
            continue
        try:
            diagram = factory()
        except TypeError:
            continue
        if not isinstance(diagram, MermaidDiagram):
            continue
        try:
            line = inspect.getsourcelines(factory)[1]
        except OSError:
            line = 1
        yield name, factory, line


def registered_mermaid_records(figures_root: Path = OUTPUT_FIGURES) -> list[VisualRecord]:
    """Build records for Mermaid diagrams registered in Python factories."""
    ensure_import_paths()
    records: list[VisualRecord] = []
    for name, factory, line in registered_mermaid_factories():
        diagram = factory()
        png = figures_root / "mermaid" / f"{diagram.name}.png"
        asset = png if png.exists() else figures_root / "mermaid" / f"{diagram.name}.mmd"
        width, height = dimensions(relative(asset), figures_root=figures_root)
        records.append(
            VisualRecord(
                kind="registered_mermaid",
                source_path="src/mermaid/biology_diagrams.py",
                line=line,
                label=f"mermaid:{diagram.name}",
                caption=diagram.title,
                alt=f"Registered Mermaid diagram showing {diagram.title}.",
                asset_path=relative(asset),
                generator=name,
                width_px=width,
                height_px=height,
                aspect_policy="mermaid-square",
            )
        )
    return sorted(records, key=lambda r: r.label)


def inline_stem(index: int, source: str) -> str:
    digest = hashlib.sha256(source.strip().encode("utf-8")).hexdigest()[:12]
    return f"inline_mermaid_{index:04d}_{digest}"


def normalise_inline_mermaid_source(source: str) -> str:
    try:
        module = import_module("infrastructure.rendering._pdf_mermaid")
        normalize = getattr(module, "_normalise_mermaid_source")
    except (AttributeError, ImportError):
        return source.replace(r"\n", "<br/>")
    return str(normalize(source))


def inline_mermaid_sources() -> Iterable[tuple[int, Path, int, str]]:
    index = 0
    for path in sorted(MANUSCRIPT_DIR.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _MERMAID_RE.finditer(text):
            index += 1
            source = normalise_inline_mermaid_source(match.group("source").strip())
            yield index, path, line_for_offset(text, match.start()), source


def inline_mermaid_records(figures_root: Path = OUTPUT_FIGURES) -> list[VisualRecord]:
    """Extract inline Mermaid records from manuscript Markdown."""
    records: list[VisualRecord] = []
    index = 0
    for path in sorted(MANUSCRIPT_DIR.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _MERMAID_RE.finditer(text):
            index += 1
            source = normalise_inline_mermaid_source(match.group("source").strip())
            stem = inline_stem(index, source)
            asset = figures_root / "mermaid_inline" / f"{stem}.png"
            width, height = dimensions(relative(asset), figures_root=figures_root)
            records.append(
                VisualRecord(
                    kind="inline_mermaid",
                    source_path=relative(path),
                    line=line_for_offset(text, match.start()),
                    label=f"mermaid-inline:{stem}",
                    caption=first_caption_after_mermaid(text, match.end()),
                    alt=first_alt_after(text, match.end()),
                    asset_path=relative(asset),
                    generator="inline_mermaid_fence",
                    width_px=width,
                    height_px=height,
                    aspect_policy="mermaid-square",
                )
            )
    return records


__all__ = [
    "inline_mermaid_records",
    "inline_mermaid_sources",
    "inline_stem",
    "normalise_inline_mermaid_source",
    "raw_figure_records",
    "registered_mermaid_factories",
    "registered_mermaid_records",
]
