#!/usr/bin/env python3
"""Insert a chapter-specific source-note section into configured chapters.

Strategy
--------

For each configured chapter file that does not already contain a further-reading
or source-notes heading, the script:

1. Parses the chapter prose for all documented natbib citation keys.
2. Parses ``manuscript/references.bib`` for the matching entries.
3. Selects 4–6 references — prioritising entries already cited in the
   chapter so the Further Reading list is self-consistent; if fewer than
   four are cited, the chapter-specific curated map in this file supplies
   supplements.
4. Renders the section as ``## Further Reading and Source Notes:
   <Chapter Title>`` plus a bulleted list of "Author (year). *Title*.
   *Venue*." lines. It injects the block AFTER ``## Review Questions`` (or
   the closest equivalent) and BEFORE the module reference footer.

Idempotent: if a further-reading/source-notes heading already exists, the file
is skipped.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from biology.citations import ordered_citation_keys
    from biology.toc import load_toc
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from biology.citations import ordered_citation_keys
    from biology.toc import load_toc
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


PROJECT_DIR = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT_DIR / "manuscript"
BIB = MANUSCRIPT / "references.bib"


# Curated supplementary reading per chapter (cite keys from references.bib).
# These are chosen because they are canonical entry points for the chapter's
# topic, even when the chapter prose does not yet cite them.
SUPPLEMENT: dict[str, list[str]] = {
    "unit_I/atoms_molecules.md": ["linus1960", "henderson1913"],
    "unit_I/water_and_life.md": ["henderson1913"],
    "unit_I/macromolecules.md": ["linus1960"],
    "unit_I/enzymes_and_kinetics.md": ["fischer1894", "koshland1958"],
    "unit_II/cell_theory.md": ["hooke1665", "schleiden1838", "schwann1839", "virchow1855"],
    "unit_II/cell_structure.md": ["margulis1967"],
    "unit_II/membrane_transport.md": ["singer1972", "mitchell1961"],
    "unit_II/cell_signaling.md": ["alon2019", "tyson2003"],
    "unit_III/bioenergetics_and_respiration.md": ["mitchell1961", "atkinson1968"],
    "unit_III/photosynthesis.md": ["calvin1961", "mitchell1961"],
    "unit_III/metabolic_integration.md": ["atkinson1968"],
    "unit_IV/dna_replication_and_cell_cycle.md": ["watson1953", "meselson1958"],
    "unit_IV/gene_expression.md": ["crick1958", "crick1966", "jacob1961"],
    "unit_IV/mutations_and_genomics.md": ["jinek2012", "doudna2014"],
    "unit_IV/epigenetics_and_gene_regulation.md": ["waddington1942", "fire1998"],
    "unit_V/mendelian_genetics.md": ["mendel1866"],
    "unit_V/chromosomal_inheritance.md": ["morgan1910", "sturtevant1913"],
    "unit_V/population_genetics.md": ["weinberg1908", "wright1931", "kimura1968"],
    "unit_VI/evolution_and_selection.md": ["darwin1858", "dobzhansky1973", "williams1966"],
    "unit_VI/genetic_drift_and_speciation.md": ["mayr1942", "wright1931"],
    "unit_VI/phylogenetics.md": ["woese1977", "zuckerkandl1965", "saitou1987"],
    "unit_VII/bacteria_archaea_viruses.md": ["woese1977", "margulis1967"],
    "unit_VII/microbial_ecology.md": ["woese1977"],
    "unit_VII/infectious_disease.md": ["ewald1994"],
    "unit_VIII/plant_structure_and_water.md": ["dixon1894"],
    "unit_VIII/plant_reproduction.md": ["darwin1877"],
    "unit_VIII/plant_responses.md": ["darwin1880"],
    "unit_IX/circulation_respiration_homeostasis.md": ["canon1932", "starling1914"],
    "unit_IX/nervous_system.md": ["sherrington1906", "hodgkin1952"],
    "unit_IX/action_potential_synapses.md": ["hodgkin1952", "katz1969", "frey1997"],
    "unit_IX/endocrine_and_immune.md": ["canon1932"],
    "unit_X/population_ecology.md": ["lotka1925", "volterra1926", "hutchinson1957"],
    "unit_X/community_ecology.md": ["paine1966", "connell1978", "ehrlich1964", "macarthur1967"],
    "unit_X/ecosystem_ecology.md": ["bormann1967", "odum1969", "levin1998"],
    "unit_X/biomes_and_conservation.md": ["wilson1988", "ehrlich1981"],
}


@dataclass
class BibEntry:
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
        """Render as a single APA-style bibliographic line."""
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
        # BibTeX authors are "Last, First and Last, First and ..."
        names = [n.strip() for n in raw.split(" and ")]
        if not names:
            return "Anon."
        def last(n: str) -> str:
            if "," in n:
                return n.split(",", 1)[0].strip()
            # fallback: last whitespace-separated token
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


def parse_bib() -> dict[str, BibEntry]:
    """Return a dict {key: BibEntry} from manuscript/references.bib."""
    text = BIB.read_text(encoding="utf-8")
    out: dict[str, BibEntry] = {}
    for m in _ENTRY_RE.finditer(text):
        etype, key, body = m.group(1), m.group(2).strip(), m.group(3)
        entry = BibEntry(key=key, entry_type=etype)
        for f in _FIELD_RE.finditer(body):
            name, value = f.group(1).lower(), f.group(2).strip()
            value = re.sub(r"\s+", " ", value).strip().rstrip(",")
            # Safe fallback: only assign fields BibEntry exposes
            if name in {"author", "year", "title", "journal", "publisher", "volume", "pages"}:
                setattr(entry, name, value)
        out[key] = entry
    return out


# ---------------------------------------------------------------------------
# Chapter parsing & injection
# ---------------------------------------------------------------------------

_FURTHER_READING_RE = re.compile(
    r"^#+\s*(?:\d+\s+)?(Further|Suggested|Recommended)\s+Reading", re.MULTILINE
)
_REVIEW_RE = re.compile(r"^##\s+(?:\d+\s+)?Review Questions", re.MULTILINE)
_MODULE_FOOTER_RE = re.compile(r"^\*Module:", re.MULTILINE)


def collect_keys(text: str) -> list[str]:
    return ordered_citation_keys(text)


def pick_keys(chapter_rel: str, chapter_keys: list[str]) -> list[str]:
    supplement = SUPPLEMENT.get(chapter_rel, [])
    picks: list[str] = []
    # Chapter-cited keys first (deduped, preserving order)
    for k in chapter_keys:
        if k not in picks:
            picks.append(k)
    # Then supplement
    for k in supplement:
        if k not in picks:
            picks.append(k)
    # Cap at 6 items
    return picks[:6]


def render_section(entries: list[BibEntry], chapter_title: str) -> str:
    lines = ["", f"## Further Reading and Source Notes: {chapter_title}", ""]
    for e in entries:
        lines.append(f"- {e.pretty()}")
    lines.append("")
    return "\n".join(lines)


def inject(path: Path, bib: dict[str, BibEntry], chapter_title: str, dry_run: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    if _FURTHER_READING_RE.search(text):
        return False  # already has one
    chapter_rel = str(path.relative_to(MANUSCRIPT))
    chapter_keys = collect_keys(text)
    picked = pick_keys(chapter_rel, chapter_keys)
    entries = [bib[k] for k in picked if k in bib]
    if not entries:
        print(f"WARN: no references found for {chapter_rel}", file=sys.stderr)
        return False
    section = render_section(entries, chapter_title)

    # Insertion site preference:
    # 1. After Review Questions block (find its end = next \n## or EOF)
    # 2. Before module footer
    # 3. Before the last "---" separator
    insertion_index: int | None = None
    review = _REVIEW_RE.search(text)
    if review:
        # Find end of Review Questions block (next top-level section or module footer)
        after = text[review.end():]
        next_heading = re.search(r"\n##[^#]", after)
        footer = _MODULE_FOOTER_RE.search(after)
        candidates = [m.start() for m in [next_heading, footer] if m]
        if candidates:
            insertion_index = review.end() + min(candidates)
    if insertion_index is None:
        footer = _MODULE_FOOTER_RE.search(text)
        if footer:
            # Insert before the footer; back up to previous blank line
            insertion_index = footer.start()
            # Find preceding --- separator if any, insert after it
            pre = text[:insertion_index].rstrip()
            if pre.endswith("---"):
                insertion_index = len(pre) + 1
    if insertion_index is None:
        # Append at end
        insertion_index = len(text.rstrip())

    new_text = text[:insertion_index].rstrip() + "\n\n" + section + "\n---\n\n" + text[insertion_index:].lstrip()
    if not dry_run:
        write_text_atomic(path, new_text)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    bib = parse_bib()
    inserted = 0
    skipped = 0
    toc = load_toc(PROJECT_DIR)
    for chapter in toc.chapters:
        ch = chapter.path
        if inject(ch, bib, chapter.title, dry_run=dry_run):
            inserted += 1
            print(f"  [{'D' if dry_run else '+'}] {ch.relative_to(MANUSCRIPT)}")
        else:
            skipped += 1
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] further_reading_inserted={inserted} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
