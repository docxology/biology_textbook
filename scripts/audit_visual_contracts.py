"""Generate and check the biology textbook visual contract manifest.

The manifest is generated into ``output/figures/visual_manifest.json`` from
authoritative source locations: manuscript figure blocks, registered Mermaid
factories, and inline Mermaid fences. Generated images under ``output/`` remain
disposable; this script re-derives their metadata whenever it runs.
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import re
import sys
from collections.abc import Callable, Iterable
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from PIL import Image

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = PROJECT_ROOT.parent.parent
SRC_DIR = PROJECT_ROOT / "src"
MANUSCRIPT_DIR = PROJECT_ROOT / "manuscript"
OUTPUT_FIGURES = PROJECT_ROOT / "output" / "figures"
DEFAULT_MANIFEST = OUTPUT_FIGURES / "visual_manifest.json"

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


def _resolve_asset(asset_path: str) -> Path:
    if asset_path.startswith("../figures/"):
        return (PROJECT_ROOT / "output" / "manuscript" / asset_path).resolve()
    return PROJECT_ROOT / asset_path


def _dimensions(asset_path: str, fallback: tuple[int, int] = (0, 0)) -> tuple[int, int]:
    resolved = _resolve_asset(asset_path)
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


def raw_figure_records() -> list[VisualRecord]:
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
            width, height = _dimensions(asset_path)
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


def registered_mermaid_records() -> list[VisualRecord]:
    """Build records for Mermaid diagrams registered in Python factories."""
    _ensure_import_paths()
    records: list[VisualRecord] = []
    for name, factory, line in _registered_mermaid_factories():
        diagram = factory()
        png = OUTPUT_FIGURES / "mermaid" / f"{diagram.name}.png"
        asset = png if png.exists() else OUTPUT_FIGURES / "mermaid" / f"{diagram.name}.mmd"
        width, height = _dimensions(_relative(asset), fallback=(1200, 800))
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
            )
        )
    return sorted(records, key=lambda r: r.label)


def _inline_stem(index: int, source: str) -> str:
    digest = hashlib.sha256(source.strip().encode("utf-8")).hexdigest()[:12]
    return f"inline_mermaid_{index:04d}_{digest}"


def inline_mermaid_records() -> list[VisualRecord]:
    """Extract inline Mermaid records from manuscript Markdown."""
    records: list[VisualRecord] = []
    index = 0
    for path in sorted(MANUSCRIPT_DIR.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _MERMAID_RE.finditer(text):
            index += 1
            source = match.group("source").strip()
            stem = _inline_stem(index, source)
            asset = OUTPUT_FIGURES / "mermaid_inline" / f"{stem}.png"
            width, height = _dimensions(_relative(asset), fallback=(1200, 800))
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
                )
            )
    return records


def build_manifest() -> list[VisualRecord]:
    """Return all visual records in a stable order."""
    records = raw_figure_records()
    records.extend(registered_mermaid_records())
    records.extend(inline_mermaid_records())
    return sorted(records, key=lambda r: (r.kind, r.source_path, r.line, r.label))


def write_manifest(records: list[VisualRecord], path: Path = DEFAULT_MANIFEST) -> Path:
    """Write manifest JSON atomically."""
    payload = [asdict(record) for record in records]
    write_text_atomic(path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
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

        if record.kind == "raw_figure" and record.width_px and record.height_px:
            ratio = record.width_px / record.height_px
            if not 0.75 <= ratio <= 3.0:
                findings.append(
                    Finding(
                        "print-aspect-ratio",
                        record.source_path,
                        record.line,
                        f"{record.asset_path} ratio {ratio:.2f} outside 0.75-3.0",
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate and check the biology visual manifest")
    parser.add_argument("--output", type=Path, default=DEFAULT_MANIFEST, help="Manifest JSON output path")
    parser.add_argument("--check", action="store_true", help="Fail if visual contract findings are present")
    args = parser.parse_args()

    records = build_manifest()
    manifest_path = write_manifest(records, args.output)
    findings = check_records(records)

    print(f"[audit_visual_contracts] manifest: {manifest_path}")
    print(f"[audit_visual_contracts] records: {len(records)}")
    if findings:
        for finding in findings:
            print(f"{finding.code}: {finding.source_path}:{finding.line}: {finding.detail}")
    else:
        print("[audit_visual_contracts] visual contracts clean")
    return 1 if args.check and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
