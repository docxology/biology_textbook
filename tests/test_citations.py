"""Tests for shared natbib citation parsing helpers."""

from __future__ import annotations

from pathlib import Path

from biology.citations import (
    bib_keys,
    citation_command_count,
    citation_keys,
    inject_citation_after_anchor,
    inject_orphan_citations,
    is_skippable_citation_context,
    iter_citations,
    iter_midword_citations,
    ordered_citation_keys,
    orphan_citation_insertions,
    validate_orphan_citation_insertions,
)


def test_iter_citations_parses_optional_notes_and_multiple_keys() -> None:
    text = r"\citet[p.~12]{watson1953} and \citealp{hodgkin1952, huxley1952} plus \citeyear{mendel1866}."
    citations = list(iter_citations(text))
    assert [c.command for c in citations] == ["citet", "citealp", "citeyear"]
    assert citations[0].keys == ("watson1953",)
    assert citations[1].keys == ("hodgkin1952", "huxley1952")
    assert citation_keys(text) == {"watson1953", "hodgkin1952", "huxley1952", "mendel1866"}


def test_ordered_citation_keys_preserves_first_seen_order() -> None:
    text = r"\citep{a,b} then \citep{b,c}."
    assert ordered_citation_keys(text) == ["a", "b", "c"]


def test_citation_command_count_and_bib_keys() -> None:
    text = r"\citep{one} \citet{two} \citep{one}"
    assert citation_command_count(text) == 3
    bib = "@article{one,\n  title={One}\n}\n@book{two, title={Two}}\n"
    assert bib_keys(bib) == {"one", "two"}


def test_iter_midword_citations_detects_glued_citations() -> None:
    text = r"word\citep{bad}ing is invalid but fine\citep{ok}'s suffix."
    matches = list(iter_midword_citations(text))
    assert len(matches) == 1
    assert r"\citep{bad}" in matches[0].group(0)


def test_orphan_citation_insertion_map_targets_exist() -> None:
    from biology.maintenance.models import PROJECT

    issues = validate_orphan_citation_insertions(PROJECT)
    assert not issues, issues


def test_orphan_citation_insertion_count_is_stable() -> None:
    from biology.maintenance.models import PROJECT

    assert len(orphan_citation_insertions(PROJECT)) == 32


def test_is_skippable_citation_context_skips_headings_and_fences() -> None:
    text = "# Heading with Darwin\n\n```\nDarwin\n```\n\nBody Darwin text."
    heading_pos = text.index("Darwin")
    fence_pos = text.index("Darwin", heading_pos + 1)
    body_pos = text.rindex("Darwin")
    assert is_skippable_citation_context(text, heading_pos)
    assert is_skippable_citation_context(text, fence_pos)
    assert not is_skippable_citation_context(text, body_pos)


def test_inject_citation_after_anchor_is_idempotent_on_repeat() -> None:
    text = "Mendel studied inheritance patterns in peas."
    updated, ok = inject_citation_after_anchor(text, "Mendel", "mendel1866")
    assert ok
    assert "\\citep{mendel1866}" in updated
    again, ok2 = inject_citation_after_anchor(updated, "Mendel", "mendel1866")
    assert not ok2
    assert again == updated


def test_inject_orphan_citations_dry_run_does_not_write(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript" / "unit_V"
    manuscript.mkdir(parents=True)
    target = manuscript / "mendelian_principles.md"
    original = "Mendel established particulate inheritance.\n"
    target.write_text(original, encoding="utf-8")
    report = inject_orphan_citations(tmp_path, dry_run=True, write=False)
    assert target.read_text(encoding="utf-8") == original
    assert report.total >= 1
