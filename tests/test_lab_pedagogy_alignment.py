"""Tests for lab outcome and rubric alignment metadata."""

from __future__ import annotations

from pathlib import Path
import sys


PROJECT = Path(__file__).resolve().parent.parent
SRC = PROJECT / "src"
TEMPLATE_ROOT = PROJECT.parent.parent
for path in (TEMPLATE_ROOT, SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from biology.assessment import (  # noqa: E402
    REQUIRED_LAB_RUBRIC_TERMS,
    chapter_learning_objectives,
    parse_lab_alignment,
)
from biology.toc import load_toc  # noqa: E402


def test_every_lab_maps_to_measurable_outcomes_and_chapter_los() -> None:
    toc = load_toc(PROJECT)
    assert len(toc.labs) == 38
    for lab in toc.labs:
        alignment = parse_lab_alignment(lab.path)
        chapter_los = set(chapter_learning_objectives(lab.chapter.path))
        assert 3 <= len(alignment.outcomes) <= 4, lab.path
        assert set(alignment.lo_ids) <= chapter_los, lab.path
        assert set(alignment.lo_ids), lab.path


def test_every_lab_rubric_covers_core_scientific_practices() -> None:
    toc = load_toc(PROJECT)
    for lab in toc.labs:
        alignment = parse_lab_alignment(lab.path)
        assert tuple(REQUIRED_LAB_RUBRIC_TERMS) == alignment.rubric_terms, lab.path
