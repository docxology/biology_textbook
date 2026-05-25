"""V1 instructor-scaffold filling for question banks."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from biology.answer_refinement.classification import (
    _LABEL_RE,
    _QUESTION_LINE,
    classify_question,
    subject_phrase,
    tier_for,
)
from biology.answer_refinement.paths import MANUSCRIPT, QUESTIONS
from textbook_io import write_text_atomic

_SCAFFOLD_BLOCK_RE = re.compile(
    r"<!-- SOLUTION\s*\n"
    r"(\*\*Answer \(Q\d+,[^)]*\)\.\*\*\s*\[INSTRUCTOR SCAFFOLD.*?)"
    r"\n\s*SOLUTION -->",
    re.DOTALL,
)


def generate_answer(q_num: int, tier: str, q_text: str, chapter_ref: str) -> str:
    """Return the legacy V1 answer scaffold body for one question."""

    kind = classify_question(q_text)
    subject = subject_phrase(q_text)
    tier_close = {
        "Recall": (
            "See \\cref{"
            + chapter_ref
            + "} for the definitions and canonical examples."
        ),
        "Application": (
            "Work through the calculation or stepwise reasoning laid out in \\cref{"
            + chapter_ref
            + "} and confirm your numerical answer against the textbook's worked example."
        ),
        "Synthesis": (
            "Use \\cref{"
            + chapter_ref
            + "} as the mechanistic foundation, then extend the argument with one "
            "experimental design or clinical implication — that extension is what "
            "distinguishes a synthesis-tier response."
        ),
    }.get(tier, f"See \\cref{{{chapter_ref}}}.")
    by_kind = {
        "define": (
            f"This question asks for a definition or factual statement about: *{subject}*. "
            "A complete answer names the term precisely, gives one mechanistic or structural detail, "
            "and anchors the definition with one concrete biological example (with a number or unit where possible)."
        ),
        "compare": (
            f"Construct a side-by-side contrast of the two (or more) items named in the question: *{subject}*. "
            "Identify at least two dimensions of comparison (e.g., mechanism, biological context, magnitude), "
            "and state one shared feature plus one distinguishing feature before drawing the final conclusion."
        ),
        "calculate": (
            "This is a numerical problem. Begin by stating the formula (with units), substitute the given values, "
            "carry units through the calculation, and check the result against a plausible biological range. "
            f"Question subject: *{subject}*."
        ),
        "explain": (
            f"Give a mechanistic explanation for *{subject}*. Identify the molecular or cellular players, trace causal "
            "flow from cause to effect, and support the narrative with one quantitative anchor (rate, concentration, or "
            "equilibrium constant) from the chapter."
        ),
        "design": (
            f"Outline an experimental or design response to the prompt on *{subject}*. Specify (i) the variable under test, "
            "(ii) the control, (iii) the measured outcome, and (iv) one prediction — tie each step to the underlying mechanism."
        ),
        "evaluate": (
            f"Take a position on *{subject}* and defend it. State the claim, marshal the strongest pro-evidence from the "
            "chapter, present one counter-consideration, and then explain why your position nevertheless holds (or the "
            "circumstances under which it would fail)."
        ),
        "apply": (
            f"Apply the chapter's framework to the specific scenario: *{subject}*. Identify which principle is invoked, "
            "compute or reason through the consequence, and state the prediction in clinically or biologically operational terms."
        ),
    }
    return f"**Answer (Q{q_num}, {tier}).** {by_kind[kind]} {tier_close}"


def process_bank(path: Path, dry_run: bool = False) -> int:
    """Fill remaining V1 instructor scaffolds in one question bank."""

    text = path.read_text(encoding="utf-8")
    match = _LABEL_RE.search(text)
    if not match:
        print(f"WARN: no label in {path}", file=sys.stderr)
        return 0
    unit, stem = match.group(1), match.group(2)
    chapter_ref = f"sec:{unit}_{stem}"
    q_text = {
        int(match.group(1)): match.group(2)
        for line in text.splitlines()
        if (match := _QUESTION_LINE.match(line))
    }

    def repl(match: re.Match[str]) -> str:
        body = match.group(1)
        header = re.match(r"\*\*Answer \(Q(\d+),\s*([^)]+)\)\.\*\*", body)
        if header is None:
            return match.group(0)
        q_num = int(header.group(1))
        tier = tier_for(q_num)
        answer = generate_answer(q_num, tier, q_text.get(q_num, ""), chapter_ref)
        return f"<!-- SOLUTION\n{answer}\nSOLUTION -->"

    new_text, count = _SCAFFOLD_BLOCK_RE.subn(repl, text)
    if count and not dry_run:
        write_text_atomic(path, new_text)
    return count


__all__ = [
    "MANUSCRIPT",
    "QUESTIONS",
    "generate_answer",
    "process_bank",
    "subject_phrase",
    "classify_question",
    "tier_for",
]
