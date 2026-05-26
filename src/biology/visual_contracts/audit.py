"""Audit visual contract records and Mermaid sources."""

from __future__ import annotations

from collections.abc import Iterable

from biology.visual_contracts.helpers import (
    ensure_import_paths,
    relative,
    tokens,
)
from biology.visual_contracts.manifest import aspect_ratio
from biology.visual_contracts.models import (
    Finding,
    VisualRecord,
    _HEX_RE,
    _MERMAID_RE,
    _STYLE_COLOR_RE,
)
from biology.visual_contracts.scan import registered_mermaid_factories
from biology.visual_contracts_paths import MANUSCRIPT_DIR


def contrast_ratio(hex_a: str, hex_b: str) -> float:
    def luminance(hex_color: str) -> float:
        rgb = [int(hex_color[i : i + 2], 16) / 255.0 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

    l1, l2 = sorted((luminance(hex_a), luminance(hex_b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def mermaid_sources() -> Iterable[tuple[str, int, str]]:
    ensure_import_paths()
    for _name, factory, line in registered_mermaid_factories():
        diagram = factory()
        yield "src/mermaid/biology_diagrams.py", line, diagram.source
    for path in sorted(MANUSCRIPT_DIR.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in _MERMAID_RE.finditer(text):
            yield relative(path), text.count("\n", 0, match.start()) + 1, match.group("source").strip()


def check_records(records: list[VisualRecord]) -> list[Finding]:
    """Return visual-contract findings."""
    findings: list[Finding] = []
    seen_labels: dict[str, VisualRecord] = {}

    for record in records:
        if record.label:
            previous = seen_labels.get(record.label)
            if previous is not None:
                findings.append(
                    Finding(
                        "duplicate-label",
                        record.source_path,
                        record.line,
                        f"also used at {previous.source_path}:{previous.line}",
                    )
                )
            seen_labels[record.label] = record

        if record.kind == "raw_figure":
            if (
                record.source_path.startswith("manuscript/unit_")
                and not record.label.startswith("fig:unit_")
            ):
                findings.append(
                    Finding(
                        "unit-prefixed-label",
                        record.source_path,
                        record.line,
                        f"label must start with fig:unit_: {record.label}",
                    )
                )
            if not record.caption:
                findings.append(Finding("missing-caption", record.source_path, record.line, record.asset_path))
            if not record.alt:
                findings.append(Finding("missing-alt", record.source_path, record.line, record.asset_path))
            caption_tokens = tokens(record.caption)
            alt_tokens = tokens(record.alt)
            if record.caption and record.alt and len(caption_tokens & alt_tokens) < 2:
                findings.append(
                    Finding(
                        "caption-alt-drift",
                        record.source_path,
                        record.line,
                        f"{record.label} caption/alt share too little domain vocabulary",
                    )
                )

        if record.width_px and record.height_px and not record.aspect_exception:
            ratio = aspect_ratio(record)
            policy = record.aspect_policy
            if not policy and record.kind == "raw_figure":
                policy = "figure-square"
            if not policy and record.kind in {"registered_mermaid", "inline_mermaid"}:
                policy = "mermaid-square"
            if policy == "figure-square" and not 0.85 <= ratio <= 1.18:
                findings.append(
                    Finding(
                        "figure-square-aspect",
                        record.source_path,
                        record.line,
                        f"{record.asset_path} ratio {ratio:.2f} outside 0.85-1.18",
                    )
                )
            if policy == "figure-landscape" and not 1.05 <= ratio <= 3.5:
                findings.append(
                    Finding(
                        "figure-landscape-aspect",
                        record.source_path,
                        record.line,
                        f"{record.asset_path} ratio {ratio:.2f} outside 1.05-3.5",
                    )
                )
            if policy == "mermaid-square" and not 0.75 <= ratio <= 1.33:
                findings.append(
                    Finding(
                        "mermaid-square-aspect",
                        record.source_path,
                        record.line,
                        f"{record.asset_path} ratio {ratio:.2f} outside 0.75-1.33",
                    )
                )

    for source_path, line, source in mermaid_sources():
        if source_path == "src/mermaid/biology_diagrams.py" and "\\n" in source:
            findings.append(
                Finding(
                    "mermaid-newline-escape",
                    source_path,
                    line,
                    "use <br/> rather than literal escaped newlines",
                )
            )
        for line_offset, mermaid_line in enumerate(source.splitlines(), start=0):
            color_match = _STYLE_COLOR_RE.search(mermaid_line)
            if not color_match:
                continue
            props = {
                m.group("key"): m.group("hex")
                for m in _HEX_RE.finditer(color_match.group("props"))
            }
            if (
                "fill" in props
                and "stroke" in props
                and contrast_ratio(props["fill"], props["stroke"]) < 3.0
            ):
                findings.append(
                    Finding(
                        "mermaid-low-contrast",
                        source_path,
                        line + line_offset,
                        f"{props['fill']} vs {props['stroke']}",
                    )
                )

    return findings


__all__ = ["check_records", "contrast_ratio", "mermaid_sources"]
