"""Behavioral regressions for maintenance entry points."""

from __future__ import annotations

from pathlib import Path

from biology.assessment_sync import write_or_record
from biology.maintenance.text_normalize import _alt_from_caption, _metadata_is_weak


def test_mermaid_alt_text_preserves_acronym_prefixes() -> None:
    alt = _alt_from_caption(
        "TLR4/MyD88/NF-κB pathway. LBP and CD14 deliver bacterial LPS.",
        "flowchart TD\n    A[TLR4 receptor complex] --> B[NF-κB]",
        "## Pattern Recognition Receptors",
    )
    assert "TLR4/MyD88" in alt
    assert "tLR4" not in alt


def test_mermaid_alt_text_cleans_nameref_artifacts() -> None:
    alt = _alt_from_caption(
        r"\nameref{sec:unit_I_unit_intro} concept map — Chemistry of Life.",
        "graph TD\n    A[Atoms] --> B[Macromolecules]",
        "## Chemistry of Life",
    )
    assert "amerefsec" not in alt
    assert _metadata_is_weak("Graph showing amerefsec:unit_I_unit_intro concept map")


def test_assessment_sync_dry_run_does_not_write(tmp_path: Path) -> None:
    target = tmp_path / "lab.md"
    target.write_text("original\n", encoding="utf-8")
    assert write_or_record(target, "updated\n", write=False) == [target]
    assert target.read_text(encoding="utf-8") == "original\n"
