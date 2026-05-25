"""Quality audit helpers — extracted from engine.py."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

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
    _companion_source_module_body,
    _first_occurrence_line,
    _generated_block_line_numbers,
    _paper_evidence_upgrade_body,
)
from biology.quality.patterns import (
    ABSOLUTE_LANGUAGE,
    ALLOWED_ADVISORY_CLASSIFICATIONS,
    BANNED_REQUIRED_LAB_TERMS,
    BENIGN_ABSOLUTE_CONTEXTS,
    BROKEN_CREF_RE,
    BROKEN_NAMEREF_RE,
    BROKEN_NAMEREF_TAIL_RE,
    COLLAPSED_UNIT_CREF_RE,
    COMPANION_SOURCE_MODULE_HEADING_RE,
    CONCEPT_CHECK_RE,
    COPYEDIT_ARTIFACT_PATTERNS,
    DOLLAR_TAG_LABEL_RE,
    EXPECTED_CONFIGURED_SURFACE_COUNTS,
    FIGURE_METADATA_ARTIFACT_PATTERNS,
    FRONTIER_BOILERPLATE_PATTERNS,
    FRONT_MATTER_GENERATED_MARKERS,
    GENERIC_COMPANION_SOURCE_PATTERNS,
    GENERIC_MERMAID_METADATA,
    HARDCODED_REF,
    HARDCODED_STRUCTURAL_REF,
    HEADING_ARTIFACT_PATTERNS,
    INLINE_CIRC_PRIME_RE,
    LATEX_EQUATION_TAG_RE,
    OPENING_VIGNETTE_RE,
    PAPER_EVIDENCE_UPGRADE_HEADING_RE,
    QUESTION_GENERIC_PATTERNS,
    RAW_LATEX_RENDERED_REF,
    STALE_CLAIM_PATTERNS,
    STUDENT_FACING_AUTHORING_BOILERPLATE,
    SUMMARY_HEADING_RE,
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

def audit_references(findings: list[Finding]) -> None:
    for path in manuscript_markdown_files():
        generated_lines = _generated_block_line_numbers(path)
        for line_no, line in iter_prose_lines(path):
            if line_no in generated_lines:
                continue
            if HARDCODED_REF.search(line):
                findings.append(Finding("error", "hardcoded-rendered-reference", path, line_no, line.strip()))
            if RAW_LATEX_RENDERED_REF.search(line):
                findings.append(Finding("error", "raw-latex-rendered-reference", path, line_no, line.strip()))
            if DOLLAR_TAG_LABEL_RE.search(line):
                findings.append(Finding("error", "dollar-tag-label-equation", path, line_no, line.strip()))
            if LATEX_EQUATION_TAG_RE.search(line):
                findings.append(Finding("error", "hardcoded-equation-tag", path, line_no, line.strip()))
            if INLINE_CIRC_PRIME_RE.search(line):
                findings.append(Finding("error", "unsafe-inline-circ-prime", path, line_no, line.strip()))
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
    bib = (paths.MANUSCRIPT / "references.bib").read_text(encoding="utf-8")
    defined = set(re.findall(r"@\w+\{([^,\s]+),", bib))
    cited: set[str] = set()
    for path in manuscript_markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\\cite[pt]?\*?\{([^}]+)\}", text):
            cited.update(key.strip() for key in match.group(1).split(",") if key.strip())
    for key in sorted(cited - defined):
        findings.append(Finding("error", "dangling-citation", paths.MANUSCRIPT / "references.bib", 1, key))
    for key in sorted(defined - cited):
        findings.append(Finding("error", "orphan-bibentry", paths.MANUSCRIPT / "references.bib", 1, key))

    glossary = (paths.MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    anchors = re.findall(r"\{#(gl:[A-Za-z0-9_-]+)\}", glossary)
    duplicates = sorted({anchor for anchor in anchors if anchors.count(anchor) > 1})
    for anchor in duplicates:
        findings.append(Finding("error", "duplicate-glossary-anchor", paths.MANUSCRIPT / "glossary.md", 1, anchor))

    anchor_set = set(anchors)
    for path in manuscript_markdown_files():
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for slug in re.findall(r"\]\(#(gl:[A-Za-z0-9_-]+)\)", line):
                if slug not in anchor_set:
                    findings.append(Finding("error", "dangling-glossary-link", path, line_no, slug))

