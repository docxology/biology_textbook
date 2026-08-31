"""Bold and link glossary terms on first use in chapter prose."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from biology.maintenance.glossary_cards import GLOSSARY_CARD_LINE_RE
from biology.maintenance.manuscript_spans import (
    GLOSSARY_FIRST_USE_SPAN_OPTIONS,
    in_protected,
    protected_spans,
)
from biology.maintenance.models import PROJECT

GLOSSARY = PROJECT / "docs" / "manuscript" / "glossary.md"


@dataclass(frozen=True)
class GlossaryTerm:
    """Canonical glossary display term and anchor slug."""

    term: str
    slug: str


def load_glossary_terms(glossary_path: Path = GLOSSARY) -> list[GlossaryTerm]:
    """Parse glossary lines into terms sorted longest-first."""
    terms: list[GlossaryTerm] = []
    for line in glossary_path.read_text(encoding="utf-8").splitlines():
        match = GLOSSARY_CARD_LINE_RE.match(line.rstrip("\n"))
        if not match:
            continue
        terms.append(GlossaryTerm(term=match.group("term").strip(), slug=match.group("slug").strip()))
    return sorted(terms, key=lambda item: -len(item.term))


def build_term_pattern(term: str) -> re.Pattern[str]:
    """Case-insensitive word-boundary pattern with optional plural suffix."""
    escaped = re.escape(term)
    return re.compile(rf"(?<![A-Za-z0-9_])({escaped})(s?)(?![A-Za-z0-9_])", re.IGNORECASE)


def bold_glossary_first_use(text: str, terms: list[GlossaryTerm]) -> tuple[str, int]:
    """Replace the first safe occurrence of each term with a bold glossary link."""
    replacements = 0
    for term in terms:
        pattern = build_term_pattern(term.term)
        spans = protected_spans(text, options=GLOSSARY_FIRST_USE_SPAN_OPTIONS)
        if f"](#gl:{term.slug})" in text:
            continue
        for match in pattern.finditer(text):
            if in_protected(match.start(), spans):
                continue
            matched = match.group(1)
            display = term.term
            if matched and matched[0].islower() and display[0].isupper():
                display = display[0].lower() + display[1:]
            suffix = match.group(2) or ""
            replacement = f"[**{display}**](#gl:{term.slug}){suffix}"
            text = text[: match.start()] + replacement + text[match.end():]
            replacements += 1
            break
    return text, replacements


def apply_glossary_first_use(
    path: Path,
    terms: list[GlossaryTerm],
    *,
    write: bool = True,
) -> int:
    """Apply first-use glossary linking to one chapter file."""
    text = path.read_text(encoding="utf-8")
    new_text, count = bold_glossary_first_use(text, terms)
    if count and write:
        from textbook_io import write_text_atomic

        write_text_atomic(path, new_text)
    return count


__all__ = [
    "GlossaryTerm",
    "apply_glossary_first_use",
    "bold_glossary_first_use",
    "build_term_pattern",
    "load_glossary_terms",
]
