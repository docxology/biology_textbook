"""Insert chapter-specific source-note sections into configured chapters.

For each chapter that does not already carry a Further Reading or Source Notes
heading, this module:

1. Parses chapter prose for documented natbib citation keys.
2. Parses ``manuscript/references.bib`` for the matching entries.
3. Picks 4-6 references, preferring keys already cited in the chapter so the
   Further Reading list stays self-consistent.
4. Renders the section as ``## Further Reading and Source Notes: <title>``
   and injects it after Review Questions but before the module reference
   footer.

Idempotent: chapters with an existing Further Reading or Source Notes
heading are left untouched. The thin CLI lives at
``scripts/insert_further_reading.py``.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from biology.citations import ordered_citation_keys
from biology.maintenance.models import PROJECT
from biology.toc import load_toc

MANUSCRIPT = PROJECT / "docs" / "manuscript"
BIB = MANUSCRIPT / "references.bib"


class _WriteFn(Protocol):
    def __call__(self, path: Path, text: str) -> None: ...


def _default_writer() -> _WriteFn:
    from textbook_io import write_text_atomic

    return write_text_atomic


# Curated supplementary reading per chapter (citekeys from references.bib).
# Keys must exist in references.bib; paths must match configured chapter files.
SUPPLEMENT: dict[str, list[str]] = {
    "unit_0/systems_science.md": ["bertalanffy1968", "strogatz2018"],
    "unit_0/complex_adaptive_systems.md": ["bak1987", "holland1992", "kauffman1993"],
    "unit_0/active_inference.md": ["friston2010", "friston2017", "sterling2015"],
    "unit_0/history_philosophy_biology.md": ["darwin1858"],
    "unit_I/atoms_molecules.md": ["pauling1932electronegativity", "henderson1913"],
    "unit_I/water_and_life.md": ["henderson1913"],
    "unit_I/macromolecules.md": ["pauling1932electronegativity"],
    "unit_I/enzymes_and_kinetics.md": ["fischer1894", "koshland1958"],
    "unit_II/cell_theory.md": ["hooke1665", "schleiden1838", "schwann1839", "virchow1855"],
    "unit_II/cell_structure.md": ["margulis1967"],
    "unit_II/membrane_transport.md": ["singer1972fluidmosaic", "mitchell1961"],
    "unit_II/cell_signaling.md": ["alon2019", "tyson2003"],
    "unit_III/bioenergetics_and_respiration.md": ["mitchell1961", "atkinson1968"],
    "unit_III/photosynthesis.md": ["calvin1961", "mitchell1961"],
    "unit_III/metabolic_integration.md": ["atkinson1968"],
    "unit_IV/dna_replication_and_cell_cycle.md": ["watson1953", "meselson1958"],
    "unit_IV/gene_expression.md": ["crick1958", "crick1966", "jacob1961"],
    "unit_IV/mutations_and_genomics.md": ["doudna2012", "doudna2014"],
    "unit_IV/chromatin_and_epigenetic_mechanisms.md": ["fire1998"],
    "unit_IV/epigenetic_inheritance_and_disease.md": ["fire1998"],
    "unit_V/mendelian_principles.md": ["mendel1866"],
    "unit_V/mendelian_extensions_and_human_genetics.md": ["mendel1866"],
    "unit_V/chromosomal_inheritance.md": ["morgan1910", "sturtevant1913"],
    "unit_V/population_genetics.md": ["weinberg1908", "wright1931", "kimura1968"],
    "unit_VI/evolution_and_selection.md": ["darwin1858", "dobzhansky1973", "williams1966"],
    "unit_VI/genetic_drift_and_speciation.md": ["mayr1942", "wright1931"],
    "unit_VI/phylogenetics.md": ["woese1977", "zuckerkandl1965", "saitou1987"],
    "unit_VII/bacteria_archaea_viruses.md": ["woese1977", "margulis1967"],
    "unit_VII/microbial_ecology.md": ["woese1977"],
    "unit_VII/host_immunity_and_vaccines.md": ["chaplin2010immuneresponse", "iwasaki2015innateadaptive"],
    "unit_VII/antimicrobial_resistance_and_epidemiology.md": ["who2024bppl", "murray2022amr"],
    "unit_VIII/plant_structure_and_water.md": ["dixon1894"],
    "unit_VIII/plant_reproduction.md": ["darwin1859"],
    "unit_VIII/plant_responses.md": ["darwin1859"],
    "unit_IX/circulation_respiration_homeostasis.md": ["cannon1932", "starling1914"],
    "unit_IX/nervous_system.md": ["sherrington1906", "hodgkin1952quantitative"],
    "unit_IX/action_potential_synapses.md": ["hodgkin1952quantitative", "frey1997"],
    "unit_IX/endocrine_signaling.md": ["cannon1932"],
    "unit_IX/immune_system_defense.md": ["chaplin2010immuneresponse", "medzhitov2007recognition"],
    "unit_X/population_ecology.md": ["lotka1925", "volterra1926", "hutchinson1957"],
    "unit_X/community_interactions.md": ["paine1966", "connell1978", "ehrlich1964", "macarthur1967"],
    "unit_X/biodiversity_and_food_webs.md": ["macarthur1967"],
    "unit_X/ecosystem_ecology.md": ["bormann1967", "odum1953", "levin1998"],
    "unit_X/biomes_and_conservation.md": ["ehrlich1964", "macarthur1967"],
}


@dataclass
class BibEntry:
    """One bibliography record rendered into APA-style prose."""

    key: str
    entry_type: str
    author: str = ""
    year: str = ""
    title: str = ""
    journal: str = ""
    publisher: str = ""
    volume: str = ""
    pages: str = ""

    def pretty(self) -> str:
        """Render the entry as a single APA-style bibliographic line."""
        author_abbrev = self._short_authors()
        parts: list[str] = [f"{author_abbrev} ({self.year})."] if self.year else [f"{author_abbrev}."]
        title = self.title.strip().rstrip(".")
        if self.entry_type.lower() in {"book"}:
            parts.append(f"*{title}*.")
            if self.publisher:
                parts.append(f"{self.publisher}.")
        else:
            parts.append(f"{title}.")
            if self.journal:
                parts.append(f"*{self.journal}*" + (f", {self.volume}" if self.volume else "") + ".")
            elif self.publisher:
                parts.append(f"{self.publisher}.")
        return " ".join(parts)

    def _short_authors(self) -> str:
        raw = self.author.replace("\n", " ").strip()
        names = [n.strip() for n in raw.split(" and ")]
        if not names:
            return "Anon."

        def last(n: str) -> str:
            if "," in n:
                return n.split(",", 1)[0].strip()
            return n.split()[-1] if n.split() else n

        if len(names) == 1:
            return last(names[0])
        if len(names) == 2:
            return f"{last(names[0])} & {last(names[1])}"
        return f"{last(names[0])} et al."


# ---------------------------------------------------------------------------
# Bibliography parsing
# ---------------------------------------------------------------------------

_ENTRY_RE = re.compile(r"@(\w+)\{([^,]+),\s*\n(.*?)^\}", re.DOTALL | re.MULTILINE)
_FIELD_RE = re.compile(r'\s*(\w+)\s*=\s*[{"]((?:[^{}]|\{[^{}]*\})*)[}"]\s*,?', re.DOTALL)
_BIB_FIELDS = {"author", "year", "title", "journal", "publisher", "volume", "pages"}


def parse_bib(bib_path: Path = BIB) -> dict[str, BibEntry]:
    """Parse ``manuscript/references.bib`` into a ``{key: BibEntry}`` mapping."""
    text = bib_path.read_text(encoding="utf-8")
    out: dict[str, BibEntry] = {}
    for entry_match in _ENTRY_RE.finditer(text):
        etype, key, body = entry_match.group(1), entry_match.group(2).strip(), entry_match.group(3)
        entry = BibEntry(key=key, entry_type=etype)
        for field_match in _FIELD_RE.finditer(body):
            name, value = field_match.group(1).lower(), field_match.group(2).strip()
            value = re.sub(r"\s+", " ", value).strip().rstrip(",")
            if name in _BIB_FIELDS:
                setattr(entry, name, value)
        out[key] = entry
    return out


def validate_supplement(*, project_root: Path = PROJECT, bib_path: Path = BIB) -> list[str]:
    """Return issues when supplement paths or citekeys drift from config or bib."""
    issues: list[str] = []
    bib = parse_bib(bib_path)
    toc = load_toc(project_root)
    configured = {f"{chapter.path.parent.name}/{chapter.path.name}" for chapter in toc.chapters}
    for rel, keys in SUPPLEMENT.items():
        if rel not in configured:
            issues.append(f"unknown chapter path in SUPPLEMENT: {rel}")
        for key in keys:
            if key not in bib:
                issues.append(f"unknown citekey {key} in SUPPLEMENT[{rel!r}]")
    return issues


# ---------------------------------------------------------------------------
# Chapter parsing and injection
# ---------------------------------------------------------------------------

_FURTHER_READING_RE = re.compile(
    r"^#+\s*(?:\d+\s+)?(Further|Suggested|Recommended)\s+Reading", re.MULTILINE
)
_REVIEW_RE = re.compile(r"^##\s+(?:\d+\s+)?Review Questions", re.MULTILINE)
_MODULE_FOOTER_RE = re.compile(r"^\*Module:", re.MULTILINE)


def collect_keys(text: str) -> list[str]:
    """Return citation keys cited in ``text``, in order of first appearance."""
    return ordered_citation_keys(text)


def pick_keys(chapter_rel: str, chapter_keys: list[str]) -> list[str]:
    """Choose up to 6 keys: chapter-cited first, supplement to round out."""
    supplement = SUPPLEMENT.get(chapter_rel, [])
    picks: list[str] = []
    for k in chapter_keys:
        if k not in picks:
            picks.append(k)
    for k in supplement:
        if k not in picks:
            picks.append(k)
    return picks[:6]


def render_section(entries: Iterable[BibEntry], chapter_title: str) -> str:
    """Render a Further Reading and Source Notes markdown block."""
    lines = ["", f"## Further Reading and Source Notes: {chapter_title}", ""]
    lines.extend(f"- {e.pretty()}" for e in entries)
    lines.append("")
    return "\n".join(lines)


def _find_insertion_index(text: str) -> int:
    """Locate the best offset at which to inject the Further Reading section."""
    review = _REVIEW_RE.search(text)
    if review:
        after = text[review.end() :]
        next_heading = re.search(r"\n##[^#]", after)
        footer = _MODULE_FOOTER_RE.search(after)
        candidates = [m.start() for m in (next_heading, footer) if m]
        if candidates:
            return review.end() + min(candidates)
    footer = _MODULE_FOOTER_RE.search(text)
    if footer:
        index = footer.start()
        pre = text[:index].rstrip()
        return len(pre) + 1 if pre.endswith("---") else index
    return len(text.rstrip())


def inject(
    path: Path,
    bib: dict[str, BibEntry],
    chapter_title: str,
    *,
    dry_run: bool = False,
    manuscript_root: Path = MANUSCRIPT,
    write_fn: _WriteFn | None = None,
) -> bool:
    """Inject Further Reading into ``path``. Return True if content changed."""
    text = path.read_text(encoding="utf-8")
    if _FURTHER_READING_RE.search(text):
        return False
    chapter_rel = str(path.relative_to(manuscript_root))
    picked = pick_keys(chapter_rel, collect_keys(text))
    entries = [bib[k] for k in picked if k in bib]
    if not entries:
        print(f"WARN: no references found for {chapter_rel}", file=sys.stderr)
        return False
    section = render_section(entries, chapter_title)
    index = _find_insertion_index(text)
    new_text = text[:index].rstrip() + "\n\n" + section + "\n---\n\n" + text[index:].lstrip()
    if not dry_run:
        writer = write_fn or _default_writer()
        writer(path, new_text)
    return True


# ---------------------------------------------------------------------------
# Orchestration entry point
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FurtherReadingResult:
    inserted: int
    skipped: int
    touched: list[Path]


def apply_further_reading(*, dry_run: bool = False, write_fn: _WriteFn | None = None) -> FurtherReadingResult:
    """Inject Further Reading sections into every configured chapter."""
    bib = parse_bib()
    toc = load_toc(PROJECT)
    inserted = 0
    skipped = 0
    touched: list[Path] = []
    for chapter in toc.chapters:
        if inject(chapter.path, bib, chapter.title, dry_run=dry_run, write_fn=write_fn):
            inserted += 1
            touched.append(chapter.path)
        else:
            skipped += 1
    return FurtherReadingResult(inserted=inserted, skipped=skipped, touched=touched)


__all__ = [
    "BIB",
    "BibEntry",
    "FurtherReadingResult",
    "MANUSCRIPT",
    "SUPPLEMENT",
    "apply_further_reading",
    "collect_keys",
    "inject",
    "parse_bib",
    "pick_keys",
    "render_section",
    "validate_supplement",
]
