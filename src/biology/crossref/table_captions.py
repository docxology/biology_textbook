"""Insert pandoc-crossref table captions for chapter and lab pipe tables."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from biology.crossref.helpers import file_stem, generated_block_lines, slugify, unit_tag
from biology.crossref.patterns import RE_PIPE_TABLE_ROW, RE_TBL_CAPTION, RE_TBL_ID

TABLE_SEP_RE = re.compile(r"^\|(?=[\s\-:|]*-)[\s\-:|]+\|$")
HEADING_RE = re.compile(r"^#{3,6}\s+(?P<title>.+?)(?:\s+\{[^}]*\})?\s*$")
SKIP_NAMES = frozenset({"README.md", "AGENTS.md", "unit_intro.md"})


@dataclass(frozen=True)
class TableAnnotation:
    """A caption line to insert immediately before a pipe table."""

    line_no: int
    caption_line: str
    tbl_id: str


@dataclass(frozen=True)
class AnnotationResult:
    path: Path
    annotations: tuple[TableAnnotation, ...]
    low_confidence: tuple[int, ...]


def in_scope_files(manuscript_root: Path) -> list[Path]:
    """Return chapter and lab markdown files eligible for table numbering."""
    files: list[Path] = []
    for unit_dir in sorted(manuscript_root.glob("unit_*")):
        if not unit_dir.is_dir():
            continue
        for md in sorted(unit_dir.glob("*.md")):
            if md.name not in SKIP_NAMES:
                files.append(md)
    labs_root = manuscript_root / "labs"
    if labs_root.is_dir():
        for md in sorted(labs_root.rglob("*.md")):
            if md.name not in SKIP_NAMES:
                files.append(md)
    return files


def collect_existing_tbl_ids(manuscript_root: Path) -> set[str]:
    """Collect every ``tbl:…`` id already present under ``manuscript/``."""
    ids: set[str] = set()
    for md in manuscript_root.rglob("*.md"):
        if md.name in {"README.md", "AGENTS.md"}:
            continue
        text = md.read_text(encoding="utf-8")
        for match in RE_TBL_ID.finditer(text):
            ids.add(match.group("id"))
        for match in re.finditer(r"\\label\{tbl:(?P<id>[^}]+)\}", text):
            ids.add(match.group("id"))
    return ids


def _strip_md(text: str) -> str:
    cleaned = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    cleaned = re.sub(r"\*([^*]+)\*", r"\1", cleaned)
    cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
    cleaned = re.sub(r"\$([^$]+)\$", r"\1", cleaned)
    return cleaned.strip()


def _nearest_heading(lines: list[str], before_index: int) -> str:
    for idx in range(before_index - 1, -1, -1):
        match = HEADING_RE.match(lines[idx].strip())
        if match:
            return _strip_md(match.group("title"))
    return ""


def _header_cells(line: str) -> list[str]:
    return [_strip_md(cell) for cell in line.strip().strip("|").split("|") if cell.strip()]


def _count_data_rows(lines: list[str], separator_index: int) -> int:
    count = 0
    for idx in range(separator_index + 1, len(lines)):
        if not RE_PIPE_TABLE_ROW.match(lines[idx]):
            break
        count += 1
    return count


def _has_caption(lines: list[str], header_index: int) -> bool:
    for idx in range(header_index - 1, max(header_index - 4, -1), -1):
        stripped = lines[idx].strip()
        if not stripped:
            continue
        if RE_TBL_CAPTION.match(stripped):
            return True
        return False
    return False


def _make_tbl_id(path: Path, descriptor: str, used_ids: set[str]) -> str:
    unit = unit_tag(path)
    stem = file_stem(path)
    slug = slugify(descriptor).replace("-", "_") or "table"
    base = f"{unit}_{stem}_{slug}"
    candidate = base
    suffix = 1
    while candidate in used_ids:
        suffix += 1
        candidate = f"{base}_{suffix}"
    used_ids.add(candidate)
    return candidate


WORKED_EXAMPLE_PREFIX = re.compile(r"^Worked Example:\s*", re.IGNORECASE)
CITEP_IN_TEXT = re.compile(r"\\cite[pt]\{[^}]+\}\.?\s*")
WORKED_DATA_PREFIX = re.compile(r"^Worked example data for\s+", re.IGNORECASE)

CAPTION_OVERRIDES: dict[str, str] = {
    "unit_I_atoms_molecules_aromatic_systems_in_biology": (
        "Aromatic amino acid absorbance maxima."
    ),
    "unit_I_atoms_molecules_reduction_potentials_and_electron_transfer": (
        "Reduction potentials for selected biological half-reactions."
    ),
    "unit_I_enzymes_and_kinetics_why_cooperativity_improves_pathway_control": (
        "Effect of cooperativity on enzyme saturation near half-maximal substrate concentration."
    ),
    "unit_I_macromolecules_condensation_and_hydrolysis": (
        "Hydrolysis free energies for selected biological bond types."
    ),
    "unit_I_macromolecules_dna_structure_base_pairing_and_helical_geometry_2": (
        "DNA base-stacking enthalpy for selected nearest-neighbor steps."
    ),
    "unit_I_macromolecules_ramachandran_plots_and_backbone_dihedral_angles": (
        "Allowed backbone dihedral-angle regions in a Ramachandran plot."
    ),
    "unit_I_water_and_life_high_heat_of_vaporisation_delta_text_vap_h_44_kj_mol_at_37_degrees_c": (
        "Heat of vaporisation for water and comparison solvents at 37 degrees C."
    ),
    "unit_I_water_and_life_the_hydrophobic_effect_quantified": (
        "Thermodynamic components of the hydrophobic effect."
    ),
    "unit_III_bioenergetics_and_respiration_standard_free_energy_and_actual_free_energy": (
        "Standard and physiological free energy changes for selected hydrolysis reactions."
    ),
    "unit_III_photosynthesis_the_z_scheme_standard_electrode_potentials": (
        "Standard reduction potentials for selected photosynthetic electron carriers."
    ),
    "unit_IX_action_potential_synapses_hodgkin_huxley_gating_variables": (
        "Hodgkin-Huxley voltage-dependent gating rate variables."
    ),
    "unit_0_systems_science_part_4_complicated_vs_complex_4": (
        "Hill-response sample values for ligand concentration and fractional occupancy."
    ),
    "unit_0_history_philosophy_biology_tinbergen_s_four_questions": (
        "Tinbergen's four complementary questions (mechanism, ontogeny, "
        "adaptive significance, phylogeny)."
    ),
    "unit_0_history_philosophy_biology_tinbergen_s_four_questions_2": (
        "Translating purpose-like language into testable biological claims."
    ),
    "unit_VIII_plant_reproduction_the_abcde_model_and_mads_box_floral_quartets_citep_coen1991": (
        "Floral organ identity in the ABCDE model: whorl, organ, and gene classes."
    ),
    "unit_X_population_ecology_source_sink_dynamics_citep_pulliam1988": (
        "Source and sink patch roles in metapopulation dynamics."
    ),
    "unit_V_mendelian_extensions_and_human_genetics_formula_and_procedure": (
        "Formula and procedure for chi-square goodness-of-fit testing."
    ),
    "unit_X_biodiversity_and_food_webs_macarthur_wilson_equilibrium_model": (
        "Effects of island characteristics on MacArthur-Wilson equilibrium richness."
    ),
}


@dataclass(frozen=True)
class CaptionPolicy:
    """Student-facing table caption normalization rules."""

    overrides: dict[str, str]

    def resolve(self, text: str, *, tbl_id: str = "") -> str:
        if tbl_id and tbl_id in self.overrides:
            return self.overrides[tbl_id]

        polished = CITEP_IN_TEXT.sub("", text).strip()
        polished = WORKED_EXAMPLE_PREFIX.sub("", polished).strip()

        redundant = re.match(
            r"^Worked example data for Worked Example:\s*(.+)$", polished, re.IGNORECASE
        )
        if redundant:
            inner = redundant.group(1).rstrip(".")
            return f"Worked example: {inner}."

        worked = WORKED_DATA_PREFIX.match(polished)
        if worked:
            inner = WORKED_DATA_PREFIX.sub("", polished).rstrip(".")
            if inner.lower().startswith("part "):
                return f"Sample data for {inner}."
            return f"Worked example: {inner}."

        if polished and not polished.endswith("."):
            polished = f"{polished}."
        return polished


DEFAULT_CAPTION_POLICY = CaptionPolicy(overrides=CAPTION_OVERRIDES)


def _clean_heading(heading: str) -> str:
    cleaned = WORKED_EXAMPLE_PREFIX.sub("", heading.strip())
    return CITEP_IN_TEXT.sub("", cleaned).strip()


def polish_caption_text(
    text: str,
    *,
    tbl_id: str = "",
    policy: CaptionPolicy = DEFAULT_CAPTION_POLICY,
) -> str:
    """Normalize an existing pandoc table caption for student-facing prose."""
    return policy.resolve(text, tbl_id=tbl_id)


def build_caption_text(heading: str, headers: list[str], data_rows: int) -> str:
    """Build a student-facing table caption from local context."""
    heading = _clean_heading(heading)
    primary = headers[0] if headers else "values"
    secondary = headers[1] if len(headers) > 1 else ""
    if data_rows <= 2:
        if heading:
            if heading.lower().startswith("part "):
                return f"Sample data for {heading}."
            return f"Worked example: {heading}."
        return f"Worked example ({primary})."
    if heading and secondary:
        return f"{heading}: {primary} and {secondary}."
    if heading:
        return f"{heading}: {primary} and related columns."
    if secondary:
        return f"Summary table: {primary} and {secondary}."
    return f"Summary table: {primary}."


def find_table_annotations(
    path: Path,
    *,
    used_ids: set[str],
) -> AnnotationResult:
    """Return caption insertions required for unlabeled pipe tables in ``path``."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    generated = generated_block_lines(text)
    annotations: list[TableAnnotation] = []
    low_confidence: list[int] = []

    in_fence = False
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if idx + 1 >= len(lines) or not RE_PIPE_TABLE_ROW.match(line):
            continue
        if not TABLE_SEP_RE.match(lines[idx + 1].strip()):
            continue
        if (idx + 1) in generated or idx in generated:
            continue
        if _has_caption(lines, idx):
            continue

        heading = _nearest_heading(lines, idx)
        headers = _header_cells(line)
        data_rows = _count_data_rows(lines, idx + 1)
        caption = build_caption_text(heading, headers, data_rows)
        descriptor = heading or (headers[0] if headers else "table")
        tbl_id = _make_tbl_id(path, descriptor, used_ids)
        caption_line = f": {caption} {{#tbl:{tbl_id}}}"
        annotations.append(TableAnnotation(line_no=idx + 1, caption_line=caption_line, tbl_id=tbl_id))
        if not heading or data_rows <= 2:
            low_confidence.append(idx + 1)

    return AnnotationResult(path=path, annotations=tuple(annotations), low_confidence=tuple(low_confidence))


def apply_annotations(path: Path, annotations: tuple[TableAnnotation, ...]) -> bool:
    """Insert caption lines; return True when the file changed."""
    if not annotations:
        return False
    lines = path.read_text(encoding="utf-8").splitlines()
    for item in sorted(annotations, key=lambda row: row.line_no, reverse=True):
        insert_at = item.line_no - 1
        if insert_at < len(lines) and RE_TBL_CAPTION.match(lines[insert_at - 1].strip() if insert_at else ""):
            continue
        lines.insert(insert_at, item.caption_line)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def polish_manuscript_captions(
    manuscript_root: Path,
    *,
    write: bool = False,
) -> tuple[int, int]:
    """Rewrite existing ``: … {#tbl:…}`` captions; return (changed, examined)."""
    changed = 0
    examined = 0
    for md in sorted(manuscript_root.rglob("*.md")):
        if md.name in {"README.md", "AGENTS.md"}:
            continue
        text = md.read_text(encoding="utf-8")
        lines = text.splitlines()
        file_changed = False
        for idx, line in enumerate(lines):
            match = RE_TBL_CAPTION.match(line.strip())
            if not match:
                continue
            examined += 1
            tbl_match = RE_TBL_ID.search(line)
            tbl_id = tbl_match.group("id") if tbl_match else ""
            old_text = match.group("caption").strip()
            new_text = polish_caption_text(old_text, tbl_id=tbl_id)
            if new_text == old_text:
                continue
            attrs = (match.group("attrs") or "").strip()
            if not attrs and tbl_id:
                attrs = f"{{#tbl:{tbl_id}}}"
            lines[idx] = f": {new_text} {attrs}".strip() if attrs else f": {new_text}"
            file_changed = True
        if file_changed and write:
            md.write_text("\n".join(lines) + "\n", encoding="utf-8")
            changed += 1
    return changed, examined


def annotate_manuscript(
    manuscript_root: Path,
    *,
    write: bool = False,
) -> tuple[list[AnnotationResult], int]:
    """Annotate all in-scope files; return results and number of files changed."""
    used_ids = collect_existing_tbl_ids(manuscript_root)
    results: list[AnnotationResult] = []
    changed = 0
    for path in in_scope_files(manuscript_root):
        result = find_table_annotations(path, used_ids=used_ids)
        if result.annotations:
            results.append(result)
            if write:
                if apply_annotations(path, result.annotations):
                    changed += 1
    return results, changed


__all__ = [
    "AnnotationResult",
    "CAPTION_OVERRIDES",
    "CaptionPolicy",
    "DEFAULT_CAPTION_POLICY",
    "TableAnnotation",
    "annotate_manuscript",
    "apply_annotations",
    "build_caption_text",
    "collect_existing_tbl_ids",
    "find_table_annotations",
    "in_scope_files",
    "polish_caption_text",
    "polish_manuscript_captions",
]
