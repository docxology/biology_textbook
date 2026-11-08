"""Tests for lab outcome and rubric alignment metadata."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SRC = PROJECT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from textbook_paths import discover_template_root

TEMPLATE_ROOT = discover_template_root(PROJECT)
for path in (TEMPLATE_ROOT, SRC):
    if path is None:
        continue
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from biology.assessment import (
    REQUIRED_LAB_RUBRIC_TERMS,
    chapter_learning_objectives,
    parse_lab_alignment,
)
from biology.toc import load_toc


def test_every_lab_maps_to_measurable_outcomes_and_chapter_los() -> None:
    toc = load_toc(PROJECT)
    assert len(toc.labs) == 44
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
