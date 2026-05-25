"""Generate and check the biology textbook visual contract manifest.

The manifest is generated into ``output/figures/visual_manifest.json`` from
authoritative source locations: manuscript figure blocks, registered Mermaid
factories, and inline Mermaid fences. Generated images under ``output/`` remain
disposable; this script re-derives their metadata whenever it runs.
"""

from __future__ import annotations

import hashlib
from importlib import import_module
import inspect
import json
import re
import shutil
import sys
from collections.abc import Callable, Iterable
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from PIL import Image

from biology.visual_contracts_paths import (
    DEFAULT_MANIFEST,
    MANUSCRIPT_DIR,
    OUTPUT_FIGURES,
    PROJECT_ROOT,
    SRC_DIR,
    TEMPLATE_ROOT,
)
from textbook_io import write_text_atomic

_LATEX_FIGURE_RE = re.compile(r"\\begin\{figure\}.*?\\end\{figure\}", re.DOTALL)
_INCLUDE_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{(?P<path>[^}]+)\}")
_CAPTION_RE = re.compile(r"\\caption\{(?P<caption>.*?)\}\s*\\label", re.DOTALL)
_LABEL_RE = re.compile(r"\\label\{(?P<label>fig:[^}]+)\}")
_ALT_RE = re.compile(r"<!--\s*alt:\s*(?P<alt>.*?)\s*-->", re.DOTALL | re.IGNORECASE)
_MERMAID_RE = re.compile(
    r"^```mermaid\s*\n(?P<source>.*?)^```\s*$",
    re.DOTALL | re.MULTILINE | re.IGNORECASE,
)
_ITALIC_CAPTION_RE = re.compile(r"^\s*\*(?!\*)(?P<caption>[^*\n].{6,}[^*\s])\*\s*$")
_STYLE_COLOR_RE = re.compile(
    r"(?:^|\s)(?:style|classDef)\s+[^;\n]*(?P<props>fill:#[0-9A-Fa-f]{6}[^;\n]*|stroke:#[0-9A-Fa-f]{6}[^;\n]*)"
)
_HEX_RE = re.compile(r"(?P<key>fill|stroke):(?P<hex>#[0-9A-Fa-f]{6})")

_STOPWORDS = {
    "and",
    "the",
    "with",
    "from",
    "into",
    "versus",
    "against",
    "showing",
    "shows",
    "figure",
    "plot",
    "panel",
    "line",
    "chart",
    "axis",
    "axes",
    "indexed",
    "illustrative",
}


@dataclass(frozen=True)
class VisualRecord:
    """One raw, registered Mermaid, or inline Mermaid visual contract entry."""

    kind: str
    source_path: str
    line: int
    label: str
    caption: str
    alt: str
    asset_path: str
    generator: str
    width_px: int
    height_px: int
    aspect_policy: str = ""
    aspect_exception: str = ""


@dataclass(frozen=True)
class Finding:
    """A visual-contract audit finding."""

    code: str
    source_path: str
    line: int
    detail: str


def _ensure_import_paths() -> None:
    for path in (SRC_DIR, TEMPLATE_ROOT):
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)


def _relative(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _normalise_space(text: str) -> str:
    return " ".join(text.replace("\n", " ").split())


def _tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[A-Za-z][A-Za-z0-9+-]{2,}", text.lower())
        if token not in _STOPWORDS
    }


def _first_alt_after(text: str, offset: int) -> str:
    window = text[offset : offset + 800]
    for line in window.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = _ALT_RE.fullmatch(stripped)
        if match:
            return _normalise_space(match.group("alt"))
        break
    return ""


def _first_caption_after_mermaid(text: str, offset: int) -> str:
    window = text[offset : offset + 800]
    for line in window.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if _ALT_RE.fullmatch(stripped):
            continue
        match = _ITALIC_CAPTION_RE.fullmatch(stripped)
        if match:
            return _normalise_space(match.group("caption"))
        break
    return ""


def _resolve_asset(asset_path: str, figures_root: Path = OUTPUT_FIGURES) -> Path:
    if asset_path.startswith("../figures/"):
        return (figures_root / asset_path.removeprefix("../figures/")).resolve()
    return PROJECT_ROOT / asset_path


def _dimensions(
    asset_path: str,
    *,
    figures_root: Path = OUTPUT_FIGURES,
    fallback: tuple[int, int] = (0, 0),
) -> tuple[int, int]:
    resolved = _resolve_asset(asset_path, figures_root)
    if not resolved.exists():
        return fallback
    try:
        with Image.open(resolved) as image:
            return int(image.width), int(image.height)
    except OSError:
        return fallback


def _raw_generator_for_asset(asset_path: str) -> str:
    stem = Path(asset_path).stem
    if stem.startswith("punnett_"):
        return "plot_punnett_square"
    known = {
        "oxygen_dissociation_curve": "plot_oxygen_dissociation",
        "light_response_curves": "plot_light_response_curve",
    }
    if stem in known:
        return known[stem]
    return f"plot_{stem}"


def _aspect_policy_for_stem(stem: str) -> str:
    _ensure_import_paths()
    from visualization.plots import FIGURE_ASPECT

    if FIGURE_ASPECT.get(stem) == "landscape":
        return "figure-landscape"
    return "figure-square"


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
            width, height = _dimensions(asset_path, figures_root=figures_root)
            stem = Path(asset_path).stem if asset_path else ""
            records.append(
                VisualRecord(
                    kind="raw_figure",
                    source_path=_relative(path),
                    line=_line_for_offset(text, match.start()),
                    label=label.group("label") if label else "",
                    caption=_normalise_space(caption.group("caption")) if caption else "",
                    alt=_first_alt_after(text, match.end()),
                    asset_path=asset_path,
                    generator=_raw_generator_for_asset(asset_path) if asset_path else "",
                    width_px=width,
                    height_px=height,
                    aspect_policy=_aspect_policy_for_stem(stem),
                )
            )
    return records


def _registered_mermaid_factories() -> Iterable[tuple[str, Callable[[], Any], int]]:
    _ensure_import_paths()
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
    _ensure_import_paths()
    records: list[VisualRecord] = []
    for name, factory, line in _registered_mermaid_factories():
        diagram = factory()
        png = figures_root / "mermaid" / f"{diagram.name}.png"
        asset = png if png.exists() else figures_root / "mermaid" / f"{diagram.name}.mmd"
        width, height = _dimensions(_relative(asset), figures_root=figures_root)
        records.append(
            VisualRecord(
                kind="registered_mermaid",
                source_path="src/mermaid/biology_diagrams.py",
                line=line,
                label=f"mermaid:{diagram.name}",
                caption=diagram.title,
                alt=f"Registered Mermaid diagram showing {diagram.title}.",
                asset_path=_relative(asset),
                generator=name,
                width_px=width,
                height_px=height,
                aspect_policy="mermaid-square",
            )
        )
    return sorted(records, key=lambda r: r.label)


def _inline_stem(index: int, source: str) -> str:
    digest = hashlib.sha256(source.strip().encode("utf-8")).hexdigest()[:12]
    return f"inline_mermaid_{index:04d}_{digest}"


def _normalise_inline_mermaid_source(source: str) -> str:
    try:
        module = import_module("infrastructure.rendering._pdf_mermaid")
        normalise = getattr(module, "_normalise_mermaid_source")
    except (AttributeError, ImportError):
        return source.replace(r"\n", "<br/>")
    return str(normalise(source))


def _inline_mermaid_sources() -> Iterable[tuple[int, Path, int, str]]:
    index = 0
    for path in sorted(MANUSCRIPT_DIR.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _MERMAID_RE.finditer(text):
            index += 1
            source = _normalise_inline_mermaid_source(match.group("source").strip())
            yield index, path, _line_for_offset(text, match.start()), source


def render_inline_mermaid_assets(figures_root: Path = OUTPUT_FIGURES) -> list[Path]:
    """Render every inline Mermaid fence to ``figures_root/mermaid_inline``."""
    if shutil.which("mmdc") is None:
        raise RuntimeError("Mermaid CLI 'mmdc' is required to render inline Mermaid assets")
    _ensure_import_paths()
    from mermaid import MermaidRenderer

    renderer = MermaidRenderer(output_dir=figures_root / "mermaid_inline", strict_png=True)
    paths: list[Path] = []
    for index, _path, _line, source in _inline_mermaid_sources():
        paths.append(renderer.render(_inline_stem(index, source), source, width=1200, height=1200))
    return paths


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
            source = _normalise_inline_mermaid_source(match.group("source").strip())
            stem = _inline_stem(index, source)
            asset = figures_root / "mermaid_inline" / f"{stem}.png"
            width, height = _dimensions(_relative(asset), figures_root=figures_root)
            records.append(
                VisualRecord(
                    kind="inline_mermaid",
                    source_path=_relative(path),
                    line=_line_for_offset(text, match.start()),
                    label=f"mermaid-inline:{stem}",
                    caption=_first_caption_after_mermaid(text, match.end()),
                    alt=_first_alt_after(text, match.end()),
                    asset_path=_relative(asset),
                    generator="inline_mermaid_fence",
                    width_px=width,
                    height_px=height,
                    aspect_policy="mermaid-square",
                )
            )
    return records


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


def _aspect_ratio(record: VisualRecord) -> float:
    if not record.width_px or not record.height_px:
        return 0.0
    return record.width_px / record.height_px


def _review_action(record: VisualRecord) -> str:
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
        ratio = _aspect_ratio(record)
        size = f"{record.width_px}x{record.height_px}" if ratio else ""
        ratio_text = f"{ratio:.2f}" if ratio else ""
        action = _review_action(record) if ratio else "asset missing"
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


def _contrast_ratio(hex_a: str, hex_b: str) -> float:
    def luminance(hex_color: str) -> float:
        rgb = [int(hex_color[i : i + 2], 16) / 255.0 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

    l1, l2 = sorted((luminance(hex_a), luminance(hex_b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def _mermaid_sources() -> Iterable[tuple[str, int, str]]:
    _ensure_import_paths()
    for _name, factory, line in _registered_mermaid_factories():
        diagram = factory()
        yield "src/mermaid/biology_diagrams.py", line, diagram.source
    for path in sorted(MANUSCRIPT_DIR.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _MERMAID_RE.finditer(text):
            yield _relative(path), _line_for_offset(text, match.start()), match.group("source").strip()


def check_records(records: list[VisualRecord]) -> list[Finding]:
    """Return visual-contract findings."""
    findings: list[Finding] = []
    seen_labels: dict[str, VisualRecord] = {}

    for record in records:
        if record.label:
            previous = seen_labels.get(record.label)
            if previous is not None:
                findings.append(
                    Finding(
                        "duplicate-label",
                        record.source_path,
                        record.line,
                        f"also used at {previous.source_path}:{previous.line}",
                    )
                )
            seen_labels[record.label] = record

        if record.kind == "raw_figure":
            if (
                record.source_path.startswith("manuscript/unit_")
                and not record.label.startswith("fig:unit_")
            ):
                findings.append(
                    Finding(
                        "unit-prefixed-label",
                        record.source_path,
                        record.line,
                        f"label must start with fig:unit_: {record.label}",
                    )
                )
            if not record.caption:
                findings.append(Finding("missing-caption", record.source_path, record.line, record.asset_path))
            if not record.alt:
                findings.append(Finding("missing-alt", record.source_path, record.line, record.asset_path))
            caption_tokens = _tokens(record.caption)
            alt_tokens = _tokens(record.alt)
            if record.caption and record.alt and len(caption_tokens & alt_tokens) < 2:
                findings.append(
                    Finding(
                        "caption-alt-drift",
                        record.source_path,
                        record.line,
                        f"{record.label} caption/alt share too little domain vocabulary",
                    )
                )

        if record.width_px and record.height_px and not record.aspect_exception:
            ratio = _aspect_ratio(record)
            policy = record.aspect_policy
            if not policy and record.kind == "raw_figure":
                policy = "figure-square"
            if not policy and record.kind in {"registered_mermaid", "inline_mermaid"}:
                policy = "mermaid-square"
            if policy == "figure-square" and not 0.85 <= ratio <= 1.18:
                findings.append(
                    Finding(
                        "figure-square-aspect",
                        record.source_path,
                        record.line,
                        f"{record.asset_path} ratio {ratio:.2f} outside 0.85-1.18",
                    )
                )
            if policy == "figure-landscape" and not 1.05 <= ratio <= 3.5:
                findings.append(
                    Finding(
                        "figure-landscape-aspect",
                        record.source_path,
                        record.line,
                        f"{record.asset_path} ratio {ratio:.2f} outside 1.05-3.5",
                    )
                )
            if policy == "mermaid-square" and not 0.75 <= ratio <= 1.33:
                findings.append(
                    Finding(
                        "mermaid-square-aspect",
                        record.source_path,
                        record.line,
                        f"{record.asset_path} ratio {ratio:.2f} outside 0.75-1.33",
                    )
                )

    for source_path, line, source in _mermaid_sources():
        if source_path == "src/mermaid/biology_diagrams.py" and "\\n" in source:
            findings.append(
                Finding(
                    "mermaid-newline-escape",
                    source_path,
                    line,
                    "use <br/> rather than literal escaped newlines",
                )
            )
        for line_offset, mermaid_line in enumerate(source.splitlines(), start=0):
            color_match = _STYLE_COLOR_RE.search(mermaid_line)
            if not color_match:
                continue
            props = {
                m.group("key"): m.group("hex")
                for m in _HEX_RE.finditer(color_match.group("props"))
            }
            if (
                "fill" in props
                and "stroke" in props
                and _contrast_ratio(props["fill"], props["stroke"]) < 3.0
            ):
                findings.append(
                    Finding(
                        "mermaid-low-contrast",
                        source_path,
                        line + line_offset,
                        f"{props['fill']} vs {props['stroke']}",
                    )
                )

    return findings
