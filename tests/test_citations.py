"""Tests for shared natbib citation parsing helpers."""

from __future__ import annotations

from biology.citations import (
    bib_keys,
    citation_command_count,
    citation_keys,
    iter_citations,
    iter_midword_citations,
    ordered_citation_keys,
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
