"""Validate authored solution coverage without inserting release scaffolds."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from biology.answer_refinement.engine import process_bank
from biology.answer_refinement.generation import UnsupportedAnswerRepair


@dataclass(frozen=True)
class SolutionScaffoldReport:
    scaffolds_inserted: int
    files_touched: int


def scaffold_block(q_num: int, question_text: str) -> str:
    raise UnsupportedAnswerRepair(
        f"Q{q_num}: author a substantive SOLUTION for {question_text!r}; placeholder insertion is not supported"
    )


def process_question_bank(path: Path, *, dry_run: bool = False, write: bool = True) -> int:
    """Require real solutions in every mode; never insert non-answers."""
    process_bank(path, dry_run=dry_run or not write)
    return 0


def insert_solution_scaffolds(
    questions_dir: Path, *, dry_run: bool = False, write: bool = True,
) -> SolutionScaffoldReport:
    banks = sorted(questions_dir.rglob("questions_*.md"))
    if not banks:
        raise ValueError(f"No question banks found in {questions_dir}; refusing a silent no-op")
    for bank in banks:
        process_question_bank(bank, dry_run=dry_run, write=write)
    return SolutionScaffoldReport(scaffolds_inserted=0, files_touched=0)


__all__ = ["SolutionScaffoldReport", "insert_solution_scaffolds", "process_question_bank", "scaffold_block"]
