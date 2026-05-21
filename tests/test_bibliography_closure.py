"""Invariant tests for the bibliography.

Asserts:
* Every ``\\citep{key}`` / ``\\citet{key}`` in the manuscript resolves to a
  ``@entry{key, …}`` in ``manuscript/references.bib`` (no dangling refs).
* Every entry in ``references.bib`` is cited at least once (no orphans).
* Citation ids contain no mid-word artifacts (e.g. ``word\\citep{…}suffix``).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
BIB = MANUSCRIPT / "references.bib"


_RE_BIB_KEY = re.compile(r"@\w+\{([^,\s]+),")
_RE_CITE = re.compile(r"\\cite[pt]?\*?\{([^}]+)\}")
_RE_MIDWORD = re.compile(r"[A-Za-z]\\cite[pt]?\*?\{[^}]+\}[A-Za-z]")


@pytest.fixture(scope="module")
def defined_keys() -> set[str]:
    return set(_RE_BIB_KEY.findall(BIB.read_text(encoding="utf-8")))


@pytest.fixture(scope="module")
def cited_keys() -> set[str]:
    cited: set[str] = set()
    for md in MANUSCRIPT.rglob("*.md"):
        if md.name in {"README.md", "AGENTS.md"}:
            continue
        for match in _RE_CITE.finditer(md.read_text(encoding="utf-8")):
            for key in match.group(1).split(","):
                cited.add(key.strip())
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
        for match in _RE_MIDWORD.finditer(text):
            # Allow ``\citep{…}'s`` (apostrophe-s), which is fine grammar.
            excerpt = match.group(0)
            if excerpt.endswith(r"'s"):
                continue
            problems.append(f"{md.name}: {excerpt}")
    assert not problems, "Mid-word citation artifacts found: " + "; ".join(problems[:5])


def test_all_cite_commands_resolve(cited_keys) -> None:
    """Sanity: cited_keys is non-empty and citations use natbib commands."""
    assert cited_keys, "No \\citep/\\citet commands found — did citation style change?"
