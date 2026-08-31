"""Tests for glossary card parsing."""

from __future__ import annotations

from pathlib import Path

from biology.maintenance.glossary_cards import parse_glossary_cards

PROJECT = Path(__file__).resolve().parent.parent


def test_parse_glossary_cards_matches_live_glossary() -> None:
    entries = parse_glossary_cards(PROJECT / "docs" / "manuscript" / "glossary.md")
    assert len(entries) > 100
    assert entries[0].term == "Abiotic"
    assert entries[0].slug == "abiotic"
    assert "\\cref" not in entries[0].definition


def test_write_glossary_cards_anki(tmp_path) -> None:
    from biology.maintenance.glossary_cards import GlossaryCardEntry, write_glossary_cards

    entries = [GlossaryCardEntry(term="Allele", slug="allele", definition="Variant form.")]
    output = tmp_path / "cards.tsv"
    write_glossary_cards(entries, output, card_format="anki")
    assert "Allele\tVariant form." in output.read_text(encoding="utf-8")
