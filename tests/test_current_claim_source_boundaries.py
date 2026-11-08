"""Current-claim ledgers cannot certify sources outside their selected project."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from biology.current_claims import load_current_claims, validate_current_claims


@pytest.mark.parametrize("field", ["file", "url"])
@pytest.mark.parametrize("escape", ["relative", "absolute", "symlink"])
def test_ledger_refuses_external_source_or_local_evidence(
    tmp_path: Path, field: str, escape: str
) -> None:
    root = tmp_path / "project"
    root.mkdir()
    foreign = tmp_path / "foreign.md"
    foreign.write_text("The claim anchor cites source-key.\n", encoding="utf-8")
    (root / "chapter.md").write_text("The claim anchor cites source-key.\n", encoding="utf-8")
    (root / "link.md").symlink_to(foreign)
    value = {"relative": "../foreign.md", "absolute": str(foreign), "symlink": "link.md"}[escape]
    record = _record()
    record[field] = value
    ledger = root / "claims.yaml"
    ledger.write_text(json.dumps({"claims": [record]}), encoding="utf-8")

    with pytest.raises(ValueError, match="escapes the selected project"):
        load_current_claims(path=ledger, project_root=root)


@pytest.mark.parametrize("bibliography_directory", [".", "docs/manuscript"])
def test_ledger_keeps_project_local_claim_and_evidence(tmp_path: Path, bibliography_directory: str) -> None:
    chapter = tmp_path / "chapter.md"
    chapter.write_text("The claim anchor cites source-key.\n", encoding="utf-8")
    evidence = tmp_path / "evidence.md"
    evidence.write_text("Source evidence.\n", encoding="utf-8")
    record = _record()
    record["url"] = "evidence.md"
    ledger = tmp_path / "claims.yaml"
    ledger.write_text(json.dumps({"claims": [record]}), encoding="utf-8")

    claims = load_current_claims(path=ledger, project_root=tmp_path)
    assert claims[0].file == chapter.resolve()
    assert claims[0].url == "evidence.md"
    references = tmp_path / bibliography_directory / "references.bib"
    references.parent.mkdir(parents=True, exist_ok=True)
    references.write_text("@misc{source-key, title={Local reviewed evidence}}\n", encoding="utf-8")
    issues = validate_current_claims(claims, today=date(2026, 5, 21), references_path=references)
    assert {issue.code for issue in issues} == {"missing-required-claim"}


@pytest.mark.parametrize("alias", ["file", "manuscript-directory", "docs-directory"])
def test_default_ledger_refuses_external_alias_before_yaml_parsing(tmp_path: Path, alias: str) -> None:
    root, _, target = _external_metadata_alias(tmp_path, "current_claims.yaml", alias)
    sentinel = "PRIVATE_LEDGER_PARSE_SENTINEL"
    target.write_text(f"claims: [{sentinel}\n", encoding="utf-8")

    with pytest.raises(ValueError, match="escapes|aliased") as refusal:
        load_current_claims(project_root=root)
    assert sentinel not in str(refusal.value)


@pytest.mark.parametrize("alias", ["file", "directory"])
def test_custom_ledger_refuses_external_alias_before_yaml_parsing(tmp_path: Path, alias: str) -> None:
    root = tmp_path / "project"
    root.mkdir()
    foreign = tmp_path / "external"
    foreign.mkdir()
    ledger = root / "fixtures" / "claims.yaml"
    target = foreign / "claims.yaml"
    if alias == "file":
        ledger.parent.mkdir()
        ledger.symlink_to(target)
    else:
        ledger.parent.symlink_to(foreign, target_is_directory=True)
    sentinel = "PRIVATE_CUSTOM_LEDGER_PARSE_SENTINEL"
    target.write_text(f"claims: [{sentinel}\n", encoding="utf-8")

    with pytest.raises(ValueError, match="escapes|aliased") as refusal:
        load_current_claims(path=ledger, project_root=root)
    assert sentinel not in str(refusal.value)


@pytest.mark.parametrize("alias", ["file", "manuscript-directory", "docs-directory"])
def test_bibliography_refuses_external_alias_before_parsing(tmp_path: Path, alias: str) -> None:
    _, references, target = _external_metadata_alias(tmp_path, "references.bib", alias)
    sentinel = "PRIVATE_BIBLIOGRAPHY_PARSE_SENTINEL"
    target.write_text(f"@misc{{{sentinel}, title={{One}}}}\n@misc{{{sentinel}, title={{Two}}}}\n", encoding="utf-8")

    with pytest.raises(ValueError, match="escapes|aliased") as refusal:
        validate_current_claims((), today=date(2026, 5, 21), references_path=references)
    assert sentinel not in str(refusal.value)


@pytest.mark.parametrize("bibliography_directory", [".", "docs/manuscript"])
def test_current_claim_validation_rejects_duplicate_bibliography_identity(
    tmp_path: Path, bibliography_directory: str,
) -> None:
    references = tmp_path / bibliography_directory / "references.bib"
    references.parent.mkdir(parents=True, exist_ok=True)
    references.write_text(
        "@misc{source-key, title={Approval announcement}}\n"
        "@misc{source-key, title={Prescribing information}}\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Duplicate BibTeX key: source-key"):
        validate_current_claims((), today=date(2026, 5, 21), references_path=references)


def _external_metadata_alias(tmp_path: Path, filename: str, alias: str) -> tuple[Path, Path, Path]:
    root = tmp_path / "project"
    root.mkdir()
    foreign = tmp_path / "external"
    foreign.mkdir()
    source = root / "docs" / "manuscript" / filename
    if alias == "file":
        source.parent.mkdir(parents=True)
        target = foreign / filename
        source.symlink_to(target)
    elif alias == "manuscript-directory":
        source.parent.parent.mkdir()
        source.parent.symlink_to(foreign, target_is_directory=True)
        target = foreign / filename
    else:
        (foreign / "manuscript").mkdir()
        source.parent.parent.symlink_to(foreign, target_is_directory=True)
        target = foreign / "manuscript" / filename
    return root, source, target


def _record() -> dict[str, str]:
    return {
        "claim_id": "custody-boundary",
        "file": "chapter.md",
        "anchor_text": "claim anchor",
        "claim_text": "The reviewed source belongs to the selected project.",
        "topic": "source custody",
        "source_tier": "official_primary",
        "citekey": "source-key",
        "evidence_date": "2026-05-21",
        "checked_as_of": "2026-05-21",
        "refresh_trigger": "Source changes.",
    }
