"""Invariant tests for ``src/biology/chapter_metadata.py``.

Ensures the metadata table is complete and internally consistent:

* Every chapter in ``manuscript/config.yaml`` has a matching record.
* Prerequisite IDs always refer to a defined chapter.
* Difficulty is in {1, 2, 3}.
* Reading and lecture times are positive; lecture ≥ reading (usually).
* Star badge has exactly three characters.
* Chapter numbers are contiguous 1..N for Units I–X.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml


PROJECT = Path(__file__).resolve().parent.parent
MODULE_PATH = PROJECT / "src" / "biology" / "chapter_metadata.py"


def _load():
    spec = importlib.util.spec_from_file_location("chapter_metadata", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load chapter metadata from {MODULE_PATH}")
    m = importlib.util.module_from_spec(spec)
    sys.modules["chapter_metadata"] = m
    spec.loader.exec_module(m)
    return m


@pytest.fixture(scope="module")
def mod():
    return _load()


def test_every_config_chapter_has_metadata(mod) -> None:
    cfg = yaml.safe_load((PROJECT / "manuscript" / "config.yaml").read_text())
    expected: set[str] = set()
    for u in cfg["units"]:
        for ch in u.get("chapters", []):
            stem = ch["file"].replace(".md", "")
            expected.add(f"{u['id']}_{stem}")
    actual = {c.chapter_id for c in mod.CHAPTERS}
    missing = expected - actual
    assert not missing, f"No metadata for chapters: {sorted(missing)}"


def test_prerequisites_refer_to_defined_chapters(mod) -> None:
    ids = {c.chapter_id for c in mod.CHAPTERS}
    for c in mod.CHAPTERS:
        for pid in c.prerequisites:
            assert pid in ids, f"{c.chapter_id} prerequisite {pid} is undefined"


def test_difficulty_in_range(mod) -> None:
    for c in mod.CHAPTERS:
        assert c.difficulty in (1, 2, 3), f"{c.chapter_id}: difficulty={c.difficulty}"


def test_times_positive(mod) -> None:
    for c in mod.CHAPTERS:
        assert c.reading_time_min > 0
        assert c.lecture_time_min > 0


def test_star_badge_three_chars(mod) -> None:
    for c in mod.CHAPTERS:
        assert len(c.star_badge) == 3
        assert all(ch in "★☆" for ch in c.star_badge)


def test_difficulty_label_is_pdf_safe(mod) -> None:
    for c in mod.CHAPTERS:
        assert c.difficulty_label == f"Level {c.difficulty}/3"
        assert "★" not in c.difficulty_label


def test_chapter_numbers_contiguous(mod) -> None:
    numbered = sorted(c.number for c in mod.CHAPTERS if c.number > 0)
    assert numbered == list(range(1, len(numbered) + 1))


def test_by_id_lookup(mod) -> None:
    c = mod.by_id("unit_I_water_and_life")
    assert c is not None
    assert c.unit == "I"
    assert c.number == 2
    assert mod.by_id("nonexistent_chapter") is None


def test_by_unit_lookup(mod) -> None:
    unit_vi = mod.by_unit("VI")
    assert len(unit_vi) == 3
    assert all(c.unit == "VI" for c in unit_vi)
