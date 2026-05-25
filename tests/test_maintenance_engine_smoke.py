"""Smoke tests for extracted maintenance engines (dry-run paths)."""

from __future__ import annotations


def test_enrichment_dry_run_exits_zero() -> None:
    from biology.enrichment.cli import main

    assert main(["--dry-run"]) == 0


def test_enrichment_dry_run_reports_no_chapter_mutations(capsys) -> None:
    from biology.enrichment.cli import main

    assert main(["--dry-run"]) == 0
    output = capsys.readouterr().out
    assert "chapters=0" in output
    assert "companion_modules=0" in output


def test_curriculum_sync_dry_run_exits_zero() -> None:
    from biology.curriculum_sync.cli import main

    assert main(["--dry-run"]) == 0


def test_refine_answers_dry_run_exits_zero() -> None:
    from biology.answer_refinement.cli import main

    assert main(["--dry-run"]) == 0


def test_quality_audit_check_exits_zero() -> None:
    from biology.quality.cli import main

    assert main(["--check", "--max-advisories", "0"]) == 0


def test_visual_contracts_check_exits_zero(tmp_path) -> None:
    from biology.visual_contracts_cli import main

    assert main([
        "--figures-root",
        str(tmp_path / "figures"),
        "--output",
        str(tmp_path / "visual_manifest.json"),
        "--check",
    ]) == 0


def test_visual_contracts_build_manifest_non_empty() -> None:
    from biology.visual_contracts import build_manifest

    records = build_manifest()
    assert len(records) > 50
