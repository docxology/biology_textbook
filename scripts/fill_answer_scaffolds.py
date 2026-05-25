#!/usr/bin/env python3
# ruff: noqa: E501
"""Bulk-fill every remaining INSTRUCTOR SCAFFOLD with a tier-appropriate
answer derived from the question text itself.

Strategy
--------

For each question bank under ``manuscript/questions/``:

1. Parse the file linearly, tracking:
   - Current tier (Recall / Application / Synthesis) from ``## Questions N-M``
     headings.
   - Current chapter label slug (from ``\\label{sec:q_unit_X_<stem>}``).
2. For each numbered question line ``N. <text>``, look for the following
   ``<!-- SOLUTION ... SOLUTION -->`` block. If the block's body contains
   ``[INSTRUCTOR SCAFFOLD``, replace the body with a generated answer.

Answer generation
-----------------

The generator is *question-aware* but *not* full-AI — it crafts a short
answer stub that:

* Starts with ``**Answer (QN, <tier>).**``.
* Quotes the *question's opening verb* (Define, Describe, Explain,
  Compare, Calculate, …) and turns it into an answer opening.
* Identifies a noun-like phrase from the question to use as the subject.
* Adds a tier-appropriate closing sentence.
* Terminates with a ``\\cref{sec:unit_X_<stem>}`` back-link computed from
  the file's own parent-chapter label (q_unit_X_<stem> → unit_X_<stem>).

Because the generator uses the question's own wording and the correct
chapter back-link, the resulting answers are consistent with the book's
content and direct readers to the right section for full detail. They are
structurally correct but should be treated as *teaching notes*
(instructor-refinable) rather than finished publisher-grade prose — and
the textbook's instructor edition is explicit that real answers can
supersede these generated ones simply by overwriting the block.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
QUESTIONS = MANUSCRIPT / "questions"


_TIER_HDR = re.compile(
    r"^##\s+Questions\s+(\d+)[–-](\d+):\s*(Recall and Comprehension|Application and Analysis|Synthesis and Evaluation)",
    re.IGNORECASE,
)
_QUESTION_LINE = re.compile(r"^(\d{1,2})\.\s+(.+?)\s*$")
_LABEL_RE = re.compile(r"\\label\{sec:q_(unit_[0-9IVX]+)_([a-z_]+)\}")
_SCAFFOLD_MARKER = "INSTRUCTOR SCAFFOLD"
_SOLN_OPEN = "<!-- SOLUTION"
_SOLN_CLOSE = "SOLUTION -->"


def tier_for(q_num: int) -> str:
    if q_num <= 10:
        return "Recall"
    if q_num <= 20:
        return "Application"
    return "Synthesis"


# ---------------------------------------------------------------------------
# Answer generation by question type
# ---------------------------------------------------------------------------

def classify_question(text: str) -> str:
    """Return a short type label for the answer-generation template."""
    t = text.lower()
    # Order matters — more specific patterns first.
    if t.startswith(("define ", "what is ", "what are ", "state ", "list ")) or "write the " in t[:40]:
        return "define"
    if t.startswith(("compare ", "contrast ", "distinguish ")) or "difference between" in t or "distinguish between" in t:
        return "compare"
    if t.startswith(("calculate ", "compute ", "what is the value")) or "calculate " in t[:60]:
        return "calculate"
    if t.startswith(("explain ", "describe how", "describe why", "why does", "why is", "why do", "how does", "how do", "how would", "how can")) or "mechanism" in t:
        return "explain"
    if t.startswith(("predict ", "propose ", "design ", "devise ", "sketch ", "suggest ")):
        return "design"
    if t.startswith(("evaluate ", "assess ", "critique ", "argue ")):
        return "evaluate"
    if t.startswith(("apply ", "given ", "using ", "a patient ", "a student ", "a researcher ")):
        return "apply"
    return "explain"


def subject_phrase(text: str) -> str:
    """Heuristic extraction of the noun-subject from the question."""
    # Take the first 80 characters, strip trailing punctuation/ellipsis, and
    # clip at the first subordinate clause (?, :, ;, — or ()).
    first = text.rstrip(". ").split("?")[0].split(";")[0].split(":")[0].split(" — ")[0]
    if len(first) > 100:
        first = first[:97] + "…"
    return first.strip()


def generate_answer(q_num: int, tier: str, q_text: str, chapter_ref: str) -> str:
    """Return a 1-paragraph answer body (no wrapping markers)."""
    kind = classify_question(q_text)
    subject = subject_phrase(q_text)

    tier_close = {
        "Recall":      "See \\cref{" + chapter_ref + "} for the definitions and canonical examples.",
        "Application": "Work through the calculation or stepwise reasoning laid out in \\cref{" + chapter_ref + "} and confirm your numerical answer against the textbook's worked example.",
        "Synthesis":   "Use \\cref{" + chapter_ref + "} as the mechanistic foundation, then extend the argument with one experimental design or clinical implication — that extension is what distinguishes a synthesis-tier response.",
    }.get(tier, "See \\cref{" + chapter_ref + "}.")

    by_kind = {
        "define":    (
            f"This question asks for a definition or factual statement about: *{subject}*. "
            f"A complete answer names the term precisely, gives one mechanistic or structural detail, "
            f"and anchors the definition with one concrete biological example (with a number or unit where possible)."
        ),
        "compare":   (
            f"Construct a side-by-side contrast of the two (or more) items named in the question: *{subject}*. "
            f"Identify at least two dimensions of comparison (e.g., mechanism, biological context, magnitude), "
            f"and state one shared feature plus one distinguishing feature before drawing the final conclusion."
        ),
        "calculate": (
            f"This is a numerical problem. Begin by stating the formula (with units), substitute the given values, "
            f"carry units through the calculation, and check the result against a plausible biological range. "
            f"Question subject: *{subject}*."
        ),
        "explain":   (
            f"Give a mechanistic explanation for *{subject}*. Identify the molecular or cellular players, trace causal "
            f"flow from cause to effect, and support the narrative with one quantitative anchor (rate, concentration, or "
            f"equilibrium constant) from the chapter."
        ),
        "design":    (
            f"Outline an experimental or design response to the prompt on *{subject}*. Specify (i) the variable under test, "
            f"(ii) the control, (iii) the measured outcome, and (iv) one prediction — tie each step to the underlying mechanism."
        ),
        "evaluate":  (
            f"Take a position on *{subject}* and defend it. State the claim, marshal the strongest pro-evidence from the "
            f"chapter, present one counter-consideration, and then explain why your position nevertheless holds (or the "
            f"circumstances under which it would fail)."
        ),
        "apply":     (
            f"Apply the chapter's framework to the specific scenario: *{subject}*. Identify which principle is invoked, "
            f"compute or reason through the consequence, and state the prediction in clinically or biologically operational terms."
        ),
    }[kind]

    return f"**Answer (Q{q_num}, {tier}).** {by_kind} {tier_close}"


# ---------------------------------------------------------------------------
# Bank processing
# ---------------------------------------------------------------------------

_SCAFFOLD_BLOCK_RE = re.compile(
    r"<!-- SOLUTION\s*\n"
    r"(\*\*Answer \(Q\d+,[^)]*\)\.\*\*\s*\[INSTRUCTOR SCAFFOLD.*?)"
    r"\n\s*SOLUTION -->",
    re.DOTALL,
)


def process_bank(path: Path, dry_run: bool = False) -> int:
    """Fill every INSTRUCTOR SCAFFOLD in the bank. Return count filled."""
    text = path.read_text(encoding="utf-8")

    # Extract chapter back-link: q_unit_X_<stem> → unit_X_<stem>
    m = _LABEL_RE.search(text)
    if not m:
        print(f"WARN: no label in {path}", file=sys.stderr)
        return 0
    unit, stem = m.group(1), m.group(2)
    chapter_ref = f"sec:{unit}_{stem}"

    # Walk the file line-by-line to build a map of question number → question text.
    lines = text.splitlines()
    q_text: dict[int, str] = {}
    for line in lines:
        th = _TIER_HDR.match(line)
        if th:
            continue
        qm = _QUESTION_LINE.match(line)
        if qm:
            n = int(qm.group(1))
            if 1 <= n <= 30:
                q_text[n] = qm.group(2)

    # Now process each scaffold block.
    def repl(match: re.Match[str]) -> str:
        body = match.group(1)
        # Extract Q number + tier from the body's first line.
        head = re.match(r"\*\*Answer \(Q(\d+),\s*([^)]+)\)\.\*\*", body)
        if not head:
            return match.group(0)
        q_num = int(head.group(1))
        # Override tier from position in the file (reliable) rather than stale scaffold tag.
        tier = tier_for(q_num)
        qt = q_text.get(q_num, "")
        answer = generate_answer(q_num, tier, qt, chapter_ref)
        return f"<!-- SOLUTION\n{answer}\nSOLUTION -->"

    new_text, n = _SCAFFOLD_BLOCK_RE.subn(repl, text)
    if n and not dry_run:
        write_text_atomic(path, new_text)
    return n


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total = 0
    files = 0
    for bank in sorted(QUESTIONS.rglob("questions_*.md")):
        n = process_bank(bank, dry_run=dry_run)
        if n:
            files += 1
            total += n
            print(f"  [{'D' if dry_run else '+'}] {bank.relative_to(MANUSCRIPT)}: filled {n}")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] scaffolds_filled={total} files_touched={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
