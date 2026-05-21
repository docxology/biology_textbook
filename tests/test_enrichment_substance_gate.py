"""Regression tests for enrichment substance gates."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast


PROJECT = Path(__file__).resolve().parent.parent
SCRIPT = PROJECT / "scripts" / "audit_textbook_quality.py"

spec = importlib.util.spec_from_file_location("audit_textbook_quality", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
sys.modules["audit_textbook_quality"] = module
assert spec.loader is not None
spec.loader.exec_module(module)


class FindingLike(Protocol):
    severity: str
    code: str
    path: Path
    message: str


class AuditModule(Protocol):
    MANUSCRIPT: Path

    def audit_templated_enrichment(self, findings: list[FindingLike]) -> None: ...


audit = cast(AuditModule, module)


def run_targeted_audits(manuscript: Path) -> list[FindingLike]:
    original_manuscript = audit.MANUSCRIPT
    try:
        audit.MANUSCRIPT = manuscript
        findings: list[FindingLike] = []
        audit.audit_templated_enrichment(findings)
        return findings
    finally:
        audit.MANUSCRIPT = original_manuscript


def test_chapter_frontier_boilerplate_is_flagged(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    chapter_path = manuscript / "unit_I" / "ch_x.md"
    chapter_path.parent.mkdir(parents=True)
    chapter_path.write_text(
        "\n".join(
            [
                "# Chapter X",
                "This chapter's frontier is not a separate topic bolted onto the end"
                "; it stays woven into the argument.",
            ]
        ),
        encoding="utf-8",
    )

    findings = run_targeted_audits(manuscript)

    assert any(
        finding.code == "templated-frontier-boilerplate"
        and finding.severity == "error"
        and finding.path == chapter_path
        for finding in findings
    )


def test_duplicate_lab_evidence_upgrade_is_flagged(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    labs_dir = manuscript / "labs" / "unit_I"
    labs_dir.mkdir(parents=True)
    shared_body = [
        "The evidence chain stays constant across these labs once the bolded title is removed.",
        "",
        "**{title}**",
        "",
        "Use the same mechanistic comparison and the same paper anchor in each case.",
    ]
    lab_paths = [
        labs_dir / "lab_a.md",
        labs_dir / "lab_b.md",
        labs_dir / "lab_c.md",
    ]
    for label, path in zip(("Title A", "Title B", "Title C"), lab_paths, strict=True):
        path.write_text(
            "\n".join(
                [
                    "# Lab",
                    "## Paper-Based Evidence Upgrade {.unnumbered}",
                    *[line.format(title=label) for line in shared_body],
                    "## Analysis Questions {.unnumbered}",
                    "1. Analyze the shared evidence.",
                ]
            ),
            encoding="utf-8",
        )

    findings = run_targeted_audits(manuscript)
    duplicate_findings = [
        finding for finding in findings if finding.code == "duplicate-lab-evidence-upgrade"
    ]

    assert len(duplicate_findings) == 3
    assert {finding.path for finding in duplicate_findings} == set(lab_paths)
    assert all(finding.severity == "error" for finding in duplicate_findings)


def test_non_duplicate_content_yields_neither(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    chapter_path = manuscript / "unit_I" / "ch_clean.md"
    labs_dir = manuscript / "labs" / "unit_I"
    chapter_path.parent.mkdir(parents=True)
    labs_dir.mkdir(parents=True)
    chapter_path.write_text(
        "\n".join(
            [
                "# Clean Chapter",
                "The frontier section ties current methods to the chapter's"
                " mechanism without relying on stock framing.",
            ]
        ),
        encoding="utf-8",
    )
    for index, body in enumerate(
        (
            "Compare membrane permeability evidence with isotope tracing from one paper.",
            "Trace a distinct ecological measurement chain using a field-observation paper.",
            "Evaluate a separate genetics result with an inheritance-focused paper.",
        ),
        start=1,
    ):
        (labs_dir / f"lab_{index}.md").write_text(
            "\n".join(
                [
                    "# Lab",
                    "## Paper-Based Evidence Upgrade {.unnumbered}",
                    body,
                    "## Analysis Questions {.unnumbered}",
                    "1. Analyze the evidence.",
                ]
            ),
            encoding="utf-8",
        )

    findings = run_targeted_audits(manuscript)

    forbidden_codes = {
        "templated-frontier-boilerplate",
        "templated-evidence-thread",
        "duplicate-lab-evidence-upgrade",
    }
    assert not any(finding.code in forbidden_codes for finding in findings)


def test_companion_source_boilerplate_is_flagged(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    chapter_path = manuscript / "unit_I" / "ch_companion.md"
    chapter_path.parent.mkdir(parents=True)
    chapter_path.write_text(
        "\n".join(
            [
                "# Chapter Companion",
                "## Companion Source Module",
                "This section is the chapter's computational reproducibility bridge.",
                "It then ties the narrative claim to a concrete code path.",
            ]
        ),
        encoding="utf-8",
    )

    findings = run_targeted_audits(manuscript)

    assert any(
        finding.code == "templated-companion-source-boilerplate"
        and finding.severity == "error"
        and finding.path == chapter_path
        for finding in findings
    )


def test_duplicate_companion_source_module_is_flagged(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    chapters_dir = manuscript / "unit_I"
    chapters_dir.mkdir(parents=True)
    shared_body = [
        "## Companion Source Module {{.unnumbered}}",
        "**{title}**",
        "",
        "Map the chapter's mechanistic claim to the same computational workflow and"
        " preserve the same evidence trail.",
        "Use the same code landmarks and the same interpretation constraints in each chapter.",
        "",
        "### Downstream Note",
        "Keep the explanation aligned with the model output.",
    ]
    duplicate_paths = [
        chapters_dir / "ch_dup_a.md",
        chapters_dir / "ch_dup_b.md",
        chapters_dir / "ch_dup_c.md",
    ]
    for label, path in zip(("Alpha Bridge", "Beta Bridge", "Gamma Bridge"), duplicate_paths, strict=True):
        path.write_text(
            "\n".join(
                [
                    f"# {label}",
                    *[line.format(title=label) for line in shared_body],
                    "## Distinct Next Section",
                    "This chapter then resumes its own argument.",
                ]
            ),
            encoding="utf-8",
        )

    distinct_path = chapters_dir / "ch_distinct.md"
    distinct_path.write_text(
        "\n".join(
            [
                "# Distinct Chapter",
                "### Companion Source Module",
                "**Distinct Bridge**",
                "",
                "Trace a different computational object and justify it with a separate"
                " experimental constraint.",
                "Name a separate model assumption and a different failure mode.",
                "## Distinct Next Section",
                "Return to the chapter-specific interpretation.",
            ]
        ),
        encoding="utf-8",
    )

    findings = run_targeted_audits(manuscript)
    duplicate_findings = [
        finding for finding in findings if finding.code == "duplicate-companion-source-module"
    ]

    assert len(duplicate_findings) == 3
    assert {finding.path for finding in duplicate_findings} == set(duplicate_paths)
    assert all(finding.severity == "error" for finding in duplicate_findings)
    assert not any(
        finding.path == distinct_path
        and finding.code in {
            "templated-companion-source-boilerplate",
            "duplicate-companion-source-module",
        }
        for finding in findings
    )
