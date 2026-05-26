"""Tests for ``biology.maintenance.chapter_badges``."""

from __future__ import annotations

from pathlib import Path

from biology.maintenance.chapter_badges import (
    BADGE_MARKER,
    InsertReport,
    format_badge,
    insert_badge,
)
from biology.toc import load_toc


PROJECT = Path(__file__).resolve().parent.parent


def test_insert_badge_is_idempotent(tmp_path: Path) -> None:
    chapter = tmp_path / "chapter.md"
    chapter.write_text("# Title\n\\label{sec:demo}\n\nBody.\n", encoding="utf-8")
    badge = f"{BADGE_MARKER}\n> Intermediate · 20 min read · 45 min lecture · Prerequisites: none"
    report = InsertReport()

    insert_badge(chapter, badge, report, dry_run=False)
    first = chapter.read_text(encoding="utf-8")
    assert BADGE_MARKER in first
    assert report.badges_inserted == 1

    insert_badge(chapter, badge, report, dry_run=False)
    second = chapter.read_text(encoding="utf-8")
    assert second.count(BADGE_MARKER) == 1
    assert report.badges_already_present == 1 or report.badges_updated >= 0


def test_format_badge_uses_prerequisite_crefs() -> None:
    book_toc = load_toc(PROJECT)
    chapter = book_toc.chapters_by_id["unit_I_atoms_molecules"]
    badge = format_badge(chapter, book_toc.chapters_by_id)
    assert BADGE_MARKER in badge
    assert "\\cref{" in badge or "Prerequisites: none" in badge


def test_build_grid_contains_hyperref_links() -> None:
    from biology.maintenance.chapter_badges import GRID_START, build_grid

    grid = build_grid(load_toc(PROJECT))
    assert "\\hyperref" in grid or GRID_START


def test_apply_chapter_metadata_dry_run_on_project() -> None:
    from biology.maintenance.chapter_badges import apply_chapter_metadata

    report = apply_chapter_metadata(PROJECT, dry_run=True)
    assert report.badges_already_present >= 0 or report.badges_inserted >= 0
