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
    rel = finding.path.relative_to(paths.PROJECT).as_posix()
    digest = hashlib.sha1(finding.message.encode("utf-8")).hexdigest()[:12]
    return f"{finding.code}:{rel}:{digest}"

def _ledger_error(code: str, message: str) -> Finding:
    return Finding("error", code, paths.QUALITY_ADVISORIES, 1, message)

def load_quality_advisory_ledger() -> tuple[dict[str, dict[str, object]], list[Finding]]:
    """Load the triage ledger for accepted quality advisories."""
    if not paths.QUALITY_ADVISORIES.is_file():
        return {}, [_ledger_error("missing-quality-advisory-ledger", str(paths.QUALITY_ADVISORIES))]

    raw = yaml.safe_load(paths.QUALITY_ADVISORIES.read_text(encoding="utf-8")) or {}
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
                    f"{advisory_id} missing from {paths.QUALITY_ADVISORIES.relative_to(paths.PROJECT)}",
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

