"""Tests for protected-span scanning."""

from __future__ import annotations

from biology.maintenance.manuscript_spans import (
    GLOSSARY_FIRST_USE_SPAN_OPTIONS,
    TYPOGRAPHY_SPAN_OPTIONS,
    in_protected,
    protected_spans,
)


def test_fenced_code_is_protected() -> None:
    text = "Before\n```python\nx --> y\n```\nAfter --> end"
    spans = protected_spans(text, options=TYPOGRAPHY_SPAN_OPTIONS)
    assert in_protected(text.index("x --> y"), spans)
    assert not in_protected(text.index("After"), spans)


def test_html_comment_is_protected() -> None:
    text = "Prose <!-- keep --> arrow --> here"
    spans = protected_spans(text, options=TYPOGRAPHY_SPAN_OPTIONS)
    assert in_protected(text.index("keep"), spans)
    assert not in_protected(text.index("arrow"), spans)


def test_inline_math_is_protected() -> None:
    text = "Use $x --> y$ but prose --> ok"
    spans = protected_spans(text, options=TYPOGRAPHY_SPAN_OPTIONS)
    assert in_protected(text.index("x --> y"), spans)
    assert not in_protected(text.index("prose"), spans)


def test_glossary_options_protect_headings_and_links() -> None:
    text = "# Heading with allele\n[**Allele**](#gl:allele)\nplain allele"
    spans = protected_spans(text, options=GLOSSARY_FIRST_USE_SPAN_OPTIONS)
    assert in_protected(text.index("# Heading"), spans)
    assert in_protected(text.index("[**Allele**]"), spans)
    assert not in_protected(text.index("plain"), spans)


def test_yaml_front_matter_is_protected() -> None:
    text = "---\ntitle: x --> y\n---\nBody --> ok"
    spans = protected_spans(text, options=TYPOGRAPHY_SPAN_OPTIONS)
    assert in_protected(text.index("title"), spans)
    assert not in_protected(text.index("Body"), spans)
