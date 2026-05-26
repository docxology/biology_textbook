"""Synchronize question-bank and lab assessment metadata from the canonical TOC."""

from __future__ import annotations

import re
from pathlib import Path

from biology.assessment import ASSESSMENT_RE, chapter_learning_objectives
from biology.toc import load_toc
from textbook_io import write_text_atomic

QUESTION_RE = re.compile(r"^(?P<number>\d+)\.\s+")
SOLUTION_START_RE = re.compile(r"^<!--\s*SOLUTION\b")
SOLUTION_END_RE = re.compile(r"^SOLUTION\s*-->\s*$")
LAB_ALIGNMENT_RE = re.compile(
    r"\n?<!--\s*lab-alignment-start\s*-->.*?<!--\s*lab-alignment-end\s*-->\n?",
    re.DOTALL,
)


def sync_all_assessment_metadata(
    project_root: Path,
    *,
    check: bool = False,
    dry_run: bool = False,
) -> tuple[list[Path], int]:
    """Synchronize assessment metadata; return changed paths and exit code hint."""

    toc = load_toc(project_root)
    changed: list[Path] = []
    write = not check and not dry_run

    for question in toc.questions:
        lo_ids = chapter_learning_objectives(question.chapter.path)
        updated = sync_question_bank(question.path, lo_ids)
        changed.extend(write_or_record(question.path, updated, write=write))

    for lab in toc.labs:
        lo_ids = chapter_learning_objectives(lab.chapter.path)[:4]
        updated = sync_lab_alignment(lab.path, lab.chapter.title, lo_ids)
        changed.extend(write_or_record(lab.path, updated, write=write))

    return changed, 1 if check and changed else 0


def sync_question_bank(path: Path, lo_ids: tuple[str, ...]) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    stripped = [line for line in lines if not ASSESSMENT_RE.match(line)]
    new_lines: list[str] = []
    in_solution = False

    for line in stripped:
        if SOLUTION_START_RE.match(line):
            in_solution = True
        if not in_solution:
            question_match = QUESTION_RE.match(line)
            if question_match:
                number = int(question_match.group("number"))
                if 1 <= number <= 30:
                    new_lines.append(assessment_comment(number, lo_ids))
        new_lines.append(line)
        if in_solution and SOLUTION_END_RE.match(line):
            in_solution = False
    return "\n".join(new_lines) + "\n"


def assessment_comment(number: int, lo_ids: tuple[str, ...]) -> str:
    lo_id = lo_ids[(number - 1) % len(lo_ids)]
    if number <= 5:
        bloom, difficulty, minutes = "Remember", "Recall", 2
    elif number <= 10:
        bloom, difficulty, minutes = "Understand", "Recall", 2
    elif number <= 15:
        bloom, difficulty, minutes = "Apply", "Application", 4
    elif number <= 20:
        bloom, difficulty, minutes = "Analyze", "Application", 5
    elif number <= 24:
        bloom, difficulty, minutes = "Analyze", "Synthesis", 7
    elif number <= 27:
        bloom, difficulty, minutes = "Evaluate", "Synthesis", 8
    else:
        bloom, difficulty, minutes = "Create", "Synthesis", 9
    return (
        "<!-- assess: "
        f"LO={lo_id}; bloom={bloom}; difficulty={difficulty}; format=short-answer; minutes={minutes} "
        "-->"
    )


def sync_lab_alignment(path: Path, chapter_title: str, lo_ids: tuple[str, ...]) -> str:
    text = LAB_ALIGNMENT_RE.sub("\n", path.read_text(encoding="utf-8")).rstrip() + "\n"
    block = lab_alignment_block(chapter_title, lo_ids)
    lines = text.splitlines()
    insert_at = lab_alignment_insert_index(lines)
    lines[insert_at:insert_at] = block.splitlines()
    return "\n".join(lines) + "\n"


def lab_alignment_insert_index(lines: list[str]) -> int:
    for index, line in enumerate(lines):
        if line.startswith("## Learning Objectives"):
            cursor = index + 1
            while cursor < len(lines):
                next_line = lines[cursor]
                if cursor > index + 1 and next_line.startswith("## "):
                    return cursor
                cursor += 1
    return min(2, len(lines))


def lab_alignment_block(chapter_title: str, lo_ids: tuple[str, ...]) -> str:
    outcome_lines = [
        f"- **Outcome {index} ({lo_id}):** {description}"
        for index, (lo_id, description) in enumerate(
            zip(lo_ids, lab_outcome_descriptions(chapter_title), strict=True),
            start=1,
        )
    ]
    lo_display = ", ".join(lo_ids)
    return "\n".join(
        [
            "<!-- lab-alignment-start -->",
            "### Alignment and Rubric Map {.unnumbered}",
            "",
            *outcome_lines,
            f"- **Chapter LO coverage:** {lo_display}",
            "- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.",
            "<!-- lab-alignment-end -->",
        ]
    )


def lab_outcome_descriptions(chapter_title: str) -> tuple[str, str, str, str]:
    return (
        f"Interpret the supplied evidence or model output for {chapter_title}.",
        "Identify controls and comparison groups that make the claim testable.",
        "Quantify uncertainty, boundary conditions, or alternative explanations before concluding.",
        "Transfer the mechanism to a new biological case or public-facing decision.",
    )


def write_or_record(path: Path, updated: str, *, write: bool) -> list[Path]:
    current = path.read_text(encoding="utf-8")
    if current == updated:
        return []
    if write:
        write_text_atomic(path, updated)
    return [path]


__all__ = [
    "assessment_comment",
    "lab_alignment_block",
    "lab_alignment_insert_index",
    "lab_outcome_descriptions",
    "sync_all_assessment_metadata",
    "sync_lab_alignment",
    "sync_question_bank",
    "write_or_record",
]
