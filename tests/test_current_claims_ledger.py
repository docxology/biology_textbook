"""Tests for current-science claim ledger coverage."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import sys


PROJECT = Path(__file__).resolve().parent.parent
SRC = PROJECT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from textbook_paths import discover_template_root  # noqa: E402

TEMPLATE_ROOT = discover_template_root(PROJECT)
for path in (TEMPLATE_ROOT, SRC):
    if path is None:
        continue
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from biology.current_claims import (  # noqa: E402
    CurrentClaim,
    load_current_claims,
    scan_stale_manuscript_phrases,
    validate_current_claims,
)


def test_current_claims_ledger_is_valid() -> None:
    claims = load_current_claims(project_root=PROJECT)
    issues = validate_current_claims(
        claims,
        today=date.today(),
        references_path=PROJECT / "docs" / "manuscript" / "references.bib",
    )
    assert not [issue.format() for issue in issues]


def test_current_claims_checked_as_of_stale_policy_fails(tmp_path: Path) -> None:
    source = tmp_path / "chapter.md"
    source.write_text("The claim anchor cites source-key.", encoding="utf-8")
    claim = _claim(source, checked_as_of=date(2026, 1, 1))

    issues = validate_current_claims((claim,), today=date(2026, 7, 1))

    assert any(issue.code == "stale-checked-date" for issue in issues)


def test_current_claims_checked_as_of_policy_allows_boundary(tmp_path: Path) -> None:
    source = tmp_path / "chapter.md"
    source.write_text("The claim anchor cites source-key.", encoding="utf-8")
    claim = _claim(source, checked_as_of=date(2026, 1, 2))

    issues = validate_current_claims((claim,), today=date(2026, 7, 1))

    assert not [issue for issue in issues if issue.code == "stale-checked-date"]


def test_current_claims_require_citekey_near_anchor(tmp_path: Path) -> None:
    source = tmp_path / "chapter.md"
    source.write_text(
        "The claim anchor has no local citation.\n\nA later paragraph cites source-key.",
        encoding="utf-8",
    )
    claim = _claim(source, checked_as_of=date(2026, 1, 2))

    issues = validate_current_claims((claim,), today=date(2026, 5, 21))

    assert any(issue.code == "missing-citekey-near-claim" for issue in issues)

    source.write_text("The claim anchor cites source-key.\n\nA later paragraph continues.", encoding="utf-8")
    issues = validate_current_claims((claim,), today=date(2026, 5, 21))
    assert not [issue for issue in issues if issue.code == "missing-citekey-near-claim"]


def test_current_claims_require_citekey_to_resolve_when_bibliography_is_checked(tmp_path: Path) -> None:
    source = tmp_path / "chapter.md"
    source.write_text("The claim anchor cites missing-key.", encoding="utf-8")
    references = tmp_path / "references.bib"
    references.write_text(
        "@article{source-key,\n"
        "  author = {Example, A.},\n"
        "  title = {Example},\n"
        "  journal = {Journal},\n"
        "  year = {2026}\n"
        "}\n",
        encoding="utf-8",
    )
    claim = _claim(source, checked_as_of=date(2026, 1, 2), citekey="missing-key")

    issues = validate_current_claims((claim,), today=date(2026, 5, 21), references_path=references)

    assert any(issue.code == "missing-bibliography-entry" for issue in issues)


def test_current_claims_require_local_source_urls_to_exist(tmp_path: Path) -> None:
    source = tmp_path / "docs" / "manuscript" / "chapter.md"
    source.parent.mkdir(parents=True)
    source.write_text("The claim anchor cites source-key.", encoding="utf-8")
    references = tmp_path / "docs" / "manuscript" / "references.bib"
    references.write_text(
        "@article{source-key,\n"
        "  author = {Example, A.},\n"
        "  title = {Example},\n"
        "  journal = {Journal},\n"
        "  year = {2026}\n"
        "}\n",
        encoding="utf-8",
    )
    claim = _claim(source, checked_as_of=date(2026, 1, 2), url="docs/manuscript/missing.md")

    issues = validate_current_claims((claim,), today=date(2026, 5, 21), references_path=references)

    assert any(issue.code == "missing-local-source" for issue in issues)


def test_current_claims_cover_required_fast_moving_topics() -> None:
    claims = load_current_claims(project_root=PROJECT)
    topics = {claim.topic for claim in claims}
    assert {
        "AI biomolecular modeling",
        "antimicrobial resistance",
        "brain cell atlases",
        "climate scenario",
        "conservation status",
        "enzyme databases",
        "gene therapy",
        "genome-editing therapy",
        "microbial taxonomy",
        "molecular biology databases",
        "pangenomics",
        "plant pangenomics",
        "population projection",
        "RNA databases",
    } <= topics


def test_removed_stale_current_claim_phrases_do_not_return() -> None:
    assert scan_stale_manuscript_phrases(PROJECT / "docs" / "manuscript", project_root=PROJECT) == []


def test_current_claim_sources_do_not_use_known_bad_targets() -> None:
    text = (PROJECT / "docs" / "manuscript" / "current_claims.yaml").read_text(encoding="utf-8")
    bad_targets = (
        "blood.2024027657",
        "9789240114708",
        "global-malaria-program/reports/world-malaria-report-2025",
        "S2213-8587(24)00380-7",
        "github.com/docxology/biology_textbook/blob/main/manuscript/glossary.md",
    )
    assert not [target for target in bad_targets if target in text]


def _claim(
    source: Path,
    *,
    checked_as_of: date,
    citekey: str = "source-key",
    url: str | None = None,
) -> CurrentClaim:
    return CurrentClaim(
        claim_id="example-current-claim",
        file=source,
        anchor_text="claim anchor",
        claim_text="Example current claim.",
        topic="example",
        source_tier="official_primary",
        evidence_date=date(2026, 1, 1),
        checked_as_of=checked_as_of,
        refresh_trigger="Source update.",
        citekey=citekey,
        url=url,
    )
