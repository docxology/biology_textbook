"""Tests for current-science claim ledger coverage."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import sys


PROJECT = Path(__file__).resolve().parent.parent
SRC = PROJECT / "src"
TEMPLATE_ROOT = PROJECT.parent.parent
for path in (TEMPLATE_ROOT, SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from biology.current_claims import CurrentClaim, load_current_claims, validate_current_claims  # noqa: E402


def test_current_claims_ledger_is_valid() -> None:
    claims = load_current_claims(project_root=PROJECT)
    issues = validate_current_claims(claims, today=date(2026, 5, 20))
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


def test_current_claims_cover_required_fast_moving_topics() -> None:
    claims = load_current_claims(project_root=PROJECT)
    topics = {claim.topic for claim in claims}
    assert {
        "AI biomolecular modeling",
        "antimicrobial resistance",
        "climate scenario",
        "conservation status",
        "genome-editing therapy",
        "pangenomics",
        "population projection",
    } <= topics


def test_removed_stale_current_claim_phrases_do_not_return() -> None:
    manuscript = PROJECT / "manuscript"
    text = "\n".join(path.read_text(encoding="utf-8") for path in manuscript.rglob("*.md"))
    stale_phrases = (
        "In SCD, ~94% of patients achieved transfusion independence",
        "UN median projection ~10.4 billion by 2100",
        "AMR is projected to cause 10 million deaths per year by 2050 (O'Neill Report, 2016)",
        "Atmospheric CO₂ levels are projected to reach 800-1000 ppm by 2100",
    )
    assert not [phrase for phrase in stale_phrases if phrase in text]


def _claim(source: Path, *, checked_as_of: date) -> CurrentClaim:
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
        citekey="source-key",
    )
