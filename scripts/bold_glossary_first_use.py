#!/usr/bin/env python3
"""Bold + link each glossary term on first use in every chapter.

For each term defined in ``manuscript/glossary.md`` as
``[**Term**]{#gl:slug}`` (bracketed span so Pandoc emits
``\\label{gl:...}``), this script finds the first case-insensitive occurrence
in each chapter and rewrites it as ``[**Term**](#gl:slug)``.

Only the *first* use is linked. Subsequent occurrences are left alone so
the prose doesn't become a sea of hyperlinks. The script skips:

* fenced code / mermaid blocks (``\\`\\`\\``` … ``\\`\\`\\```)
* inline code spans (`\\`term\\``)
* raw-LaTeX environments (``\\begin{…}…\\end{…}``)
* LaTeX display math (``$$…$$``) and inline math (``$…$``)
* markdown headings (lines starting with ``#``)
* existing markdown links (no nesting)
* HTML comments (``<!-- … -->``)

Idempotent: if a term is already bolded+linked to its ``#gl:`` anchor on
its first occurrence, the file is unchanged.

Run ``uv run python scripts/bold_glossary_first_use.py`` (or with
``--dry-run``).
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
GLOSSARY = MANUSCRIPT / "glossary.md"


@dataclass(frozen=True)
class Term:
    term: str        # canonical display form (as written in glossary)
    slug: str        # glossary anchor slug (without `gl:`)


_GLOSSARY_LINE = re.compile(
    r"^\[\*\*(?P<term>[^*]+)\*\*\]\{#gl:(?P<slug>[^}]+)\}"
)


def load_terms() -> list[Term]:
    """Parse the glossary and return every ``Term(term, slug)``."""
    terms: list[Term] = []
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        m = _GLOSSARY_LINE.match(line)
        if not m:
            continue
        terms.append(Term(term=m.group("term").strip(), slug=m.group("slug").strip()))
    # Longest term first so "Action potential" matches before "action" would.
    return sorted(terms, key=lambda t: -len(t.term))


# ---------------------------------------------------------------------------
# Protected-range scanner
# ---------------------------------------------------------------------------

_FENCED_CODE = re.compile(r"```[a-zA-Z0-9_+-]*\n.*?\n```", re.DOTALL)
_INLINE_CODE = re.compile(r"`[^`\n]+`")
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_LATEX_ENV = re.compile(
    r"\\begin\{(?P<e>[A-Za-z]+\*?)\}.*?\\end\{(?P=e)\}", re.DOTALL
)
_DISPLAY_MATH = re.compile(r"\$\$.*?\$\$", re.DOTALL)
_INLINE_MATH = re.compile(r"(?<!\$)\$[^$\n]+\$")
_HEADING = re.compile(r"(?m)^#{1,6} .*$")
_MD_LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
# Glossary-tagged terms in text: [**](…){#} or legacy **…** {#} (do not re-wrap)
_TAGGED_BOLD = re.compile(
    r"(?:\[\*\*[^*]+\*\*\]|\*\*[^*]+\*\*)\s*\{#[^}]+\}"
)
_YAML_FRONT = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def protected_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for pat in (_FENCED_CODE, _HTML_COMMENT, _LATEX_ENV, _DISPLAY_MATH,
                _INLINE_MATH, _INLINE_CODE, _HEADING, _MD_LINK, _TAGGED_BOLD):
        for m in pat.finditer(text):
            spans.append(m.span())
    fm = _YAML_FRONT.match(text)
    if fm:
        spans.append(fm.span())
    return sorted(spans)


def in_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    for s, e in spans:
        if s <= pos < e:
            return True
        if s > pos:
            return False
    return False


# ---------------------------------------------------------------------------
# Per-chapter rewrite
# ---------------------------------------------------------------------------

def build_pattern(term: str) -> re.Pattern[str]:
    """Case-insensitive word-boundary pattern matching the term.

    Handles plural ``s`` as an optional suffix so "alleles" matches the term
    "Allele" too. Compound terms (multi-word) require the exact compound.
    """
    escaped = re.escape(term)
    return re.compile(rf"(?<![A-Za-z0-9_])({escaped})(s?)(?![A-Za-z0-9_])", re.IGNORECASE)


def bold_first_use(text: str, terms: list[Term]) -> tuple[str, int]:
    """For every term, replace its first safe occurrence with a bold link.

    Returns (new_text, number_of_replacements).
    """
    # Since replacements change offsets, process terms one at a time and
    # re-scan protected spans after each successful replacement.
    replacements = 0
    for term in terms:
        pattern = build_pattern(term.term)
        spans = protected_spans(text)
        # Idempotency: skip if this gl-anchor is already linked anywhere in the file.
        if f"](#gl:{term.slug})" in text:
            continue
        for m in pattern.finditer(text):
            if in_protected(m.start(), spans):
                continue
            # Preserve original capitalization: if the matched text starts
            # with a lowercase letter, lowercase the display form.
            matched = m.group(1)
            display = term.term
            if matched and matched[0].islower() and display[0].isupper():
                display = display[0].lower() + display[1:]
            suffix = m.group(2) or ""
            replacement = f"[**{display}**](#gl:{term.slug}){suffix}"
            text = text[: m.start()] + replacement + text[m.end():]
            replacements += 1
            break  # first use only
    return text, replacements


def process_file(path: Path, terms: list[Term], dry_run: bool = False) -> int:
    text = path.read_text(encoding="utf-8")
    new_text, n = bold_first_use(text, terms)
    if n and not dry_run:
        write_text_atomic(path, new_text)
    return n


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    terms = load_terms()
    total = 0
    files = 0
    for unit_dir in sorted(MANUSCRIPT.glob("unit_*")):
        for ch in sorted(unit_dir.glob("*.md")):
            if ch.name in {"README.md", "AGENTS.md", "unit_intro.md"}:
                continue
            n = process_file(ch, terms, dry_run=dry_run)
            if n:
                files += 1
                total += n
                print(f"  [{'D' if dry_run else '+'}] {ch.relative_to(MANUSCRIPT)}: {n} terms")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] linked_total={total} files_touched={files} terms={len(terms)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
