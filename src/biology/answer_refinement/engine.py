"""Non-writing validation of answer banks, preserving reviewed solutions."""

from __future__ import annotations

import re
from pathlib import Path

from biology.answer_refinement.classification import _LABEL_RE, is_v1_generated
from biology.answer_refinement.generation import UnsupportedAnswerRepair
from biology.crossref.source import visible_text

_SOLUTION_RE = re.compile(r"<!--\s*SOLUTION\b(?P<body>.*?)\bSOLUTION\s*-->", re.DOTALL)
_QUESTION_RE = re.compile(r"^(\d{1,2})\.\s+(.+)$", re.MULTILINE)


def process_bank(path: Path, dry_run: bool = False) -> tuple[int, int]:
    """Refuse unsupported repairs in both modes, without changing any bytes."""
    text = path.read_text(encoding="utf-8")
    visible = visible_text(text)
    labels = set(_LABEL_RE.findall(visible))
    if len(labels) != 1:
        raise ValueError(f"{path}: author one canonical H1 question-bank identifier (sec:q_unit_...).")
    blocks = list(_SOLUTION_RE.finditer(visible))
    if len(re.findall(r"<!--\s*SOLUTION\b", visible)) != len(blocks):
        raise ValueError(f"{path}: malformed SOLUTION block; repair its delimiters before proceeding")
    prompt_text = _SOLUTION_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group()), visible)
    questions = list(_QUESTION_RE.finditer(prompt_text))
    if not questions:
        raise ValueError(f"{path}: no numbered question items; refusing a silent no-op")
    numbers = [int(question.group(1)) for question in questions]
    if any(not 1 <= number <= 30 for number in numbers) or len(numbers) != len(set(numbers)):
        raise ValueError(f"{path}: author unique question identifiers in the range 1–30")
    preserved = 0
    used: set[int] = set()
    for index, question in enumerate(questions):
        number = int(question.group(1))
        end = questions[index + 1].start() if index + 1 < len(questions) else len(text)
        answers = [(i, block) for i, block in enumerate(blocks) if question.end() <= block.start() < end]
        if len(answers) != 1:
            raise UnsupportedAnswerRepair(f"{path}: Q{number} requires one authored substantive SOLUTION; no changes written")
        block_index, block = answers[0]
        used.add(block_index)
        body = block.group("body").strip()
        if not body or "INSTRUCTOR SCAFFOLD" in body or is_v1_generated(body):
            raise UnsupportedAnswerRepair(f"{path}: Q{number} has no supported automatic repair; author its prompt-specific SOLUTION. No changes written.")
        header = re.search(r"\*\*Answer \(Q(\d+),", body)
        if header and int(header.group(1)) != number:
            raise ValueError(f"{path}: SOLUTION label does not match Q{number}")
        preserved += 1
    if len(used) != len(blocks):
        raise ValueError(f"{path}: unattached SOLUTION block; author an unambiguous item mapping")
    return 0, preserved


__all__ = ["process_bank"]
