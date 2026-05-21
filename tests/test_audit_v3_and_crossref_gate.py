"""Regression tests for v3 solution signatures and broken cross-reference gates."""

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

    def audit_question_answers(self, findings: list[FindingLike]) -> None: ...

    def audit_broken_crossrefs(self, findings: list[FindingLike]) -> None: ...


audit = cast(AuditModule, module)


def run_targeted_audits(manuscript: Path) -> list[FindingLike]:
    original_manuscript = audit.MANUSCRIPT
    try:
        audit.MANUSCRIPT = manuscript
        findings: list[FindingLike] = []
        audit.audit_question_answers(findings)
        audit.audit_broken_crossrefs(findings)
        return findings
    finally:
        audit.MANUSCRIPT = original_manuscript


def test_v3_solution_signatures_are_flagged(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    questions_dir = manuscript / "questions"
    questions_dir.mkdir(parents=True)
    (questions_dir / "questions_synthetic.md").write_text(
        "\n".join(
            [
                "# Synthetic Question Bank",
                "1. Explain the mechanism.",
                "<!-- SOLUTION",
                "The answer should give the causal chain from sensing to response.",
                "Scholarship standard: use chapter-specific evidence rather than generic summary.",
                "-->",
            ]
        ),
        encoding="utf-8",
    )

    findings = run_targeted_audits(manuscript)

    assert any(
        finding.code.startswith("generic-answer-v3-")
        for finding in findings
        if finding.severity == "error"
    )


def test_broken_crossrefs_are_flagged_from_raw_lines(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    questions_dir = manuscript / "questions"
    unit_dir = manuscript / "unit_I"
    questions_dir.mkdir(parents=True)
    unit_dir.mkdir()
    (questions_dir / "questions_crossrefs.md").write_text(
        "\n".join(
            [
                "# Synthetic Question Bank",
                "1. Explain the mechanism.",
                "<!-- SOLUTION",
                "Chapter anchor: cref{sec:foo}",
                "Interpret the outcome using: \\cref{sec:unitIwaterandlife}",
                "-->",
            ]
        ),
        encoding="utf-8",
    )
    clean_path = unit_dir / "clean.md"
    clean_path.write_text(
        "This chapter stays anchored to \\cref{sec:unit_I_intro} without generic phrasing.",
        encoding="utf-8",
    )

    findings = run_targeted_audits(manuscript)
    broken = [finding for finding in findings if finding.code == "broken-crossref"]

    assert len(broken) == 2
    assert any("cref{sec:foo}" in finding.message for finding in broken)
    assert any("\\cref{sec:unitIwaterandlife}" in finding.message for finding in broken)
    assert not any(
        finding.path == clean_path
        and finding.code in {
            "broken-crossref",
            "generic-answer-v3-causal-chain",
            "generic-answer-v3-scholarship-standard",
        }
        for finding in findings
    )


def test_clean_content_avoids_v3_and_crossref_findings(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    questions_dir = manuscript / "questions"
    unit_dir = manuscript / "unit_I"
    questions_dir.mkdir(parents=True)
    unit_dir.mkdir()
    question_path = questions_dir / "questions_clean.md"
    question_path.write_text(
        "\n".join(
            [
                "# Synthetic Question Bank",
                "1. Explain how water polarity shapes emergent behavior.",
                "<!-- SOLUTION",
                "Water polarity enables hydrogen bonding, which explains cohesion and heat capacity.",
                "Ground the explanation in \\cref{sec:unit_I_intro} and the chapter's named examples.",
                "-->",
            ]
        ),
        encoding="utf-8",
    )
    unit_path = unit_dir / "clean.md"
    unit_path.write_text(
        "The clean chapter reference stays intact as \\cref{sec:unit_I_intro}.",
        encoding="utf-8",
    )

    findings = run_targeted_audits(manuscript)

    assert not any(
        finding.code.startswith("generic-answer-v3-") or finding.code == "broken-crossref"
        for finding in findings
    )
    assert not any(finding.path in {question_path, unit_path} for finding in findings)
