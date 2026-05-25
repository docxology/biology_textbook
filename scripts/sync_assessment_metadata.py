#!/usr/bin/env python3
"""Synchronize question-bank and lab assessment metadata from the canonical TOC."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.assessment import chapter_learning_objectives
from biology.toc import load_toc

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


ASSESSMENT_COMMENT_RE = re.compile(r"^<!--\s*assess:\s*.*?-->\s*$")
QUESTION_RE = re.compile(r"^(?P<number>\d+)\.\s+")
SOLUTION_START_RE = re.compile(r"^<!--\s*SOLUTION\b")
SOLUTION_END_RE = re.compile(r"^SOLUTION\s*-->\s*$")
LAB_ALIGNMENT_RE = re.compile(
    r"\n?<!--\s*lab-alignment-start\s*-->.*?<!--\s*lab-alignment-end\s*-->\n?",
    re.DOTALL,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Exit non-zero if files are not synchronized")
    mode.add_argument("--dry-run", action="store_true", help="Preview synchronized files without writing changes")
    args = parser.parse_args()

    toc = load_toc(PROJECT)
    changed: list[Path] = []

    for question in toc.questions:
        lo_ids = chapter_learning_objectives(question.chapter.path)
        updated = _sync_question_bank(question.path, lo_ids)
        changed.extend(_write_or_record(question.path, updated, write=not args.check and not args.dry_run))

    for lab in toc.labs:
        lo_ids = chapter_learning_objectives(lab.chapter.path)[:4]
        updated = _sync_lab_alignment(lab.path, lab.chapter.title, lo_ids)
        changed.extend(_write_or_record(lab.path, updated, write=not args.check and not args.dry_run))

    if changed:
        action = "out of sync" if args.check else "would update" if args.dry_run else "updated"
        for path in changed:
            print(f"assessment metadata {action}: {path.relative_to(PROJECT)}")
        return 1 if args.check else 0
    print("assessment metadata synchronized")
    return 0


def _sync_question_bank(path: Path, lo_ids: tuple[str, ...]) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    stripped = [line for line in lines if not ASSESSMENT_COMMENT_RE.match(line)]
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
                    new_lines.append(_assessment_comment(number, lo_ids))
        new_lines.append(line)
        if in_solution and SOLUTION_END_RE.match(line):
            in_solution = False
    return "\n".join(new_lines) + "\n"


def _assessment_comment(number: int, lo_ids: tuple[str, ...]) -> str:
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


def _sync_lab_alignment(path: Path, chapter_title: str, lo_ids: tuple[str, ...]) -> str:
    text = LAB_ALIGNMENT_RE.sub("\n", path.read_text(encoding="utf-8")).rstrip() + "\n"
    block = _lab_alignment_block(chapter_title, lo_ids)
    lines = text.splitlines()
    insert_at = _lab_alignment_insert_index(lines)
    lines[insert_at:insert_at] = block.splitlines()
    return "\n".join(lines) + "\n"


def _lab_alignment_insert_index(lines: list[str]) -> int:
    for index, line in enumerate(lines):
        if line.startswith("## Learning Objectives"):
            cursor = index + 1
            while cursor < len(lines):
                next_line = lines[cursor]
                if cursor > index + 1 and next_line.startswith("## "):
                    return cursor
                cursor += 1
    return min(2, len(lines))


def _lab_alignment_block(chapter_title: str, lo_ids: tuple[str, ...]) -> str:
    outcome_lines = [
        f"- **Outcome {index} ({lo_id}):** {description}"
        for index, (lo_id, description) in enumerate(
            zip(lo_ids, _lab_outcome_descriptions(chapter_title), strict=True),
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


def _lab_outcome_descriptions(chapter_title: str) -> tuple[str, str, str, str]:
    return (
        f"Interpret the supplied evidence or model output for {chapter_title}.",
        "Identify controls and comparison groups that make the claim testable.",
        "Quantify uncertainty, boundary conditions, or alternative explanations before concluding.",
        "Transfer the mechanism to a new biological case or public-facing decision.",
    )


def _write_or_record(path: Path, updated: str, *, write: bool) -> list[Path]:
    current = path.read_text(encoding="utf-8")
    if current == updated:
        return []
    if write:
        write_text_atomic(path, updated)
    return [path]


if __name__ == "__main__":
    raise SystemExit(main())
