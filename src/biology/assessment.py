"""Assessment metadata parsing for textbook question banks and labs."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
import re


ASSESSMENT_RE = re.compile(r"^<!--\s*assess:\s*(?P<body>.*?)\s*-->\s*$")
QUESTION_RE = re.compile(r"^(?P<number>\d+)\.\s+")
SOLUTION_START_RE = re.compile(r"^<!--\s*SOLUTION\b")
SOLUTION_END_RE = re.compile(r"^SOLUTION\s*-->\s*$")
LAB_ALIGNMENT_RE = re.compile(
    r"<!--\s*lab-alignment-start\s*-->(?P<body>.*?)<!--\s*lab-alignment-end\s*-->",
    re.DOTALL,
)

ALLOWED_BLOOM_LEVELS = {"Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"}
ALLOWED_DIFFICULTIES = {"Recall", "Application", "Synthesis"}
REQUIRED_LAB_RUBRIC_TERMS = ("evidence", "controls", "uncertainty", "mechanism", "transfer")


@dataclass(frozen=True)
class QuestionAssessment:
    """Metadata attached to one question-bank item."""

    number: int
    lo: str
    bloom: str
    difficulty: str
    format: str
    minutes: int


@dataclass(frozen=True)
class QuestionBankAssessment:
    """Parsed assessment view for a single question-bank file."""

    path: Path
    items: tuple[QuestionAssessment, ...]

    @property
    def assessed_los(self) -> set[str]:
        """Return the chapter learning-objective IDs covered by this bank."""
        return {item.lo for item in self.items}

    @property
    def bloom_mix(self) -> dict[str, int]:
        """Return item counts by Bloom level."""
        return _count_by(item.bloom for item in self.items)

    @property
    def difficulty_mix(self) -> dict[str, int]:
        """Return item counts by difficulty band."""
        return _count_by(item.difficulty for item in self.items)


@dataclass(frozen=True)
class LabAlignment:
    """Parsed measurable outcomes and rubric terms for a lab companion."""

    path: Path
    outcomes: tuple[str, ...]
    lo_ids: tuple[str, ...]
    rubric_terms: tuple[str, ...]


def parse_question_bank(path: Path) -> QuestionBankAssessment:
    """Parse all ``<!-- assess: ... -->`` comments in a question bank."""

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    items: list[QuestionAssessment] = []
    pending: dict[str, str] | None = None
    in_solution = False

    for line in lines:
        if SOLUTION_START_RE.match(line):
            in_solution = True
        if in_solution:
            if SOLUTION_END_RE.match(line):
                in_solution = False
            continue
        assessment_match = ASSESSMENT_RE.match(line)
        if assessment_match:
            pending = _parse_assessment_fields(assessment_match.group("body"))
            continue
        question_match = QUESTION_RE.match(line)
        if question_match:
            number = int(question_match.group("number"))
            if 1 <= number <= 30:
                if pending is None:
                    raise ValueError(f"Missing assessment metadata before question {number} in {path}")
                items.append(_question_assessment(number, pending, path))
                pending = None
    return QuestionBankAssessment(path=path, items=tuple(items))


def parse_lab_alignment(path: Path) -> LabAlignment:
    """Parse the lab alignment block produced by ``sync_assessment_metadata``."""

    text = path.read_text(encoding="utf-8")
    match = LAB_ALIGNMENT_RE.search(text)
    if not match:
        raise ValueError(f"Missing lab alignment block in {path}")
    body = match.group("body")
    outcomes = tuple(
        line.strip()
        for line in body.splitlines()
        if re.match(r"- \*\*Outcome \d+ \(LO\d+\):\*\*", line.strip())
    )
    lo_ids = tuple(dict.fromkeys(re.findall(r"\bLO\d+\b", body)))
    rubric_terms = tuple(term for term in REQUIRED_LAB_RUBRIC_TERMS if re.search(rf"\b{term}\b", body, re.I))
    return LabAlignment(path=path, outcomes=outcomes, lo_ids=lo_ids, rubric_terms=rubric_terms)


def chapter_learning_objectives(path: Path) -> tuple[str, ...]:
    """Return stable LO IDs derived from the chapter's Learning Objectives list."""

    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## Learning Objectives.*?\n(?P<body>.*?)(?=^##\s|\Z)", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError(f"Missing Learning Objectives section in {path}")
    objective_numbers = re.findall(r"^\d+\.\s+", match.group("body"), re.MULTILINE)
    if not objective_numbers:
        raise ValueError(f"Learning Objectives section has no numbered items in {path}")
    return tuple(f"LO{index}" for index in range(1, len(objective_numbers) + 1))


def _parse_assessment_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for part in body.split(";"):
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        fields[key.strip()] = value.strip()
    return fields


def _question_assessment(number: int, fields: dict[str, str], path: Path) -> QuestionAssessment:
    required = {"LO", "bloom", "difficulty", "format", "minutes"}
    missing = required - set(fields)
    if missing:
        raise ValueError(f"Question {number} in {path} missing metadata fields: {sorted(missing)}")
    if fields["bloom"] not in ALLOWED_BLOOM_LEVELS:
        raise ValueError(
            f"Question {number} in {path} has invalid bloom level {fields['bloom']!r}; "
            f"expected one of {sorted(ALLOWED_BLOOM_LEVELS)}"
        )
    if fields["difficulty"] not in ALLOWED_DIFFICULTIES:
        raise ValueError(
            f"Question {number} in {path} has invalid difficulty {fields['difficulty']!r}; "
            f"expected one of {sorted(ALLOWED_DIFFICULTIES)}"
        )
    try:
        minutes = int(fields["minutes"])
    except ValueError as exc:
        raise ValueError(f"Question {number} in {path} has non-integer minutes") from exc
    return QuestionAssessment(
        number=number,
        lo=fields["LO"],
        bloom=fields["bloom"],
        difficulty=fields["difficulty"],
        format=fields["format"],
        minutes=minutes,
    )


def _count_by(values: Iterable[object]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        key = str(value)
        counts[key] = counts.get(key, 0) + 1
    return counts


__all__ = [
    "ALLOWED_BLOOM_LEVELS",
    "ALLOWED_DIFFICULTIES",
    "QuestionAssessment",
    "QuestionBankAssessment",
    "LabAlignment",
    "REQUIRED_LAB_RUBRIC_TERMS",
    "chapter_learning_objectives",
    "parse_lab_alignment",
    "parse_question_bank",
]
