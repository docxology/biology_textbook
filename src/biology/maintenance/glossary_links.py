"""Glossary anchor normalization and appendix index generation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from biology.maintenance.models import PROJECT

GLOSSARY = PROJECT / "docs" / "manuscript" / "glossary.md"
INDEX = PROJECT / "docs" / "manuscript" / "appendices" / "appendix_index.md"

from biology.maintenance.glossary_cards import GLOSSARY_TERM_LINE_RE
_GLOSSARY_CHAPTER_REF_RE = re.compile(r"→\s*Chapters?\s+(?P<refs>[0-9][0-9.,\s]*)")
_INDEX_CHAPTER_REF_RE = re.compile(r"→\s*Ch\s+(?P<refs>[0-9][0-9.,\s]*(?:,\s*Ch\s+[0-9][0-9.,\s]*)*)")
_CREF_CH_TAIL_RE = re.compile(
    r"\\cref\{(?P<labels>[^}]+)\}(?P<tail>(?:\s*,?\s*Ch\s+[0-9]+(?:\.[0-9]+)?)+)"
)
_HARD_CODED_BACKREF_RE = re.compile(r"→\s*(?:Chapters?|Ch)\s+[0-9]")
_CREF_RE = re.compile(r"\\cref\{(?P<labels>[^}]+)\}")
_GLOSSARY_LINK_RE = re.compile(r"\]\(#(?P<slug>gl:[A-Za-z0-9_-]+)\)")
_GLOSSARY_ANCHOR_RE = re.compile(r"\{#(?P<slug>gl:[A-Za-z0-9_-]+)\}")


@dataclass(frozen=True)
class GlossaryIndexEntry:
    """One row in the generated appendix index."""

    term: str
    slug: str
    backref: str


def _manuscript_markdown_files() -> list[Path]:
    return [
        path
        for path in sorted((PROJECT / "docs" / "manuscript").rglob("*.md"))
        if path.name not in {"README.md", "AGENTS.md"}
    ]


def slug_from_term(term: str) -> str:
    """Return the canonical ``gl:`` slug for a glossary term."""
    s = term.lower()
    s = re.sub(r"\s*\([^)]*\)", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "term"


def _chapter_ref_map() -> dict[str, str]:
    from biology.toc import load_toc

    book_toc = load_toc(PROJECT)
    refs: dict[str, str] = {}
    for chapter in book_toc.chapters:
        refs[chapter.companion_number] = chapter.section_label
        if chapter.meta.number > 0:
            refs[str(chapter.meta.number)] = chapter.section_label
    return refs


def _split_ref_tokens(raw: str) -> list[str]:
    return re.findall(r"\d+(?:\.\d+)?", raw)


def _format_cref(labels: list[str]) -> str:
    return f"→ \\cref{{{','.join(labels)}}}"


def _merge_cref_ch_tail(line: str, ref_map: dict[str, str]) -> tuple[str, int, list[str]]:
    bad_refs: list[str] = []
    rewrites = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal rewrites
        labels = [label.strip() for label in match.group("labels").split(",") if label.strip()]
        for token in _split_ref_tokens(match.group("tail")):
            label = ref_map.get(token)
            if label is None:
                bad_refs.append(token)
                continue
            if label not in labels:
                labels.append(label)
        rewrites += 1
        return f"\\cref{{{','.join(labels)}}}"

    return _CREF_CH_TAIL_RE.sub(replace, line), rewrites, bad_refs


def _rewrite_backrefs(
    line: str,
    pattern: re.Pattern[str],
    ref_map: dict[str, str],
) -> tuple[str, int, list[str]]:
    bad_refs: list[str] = []
    rewrites = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal rewrites
        labels: list[str] = []
        for token in _split_ref_tokens(match.group("refs")):
            label = ref_map.get(token)
            if label is None:
                bad_refs.append(token)
                return match.group(0)
            labels.append(label)
        if not labels:
            return match.group(0)
        replacement = _format_cref(labels)
        if replacement != match.group(0):
            rewrites += 1
        return replacement

    return pattern.sub(replace, line), rewrites, bad_refs


def parse_glossary_index_entries(glossary_text: str) -> list[GlossaryIndexEntry]:
    """Parse glossary lines into appendix index rows."""
    entries: list[GlossaryIndexEntry] = []
    for line in glossary_text.splitlines():
        match = GLOSSARY_TERM_LINE_RE.match(line)
        if not match:
            continue
        term = match.group("term").strip()
        anchor = match.group("anchor").strip()
        slug_match = _GLOSSARY_ANCHOR_RE.search(anchor)
        slug = slug_match.group("slug") if slug_match else f"gl:{slug_from_term(term)}"
        body = match.group("body")
        cref_match = _CREF_RE.search(body)
        backref = f"→ \\cref{{{cref_match.group(1)}}}" if cref_match else ""
        entries.append(GlossaryIndexEntry(term=term, slug=slug, backref=backref))
    return sorted(entries, key=lambda item: item.term.casefold())


def build_appendix_index(glossary_text: str) -> str:
    """Rebuild ``appendix_index.md`` from normalized glossary content."""
    entries = parse_glossary_index_entries(glossary_text)
    count = len(entries)
    lines = [
        "# Appendix G — Index of Key Terms {#sec:appendix_index .unnumbered}",
        "",
        "",
        "<!-- chapter-metadata-badge -->",
        "> **Appendix G** · Level 1/3 · Use as reference",
        "",
        f"An index of the {count} glossary terms, each with the chapter(s) where the term is "
        "introduced, bolded, or discussed at length. Terms marked in **bold** appear as section "
        "headings somewhere in the textbook; the glossary entry carries the full definition.",
        "",
        "Each entry follows the pattern:",
        "",
        "```",
        "**Term** (`#gl:slug`) with semantic chapter links",
        "```",
        "",
        "The `#gl:slug` anchor is the canonical location defined in the master glossary "
        "(`manuscript/glossary.md`). Full-text search for the slug string finds every cross-reference.",
        "",
        "> **Note on maintenance.** This index is maintained by `scripts/link_glossary.py` from the "
        "glossary file and canonical ToC labels. To verify after editing `glossary.md`, run "
        "`uv run python scripts/link_glossary.py --check`.",
        "",
        "---",
        "",
    ]
    current_letter = ""
    for entry in entries:
        letter = entry.term[0].upper() if entry.term else "#"
        if not letter.isalpha():
            letter = "#"
        if letter != current_letter:
            if current_letter:
                lines.append("")
            lines.append(f"## {letter} {{.unnumbered}}")
            lines.append("")
            current_letter = letter
        cref_part = f" {entry.backref}" if entry.backref else ""
        lines.append(f"**{entry.term}** (`#{entry.slug}`){cref_part}")
    lines.extend(
        [
            "",
            "---",
            "",
            "> **Using the index.** When a term appears as a bolded, `#gl:`-linked first use in a "
            "chapter (see \\nameref{sec:unit_I_unit_intro} onward), clicking the term jumps to the "
            "canonical entry in the master glossary. This appendix provides an author- and "
            "instructor-facing overview of which chapter establishes each concept first, useful "
            "for lecture planning and term-by-term syllabus design.",
            "",
            "*Module: reference only (no code)*",
            "",
        ]
    )
    return "\n".join(lines)


def collect_glossary_anchors(text: str | None = None) -> set[str]:
    source = text if text is not None else GLOSSARY.read_text(encoding="utf-8")
    return set(_GLOSSARY_ANCHOR_RE.findall(source))


def find_duplicate_glossary_anchors(text: str | None = None) -> dict[str, int]:
    source = text if text is not None else GLOSSARY.read_text(encoding="utf-8")
    counts: dict[str, int] = {}
    for slug in _GLOSSARY_ANCHOR_RE.findall(source):
        counts[slug] = counts.get(slug, 0) + 1
    return {slug: count for slug, count in sorted(counts.items()) if count > 1}


def collect_manuscript_glossary_links() -> dict[str, list[str]]:
    links: dict[str, list[str]] = {}
    for path in _manuscript_markdown_files():
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in _GLOSSARY_LINK_RE.finditer(line):
                links.setdefault(match.group("slug"), []).append(
                    f"{path.relative_to(PROJECT / 'manuscript')}:{line_no}"
                )
    return links


def find_dangling_glossary_links() -> dict[str, list[str]]:
    anchors = collect_glossary_anchors()
    links = collect_manuscript_glossary_links()
    return {slug: locations for slug, locations in sorted(links.items()) if slug not in anchors}


def validate_cref_labels(texts: list[tuple[Path, str]], ref_map: dict[str, str]) -> list[str]:
    known_labels = set(ref_map.values())
    bad: list[str] = []
    for path, text in texts:
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in _CREF_RE.finditer(line):
                for label in match.group("labels").split(","):
                    label = label.strip()
                    if label.startswith("sec:") and label not in known_labels:
                        bad.append(f"{path.relative_to(PROJECT)}:{line_no}: {label}")
    return bad


def rewrite_glossary(text: str, ref_map: dict[str, str]) -> tuple[str, int, int, list[str]]:
    new_lines: list[str] = []
    anchors_touched = 0
    refs_rewritten = 0
    bad_refs: list[str] = []

    for line in text.splitlines():
        match = GLOSSARY_TERM_LINE_RE.match(line)
        if not match:
            new_lines.append(line)
            continue

        term = match.group("term").strip()
        anchor = (match.group("anchor") or "").strip()
        body = match.group("body")

        desired_anchor = f"{{#gl:{slug_from_term(term)}}}"
        body, n_rewrites, bad = _rewrite_backrefs(body, _GLOSSARY_CHAPTER_REF_RE, ref_map)
        refs_rewritten += n_rewrites
        bad_refs.extend(f"{term}: {token}" for token in bad)

        new_line = f"[**{term}**]{desired_anchor}{body}"
        if anchor != desired_anchor:
            anchors_touched += 1
        new_lines.append(new_line)

    out = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
    return out, anchors_touched, refs_rewritten, bad_refs


def glossary_term_count(glossary_text: str) -> int:
    """Return the number of glossary entries with ``{#gl:…}`` anchors."""
    return len(parse_glossary_index_entries(glossary_text))


def run_glossary_sync(*, dry_run: bool = False, check: bool = False) -> tuple[int, dict[str, int | bool]]:
    """Normalize glossary anchors and rebuild the appendix index."""
    from textbook_io import write_text_atomic

    ref_map = _chapter_ref_map()
    glossary_text = GLOSSARY.read_text(encoding="utf-8")
    glossary_out, anchors_updated, glossary_refs_rewritten, bad_chapter_refs = rewrite_glossary(
        glossary_text, ref_map
    )
    index_out = build_appendix_index(glossary_out)
    pending_changes = (glossary_out != glossary_text) or (
        not INDEX.exists() or INDEX.read_text(encoding="utf-8") != index_out
    )

    if pending_changes and not dry_run and not check:
        write_text_atomic(GLOSSARY, glossary_out)
        write_text_atomic(INDEX, index_out)

    duplicate_anchors = find_duplicate_glossary_anchors(glossary_out)
    hardcoded = [
        f"{path.relative_to(PROJECT)}:{line_no}: {line.strip()}"
        for path, source in ((GLOSSARY, glossary_out), (INDEX, index_out))
        for line_no, line in enumerate(source.splitlines(), start=1)
        if _HARD_CODED_BACKREF_RE.search(line)
    ]
    dangling_links = find_dangling_glossary_links()
    bad_crefs = validate_cref_labels([(GLOSSARY, glossary_out), (INDEX, index_out)], ref_map)

    failed = (
        (check and pending_changes)
        or bool(bad_chapter_refs)
        or bool(duplicate_anchors)
        or bool(hardcoded)
        or bool(dangling_links)
        or bool(bad_crefs)
    )
    stats: dict[str, int | bool] = {
        "anchors_updated": anchors_updated,
        "glossary_refs_rewritten": glossary_refs_rewritten,
        "index_terms": glossary_term_count(glossary_out),
        "pending_changes": pending_changes,
        "failed": failed,
    }
    return (1 if failed else 0), stats


__all__ = [
    "GLOSSARY",
    "INDEX",
    "GlossaryIndexEntry",
    "build_appendix_index",
    "collect_glossary_anchors",
    "find_dangling_glossary_links",
    "find_duplicate_glossary_anchors",
    "glossary_term_count",
    "parse_glossary_index_entries",
    "run_glossary_sync",
    "slug_from_term",
]
