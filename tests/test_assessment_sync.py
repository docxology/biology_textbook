"""Tests for ``biology.assessment_sync``."""

from __future__ import annotations

from pathlib import Path

from biology.assessment_sync import (
    assessment_comment,
    lab_alignment_block,
    lab_alignment_insert_index,
    sync_all_assessment_metadata,
    sync_lab_alignment,
    sync_question_bank,
    write_or_record,
)


def test_assessment_comment_tiers() -> None:
    lo = ("lo_a", "lo_b")
    assert "Remember" in assessment_comment(1, lo)
    assert "Create" in assessment_comment(30, lo)
    assert "LO=lo_b" in assessment_comment(2, lo)


def test_sync_question_bank_inserts_assess_comments(tmp_path: Path) -> None:
    bank = tmp_path / "questions_demo.md"
    bank.write_text(
        "1. First?\n\n<!-- SOLUTION\nAnswer\nSOLUTION -->\n\n2. Second?\n",
        encoding="utf-8",
    )
    updated = sync_question_bank(bank, ("lo_one", "lo_two"))
    assert "<!-- assess:" in updated
    assert updated.count("<!-- assess:") == 2
    assert "<!-- SOLUTION" in updated


def test_sync_lab_alignment_inserts_block(tmp_path: Path) -> None:
    lab = tmp_path / "lab_demo.md"
    lab.write_text(
        "# Lab\n\n## Learning Objectives\n\n- one\n\n## Procedure\n\nstep\n",
        encoding="utf-8",
    )
    updated = sync_lab_alignment(lab, "Demo Chapter", ("lo1", "lo2", "lo3", "lo4"))
    assert "<!-- lab-alignment-start -->" in updated
    assert "Demo Chapter" in updated


def test_lab_alignment_insert_index_falls_back_without_objectives() -> None:
    assert lab_alignment_insert_index(["# Lab", "Body"]) == 2


def test_lab_alignment_block_lists_outcomes() -> None:
    block = lab_alignment_block("Photosynthesis", ("lo1", "lo2", "lo3", "lo4"))
    assert "Photosynthesis" in block
    assert "Rubric dimensions" in block


def test_write_or_record_respects_write_flag(tmp_path: Path) -> None:
    target = tmp_path / "file.md"
    target.write_text("old\n", encoding="utf-8")
    assert write_or_record(target, "new\n", write=False) == [target]
    assert target.read_text(encoding="utf-8") == "old\n"
    write_or_record(target, "new\n", write=True)
    assert target.read_text(encoding="utf-8") == "new\n"
    assert write_or_record(target, "new\n", write=True) == []


def test_sync_all_assessment_metadata_dry_run() -> None:
    from biology.maintenance.models import PROJECT

    changed, code = sync_all_assessment_metadata(PROJECT, dry_run=True)
    assert code == 0
    assert isinstance(changed, list)
