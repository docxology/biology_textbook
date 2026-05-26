"""Protected-span scanning for manuscript prose transforms."""

from __future__ import annotations

import re
from dataclasses import dataclass

PROTECTED_FENCE_LANGS = frozenset(
    {
        "python",
        "py",
        "yaml",
        "yml",
        "json",
        "bash",
        "sh",
        "shell",
        "r",
        "sql",
        "javascript",
        "js",
        "typescript",
        "ts",
    }
)

_FENCED_CODE = re.compile(r"```([a-zA-Z0-9_+-]*)\s*\n.*?\n```", re.DOTALL)
_INLINE_CODE = re.compile(r"`[^`\n]+`")
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_LATEX_ENV = re.compile(r"\\begin\{(?P<e>[A-Za-z]+\*?)\}.*?\\end\{(?P=e)\}", re.DOTALL)
_DISPLAY_MATH = re.compile(r"\$\$.*?\$\$", re.DOTALL)
_INLINE_MATH = re.compile(r"(?<!\$)\$[^$\n]+\$")
_HEADING = re.compile(r"(?m)^#{1,6} .*$")
_MD_LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
_TAGGED_BOLD = re.compile(r"(?:\[\*\*[^*]+\*\*\]|\*\*[^*]+\*\*)\s*\{#[^}]+\}")
_YAML_FRONT = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
_URL = re.compile(r"https?://[^\s)>\]}]+")


@dataclass(frozen=True)
class SpanOptions:
    """Configure which regions are protected from prose transforms."""

    protect_all_fenced_code: bool = True
    fenced_code_langs: frozenset[str] = PROTECTED_FENCE_LANGS
    include_html_comments: bool = True
    include_headings: bool = False
    include_md_links: bool = False
    include_tagged_bold: bool = False
    include_urls: bool = False
    include_yaml_front_matter: bool = True
    include_latex_envs: bool = True
    include_display_math: bool = True
    include_inline_math: bool = True
    include_inline_code: bool = True


DEFAULT_SPAN_OPTIONS = SpanOptions()
TYPOGRAPHY_SPAN_OPTIONS = SpanOptions(
    protect_all_fenced_code=True,
    include_html_comments=True,
)
GLOSSARY_FIRST_USE_SPAN_OPTIONS = SpanOptions(
    protect_all_fenced_code=True,
    include_html_comments=True,
    include_headings=True,
    include_md_links=True,
    include_tagged_bold=True,
)
AMERICAN_ENGLISH_SPAN_OPTIONS = SpanOptions(
    protect_all_fenced_code=False,
    include_html_comments=False,
    include_urls=True,
)
GREEK_PROSE_SPAN_OPTIONS = SpanOptions(
    protect_all_fenced_code=True,
    include_html_comments=False,
    include_latex_envs=True,
    include_inline_code=True,
    include_display_math=True,
    include_inline_math=False,
)


def protected_spans(text: str, *, options: SpanOptions | None = None) -> list[tuple[int, int]]:
    """Return sorted (start, end) spans that must not be rewritten."""
    opts = options or DEFAULT_SPAN_OPTIONS
    spans: list[tuple[int, int]] = []

    if opts.protect_all_fenced_code or opts.fenced_code_langs:
        for match in _FENCED_CODE.finditer(text):
            lang = match.group(1).strip().lower()
            if opts.protect_all_fenced_code or lang in opts.fenced_code_langs:
                spans.append(match.span())

    if opts.include_html_comments:
        for match in _HTML_COMMENT.finditer(text):
            spans.append(match.span())

    if opts.include_latex_envs:
        for match in _LATEX_ENV.finditer(text):
            spans.append(match.span())
        for env in ("equation", "align", "gather", "multline", "figure", "table"):
            for match in re.finditer(
                rf"\\begin\{{{env}\*?\}}.*?\\end\{{{env}\*?\}}", text, re.DOTALL
            ):
                spans.append(match.span())

    if opts.include_display_math:
        for match in _DISPLAY_MATH.finditer(text):
            spans.append(match.span())

    if opts.include_inline_math:
        for match in _INLINE_MATH.finditer(text):
            spans.append(match.span())

    if opts.include_inline_code:
        for match in _INLINE_CODE.finditer(text):
            spans.append(match.span())

    if opts.include_headings:
        for match in _HEADING.finditer(text):
            spans.append(match.span())

    if opts.include_md_links:
        for match in _MD_LINK.finditer(text):
            spans.append(match.span())

    if opts.include_tagged_bold:
        for match in _TAGGED_BOLD.finditer(text):
            spans.append(match.span())

    if opts.include_urls:
        for match in _URL.finditer(text):
            spans.append(match.span())

    if opts.include_yaml_front_matter:
        front_matter = _YAML_FRONT.match(text)
        if front_matter:
            spans.append(front_matter.span())

    return sorted(spans)


def in_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    """Return True when ``pos`` falls inside any protected span."""
    for start, end in spans:
        if start <= pos < end:
            return True
        if start > pos:
            return False
    return False


__all__ = [
    "AMERICAN_ENGLISH_SPAN_OPTIONS",
    "DEFAULT_SPAN_OPTIONS",
    "GLOSSARY_FIRST_USE_SPAN_OPTIONS",
    "GREEK_PROSE_SPAN_OPTIONS",
    "PROTECTED_FENCE_LANGS",
    "SpanOptions",
    "TYPOGRAPHY_SPAN_OPTIONS",
    "in_protected",
    "protected_spans",
]
