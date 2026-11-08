"""Reviewed manuscript content remains author-owned during maintenance."""
from pathlib import Path

import pytest

from biology.enrichment.companion import normalize_companion_source_modules
from biology.enrichment.engine import enrich_chapters
from biology.enrichment.models import ChapterRecord
from biology.maintenance.chapter_shells import repair_record


def record_at(path: Path) -> ChapterRecord:
    return ChapterRecord("unit_IV", "Genetics", str(path), "Epigenetic Inheritance and Disease")


@pytest.mark.parametrize("body", ["A concise author-reviewed causal control.", "Detailed author evidence. " * 400])
def test_frontier_enrichment_preserves_authored_sections(tmp_path: Path, body: str) -> None:
    path = tmp_path / "epigenetic_inheritance_and_disease.md"
    original = "# Chapter\n\n## Current Evidence and Frontier Biology: Epigenetic Inheritance and Disease\n\n" + body + "\n\n## Summary\n\nKeep the surrounding source.\n"
    path.write_text(original, encoding="utf-8")
    assert enrich_chapters([record_at(path)], dry_run=False) == 0
    assert path.read_text(encoding="utf-8") == original


def test_shell_repair_preserves_reviewed_frontier(tmp_path: Path) -> None:
    path = tmp_path / "epigenetic_inheritance_and_disease.md"
    frontier = "## Current Evidence and Frontier Biology: Epigenetic Inheritance and Disease\n\nMaternal F0 exposure also exposes F1 and its F2 germline; F3 is the first unexposed generation."
    path.write_text("# Chapter\n\n" + frontier + "\n\n## Summary\n\nAuthored summary.\n", encoding="utf-8")
    record = record_at(path)
    repair_record(record)
    repaired = path.read_text(encoding="utf-8")
    assert frontier in repaired
    assert "Authored summary." in repaired
    assert not repair_record(record)
    assert path.read_text(encoding="utf-8") == repaired


def test_companion_maintenance_preserves_authored_sources_and_anchors(tmp_path: Path) -> None:
    path = tmp_path / "epigenetic_inheritance_and_disease.md"
    original = "# Chapter\n\n## Companion Source Module: Reviewed sources {#sec:my-sources}\n\nA laboratory-specific provenance note.\n\n: Verified source trail. {#tbl:reviewed-trail}\n| Source | Scope |\n| --- | --- |\n| primary.csv | Recorded observations, not a simulation |\n"
    path.write_text(original, encoding="utf-8")
    assert normalize_companion_source_modules([record_at(path)], dry_run=False) == 0
    assert path.read_text(encoding="utf-8") == original
