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

def audit_embedded_enrichment(findings: list[Finding]) -> None:
    """Ensure the current embedded enrichment pass stays present."""
    matrix = paths.PROJECT / "docs" / "embedded_enrichment_audit_matrix.md"
    if not matrix.is_file():
        findings.append(Finding("error", "missing-enrichment-audit-matrix", paths.PROJECT / "docs", 1, str(matrix)))

    chapter_titles = configured_chapter_title_by_path()
    for path in sorted(paths.MANUSCRIPT.glob("unit_*/*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        if path.name == "unit_intro.md":
            required = "## Current Evidence Thread"
            code = "missing-unit-evidence-thread"
        else:
            title = chapter_titles.get(path)
            if title is None:
                continue
            required = f"## Current Evidence and Frontier Biology: {title}"
            code = "missing-chapter-frontier-box"
        if required not in path.read_text(encoding="utf-8"):
            findings.append(Finding("error", code, path, 1, required))

    for path in sorted((paths.MANUSCRIPT / "labs").rglob("lab_*.md")):
        if "## Paper-Based Evidence Upgrade" not in path.read_text(encoding="utf-8"):
            findings.append(Finding("error", "missing-lab-evidence-upgrade", path, 1, "Paper-Based Evidence Upgrade"))

def audit_frontier_boilerplate(findings: list[Finding]) -> None:
    """Block confirmed family-level frontier boilerplate from returning."""
    for path in configured_chapter_files():
        for line_no, line in iter_prose_lines(path):
            add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=FRONTIER_BOILERPLATE_PATTERNS,
            )

def audit_templated_enrichment(findings: list[Finding]) -> None:
    chapter_frontier_boilerplate = "This chapter's frontier is not a separate topic bolted onto the end"
    unit_evidence_thread_boilerplate = "Use this unit as an evidence trail rather than a list of topics"
    companion_source_module_boilerplate = "This section is the chapter's computational reproducibility bridge"
    chapter_files = sorted(paths.MANUSCRIPT.glob("unit_*/*.md"))
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
    for path in sorted((paths.MANUSCRIPT / "labs").rglob("lab_*.md")):
        body = _paper_evidence_upgrade_body(path.read_text(encoding="utf-8"))
        if body is None:
            continue
        normalized = re.sub(r"\*\*.*?\*\*", "", body, flags=re.DOTALL)
        normalized = re.sub(r"\s+", " ", normalized).strip().lower()
        digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        grouped_paths.setdefault(digest, []).append(path)

    for _, group_paths in sorted(grouped_paths.items()):
        if len(group_paths) < 3:
            continue
        shared_count = len(group_paths) - 1
        for path in group_paths:
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

    for _, group_paths in sorted(grouped_companion_paths.items()):
        if len(group_paths) < 3:
            continue
        shared_count = len(group_paths) - 1
        for path in group_paths:
            findings.append(
                Finding(
                    "error",
                    "duplicate-companion-source-module",
                    path,
                    1,
                    f"identical to {shared_count} other chapters",
                )
            )

