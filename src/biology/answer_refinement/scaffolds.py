"""Refuse unsupported scaffold filling rather than publish generic guidance."""

from biology.answer_refinement.classification import (
    classify_question,
    subject_phrase,
    tier_for,
)
from biology.answer_refinement.engine import process_bank as _process_bank
from biology.answer_refinement.generation import generate_answer
from biology.answer_refinement.paths import MANUSCRIPT, QUESTIONS


def process_bank(path, dry_run: bool = False) -> int:
    """Preserve authored answers, or fail without writing for missing scaffolds."""
    refined, _ = _process_bank(path, dry_run=dry_run)
    return refined


__all__ = ["MANUSCRIPT", "QUESTIONS", "classify_question", "generate_answer", "process_bank", "subject_phrase", "tier_for"]
