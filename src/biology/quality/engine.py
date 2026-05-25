"""Textbook quality audit engine."""

from __future__ import annotations

from biology.maintenance.manuscript_walker import (
    configured_chapter_files,
    configured_chapter_title_by_path,
    configured_manuscript_surfaces,
    iter_markdown_headings,
    iter_prose_lines,
    manuscript_markdown_files,
)
from biology.quality.audits.advisories import (
    audit_absolute_language,
    audit_quality_advisory_ledger,
    load_quality_advisory_ledger,
    quality_advisory_id,
)
from biology.quality.audits.content import (
    audit_accessibility_metadata,
    audit_companion_source_modules,
    audit_core_chapter_structure,
    audit_heading_quality,
    audit_lab_defaults,
    audit_question_answers,
    audit_source_section_titles,
    audit_stale_claims,
)
from biology.quality.audits.enrichment import (
    audit_embedded_enrichment,
    audit_frontier_boilerplate,
    audit_templated_enrichment,
)
from biology.quality.audits.helpers import add_line_findings, _generated_block_line_numbers
from biology.quality.audits.references import (
    audit_broken_crossrefs,
    audit_glossary_and_citations,
    audit_references,
)
from biology.quality.audits.surfaces import audit_configured_surfaces
from biology.quality.models import Finding

__all__ = [
    "Finding",
    "add_line_findings",
    "audit_absolute_language",
    "audit_accessibility_metadata",
    "audit_broken_crossrefs",
    "audit_companion_source_modules",
    "audit_configured_surfaces",
    "audit_core_chapter_structure",
    "audit_embedded_enrichment",
    "audit_frontier_boilerplate",
    "audit_glossary_and_citations",
    "audit_heading_quality",
    "audit_lab_defaults",
    "audit_quality_advisory_ledger",
    "audit_question_answers",
    "audit_references",
    "audit_source_section_titles",
    "audit_stale_claims",
    "audit_templated_enrichment",
    "collect_findings",
    "configured_chapter_files",
    "configured_chapter_title_by_path",
    "configured_manuscript_surfaces",
    "iter_markdown_headings",
    "iter_prose_lines",
    "load_quality_advisory_ledger",
    "manuscript_markdown_files",
    "print_report",
    "quality_advisory_id",
    "_generated_block_line_numbers",
]


def collect_findings() -> list[Finding]:
    findings: list[Finding] = []
    audit_configured_surfaces(findings)
    audit_question_answers(findings)
    audit_broken_crossrefs(findings)
    audit_stale_claims(findings)
    audit_lab_defaults(findings)
    audit_accessibility_metadata(findings)
    audit_heading_quality(findings)
    audit_source_section_titles(findings)
    audit_companion_source_modules(findings)
    audit_core_chapter_structure(findings)
    audit_references(findings)
    audit_glossary_and_citations(findings)
    audit_embedded_enrichment(findings)
    audit_frontier_boilerplate(findings)
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
