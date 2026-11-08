"""Collect ordered manuscript paths from config and canonical ToC."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, cast

import yaml

from biology.maintenance.manuscript_walker import require_manuscript_source
from biology.pipeline.paths import CONFIG_FILE, MANUSCRIPT_DIR, PROJECT_ROOT

logger = logging.getLogger(__name__)


def load_config() -> dict[str, Any]:
    """Load the canonical docs/manuscript/config.yaml snapshot."""
    require_manuscript_source(CONFIG_FILE, MANUSCRIPT_DIR, project_root=PROJECT_ROOT)
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_FILE}")
    with CONFIG_FILE.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if not isinstance(config, dict):
        raise TypeError(f"Manuscript configuration must be a mapping: {CONFIG_FILE}")
    return cast(dict[str, Any], config)


def collect_ordered_chapters(config: dict[str, Any]) -> list[Path]:
    """Select one configuration snapshot; refuse missing or escaping inputs."""
    from biology.toc import load_toc

    book_toc = load_toc(PROJECT_ROOT, config=config)
    chapters: list[Path] = []
    selected: set[Path] = set()

    def append(path: Path) -> None:
        require_manuscript_source(path, MANUSCRIPT_DIR, project_root=PROJECT_ROOT)
        resolved = path.resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Selected manuscript source is missing: {path}")
        if resolved in selected:
            raise ValueError(f"Manuscript source selected more than once: {path}")
        selected.add(resolved)
        chapters.append(path)

    front_matter = config.get("front_matter", {}) or {}
    if front_matter.get("include_front_matter", False):
        for entry in front_matter.get("files", []):
            file_name = str(entry["file"]) if isinstance(entry, dict) else str(entry)
            if Path(file_name).name == "preface.md" and not front_matter.get("include_preface", True):
                continue
            append(MANUSCRIPT_DIR / file_name)

    for unit in book_toc.units:
        # Unit introductions are optional orientation files, unlike configured chapters.
        require_manuscript_source(unit.intro_path, MANUSCRIPT_DIR, project_root=PROJECT_ROOT)
        if unit.intro_path.is_file():
            append(unit.intro_path)
        for chapter in unit.chapters:
            append(chapter.path)

    appendices = config.get("appendices", {}) or {}
    for enabled_key, items in (
        ("include_labs", book_toc.labs),
        ("include_questions", book_toc.questions),
        ("include_reference", book_toc.references),
    ):
        if appendices.get(enabled_key, False):
            for item in items:
                append(item.path)

    if not chapters:
        raise ValueError("Manuscript selection is empty")
    logger.info("Selected %d manuscript sources from one configuration snapshot", len(chapters))
    return chapters


__all__ = ["collect_ordered_chapters", "load_config"]
