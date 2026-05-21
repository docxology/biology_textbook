"""Biology Textbook: Chapter Collector and Analysis Script.

Reads manuscript/config.yaml, runs all biology analysis modules, then copies
all ordered chapter files into output/manuscript/ for the generic rendering
pipeline (scripts/03_render_pdf.py checks that directory first).

Usage (called automatically by scripts/02_run_analysis.py when the project is active):
    uv run python scripts/biology_analysis.py   # from projects/biology_textbook/
"""

from __future__ import annotations

import json
import logging
import re
import shutil
import sys
import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any, cast

import yaml

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = PROJECT_ROOT.parent.parent
_SRC = PROJECT_ROOT / "src"
logger = logging.getLogger(__name__)

MANUSCRIPT_DIR = PROJECT_ROOT / "manuscript"
CONFIG_FILE = MANUSCRIPT_DIR / "config.yaml"
OUTPUT_DIR = PROJECT_ROOT / "output" / "manuscript"

_UNIT_ZERO_NUMBERING_DIRECTIVE = (
    "% Unit 0 chapters render as 0.1, 0.2, ... without shifting Unit I.\n"
    "\\setcounter{section}{0}\n"
    "\\renewcommand{\\thesection}{0.\\arabic{section}}"
)
_MAIN_NUMBERING_DIRECTIVE = (
    "% Reset main chapter numbering after Unit 0.\n"
    "\\setcounter{section}{0}\n"
    "\\renewcommand{\\thesection}{\\arabic{section}}"
)


def _clear_stale_slide_artifacts() -> None:
    """Remove stale generated slide files before a fresh WIP render."""
    slides_dir = PROJECT_ROOT / "output" / "slides"
    slides_dir.mkdir(parents=True, exist_ok=True)
    removed = 0
    for path in slides_dir.iterdir():
        if path.is_file():
            path.unlink()
            removed += 1
    if removed:
        logger.info("Cleared %d stale slide artifact(s) from %s", removed, slides_dir)


def _ensure_import_paths() -> None:
    for path in (_SRC, TEMPLATE_ROOT):
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)


def _configure_logging() -> None:
    if not logging.getLogger().handlers:
        logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")


def _require_nonempty(name: str, value: object) -> None:
    """Fail fast when a required reference registry is empty."""
    if not value:
        raise RuntimeError(f"Expected non-empty {name} registry during analysis.")


def _section_numbering_directives(chapters: list[Path]) -> dict[Path, str]:
    """Return raw-LaTeX numbering directives keyed by source file path."""
    resolved = [path.resolve() for path in chapters]
    chapter_set = set(resolved)
    directives: dict[Path, str] = {}

    first_unit_zero_chapter = next(
        (
            path for path in resolved
            if path.parent == (MANUSCRIPT_DIR / "unit_0").resolve()
            and path.name not in {"README.md", "AGENTS.md", "unit_intro.md"}
        ),
        None,
    )
    if first_unit_zero_chapter is not None:
        directives[first_unit_zero_chapter] = _UNIT_ZERO_NUMBERING_DIRECTIVE

    first_main_chapter = next(
        (
            path for path in resolved
            if path.parent.name.startswith("unit_")
            and path.parent.name != "unit_0"
            and path.name not in {"README.md", "AGENTS.md", "unit_intro.md"}
        ),
        None,
    )
    if first_main_chapter is not None:
        unit_intro = first_main_chapter.parent / "unit_intro.md"
        reset_target = unit_intro if unit_intro in chapter_set else first_main_chapter
        directives[reset_target] = _MAIN_NUMBERING_DIRECTIVE

    return directives


# ---------------------------------------------------------------------------
# Config helpers
# ---------------------------------------------------------------------------

def _load_config() -> dict[str, Any]:
    """Load and parse manuscript/config.yaml."""
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config not found: {CONFIG_FILE}")
    with CONFIG_FILE.open(encoding="utf-8") as f:
        return cast(dict[str, Any], yaml.safe_load(f) or {})


def collect_ordered_chapters(config: dict[str, Any]) -> list[Path]:
    """Return all chapter Path objects in rendering order."""
    _ensure_import_paths()
    from biology.toc import load_toc

    book_toc = load_toc(PROJECT_ROOT)
    chapters: list[Path] = []

    # Front matter files (cover page, acknowledgements, etc.) — new config key
    front_matter_cfg = config.get("front_matter", {})
    if front_matter_cfg.get("include_front_matter", False):
        for fm_entry in front_matter_cfg.get("files", []):
            fm_file = fm_entry.get("file", "") if isinstance(fm_entry, dict) else str(fm_entry)
            fm_path = MANUSCRIPT_DIR / fm_file
            if fm_path.exists():
                chapters.append(fm_path)
                logger.info(f"  Front matter: {fm_file}")
            else:
                logger.warning(f"  Front matter file not found: {fm_path}")

    for unit in book_toc.units:
        logger.info(f"  Unit {unit.label}: {unit.title}")
        if unit.intro_path.exists():
            chapters.append(unit.intro_path)
            logger.info(f"    + unit intro: {unit.intro_path.name}")
        for chapter in unit.chapters:
            if chapter.path.exists():
                chapters.append(chapter.path)
                logger.info(f"    + {chapter.file}: {chapter.title}")
            else:
                logger.warning(f"    MISSING: {chapter.path}")

    # Appendices: labs and question banks (config-toggled)
    appendices = config.get("appendices", {}) or {}
    if appendices.get("include_labs", False):
        logger.info("  Appendix: Laboratory Activities")
        for lab in book_toc.labs:
            if lab.path.exists():
                chapters.append(lab.path)
                logger.info(f"    + lab {lab.unit_id}/{lab.file}")
            else:
                logger.warning(f"    MISSING lab: {lab.path}")
    if appendices.get("include_questions", False):
        logger.info("  Appendix: Question Banks")
        for question in book_toc.questions:
            if question.path.exists():
                chapters.append(question.path)
                logger.info(f"    + question bank {question.unit_id}/{question.file}")
            else:
                logger.warning(f"    MISSING question bank: {question.path}")

    # Reference appendices (math review, units & constants, periodic table, index)
    if appendices.get("include_reference", False):
        logger.info("  Appendix: Reference Material")
        for reference in book_toc.references:
            if reference.path.exists():
                chapters.append(reference.path)
                logger.info(f"    + reference appendix {reference.file}")
            else:
                logger.warning(f"    MISSING reference appendix: {reference.path}")

    return chapters


_SOLUTION_BLOCK_RE = re.compile(
    r"<!--\s*SOLUTION\s*\n(.*?)\n\s*SOLUTION\s*-->",
    re.DOTALL,
)
_FIGURE_BLOCK_RE = re.compile(r"\\begin\{figure\}.*?\\end\{figure\}", re.DOTALL)
_FIGURE_INCLUDE_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
_FIGURE_LABEL_RE = re.compile(r"\\label\{(fig:[^}]+)\}")


def _reveal_solutions(text: str) -> str:
    """Strip the ``<!-- SOLUTION`` / ``SOLUTION -->`` comment markers so the
    enclosed answer block renders as regular markdown prose.

    A narrow blockquote (``>``) is added to every answer line to distinguish
    instructor solutions visually from student prose.
    """
    def repl(match: re.Match[str]) -> str:
        body = match.group(1).strip("\n")
        quoted = "\n".join(f"> {line}" if line.strip() else ">"
                              for line in body.splitlines())
        return quoted
    return _SOLUTION_BLOCK_RE.sub(repl, text)


def inject_chapters_for_rendering(chapters: list[Path], *, include_solutions: bool = False) -> None:
    """Copy all chapters into OUTPUT_DIR with sequential numeric prefixes.

    The generic render pipeline (scripts/03_render_pdf.py) looks for
    injected_dir = project_root/output/manuscript first. We populate it
    with xx_<name>.md files so the renderer picks them up in order.

    Also copies ``config.yaml``, ``references.bib``, and ``preamble.md``
    alongside the chapters so the renderer can locate the live book metadata,
    bibliography, and LaTeX preamble without additional path resolution.

    If ``include_solutions`` is True (from ``export.include_solutions`` in
    ``config.yaml``), every ``<!-- SOLUTION … SOLUTION -->`` answer block
    embedded in a question bank is revealed as a blockquoted "Answer"
    section; otherwise the HTML comments hide them naturally.

    Args:
        chapters: Ordered list of chapter source paths.
        include_solutions: Render instructor edition with answer keys.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for existing in OUTPUT_DIR.glob("*.md"):
        existing.unlink()

    prefix_width = max(2, len(str(len(chapters))))
    numbering_directives = _section_numbering_directives(chapters)

    for i, src in enumerate(chapters, start=1):
        dest = OUTPUT_DIR / f"{i:0{prefix_width}d}_{src.name}"
        content = src.read_text(encoding="utf-8")
        if include_solutions:
            content = _reveal_solutions(content)
        directive = numbering_directives.get(src.resolve())
        if directive is not None:
            content = f"{directive}\n\n{content}"
        if "<!-- render:skip-beamer -->" not in content:
            content = "<!-- render:skip-beamer -->\n\n" + content
        write_text_atomic(dest, content)
        # Preserve source mtime for reproducibility.
        shutil.copystat(src, dest)
        logger.info(f"  Injected [{i:02d}] {src.name} → {dest.name}")

    # Copy source metadata and auxiliary files alongside the injected chapters.
    # The renderer checks the injected directory first, so config.yaml must stay
    # fresh here; otherwise book-opening metadata such as book.cover can drift.
    for aux in ("config.yaml", "references.bib", "preamble.md"):
        src = MANUSCRIPT_DIR / aux
        if src.exists():
            shutil.copy2(src, OUTPUT_DIR / aux)
            logger.info(f"  Copied auxiliary file: {aux}")

    cover_assets = MANUSCRIPT_DIR / "assets" / "cover"
    if cover_assets.exists():
        dest_assets = OUTPUT_DIR / "assets" / "cover"
        dest_assets.mkdir(parents=True, exist_ok=True)
        for src in cover_assets.iterdir():
            if src.is_file():
                shutil.copy2(src, dest_assets / src.name)
        logger.info(f"  Copied cover assets: {cover_assets} → {dest_assets}")

    edition = "instructor" if include_solutions else "student"
    logger.info(f"Injected {len(chapters)} chapter files into {OUTPUT_DIR} ({edition} edition)")


def write_figure_registry() -> Path:
    """Write a validator-compatible registry for figure labels in injected chapters."""
    figures_dir = PROJECT_ROOT / "output" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    registry_path = figures_dir / "figure_registry.json"

    records: list[dict[str, str]] = []
    seen: set[str] = set()
    for md_file in sorted(OUTPUT_DIR.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        for block in _FIGURE_BLOCK_RE.findall(text):
            includes = _FIGURE_INCLUDE_RE.findall(block)
            labels = _FIGURE_LABEL_RE.findall(block)
            filename = Path(includes[0]).name if includes else ""
            for label in labels:
                if label in seen:
                    continue
                record = {
                    "label": label,
                    "source": md_file.name,
                }
                if filename:
                    record["filename"] = filename
                records.append(record)
                seen.add(label)

    write_text_atomic(registry_path, json.dumps(records, indent=2) + "\n")
    logger.info(f"Figure registry written to {registry_path} ({len(records)} labels)")
    return registry_path


def write_visual_manifest() -> Path:
    """Write the full visual contract manifest via the dedicated audit module."""
    module = _load_local_script_module(
        "biology_textbook_audit_visual_contracts",
        PROJECT_ROOT / "scripts" / "audit_visual_contracts.py",
    )
    build_manifest = cast(Any, getattr(module, "build_manifest"))
    default_manifest = cast(Path, getattr(module, "DEFAULT_MANIFEST"))
    write_manifest = cast(Any, getattr(module, "write_manifest"))
    manifest_path = write_manifest(build_manifest(), default_manifest)
    logger.info(f"Visual manifest written to {manifest_path}")
    return cast(Path, manifest_path)


def _load_local_script_module(name: str, path: Path) -> ModuleType:
    """Load a sibling script by path without relying on the top-level scripts package."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {name!r} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def run_analysis() -> None:
    """Run all biology analysis modules and inject chapters for rendering."""
    _configure_logging()
    _ensure_import_paths()
    logger.info("Starting: Execute biology_analysis.py")
    _clear_stale_slide_artifacts()
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Cell biology --------------------------------------------------------
    from biology.cell.cell_biology import (
        ORGANELLES, nernst_potential, IonConcentration,
    )
    logger.info("Running cell_biology analysis...")
    ions = [
        IonConcentration(ion="K+",   charge=1,  inside_mM=140.0, outside_mM=5.0),
        IonConcentration(ion="Na+",  charge=1,  inside_mM=15.0,  outside_mM=145.0),
        IonConcentration(ion="Ca2+", charge=2,  inside_mM=0.1,   outside_mM=2.0),
        IonConcentration(ion="Cl-",  charge=-1, inside_mM=10.0,  outside_mM=110.0),
    ]
    e_potentials = [nernst_potential(ion) for ion in ions]
    n_organelles = len(ORGANELLES)
    logger.info(f"Cell biology: {len(e_potentials)} Nernst potentials; {n_organelles} organelles")

    # 2. Genetics ------------------------------------------------------------
    from biology.genetics.genetics import (
        dna_complement, transcribe_dna_to_mrna, translate_mrna, GENETIC_CODE,
        hardy_weinberg,
    )
    logger.info("Running genetics analysis...")
    seq = "ATCGATCG"
    _comp = dna_complement(seq)
    _mrna = transcribe_dna_to_mrna(seq)
    _protein = translate_mrna(_mrna)
    _hw = hardy_weinberg(p=0.6, q=0.4)
    if len(GENETIC_CODE) != 64:
        raise RuntimeError(f"Expected 64 genetic-code entries, got {len(GENETIC_CODE)}.")
    logger.info("Genetics analysis complete.")

    # 3. Evolution -----------------------------------------------------------
    from biology.evolution.evolution import (
        simulate_selection, Population,
    )
    logger.info("Running evolution analysis...")
    pop = Population(name="demo", p=0.3, q=0.7, fitness_AA=1.0, fitness_Aa=0.9, fitness_aa=0.5)
    history = simulate_selection(pop, generations=50)
    logger.info(f"Evolution: {len(history)} generations; final p={history[-1].p:.6f}")

    # 4. Ecology -------------------------------------------------------------
    from biology.ecology.ecology import (
        logistic_growth, biodiversity_indices, BIOMES,
    )
    logger.info("Running ecology analysis...")
    _growth = logistic_growth(N0=100, r=0.3, K=1000, t_end=50)
    div = biodiversity_indices([120, 80, 60])
    _require_nonempty("BIOMES", BIOMES)
    logger.info("Ecology analysis complete.")

    # 5. Biochemistry --------------------------------------------------------
    from biology.biochemistry.biochemistry import (
        glycolysis_summary, atp_free_energy,
    )
    logger.info("Running biochemistry analysis...")
    glycolysis = glycolysis_summary()
    _atp = atp_free_energy()
    logger.info(
        f"Glycolysis: net ATP={glycolysis.net_atp}, "
        f"ΔG_total={glycolysis.total_delta_G_kJ:.1f} kJ/mol"
    )

    # 6. Physiology ----------------------------------------------------------
    from biology.physiology.physiology import (
        poiseuille_flow, oxygen_saturation, homeostasis_response, ORGAN_SYSTEMS,
    )
    logger.info("Running physiology analysis...")
    _flow = poiseuille_flow(radius_m=0.001, length_m=0.1, pressure_difference_Pa=100.0)
    _sat = oxygen_saturation(pO2_mmHg=95.0)
    _hom = homeostasis_response(set_point=37.0, measured_value=39.0, gain=0.5, tolerance=0.5)
    _require_nonempty("ORGAN_SYSTEMS", ORGAN_SYSTEMS)
    logger.info("Physiology analysis complete.")

    # 7. Microbiology --------------------------------------------------------
    from biology.microbiology.microbiology import (
        bacterial_growth_curve, mic_fold_dilution, REFERENCE_ORGANISMS,
    )
    logger.info("Running microbiology analysis...")
    _gc = bacterial_growth_curve(N0=1e6, doubling_time_hr=0.75, t_end_hr=6.0)
    _mic = mic_fold_dilution(starting_concentration_ug_mL=128.0, dilution_factor=2, n_tubes=8)
    _require_nonempty("REFERENCE_ORGANISMS", REFERENCE_ORGANISMS)
    logger.info("Microbiology analysis complete.")

    # 8. Botany --------------------------------------------------------------
    from biology.botany.botany import (
        water_potential, transpiration_flux, photosynthesis_rate, PHOTOSYNTHESIS_PATHWAYS,
    )
    logger.info("Running botany analysis...")
    _psi = water_potential(solute_concentration_M=0.2, turgor_pressure_MPa=0.5)
    _E = transpiration_flux(
        stomatal_conductance_mol_m2_s=0.2,
        internal_vapor_conc_mol_m3=0.5,
        external_vapor_conc_mol_m3=0.4,
    )
    _A = photosynthesis_rate(photon_flux_µmol_m2_s=800.0)
    _require_nonempty("PHOTOSYNTHESIS_PATHWAYS", PHOTOSYNTHESIS_PATHWAYS)
    logger.info("Botany analysis complete.")

    # 9. Neuroscience --------------------------------------------------------
    from biology.neuroscience.neuroscience import (
        action_potential_hh,
    )
    logger.info("Running neuroscience analysis...")
    hh = action_potential_hh(stimulus_current_µA=10.0)
    fired = hh.fired
    peak = max(hh.voltage_mV)
    logger.info(f"HH simulation: peak={peak:.2f} mV, fired={fired}")

    # 10. Chapter injection --------------------------------------------------
    logger.info("Collecting chapters from config.yaml for rendering injection...")
    config = _load_config()
    chapters = collect_ordered_chapters(config)
    logger.info(f"Collected {len(chapters)} chapter files from config.yaml")
    # Instructor edition flag — overridable via env var BIOLOGY_INCLUDE_SOLUTIONS=1
    import os
    cfg_solutions = bool(config.get("export", {}).get("include_solutions", False))
    env_solutions = os.environ.get("BIOLOGY_INCLUDE_SOLUTIONS") == "1"
    include_solutions = cfg_solutions or env_solutions
    if include_solutions:
        logger.info("  → Instructor edition: revealing answer keys in question banks")
    inject_chapters_for_rendering(chapters, include_solutions=include_solutions)
    figure_registry_path = write_figure_registry()
    visual_manifest_path = write_visual_manifest()

    # Write report -----------------------------------------------------------
    report = {
        "cell_biology": {"nernst_potentials": len(e_potentials), "organelles": n_organelles},
        "genetics": {"codons": len(GENETIC_CODE)},
        "evolution": {"generations": len(history), "final_p": history[-1].p},
        "ecology": {"biomes": len(BIOMES), "shannon_index": div.shannon_index},
        "biochemistry": {"net_atp": glycolysis.net_atp, "dG_kJ": glycolysis.total_delta_G_kJ},
        "physiology": {"organ_systems": len(ORGAN_SYSTEMS)},
        "microbiology": {"reference_organisms": len(REFERENCE_ORGANISMS)},
        "botany": {"pathways": len(PHOTOSYNTHESIS_PATHWAYS)},
        "neuroscience": {"hh_peak_mV": peak, "hh_fired": fired},
        "chapters_injected": len(chapters),
        "figure_registry": str(figure_registry_path.relative_to(PROJECT_ROOT)),
        "visual_manifest": str(visual_manifest_path.relative_to(PROJECT_ROOT)),
    }

    report_path = output_dir / "analysis_report.json"
    write_text_atomic(report_path, json.dumps(report, indent=2) + "\n")
    logger.info(f"Analysis report written to {report_path}")
    print(f"[biology_analysis] Report: {report_path}")


if __name__ == "__main__":
    run_analysis()
