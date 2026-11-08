"""Position-preserving visibility for rendered manuscript cross-references."""

from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass

_FENCE_START = re.compile(r" {0,3}(`{3,}|~{3,})([^\n]*)")


def _mask(text: str) -> str:
    return re.sub(r"[^\n]", " ", text)


def visible_text(
    text: str, *, keep_comments: tuple[str, ...] = ("SOLUTION",), keep_raw_latex: bool = True,
    keep_inline_code: bool = False,
) -> str:
    """Hide examples/comments, retaining raw LaTeX and instructor solutions.

    SOLUTION comments are deliberate instructor-edition content, not ordinary
    HTML comments. Raw ``{=latex}``/``{=tex}`` fences also render. Reference scans
    hide pedagogical inline/fenced code by default; Markdown-structure readers
    retain inline code because it can be a legitimate heading title. Source
    character positions are retained in either view.
    """
    parts: list[str] = []
    fence: str | None = None
    raw = False
    kept_starts = [
        re.compile(r"<!--\s*" + re.escape(name) + r"(?=\s|:|$)")
        for name in keep_comments
    ]
    position = 0
    while position < len(text):
        at_line_start = position == 0 or text[position - 1] == "\n"
        if fence is not None:
            end = text.find("\n", position)
            end = len(text) if end < 0 else end + 1
            line = text[position:end]
            closing = re.fullmatch(r" {0,3}([`~]+)[ \t\r\n]*", line)
            if closing and set(closing.group(1)) == {fence[0]} and len(closing.group(1)) >= len(fence):
                fence = None
                parts.append(_mask(line))
            else:
                parts.append(line if raw else _mask(line))
            position = end
            continue
        if at_line_start:
            marker = _FENCE_START.match(text, position)
            if marker:
                fence = marker.group(1)
                raw = keep_raw_latex and marker.group(2).strip() in {"{=latex}", "{=tex}"}
                end = marker.end()
                if end < len(text) and text[end] == "\n":
                    end += 1
                parts.append(_mask(text[position:end]))
                position = end
                continue
        # Recognize the first actual construct, not independent regex passes:
        # comment contents cannot open fences, and code contents cannot open comments.
        if text.startswith("<!--", position):
            kept = any(pattern.match(text, position) for pattern in kept_starts)
            if kept:
                # The wrapper stays available to instructor/assessment consumers;
                # its body is scanned as rendered prose, including code exclusions.
                parts.append("<!--")
                position += 4
            else:
                end = text.find("-->", position + 4)
                end = len(text) if end < 0 else end + 3
                parts.append(_mask(text[position:end]))
                position = end
            continue
        if text[position] == "`":
            end = position + 1
            while end < len(text) and text[end] == "`":
                end += 1
            line_end = text.find("\n", end)
            line_end = len(text) if line_end < 0 else line_end
            delimiter = re.escape(text[position:end])
            closing = re.search(r"(?<!`)" + delimiter + r"(?!`)", text[end:line_end])
            if closing:
                end += closing.end()
                parts.append(text[position:end] if keep_inline_code else _mask(text[position:end]))
            else:
                parts.append(text[position:end])
            position = end
            continue
        parts.append(text[position])
        position += 1
    visible = "".join(parts)
    return re.sub(r"(?m)^[ \t]*%[^\n]*|(?<=})[ \t]*%[^\n]*", lambda m: _mask(m.group()), visible)


@dataclass(frozen=True)
class MarkdownHeading:
    """One real ATX heading, with source-preserving character boundaries."""

    start: int
    end: int
    line_no: int
    level: int
    indent: str
    title: str
    visible_title: str


_YAML_FRONT = re.compile(r"\A---[ \t]*\n.*?\n(?:---|\.\.\.)[ \t]*(?:\n|$)", re.DOTALL)
_ATX_HEADING = re.compile(r"(?P<indent> {0,3})(?P<hashes>#{1,6})(?:[ \t]+|$)(?P<title>.*)")
_CLOSING_HASHES = re.compile(r"(?:[ \t]+|^)#+[ \t]*$")
_HEADING_ATTRIBUTES = re.compile(r"[ \t]+\{[^}\n]*\}[ \t]*$")


def _heading_title(title: str) -> str:
    title = title.rstrip()
    attributes = _HEADING_ATTRIBUTES.search(title)
    suffix = attributes.group(0) if attributes is not None else ""
    body = title[:attributes.start()] if attributes is not None else title
    return (_CLOSING_HASHES.sub("", body).rstrip() + suffix).strip()


def markdown_text(text: str, *, keep_comments: tuple[str, ...] = ("SOLUTION",)) -> str:
    """Expose Markdown structure, not YAML or raw-TeX/fenced literal headings."""
    front = _YAML_FRONT.match(text)
    if front is not None:
        text = _mask(text[:front.end()]) + text[front.end():]
    return visible_text(text, keep_comments=keep_comments, keep_raw_latex=False, keep_inline_code=True)


def iter_headings(text: str) -> Iterator[MarkdownHeading]:
    """Read ATX headings without promoting tags, examples, or seven-hash prose."""
    position = 0
    for line_no, line in enumerate(markdown_text(text).split("\n"), start=1):
        visible_line = line.removesuffix("\r")
        match = _ATX_HEADING.fullmatch(visible_line)
        if match is not None:
            original_line = text[position:position + len(visible_line)]
            original = _ATX_HEADING.fullmatch(original_line)
            if original is not None:
                yield MarkdownHeading(
                    start=position, end=position + len(visible_line), line_no=line_no,
                    level=len(original.group("hashes")), indent=original.group("indent"),
                    title=_heading_title(original.group("title")),
                    visible_title=_heading_title(match.group("title")),
                )
        position += len(line) + 1


__all__ = ["MarkdownHeading", "iter_headings", "markdown_text", "visible_text"]
