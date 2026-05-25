"""Regex patterns for manuscript cross-reference scanning."""

from __future__ import annotations

import re

RE_IMG = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)\s]+)(?:\s+\"[^\"]*\")?\)(?P<attrs>\{[^}]*\})?")
RE_FIG_ID = re.compile(r"\{[^}]*#fig:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")
RE_LATEX_FIG_OPEN = re.compile(r"\\begin\{figure\*?\}")
RE_LATEX_FIG_END = re.compile(r"\\end\{figure\*?\}")
RE_LATEX_INCLUDE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{(?P<path>[^}]+)\}")
RE_LATEX_TBL_OPEN = re.compile(r"\\begin\{table\*?\}")
RE_LATEX_TBL_END = re.compile(r"\\end\{table\*?\}")
RE_INLINE_DISPLAY_EQ = re.compile(r"^\s*\$\$(?P<body>.+)\$\$\s*$")
RE_EQ_TAG = re.compile(r"\\tag\{(?P<num>[^}]+)\}")
RE_RAW_LATEX_REF = re.compile(
    r"\b(?:Chapter|Ch\.?|Figure|Fig\.?|Equation|Eq\.?|Section|Table)s?(?:~|\s+)?\\(?:eqref|ref)\{[^}]+\}"
    r"|\\(?:eqref|ref|autoref)\{(?:sec|fig|eq|tbl):[^}]+\}"
)
RE_DISPLAY_EQ_OPEN = re.compile(r"^\s*\$\$\s*$")
RE_LATEX_EQ_OPEN = re.compile(r"\\begin\{(?:equation|align|gather|multline)\*?\}")
RE_LATEX_EQ_END = re.compile(r"\\end\{(?:equation|align|gather|multline)\*?\}")
RE_LATEX_LABEL = re.compile(r"\\label\{(?P<kind>eq|fig|tbl|sec):(?P<id>[A-Za-z0-9_\-:]+)\}")
RE_EQ_ID = re.compile(r"\{[^}]*#eq:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")
RE_TBL_CAPTION = re.compile(r"^(?:Table)?\s*:\s*(?P<caption>.+?)(?P<attrs>\{[^}]*\})?\s*$")
RE_TBL_ID = re.compile(r"\{[^}]*#tbl:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")
RE_PIPE_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
RE_HEADING = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)(?:\s+(?P<attrs>\{[^}]*\}))?\s*$")
RE_SEC_ID = re.compile(r"\{[^}]*#sec:(?P<id>[A-Za-z0-9_\-:]+)[^}]*\}")
RE_REF_USE = re.compile(r"(?<![A-Za-z0-9_])@(?P<kind>fig|eq|tbl|sec):(?P<id>[A-Za-z0-9_\-:]+)")
RE_PROSE_XREF = re.compile(
    r"("
    r"(?:→\s*)?(?:Chapters?|Chapter|Ch\.?|Figures?|Fig\.|Equations?|Eq\.|Sections?|Tables?)"
    r"\s+\d+(?:\.\d+)?"
    r"(?:\s*(?:,|and|or|/|[–-])\s*"
    r"(?:(?:Chapters?|Chapter|Ch\.?|Figures?|Fig\.|Equations?|Eq\.|Sections?|Tables?)\s+)?"
    r"\d+(?:\.\d+)?)*"
    r"|§+\s*\d+(?:\.\d+)?"
    r"|\bUnits?\s+(?:0(?:\.\d+)?(?:'s)?|[IVX]+(?:\s*[–-]\s*[IVX]+)?"
    r"(?:\s*(?:,|and|or|/|\+)\s*[IVX]+)*)\b"
    r"|\bAppendix\s+[A-Z]\b"
    r"|\b(?:Figure|Fig\.)\s+FM-\d+\b"
    r"|\bChapter numbers\b"
    r")",
)
RE_FENCE = re.compile(r"^\s*```\s*(?P<lang>[A-Za-z0-9_-]*)")

GENERATED_BLOCK_MARKERS: tuple[tuple[str, str], ...] = (
    ("<!-- toc-navigation-start -->", "<!-- toc-navigation-end -->"),
    ("<!-- suggested-reading-paths-start -->", "<!-- suggested-reading-paths-end -->"),
    ("<!-- textbook-concept-map-start -->", "<!-- textbook-concept-map-end -->"),
    ("<!-- course-planning-grid-start -->", "<!-- course-planning-grid-end -->"),
    ("<!-- preface-scope-start -->", "<!-- preface-scope-end -->"),
)

__all__ = [
    "GENERATED_BLOCK_MARKERS",
    "RE_DISPLAY_EQ_OPEN",
    "RE_EQ_ID",
    "RE_EQ_TAG",
    "RE_FENCE",
    "RE_FIG_ID",
    "RE_HEADING",
    "RE_IMG",
    "RE_INLINE_DISPLAY_EQ",
    "RE_LATEX_EQ_END",
    "RE_LATEX_EQ_OPEN",
    "RE_LATEX_FIG_END",
    "RE_LATEX_FIG_OPEN",
    "RE_LATEX_INCLUDE",
    "RE_LATEX_LABEL",
    "RE_LATEX_TBL_END",
    "RE_LATEX_TBL_OPEN",
    "RE_PIPE_TABLE_ROW",
    "RE_PROSE_XREF",
    "RE_RAW_LATEX_REF",
    "RE_REF_USE",
    "RE_SEC_ID",
    "RE_TBL_CAPTION",
    "RE_TBL_ID",
]
