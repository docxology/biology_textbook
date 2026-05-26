"""Path, dimension, and text helpers for visual contracts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from PIL import Image

from biology.visual_contracts.models import (
    _ALT_RE,
    _ITALIC_CAPTION_RE,
    _STOPWORDS,
)
from biology.visual_contracts_paths import (
    OUTPUT_FIGURES,
    PROJECT_ROOT,
    SRC_DIR,
    TEMPLATE_ROOT,
)


def ensure_import_paths() -> None:
    for path in (SRC_DIR, TEMPLATE_ROOT):
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)


def relative(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def normalise_space(text: str) -> str:
    return " ".join(text.replace("\n", " ").split())


def tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[A-Za-z][A-Za-z0-9+-]{2,}", text.lower())
        if token not in _STOPWORDS
    }


def first_alt_after(text: str, offset: int) -> str:
    window = text[offset : offset + 800]
    for line in window.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = _ALT_RE.fullmatch(stripped)
        if match:
            return normalise_space(match.group("alt"))
        break
    return ""


def first_caption_after_mermaid(text: str, offset: int) -> str:
    window = text[offset : offset + 800]
    for line in window.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if _ALT_RE.fullmatch(stripped):
            continue
        match = _ITALIC_CAPTION_RE.fullmatch(stripped)
        if match:
            return normalise_space(match.group("caption"))
        break
    return ""


def resolve_asset(asset_path: str, figures_root: Path = OUTPUT_FIGURES) -> Path:
    if asset_path.startswith("../figures/"):
        return (figures_root / asset_path.removeprefix("../figures/")).resolve()
    return PROJECT_ROOT / asset_path


def dimensions(
    asset_path: str,
    *,
    figures_root: Path = OUTPUT_FIGURES,
    fallback: tuple[int, int] = (0, 0),
) -> tuple[int, int]:
    resolved = resolve_asset(asset_path, figures_root)
    if not resolved.exists():
        return fallback
    try:
        with Image.open(resolved) as image:
            return int(image.width), int(image.height)
    except OSError:
        return fallback


def raw_generator_for_asset(asset_path: str) -> str:
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


def aspect_policy_for_stem(stem: str) -> str:
    ensure_import_paths()
    from visualization.plots import FIGURE_ASPECT

    if FIGURE_ASPECT.get(stem) == "landscape":
        return "figure-landscape"
    return "figure-square"


__all__ = [
    "aspect_policy_for_stem",
    "dimensions",
    "ensure_import_paths",
    "first_alt_after",
    "first_caption_after_mermaid",
    "line_for_offset",
    "normalise_space",
    "raw_generator_for_asset",
    "relative",
    "resolve_asset",
    "tokens",
]
