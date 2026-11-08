"""Scientific review is source-bound; copying a valid ID cannot authorize other prose."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from biology.maintenance import manuscript_walker
from biology.quality import paths
from biology.quality.audits.advisories import (
    audit_absolute_language,
    audit_quality_advisory_ledger,
    quality_advisory_id,
)
from biology.quality.models import Finding


@pytest.fixture
def advisory_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path]:
    manuscript = tmp_path / "docs/manuscript"
    source = manuscript / "unit_test/model.md"
    source.parent.mkdir(parents=True)
    source.write_text("# Finite model\n\nAlways apply transition T in this stipulated four-state simulation.\n")
    ledger = manuscript / "quality_advisories.yaml"
    monkeypatch.setattr(manuscript_walker, "MANUSCRIPT", manuscript)
    monkeypatch.setattr(paths, "PROJECT", tmp_path)
    monkeypatch.setattr(paths, "QUALITY_ADVISORIES", ledger)
    return source, ledger


def candidate_entries() -> list[dict[str, object]]:
    candidates: list[Finding] = []
    audit_absolute_language(candidates)
    return [
        {
            "advisory_id": quality_advisory_id(finding),
            "source_path": finding.path.relative_to(paths.PROJECT).as_posix(),
            "line": finding.line, "excerpt": finding.message,
            "classification": "valid_scientific_absolute",
            "rationale": "The instruction is restricted to the explicitly stipulated finite simulation, not a universal empirical claim.",
        }
        for finding in candidates
    ]


def test_valid_review_remains_explicitly_reviewed_not_outstanding(advisory_tree: tuple[Path, Path]) -> None:
    _source, ledger = advisory_tree
    ledger.write_text(json.dumps({"absolute_language": candidate_entries()}))
    findings: list[Finding] = []
    audit_absolute_language(findings)
    audit_quality_advisory_ledger(findings)
    assert [(finding.code, finding.severity) for finding in findings] == [("absolute-language-review", "reviewed")]


@pytest.mark.parametrize("mutation", ["missing-rationale", "wrong-path", "wrong-excerpt", "wrong-line", "noninteger-line", "unresolved", "duplicate", "changed-source", "moved-source", "forged-id", "untriaged"])
def test_invalid_review_cannot_promote_a_candidate(advisory_tree: tuple[Path, Path], mutation: str) -> None:
    source, ledger = advisory_tree
    entry, = candidate_entries()
    entries = [entry]
    if mutation == "missing-rationale":
        entry.pop("rationale")
    elif mutation == "wrong-path":
        entry["source_path"] = "docs/manuscript/another.md"
    elif mutation == "wrong-excerpt":
        entry["excerpt"] = "A different scientific claim."
    elif mutation == "wrong-line":
        entry["line"] = 50
    elif mutation == "noninteger-line":
        source.write_text("Always apply transition T in this stipulated four-state simulation.\n")
        entry["line"] = True
    elif mutation == "unresolved":
        entry["classification"] = "needs_qualifier"
    elif mutation == "duplicate":
        entries.append(dict(entry))
    elif mutation == "changed-source":
        source.write_text("# Changed source\n\nApply transition T.\n")
    elif mutation == "moved-source":
        source.write_text("\n" + source.read_text(encoding="utf-8"), encoding="utf-8")
    elif mutation == "forged-id":
        entry["advisory_id"] = str(entry["advisory_id"]) + "-forged"
    elif mutation == "untriaged":
        entries = []
    ledger.write_text(json.dumps({"absolute_language": entries}))
    findings: list[Finding] = []
    audit_absolute_language(findings)
    audit_quality_advisory_ledger(findings)
    assert any(finding.severity == "error" for finding in findings)
    assert not any(finding.severity == "reviewed" for finding in findings)


@pytest.mark.parametrize("reviewed_lines", [(3,), (5,), (3, 5)])
def test_identical_claims_require_independent_occurrence_reviews(
    advisory_tree: tuple[Path, Path], reviewed_lines: tuple[int, ...],
) -> None:
    source, ledger = advisory_tree
    claim = "Always apply transition T in this stipulated four-state simulation."
    source.write_text(f"# Finite model\n\n{claim}\n\n{claim}\n", encoding="utf-8")
    entries = candidate_entries()
    assert [entry["line"] for entry in entries] == [3, 5]
    assert len({entry["advisory_id"] for entry in entries}) == 2
    ledger.write_text(json.dumps({
        "absolute_language": [entry for entry in entries if entry["line"] in reviewed_lines],
    }), encoding="utf-8")
    findings: list[Finding] = []
    audit_absolute_language(findings)
    audit_quality_advisory_ledger(findings)
    candidates = [finding for finding in findings if finding.code == "absolute-language-review"]
    assert [(finding.line, finding.severity) for finding in candidates] == [
        (line, "reviewed" if line in reviewed_lines else "advisory") for line in (3, 5)
    ]
    assert [(finding.code, finding.line) for finding in findings if finding.severity == "error"] == [
        ("untriaged-absolute-language", line) for line in (3, 5) if line not in reviewed_lines
    ]


def test_duplicate_review_for_one_repeated_occurrence_blocks_all_promotions(
    advisory_tree: tuple[Path, Path],
) -> None:
    source, ledger = advisory_tree
    claim = "Always apply transition T in this stipulated four-state simulation."
    source.write_text(f"# Finite model\n\n{claim}\n\n{claim}\n", encoding="utf-8")
    entries = candidate_entries()
    ledger.write_text(json.dumps({"absolute_language": [*entries, dict(entries[0])]}), encoding="utf-8")
    findings: list[Finding] = []
    audit_absolute_language(findings)
    audit_quality_advisory_ledger(findings)
    assert any(finding.code == "duplicate-quality-advisory" for finding in findings)
    assert not any(finding.severity == "reviewed" for finding in findings)
