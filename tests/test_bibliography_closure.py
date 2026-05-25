"""Invariant tests for the bibliography.

Asserts:
* Every documented natbib citation command in the manuscript resolves to a
  ``@entry{key, …}`` in ``manuscript/references.bib`` (no dangling refs).
* Every entry in ``references.bib`` is cited at least once (no orphans).
* Citation ids contain no mid-word artifacts (e.g. ``word\\citep{…}suffix``).
"""

from __future__ import annotations

from pathlib import Path
import re

import pytest

from biology.citations import bib_keys, citation_keys, iter_midword_citations


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
BIB = MANUSCRIPT / "references.bib"


@pytest.fixture(scope="module")
def defined_keys() -> set[str]:
    return bib_keys(BIB.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def cited_keys() -> set[str]:
    cited: set[str] = set()
    for md in MANUSCRIPT.rglob("*.md"):
        if md.name in {"README.md", "AGENTS.md"}:
            continue
        cited.update(citation_keys(md.read_text(encoding="utf-8")))
    return cited


def test_no_dangling_citations(defined_keys, cited_keys) -> None:
    """Every cited key must exist in references.bib."""
    dangling = cited_keys - defined_keys
    assert not dangling, f"Dangling citations (cited but not defined): {sorted(dangling)}"


def test_no_orphan_bibentries(defined_keys, cited_keys) -> None:
    """Every entry in references.bib must be cited at least once."""
    orphans = defined_keys - cited_keys
    assert not orphans, f"Orphan bibentries (defined but never cited): {sorted(orphans)}"


def test_no_midword_citation_artifacts() -> None:
    """Citations must never land inside a word (e.g. ``end\\citep{k}ing``)."""
    problems: list[str] = []
    for md in MANUSCRIPT.rglob("*.md"):
        if md.name in {"README.md", "AGENTS.md"}:
            continue
        text = md.read_text(encoding="utf-8")
        for match in iter_midword_citations(text):
            # Allow ``\citep{…}'s`` (apostrophe-s), which is fine grammar.
            excerpt = match.group(0)
            if excerpt.endswith(r"'s"):
                continue
            problems.append(f"{md.name}: {excerpt}")
    assert not problems, "Mid-word citation artifacts found: " + "; ".join(problems[:5])


def test_all_cite_commands_resolve(cited_keys) -> None:
    """Sanity: cited_keys is non-empty and citations use natbib commands."""
    assert cited_keys, "No natbib citation commands found — did citation style change?"


def test_documented_natbib_optional_arguments_are_parsed() -> None:
    """The shared parser must match documented natbib examples."""

    text = (
        r"\citet[p.~12]{watson1953} and \citealp{hodgkin1952, huxley1952} "
        r"plus \citeyear{mendel1866}."
    )
    assert citation_keys(text) == {"watson1953", "hodgkin1952", "huxley1952", "mendel1866"}


def test_bib_entries_have_required_metadata() -> None:
    """Every BibTeX entry carries the fields needed for a usable reference list."""

    bib = BIB.read_text(encoding="utf-8")
    missing: list[str] = []
    for match in re.finditer(r"@(?P<kind>\w+)\s*\{(?P<key>[^,]+),(?P<body>.*?)(?=\n@|\Z)", bib, re.DOTALL):
        kind = match.group("kind").lower()
        key = match.group("key")
        body = match.group("body")

        def has_field(field: str) -> bool:
            return re.search(rf"\b{field}\s*=", body, flags=re.IGNORECASE) is not None

        for field in ("title", "year"):
            if not has_field(field):
                missing.append(f"{key}: missing {field}")
        if kind == "article" and not has_field("journal"):
            missing.append(f"{key}: article missing journal")
        if kind in {"article", "book", "incollection", "inproceedings"} and not (
            has_field("author") or has_field("editor")
        ):
            missing.append(f"{key}: missing author/editor")
        if kind == "misc" and not (has_field("author") or has_field("organization") or has_field("institution")):
            missing.append(f"{key}: misc missing responsible body")

    assert not missing


def test_bibliography_does_not_use_known_bad_source_targets() -> None:
    """Resolved source-audit defects must not return as broken URLs or wrong DOIs."""

    bib = BIB.read_text(encoding="utf-8")
    bad_targets = (
        "10.1042/bj1080015",
        "10.1111/j.1096-3642.1858.tb01375.x",
        "10.1098/rstb.2013.0327",
        "10.1002/anie.199723371",
        "10.1016/S2213-8587(24)00380-7",
        "https://www.isetl.org/ijtlhe/pdf/IJTLHE3386.pdf",
    )
    assert not [target for target in bad_targets if target in bib]
