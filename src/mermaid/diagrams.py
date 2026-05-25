"""Generic Mermaid diagram builders.

Provides builder functions for common Mermaid diagram types:
flowchart, sequence, class, state, ER, and pie diagrams.
All return MermaidDiagram instances, ready for rendering.
"""

from __future__ import annotations

import re

from .renderer import MermaidDiagram
from textbook_logging import get_logger

logger = get_logger(__name__)


def _label(text: str) -> str:
    """Return a Mermaid-safe quoted label."""
    return text.replace("\\", "\\\\").replace('"', "&quot;").replace("\n", "<br/>")


def _participant_id(index: int) -> str:
    """Return a stable sequence-diagram participant id."""
    return f"P{index}"


# ---------------------------------------------------------------------------
# Flowchart
# ---------------------------------------------------------------------------


def flowchart(
    name: str,
    title: str,
    nodes: list[tuple[str, str]],  # (id, label)
    edges: list[tuple[str, str, str]],  # (from_id, to_id, label)
    direction: str = "TD",
) -> MermaidDiagram:
    """Build a Mermaid flowchart diagram.

    Args:
        name: Filename stem.
        title: Human-readable title.
        nodes: List of (node_id, node_label) tuples.
        edges: List of (from_id, to_id, edge_label) tuples.
        direction: Graph direction — TB, TD, BT, LR, RL (default TD).

    Returns:
        MermaidDiagram ready to render.
    """
    lines = [f"flowchart {direction}"]
    for node_id, label in nodes:
        lines.append(f'    {node_id}["{_label(label)}"]')
    for from_id, to_id, label in edges:
        if label:
            lines.append(f"    {from_id} -->|{label}| {to_id}")
        else:
            lines.append(f"    {from_id} --> {to_id}")
    source = "\n".join(lines)
    logger.debug(f"Built flowchart diagram: {name}")
    return MermaidDiagram(name=name, source=source, title=title)


# ---------------------------------------------------------------------------
# Sequence Diagram
# ---------------------------------------------------------------------------


def sequence_diagram(
    name: str,
    title: str,
    participants: list[str],
    messages: list[tuple[str, str, str]],  # (from, to, message)
) -> MermaidDiagram:
    """Build a Mermaid sequence diagram.

    Args:
        name: Filename stem.
        title: Title.
        participants: List of participant names.
        messages: List of (sender, receiver, message_text) tuples.

    Returns:
        MermaidDiagram.
    """
    aliases = {p: _participant_id(i) for i, p in enumerate(participants)}
    lines = ["sequenceDiagram"]
    for p in participants:
        lines.append(f"    participant {aliases[p]} as {_label(p)}")
    for sender, receiver, msg in messages:
        safe_sender = aliases.get(sender, re.sub(r"\W+", "_", sender))
        safe_receiver = aliases.get(receiver, re.sub(r"\W+", "_", receiver))
        lines.append(f"    {safe_sender}->>{safe_receiver}: {_label(msg)}")
    source = "\n".join(lines)
    return MermaidDiagram(name=name, source=source, title=title)


# ---------------------------------------------------------------------------
# Class Diagram
# ---------------------------------------------------------------------------


def class_diagram(
    name: str,
    title: str,
    classes: list[tuple[str, list[str], list[str]]],  # (name, attributes, methods)
    relationships: list[tuple[str, str, str]],  # (from, relation, to)
) -> MermaidDiagram:
    """Build a Mermaid class diagram.

    Args:
        name: Filename stem.
        title: Title.
        classes: List of (class_name, [attributes], [methods]).
        relationships: List of (class_a, relation_type, class_b).
                       relation_type: --|>, --*, --, ..>, etc.

    Returns:
        MermaidDiagram.
    """
    lines = ["classDiagram"]
    for class_name, attrs, methods in classes:
        lines.append(f"    class {class_name} {{")
        for attr in attrs:
            lines.append(f"        +{attr}")
        for method in methods:
            lines.append(f"        +{method}()")
        lines.append("    }")
    for class_a, relation, class_b in relationships:
        lines.append(f"    {class_a} {relation} {class_b}")
    source = "\n".join(lines)
    return MermaidDiagram(name=name, source=source, title=title)


# ---------------------------------------------------------------------------
# State Diagram
# ---------------------------------------------------------------------------


def state_diagram(
    name: str,
    title: str,
    states: list[str],
    transitions: list[tuple[str, str, str]],  # (from_state, to_state, event)
    initial_state: str = "",
    final_states: list[str] | None = None,
) -> MermaidDiagram:
    """Build a Mermaid state diagram (v2).

    Declares each state with ``state "label" as stN`` so labels can contain
    spaces, parentheses, and other characters that break bare identifiers.

    Args:
        name: Filename stem.
        title: Title.
        states: List of state names (include every state referenced in transitions).
        transitions: (from_state, to_state, event_label).
        initial_state: Name of the initial state.
        final_states: List of terminal/final states.

    Returns:
        MermaidDiagram.
    """
    # Collect all unique state labels in a stable order.
    order: list[str] = []
    for s in list(states) + [initial_state, *(final_states or [])]:
        if s and s not in order:
            order.append(s)
    for from_s, to_s, _e in transitions:
        for s in (from_s, to_s):
            if s and s not in order:
                order.append(s)
    for fs in final_states or []:
        if fs and fs not in order:
            order.append(fs)
    st_id: dict[str, str] = {label: f"st{i}" for i, label in enumerate(order)}

    lines = ["stateDiagram-v2"]
    for _i, label in enumerate(order):
        esc = label.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'    state "{esc}" as {st_id[label]}')
    if initial_state:
        lines.append(f"    [*] --> {st_id[initial_state]}")
    for from_s, to_s, event in transitions:
        a, b = st_id[from_s], st_id[to_s]
        if event:
            lines.append(f"    {a} --> {b} : {event}")
        else:
            lines.append(f"    {a} --> {b}")
    for fs in final_states or []:
        lines.append(f"    {st_id[fs]} --> [*]")
    source = "\n".join(lines)
    return MermaidDiagram(name=name, source=source, title=title)


# ---------------------------------------------------------------------------
# Pie Chart
# ---------------------------------------------------------------------------


def pie_chart(
    name: str,
    title: str,
    labels_values: list[tuple[str, float]],
) -> MermaidDiagram:
    """Build a Mermaid pie chart.

    Args:
        name: Filename stem.
        title: Chart title.
        labels_values: List of (label, value) tuples.

    Returns:
        MermaidDiagram.
    """
    lines = [f"pie title {title}"]
    for label, value in labels_values:
        lines.append(f'    "{label}" : {value:.1f}')
    source = "\n".join(lines)
    return MermaidDiagram(name=name, source=source, title=title)
