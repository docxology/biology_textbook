"""Embedded enrichment engine for the biology textbook."""

from __future__ import annotations

from functools import partial
import re

from biology.enrichment.catalog import (
    COMPANION_INTRO_BY_STEM,
    COMPANION_SOURCE_BY_STEM,
    EXTRA_FRONTIER_BY_STEM,
    FIGURE_BY_STEM,
    FOCUS_BY_STEM,
    FRONTIER_BY_UNIT,
    SOURCE_PRACTICE_BY_UNIT,
    _COMPANION_NOTE_LINE_RE,
    _COMPANION_SECTION_RE,
    _INLINE_COMPANION_NOTE_RE,
)
from pathlib import Path

from biology.enrichment.models import ChapterRecord
from biology.enrichment.paths import DOCS, MANUSCRIPT, PROJECT
from biology.maintenance.text_normalize import normalize_text
from textbook_io import write_text_atomic


def companion_source_section(record: ChapterRecord) -> str:
    intro = COMPANION_INTRO_BY_STEM.get(
        record.stem,
        (
            f"**{record.title}** should leave a reproducible trail from a biological claim to\n"
            "the code, figure, diagram, or paper-based activity that can test it. Use the\n"
            "surfaces below to inspect the chapter's assumptions, rerun the relevant model,\n"
            "or compare the manuscript explanation with companion labs and figures."
        ),
    )
    body = COMPANION_SOURCE_BY_STEM.get(
        record.stem,
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/` | Connect the chapter concept to a tested model or data structure. |\n\n"
        "**Reproducibility check:** name the input, output, assumption, and evidence limit before using code as support.",
    )
    return f"""
---

## Companion Source Module: {record.title}

{intro}

{body}
"""


def _normalize_companion_heading(text: str, title: str) -> str:
    return re.sub(
        r"(?m)^#{2,3}\s+Companion Source Module(?::[^\n{]+)?(?:\s+\{[^}]*\})?\s*$",
        f"## Companion Source Module: {title}",
        text,
    )


def normalize_companion_source_modules(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        new_text = _COMPANION_SECTION_RE.sub("", text)
        new_text = _COMPANION_NOTE_LINE_RE.sub("", new_text)
        new_text = _INLINE_COMPANION_NOTE_RE.sub("", new_text)
        new_text = re.sub(r"\n---\s*\n\s*\n---\s*\n", "\n---\n", new_text)
        new_text = re.sub(r"\n---\s*\n\s*(?=---\s*\n)", "\n", new_text)
        new_text = re.sub(r"\n{4,}", "\n\n\n", new_text).rstrip()
        rebuilt = f"{new_text}\n\n{companion_source_section(record).strip()}\n"
        rebuilt_normalized = _normalize_companion_heading(rebuilt, record.title)
        existing_normalized = _normalize_companion_heading(text, record.title)
        if rebuilt_normalized == existing_normalized:
            continue
        if rebuilt != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, rebuilt)
    return changed


def frontier_section(record: ChapterRecord) -> str:
    unit_claim, unit_move = FRONTIER_BY_UNIT[record.unit_id]
    focus = FOCUS_BY_STEM[record.stem]
    source_practice = SOURCE_PRACTICE_BY_UNIT[record.unit_id]
    extra = EXTRA_FRONTIER_BY_STEM.get(record.stem, "")
    extra_block = f"\n\n{extra}" if extra else ""
    figure = FIGURE_BY_STEM.get(record.stem)
    figure_block = ""
    if figure is not None:
        figure_title, mermaid, alt, caption = figure
        figure_block = f"""
### Current Evidence Map: {figure_title}

```mermaid
{mermaid}
```
<!-- alt: {alt} -->
*{caption}*
"""
    title = f"## Current Evidence and Frontier Biology: {record.title}"
    return f"""
{title}

For **{record.title}**, frontier biology belongs inside the evidence logic of
the chapter. {unit_claim} The core reading question is this: {focus}

- **What to verify:** identify the observation, model, assay, or dataset that
  would make the claim stronger or weaker.
- **What to qualify:** state the scale, organism, cell type, environmental
  condition, or population where the claim is expected to hold.
- **What to compare:** test at least one alternative explanation, baseline, or
  null model before treating the pattern as causal.
- **What to cite:** distinguish primary evidence, review synthesis, public
  dataset, and institutional guidance; for recent or numeric claims, prefer
  the source closest to the measurement and state what has changed since it was
  published.

{unit_move}

**Source practice:** {source_practice}{extra_block}
{figure_block}
"""


_FRONTIER_SECTION_RE = re.compile(
    r"^## Current Evidence and Frontier Biology(?::[^\n]+)?\n.*?"
    r"(?=^## (?:Summary|Key Terms|Further Reading|Companion Source Module)(?::|\s|\{|$)|\Z)",
    flags=re.DOTALL | re.MULTILINE,
)


UNIT_THREAD_BY_UNIT: dict[str, str] = {
    unit: f"""
## Current Evidence Thread

Use this unit as an evidence trail rather than a list of topics. {claim} As you
move through the chapters, keep a two-column note: **claim** on the left,
**evidence that would change my confidence** on the right. By the end of the
unit, each major idea should be tied to a measurement, model, citation, or
paper-based lab decision.
"""
    for unit, (claim, _move) in FRONTIER_BY_UNIT.items()
}


def insert_before_anchor(text: str, section: str, anchors: tuple[str, ...]) -> str:
    lines = [line.strip() for line in section.strip().splitlines() if line.strip()]
    marker = lines[0] if lines else ""
    if marker and marker in text:
        return text
    positions = [text.find(anchor) for anchor in anchors if text.find(anchor) != -1]
    if not positions:
        return text.rstrip() + "\n\n" + section.strip() + "\n"
    pos = min(positions)
    return text[:pos].rstrip() + "\n\n" + section.strip() + "\n\n" + text[pos:].lstrip()


def _constant_replacement(_match: re.Match[str], *, replacement: str) -> str:
    return replacement


_FRONTIER_BOILERPLATE_MARKER = (
    "This chapter's frontier is not a separate topic bolted onto the end"
)


def _expected_frontier_heading(title: str) -> str:
    return f"## Current Evidence and Frontier Biology: {title}"


def _substantive_frontier_section(existing: str, generated: str, *, title: str) -> bool:
    """Return True when the on-disk frontier should be preserved over catalog output."""
    expected_heading = _expected_frontier_heading(title)
    first_line = existing.splitlines()[0].strip() if existing.strip() else ""
    if first_line and first_line != expected_heading:
        return False
    if existing.strip() == generated.strip():
        return True
    if _FRONTIER_BOILERPLATE_MARKER in existing:
        return False
    generic_physiology = (
        "Interpret physiological data by separating baseline variation"
    )
    if generic_physiology in existing:
        return False
    return len(existing.strip()) > len(generated.strip())


def enrich_chapters(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        section = frontier_section(record).strip() + "\n\n"
        generated = section.strip()
        if _FRONTIER_SECTION_RE.search(text):
            match = _FRONTIER_SECTION_RE.search(text)
            if match is None:
                continue
            existing = match.group(0).strip()
            if _substantive_frontier_section(existing, generated, title=record.title):
                continue
            replacer = partial(_constant_replacement, replacement=section)
            new_text = _FRONTIER_SECTION_RE.sub(replacer, text, count=1)
        else:
            new_text = insert_before_anchor(
                text,
                frontier_section(record),
                (
                    "## Summary",
                    "## Key Terms",
                    "## Further Reading and Source Notes:",
                    "## Further Reading and Source Notes",
                ),
            )
        if new_text != text:
            new_text = normalize_text(new_text).text
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def refresh_chapter_scholarship_bullets(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    marker = (
        "- **What to compare:** test at least one alternative explanation, baseline, or\n"
        "  null model before treating the pattern as causal.\n"
    )
    insertion = (
        "- **What to cite:** distinguish primary evidence, review synthesis, public\n"
        "  dataset, and institutional guidance; for recent or numeric claims, prefer\n"
        "  the source closest to the measurement and state what has changed since it was\n"
        "  published.\n"
    )
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        if "- **What to cite:**" in text or marker not in text:
            continue
        new_text = text.replace(marker, marker + insertion, 1)
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def enrich_unit_intros(dry_run: bool) -> int:
    changed = 0
    for unit_id, section in UNIT_THREAD_BY_UNIT.items():
        path = MANUSCRIPT / unit_id / "unit_intro.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = insert_before_anchor(
            text,
            section,
            ("## Computational Toolbox", "## Connections Across the Textbook", "## Chapter Roadmap"),
        )
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def lab_evidence_section(record: ChapterRecord) -> str:
    focus = FOCUS_BY_STEM[record.stem]
    return f"""
## Paper-Based Evidence Upgrade

Before answering the analysis questions, annotate the paper dataset for
**{record.title}** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: {focus} Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.
"""


def enrich_labs(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    for record in records:
        path = record.lab_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = insert_before_anchor(
            text,
            lab_evidence_section(record),
            ("## Analysis Questions", "## Additional Analysis Questions", "## Debrief and Reflection"),
        )
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


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


def question_kind(question: str) -> str:
    q = question.lower()
    starts_quant = q.startswith(("calculate ", "compute ", "estimate ", "determine the value", "find the value"))
    if starts_quant or re.search(r"\b(χ²|chi[- ]square)\b", q):
        return "quantitative"
    if re.search(r"\b(calculate|compute|estimate|set up|solve|expected)\b", q) and (
        re.search(r"\d|%|χ²", q)
        or re.search(
            r"\b(ratio|ratios|probability|frequency|frequencies|value|km|mm|mol|percent|chi[- ]square)\b",
            q,
        )
    ):
        return "quantitative"
    if re.search(r"\b(evaluate|critique|argue|assess|weigh|defend or refute)\b", q[:80]):
        return "evaluation"
    if re.search(r"\b(design|designs|experiment|test whether|propose|devise|what experiment)\b", q):
        return "experimental"
    if re.search(r"\b(compare|contrast|distinguish|differentiate|difference between)\b", q[:120]):
        return "comparison"
    if re.search(
        r"\b(probability|expected ratios?|phenotype ratios?|genotype ratios?|allele frequenc(?:y|ies)|genotype frequenc(?:y|ies)|recombination frequenc(?:y|ies)|frequency|frequencies)\b",
        q,
    ):
        return "quantitative"
    if q.startswith(("a patient ", "a researcher ", "a student ", "given ", "consider ", "suppose ")):
        return "application"
    if re.search(r"\b(why|how|explain|mechanism|cause|causes|predict)\b", q[:140]):
        return "mechanism"
    return "definition"


_QUESTION_PREAMBLE_RE = re.compile(
    r"^(?:a\s+(?:student|patient|researcher|scientist|clinician|farmer|breeder|conservationist)\s+[^.]*\.\s*"
    r"|consider(?:\s+a|\s+the)?\s+[^.]*\.\s*"
    r"|given\s+[^.]*\.\s*"
    r"|suppose\s+[^.]*\.\s*"
    r"|imagine\s+[^.]*\.\s*)",
    flags=re.IGNORECASE,
)

_QUESTION_VERB_PREFIXES = (
    "state ",
    "define ",
    "list ",
    "identify ",
    "name ",
    "rank ",
    "describe ",
    "describe the ",
    "outline ",
    "outline the ",
    "sketch ",
    "draw ",
    "write ",
    "write the ",
    "give ",
    "what is ",
    "what are ",
    "compare ",
    "contrast ",
    "distinguish ",
    "differentiate ",
    "explain ",
    "evaluate ",
    "assess ",
    "critique ",
    "calculate ",
    "compute ",
    "estimate ",
    "determine ",
    "find ",
    "design ",
    "propose ",
    "devise ",
    "suggest ",
)


def subject_phrase(question: str) -> str:
    """Return a concise, prompt-specific subject for an answer key."""

    subject = question.strip().rstrip(". ")
    subject = _QUESTION_PREAMBLE_RE.sub("", subject).strip()
    lowered = subject.lower()
    for prefix in sorted(_QUESTION_VERB_PREFIXES, key=len, reverse=True):
        if lowered.startswith(prefix):
            subject = subject[len(prefix) :].lstrip()
            break
    if "?" in subject:
        subject = subject.split("?", 1)[0]
    if ". " in subject:
        subject = subject.split(". ", 1)[0]
    if len(subject) > 150:
        boundary = max(subject.rfind(", ", 0, 145), subject.rfind("; ", 0, 145))
        if boundary < 70:
            boundary = 147
        subject = subject[:boundary].rstrip(",; ") + "..."
    return subject or "the prompt"


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

    cues: list[str] = []
    for marker, body in re.findall(r"\(([a-e])\)\s*([^;(]+(?:\([^)]*\))?)", question):
        cue = " ".join(body.split()).strip(" .")
        if cue:
            cues.append(f"{marker}) {cue}")
    if cues:
        return "; ".join(cues[:5])

    quantities: list[str] = []
    quantity_pattern = re.compile(
        r"(?<![-A-Za-z])(?P<op>[~≈<>])?\s*(?P<num>\d+(?:\.\d+)?)\s*"
        r"(?P<unit>%|km²|ha|mm|°C|yr|years?|days?|individuals?|species|M|s⁻¹)?"
        r"(?:\s*(?P<scale>million|billion|trillion))?",
        flags=re.IGNORECASE,
    )
    for match in quantity_pattern.finditer(question):
        op = match.group("op") or ""
        num = match.group("num")
        unit = match.group("unit") or ""
        scale = match.group("scale") or ""
        if not (op or unit or scale or "." in num or float(num) > 10):
            continue
        quantities.append(" ".join(part for part in (op + num, unit, scale) if part).strip())
    if quantities:
        return "carry through the provided values " + ", ".join(list(dict.fromkeys(quantities))[:5])

    stop_words = {
        "Apply",
        "Assess",
        "Calculate",
        "Compare",
        "Construct",
        "Critically",
        "Define",
        "Describe",
        "Design",
        "Determine",
        "Distinguish",
        "During",
        "Evaluate",
        "Explain",
        "For",
        "Give",
        "How",
        "Identify",
        "In",
        "List",
        "Name",
        "Predict",
        "Propose",
        "Rank",
        "State",
        "The",
        "Using",
        "What",
        "Why",
    }
    named_items = re.findall(r"\b[A-Z][A-Za-z0-9+/βαγδκλ-]{2,}\b", question)
    named_items = [item for item in named_items if item not in stop_words]
    if named_items:
        unique = list(dict.fromkeys(named_items))[:6]
        return "explicitly use " + ", ".join(unique)

    return "answer every requested clause, not just the opening phrase"


def common_pitfall(kind: str, question: str) -> str:
    q = question.lower()
    if kind == "quantitative":
        return "writing a formula without checking units, assumptions, or biological meaning"
    if "correlation" in q or "evidence" in q or kind == "evaluation":
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
        questions = {int(m.group(1)): m.group(2) for m in _QUESTION_LINE.finditer(text)}
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
            if not any(sig in body for sig in ANSWER_SIGNATURES):
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


def count_pattern(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.MULTILINE))


def write_audit_matrix(records: list[ChapterRecord], dry_run: bool) -> int:
    lines = [
        "# Embedded Enrichment Audit Matrix",
        "",
        "Generated by `scripts/enrich_embedded_textbook.py`. This matrix is a planning and review surface; canonical ordering remains `manuscript/config.yaml`.",
        "",
        "| Unit | Surface | Path | Current evidence | Embedded pass target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        chapter_text = record.chapter_path.read_text(encoding="utf-8")
        h2_count = count_pattern(chapter_text, r"^##\s+")
        citation_count = count_pattern(chapter_text, r"\\cite[tp]?\{")
        mermaid_count = count_pattern(chapter_text, r"^```mermaid")
        chapter_evidence = (
            f"{len(chapter_text):,} chars; "
            f"{h2_count} H2; "
            f"{citation_count} citations; "
            f"{mermaid_count} Mermaid"
        )
        lines.append(
            f"| {record.unit_id} | Chapter | `{record.chapter_path.relative_to(PROJECT)}` | {chapter_evidence} | Current evidence/frontier box; accessibility and citation review |"
        )
        if record.lab_path.exists():
            lab_text = record.lab_path.read_text(encoding="utf-8")
            lines.append(
                f"| {record.unit_id} | Lab | `{record.lab_path.relative_to(PROJECT)}` | {len(lab_text):,} chars | Paper-based evidence upgrade, controls, uncertainty, reproducibility |"
            )
        if record.question_path.exists():
            question_text = record.question_path.read_text(encoding="utf-8")
            solution_count = count_pattern(question_text, r"<!-- SOLUTION")
            lines.append(
                f"| {record.unit_id} | Questions | `{record.question_path.relative_to(PROJECT)}` | {solution_count} solution blocks | Prompt-specific answer keys, evidence use, scholarship checks |"
            )
    glossary_text = (MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    glossary_anchor_count = count_pattern(glossary_text, r"\{#gl:")
    lines.extend(
        [
            f"| all | Glossary | `manuscript/glossary.md` | {glossary_anchor_count} anchors | Semantic references, qualified definitions, first-use closure |",
            "| all | Appendices | `manuscript/appendices/*.md` | reference appendices | Accessibility, semantic references, no hard-coded rendered numbers |",
            "",
            "## Review Defaults",
            "",
            "- Preserve 44 chapters, 44 labs, and 44 question banks.",
            "- Add embedded improvements only; do not add new renderable chapter surfaces.",
            "- Cite or qualify recent and numeric claims.",
            "- Keep required labs paper-based; optional material extensions stay clearly optional.",
            "- Use `\\cref{...}` and generated figure/equation labels instead of hard-coded rendered numbers.",
        ]
    )
    out = DOCS / "embedded_enrichment_audit_matrix.md"
    text = "\n".join(lines) + "\n"
    old = out.read_text(encoding="utf-8") if out.exists() else ""
    if text == old:
        return 0
    if not dry_run:
        write_text_atomic(out, text)
    return 1
