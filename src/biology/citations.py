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
    from biology.pipeline.orphan_citations import load_orphan_citation_insertions

    return load_orphan_citation_insertions(manuscript_root=manuscript_root / "docs" / "manuscript")


def validate_orphan_citation_insertions(manuscript_root: Path) -> list[str]:
    """Return human-readable issues when insertion targets or keys are invalid."""
    issues: list[str] = []
    bib = bib_keys((manuscript_root / "docs" / "manuscript" / "references.bib").read_text(encoding="utf-8"))
    for insertion in orphan_citation_insertions(manuscript_root):
        if not insertion.target.exists():
            issues.append(f"missing target for {insertion.citekey}: {insertion.target}")
        if insertion.citekey not in bib:
            issues.append(f"unknown citekey in insertion map: {insertion.citekey}")
    return issues


@dataclass(frozen=True)
class OrphanCitationIntegrationReport:
    """Summary from ``inject_orphan_citations``."""

    inserted: int
    skipped_already_cited: int
    skipped_no_anchor: int
    total: int


def is_skippable_citation_context(text: str, pos: int) -> bool:
    """Return True when ``pos`` falls inside headings, fences, or LaTeX macro args."""
    line_start = text.rfind("\n", 0, pos) + 1
    line_end = text.find("\n", pos)
    if line_end == -1:
        line_end = len(text)
    line = text[line_start:line_end]
    stripped = line.lstrip()
    if stripped.startswith("#"):
        return True
    if stripped.startswith("\\label") or stripped.startswith("\\cref") or stripped.startswith("\\Cref"):
        return True
    before = text[:pos]
    if before.count("```") % 2 == 1:
        return True
    line_up_to_pos = text[line_start:pos]
    depth = 0
    index = len(line_up_to_pos) - 1
    while index >= 0:
        char = line_up_to_pos[index]
        if char == "}":
            depth += 1
        elif char == "{":
            if depth == 0:
                brace_index = index - 1
                while brace_index >= 0 and (line_up_to_pos[brace_index].isalpha() or line_up_to_pos[brace_index] == "*"):
                    brace_index -= 1
                if brace_index >= 0 and line_up_to_pos[brace_index] == "\\":
                    return True
                break
            depth -= 1
        index -= 1
    return False


def inject_citation_after_anchor(text: str, anchor: str, citekey: str) -> tuple[str, bool]:
    """Find first safe occurrence of ``anchor`` and inject ``\\citep{key}``."""
    pattern = re.compile(re.escape(anchor) + r"\w*", re.IGNORECASE)
    for match in pattern.finditer(text):
        if is_skippable_citation_context(text, match.start()):
            continue
        end = match.end()
        tail = text[end : end + len(citekey) + 12]
        if f"\\citep{{{citekey}}}" in tail:
            continue
        return text[:end] + f" \\citep{{{citekey}}}" + text[end:], True
    return text, False


def inject_orphan_citations(
    manuscript_root: Path,
    *,
    dry_run: bool = False,
    write: bool = True,
) -> OrphanCitationIntegrationReport:
    """Weave orphan BibTeX entries into manuscript prose using the curated map."""
    from textbook_io import write_text_atomic

    insertions = orphan_citation_insertions(manuscript_root)
    inserted = 0
    skipped_already_cited = 0
    skipped_no_anchor = 0

    for insertion in insertions:
        if not insertion.target.exists():
            continue
        text = insertion.target.read_text(encoding="utf-8")
        if insertion.citekey in citation_keys(text):
            skipped_already_cited += 1
            continue
        new_text, ok = inject_citation_after_anchor(text, insertion.anchor, insertion.citekey)
        if not ok:
            skipped_no_anchor += 1
            continue
        if write and not dry_run:
            write_text_atomic(insertion.target, new_text)
        inserted += 1

    return OrphanCitationIntegrationReport(
        inserted=inserted,
        skipped_already_cited=skipped_already_cited,
        skipped_no_anchor=skipped_no_anchor,
        total=len(insertions),
    )


__all__ = [
    "Citation",
    "OrphanCitationInsertion",
    "OrphanCitationIntegrationReport",
    "bib_keys",
    "inject_citation_after_anchor",
    "inject_orphan_citations",
    "is_skippable_citation_context",
    "citation_command_count",
    "citation_keys",
    "iter_citations",
    "iter_midword_citations",
    "ordered_citation_keys",
    "orphan_citation_insertions",
    "strip_citations",
    "validate_orphan_citation_insertions",
]
