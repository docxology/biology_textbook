"""Tests for declarative Mermaid diagram specs."""

from __future__ import annotations

from mermaid.diagram_spec_loader import build_diagram_from_spec, load_all_diagrams


def test_load_all_diagrams_returns_non_empty_registry() -> None:
    diagrams = load_all_diagrams()
    assert diagrams
    names = {diagram.name for diagram in diagrams}
    assert len(names) == len(diagrams)


def test_build_diagram_from_spec_flowchart() -> None:
    diagram = build_diagram_from_spec(
        {
            "name": "test_flow",
            "type": "flowchart",
            "title": "Test flow",
            "nodes": [["A", "Start"], ["B", "End"]],
            "edges": [["A", "B", "goes"]],
            "direction": "LR",
        }
    )
    assert diagram.name == "test_flow"
    assert "flowchart LR" in diagram.source
    assert "Start" in diagram.source
