#!/usr/bin/env python3
"""Audit high-value textbook quality invariants.

Thin CLI wrapper around :mod:`biology.quality`.
"""

from __future__ import annotations

from _bootstrap import ensure_project_paths

ensure_project_paths()

from biology.quality import cli, engine, models, paths, patterns
from biology.quality.cli import main

Finding = models.Finding
ManuscriptSurface = models.ManuscriptSurface
PROJECT = paths.PROJECT
MANUSCRIPT = paths.MANUSCRIPT
QUALITY_ADVISORIES = paths.QUALITY_ADVISORIES
ALLOWED_ADVISORY_CLASSIFICATIONS = patterns.ALLOWED_ADVISORY_CLASSIFICATIONS
EXPECTED_CONFIGURED_SURFACE_COUNTS = patterns.EXPECTED_CONFIGURED_SURFACE_COUNTS
QUESTION_GENERIC_PATTERNS = patterns.QUESTION_GENERIC_PATTERNS
COPYEDIT_ARTIFACT_PATTERNS = patterns.COPYEDIT_ARTIFACT_PATTERNS
FIGURE_METADATA_ARTIFACT_PATTERNS = patterns.FIGURE_METADATA_ARTIFACT_PATTERNS
HEADING_ARTIFACT_PATTERNS = patterns.HEADING_ARTIFACT_PATTERNS
FRONTIER_BOILERPLATE_PATTERNS = patterns.FRONTIER_BOILERPLATE_PATTERNS
GENERIC_COMPANION_SOURCE_PATTERNS = patterns.GENERIC_COMPANION_SOURCE_PATTERNS
HARDCODED_STRUCTURAL_REF = patterns.HARDCODED_STRUCTURAL_REF
HARDCODED_REF = patterns.HARDCODED_REF
RAW_LATEX_RENDERED_REF = patterns.RAW_LATEX_RENDERED_REF
DOLLAR_TAG_LABEL_RE = patterns.DOLLAR_TAG_LABEL_RE
LATEX_EQUATION_TAG_RE = patterns.LATEX_EQUATION_TAG_RE
INLINE_CIRC_PRIME_RE = patterns.INLINE_CIRC_PRIME_RE
OPENING_VIGNETTE_RE = patterns.OPENING_VIGNETTE_RE
SUMMARY_HEADING_RE = patterns.SUMMARY_HEADING_RE
CONCEPT_CHECK_RE = patterns.CONCEPT_CHECK_RE
BROKEN_CREF_RE = patterns.BROKEN_CREF_RE
BROKEN_NAMEREF_RE = patterns.BROKEN_NAMEREF_RE
collect_findings = engine.collect_findings
print_report = engine.print_report
manuscript_markdown_files = engine.manuscript_markdown_files
configured_manuscript_surfaces = engine.configured_manuscript_surfaces
configured_chapter_files = engine.configured_chapter_files
audit_configured_surfaces = engine.audit_configured_surfaces
audit_core_chapter_structure = engine.audit_core_chapter_structure
audit_quality_advisory_ledger = engine.audit_quality_advisory_ledger
audit_templated_enrichment = engine.audit_templated_enrichment
audit_question_answers = engine.audit_question_answers
audit_broken_crossrefs = engine.audit_broken_crossrefs
load_quality_advisory_ledger = engine.load_quality_advisory_ledger
quality_advisory_id = engine.quality_advisory_id
add_line_findings = engine.add_line_findings
iter_markdown_headings = engine.iter_markdown_headings
iter_prose_lines = engine.iter_prose_lines
_generated_block_line_numbers = engine._generated_block_line_numbers

__all__ = [
    "ALLOWED_ADVISORY_CLASSIFICATIONS",
    "BROKEN_CREF_RE",
    "BROKEN_NAMEREF_RE",
    "CONCEPT_CHECK_RE",
    "COPYEDIT_ARTIFACT_PATTERNS",
    "DOLLAR_TAG_LABEL_RE",
    "EXPECTED_CONFIGURED_SURFACE_COUNTS",
    "FIGURE_METADATA_ARTIFACT_PATTERNS",
    "Finding",
    "FRONTIER_BOILERPLATE_PATTERNS",
    "GENERIC_COMPANION_SOURCE_PATTERNS",
    "HARDCODED_REF",
    "HARDCODED_STRUCTURAL_REF",
    "HEADING_ARTIFACT_PATTERNS",
    "INLINE_CIRC_PRIME_RE",
    "LATEX_EQUATION_TAG_RE",
    "MANUSCRIPT",
    "ManuscriptSurface",
    "OPENING_VIGNETTE_RE",
    "PROJECT",
    "QUALITY_ADVISORIES",
    "QUESTION_GENERIC_PATTERNS",
    "RAW_LATEX_RENDERED_REF",
    "SUMMARY_HEADING_RE",
    "_generated_block_line_numbers",
    "add_line_findings",
    "audit_broken_crossrefs",
    "audit_configured_surfaces",
    "audit_core_chapter_structure",
    "audit_quality_advisory_ledger",
    "audit_question_answers",
    "audit_templated_enrichment",
    "cli",
    "collect_findings",
    "configured_chapter_files",
    "configured_manuscript_surfaces",
    "iter_markdown_headings",
    "iter_prose_lines",
    "load_quality_advisory_ledger",
    "main",
    "manuscript_markdown_files",
    "print_report",
    "quality_advisory_id",
]

if __name__ == "__main__":
    raise SystemExit(main())
