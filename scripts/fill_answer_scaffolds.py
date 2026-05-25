#!/usr/bin/env python3
"""Answer scaffold filling — thin CLI."""

from __future__ import annotations

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.answer_refinement.classification import classify_question, subject_phrase, tier_for
from biology.answer_refinement.cli import fill_main
from biology.answer_refinement.paths import MANUSCRIPT, QUESTIONS
from biology.answer_refinement.scaffolds import generate_answer, process_bank

for _name, _value in (
    ("subject_phrase", subject_phrase),
    ("classify_question", classify_question),
    ("generate_answer", generate_answer),
    ("tier_for", tier_for),
    ("process_bank", process_bank),
    ("MANUSCRIPT", MANUSCRIPT),
):
    globals()[_name] = _value
globals()["QUESTIONS"] = QUESTIONS

if __name__ == "__main__":
    raise SystemExit(fill_main())
