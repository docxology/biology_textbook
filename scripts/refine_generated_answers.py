#!/usr/bin/env python3
"""Answer refinement — thin CLI."""

from __future__ import annotations

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.answer_refinement import engine as _engine
from biology.answer_refinement.classification import (
    classify_question,
    is_v1_generated,
    subject_phrase,
)
from biology.answer_refinement.cli import main
from biology.answer_refinement.generation import generate_answer
from biology.answer_refinement.paths import MANUSCRIPT, QUESTIONS

for _name, _value in (
    ("subject_phrase", subject_phrase),
    ("classify_question", classify_question),
    ("is_v1_generated", is_v1_generated),
    ("generate_answer", generate_answer),
    ("process_bank", _engine.process_bank),
    ("MANUSCRIPT", MANUSCRIPT),
):
    globals()[_name] = _value
globals()["QUESTIONS"] = QUESTIONS

if __name__ == "__main__":
    raise SystemExit(main())
