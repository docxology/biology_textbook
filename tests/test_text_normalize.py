"""Tests for shared Mermaid metadata normalization."""

from __future__ import annotations

from pathlib import Path

from biology.maintenance.text_normalize import normalize_text


def test_normalize_text_is_idempotent_on_clean_block() -> None:
    sample = (
        "# Chapter\n\n```mermaid\nflowchart TD\n  A[Start] --> B[End]\n```\n"
        "<!-- alt: Flowchart from Start node to End node with one directed arrow. -->\n\n"
        "*Flow from Start to End across a single regulatory step.*"
    )
    first = normalize_text(sample).text
    second = normalize_text(first).text
    assert first == second


def test_normalize_file_rewrites_weak_mermaid_metadata(tmp_path: Path) -> None:
    from biology.maintenance.text_normalize import normalize_file

    path = tmp_path / "chapter.md"
    path.write_text(
        "## Signal transduction\n\n```mermaid\nflowchart TD\n  A[Receptor] --> B[Kinase cascade]\n```\n"
        "<!-- alt: network graph showing biological relationships -->\n\n"
        "*Network graph showing biological relationships.*",
        encoding="utf-8",
    )
    result = normalize_file(path, write=True)
    assert result.blocks == 1
    updated = path.read_text(encoding="utf-8")
    assert "network graph showing biological relationships" not in updated.lower()


def test_diagram_kind_ignores_configuration_and_literal_yaml_delimiters() -> None:
    from biology.maintenance.text_normalize import _diagram_kind

    configuration = (
        "---\ntitle: |\n  stateDiagram-v2\n  ---\n"
        "config:\n  layout: dagre\n---\n%% explanatory comment\n"
    )
    for declaration, expected in (
        ("graph TD", "graph"),
        ("sequenceDiagram", "sequenceDiagram"),
        ("stateDiagram-v2", "stateDiagram-v2"),
    ):
        assert _diagram_kind(configuration + declaration + "\n") == expected
