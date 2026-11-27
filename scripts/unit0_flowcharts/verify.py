"""Independently check the Mermaid subset used by the reviewed sources."""

from collections import Counter
import json
from pathlib import Path
import re
from xml.etree import ElementTree as ET

from PIL import Image


def verify_flowchart(path: Path) -> dict[str, int]:
    lines = path.read_text().splitlines()
    dialect, direction = lines[0].split()
    assert dialect in ("graph", "flowchart")
    nodes: dict[str, tuple[str, str]] = {}
    edges: Counter[tuple[str, str, str, str]] = Counter()
    group = None
    groups: dict[str, set[str]] = {}
    styles: dict[str, dict[str, str]] = {}

    def endpoint(value: str) -> str:
        match = re.fullmatch(
            r'([A-Za-z][A-Za-z0-9]*)(?:(\[|\{|\(\()"(.+)"(\]|\}|\)\)))?', value
        )
        assert match, value
        node, opener, label, closer = match.groups()
        if opener is not None:
            shape, expected_closer = {
                "[": ("rectangle", "]"),
                "{": ("diamond", "}"),
                "((": ("circle", "))"),
            }[opener]
            assert closer == expected_closer
            nodes[node] = (normal(label), shape)
        if group is not None:
            groups[group].add(node)
        return node

    def normal(label: str) -> str:
        return re.sub(
            r"\s+", " ", label.replace("\\n", " ").replace("<br/>", " ")
        ).strip()

    for line in map(str.strip, lines[1:]):
        if not line:
            continue
        if line.startswith("subgraph "):
            assert group is None
            group = line[len("subgraph ") :].strip('"')
            groups[group] = set()
        elif line == "end":
            assert group is not None
            group = None
        elif line.startswith("style "):
            _, name, style = line.split(" ", 2)
            styles[name] = dict(part.split(":", 1) for part in style.split(","))
        elif match := re.fullmatch(
            r'(.+?)\s+(-->|-\.->)\s*(?:\|(".*?"|[^|]+)\|\s*)?(.+)', line
        ):
            left, arrow, label, right = match.groups()
            target = endpoint(right)
            for source in re.split(r' & (?=(?:[^"]*"[^"]*")*[^"]*$)', left):
                edges[
                    endpoint(source),
                    target,
                    normal((label or "").strip('"')),
                    "dotted" if arrow == "-.->" else "solid",
                ] += 1
        else:
            endpoint(line)
    svg = path.with_suffix(".svg")
    model = json.loads(path.with_suffix(".json").read_text())
    assert model["direction"] == direction
    assert {
        group["label"]: set(group["nodeIds"]) for group in model["subgraphs"]
    } == groups, path
    root = ET.parse(svg).getroot()
    output_nodes = {
        item.get("data-id"): (
            normal(item.get("data-label", "")),
            item.get("data-shape"),
        )
        for item in root.iter()
        if item.get("class") == "node"
    }
    assert output_nodes == nodes, (path, output_nodes, nodes)
    for item in root.iter():
        if item.get("class") in {"node", "edge-label", "subgraph"}:
            pieces = [
                "".join(part.itertext())
                for child in item
                if child.tag.endswith("}text")
                for part in (list(child) or [child])
            ]
            assert normal(" ".join(pieces)) == normal(item.get("data-label", "")), (
                path,
                item.get("data-label"),
                pieces,
            )
    output_edges: Counter[tuple[str, str, str, str]] = Counter()
    for item in root.iter():
        if item.get("class") == "edge":
            assert (
                item.get("data-arrow-start") == "false"
                and item.get("data-arrow-end") == "true"
                and item.get("marker-end")
            )
            output_edges[
                item.get("data-from", ""),
                item.get("data-to", ""),
                normal(item.get("data-label", "")),
                item.get("data-style", ""),
            ] += 1
    assert output_edges == edges, (path, output_edges, edges)
    assert {
        item.get("data-label")
        for item in root.iter()
        if item.get("class") == "subgraph"
    } == groups.keys(), path
    for node, style in styles.items():
        rendered = next(
            item
            for item in root.iter()
            if item.get("class") == "node" and item.get("data-id") == node
        )
        for expected in style.values():
            assert expected in ET.tostring(rendered, encoding="unicode"), (
                path,
                node,
                expected,
            )
    with Image.open(path.with_suffix(".png")) as image:
        image.load()
        assert (
            image.format == "PNG" and max(image.size) == 1600 and min(image.size) >= 100
        ), path
        assert len(image.getcolors(1_000_000)) > 25, path
        return dict(
            nodes=len(nodes),
            edges=sum(edges.values()),
            groups=len(groups),
            width=image.width,
            height=image.height,
        )
