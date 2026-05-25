#!/usr/bin/env python3
"""Weave orphan BibTeX entries into the manuscript narrative.

The bibliography (``manuscript/references.bib``) is kept closed by tests:
every entry must be cited and every citekey must resolve. This script maps
orphaned entries to a natural home — the chapter that already names the concept
the paper is famous for — and inserts a single ``\\citep{key}`` or
``\\citet{key}`` after an anchor phrase in the prose.

The script is idempotent: a citation already present in the target file
is left alone. A run that inserts zero citations means the goal has been
reached (bibliography closure).
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from biology.citations import citation_keys
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from biology.citations import citation_keys
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"


@dataclass
class Insertion:
    citekey: str
    target: Path           # chapter file
    anchor: str            # literal substring that marks the insertion point
    form: str = "citep"    # "citep" or "citet"
    prefix: str = ""       # e.g. "see also " — placed before the \cite…
    replace_with: str = "" # if non-empty, replace the anchor with this string


# ---------------------------------------------------------------------------
# Map of 32 orphan citations to their natural home (chapter + anchor phrase).
# Anchors chosen to be unambiguous (first occurrence in the file) and on a
# sentence boundary so the citation reads as "…foo \citep{bar}".
# ---------------------------------------------------------------------------

# Anchors are matched case-insensitively against the first occurrence.  The
# replacement simply injects ``\citep{key}`` immediately after the matched
# span.  ``replace_with`` is retained in the dataclass for backward compat
# but is no longer read by the script — the logic always injects.
INSERTIONS: list[Insertion] = [
    Insertion("alon2019", MANUSCRIPT / "unit_II/cell_signaling.md", "feedback loop"),
    Insertion("bak1987", MANUSCRIPT / "unit_0/complex_adaptive_systems.md", "self-organi"),
    Insertion("beggs2003", MANUSCRIPT / "unit_IX/nervous_system.md", "critical period"),
    Insertion("bertalanffy1968", MANUSCRIPT / "unit_0/systems_science.md", "General System"),
    Insertion("bormann1967", MANUSCRIPT / "unit_X/ecosystem_ecology.md", "nutrient cycling"),
    Insertion("connell1978", MANUSCRIPT / "unit_X/community_ecology.md", "intermediate disturbance"),
    Insertion("darwin1858", MANUSCRIPT / "unit_VI/evolution_and_selection.md", "Darwin"),
    Insertion("dixon1894", MANUSCRIPT / "unit_VIII/plant_structure_and_water.md", "cohesion-tension"),
    Insertion("ehrlich1964", MANUSCRIPT / "unit_X/community_ecology.md", "coevolution"),
    Insertion("fire1998", MANUSCRIPT / "unit_IV/epigenetics_and_gene_regulation.md", "miRNA"),
    Insertion("frey1997", MANUSCRIPT / "unit_IX/action_potential_synapses.md", "long-term potentiation"),
    Insertion("friston2010", MANUSCRIPT / "unit_0/active_inference.md", "free energy principle"),
    Insertion("friston2017", MANUSCRIPT / "unit_0/active_inference.md", "active inference"),
    Insertion("henderson1913", MANUSCRIPT / "unit_I/water_and_life.md", "tetrahedral"),
    Insertion("holland1992", MANUSCRIPT / "unit_0/complex_adaptive_systems.md", "John Holland"),
    Insertion("jacob1961", MANUSCRIPT / "unit_IV/gene_expression.md", "lac operon"),
    Insertion("kauffman1993", MANUSCRIPT / "unit_0/complex_adaptive_systems.md", "Stuart Kauffman"),
    Insertion("levin1998", MANUSCRIPT / "unit_X/ecosystem_ecology.md", "ecosystem"),
    Insertion("lotka1925", MANUSCRIPT / "unit_X/population_ecology.md", "Lotka"),
    Insertion("margulis1967", MANUSCRIPT / "unit_II/cell_theory.md", "endosymbio"),
    Insertion("mendel1866", MANUSCRIPT / "unit_V/mendelian_genetics.md", "Mendel"),
    Insertion("mitchell1961", MANUSCRIPT / "unit_III/bioenergetics_and_respiration.md", "chemiosmo"),
    Insertion("paine1966", MANUSCRIPT / "unit_X/community_ecology.md", "keystone"),
    Insertion("sherrington1906", MANUSCRIPT / "unit_IX/nervous_system.md", "integrative action"),
    Insertion("starling1914", MANUSCRIPT / "unit_IX/circulation_respiration_homeostasis.md", "Frank-Starling"),
    Insertion("sterling2015", MANUSCRIPT / "unit_0/active_inference.md", "allosta"),
    Insertion("strogatz2018", MANUSCRIPT / "unit_0/systems_science.md", "nonlinear dynamics"),
    Insertion("tyson2003", MANUSCRIPT / "unit_II/cell_signaling.md", "bistab"),
    Insertion("volterra1926", MANUSCRIPT / "unit_X/population_ecology.md", "Volterra"),
    Insertion("weinberg1908", MANUSCRIPT / "unit_V/population_genetics.md", "Weinberg"),
    Insertion("williams1966", MANUSCRIPT / "unit_VI/evolution_and_selection.md", "natural selection"),
    Insertion("woese1977", MANUSCRIPT / "unit_VII/bacteria_archaea_viruses.md", "three domain"),
]


def _is_skippable_context(text: str, pos: int) -> bool:
    """Return True if ``pos`` falls inside:

    * a markdown heading line (``# …``)
    * a fenced code / mermaid block (between ``\\`\\`\\``` pairs)
    * a LaTeX macro argument (``\\label{…}``, ``\\cref{…}``, ``\\citep{…}``, …)
    """
    # Heading
    line_start = text.rfind("\n", 0, pos) + 1
    line_end = text.find("\n", pos)
    if line_end == -1:
        line_end = len(text)
    line = text[line_start:line_end]
    stripped = line.lstrip()
    if stripped.startswith("#"):
        return True
    if stripped.startswith("\\label") or stripped.startswith("\\cref") or stripped.startswith("\\Cref"):
        return True
    # Fenced code / mermaid block: count ``` fences before pos
    before = text[:pos]
    fences = before.count("```")
    if fences % 2 == 1:
        return True
    # Inside a LaTeX macro argument on the same line — heuristic: unmatched
    # ``\command{`` before pos without a matching closing ``}`` before pos.
    # Walk backwards across the current line looking for an opening ``{``
    # preceded by ``\<name>`` without a matching close.
    line_up_to_pos = text[line_start:pos]
    depth = 0
    i = len(line_up_to_pos) - 1
    while i >= 0:
        c = line_up_to_pos[i]
        if c == "}":
            depth += 1
        elif c == "{":
            if depth == 0:
                # unmatched open — check preceding chars for \word
                j = i - 1
                while j >= 0 and (line_up_to_pos[j].isalpha() or line_up_to_pos[j] == "*"):
                    j -= 1
                if j >= 0 and line_up_to_pos[j] == "\\":
                    return True
                break
            depth -= 1
        i -= 1
    return False


def _inject_citation(text: str, anchor: str, citekey: str) -> tuple[str, bool]:
    """Find first safe occurrence of ``anchor`` and inject ``\\citep{key}``.

    The matched anchor is extended to the next word boundary so the citation
    never lands inside a word.  Returns ``(new_text, inserted?)``.
    """
    pattern = re.compile(re.escape(anchor) + r"\w*", re.IGNORECASE)
    for match in pattern.finditer(text):
        if _is_skippable_context(text, match.start()):
            continue
        end = match.end()
        return text[:end] + f" \\citep{{{citekey}}}" + text[end:], True
    return text, False


def run(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    inserted = 0
    skipped_already_cited = 0
    skipped_no_anchor = 0

    for ins in INSERTIONS:
        if not ins.target.exists():
            print(f"WARN: target missing {ins.target}", file=sys.stderr)
            continue
        text = ins.target.read_text(encoding="utf-8")
        if ins.citekey in citation_keys(text):
            skipped_already_cited += 1
            continue
        new_text, ok = _inject_citation(text, ins.anchor, ins.citekey)
        if not ok:
            skipped_no_anchor += 1
            print(f"  skip {ins.citekey}: no safe anchor '{ins.anchor}' in {ins.target.name}")
            continue
        if not dry_run:
            write_text_atomic(ins.target, new_text)
        inserted += 1
        print(f"  [{'D' if dry_run else '+'}] {ins.citekey:18s}  {ins.target.relative_to(MANUSCRIPT)}")

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] inserted={inserted} already_cited={skipped_already_cited} "
          f"no_anchor={skipped_no_anchor} total={len(INSERTIONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
