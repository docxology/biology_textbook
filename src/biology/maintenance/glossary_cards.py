"""Parse glossary entries from ``manuscript/glossary.md``."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

GLOSSARY_TERM_LINE_RE = re.compile(
    r"^\[\*\*(?P<term>[^*]+?)\*\*\]"
    r"(?P<anchor>\{#gl:[^}]+\})"
    r"(?P<body>.*)$",
)
GLOSSARY_CARD_LINE_RE = re.compile(
    r"^\[\*\*(?P<term>.+?)\*\*\]\{#gl:(?P<slug>[^}]+)\}"
    r"(?:\s+\[[^\]]+\])?\s+—\s+(?P<definition>.+)$"
)
_TRAILING_CREF_RE = re.compile(r"\s*→\s*\\cref\{[^}]+\}\s*$")


@dataclass(frozen=True)
class GlossaryCardEntry:
    """One glossary term suitable for study-card export."""

    term: str
    slug: str
    definition: str


def parse_glossary_cards(path: Path) -> list[GlossaryCardEntry]:
    """Parse glossary markdown into study-card rows."""
    entries: list[GlossaryCardEntry] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = GLOSSARY_CARD_LINE_RE.match(line.rstrip("\n"))
        if not match:
            continue
        term = match.group("term").strip()
        slug = match.group("slug").strip()
        definition = _TRAILING_CREF_RE.sub("", match.group("definition").strip())
        entries.append(GlossaryCardEntry(term=term, slug=slug, definition=definition))
    return entries


def write_glossary_cards(
    entries: list[GlossaryCardEntry],
    output: Path,
    *,
    card_format: str = "anki",
) -> None:
    """Write glossary cards as Anki TSV or Quizlet CSV."""
    import csv

    output.parent.mkdir(parents=True, exist_ok=True)
    if card_format == "anki":
        with output.open("w", newline="", encoding="utf-8") as handle:
            tsv_writer = csv.writer(handle, delimiter="\t")
            for entry in entries:
                tsv_writer.writerow([entry.term, entry.definition])
        return
    with output.open("w", newline="", encoding="utf-8") as handle:
        dict_writer = csv.DictWriter(handle, fieldnames=["Term", "Definition"])
        dict_writer.writeheader()
        for entry in entries:
            dict_writer.writerow({"Term": entry.term, "Definition": entry.definition})


__all__ = [
    "GLOSSARY_CARD_LINE_RE",
    "GLOSSARY_TERM_LINE_RE",
    "GlossaryCardEntry",
    "parse_glossary_cards",
    "write_glossary_cards",
]
