"""Typed loader for enrichment catalog data stored in catalog.yaml."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_CATALOG_PATH = Path(__file__).with_name("catalog.yaml")


def _compile_pattern(name: str, pattern: str, flags: int) -> re.Pattern[str]:
    return re.compile(pattern, flags=flags)


@lru_cache(maxsize=1)
def _load_raw() -> dict[str, Any]:
    raw = yaml.safe_load(_CATALOG_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{_CATALOG_PATH} must contain a mapping at the top level")
    return raw


def _tuple_map(raw: dict[str, list[str]]) -> dict[str, tuple[str, ...]]:
    return {key: tuple(value) for key, value in raw.items()}


def _figure_map(raw: dict[str, list[str]]) -> dict[str, tuple[str, str, str, str]]:
    return {key: tuple(value) for key, value in raw.items()}  # type: ignore[return-value]


@lru_cache(maxsize=1)
def frontier_by_unit() -> dict[str, tuple[str, str]]:
    return _tuple_map(_load_raw()["FRONTIER_BY_UNIT"])  # type: ignore[arg-type]


@lru_cache(maxsize=1)
def source_practice_by_unit() -> dict[str, str]:
    return dict(_load_raw()["SOURCE_PRACTICE_BY_UNIT"])  # type: ignore[arg-type]


@lru_cache(maxsize=1)
def extra_frontier_by_stem() -> dict[str, str]:
    return dict(_load_raw()["EXTRA_FRONTIER_BY_STEM"])  # type: ignore[arg-type]


@lru_cache(maxsize=1)
def focus_by_stem() -> dict[str, str]:
    return dict(_load_raw()["FOCUS_BY_STEM"])  # type: ignore[arg-type]


@lru_cache(maxsize=1)
def figure_by_stem() -> dict[str, tuple[str, str, str, str]]:
    return _figure_map(_load_raw()["FIGURE_BY_STEM"])  # type: ignore[arg-type]


@lru_cache(maxsize=1)
def companion_intro_by_stem() -> dict[str, str]:
    return dict(_load_raw()["COMPANION_INTRO_BY_STEM"])  # type: ignore[arg-type]


@lru_cache(maxsize=1)
def companion_source_by_stem() -> dict[str, str]:
    return dict(_load_raw()["COMPANION_SOURCE_BY_STEM"])  # type: ignore[arg-type]


@lru_cache(maxsize=1)
def companion_section_pattern() -> re.Pattern[str]:
    patterns = _load_raw()["companion_patterns"]
    return _compile_pattern("section", patterns["section"], int(patterns["section_flags"]))


@lru_cache(maxsize=1)
def companion_note_line_pattern() -> re.Pattern[str]:
    patterns = _load_raw()["companion_patterns"]
    return _compile_pattern("note_line", patterns["note_line"], int(patterns["note_line_flags"]))


@lru_cache(maxsize=1)
def companion_inline_note_pattern() -> re.Pattern[str]:
    patterns = _load_raw()["companion_patterns"]
    return _compile_pattern("inline_note", patterns["inline_note"], int(patterns["inline_note_flags"]))


def __getattr__(name: str) -> Any:
    if name == "FRONTIER_BY_UNIT":
        return frontier_by_unit()
    if name == "SOURCE_PRACTICE_BY_UNIT":
        return source_practice_by_unit()
    if name == "EXTRA_FRONTIER_BY_STEM":
        return extra_frontier_by_stem()
    if name == "FOCUS_BY_STEM":
        return focus_by_stem()
    if name == "FIGURE_BY_STEM":
        return figure_by_stem()
    if name == "COMPANION_INTRO_BY_STEM":
        return companion_intro_by_stem()
    if name == "COMPANION_SOURCE_BY_STEM":
        return companion_source_by_stem()
    if name == "_COMPANION_SECTION_RE":
        return companion_section_pattern()
    if name == "_COMPANION_NOTE_LINE_RE":
        return companion_note_line_pattern()
    if name == "_INLINE_COMPANION_NOTE_RE":
        return companion_inline_note_pattern()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "COMPANION_INTRO_BY_STEM",
    "COMPANION_SOURCE_BY_STEM",
    "EXTRA_FRONTIER_BY_STEM",
    "FIGURE_BY_STEM",
    "FOCUS_BY_STEM",
    "FRONTIER_BY_UNIT",
    "SOURCE_PRACTICE_BY_UNIT",
    "_COMPANION_NOTE_LINE_RE",
    "_COMPANION_SECTION_RE",
    "_INLINE_COMPANION_NOTE_RE",
    "companion_inline_note_pattern",
    "companion_intro_by_stem",
    "companion_note_line_pattern",
    "companion_section_pattern",
    "companion_source_by_stem",
    "extra_frontier_by_stem",
    "figure_by_stem",
    "focus_by_stem",
    "frontier_by_unit",
    "source_practice_by_unit",
]
