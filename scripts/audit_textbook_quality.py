#!/usr/bin/env python3
"""Audit high-value textbook quality invariants.

This project has many focused maintenance scripts. This audit is the
publication-readiness umbrella: it reports patterns that should not drift back
into the manuscript after a content-quality pass. Use ``--check`` for a CI-style
gate; without it the script prints the same report and exits successfully.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import re

import yaml


PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "manuscript"
QUALITY_ADVISORIES = MANUSCRIPT / "quality_advisories.yaml"
ALLOWED_ADVISORY_CLASSIFICATIONS = {
    "valid_scientific_absolute",
    "needs_qualifier",
    "copyedit_artifact",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: Path
    line: int
    message: str

    def format(self) -> str:
        rel = self.path.relative_to(PROJECT)
        return f"{self.severity.upper()} {self.code} {rel}:{self.line}: {self.message}"


QUESTION_GENERIC_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("generic-answer-define", re.compile(r"Give the canonical definition of")),
    ("generic-answer-mechanism", re.compile(r"Build a mechanistic answer")),
    ("generic-answer-numeric", re.compile(r"Numerical problem on")),
    ("generic-answer-position", re.compile(r"Take a position on \*")),
    ("generic-answer-design", re.compile(r"Propose an experimental or engineering response")),
    ("generic-answer-rubric", re.compile(r"Rubric for \*")),
    ("generic-answer-players", re.compile(r"name the relevant players")),
    ("generic-answer-scale-setting", re.compile(r"scale-setting detail")),
    ("generic-answer-thin-evidence", re.compile(r"state the judgment, cite two lines of evidence")),
    ("generic-answer-thin-numeric", re.compile(r"identify the governing equation or ratio")),
    ("generic-answer-thin-design", re.compile(r"specify the manipulated variable")),
    ("generic-answer-key-prefix", re.compile(r"Answer key for \*")),
    ("generic-answer-define-precisely", re.compile(r"define the concept precisely")),
    ("generic-answer-scale", re.compile(r"place it at the correct biological scale")),
    ("generic-answer-causal-sequence", re.compile(r"trace the causal sequence")),
    ("generic-answer-equation-ratio", re.compile(r"choose the relevant equation, ratio, or probability model")),
    ("generic-answer-hypothesis-variable", re.compile(r"state the hypothesis, variable being changed")),
    ("generic-answer-judgment", re.compile(r"make a justified judgment")),
    ("generic-answer-vocab-pitfall", re.compile(r"giving a vocabulary-only answer")),
    ("generic-answer-name-term", re.compile(r"Name the term in ")),
    ("generic-answer-evidence-anchor", re.compile(r"Evidence anchor:")),
    ("generic-answer-credit-requires", re.compile(r"Credit requires an explicit mechanism")),
    ("generic-answer-prompt-linked", re.compile(r"prompt-linked evidence")),
    ("generic-answer-core-response", re.compile(r"Core response for \*")),
    ("generic-answer-expected-answer", re.compile(r"Expected answer for \*")),
    ("generic-answer-prompt-cues", re.compile(r"Prompt cues to cover:")),
    ("generic-answer-source-standard", re.compile(r"Source standard:")),
    ("generic-answer-common-pitfall", re.compile(r"Common pitfall:")),
    ("generic-answer-chapter-lens", re.compile(r"Chapter lens:")),
    ("generic-answer-governing-equation", re.compile(r"set up the governing equation")),
    ("generic-answer-defensible-judgment", re.compile(r"state a defensible judgment")),
    ("generic-answer-two-observations", re.compile(r"support it with two chapter-specific observations")),
    ("generic-answer-every-clause", re.compile(r"Answer every requested clause")),
    ("generic-answer-ground-cref", re.compile(r"Ground the answer in \\cref")),
    ("generic-answer-use-cref", re.compile(r"Use \\cref")),
    ("generic-answer-extend-cref", re.compile(r"Extend \\cref")),
    ("generic-answer-biological-players", re.compile(r"Name the biological players")),
    ("generic-answer-one-limitation", re.compile(r"name one limitation or counterexample")),
    ("generic-answer-boundary-condition", re.compile(r"boundary condition that prevents overgeneralising")),
    ("generic-answer-carry-values", re.compile(r"Carry through these values:")),
    ("generic-answer-named-items", re.compile(r"Use these named items explicitly:")),
    ("generic-answer-current-define", re.compile(r"Define \*")),
    ("generic-answer-current-compare", re.compile(r"Compare \*")),
    ("generic-answer-current-solve", re.compile(r"Solve \*")),
    ("generic-answer-current-explain", re.compile(r"Explain \*")),
    ("generic-answer-current-design", re.compile(r"Design the test for \*")),
    ("generic-answer-current-evaluate", re.compile(r"Evaluate \*")),
    ("generic-answer-current-apply", re.compile(r"Apply the chapter principle to \*")),
    ("generic-answer-current-required-clauses", re.compile(r"Required clauses:")),
    ("generic-answer-current-values", re.compile(r"Use the stated values explicitly:")),
    ("generic-answer-current-named-evidence", re.compile(r"Named evidence to include:")),
    ("generic-answer-current-first-noun", re.compile(r"Do not stop at the first noun phrase")),
    ("generic-answer-current-anchor", re.compile(r"Anchor the response to \\cref")),
    ("generic-answer-complete-response", re.compile(r"A complete response should")),
    ("generic-answer-expected-reasoning", re.compile(r"Expected reasoning:")),
    ("generic-answer-scoring-focus", re.compile(r"Scoring focus:")),
    ("generic-answer-key-label", re.compile(r"Key answer:")),
    ("generic-answer-comparison-label", re.compile(r"Comparison answer:")),
    ("generic-answer-calculation-label", re.compile(r"Calculation answer:")),
    ("generic-answer-mechanistic-label", re.compile(r"Mechanistic answer:")),
    ("generic-answer-design-label", re.compile(r"Design answer:")),
    ("generic-answer-evaluation-label", re.compile(r"Evaluation answer:")),
    ("generic-answer-application-label", re.compile(r"Application answer:")),
    ("generic-answer-chapter-evidence-label", re.compile(r"Chapter evidence:")),
    ("generic-answer-evidence-check-label", re.compile(r"Evidence check:")),
    ("generic-answer-trace-star", re.compile(r"Trace \*")),
    ("generic-answer-precise-account", re.compile(r"Give a precise account of \*")),
    ("generic-answer-write-model", re.compile(r"Write the model for \*")),
    ("generic-answer-turn-star", re.compile(r"Turn \*")),
    ("generic-answer-assess-star", re.compile(r"Assess \*")),
    ("generic-answer-use-principle", re.compile(r"Use the chapter principle with \*")),
    ("generic-answer-reference-point", re.compile(r"Reference point: \\cref")),
    ("generic-answer-v3-mechanism", re.compile(r"should first state the chapter.s concrete mechanism")),
    ("generic-answer-v3-causal-chain", re.compile(r"should give the causal chain")),
    ("generic-answer-v3-shared-principle", re.compile(r"should name the shared biological principle")),
    ("generic-answer-v3-model-substitute", re.compile(r"should name the model, substitute the stated values")),
    ("generic-answer-v3-scholarship-standard", re.compile(r"Scholarship standard:")),
    ("generic-answer-v3-pitfall", re.compile(r"Pitfall to avoid:")),
    ("generic-answer-v3-chapter-anchor", re.compile(r"Chapter anchor:")),
    (
        "generic-answer-v3-same-scale",
        re.compile(r"Then give one same-scale example or boundary condition using this evidence"),
    ),
    ("generic-answer-v3-decisive-contrast", re.compile(r"The decisive contrast or boundary condition is")),
    ("generic-answer-v3-interpret-outcome", re.compile(r"Interpret the outcome using:")),
    ("mismatched-popgen-tail", re.compile(r"propose one comparative or population-genomic test")),
    ("mismatched-clinical-tail", re.compile(r"propose one clinical intervention")),
    ("mismatched-molecular-tail", re.compile(r"propose one molecular intervention")),
)

BROKEN_CREF_RE = re.compile(r"(?<!\\)\bcref\{")
BROKEN_NAMEREF_RE = re.compile(r"(?<!\\)\bnameref\{")
BROKEN_NAMEREF_TAIL_RE = re.compile(r"(?<![A-Za-z\\])ameref\{")
COLLAPSED_UNIT_CREF_RE = re.compile(r"\\cref\{sec:unit[IVX]+[a-z]")


STALE_CLAIM_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("stale-who-2022", re.compile(r"\bWHO 2022\b")),
    ("stale-tb-burden", re.compile(r"10\.6 million new cases and 1\.3 million deaths")),
    ("stale-malaria-burden", re.compile(r"247 million cases and 619,000 deaths")),
    ("unsupported-antibiotic-void", re.compile(r"no new antibiotic classes have been approved since 2003")),
    ("overfixed-livestock-share", re.compile(r"70% of antibiotics sold in the U\.S\. are used in livestock")),
    ("overfixed-outpatient-share", re.compile(r"estimated 30% of outpatient prescriptions are unnecessary")),
    ("stale-un-population-2022", re.compile(r"10\.4 billion around 2080-2100 \(UN 2022 revision\)")),
    ("stale-iucn-2024-count", re.compile(r"44,016 classified as threatened")),
    ("stale-living-planet-2022", re.compile(r"Living Planet Report \(2022\)")),
    ("stale-living-planet-69", re.compile(r"69% average decline")),
    ("stale-food-10b-2050", re.compile(r"feeding a projected 10 billion people by 2050")),
    ("overbroad-beta-lactam", re.compile(r"all β-lactams", flags=re.IGNORECASE)),
    ("overbroad-atp-currency", re.compile(r"universal energy currency", flags=re.IGNORECASE)),
)


BANNED_REQUIRED_LAB_TERMS = re.compile(
    r"\b("
    r"beakers?|pipettes?|reagents?|Benedict'?s|Biuret|Sudan|HCl|NaOH|"
    r"hot water bath|compound microscope|dissecting microscope|glass slides?|"
    r"coverslips?|wet mounts?|cheek swabs?|agar plates?|LB agar|Mueller-Hinton|"
    r"swabbed|duckweed cultures?|pollen germination medium|"
    r"fresh flowers?|dissect(?:ion|ed|ing)|sharp knife|celery cross-sections?|"
    r"microscope magnification|staining protocol|sample preparation"
    r")\b",
    flags=re.IGNORECASE,
)


GENERIC_MERMAID_METADATA = (
    "flowchart depicting biological process or pathway",
    "network graph showing biological relationships",
    "sequence diagram showing step-by-step molecular or cellular interactions",
    "mermaid directed graph summarising a conceptual relationship described in the surrounding text",
)


GENERIC_COMPANION_SOURCE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "generic-companion-source-intro",
        re.compile(r"The computational concepts discussed in this chapter are implemented"),
    ),
    ("stale-companion-source-note", re.compile(r"Companion source note:")),
    ("stale-companion-module-line", re.compile(r"^\*Module:")),
    ("stale-companion-figure-line", re.compile(r"^\*Figure:")),
    ("stale-companion-diagram-line", re.compile(r"^\*Diagram:")),
    ("stale-companion-crossrefs-line", re.compile(r"^\*Cross-references:")),
)


STUDENT_FACING_AUTHORING_BOILERPLATE: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "student-facing-current-source-boilerplate",
        re.compile(r"Recent and numeric claims should remain tied to authoritative sources"),
    ),
)


COPYEDIT_ARTIFACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("copyedit-uppercase-most", re.compile(r"\bMOST\b")),
    ("copyedit-not-most", re.compile(r"\bNot most\b")),
    ("copyedit-most-involve", re.compile(r"\bmost involve\b")),
    ("copyedit-most-the", re.compile(r"\bmost the\b")),
    ("copyedit-most-four", re.compile(r"\bmost four\b")),
    ("copyedit-virtually-most", re.compile(r"\bvirtually most\b", flags=re.IGNORECASE)),
    ("copyedit-almost-most", re.compile(r"\balmost most\b", flags=re.IGNORECASE)),
    (
        "copyedit-quantified-of-most",
        re.compile(r"\b(?:approximately\s+|~)?\d+(?:[-–]\d+)?\s*%?\s+of most\b", flags=re.IGNORECASE),
    ),
    ("copyedit-of-most-known-recorded", re.compile(r"\bof most (?:known|recorded)\b")),
    ("copyedit-of-most-time", re.compile(r"\bof most time\b")),
    ("copyedit-most-bear", re.compile(r"\bmost bear\b")),
    ("copyedit-sum-of-most", re.compile(r"\bsum of most\b")),
    ("copyedit-space-of-most", re.compile(r"\bspace of most\b")),
    ("copyedit-set-of-most", re.compile(r"\bset of most\b")),
    ("copyedit-partition-of-most", re.compile(r"\bpartition of most\b")),
    ("copyedit-primarily-quantifier", re.compile(r"\bprimarily\s+~?\d")),
    ("copyedit-primarily-a-has", re.compile(r"\bprimarily a has\b")),
    ("copyedit-the-primarily", re.compile(r"\bthe primarily\b")),
    ("copyedit-primarily-partially", re.compile(r"\bprimarily partially\b")),
    ("copyedit-primarily-by-approx", re.compile(r"\bprimarily by ~")),
    ("copyedit-primarily-as-good", re.compile(r"\bprimarily as good as\b")),
    ("copyedit-need-primarily-open", re.compile(r"\bneed primarily open\b")),
    ("copyedit-hyphen-primarily", re.compile(r"\b[A-Za-z]+-primarily\b")),
)


HARDCODED_REF = re.compile(
    r"(?<![A-Za-z])(?:Chapter|Ch\.?|Figure|Fig\.?|Equation|Eq\.?|Section|§)\s*\d+(?:\.\d+)*",
)

HARDCODED_STRUCTURAL_REF = re.compile(
    r"\bUnits?\s+(?:0(?:\.\d+)?(?:'s)?|[IVX]+(?:\s*[–-]\s*[IVX]+)?"
    r"(?:\s*(?:,|and|or|/|\+)\s*[IVX]+)*)\b"
    r"|\bAppendix\s+[A-Z]\b"
    r"|\b(?:Figure|Fig\.)\s+FM-\d+\b"
    r"|\bChapter numbers\b"
)

FRONT_MATTER_GENERATED_MARKERS: tuple[tuple[str, str], ...] = (
    ("<!-- toc-navigation-start -->", "<!-- toc-navigation-end -->"),
    ("<!-- suggested-reading-paths-start -->", "<!-- suggested-reading-paths-end -->"),
    ("<!-- textbook-concept-map-start -->", "<!-- textbook-concept-map-end -->"),
    ("<!-- course-planning-grid-start -->", "<!-- course-planning-grid-end -->"),
)


ABSOLUTE_LANGUAGE = re.compile(
    r"\b(always|never|universal|universally|all|only|impossible|guarantees?)\b",
    flags=re.IGNORECASE,
)


BENIGN_ABSOLUTE_CONTEXTS = (
    "all requested clause",
    "all requested clauses",
    "all figures were generated",
    "all numerical",
    "all 10 units",
    "all ordered chapter files",
    "applies only to",
    "belongs only in an optional extension",
    "equipment version belongs only in an optional extension",
    "not always",
    "not all",
    "not only",
    "only about",
    "only tools needed",
    "reference only",
    "almost universally",
    "near-universal",
    "universal donor",
    "universal recipient",
    "universal genetic code",
    "universal primers",
    "universal primer",
    "ab only",
    "o only",
    "all rights reserved",
    "all-or-none",
    "almost always",
    "nearly universal",
    "*pan* = all",
    "one-size-fits-all",
)



PAPER_EVIDENCE_UPGRADE_HEADING_RE = re.compile(
    r"^## Paper-Based Evidence Upgrade(?:\s+\{[^}]*\})?\s*$",
    flags=re.MULTILINE,
)

COMPANION_SOURCE_MODULE_HEADING_RE = re.compile(
    r"^#{2,3}\s+Companion Source Module(?:\s+\{[^}]*\})?\s*$",
    flags=re.MULTILINE,
)


def manuscript_markdown_files() -> list[Path]:
    return [
        path
        for path in sorted(MANUSCRIPT.rglob("*.md"))
        if path.name not in {"AGENTS.md", "README.md"}
    ]


def _first_occurrence_line(text: str, needle: str) -> int:
    for line_no, line in enumerate(text.splitlines(), start=1):
        if needle in line:
            return line_no
    raise ValueError(f"needle not found: {needle}")


def _paper_evidence_upgrade_body(text: str) -> str | None:
    match = PAPER_EVIDENCE_UPGRADE_HEADING_RE.search(text)
    if match is None:
        return None
    body_start = match.end()
    if text[body_start:body_start + 2] == "\r\n":
        body_start += 2
    elif text[body_start:body_start + 1] in {"\r", "\n"}:
        body_start += 1
    next_heading = re.search(r"^## ", text[body_start:], flags=re.MULTILINE)
    if next_heading is None:
        return text[body_start:]
    body_end = body_start + next_heading.start()
    return text[body_start:body_end]


def _companion_source_module_body(text: str) -> str | None:
    match = COMPANION_SOURCE_MODULE_HEADING_RE.search(text)
    if match is None:
        return None
    body_start = match.end()
    if text[body_start:body_start + 2] == "\r\n":
        body_start += 2
    elif text[body_start:body_start + 1] in {"\r", "\n"}:
        body_start += 1
    next_heading = re.search(r"^#{1,3} ", text[body_start:], flags=re.MULTILINE)
    if next_heading is None:
        return text[body_start:]
    body_end = body_start + next_heading.start()
    return text[body_start:body_end]


def iter_prose_lines(path: Path) -> list[tuple[int, str]]:
    """Return non-code, non-HTML-comment lines for prose-oriented scans."""
    lines: list[tuple[int, str]] = []
    in_fence = False
    in_comment = False
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith("#"):
            continue
        if re.match(r"^>\s*\*\*(?:Ch|Appendix)\s+[A-Za-z0-9.]+", stripped):
            continue
        if "<!--" in stripped:
            in_comment = True
        if not in_comment:
            lines.append((line_no, line))
        if "-->" in stripped:
            in_comment = False
    return lines


def _generated_block_line_numbers(path: Path) -> set[int]:
    """Return line numbers owned by approved front-matter generators."""
    if path != MANUSCRIPT / "front_matter.md":
        return set()
    text = path.read_text(encoding="utf-8")
    line_starts: list[int] = []
    offset = 0
    for line in text.splitlines(keepends=True):
        line_starts.append(offset)
        offset += len(line)
    generated: set[int] = set()
    for start_marker, end_marker in FRONT_MATTER_GENERATED_MARKERS:
        start = text.find(start_marker)
        end = text.find(end_marker, start)
        if start == -1 or end == -1:
            continue
        end += len(end_marker)
        for line_no, line_start in enumerate(line_starts, start=1):
            if start <= line_start < end:
                generated.add(line_no)
    return generated


def add_line_findings(
    findings: list[Finding],
    *,
    path: Path,
    line_no: int,
    line: str,
    patterns: tuple[tuple[str, re.Pattern[str]], ...],
    severity: str = "error",
) -> None:
    for code, pattern in patterns:
        if pattern.search(line):
            findings.append(Finding(severity, code, path, line_no, line.strip()))


def audit_question_answers(findings: list[Finding]) -> None:
    for path in sorted((MANUSCRIPT / "questions").rglob("questions_*.md")):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=QUESTION_GENERIC_PATTERNS,
            )


def audit_broken_crossrefs(findings: list[Finding]) -> None:
    for path in manuscript_markdown_files():
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if (
                BROKEN_CREF_RE.search(line)
                or BROKEN_NAMEREF_RE.search(line)
                or BROKEN_NAMEREF_TAIL_RE.search(line)
                or COLLAPSED_UNIT_CREF_RE.search(line)
            ):
                findings.append(Finding("error", "broken-crossref", path, line_no, line.strip()))


def audit_stale_claims(findings: list[Finding]) -> None:
    for path in manuscript_markdown_files():
        for line_no, line in iter_prose_lines(path):
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=STALE_CLAIM_PATTERNS,
            )
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=STUDENT_FACING_AUTHORING_BOILERPLATE,
            )
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=COPYEDIT_ARTIFACT_PATTERNS,
            )


def audit_lab_defaults(findings: list[Finding]) -> None:
    for path in sorted((MANUSCRIPT / "labs").rglob("lab_*.md")):
        text = path.read_text(encoding="utf-8")
        default_text = re.split(r"## Optional (?:Material|Wet-Lab)", text, maxsplit=1)[0]
        default_text = default_text.split("## Safety and Ethics Notes", 1)[0]
        default_text = default_text.split("## Debrief and Reflection", 1)[0]
        default_text = default_text.split("## Analysis Questions", 1)[0]
        for line_no, line in enumerate(default_text.splitlines(), start=1):
            if BANNED_REQUIRED_LAB_TERMS.search(line):
                findings.append(
                    Finding("error", "required-wet-lab-language", path, line_no, line.strip())
                )


def audit_accessibility_metadata(findings: list[Finding]) -> None:
    for path in manuscript_markdown_files():
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            normalized = " ".join(line.lower().split())
            for phrase in GENERIC_MERMAID_METADATA:
                if phrase in normalized:
                    findings.append(Finding("error", "generic-mermaid-metadata", path, line_no, line.strip()))


def audit_companion_source_modules(findings: list[Finding]) -> None:
    chapter_files = [
        path
        for path in sorted(MANUSCRIPT.glob("unit_*/*.md"))
        if path.name not in {"AGENTS.md", "README.md", "unit_intro.md"}
    ]
    for path in chapter_files:
        text = path.read_text(encoding="utf-8")
        count = len(re.findall(r"^#{2,3}\s+Companion Source Module$", text, flags=re.MULTILINE))
        if count != 1:
            findings.append(
                Finding("error", "chapter-companion-source-count", path, 1, f"expected 1, found {count}")
            )
        for line_no, line in iter_prose_lines(path):
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=GENERIC_COMPANION_SOURCE_PATTERNS,
            )


def audit_references(findings: list[Finding]) -> None:
    for path in manuscript_markdown_files():
        generated_lines = _generated_block_line_numbers(path)
        for line_no, line in iter_prose_lines(path):
            if line_no in generated_lines:
                continue
            if HARDCODED_REF.search(line):
                findings.append(Finding("error", "hardcoded-rendered-reference", path, line_no, line.strip()))
            if HARDCODED_STRUCTURAL_REF.search(line):
                findings.append(
                    Finding(
                        "error",
                        "hardcoded-rendered-structural-reference",
                        path,
                        line_no,
                        line.strip(),
                    )
                )


def audit_glossary_and_citations(findings: list[Finding]) -> None:
    bib = (MANUSCRIPT / "references.bib").read_text(encoding="utf-8")
    defined = set(re.findall(r"@\w+\{([^,\s]+),", bib))
    cited: set[str] = set()
    for path in manuscript_markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\\cite[pt]?\*?\{([^}]+)\}", text):
            cited.update(key.strip() for key in match.group(1).split(",") if key.strip())
    for key in sorted(cited - defined):
        findings.append(Finding("error", "dangling-citation", MANUSCRIPT / "references.bib", 1, key))
    for key in sorted(defined - cited):
        findings.append(Finding("error", "orphan-bibentry", MANUSCRIPT / "references.bib", 1, key))

    glossary = (MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    anchors = re.findall(r"\{#(gl:[A-Za-z0-9_-]+)\}", glossary)
    duplicates = sorted({anchor for anchor in anchors if anchors.count(anchor) > 1})
    for anchor in duplicates:
        findings.append(Finding("error", "duplicate-glossary-anchor", MANUSCRIPT / "glossary.md", 1, anchor))

    anchor_set = set(anchors)
    for path in manuscript_markdown_files():
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for slug in re.findall(r"\]\(#(gl:[A-Za-z0-9_-]+)\)", line):
                if slug not in anchor_set:
                    findings.append(Finding("error", "dangling-glossary-link", path, line_no, slug))


def audit_absolute_language(findings: list[Finding]) -> None:
    """Advisory scan: broad terms can be correct, but deserve review."""
    for path in manuscript_markdown_files():
        for line_no, line in iter_prose_lines(path):
            normalized = " ".join(line.lower().split())
            if any(context in normalized for context in BENIGN_ABSOLUTE_CONTEXTS):
                continue
            if ABSOLUTE_LANGUAGE.search(line):
                findings.append(Finding("advisory", "absolute-language-review", path, line_no, line.strip()))


def quality_advisory_id(finding: Finding) -> str:
    """Return a stable identifier for an advisory finding."""
    rel = finding.path.relative_to(PROJECT).as_posix()
    digest = hashlib.sha1(finding.message.encode("utf-8")).hexdigest()[:12]
    return f"{finding.code}:{rel}:{digest}"


def _ledger_error(code: str, message: str) -> Finding:
    return Finding("error", code, QUALITY_ADVISORIES, 1, message)


def load_quality_advisory_ledger() -> tuple[dict[str, dict[str, object]], list[Finding]]:
    """Load the triage ledger for accepted quality advisories."""
    if not QUALITY_ADVISORIES.is_file():
        return {}, [_ledger_error("missing-quality-advisory-ledger", str(QUALITY_ADVISORIES))]

    raw = yaml.safe_load(QUALITY_ADVISORIES.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        return {}, [_ledger_error("invalid-quality-advisory-ledger", "top-level YAML must be a mapping")]

    entries = raw.get("absolute_language")
    if not isinstance(entries, list):
        return {}, [_ledger_error("invalid-quality-advisory-ledger", "absolute_language must be a list")]

    ledger: dict[str, dict[str, object]] = {}
    errors: list[Finding] = []
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(_ledger_error("invalid-quality-advisory-ledger", f"entry {index} must be a mapping"))
            continue
        advisory_id = entry.get("advisory_id")
        classification = entry.get("classification")
        source_path = entry.get("source_path")
        line = entry.get("line")
        excerpt = entry.get("excerpt")
        if not isinstance(advisory_id, str) or not advisory_id:
            errors.append(_ledger_error("invalid-quality-advisory-ledger", f"entry {index} missing advisory_id"))
            continue
        if advisory_id in ledger:
            errors.append(_ledger_error("duplicate-quality-advisory", advisory_id))
        if classification not in ALLOWED_ADVISORY_CLASSIFICATIONS:
            errors.append(
                _ledger_error(
                    "invalid-quality-advisory-classification",
                    f"{advisory_id} classification={classification!r}",
                )
            )
        if not isinstance(source_path, str) or not source_path.startswith("manuscript/"):
            errors.append(_ledger_error("invalid-quality-advisory-source", advisory_id))
        if not isinstance(line, int) or line < 1:
            errors.append(_ledger_error("invalid-quality-advisory-line", advisory_id))
        if not isinstance(excerpt, str) or not excerpt.strip():
            errors.append(_ledger_error("invalid-quality-advisory-excerpt", advisory_id))
        ledger[advisory_id] = entry
    return ledger, errors


def audit_quality_advisory_ledger(findings: list[Finding]) -> None:
    """Fail on untriaged or unresolved absolute-language advisories."""
    current = [finding for finding in findings if finding.code == "absolute-language-review"]
    ledger, ledger_errors = load_quality_advisory_ledger()
    findings.extend(ledger_errors)
    if ledger_errors:
        return

    current_ids = {quality_advisory_id(finding): finding for finding in current}
    for finding in current:
        advisory_id = quality_advisory_id(finding)
        entry = ledger.get(advisory_id)
        if entry is None:
            findings.append(
                Finding(
                    "error",
                    "untriaged-absolute-language",
                    finding.path,
                    finding.line,
                    f"{advisory_id} missing from {QUALITY_ADVISORIES.relative_to(PROJECT)}",
                )
            )
            continue
        if entry.get("classification") != "valid_scientific_absolute":
            findings.append(
                Finding(
                    "error",
                    "unresolved-triaged-absolute-language",
                    finding.path,
                    finding.line,
                    f"{advisory_id} remains but is classified {entry.get('classification')!r}",
                )
            )

    for advisory_id, entry in sorted(ledger.items()):
        if entry.get("classification") == "valid_scientific_absolute" and advisory_id not in current_ids:
            findings.append(
                _ledger_error("stale-valid-absolute-advisory", f"{advisory_id} no longer matches current audit output")
            )


def audit_embedded_enrichment(findings: list[Finding]) -> None:
    """Ensure the current embedded enrichment pass stays present."""
    matrix = PROJECT / "docs" / "embedded_enrichment_audit_matrix.md"
    if not matrix.is_file():
        findings.append(Finding("error", "missing-enrichment-audit-matrix", PROJECT / "docs", 1, str(matrix)))

    for path in sorted(MANUSCRIPT.glob("unit_*/*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        if path.name == "unit_intro.md":
            required = "## Current Evidence Thread"
            code = "missing-unit-evidence-thread"
        else:
            required = "## Current Evidence and Frontier Biology"
            code = "missing-chapter-frontier-box"
        if required not in path.read_text(encoding="utf-8"):
            findings.append(Finding("error", code, path, 1, required))

    for path in sorted((MANUSCRIPT / "labs").rglob("lab_*.md")):
        if "## Paper-Based Evidence Upgrade" not in path.read_text(encoding="utf-8"):
            findings.append(Finding("error", "missing-lab-evidence-upgrade", path, 1, "Paper-Based Evidence Upgrade"))


def audit_templated_enrichment(findings: list[Finding]) -> None:
    chapter_frontier_boilerplate = "This chapter's frontier is not a separate topic bolted onto the end"
    unit_evidence_thread_boilerplate = "Use this unit as an evidence trail rather than a list of topics"
    companion_source_module_boilerplate = "This section is the chapter's computational reproducibility bridge"
    chapter_files = sorted(MANUSCRIPT.glob("unit_*/*.md"))
    for path in chapter_files:
        if path.name in {"AGENTS.md", "README.md", "unit_intro.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if chapter_frontier_boilerplate in text:
            findings.append(
                Finding(
                    "error",
                    "templated-frontier-boilerplate",
                    path,
                    _first_occurrence_line(text, chapter_frontier_boilerplate),
                    "shared boilerplate frontier opening",
                )
            )

    for path in chapter_files:
        if path.name != "unit_intro.md":
            continue
        text = path.read_text(encoding="utf-8")
        if unit_evidence_thread_boilerplate in text:
            findings.append(
                Finding(
                    "error",
                    "templated-evidence-thread",
                    path,
                    _first_occurrence_line(text, unit_evidence_thread_boilerplate),
                    "shared boilerplate evidence thread opening",
                )
            )

    grouped_paths: dict[str, list[Path]] = {}
    for path in sorted((MANUSCRIPT / "labs").rglob("lab_*.md")):
        body = _paper_evidence_upgrade_body(path.read_text(encoding="utf-8"))
        if body is None:
            continue
        normalized = re.sub(r"\*\*.*?\*\*", "", body, flags=re.DOTALL)
        normalized = re.sub(r"\s+", " ", normalized).strip().lower()
        digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        grouped_paths.setdefault(digest, []).append(path)

    for _, paths in sorted(grouped_paths.items()):
        if len(paths) < 3:
            continue
        shared_count = len(paths) - 1
        for path in paths:
            findings.append(
                Finding(
                    "error",
                    "duplicate-lab-evidence-upgrade",
                    path,
                    1,
                    f"identical normalized Paper-Based Evidence Upgrade body shared with {shared_count} other labs",
                )
            )

    for path in chapter_files:
        if path.name in {"AGENTS.md", "README.md", "unit_intro.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if companion_source_module_boilerplate in text:
            findings.append(
                Finding(
                    "error",
                    "templated-companion-source-boilerplate",
                    path,
                    _first_occurrence_line(text, companion_source_module_boilerplate),
                    "shared boilerplate Companion Source Module opening",
                )
            )

    grouped_companion_paths: dict[str, list[Path]] = {}
    for path in chapter_files:
        if path.name in {"AGENTS.md", "README.md", "unit_intro.md"}:
            continue
        body = _companion_source_module_body(path.read_text(encoding="utf-8"))
        if body is None:
            continue
        normalized = re.sub(r"\*\*.*?\*\*", "", body, flags=re.DOTALL)
        normalized = re.sub(r"\s+", " ", normalized).strip().lower()
        digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        grouped_companion_paths.setdefault(digest, []).append(path)

    for _, paths in sorted(grouped_companion_paths.items()):
        if len(paths) < 3:
            continue
        shared_count = len(paths) - 1
        for path in paths:
            findings.append(
                Finding(
                    "error",
                    "duplicate-companion-source-module",
                    path,
                    1,
                    f"identical to {shared_count} other chapters",
                )
            )


def collect_findings() -> list[Finding]:
    findings: list[Finding] = []
    audit_question_answers(findings)
    audit_broken_crossrefs(findings)
    audit_stale_claims(findings)
    audit_lab_defaults(findings)
    audit_accessibility_metadata(findings)
    audit_companion_source_modules(findings)
    audit_references(findings)
    audit_glossary_and_citations(findings)
    audit_embedded_enrichment(findings)
    audit_templated_enrichment(findings)
    audit_absolute_language(findings)
    audit_quality_advisory_ledger(findings)
    return findings


def print_report(findings: list[Finding], *, max_advisories: int = 0) -> None:
    errors = [finding for finding in findings if finding.severity == "error"]
    advisories = [finding for finding in findings if finding.severity == "advisory"]
    for finding in errors:
        print(finding.format())
    for finding in advisories[:max_advisories]:
        print(finding.format())
    if len(advisories) > max_advisories:
        suppressed = len(advisories) - max_advisories
        print(
            "ADVISORY absolute-language-review ... "
            f"{suppressed} more advisory findings suppressed"
        )
    status = "PASS" if not errors else "FAIL"
    print(f"audit_textbook_quality: {status} ({len(errors)} errors, {len(advisories)} advisories)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit nonzero when blocking findings are present.")
    parser.add_argument(
        "--max-advisories",
        type=int,
        default=0,
        help="Number of advisory findings to print and enforce in --check mode.",
    )
    args = parser.parse_args(argv)

    findings = collect_findings()
    if args.check:
        advisory_count = sum(1 for finding in findings if finding.severity == "advisory")
        if advisory_count > args.max_advisories:
            findings.append(
                Finding(
                    "error",
                    "advisory-limit-exceeded",
                    QUALITY_ADVISORIES,
                    1,
                    f"{advisory_count} advisories exceeds --max-advisories={args.max_advisories}",
                )
            )
    print_report(findings, max_advisories=args.max_advisories)
    if args.check and any(finding.severity == "error" for finding in findings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
