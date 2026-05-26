"""Insert instructor-edition answer scaffolds into question banks."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from biology.answer_refinement.classification import tier_for
from textbook_io import write_text_atomic

QUESTION_LINE = re.compile(r"^(\d{1,2})\.\s+(.+)$")


@dataclass(frozen=True)
class SolutionScaffoldReport:
    scaffolds_inserted: int
    files_touched: int


def scaffold_block(q_num: int, question_text: str) -> str:
    tier = tier_for(q_num)
    anchor = question_text.strip()
    if len(anchor) > 80:
        anchor = anchor[:77] + "..."
    return (
        f"<!-- SOLUTION\n"
        f"**Answer (Q{q_num}, {tier}).** [INSTRUCTOR SCAFFOLD — fill in]\n\n"
        f"_Question anchor: {anchor}_\n\n"
        f"Key concepts this answer should address (fill in by instructor):\n"
        f"- Core definition or mechanism relevant to the question.\n"
        f"- At least one quantitative or specific-example detail.\n"
        f"- Connection to a textbook section (use `\\cref{{sec:…}}`).\n"
        f"- For synthesis questions: one experimental or clinical implication.\n"
        f"SOLUTION -->"
    )


def process_question_bank(path: Path, *, dry_run: bool = False, write: bool = True) -> int:
    """Insert scaffolds after numbered questions that lack answer blocks."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=False)
    out: list[str] = []
    inserted = 0
    index = 0
    while index < len(lines):
        line = lines[index]
        out.append(line)
        match = QUESTION_LINE.match(line)
        if match:
            q_num = int(match.group(1))
            if 1 <= q_num <= 30:
                lookahead = index + 1
                while lookahead < len(lines) and lines[lookahead].strip() == "":
                    lookahead += 1
                has_solution = lookahead < len(lines) and lines[lookahead].lstrip().startswith("<!-- SOLUTION")
                if not has_solution:
                    out.append("")
                    out.extend(scaffold_block(q_num, match.group(2)).splitlines())
                    inserted += 1
        index += 1
    new_text = "\n".join(out)
    if not new_text.endswith("\n"):
        new_text += "\n"
    if inserted and write and not dry_run:
        write_text_atomic(path, new_text)
    return inserted


def insert_solution_scaffolds(
    questions_dir: Path,
    *,
    dry_run: bool = False,
    write: bool = True,
) -> SolutionScaffoldReport:
    total = 0
    files_touched = 0
    for bank in sorted(questions_dir.rglob("questions_*.md")):
        inserted = process_question_bank(bank, dry_run=dry_run, write=write)
        if inserted:
            files_touched += 1
            total += inserted
    return SolutionScaffoldReport(scaffolds_inserted=total, files_touched=files_touched)


__all__ = [
    "SolutionScaffoldReport",
    "insert_solution_scaffolds",
    "process_question_bank",
    "scaffold_block",
]
