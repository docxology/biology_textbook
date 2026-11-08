"""Tests for ``biology.maintenance.chapter_badges``."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import pytest

from biology.maintenance.chapter_badges import (
    BADGE_MARKER,
    InsertReport,
    apply_chapter_metadata,
    insert_badge,
)
from biology.toc import load_toc


def test_insert_badge_is_idempotent(tmp_path: Path) -> None:
    chapter = tmp_path / "chapter.md"
    chapter.write_text("# Title\n\\label{sec:demo}\n\nBody.\n", encoding="utf-8")
    badge = f"{BADGE_MARKER}\n> Intermediate · 20 min read · 45 min lecture · Prerequisites: none"
    report = InsertReport()

    insert_badge(chapter, badge, report, dry_run=False)
    first = chapter.read_text(encoding="utf-8")
    assert BADGE_MARKER in first
    assert report.badges_inserted == 1
    first_stat = chapter.stat()

    insert_badge(chapter, badge, report, dry_run=False)
    second = chapter.read_text(encoding="utf-8")
    assert second.count(BADGE_MARKER) == 1
    assert second == first
    assert chapter.stat().st_ino == first_stat.st_ino
    assert chapter.stat().st_mtime_ns == first_stat.st_mtime_ns
    assert report.badges_already_present == 1
    assert report.badges_updated == 0


@pytest.mark.parametrize("authored_suffix", ["", "\n\n\\newpage\n\n# Authored notes\n\nPreserve these notes.\n"])
def test_metadata_preview_and_apply_preserve_unrelated_authored_sources(tmp_path: Path, authored_suffix: str) -> None:
    manuscript = tmp_path / "docs" / "manuscript"
    shutil.copytree(Path(__file__).resolve().parents[1] / "docs" / "manuscript", manuscript)
    chapter = load_toc(tmp_path).chapters[0].path
    chapter.write_text(re.sub(
        re.escape(BADGE_MARKER) + r"\n> [^\n]*\n?", "", chapter.read_text(encoding="utf-8"), count=1,
    ), encoding="utf-8")
    front = manuscript / "front_matter.md"
    authored = "# Front matter\n\nAn independently authored introduction must survive regeneration.\n"
    front.write_text(authored + authored_suffix, encoding="utf-8")

    def snapshot() -> dict[Path, tuple[bytes, int, int]]:
        return {path: (path.read_bytes(), path.stat().st_mtime_ns, path.stat().st_ino)
                for path in manuscript.rglob("*.md")}

    before = snapshot()
    preview = apply_chapter_metadata(tmp_path, dry_run=True)
    assert preview.badges_inserted == 1 and preview.grid_updated
    assert snapshot() == before
    applied = apply_chapter_metadata(tmp_path)
    assert applied.badges_inserted == 1 and applied.grid_updated
    assert front.read_text(encoding="utf-8").startswith(authored)
    if authored_suffix:
        assert front.read_text(encoding="utf-8").endswith(authored_suffix)
    assert front.read_text(encoding="utf-8").count("\\newpage") == 1
    after = snapshot()
    assert {path for path in before if before[path] != after[path]} == {chapter, front}
    repeated = apply_chapter_metadata(tmp_path)
    assert repeated.badges_inserted == repeated.badges_updated == 0
    assert not repeated.grid_updated
    assert snapshot() == after
