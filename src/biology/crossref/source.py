"""Position-preserving visibility for rendered manuscript cross-references."""

from __future__ import annotations

import re

_FENCE_START = re.compile(r" {0,3}(`{3,}|~{3,})([^\n]*)")


def _mask(text: str) -> str:
    return re.sub(r"[^\n]", " ", text)


def visible_text(text: str, *, keep_comments: tuple[str, ...] = ("SOLUTION",)) -> str:
    """Hide examples/comments, retaining raw LaTeX and instructor solutions.

    SOLUTION comments are deliberate instructor-edition content, not ordinary
    HTML comments. Raw ``{=latex}``/``{=tex}`` fences also render; other fences
    and inline code are pedagogical examples and cannot define/use book IDs.
    Character positions and line numbers are retained.
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
                raw = marker.group(2).strip() in {"{=latex}", "{=tex}"}
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
                parts.append(_mask(text[position:end]))
            else:
                parts.append(text[position:end])
            position = end
            continue
        parts.append(text[position])
        position += 1
    visible = "".join(parts)
    return re.sub(r"(?m)^[ \t]*%[^\n]*|(?<=})[ \t]*%[^\n]*", lambda m: _mask(m.group()), visible)


__all__ = ["visible_text"]
