"""Visual contract datatypes and scan regexes."""

from __future__ import annotations

import re
from dataclasses import dataclass

_LATEX_FIGURE_RE = re.compile(r"\\begin\{figure\}.*?\\end\{figure\}", re.DOTALL)
_INCLUDE_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{(?P<path>[^}]+)\}")
_CAPTION_RE = re.compile(r"\\caption\{(?P<caption>.*?)\}\s*\\label", re.DOTALL)
_LABEL_RE = re.compile(r"\\label\{(?P<label>fig:[^}]+)\}")
_ALT_RE = re.compile(r"<!--\s*alt:\s*(?P<alt>.*?)\s*-->", re.DOTALL | re.IGNORECASE)
_MERMAID_RE = re.compile(
    r"^```mermaid\s*\n(?P<source>.*?)^```\s*$",
    re.DOTALL | re.MULTILINE | re.IGNORECASE,
)
_ITALIC_CAPTION_RE = re.compile(r"^\s*\*(?!\*)(?P<caption>[^*\n].{6,}[^*\s])\*\s*$")
_STYLE_COLOR_RE = re.compile(
    r"(?:^|\s)(?:style|classDef)\s+[^;\n]*(?P<props>fill:#[0-9A-Fa-f]{6}[^;\n]*|stroke:#[0-9A-Fa-f]{6}[^;\n]*)"
)
_HEX_RE = re.compile(r"(?P<key>fill|stroke):(?P<hex>#[0-9A-Fa-f]{6})")

_STOPWORDS = {
    "and",
    "the",
    "with",
    "from",
    "into",
    "versus",
    "against",
    "showing",
    "shows",
    "figure",
    "plot",
    "panel",
    "line",
    "chart",
    "axis",
    "axes",
    "indexed",
    "illustrative",
}


@dataclass(frozen=True)
class VisualRecord:
    """One raw, registered Mermaid, or inline Mermaid visual contract entry."""

    kind: str
    source_path: str
    line: int
    label: str
    caption: str
    alt: str
    asset_path: str
    generator: str
    width_px: int
    height_px: int
    aspect_policy: str = ""
    aspect_exception: str = ""


@dataclass(frozen=True)
class Finding:
    """A visual-contract audit finding."""

    code: str
    source_path: str
    line: int
    detail: str


__all__ = [
    "Finding",
    "VisualRecord",
    "_ALT_RE",
    "_CAPTION_RE",
    "_HEX_RE",
    "_INCLUDE_RE",
    "_ITALIC_CAPTION_RE",
    "_LABEL_RE",
    "_LATEX_FIGURE_RE",
    "_MERMAID_RE",
    "_STOPWORDS",
    "_STYLE_COLOR_RE",
]
