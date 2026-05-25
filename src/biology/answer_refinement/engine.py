"""Answer refinement engine."""

from __future__ import annotations

import re
from pathlib import Path

from biology.answer_refinement.classification import (
    _LABEL_RE,
    _QUESTION_LINE,
    is_v1_generated,
    tier_for,
)
from biology.answer_refinement.evidence import chapter_category, chapter_evidence
from biology.answer_refinement.generation import _BLOCK_RE, generate_answer
from textbook_io import write_text_atomic

__all__ = ["process_bank"]


def process_bank(path: Path, dry_run: bool = False) -> tuple[int, int]:
    """Refine every v1-generated answer. Return (refined, skipped_non_v1)."""
    text = path.read_text(encoding="utf-8")

    match = _LABEL_RE.search(text)
    if not match:
        return (0, 0)
    unit, stem = match.group(1), match.group(2)
    chapter_ref = f"sec:{unit}_{stem}"
    category = chapter_category(stem)

    q_text: dict[int, str] = {}
    for line in text.splitlines():
        if (qm := _QUESTION_LINE.match(line)):
            number = int(qm.group(1))
            if 1 <= number <= 30:
                q_text[number] = qm.group(2)

    refined = 0
    skipped = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal refined, skipped
        opener, body, q_num_str, closer = match.group(1), match.group(2), match.group(3), match.group(4)
        if not is_v1_generated(body):
            skipped += 1
            return match.group(0)
        q_num = int(q_num_str)
        tier = tier_for(q_num)
        qt = q_text.get(q_num, "")
        evidence = chapter_evidence(unit, stem, qt, category)
        new_body = generate_answer(q_num, tier, qt, chapter_ref, category, evidence)
        if new_body == body:
            skipped += 1
            return match.group(0)
        refined += 1
        return f"{opener}{new_body}{closer}"

    new_text = _BLOCK_RE.sub(repl, text)
    if refined and not dry_run:
        write_text_atomic(path, new_text)
    return (refined, skipped)
