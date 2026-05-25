"""Tests for ``biology.maintenance.chapter_shells``."""

from __future__ import annotations

from biology.maintenance.chapter_shells import (
    OLD_TITLES_BY_STEM,
    SPLIT_STEMS,
    dedupe_badges,
    ensure_concept_check,
    insert_opening_vignette,
    reorder_back_matter,
    replace_legacy_titles,
)


def test_split_stems_match_old_titles_keys() -> None:
    assert SPLIT_STEMS == frozenset(OLD_TITLES_BY_STEM)
    assert "mendelian_principles" in SPLIT_STEMS


def test_dedupe_badges_collapses_duplicates() -> None:
    text = (
        "# Chapter\n\n"
        "<!-- chapter-metadata-badge -->\n"
        "> badge one\n\n"
        "Body.\n\n"
        "<!-- chapter-metadata-badge -->\n"
        "> badge two\n"
    )
    cleaned = dedupe_badges(text)
    assert cleaned.count("<!-- chapter-metadata-badge -->") == 1


def test_dedupe_badges_single_marker_is_passthrough() -> None:
    text = "<!-- chapter-metadata-badge -->\n> badge\n"
    assert dedupe_badges(text) == text


def test_replace_legacy_titles_rewrites_suffix() -> None:
    text = "## Current Evidence and Frontier Biology: Stale Old Title\n\nBody.\n"
    rewritten = replace_legacy_titles(text, title="Mendelian Principles")
    assert "Current Evidence and Frontier Biology: Mendelian Principles" in rewritten


def test_insert_opening_vignette_is_idempotent_when_present() -> None:
    text = (
        "# Chapter\n<!-- curriculum-scaffold-end -->\n"
        "\n---\n\n> **Opening Vignette — Demo**\n>\n> Existing.\n\nBody.\n"
    )
    assert insert_opening_vignette(text, "Demo") == text


def test_insert_opening_vignette_adds_block_when_missing() -> None:
    text = "# Chapter\n<!-- curriculum-scaffold-end -->\n\nBody after scaffold.\n"
    out = insert_opening_vignette(text, "Mendelian Principles")
    assert "Opening Vignette — Mendelian Principles" in out


def test_ensure_concept_check_idempotent() -> None:
    text = (
        "# Demo\n\n"
        "Body.\n\n"
        "> **Concept Check:** State one claim from **Demo** and the observation.\n"
        "\n---\n"
    )
    assert ensure_concept_check(text, "Demo") == text


def test_ensure_concept_check_adds_prompt_when_missing() -> None:
    text = "# Demo\n\nBody.\n\n---\n"
    out = ensure_concept_check(text, "Demo")
    assert "**Concept Check:**" in out
    assert "**Demo**" in out


def test_reorder_back_matter_arranges_canonical_order() -> None:
    text = (
        "# Chapter\n\nBody.\n\n"
        "## Companion Source Module\n\ncm\n\n"
        "## Summary\n\ns\n\n"
        "## Current Evidence and Frontier Biology\n\nf\n\n"
        "## Review Questions\n\nrq\n\n"
        "## Further Reading and Source Notes\n\nfr\n\n"
        "## Key Terms\n\nkt\n"
    )
    out = reorder_back_matter(text)
    front_idx = out.index("## Current Evidence and Frontier Biology")
    summary_idx = out.index("## Summary")
    review_idx = out.index("## Review Questions")
    further_idx = out.index("## Further Reading and Source Notes")
    key_idx = out.index("## Key Terms")
    companion_idx = out.index("## Companion Source Module")
    assert front_idx < summary_idx < review_idx < further_idx < key_idx < companion_idx
