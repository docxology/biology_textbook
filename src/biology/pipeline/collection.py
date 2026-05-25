"""Collect ordered manuscript paths from config and canonical ToC."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, cast

import yaml

from biology.pipeline.paths import CONFIG_FILE, MANUSCRIPT_DIR, PROJECT_ROOT

logger = logging.getLogger(__name__)


def load_config() -> dict[str, Any]:
    """Load and parse manuscript/config.yaml."""
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_FILE}")
    with CONFIG_FILE.open(encoding="utf-8") as handle:
        return cast(dict[str, Any], yaml.safe_load(handle) or {})


def collect_ordered_chapters(config: dict[str, Any]) -> list[Path]:
    """Return all chapter Path objects in rendering order."""
    from biology.toc import load_toc

    book_toc = load_toc(PROJECT_ROOT)
    chapters: list[Path] = []

    front_matter_cfg = config.get("front_matter", {})
    if front_matter_cfg.get("include_front_matter", False):
        for fm_entry in front_matter_cfg.get("files", []):
            fm_file = fm_entry.get("file", "") if isinstance(fm_entry, dict) else str(fm_entry)
            fm_path = MANUSCRIPT_DIR / fm_file
            if fm_path.exists():
                chapters.append(fm_path)
                logger.info("  Front matter: %s", fm_file)
            else:
                logger.warning("  Front matter file not found: %s", fm_path)

    for unit in book_toc.units:
        logger.info("  Unit %s: %s", unit.label, unit.title)
        if unit.intro_path.exists():
            chapters.append(unit.intro_path)
            logger.info("    + unit intro: %s", unit.intro_path.name)
        for chapter in unit.chapters:
            if chapter.path.exists():
                chapters.append(chapter.path)
                logger.info("    + %s: %s", chapter.file, chapter.title)
            else:
                logger.warning("    MISSING: %s", chapter.path)

    appendices = config.get("appendices", {}) or {}
    if appendices.get("include_labs", False):
        logger.info("  Appendix: Laboratory Activities")
        for lab in book_toc.labs:
            if lab.path.exists():
                chapters.append(lab.path)
                logger.info("    + lab %s/%s", lab.unit_id, lab.file)
            else:
                logger.warning("    MISSING lab: %s", lab.path)
    if appendices.get("include_questions", False):
        logger.info("  Appendix: Question Banks")
        for question in book_toc.questions:
            if question.path.exists():
                chapters.append(question.path)
                logger.info("    + question bank %s/%s", question.unit_id, question.file)
            else:
                logger.warning("    MISSING question bank: %s", question.path)

    if appendices.get("include_reference", False):
        logger.info("  Appendix: Reference Material")
        for reference in book_toc.references:
            if reference.path.exists():
                chapters.append(reference.path)
                logger.info("    + reference appendix %s", reference.file)
            else:
                logger.warning("    MISSING reference appendix: %s", reference.path)

    return chapters


__all__ = ["collect_ordered_chapters", "load_config"]
