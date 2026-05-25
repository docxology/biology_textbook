"""Biology-specific Mermaid diagram factory functions.

Diagram structure is declared in ``diagram_specs.yaml``; this module exposes
named factory callables and the ``ALL_BIOLOGY_DIAGRAMS`` registry for rendering.
"""

from __future__ import annotations

from .diagram_spec_loader import (
    _load_specs,
    build_diagram_from_spec,
    diagram_factory_names,
    load_all_diagrams,
)
from .renderer import MermaidDiagram

_SPECS_BY_FACTORY = {spec["factory"]: spec for spec in _load_specs()}

for _factory_name in diagram_factory_names():
    _spec = _SPECS_BY_FACTORY[_factory_name]

    def _make(_bound_spec: dict = _spec) -> MermaidDiagram:
        return build_diagram_from_spec(_bound_spec)

    _make.__name__ = _factory_name
    _make.__doc__ = f"Build the {_spec.get('title', _factory_name)} diagram."
    globals()[_factory_name] = _make

del _make, _factory_name, _spec

ALL_BIOLOGY_DIAGRAMS: list[MermaidDiagram] = load_all_diagrams()

__all__ = ["ALL_BIOLOGY_DIAGRAMS", *diagram_factory_names()]
