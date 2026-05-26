"""Shared natbib citation parsing helpers for manuscript maintenance."""

from __future__ import annotations

import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Citation:
    """One natbib citation command and its comma-separated citekeys."""

    command: str
    keys: tuple[str, ...]
    start: int
    end: int


_CITE_COMMANDS = (
    "cite",
    "citep",
    "citet",
    "citealt",
    "citealp",
    "citeauthor",
    "citeyear",
)
_CITE_RE = re.compile(
    rf"\\(?P<command>{'|'.join(_CITE_COMMANDS)})\*?"
    r"(?:\[[^\]]*\]){0,2}"
    r"\{(?P<keys>[^}]+)\}"
)
_INCOMPLETE_CITE_RE = re.compile(
    rf"\\(?:{'|'.join(_CITE_COMMANDS)})\*?"
    r"(?:\[[^\]]*\]){0,2}"
    r"\{[^}]*$"
)
_MIDWORD_CITE_RE = re.compile(
    rf"[A-Za-z]\\(?:{'|'.join(_CITE_COMMANDS)})\*?"
    r"(?:\[[^\]]*\]){0,2}"
    r"\{[^}]+\}[A-Za-z]"
)
_BIB_KEY_RE = re.compile(r"@\w+\{([^,\s]+),")


def iter_citations(text: str) -> Iterator[Citation]:
    """Yield natbib citations, including optional pre/post-note arguments."""

    for match in _CITE_RE.finditer(text):
        keys = tuple(key.strip() for key in match.group("keys").split(",") if key.strip())
        if keys:
            yield Citation(
                command=match.group("command"),
                keys=keys,
                start=match.start(),
                end=match.end(),
            )


def citation_keys(text: str) -> set[str]:
    """Return all citekeys referenced by natbib commands in ``text``."""

    return {key for citation in iter_citations(text) for key in citation.keys}


def citation_command_count(text: str) -> int:
    """Return the number of natbib citation commands in ``text``."""

    return sum(1 for _ in iter_citations(text))


def ordered_citation_keys(text: str) -> list[str]:
    """Return citekeys in first-seen order, de-duplicated."""

    seen: set[str] = set()
    keys: list[str] = []
    for citation in iter_citations(text):
        for key in citation.keys:
            if key not in seen:
                keys.append(key)
                seen.add(key)
    return keys


def strip_citations(text: str, *, strip_incomplete_tail: bool = False) -> str:
    """Remove documented natbib citation commands from prose-like text."""

    stripped = _CITE_RE.sub("", text)
    if strip_incomplete_tail:
        stripped = _INCOMPLETE_CITE_RE.sub("", stripped)
    return stripped


def bib_keys(text: str) -> set[str]:
    """Return BibTeX entry keys from a ``references.bib`` body."""

    return set(_BIB_KEY_RE.findall(text))


def iter_midword_citations(text: str) -> Iterable[re.Match[str]]:
    """Yield citations glued to letters on both sides."""

    return _MIDWORD_CITE_RE.finditer(text)


@dataclass(frozen=True)
class OrphanCitationInsertion:
    """Map one BibTeX key to a chapter anchor for ``integrate_orphan_citations``."""

    citekey: str
    target: Path
    anchor: str
    form: str = "citep"
    prefix: str = ""
    replace_with: str = ""


def orphan_citation_insertions(manuscript_root: Path) -> tuple[OrphanCitationInsertion, ...]:
    """Return the curated orphan-citation insertion map for ``manuscript_root``."""
    manuscript = manuscript_root / "manuscript"
    return (
        OrphanCitationInsertion("alon2019", manuscript / "unit_II/cell_signaling.md", "feedback loop"),
        OrphanCitationInsertion("bak1987", manuscript / "unit_0/complex_adaptive_systems.md", "self-organi"),
        OrphanCitationInsertion("beggs2003", manuscript / "unit_IX/nervous_system.md", "critical period"),
        OrphanCitationInsertion("bertalanffy1968", manuscript / "unit_0/systems_science.md", "General System"),
        OrphanCitationInsertion("bormann1967", manuscript / "unit_X/ecosystem_ecology.md", "nutrient cycling"),
        OrphanCitationInsertion(
            "connell1978",
            manuscript / "unit_X/community_interactions.md",
            "intermediate disturbance",
        ),
        OrphanCitationInsertion("darwin1858", manuscript / "unit_VI/evolution_and_selection.md", "Darwin"),
        OrphanCitationInsertion("dixon1894", manuscript / "unit_VIII/plant_structure_and_water.md", "cohesion-tension"),
        OrphanCitationInsertion("ehrlich1964", manuscript / "unit_X/community_interactions.md", "coevolution"),
        OrphanCitationInsertion(
            "fire1998",
            manuscript / "unit_IV/chromatin_and_epigenetic_mechanisms.md",
            "miRNA",
        ),
        OrphanCitationInsertion("frey1997", manuscript / "unit_IX/action_potential_synapses.md", "long-term potentiation"),
        OrphanCitationInsertion("friston2010", manuscript / "unit_0/active_inference.md", "free energy principle"),
        OrphanCitationInsertion("friston2017", manuscript / "unit_0/active_inference.md", "active inference"),
        OrphanCitationInsertion("henderson1913", manuscript / "unit_I/water_and_life.md", "tetrahedral"),
        OrphanCitationInsertion("holland1992", manuscript / "unit_0/complex_adaptive_systems.md", "John Holland"),
        OrphanCitationInsertion("jacob1961", manuscript / "unit_IV/gene_expression.md", "lac operon"),
        OrphanCitationInsertion("kauffman1993", manuscript / "unit_0/complex_adaptive_systems.md", "Stuart Kauffman"),
        OrphanCitationInsertion("levin1998", manuscript / "unit_X/ecosystem_ecology.md", "ecosystem"),
        OrphanCitationInsertion("lotka1925", manuscript / "unit_X/population_ecology.md", "Lotka"),
        OrphanCitationInsertion("margulis1967", manuscript / "unit_II/cell_theory.md", "endosymbio"),
        OrphanCitationInsertion("mendel1866", manuscript / "unit_V/mendelian_principles.md", "Mendel"),
        OrphanCitationInsertion("mitchell1961", manuscript / "unit_III/bioenergetics_and_respiration.md", "chemiosmo"),
        OrphanCitationInsertion("paine1966", manuscript / "unit_X/community_interactions.md", "keystone"),
        OrphanCitationInsertion("sherrington1906", manuscript / "unit_IX/nervous_system.md", "integrative action"),
        OrphanCitationInsertion(
            "starling1914",
            manuscript / "unit_IX/circulation_respiration_homeostasis.md",
            "Frank-Starling",
        ),
        OrphanCitationInsertion("sterling2015", manuscript / "unit_0/active_inference.md", "allosta"),
        OrphanCitationInsertion("strogatz2018", manuscript / "unit_0/systems_science.md", "nonlinear dynamics"),
        OrphanCitationInsertion("tyson2003", manuscript / "unit_II/cell_signaling.md", "bistab"),
        OrphanCitationInsertion("volterra1926", manuscript / "unit_X/population_ecology.md", "Volterra"),
        OrphanCitationInsertion("weinberg1908", manuscript / "unit_V/population_genetics.md", "Weinberg"),
        OrphanCitationInsertion("williams1966", manuscript / "unit_VI/evolution_and_selection.md", "natural selection"),
        OrphanCitationInsertion("woese1977", manuscript / "unit_VII/bacteria_archaea_viruses.md", "three domain"),
    )


def validate_orphan_citation_insertions(manuscript_root: Path) -> list[str]:
    """Return human-readable issues when insertion targets or keys are invalid."""
    issues: list[str] = []
    bib = bib_keys((manuscript_root / "manuscript" / "references.bib").read_text(encoding="utf-8"))
    for insertion in orphan_citation_insertions(manuscript_root):
        if not insertion.target.exists():
            issues.append(f"missing target for {insertion.citekey}: {insertion.target}")
        if insertion.citekey not in bib:
            issues.append(f"unknown citekey in insertion map: {insertion.citekey}")
    return issues


__all__ = [
    "Citation",
    "OrphanCitationInsertion",
    "bib_keys",
    "citation_command_count",
    "citation_keys",
    "iter_citations",
    "iter_midword_citations",
    "ordered_citation_keys",
    "orphan_citation_insertions",
    "strip_citations",
    "validate_orphan_citation_insertions",
]
