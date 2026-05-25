"""Tests for enrichment catalog YAML loader."""

from __future__ import annotations

import re

from biology.enrichment import catalog


def test_catalog_yaml_loads_required_keys() -> None:
    assert len(catalog.FRONTIER_BY_UNIT) == 11
    assert catalog.SOURCE_PRACTICE_BY_UNIT
    assert catalog.FOCUS_BY_STEM
    assert catalog.FIGURE_BY_STEM
    assert catalog.COMPANION_SOURCE_BY_STEM


def test_frontier_by_unit_values_are_two_part_tuples() -> None:
    for unit_id, parts in catalog.FRONTIER_BY_UNIT.items():
        assert unit_id.startswith("unit_")
        assert len(parts) == 2
        assert all(isinstance(part, str) and part for part in parts)


def test_companion_source_stems_are_unique() -> None:
    stems = list(catalog.COMPANION_SOURCE_BY_STEM)
    assert len(stems) == len(set(stems))


def test_companion_regex_patterns_compile() -> None:
    assert isinstance(catalog._COMPANION_SECTION_RE, re.Pattern)
    assert isinstance(catalog._COMPANION_NOTE_LINE_RE, re.Pattern)
    assert isinstance(catalog._INLINE_COMPANION_NOTE_RE, re.Pattern)


def test_critical_frontier_entry_matches_snapshot() -> None:
    unit_iv = catalog.FRONTIER_BY_UNIT["unit_IV"]
    assert "pangenome" in unit_iv[0].lower()
    assert "humanpangenome2023" in unit_iv[1]
