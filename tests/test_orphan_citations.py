"""Tests for orphan citation YAML loader."""

from __future__ import annotations

from biology.pipeline.orphan_citations import load_orphan_citation_insertions


def test_load_orphan_citation_insertions_matches_catalog_size() -> None:
    insertions = load_orphan_citation_insertions()
    assert len(insertions) == 32
    assert insertions[0].citekey == "alon2019"
