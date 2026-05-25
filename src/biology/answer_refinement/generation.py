"""Generated answer templates for question-bank refinement."""

from __future__ import annotations

import re

from biology.answer_refinement.classification import (
    _CLAUSE_RE,
    _NAMED_ENTITY_RE,
    _QUANTITY_RE,
    _STOP_NAMED,
    classify_question,
    subject_phrase,
)
from biology.answer_refinement.evidence import chapter_method, fallback_evidence, pitfall_for


def answer_clauses(q_text: str) -> str:
    clauses = [
        f"{marker}) {body.strip(' .')}"
        for marker, body in _CLAUSE_RE.findall(q_text)
        if body.strip(" .")
    ]
    if clauses:
        return " Address the requested parts explicitly: " + "; ".join(clauses[:5]) + "."
    quantities = []
    for match in _QUANTITY_RE.finditer(q_text):
        op = match.group("op") or ""
        num = match.group("num")
        unit = match.group("unit") or ""
        scale = match.group("scale") or ""
        if op or unit or scale or "." in num or float(num) > 10:
            quantities.append(" ".join(part for part in (op + num, unit, scale) if part).strip())
    if quantities:
        return " Use the stated quantitative evidence: " + ", ".join(list(dict.fromkeys(quantities))[:6]) + "."
    named_items = [item for item in _NAMED_ENTITY_RE.findall(q_text) if item not in _STOP_NAMED]
    if named_items:
        return " Include the named evidence: " + ", ".join(list(dict.fromkeys(named_items))[:6]) + "."
    return ""


def generate_answer(
    q_num: int,
    tier: str,
    q_text: str,
    chapter_ref: str,
    category: str,
    evidence: tuple[str, str] | None = None,
) -> str:
    kind = classify_question(q_text)
    subject = subject_phrase(q_text)
    evidence_1, evidence_2 = evidence or fallback_evidence(category)
    clause_text = answer_clauses(q_text)
    pitfall = pitfall_for(kind, category)
    method = chapter_method(category)
    templates = {
        "define": (
            f"The response on *{subject}* should first state the chapter's concrete mechanism: {evidence_1} "
            f"Then give one same-scale example or boundary condition using this evidence: {evidence_2}"
        ),
        "compare": (
            f"The response on *{subject}* should name the shared biological principle and the difference that changes interpretation. "
            f"The shared principle is supported by: {evidence_1} The decisive contrast or boundary condition is: {evidence_2}"
        ),
        "calculate": (
            f"The response on *{subject}* should name the model, substitute the stated values with units, and check the biological range. "
            f"Use this chapter context for the interpretation: {evidence_1} Check the result against: {evidence_2}"
        ),
        "explain": (
            f"The response on *{subject}* should give the causal chain: initiating condition, changed component, intermediate mechanism, and observable outcome. "
            f"The mechanism should be grounded in: {evidence_1} Interpret the outcome using: {evidence_2}"
        ),
        "design": (
            f"The response on *{subject}* should name the hypothesis, comparison/control, changed factor, measured outcome, replication, and falsifying result. "
            f"The mechanistic basis is: {evidence_1} The decision rule should distinguish that mechanism from the alternative implied by: {evidence_2}"
        ),
        "evaluate": (
            f"The response on *{subject}* should separate empirical evidence from the judgment and name what would change the conclusion. "
            f"Use this evidence line: {evidence_1} State this limitation or boundary condition: {evidence_2}"
        ),
        "apply": (
            f"The response on *{subject}* should identify the relevant variable, mechanism, prediction, and evidence that would decide the case. "
            f"Use this mechanism: {evidence_1} Evidence that would support or weaken the prediction is: {evidence_2}"
        ),
    }

    body = templates[kind]
    return (
        f"**Answer (Q{q_num}, {tier}).** {body}{clause_text} "
        f"Scholarship standard: {method}. {pitfall} Chapter anchor: \\cref{{{chapter_ref}}}."
    )


# Match a full SOLUTION block with its Answer body (used by engine re-exports).
_BLOCK_RE = re.compile(
    r"(<!-- SOLUTION\s*\n)"
    r"(\*\*Answer \(Q(\d+),\s*[^)]+\)\.\*\*[^\n]*(?:\n(?!SOLUTION -->)[^\n]*)*)"
    r"(\n\s*SOLUTION -->)",
    re.DOTALL,
)
