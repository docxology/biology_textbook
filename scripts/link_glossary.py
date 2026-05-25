#!/usr/bin/env python3
"""Normalize anchors and semantic cross-references in the master glossary.

For every bolded term in ``manuscript/glossary.md`` this script:

1. Normalises Pandoc bracketed-span anchors ``[**Term**]{#gl:term-slug}`` (required for PDF
   ``\\label{gl:...}``) so chapters can link with ``[**term**](#gl:term-slug)``.
2. Rewrites legacy ``→ Chapter N`` / ``→ Ch N`` back-references into
   semantic ``\\cref{sec:...}`` labels derived from ``biology.toc``.
3. Checks that all manuscript ``#gl:*`` links resolve to glossary anchors.

The script is idempotent and safe to re-run. Pass ``--dry-run`` to preview
changes without writing, or ``--check`` to fail if changes are pending.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]

GLOSSARY = PROJECT / "manuscript" / "glossary.md"
INDEX = PROJECT / "manuscript" / "appendices" / "appendix_index.md"


# Bracketed span: [**Term**]{#gl:slug} — Pandoc `markdown+bracketed_spans` emits
# `\label{gl:slug}{...}`. (Plain `**Term**{#gl:...}` is not supported as an attribute
# on strong text and is escaped in TeX output.)
_TERM_RE = re.compile(
    r"^\[\*\*(?P<term>[^*]+?)\*\*\]"               # [**Bold term**]
    r"(?P<anchor>\{#gl:[^}]+\})"                    # {#gl:slug} (required in glossary)
    r"(?P<body>.*)$",                               # rest of line
)
_GLOSSARY_CHAPTER_REF_RE = re.compile(r"→\s*Chapters?\s+(?P<refs>[0-9][0-9.,\s]*)")
_INDEX_CHAPTER_REF_RE = re.compile(r"→\s*Ch\s+(?P<refs>[0-9][0-9.,\s]*(?:,\s*Ch\s+[0-9][0-9.,\s]*)*)")
_CREF_CH_TAIL_RE = re.compile(
    r"\\cref\{(?P<labels>[^}]+)\}(?P<tail>(?:\s*,?\s*Ch\s+[0-9]+(?:\.[0-9]+)?)+)"
)
_HARD_CODED_BACKREF_RE = re.compile(r"→\s*(?:Chapters?|Ch)\s+[0-9]")
_CREF_RE = re.compile(r"\\cref\{(?P<labels>[^}]+)\}")
_GLOSSARY_LINK_RE = re.compile(r"\]\(#(?P<slug>gl:[A-Za-z0-9_-]+)\)")
_GLOSSARY_ANCHOR_RE = re.compile(r"\{#(?P<slug>gl:[A-Za-z0-9_-]+)\}")


def _manuscript_markdown_files() -> list[Path]:
    return [
        path
        for path in sorted((PROJECT / "manuscript").rglob("*.md"))
        if path.name not in {"README.md", "AGENTS.md"}
    ]


def _slug(term: str) -> str:
    s = term.lower()
    s = re.sub(r"\s*\([^)]*\)", "", s)        # drop (parenthetical)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "term"


def _chapter_ref_map() -> dict[str, str]:
    """Return legacy display numbers mapped to canonical section labels."""
    from biology.toc import load_toc

    book_toc = load_toc(PROJECT)
    refs: dict[str, str] = {}
    for chapter in book_toc.chapters:
        refs[chapter.companion_number] = chapter.section_label
        if chapter.meta.number > 0:
            refs[str(chapter.meta.number)] = chapter.section_label
    return refs


def _split_ref_tokens(raw: str) -> list[str]:
    """Extract chapter display tokens from old prose back-reference text."""
    return re.findall(r"\d+(?:\.\d+)?", raw)


def _format_cref(labels: list[str]) -> str:
    return f"→ \\cref{{{','.join(labels)}}}"


def _merge_cref_ch_tail(line: str, ref_map: dict[str, str]) -> tuple[str, int, list[str]]:
    """Merge stale ``\\cref{...}Ch N`` tails into the existing semantic ref."""
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
    """Rewrite legacy chapter back-references in one line."""
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


def collect_glossary_anchors(text: str | None = None) -> set[str]:
    """Return all ``gl:*`` anchors declared in the master glossary."""
    source = text if text is not None else GLOSSARY.read_text(encoding="utf-8")
    return set(_GLOSSARY_ANCHOR_RE.findall(source))


def find_duplicate_glossary_anchors(text: str | None = None) -> dict[str, int]:
    """Return glossary anchors declared more than once."""
    source = text if text is not None else GLOSSARY.read_text(encoding="utf-8")
    counts: dict[str, int] = {}
    for slug in _GLOSSARY_ANCHOR_RE.findall(source):
        counts[slug] = counts.get(slug, 0) + 1
    return {slug: count for slug, count in sorted(counts.items()) if count > 1}


def collect_manuscript_glossary_links() -> dict[str, list[str]]:
    """Return ``gl:*`` links used across renderable Markdown files."""
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
    """Return manuscript glossary links with no matching glossary anchor."""
    anchors = collect_glossary_anchors()
    links = collect_manuscript_glossary_links()
    return {slug: locations for slug, locations in sorted(links.items()) if slug not in anchors}


def _validate_cref_labels(texts: list[tuple[Path, str]], ref_map: dict[str, str]) -> list[str]:
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


def _rewrite_glossary(text: str, ref_map: dict[str, str]) -> tuple[str, int, int, list[str]]:
    new_lines: list[str] = []
    anchors_touched = 0
    refs_rewritten = 0
    bad_refs: list[str] = []

    for line in text.splitlines():
        match = _TERM_RE.match(line)
        if not match:
            new_lines.append(line)
            continue

        term = match.group("term").strip()
        anchor = (match.group("anchor") or "").strip()
        body = match.group("body")

        slug = _slug(term)
        desired_anchor = f"{{#gl:{slug}}}"
        body, n_rewrites, bad = _rewrite_backrefs(body, _GLOSSARY_CHAPTER_REF_RE, ref_map)
        refs_rewritten += n_rewrites
        bad_refs.extend(f"{term}: {token}" for token in bad)

        new_line = f"[**{term}**]{desired_anchor}{body}"
        if anchor != desired_anchor:
            anchors_touched += 1
        new_lines.append(new_line)

    out = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
    return out, anchors_touched, refs_rewritten, bad_refs


def _rewrite_index(text: str, ref_map: dict[str, str]) -> tuple[str, int, list[str]]:
    lines: list[str] = []
    refs_rewritten = 0
    bad_refs: list[str] = []
    for line in text.splitlines():
        line, n_rewrites, bad = _rewrite_backrefs(line, _INDEX_CHAPTER_REF_RE, ref_map)
        refs_rewritten += n_rewrites
        bad_refs.extend(f"appendix_index.md: {token}" for token in bad)
        line, n_tail_rewrites, bad_tail = _merge_cref_ch_tail(line, ref_map)
        refs_rewritten += n_tail_rewrites
        bad_refs.extend(f"appendix_index.md: {token}" for token in bad_tail)
        line = line.replace(
            "**Term** (gl:slug) → Ch N, Ch M, Ch K",
            "**Term** (`#gl:slug`) with semantic chapter links",
        )
        line = line.replace(
            "This index is generated by `scripts/build_index.py` from the glossary file. "
            "To regenerate after editing `glossary.md`, run `uv run python scripts/build_index.py`.",
            "This index is maintained by `scripts/link_glossary.py` from the glossary file and canonical ToC labels. "
            "To verify after editing `glossary.md`, run `uv run python scripts/link_glossary.py --check`.",
        )
        lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), refs_rewritten, bad_refs


def run(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    ref_map = _chapter_ref_map()
    glossary_text = GLOSSARY.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    glossary_out, anchors_updated, glossary_refs_rewritten, bad_chapter_refs = _rewrite_glossary(
        glossary_text, ref_map
    )
    index_out, index_refs_rewritten, bad_index_refs = _rewrite_index(index_text, ref_map)
    bad_chapter_refs.extend(bad_index_refs)

    pending_changes = (glossary_out != glossary_text) or (index_out != index_text)
    if pending_changes and not args.dry_run and not args.check:
        write_text_atomic(GLOSSARY, glossary_out)
        if INDEX.exists():
            write_text_atomic(INDEX, index_out)

    duplicate_anchors = find_duplicate_glossary_anchors(glossary_out)
    hardcoded = [
        f"{path.relative_to(PROJECT)}:{line_no}: {line.strip()}"
        for path, source in ((GLOSSARY, glossary_out), (INDEX, index_out))
        for line_no, line in enumerate(source.splitlines(), start=1)
        if _HARD_CODED_BACKREF_RE.search(line)
    ]
    dangling_links = find_dangling_glossary_links()
    bad_crefs = _validate_cref_labels([(GLOSSARY, glossary_out), (INDEX, index_out)], ref_map)

    if args.check:
        mode = "CHECK"
    elif args.dry_run:
        mode = "DRY RUN"
    else:
        mode = "APPLIED"
    print(
        f"[{mode}] anchors_updated={anchors_updated} "
        f"glossary_refs_rewritten={glossary_refs_rewritten} "
        f"index_refs_rewritten={index_refs_rewritten} "
        f"pending_changes={int(pending_changes)}"
    )
    if args.check and pending_changes:
        print("  pending glossary/index normalization changes", file=sys.stderr)
    if bad_chapter_refs:
        print(f"  unresolved chapter refs found ({len(bad_chapter_refs)}, sample):", file=sys.stderr)
        for s in bad_chapter_refs[:10]:
            print(f"    {s}", file=sys.stderr)
    if duplicate_anchors:
        print(f"  duplicate glossary anchors found ({len(duplicate_anchors)}):", file=sys.stderr)
        for slug, count in list(duplicate_anchors.items())[:10]:
            print(f"    {slug}: {count}", file=sys.stderr)
    if hardcoded:
        print(f"  hard-coded chapter back-refs found ({len(hardcoded)}, sample):", file=sys.stderr)
        for line in hardcoded[:10]:
            print(f"    {line}", file=sys.stderr)
    if dangling_links:
        print(f"  dangling glossary links found ({len(dangling_links)} terms):", file=sys.stderr)
        for slug, locations in list(dangling_links.items())[:10]:
            print(f"    {slug}: {', '.join(locations[:5])}", file=sys.stderr)
    if bad_crefs:
        print(f"  unresolved semantic chapter labels found ({len(bad_crefs)}, sample):", file=sys.stderr)
        for line in bad_crefs[:10]:
            print(f"    {line}", file=sys.stderr)

    failed = (
        (args.check and pending_changes)
        or bool(bad_chapter_refs)
        or bool(duplicate_anchors)
        or bool(hardcoded)
        or bool(dangling_links)
        or bool(bad_crefs)
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(run())
