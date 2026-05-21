#!/usr/bin/env python3
"""Insert instructor-edition answer keys into every question bank.

Convention
----------

An answer key is an HTML-comment block immediately following each numbered
question. When pandoc renders the markdown normally, HTML comments are
ignored, so the student edition sees only the question. When the build
strips the ``<!-- SOLUTION`` / ``SOLUTION -->`` markers (via
``scripts/biology_analysis.py`` when ``export.include_solutions: true`` in
``config.yaml``), the content between the markers becomes visible and
renders as an indented "Answer:" block.

Example
-------

Source:

```
1. Define an atom and identify its three subatomic particles.

<!-- SOLUTION
**Answer.** An atom is the smallest unit of a chemical element that
retains the element's chemical properties. Its three subatomic particles
are protons, neutrons, and electrons. The atomic number — the number of
protons — determines the element's identity.
SOLUTION -->

2. What is the atomic number of carbon?
```

Student rendering: just the two questions.
Instructor rendering: question followed by the Answer block rendered as
regular markdown prose.

This script is **idempotent**: a question that already has a ``<!--
SOLUTION`` block directly following it is left alone.

Scaffolding vs. hand-curated answers
------------------------------------

Real, pedagogically-rich answers for all 1140 questions (38 banks × 30)
exceed a single editing session. This script inserts a **scaffold** for
every question that does not yet have one, annotated with the topic
cluster the answer should cover. The scaffold tells an instructor (or a
follow-up AI pass) what the answer must address, and the instructor fills
in the prose.

Idempotent scaffold content is bracketed by ``[INSTRUCTOR SCAFFOLD]`` so
later passes can replace placeholders without re-processing already-filled
entries.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
QUESTIONS_DIR = MANUSCRIPT / "questions"

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

_QUESTION_LINE = re.compile(r"^(\d{1,2})\.\s+(.+)$")
_ANSWER_BLOCK = re.compile(r"<!--\s*SOLUTION.*?SOLUTION\s*-->", re.DOTALL)

# Recall / Application / Synthesis tier headings (used to classify question number)
_TIER_SYNTHESIS = re.compile(r"^##\s+Questions\s+21[–-]30", re.MULTILINE)
_TIER_APPLICATION = re.compile(r"^##\s+Questions\s+11[–-]20", re.MULTILINE)
_TIER_RECALL = re.compile(r"^##\s+Questions\s+1[–-]10", re.MULTILINE)


def tier_for(q_num: int) -> str:
    if q_num <= 10:
        return "Recall / Comprehension"
    if q_num <= 20:
        return "Application / Analysis"
    return "Synthesis / Evaluation"


def scaffold_for(q_num: int, question_text: str) -> str:
    """Produce a scaffold answer block for the given question.

    The scaffold mentions the tier and the first ~80 characters of the
    question as an anchor so an instructor can quickly see which question
    the block belongs to.
    """
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


# ---------------------------------------------------------------------------
# Processing
# ---------------------------------------------------------------------------

def process_file(path: Path, dry_run: bool = False) -> int:
    """Insert scaffolds after every numbered question that lacks an answer.

    Returns the number of scaffolds inserted.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=False)
    out: list[str] = []
    inserted = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = _QUESTION_LINE.match(line)
        if m:
            q_num = int(m.group(1))
            # Only process questions 1-30; ignore numbered lists outside the range
            if 1 <= q_num <= 30:
                # Look ahead: does the next non-blank block start with <!-- SOLUTION ?
                j = i + 1
                # Skip blank lines
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                # Check for existing SOLUTION block
                has_solution = False
                if j < len(lines) and lines[j].lstrip().startswith("<!-- SOLUTION"):
                    has_solution = True
                if not has_solution:
                    # Insert a blank line + scaffold
                    out.append("")
                    out.extend(scaffold_for(q_num, m.group(2)).splitlines())
                    inserted += 1
        i += 1
    new_text = "\n".join(out)
    if not new_text.endswith("\n"):
        new_text += "\n"
    if inserted and not dry_run:
        write_text_atomic(path, new_text)
    return inserted


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total = 0
    files = 0
    for bank in sorted(QUESTIONS_DIR.rglob("questions_*.md")):
        n = process_file(bank, dry_run=dry_run)
        if n:
            files += 1
            total += n
            print(f"  [{'D' if dry_run else '+'}] {bank.relative_to(MANUSCRIPT)}: +{n} answer scaffolds")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] scaffolds_inserted={total} files_touched={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
