"""Mermaid diagram subpackage."""

from __future__ import annotations

from . import biology_diagrams as _biology_diagrams
from .diagram_spec_loader import diagram_factory_names
from .diagrams import class_diagram, flowchart, pie_chart, sequence_diagram, state_diagram
from .renderer import MermaidDiagram, MermaidRenderer

ALL_BIOLOGY_DIAGRAMS = _biology_diagrams.ALL_BIOLOGY_DIAGRAMS

_FACTORY_NAMES = diagram_factory_names()
globals().update({name: getattr(_biology_diagrams, name) for name in _FACTORY_NAMES})

__all__ = [
    "MermaidDiagram",
    "MermaidRenderer",
    "flowchart",
    "sequence_diagram",
    "class_diagram",
    "state_diagram",
    "pie_chart",
    "ALL_BIOLOGY_DIAGRAMS",
    *_FACTORY_NAMES,
]
