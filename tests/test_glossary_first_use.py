"""Tests for first-use glossary linking."""

from __future__ import annotations

from biology.maintenance.glossary_first_use import (
    GlossaryTerm,
    apply_glossary_first_use,
    bold_glossary_first_use,
)


def test_bold_glossary_first_use_links_once_and_skips_code() -> None:
    text = "The allele binds DNA.\n```python\nallele = 1\n```\nAnother allele."
    terms = [GlossaryTerm(term="Allele", slug="allele")]
    updated, count = bold_glossary_first_use(text, terms)
    assert count == 1
    assert updated.count("](#gl:allele)") == 1
    assert "allele = 1" in updated


def test_bold_glossary_first_use_is_idempotent_when_linked() -> None:
    text = "[**Allele**](#gl:allele) appears again as allele."
    terms = [GlossaryTerm(term="Allele", slug="allele")]
    updated, count = bold_glossary_first_use(text, terms)
    assert count == 0
    assert updated == text


def test_apply_glossary_first_use_writes_once(tmp_path) -> None:
    path = tmp_path / "chapter.md"
    path.write_text("The allele binds DNA.\n", encoding="utf-8")
    terms = [GlossaryTerm(term="Allele", slug="allele")]
    assert apply_glossary_first_use(path, terms) == 1
    assert "](#gl:allele)" in path.read_text(encoding="utf-8")
