"""Tests for ``biology.maintenance.further_reading``."""

from __future__ import annotations

from pathlib import Path

from biology.maintenance.further_reading import (
    BIB,
    BibEntry,
    collect_keys,
    inject,
    parse_bib,
    pick_keys,
    render_section,
    validate_supplement,
)


def test_bib_entry_pretty_renders_journal_article() -> None:
    entry = BibEntry(
        key="ex2026",
        entry_type="article",
        author="Example, Ada and Other, Ben",
        year="2026",
        title="A discovery.",
        journal="Journal of Biology",
        volume="42",
    )
    rendered = entry.pretty()
    assert "Example & Other (2026)." in rendered
    assert "*Journal of Biology*, 42." in rendered


def test_bib_entry_pretty_renders_book() -> None:
    entry = BibEntry(
        key="text",
        entry_type="book",
        author="Lone, Author",
        year="1990",
        title="Foundations",
        publisher="Acme Press",
    )
    rendered = entry.pretty()
    assert "*Foundations*." in rendered
    assert "Acme Press." in rendered


def test_short_authors_handles_three_or_more_names() -> None:
    entry = BibEntry(
        key="multi",
        entry_type="article",
        author="One, A and Two, B and Three, C",
        year="2024",
    )
    assert entry.pretty().startswith("One et al. (2024).")


def test_render_section_uses_specialized_source_heading() -> None:
    entry = BibEntry(
        key="ex",
        entry_type="article",
        author="Example, Ada",
        year="2026",
        title="A claim",
        journal="J",
    )
    section = render_section([entry], "Cell Theory")
    assert "## Further Reading and Source Notes: Cell Theory" in section
    assert "\n## Further Reading\n" not in section


def test_pick_keys_prefers_cited_keys_then_supplement() -> None:
    picked = pick_keys("unit_I/water_and_life.md", ["henderson1913", "linus1960"])
    assert picked[0] == "henderson1913"
    assert "linus1960" in picked


def test_collect_keys_returns_only_documented_citation_keys() -> None:
    text = r"As shown in \citep{watson1953} and \citet{crick1958}, ..."
    keys = collect_keys(text)
    assert keys == ["watson1953", "crick1958"]


def test_parse_bib_reads_live_references() -> None:
    bib = parse_bib(BIB)
    assert bib, "references.bib should parse into at least one entry"
    sample = next(iter(bib.values()))
    assert isinstance(sample, BibEntry)


def test_inject_skips_chapters_with_existing_further_reading(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    manuscript.mkdir()
    chapter = manuscript / "ch.md"
    chapter.write_text("# Demo\n\n## Further Reading\n\n- existing\n", encoding="utf-8")
    bib = {"k": BibEntry(key="k", entry_type="article", author="A", year="2024", title="t", journal="j")}
    assert not inject(chapter, bib, "Demo", manuscript_root=manuscript)


def test_supplement_map_paths_and_citekeys_are_valid() -> None:
    issues = validate_supplement()
    assert not issues, issues
