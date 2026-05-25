"""Tests for shared Mermaid metadata normalization."""

from __future__ import annotations

from pathlib import Path

from biology.maintenance.text_normalize import _read_immediate_metadata, normalize_text


def test_read_immediate_metadata_reads_alt_and_caption() -> None:
    text_after = "\n".join(
        [
            "<!-- alt: Directed graph from A to B showing a simple causal link. -->",
            "",
            "*Simple causal link from stimulus A to response B in the pathway model.*",
            "",
            "Next paragraph.",
        ]
    )
    metadata = _read_immediate_metadata(text_after)
    assert metadata.alts
    assert metadata.captions
    assert "Directed graph" in metadata.alts[0]
    assert "Simple causal link" in metadata.captions[0]


def test_normalize_text_is_idempotent_on_clean_block() -> None:
    sample = "\n".join(
        [
            "# Chapter",
            "",
            "```mermaid",
            "flowchart TD",
            "  A[Start] --> B[End]",
            "```",
            "<!-- alt: Flowchart from Start node to End node with one directed arrow. -->",
            "",
            "*Flow from Start to End across a single regulatory step.*",
        ]
    )
    first = normalize_text(sample).text
    second = normalize_text(first).text
    assert first == second


def test_normalize_file_rewrites_weak_mermaid_metadata(tmp_path: Path) -> None:
    from biology.maintenance.text_normalize import normalize_file

    path = tmp_path / "chapter.md"
    path.write_text(
        "\n".join(
            [
                "## Signal transduction",
                "",
                "```mermaid",
                "flowchart TD",
                "  A[Receptor] --> B[Kinase cascade]",
                "```",
                "<!-- alt: network graph showing biological relationships -->",
                "",
                "*Network graph showing biological relationships.*",
            ]
        ),
        encoding="utf-8",
    )
    result = normalize_file(path, write=True)
    assert result.blocks == 1
    updated = path.read_text(encoding="utf-8")
    assert "network graph showing biological relationships" not in updated.lower()
