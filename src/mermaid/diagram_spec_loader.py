"""Load declarative diagram specs and build MermaidDiagram instances."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .diagrams import flowchart, sequence_diagram, state_diagram
from .renderer import MermaidDiagram

_SPECS_PATH = Path(__file__).resolve().parent / "diagram_specs.yaml"


def _load_specs() -> list[dict[str, Any]]:
    raw = yaml.safe_load(_SPECS_PATH.read_text(encoding="utf-8"))
    diagrams = raw.get("diagrams", [])
    if not isinstance(diagrams, list):
        raise ValueError("diagram_specs.yaml must contain a top-level 'diagrams' list")
    return diagrams


def build_diagram_from_spec(spec: dict[str, Any]) -> MermaidDiagram:
    """Build one diagram from a YAML spec dict."""
    kind = spec["type"]
    if kind == "flowchart":
        nodes = [(node_id, label) for node_id, label in spec["nodes"]]
        edges = [(from_id, to_id, label) for from_id, to_id, label in spec["edges"]]
        return flowchart(
            name=spec["name"],
            title=spec["title"],
            nodes=nodes,
            edges=edges,
            direction=spec.get("direction", "TD"),
        )
    if kind == "sequence":
        messages = [(a, b, c) for a, b, c in spec["messages"]]
        return sequence_diagram(
            name=spec["name"],
            title=spec["title"],
            participants=list(spec["participants"]),
            messages=messages,
        )
    if kind == "state":
        transitions = [(a, b, c) for a, b, c in spec["transitions"]]
        return state_diagram(
            name=spec["name"],
            title=spec["title"],
            states=list(spec["states"]),
            transitions=transitions,
            initial_state=spec.get("initial_state", ""),
            final_states=list(spec.get("final_states") or []),
        )
    raise ValueError(f"Unknown diagram type: {kind!r}")


def load_all_diagrams() -> list[MermaidDiagram]:
    """Load every diagram declared in diagram_specs.yaml."""
    return [build_diagram_from_spec(spec) for spec in _load_specs()]


def diagram_factory_names() -> list[str]:
    """Return factory function names in YAML declaration order."""
    return [str(spec["factory"]) for spec in _load_specs()]


__all__ = [
    "build_diagram_from_spec",
    "diagram_factory_names",
    "load_all_diagrams",
]
