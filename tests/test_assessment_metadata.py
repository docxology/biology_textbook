"""Tests for question-bank assessment metadata coverage."""

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
    ALLOWED_BLOOM_LEVELS,
    ALLOWED_DIFFICULTIES,
    chapter_learning_objectives,
    parse_question_bank,
)
from biology.toc import load_toc  # noqa: E402


def test_all_question_bank_items_have_assessment_metadata() -> None:
    toc = load_toc(PROJECT)
    item_count = 0
    for question in toc.questions:
        bank = parse_question_bank(question.path)
        assert len(bank.items) == 30, question.path
        assert [item.number for item in bank.items] == list(range(1, 31))
        item_count += len(bank.items)
    assert item_count == 1170


def test_each_chapter_learning_objective_is_assessed() -> None:
    toc = load_toc(PROJECT)
    for question in toc.questions:
        expected_los = set(chapter_learning_objectives(question.chapter.path))
        bank = parse_question_bank(question.path)
        assert expected_los <= bank.assessed_los, question.path


def test_question_bank_metadata_has_auditable_bloom_and_difficulty_mix() -> None:
    toc = load_toc(PROJECT)
    for question in toc.questions:
        bank = parse_question_bank(question.path)
        assert {item.bloom for item in bank.items} <= ALLOWED_BLOOM_LEVELS
        assert {item.difficulty for item in bank.items} <= ALLOWED_DIFFICULTIES
        assert {"Recall", "Application", "Synthesis"} <= set(bank.difficulty_mix)
        assert {"Analyze", "Evaluate", "Create"} & set(bank.bloom_mix)
        assert all(item.format == "short-answer" for item in bank.items)
        assert all(item.minutes > 0 for item in bank.items)
