"""Normalize inline Mermaid alt text and captions (shared library)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from biology.citations import strip_citations
from biology.maintenance.models import PROJECT
from textbook_io import write_text_atomic

MANUSCRIPT = PROJECT / "docs" / "manuscript"

MERMAID_BLOCK_RE = re.compile(
    r"^```mermaid\s*\n(?P<source>.*?)^```\s*$",
    re.DOTALL | re.MULTILINE,
)
ALT_LINE_RE = re.compile(r"^\s*<!--\s*alt:\s*(?P<body>.*?)\s*-->\s*$", re.IGNORECASE)
ITALIC_CAPTION_RE = re.compile(r"^\s*\*(?P<body>[^*\n].{6,}[^*\s])\*\s*$")
BOLD_CAPTION_RE = re.compile(
    r"^\s*\*\*(?P<title>[^*\n]{3,90})\*\*[:.]?\s*(?P<body>.{10,})\s*$"
)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(?P<title>.+?)\s*(?:\{#.*?\})?\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
SQUARE_LABEL_RE = re.compile(r"\[\s*\"?(?P<label>[^\"\]\n][^\]\n]{2,110})\"?\s*\]")
CURLY_LABEL_RE = re.compile(r"\{\s*\"?(?P<label>[^\"}\n][^}\n]{2,110})\"?\s*\}")

WEAK_METADATA_FRAGMENTS: tuple[str, ...] = (
    "flowchart of c4 carbon fixation pathway showing co2 concentration and spatial separation",
    "flowchart depicting biological process or pathway",
    "network graph showing biological relationships",
    "sequence diagram showing step-by-step molecular or cellular interactions",
    "gene regulatory network showing interactions between transcription factors and target genes",
    "metabolic network diagram showing biochemical pathways and their connections",
    "state diagram showing biological states and transitions",
    "mermaid directed graph summarizing a conceptual relationship described in the surrounding text",
    "mermaid sequence diagram summarizing a conceptual relationship described in the surrounding text",
    "phylogenetic tree showing evolutionary relationships among taxa",
    "food web network showing trophic interactions",
    "flowchart of the global carbon cycle showing major carbon fluxes between reservoirs",
    "identify the main nodes and their directional relationships",
    "mark the main actors or messages in the ordered interaction",
    "mark the major states and transitions",
    "ordered messages show how the process unfolds over time",
    "arrows connect the major causes, components, or outcomes",
    "section's process model",
    "amerefsec:",
)


@dataclass(frozen=True)
class MermaidMetadata:
    """Immediate metadata following a Mermaid fence."""

    consumed_chars: int
    alts: tuple[str, ...]
    captions: tuple[str, ...]


@dataclass(frozen=True)
class FileResult:
    """Result of normalizing one file."""

    path: Path
    blocks: int
    changed: bool


@dataclass(frozen=True)
class TextResult:
    """Result of normalizing Mermaid metadata in a markdown string."""

    text: str
    blocks: int


def _manuscript_markdown_files() -> list[Path]:
    """Return manuscript markdown files that can contain renderable diagrams."""
    return [
        p
        for p in sorted(MANUSCRIPT.rglob("*.md"))
        if p.name not in {"AGENTS.md", "README.md"}
    ]


def _diagram_kind(source: str) -> str:
    for line in source.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped.split()[0]
    return "diagram"


def _plain_text(markdown: str) -> str:
    """Return readable text from a one-line caption or Mermaid label."""
    text = MARKDOWN_LINK_RE.sub(lambda match: match.group(1), markdown)
    text = re.sub(r"<[^>]+>", " ", text)
    text = strip_citations(text, strip_incomplete_tail=True)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("<br/>", " ").replace(r"\n", " ")
    text = text.replace("$", "")
    text = re.sub(r"\\(?:[Cc]ref|[Nn]ameref|ref)\{[^}]+\}", "the referenced section", text)
    text = re.sub(r"\bamerefsec:[A-Za-z0-9_:-]+\b", "the referenced section", text)
    text = strip_citations(text)
    text = re.sub(r"\\[a-zA-Z]+", "", text)
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\b[A-Za-z]+[0-9]{4}\b", "", text)
    text = re.sub(r"\s*\|.*$", "", text)
    text = re.sub(r"^\s*[\[(]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    text = re.sub(r"([.!?])\s*([.!?])+", r"\1", text)
    return text


def _clean_caption(raw_caption: str) -> str:
    """Normalize an italic caption while preserving its textbook content."""
    caption = " ".join(raw_caption.split())
    caption = re.sub(r"\s*\(Mermaid\)\.?", "", caption, flags=re.IGNORECASE)
    caption = re.sub(r"\.\s*\.", ".", caption)
    caption = re.sub(r"\s+([,.;:])", r"\1", caption)
    caption = re.sub(r"\s+", " ", caption).strip()
    if caption and caption[-1] not in ".!?":
        caption += "."
    return caption


def _metadata_is_weak(text: str) -> bool:
    raw = text.lower()
    cleaned = _plain_text(text).lower().strip(" .")
    return (
        len(cleaned) < 24
        or any(fragment in cleaned for fragment in WEAK_METADATA_FRAGMENTS)
        or any(fragment in raw for fragment in WEAK_METADATA_FRAGMENTS)
    )


def _labels_from_source(source: str) -> list[str]:
    """Extract human labels from Mermaid source in stable order."""
    labels: list[str] = []
    seen: set[str] = set()

    for line in source.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("classDef ", "class ", "style ")):
            continue
        if stripped.startswith("participant "):
            label = stripped.removeprefix("participant ").strip()
            if " as " in label:
                label = label.split(" as ", 1)[1].strip()
            _append_label(labels, seen, label)
            continue
        if ":" in stripped and "->" in stripped:
            _append_label(labels, seen, stripped.split(":", 1)[1].strip())
        for pattern in (SQUARE_LABEL_RE, CURLY_LABEL_RE):
            for match in pattern.finditer(stripped):
                _append_label(labels, seen, match.group("label"))

    return labels


def _discard_label(label: str) -> bool:
    low = label.lower()
    if low.startswith(("fill:", "stroke:", "color:", "http")):
        return True
    return any(token in label for token in ("-->", "-.->", "==>", ":::", "classDef"))


def _append_label(labels: list[str], seen: set[str], label: str) -> None:
    label = _plain_text(label).strip('" ')
    if not label or _discard_label(label):
        return
    if len(label) < 3 or len(label) > 90:
        return
    if label not in seen:
        labels.append(label)
        seen.add(label)


def _nearest_heading(text_before: str) -> str:
    headings = [match.group("title") for match in HEADING_RE.finditer(text_before)]
    if not headings:
        return "the surrounding section"
    heading = headings[-1]
    heading = re.sub(r"\s*\{[^}]*\}\s*$", "", heading)
    heading = re.sub(r"^\d+(?:\.\d+)*\s+", "", heading)
    return _plain_text(heading).strip() or "the surrounding section"


def _join_examples(labels: list[str]) -> str:
    sample = labels[:4]
    if not sample:
        return ""
    if len(sample) == 1:
        return sample[0]
    if len(sample) == 2:
        return f"{sample[0]} and {sample[1]}"
    return f"{', '.join(sample[:-1])}, and {sample[-1]}"


def _caption_from_source(source: str, text_before: str) -> str:
    kind = _diagram_kind(source)
    labels = _labels_from_source(source)
    heading = _nearest_heading(text_before)
    examples = _join_examples(labels)
    if kind == "sequenceDiagram":
        if examples:
            return f"Sequence diagram for {heading} showing ordered interaction among {examples}."
        return f"Sequence diagram for {heading}: message order defines the process timing."
    if kind.startswith("stateDiagram"):
        if examples:
            return f"State diagram for {heading} showing transitions among {examples}."
        return f"State diagram for {heading}: transition arrows define the biological state changes."
    if kind in {"flowchart", "graph"}:
        if examples:
            return f"Flowchart for {heading}: {examples} form the diagram's primary path or branches."
        return (
            f"Flowchart for {heading} showing directional links among the section's causes, "
            "components, and outcomes."
        )
    if examples:
        return f"Diagram for {heading}: {examples} summarize the main labeled relationships."
    return f"Diagram for {heading}: labeled elements summarize the process described in the surrounding text."


def _alt_from_caption(caption: str, source: str, text_before: str) -> str:
    """Create one sentence of alt text from a caption or diagram source."""
    if _metadata_is_weak(caption):
        caption = _caption_from_source(source, text_before)
    alt = _plain_text(caption)
    alt = re.sub(r"^The\s+", "", alt).strip()
    if not re.match(r"^(Flowchart|Diagram|Sequence diagram|State diagram|Network|Timeline)\b", alt):
        kind = _diagram_kind(source)
        prefix = {
            "sequenceDiagram": "Sequence diagram showing ",
            "stateDiagram": "State diagram showing ",
            "stateDiagram-v2": "State diagram showing ",
            "flowchart": "Flowchart showing ",
            "graph": "Graph showing ",
        }.get(kind, "Diagram showing ")
        if re.match(r"^[A-Z0-9]{2,}(?:\b|/)", alt):
            alt = prefix + alt
        else:
            alt = prefix + alt[:1].lower() + alt[1:]
    alt = re.sub(r"\s+", " ", alt).strip()
    alt = alt.replace("--", "-")
    if len(alt) > 500:
        alt = alt[:497].rsplit(" ", 1)[0].rstrip(" ,;:")
    if alt and alt[-1] not in ".!?":
        alt += "."
    return alt


def _read_immediate_metadata(text_after: str) -> MermaidMetadata:
    """Read blank lines, alt comments, and italic captions immediately after a fence."""
    alts: list[str] = []
    captions: list[str] = []
    consumed = 0
    for line in text_after.splitlines(keepends=True):
        stripped = line.strip()
        alt_match = ALT_LINE_RE.match(line)
        caption_match = ITALIC_CAPTION_RE.match(line)
        if stripped == "":
            consumed += len(line)
            continue
        if alt_match:
            alts.append(alt_match.group("body").strip())
            consumed += len(line)
            continue
        if caption_match:
            captions.append(caption_match.group("body").strip())
            consumed += len(line)
            continue
        bold_caption_match = BOLD_CAPTION_RE.match(line)
        if bold_caption_match:
            title = bold_caption_match.group("title").strip().rstrip(".")
            body = bold_caption_match.group("body").strip()
            captions.append(f"{title}. {body}")
            consumed += len(line)
            continue
        break
    return MermaidMetadata(consumed, tuple(alts), tuple(captions))


def _replacement_metadata(source: str, text_before: str, existing_captions: tuple[str, ...]) -> str:
    """Return canonical metadata text for one Mermaid block."""
    caption = next((c for c in existing_captions if not _metadata_is_weak(c)), "")
    caption = _clean_caption(caption) if caption else _caption_from_source(source, text_before)
    caption = _clean_caption(caption)
    alt = _alt_from_caption(caption, source, text_before)
    return f"\n<!-- alt: {alt} -->\n\n*{caption}*\n\n"


def normalize_file(path: Path, *, write: bool) -> FileResult:
    """Normalize Mermaid metadata in ``path``."""
    source_text = path.read_text(encoding="utf-8")
    result = normalize_text(source_text)
    changed = result.text != source_text
    if changed and write:
        write_text_atomic(path, result.text)
    return FileResult(path, result.blocks, changed)


def normalize_text(source_text: str) -> TextResult:
    """Normalize Mermaid metadata in a markdown string."""
    out_parts: list[str] = []
    last = 0
    blocks = 0

    for match in MERMAID_BLOCK_RE.finditer(source_text):
        blocks += 1
        metadata = _read_immediate_metadata(source_text[match.end() :])
        out_parts.append(source_text[last : match.end()])
        out_parts.append(
            _replacement_metadata(
                match.group("source"),
                source_text[: match.start()],
                metadata.captions,
            )
        )
        last = match.end() + metadata.consumed_chars

    if blocks == 0:
        return TextResult(source_text, 0)

    out_parts.append(source_text[last:])
    normalized = "".join(out_parts)
    return TextResult(normalized, blocks)


def normalize_all(*, manuscript: Path, write: bool) -> list[FileResult]:
    """Normalize all Mermaid blocks under ``manuscript``."""
    files = [
        path
        for path in sorted(manuscript.rglob("*.md"))
        if path.name not in {"AGENTS.md", "README.md"}
    ]
    return [normalize_file(path, write=write) for path in files]
