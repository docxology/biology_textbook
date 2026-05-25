"""Question-bank answer-key refinement for embedded enrichment."""

from __future__ import annotations

import re

from biology.answer_refinement.classification import (
    _CLAUSE_RE,
    _NAMED_ENTITY_RE,
    _QUANTITY_RE,
    _STOP_NAMED,
    question_kind,
    subject_phrase,
)
from biology.enrichment.catalog import FOCUS_BY_STEM
from biology.enrichment.models import ChapterRecord
from textbook_io import write_text_atomic

_QUESTION_LINE = re.compile(r"^(\d{1,2})\.\s+(.+?)\s*$", re.MULTILINE)
_SOLUTION_BLOCK = re.compile(
    r"(<!-- SOLUTION\s*\n)(.*?)(\n\s*SOLUTION -->)",
    flags=re.DOTALL,
)

ANSWER_SIGNATURES = (
    "Rubric for *",
    "name the relevant players",
    "scale-setting detail",
    "state the judgment, cite two lines of evidence",
    "identify the governing equation or ratio",
    "specify the manipulated variable",
    "a complete response should",
    "Chapter-specific anchor:",
    "Common pitfall:",
    "Answer key for *",
    "define the concept precisely",
    "place it at the correct biological scale",
    "trace the causal sequence",
    "choose the relevant equation, ratio, or probability model",
    "state the hypothesis, variable being changed",
    "make a justified judgment",
    "Name the term in ",
    "Evidence anchor:",
    "Tie the reasoning to \\cref{",
    "Credit requires an explicit mechanism",
    "prompt-linked evidence",
    "Core response for *",
    "Expected answer for *",
)


def evidence_target(kind: str, record: ChapterRecord) -> str:
    targets = {
        "definition": "definition, boundary condition, and one concrete example",
        "mechanism": "causal sequence, named components, and a measurable intermediate",
        "comparison": "two comparison axes, shared feature, difference, and consequence",
        "quantitative": "equation or ratio, substitutions with units, range check, and interpretation",
        "experimental": "hypothesis, control, measured response, predicted pattern, and falsifier",
        "evaluation": "judgment, two evidence lines, limitation, and condition that would change the conclusion",
        "application": "chapter principle, decisive evidence in the scenario, and observable prediction",
    }
    return targets[kind] + f" from \\cref{{{record.section_ref}}}"


def scholarship_check(kind: str) -> str:
    checks = {
        "definition": "give the scale or context where the definition changes interpretation",
        "mechanism": "separate mechanism from correlation and name the weakest inferential step",
        "comparison": "explain why the contrast changes prediction or interpretation",
        "quantitative": "report assumptions, units, and whether model choice could change the conclusion",
        "experimental": "make the control strong enough that a negative result would be informative",
        "evaluation": "separate empirical evidence from value judgments and state a counterexample",
        "application": "state which observation would decide between the chapter model and an alternative",
    }
    return checks[kind]


def prompt_cues(question: str) -> str:
    """Extract a compact list of requirements already present in the prompt."""

    cues = [
        f"{marker}) {' '.join(body.split()).strip(' .')}"
        for marker, body in _CLAUSE_RE.findall(question)
        if " ".join(body.split()).strip(" .")
    ]
    if cues:
        return "; ".join(cues[:5])

    quantities: list[str] = []
    for match in _QUANTITY_RE.finditer(question):
        op = match.group("op") or ""
        num = match.group("num")
        unit = match.group("unit") or ""
        scale = match.group("scale") or ""
        if not (op or unit or scale or "." in num or float(num) > 10):
            continue
        quantities.append(" ".join(part for part in (op + num, unit, scale) if part).strip())
    if quantities:
        return "carry through the provided values " + ", ".join(list(dict.fromkeys(quantities))[:5])

    named_items = [item for item in _NAMED_ENTITY_RE.findall(question) if item not in _STOP_NAMED]
    if named_items:
        unique = list(dict.fromkeys(named_items))[:6]
        return "explicitly use " + ", ".join(unique)

    return "answer every requested clause, not just the opening phrase"


def common_pitfall(kind: str, question: str) -> str:
    lowered = question.lower()
    if kind == "quantitative":
        return "writing a formula without checking units, assumptions, or biological meaning"
    if "correlation" in lowered or "evidence" in lowered or kind == "evaluation":
        return "treating evidence strength and personal judgment as the same thing"
    if kind == "comparison":
        return "listing two facts without naming the decision that the contrast changes"
    if kind == "experimental":
        return "proposing a measurement without a baseline, control, or falsifying result"
    if kind == "mechanism":
        return "jumping from input to outcome without the intermediate biological step"
    return "giving a vocabulary label without an example, boundary condition, or consequence"


def answer_key(q_num: int, question: str, record: ChapterRecord) -> str:
    kind = question_kind(question)
    tier = "Recall" if q_num <= 10 else "Application" if q_num <= 20 else "Synthesis"
    focus = FOCUS_BY_STEM[record.stem]
    subject = subject_phrase(question)
    return (
        f"**Answer (Q{q_num}, {tier}).** The response on *{subject}* should use "
        f"the {evidence_target(kind, record)}. Prompt-specific details to include: "
        f"{prompt_cues(question)}. Evidence standard: {scholarship_check(kind)}. "
        f"Avoid {common_pitfall(kind, question)}. Chapter context: {focus}"
    )


def refine_question_banks(records: list[ChapterRecord], dry_run: bool) -> tuple[int, int]:
    changed_files = 0
    changed_blocks = 0
    by_question_path = {record.question_path: record for record in records}
    for path, record in sorted(by_question_path.items()):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        questions = {int(match.group(1)): match.group(2) for match in _QUESTION_LINE.finditer(text)}
        counter = 0

        def repl(
            match: re.Match[str],
            *,
            chapter_record: ChapterRecord = record,
            chapter_questions: dict[int, str] = questions,
        ) -> str:
            nonlocal counter, changed_blocks
            counter += 1
            body = match.group(2).strip()
            q_num = counter
            if not any(signature in body for signature in ANSWER_SIGNATURES):
                return match.group(0)
            new_body = answer_key(q_num, chapter_questions.get(q_num, ""), chapter_record)
            if new_body == body:
                return match.group(0)
            changed_blocks += 1
            return f"{match.group(1)}{new_body}{match.group(3)}"

        new_text = _SOLUTION_BLOCK.sub(repl, text)
        if new_text != text:
            changed_files += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed_files, changed_blocks


__all__ = [
    "ANSWER_SIGNATURES",
    "_QUESTION_LINE",
    "_SOLUTION_BLOCK",
    "answer_key",
    "common_pitfall",
    "evidence_target",
    "prompt_cues",
    "refine_question_banks",
    "scholarship_check",
]
