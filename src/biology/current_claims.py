"""Current-claim ledger validation for fast-moving textbook facts."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml


PROJECT = Path(__file__).resolve().parents[2]
DEFAULT_LEDGER = PROJECT / "manuscript" / "current_claims.yaml"

ALLOWED_SOURCE_TIERS = {
    "official_primary",
    "official_summary",
    "scholarly_primary",
    "scholarly_review",
}

REQUIRED_CLAIM_IDS = {
    "casgevy-endpoints-2026",
    "un-wpp-2024-population-peak",
    "oneill-amr-warning-scenario",
    "photosynthesis-co2-scenario-range",
    "alphafold3-hypothesis-generator",
    "iucn-red-list-2025-1",
    "who-bppl-2024-amr-triage",
    "human-pangenome-2023-reference",
}

DEFAULT_MAX_CHECKED_AGE_DAYS = 180


@dataclass(frozen=True)
class CurrentClaim:
    """One auditable fast-moving claim."""

    claim_id: str
    file: Path
    anchor_text: str
    claim_text: str
    topic: str
    source_tier: str
    evidence_date: date
    checked_as_of: date
    refresh_trigger: str
    citekey: str | None = None
    url: str | None = None


@dataclass(frozen=True)
class ClaimIssue:
    """Validation issue for a current-claim ledger row."""

    claim_id: str
    code: str
    message: str

    def format(self) -> str:
        return f"{self.code} {self.claim_id}: {self.message}"


def load_current_claims(path: Path | None = None, project_root: Path | None = None) -> tuple[CurrentClaim, ...]:
    """Load ``manuscript/current_claims.yaml`` as typed claim records."""

    root = project_root or PROJECT
    ledger = path or root / "manuscript" / "current_claims.yaml"
    raw = yaml.safe_load(ledger.read_text(encoding="utf-8")) or {}
    records = raw.get("claims", [])
    if not isinstance(records, list):
        raise ValueError("current_claims.yaml must contain a top-level 'claims' list")
    return tuple(_claim_from_mapping(record, root) for record in records)


def validate_current_claims(
    claims: tuple[CurrentClaim, ...],
    *,
    today: date | None = None,
    max_checked_age_days: int = DEFAULT_MAX_CHECKED_AGE_DAYS,
) -> list[ClaimIssue]:
    """Return all structural, source-link, and freshness issues in ``claims``."""

    today = today or date.today()
    issues: list[ClaimIssue] = []
    seen: set[str] = set()
    claim_ids = {claim.claim_id for claim in claims}

    for required_id in sorted(REQUIRED_CLAIM_IDS - claim_ids):
        issues.append(ClaimIssue(required_id, "missing-required-claim", "required high-velocity topic is absent"))

    for claim in claims:
        if claim.claim_id in seen:
            issues.append(ClaimIssue(claim.claim_id, "duplicate-claim-id", "claim_id appears more than once"))
        seen.add(claim.claim_id)
        if claim.source_tier not in ALLOWED_SOURCE_TIERS:
            issues.append(
                ClaimIssue(
                    claim.claim_id,
                    "invalid-source-tier",
                    f"source_tier must be one of {sorted(ALLOWED_SOURCE_TIERS)}",
                )
            )
        if not claim.citekey and not claim.url:
            issues.append(ClaimIssue(claim.claim_id, "missing-source", "citekey or url is required"))
        if not claim.refresh_trigger.strip():
            issues.append(ClaimIssue(claim.claim_id, "missing-refresh-trigger", "refresh_trigger is required"))
        if claim.evidence_date > today:
            issues.append(ClaimIssue(claim.claim_id, "future-evidence-date", "evidence_date is in the future"))
        if claim.checked_as_of > today:
            issues.append(ClaimIssue(claim.claim_id, "future-checked-date", "checked_as_of is in the future"))
        if (today - claim.checked_as_of).days > max_checked_age_days:
            issues.append(
                ClaimIssue(
                    claim.claim_id,
                    "stale-checked-date",
                    f"checked_as_of is older than {max_checked_age_days} days",
                )
            )
        if not claim.file.exists():
            issues.append(ClaimIssue(claim.claim_id, "missing-file", f"{claim.file} does not exist"))
            continue
        text = claim.file.read_text(encoding="utf-8")
        if claim.anchor_text not in text:
            issues.append(ClaimIssue(claim.claim_id, "missing-anchor", "anchor_text not found in source file"))
        if claim.citekey and claim.citekey not in text:
            issues.append(ClaimIssue(claim.claim_id, "missing-citekey-near-claim", "citekey not found in source file"))
    return issues


def _claim_from_mapping(record: Any, project_root: Path) -> CurrentClaim:
    if not isinstance(record, dict):
        raise ValueError("Each current claim must be a mapping")
    return CurrentClaim(
        claim_id=str(record["claim_id"]),
        file=project_root / str(record["file"]),
        anchor_text=str(record["anchor_text"]),
        claim_text=str(record["claim_text"]),
        topic=str(record["topic"]),
        source_tier=str(record["source_tier"]),
        evidence_date=date.fromisoformat(str(record["evidence_date"])),
        checked_as_of=date.fromisoformat(str(record["checked_as_of"])),
        refresh_trigger=str(record["refresh_trigger"]),
        citekey=str(record["citekey"]) if record.get("citekey") else None,
        url=str(record["url"]) if record.get("url") else None,
    )
