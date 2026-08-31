"""Accessibility tests for the manuscript.

Alt text in ``<!-- alt: ... -->`` comments and adjacent captions is **enforced
here** (pytest), not by the template PDF engine. The policy is **declared** in
``manuscript/config.yaml`` (``accessibility.alt_text_required: true``) for
authors; see ``docs/accessibility.md`` for the full enforcement table.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

MANUSCRIPT = Path(__file__).resolve().parent.parent / "docs" / "manuscript"


def _manuscript_markdown_files() -> list[Path]:
    """Core chapters, labs, and question banks that may include figures or Mermaid."""
    out: list[Path] = []
    out.extend(sorted(MANUSCRIPT.glob("unit_*/*.md")))
    out.extend(sorted(MANUSCRIPT.glob("labs/**/*.md")))
    out.extend(sorted(MANUSCRIPT.glob("questions/**/*.md")))
    return out


def _all_manuscript_markdown_files() -> list[Path]:
    """All renderable manuscript markdown files that can contain inline Mermaid."""
    return [
        p
        for p in sorted(MANUSCRIPT.rglob("*.md"))
        if p.name not in {"AGENTS.md", "README.md"}
    ]


MARKDOWN_PATHS = _manuscript_markdown_files()
ALL_MARKDOWN_PATHS = _all_manuscript_markdown_files()
# Unit directories may contain AGENTS.md / README.md — figures and Mermaid live in chapter .md only
UNIT_CHAPTER_FILES = [
    p for p in sorted(MANUSCRIPT.glob("unit_*/*.md")) if p.name not in ("AGENTS.md", "README.md")
]

_ALT_COMMENT = re.compile(r"<!--\s*alt:", re.IGNORECASE)
# Capture inner text (non-greedy) up to comment close; allow newlines in rare multiline alts
_ALT_BODY = re.compile(
    r"<!--\s*alt:\s*(?P<body>.*?)-->",
    re.DOTALL | re.IGNORECASE,
)
_LATEX_FIG = re.compile(
    r"\\begin\{figure\}.*?\\end\{figure\}",
    re.DOTALL,
)
_MERMAID_BLOCK = re.compile(
    r"^```mermaid\s*\n(.*?)^```\s*$",
    re.DOTALL | re.MULTILINE,
)
_ITALIC_CAPTION = re.compile(r"^\s*\*[^*\n].{6,}[^*\s]\*\s*$", re.MULTILINE)

# Generic placeholder single-word "alts" and weak openers
_BANNED_ALT_PREFIXES = (
    "image of ",
    "picture of ",
    "photo of ",
    "fig ",
    "figure ",
)
_MIN_ALT_LEN = 18
_BANNED_MERMAID_METADATA_FRAGMENTS = (
    "generic agent-based simulation loop",
    "flowchart of c4 carbon fixation pathway showing co2 concentration and spatial separation",
    "flowchart depicting biological process or pathway",
    "network graph showing biological relationships",
    "sequence diagram showing step-by-step molecular or cellular interactions",
    "gene regulatory network showing interactions between transcription factors and target genes",
    "metabolic network diagram showing biochemical pathways and their connections",
    "state diagram showing biological states and transitions",
    "mermaid directed graph summarising a conceptual relationship described in the surrounding text",
    "mermaid sequence diagram summarising a conceptual relationship described in the surrounding text",
    "phylogenetic tree showing evolutionary relationships among taxa",
    "food web network showing trophic interactions",
)


def _alt_texts_from_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [m.group("body").strip() for m in _ALT_BODY.finditer(text)]


def _is_weak_alt(body: str) -> bool:
    b = " ".join(body.split())
    low = b.lower().strip(" .")
    if len(b) < _MIN_ALT_LEN:
        return True
    for prefix in _BANNED_ALT_PREFIXES:
        if low.startswith(prefix):
            return True
    if low in ("diagram", "figure", "chart", "image", "mermaid", "mermaid diagram"):
        return True
    return False


def _immediate_mermaid_metadata(text_after: str) -> tuple[list[str], list[str]]:
    """Return immediate alt comments and captions after a Mermaid fence."""
    alts: list[str] = []
    captions: list[str] = []
    for line in text_after.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        alt = _ALT_BODY.fullmatch(stripped)
        if alt:
            alts.append(alt.group("body").strip())
            continue
        if _ITALIC_CAPTION.fullmatch(stripped):
            captions.append(stripped.strip("*").strip())
            continue
        break
    return alts, captions


def test_global_alt_text_count_meets_threshold() -> None:
    total = 0
    for path in UNIT_CHAPTER_FILES:
        total += len(_ALT_COMMENT.findall(path.read_text(encoding="utf-8")))
    assert total >= 60, (
        f"expected >= 60 alt-text comments across unit chapter files, found {total}"
    )


@pytest.mark.parametrize("path", UNIT_CHAPTER_FILES, ids=lambda p: p.relative_to(MANUSCRIPT).as_posix())
def test_every_latex_figure_has_alt_nearby(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for m in _LATEX_FIG.finditer(text):
        end = m.end()
        window = text[end : end + 500]
        assert _ALT_COMMENT.search(window), (
            f"{path}: figure ending at char {end} lacks <!-- alt: ... --> "
            "comment within 500 chars after \\end{figure}"
        )


@pytest.mark.parametrize("path", UNIT_CHAPTER_FILES, ids=lambda p: p.relative_to(MANUSCRIPT).as_posix())
def test_every_mermaid_block_has_alt_and_caption(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for m in _MERMAID_BLOCK.finditer(text):
        end = m.end()
        alts, captions = _immediate_mermaid_metadata(text[end:])
        has_alt = bool(alts)
        has_italic_caption = bool(captions)
        assert has_alt, f"{path}: mermaid block ending at char {end} lacks alt-text"
        assert has_italic_caption, f"{path}: mermaid block ending at char {end} lacks italic caption"


@pytest.mark.parametrize("path", MARKDOWN_PATHS, ids=lambda p: p.relative_to(MANUSCRIPT).as_posix())
def test_alt_text_body_is_substantive(path: Path) -> None:
    """Reject boilerplate and very short ``<!-- alt: ... -->`` comments."""
    for body in _alt_texts_from_file(path):
        assert not _is_weak_alt(body), (
            f"{path}: alt text is missing detail or is boilerplate: {body!r} "
            f"(minimum length {_MIN_ALT_LEN} after normalizing whitespace; "
            "do not use 'image of…' or a single word like 'diagram')"
        )


def test_mermaid_labs_covered_by_alt_or_caption_contract() -> None:
    """If a lab file includes Mermaid, it must have both metadata forms."""
    for path in sorted(MANUSCRIPT.glob("labs/**/*.md")):
        text = path.read_text(encoding="utf-8")
        if not _MERMAID_BLOCK.search(text):
            continue
        for m in _MERMAID_BLOCK.finditer(text):
            alts, captions = _immediate_mermaid_metadata(text[m.end() :])
            assert alts, f"{path}: mermaid must have <!-- alt: ... --> after block"
            assert captions, f"{path}: mermaid must have italic caption after block"


@pytest.mark.parametrize("path", ALL_MARKDOWN_PATHS, ids=lambda p: p.relative_to(MANUSCRIPT).as_posix())
def test_every_mermaid_block_has_exactly_one_alt_and_caption(path: Path) -> None:
    """Every inline Mermaid block has one alt comment and one italic caption."""
    text = path.read_text(encoding="utf-8")
    for match in _MERMAID_BLOCK.finditer(text):
        alts, captions = _immediate_mermaid_metadata(text[match.end() :])
        line = text[: match.start()].count("\n") + 1
        assert len(alts) == 1, (
            f"{path}:{line}: expected exactly one immediate Mermaid alt comment, found {len(alts)}"
        )
        assert len(captions) == 1, (
            f"{path}:{line}: expected exactly one immediate italic Mermaid caption, found {len(captions)}"
        )


@pytest.mark.parametrize("path", ALL_MARKDOWN_PATHS, ids=lambda p: p.relative_to(MANUSCRIPT).as_posix())
def test_mermaid_alt_and_caption_text_not_generic(path: Path) -> None:
    """Reject stale auto-generated Mermaid metadata that misdescribes diagrams."""
    text = path.read_text(encoding="utf-8")
    for match in _MERMAID_BLOCK.finditer(text):
        alts, captions = _immediate_mermaid_metadata(text[match.end() :])
        line = text[: match.start()].count("\n") + 1
        for value in (*alts, *captions):
            normalized = " ".join(value.lower().split()).strip(" .")
            for fragment in _BANNED_MERMAID_METADATA_FRAGMENTS:
                assert fragment not in normalized, (
                    f"{path}:{line}: Mermaid metadata is generic or stale: {value!r}"
                )
