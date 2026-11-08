"""Source preservation and fail-closed maintenance CLI behavior."""

from __future__ import annotations

import hashlib
from pathlib import Path

from biology.pipeline.paths import MANUSCRIPT_DIR, PROJECT_ROOT


def source_snapshot() -> dict[Path, str]:
    paths = [path for path in MANUSCRIPT_DIR.rglob("*") if path.is_file()]
    paths.append(PROJECT_ROOT / "docs" / "embedded_enrichment_audit_matrix.md")
    return {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths if path.is_file()}


def test_maintenance_previews_preserve_curated_sources() -> None:
    from biology.answer_refinement.cli import main as refine
    from biology.curriculum_sync.cli import main as curriculum
    from biology.enrichment.cli import main as enrich

    before = source_snapshot()
    for preview in (enrich, curriculum, refine):
        assert preview(["--dry-run"]) == 0
    assert source_snapshot() == before


def test_missing_figure_tree_fails_publication_check(tmp_path: Path) -> None:
    from biology.visual_contracts_cli import main

    assert main(["--figures-root", str(tmp_path / "figures"),
                 "--output", str(tmp_path / "visual_manifest.json"), "--check"]) != 0
