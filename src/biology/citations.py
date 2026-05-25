"""Shared natbib citation parsing helpers for manuscript maintenance."""

from __future__ import annotations

import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass


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
