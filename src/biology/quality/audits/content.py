"""Quality audit helpers — extracted from engine.py."""

from __future__ import annotations

import re


from biology.maintenance.manuscript_walker import (
    configured_chapter_files,
    configured_chapter_title_by_path,
    configured_manuscript_surfaces,
    iter_markdown_headings,
    iter_prose_lines,
    manuscript_markdown_files,
)
from biology.quality import paths
from biology.quality.models import Finding
from biology.quality.audits.helpers import (
    add_line_findings,
    _generated_block_line_numbers,
)
from biology.quality.patterns import (
    BANNED_REQUIRED_LAB_TERMS,
    CONCEPT_CHECK_RE,
    COPYEDIT_ARTIFACT_PATTERNS,
    FIGURE_METADATA_ARTIFACT_PATTERNS,
    GENERIC_COMPANION_SOURCE_PATTERNS,
    GENERIC_MERMAID_METADATA,
    HEADING_ARTIFACT_PATTERNS,
    OPENING_VIGNETTE_RE,
    QUESTION_GENERIC_PATTERNS,
    STALE_CLAIM_PATTERNS,
    STUDENT_FACING_AUTHORING_BOILERPLATE,
    SUMMARY_HEADING_RE,
)

SOURCE_SECTION_TITLES = (
    "Current Evidence and Frontier Biology",
    "Further Reading and Source Notes",
    "Companion Source Module",
)
BARE_SOURCE_SECTION_HEADING_RE = re.compile(
    r"^## (?:Current Evidence and Frontier Biology|Further Reading and Source Notes|Companion Source Module)$",
    flags=re.MULTILINE,
)

def audit_question_answers(findings: list[Finding]) -> None:
    for path in sorted((paths.MANUSCRIPT / "questions").rglob("questions_*.md")):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=QUESTION_GENERIC_PATTERNS,
            )

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
    for path in sorted((paths.MANUSCRIPT / "labs").rglob("lab_*.md")):
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
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=FIGURE_METADATA_ARTIFACT_PATTERNS,
            )

def audit_heading_quality(findings: list[Finding]) -> None:
    for surface in configured_manuscript_surfaces():
        path = surface.path
        if not path.exists():
            continue
        generated_lines = _generated_block_line_numbers(path)
        for line_no, line in iter_markdown_headings(path):
            if line_no in generated_lines:
                continue
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=HEADING_ARTIFACT_PATTERNS,
            )

def audit_source_section_titles(findings: list[Finding]) -> None:
    """Require chapter-specific source-section headings in configured chapters."""
    for path, title in configured_chapter_title_by_path().items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in BARE_SOURCE_SECTION_HEADING_RE.finditer(text):
            findings.append(
                Finding(
                    "error",
                    "bare-source-section-heading",
                    path,
                    text[: match.start()].count("\n") + 1,
                    match.group(0),
                )
            )
        for section_title in SOURCE_SECTION_TITLES:
            expected = f"## {section_title}: {title}"
            if re.search(rf"^{re.escape(expected)}$", text, flags=re.MULTILINE):
                continue
            findings.append(
                Finding(
                    "error",
                    "missing-specialized-source-heading",
                    path,
                    1,
                    expected,
                )
            )

def audit_companion_source_modules(findings: list[Finding]) -> None:
    for path, title in sorted(configured_chapter_title_by_path().items()):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        expected = f"## Companion Source Module: {title}"
        count = len(re.findall(rf"^{re.escape(expected)}$", text, flags=re.MULTILINE))
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

def audit_core_chapter_structure(findings: list[Finding]) -> None:
    """Ensure every config-registered core chapter keeps the standard pedagogy shell."""
    for path in configured_chapter_files():
        if not path.is_file():
            findings.append(Finding("error", "missing-configured-chapter", path, 1, str(path)))
            continue
        text = path.read_text(encoding="utf-8")
        required = (
            ("missing-opening-vignette", OPENING_VIGNETTE_RE, "Opening Vignette"),
            ("missing-summary-section", SUMMARY_HEADING_RE, "## Summary"),
            ("missing-concept-check", CONCEPT_CHECK_RE, "Concept Check"),
        )
        for code, pattern, label in required:
            if not pattern.search(text):
                findings.append(Finding("error", code, path, 1, f"missing {label}"))

