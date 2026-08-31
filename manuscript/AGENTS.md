# Manuscript AGENTS.md

## Purpose

This directory contains all textbook manuscript source files, organized by unit. Each unit directory contains registered chapter files and may also contain orientation files such as `unit_intro.md`. A master `config.yaml` in this directory controls rendered chapter ordering, auto-numbering, page layout, typography, front matter, labs, question banks, and reference appendices.

> **Composable workflows** (add chapter, register figure, `ChapterMeta` / `\label` naming, which tests to run): [../docs/composable_authoring.md](../docs/composable_authoring.md). This file is the **manuscript** contract; that doc ties it to scripts and tests.

## Auto-Numbering System

**Chapter, figure, equation, and table numbers are assigned at render time — not in filenames.**

- Chapter files use **descriptive names only** (e.g., `atoms_molecules.md`, not `ch01_atoms_molecules.md`).
- Ordering is controlled entirely by `manuscript/config.yaml`.
- To reorder chapters: edit the `chapters:` list in the relevant unit entry in `config.yaml`.
- To add a chapter: create the Markdown file with a descriptive name; add it to `config.yaml`.
- To skip a chapter: add `enabled: false` to its entry in `config.yaml`.

## Configuration Keys in `config.yaml`

| Section | Key | Purpose |
| ------- | --- | ------- |
| `book` | `author`, `orcid`, `edition`, `cover.image` | Bibliographic metadata; ORCID on title page; cover PNG path under `assets/` |
| `authors[]` | `name`, `orcid`, `email`, `affiliation` | Full author list with affiliations |
| `publication` | `doi`, `repository_url`, `repository_label`, `keywords` | Zenodo DOI and living Git source on generated publishing page |
| `layout` | `margin_*_mm`, `page_size`, `line_height` | Page margins, paper size, and `setspace` stretch — **must match** `preamble.md` geometry and `\setstretch{...}` |
| `typography` | `link_color`, `link_color_internal`, `link_color_external` | Hyperlink color (default: `#CC0000` red) |
| `typography` | `body_font`, `heading_font`, `base_font_size_pt` | Font settings; **body point size is applied in** `preamble.md` via `\renewcommand{\normalsize}{...}` (keep equal to `base_font_size_pt`) |
| `front_matter` | `include_front_matter`, `files[]`, `include_preface` | Source files rendered after the generated cover, publishing-information page, and table of contents; preface appears only when listed and enabled |
| `appendices` | `include_labs`, `include_questions`, `labs[]`, `questions[]`, `reference[]` | Optional labs, question banks, and reference appendices after core units. Lab/question entries store only `file:` names; their display titles are derived from chapter titles by `src/biology/toc.py`. |
| `rendering` | `auto_number_*`, `output_format` | Numbering and rendering options |
| `units[]` | `chapters[].file`, `chapters[].title` | Chapter files and display titles, in rendering order |
| `llm` | `reviews.enabled`, `translations.enabled` | Optional LLM review/translation stage |
| `accessibility`, `content_notes`, `export`, `chapter_metadata` (tail of file) | mixed | **Advisory vs enforced:** not every key is read by the build. See [../docs/accessibility.md](../docs/accessibility.md) for the table. **Tests** (`test_accessibility.py` and other invariant modules) and **`src/visualization/cvd.py`** (matplotlib palette) are the main enforcement for alt text and colorvision–friendly figures when `color_blindness_safe` is true. |

## Directory Structure

```text
manuscript/
├── config.yaml          # Master configuration (layout, typography, units, appendices)
├── assets/              # Cover art (`book.cover.image`); see assets/README.md
├── front_matter.md      # Dedication, acknowledgements, navigation (after generated cover/ToC)
├── preface.md           # Book preface
├── preamble.md          # LaTeX preamble (keep geometry in sync with config layout.*)
├── glossary.md          # Master glossary (Appendix F when `appendices.reference` includes it)
├── references.bib       # Bibliography
├── AGENTS.md            # This file
├── README.md            # Quick reference
├── appendices/          # Generated/reference appendices (math, units/constants, periodic table, index)
├── unit_0/              # Systems science / complexity prelude (see config.yaml)
├── unit_I/ … unit_X/    # One directory per unit; registered chapters plus optional unit_intro.md
├── labs/                # Appendix lab activities (per-unit subdirs)
└── questions/           # Appendix question banks (per-unit subdirs)
```

## Chapter File Conventions

- **One chapter = one Markdown file registered in `config.yaml`.** Unit orientation files such as `unit_intro.md` are source notes unless they are explicitly added to the render order.
- **Filename**: `descriptive_slug.md` — all lowercase, underscores, no chapter numbers.
- **First heading** in file = exact chapter title from `config.yaml` (rendered with auto-assigned number). Run `scripts/sync_curriculum_materials.py` after title or order edits to normalize chapter, unit-intro, lab, question-bank, glossary, and reference-appendix H1s from `src/biology/toc.py`.
- **Numbered chapter section label**: the first non-blank line after the H1 title must be `\label{sec:unit_X_<stem>}` (inserted by `scripts/insert_crossref_labels.py`). Refer to this chapter elsewhere with `\cref{sec:unit_X_<stem>}`. Enforced by `tests/test_build_invariants.py::test_every_chapter_has_section_label`.
- **Unnumbered section label** (unit intros, labs, question banks, reference appendices, glossary): embed the canonical id on the H1 as a Pandoc identifier, e.g. `# Title {#sec:unit_I_unit_intro .unnumbered}`. Do **not** use a standalone `\label{sec:…}` line between H1 and the first `##` heading — that breaks `\nameref` on `\section*` and prevents Pandoc from parsing subsequent headings. Maintained by `scripts/sync_curriculum_materials.py` and `scripts/insert_crossref_labels.py` (labs/questions). Enforced by `tests/test_build_invariants.py::test_unnumbered_surfaces_use_h1_identifiers` and related lab/question checks.
- **Metadata badge**: after the label, a `<!-- chapter-metadata-badge -->` blockquote (inserted by `scripts/insert_chapter_metadata.py` from data in `src/biology/chapter_metadata.py`) shows Level 1/3–3/3 difficulty, reading time, lecture time, and prerequisites. Enforced by `tests/test_build_invariants.py::test_every_chapter_has_metadata_badge`.
- **Figures**: raw-LaTeX `\begin{figure}\centering\includegraphics[…]{../figures/<name>.png}\caption{…}\label{fig:unit_X_<descriptor>}\end{figure}` blocks. Paths are relative to `output/manuscript/`.
- **Diagrams (authoring)**: inline ` ```mermaid ` fences are fine for HTML review; the manuscript currently has 197 inline fences (196 outside README/AGENTS docs). Every fence must be followed by exactly one `<!-- alt: ... -->` comment and one italic caption. At PDF-build time the renderer converts each block strictly to a PNG image; missing `mmdc` or a render failure is a build failure.
- **Diagrams (registered)**: factories in `src/mermaid/biology_diagrams.py` that appear in `ALL_BIOLOGY_DIAGRAMS` are rendered by `scripts/generate_diagrams.py`; use `--strict-png` for publication gates. Reference via the usual markdown image syntax if a static PNG is desired.
- **Equations**: Use LaTeX `\begin{equation}\label{eq:unit_X_<descriptor>}…\end{equation}` or `align` environments for numbered display equations. Use unnumbered display math only for worked steps that are not referenced. Do not use manual equation-number tags in manuscript prose; rendered equation numbers are assigned by LaTeX and cross-referenced with `\cref{eq:...}`.
- **Tables**: Chapter and lab pipe tables carry a pandoc caption line immediately above the header row: `: Summary text {#tbl:unit_X_<descriptor>}`. Regenerate missing captions with `scripts/annotate_table_captions.py --write`; polish weak auto-generated titles with `scripts/polish_table_captions.py --write`. Cross-reference numbered tables with `\cref{tbl:…}`. Plain pipe tables in unit intros (Landmark Discoveries), front matter, appendices, and question banks stay unnumbered.
- **Citations**: `\citep{key}` for parenthetical, `\citet{key}` for textual. All citekeys must exist in `references.bib`; `tests/test_bibliography_closure.py` enforces this bidirectionally.
- **Cross-references** in prose: numbered chapters use `\cref{sec:…}`; unnumbered surfaces (unit intros, labs, question banks, reference appendices, glossary) use `\nameref{sec:…}` because `\cref` on `\section*` resolves to a shared counter. Figures, equations, and numbered tables use `\cref{fig:…}` / `\cref{eq:…}` / `\cref{tbl:…}`. Never hand-type rendered numbers such as "Chapter 11", "Figure 4.3", "Equation 5.7", "Section 2", or "§2".
- **Visible unit/appendix references** in student-facing prose: use `\nameref{sec:unit_X_unit_intro}` for units and `\nameref{sec:appendix_<slug>}` (or `\nameref{sec:glossary}`) for appendices; use generator-owned marker blocks for navigation/scope tables. Do not hand-author visible labels such as "Unit I", "Appendix C", or "Figure FM-1" outside generated blocks.
- **Glossary terms**: on first use in a chapter, link with the markdown-link syntax `` `[**term**](#gl:<slug>)` `` (slug is generated from the term by `scripts/link_glossary.py`); the `{#gl:<slug>}` anchor is defined in `manuscript/glossary.md`.
- **Code blocks**: standard fenced blocks; imports from `biology.*` src modules.

## Front Matter

The PDF renderer creates the book-style opening from `config.yaml` before
manuscript source is concatenated: page 1 is the title/author cover with
`book.cover.image`, page 2 is publishing and licensing information, and page 3
begins the detailed table of contents.

Optional `config.yaml → front_matter.page_two_quote` and
`front_matter.page_two_acknowledgements` blocks render directly on page 2. Use
them for compact epigraph and acknowledgement material that belongs beside the
generated publishing information.

`front_matter.md` is source material that follows that generated opening. It
contains dedication, acknowledgements, generated navigation, generated reading
paths, a generated concept map, and "About This Textbook" material.
`preface.md` follows when it is listed under
`config.yaml → front_matter.files[]` and `front_matter.include_preface` is true.
Its scope table is generated from the same `BookToc` source. Do not duplicate
cover, copyright, author metadata, or hand-maintained unit-title lists inside
`front_matter.md` or `preface.md`.

## Render workflow (injected manuscript)

The template PDF stage prefers `projects/biology_textbook/output/manuscript/` when that directory contains markdown files. Edits under `manuscript/` alone do **not** change the combined PDF until analysis refreshes the injection.

```bash
cd projects/biology_textbook
uv run python scripts/sync_curriculum_materials.py   # after scaffold/label/title edits
uv run python scripts/biology_analysis.py            # copies ordered manuscript → output/manuscript/
cd ../..  # template root
uv run python scripts/03_render_pdf.py --project biology_textbook
```

Run `uv run python scripts/audit_textbook_quality.py --check --max-advisories 0` before render when chapters, labs, question banks, or biological claims changed.

## Adding a New Chapter

1. Create `unit_<X>/<descriptive_name>.md`
2. Add an entry to the relevant unit in `manuscript/config.yaml`:

   ```yaml
   - file: descriptive_name.md
     title: "Chapter Title"
   ```

3. Add a matching entry to `../src/biology/chapter_metadata.py`:

   ```python
   ChapterMeta("unit_X_descriptive_name", <N>, "X", <difficulty>, <reading_min>, <lecture_min>,
               ("unit_Y_prereq_one", "unit_Z_prereq_two")),
   ```

4. Create paired lab (`manuscript/labs/unit_X/lab_descriptive_name.md`) and question bank (`manuscript/questions/unit_X/questions_descriptive_name.md`); register both in `config.yaml` under `appendices.labs[]` / `appendices.questions[]` with only `file:` entries. Do not duplicate derived `title:` strings for labs or question banks.
5. Run the maintenance pipeline (each script is idempotent):

   ```bash
   uv run python scripts/insert_crossref_labels.py      # \label{sec:unit_X_…} + prose → \cref
   uv run python scripts/link_labs_to_chapters.py       # \cref from lab + question bank
   uv run python scripts/sync_curriculum_materials.py   # canonical H1s, unit labels, generated appendices/navigation/scope
   uv run python scripts/insert_chapter_metadata.py     # badge + refresh Course Planning Grid
   uv run python scripts/link_glossary.py --check       # glossary anchors and semantic back-reference check
   uv run python scripts/generate_figures.py            # if chapter references new figures
   uv run python scripts/generate_diagrams.py           # if chapter registers new mermaid diagrams
   ```

6. Verify invariants: `uv run python -m pytest tests/test_toc_consistency.py tests/test_build_invariants.py tests/test_chapter_metadata.py tests/test_bibliography_closure.py -v`
7. Render: `uv run python scripts/03_render_pdf.py --project biology_textbook` from the template repo root when template infrastructure is available.

## Module Reference Footer

Each chapter should end with a module reference footer:

```text
*Module: `src/biology/<domain>/<file>.py` (key functions used)*
*Figure: `src/visualization/plots.py` — `plot_*` from `ALL_FIGURE_GENERATORS`*
*Diagram: `src/mermaid/biology_diagrams.py` — `*_diagram()` factory listed in `ALL_BIOLOGY_DIAGRAMS`*
*Cross-references: \cref{sec:unit_X_...} (short topic), \cref{sec:unit_Z_...} (short topic)*  — semantic section refs, not hand-typed chapter numbers
```

### Allowed figure and diagram names (authoring allowlist)

Cite only these **matplotlib** generators (registry keys in parentheses match `ALL_FIGURE_GENERATORS`):

`plot_nernst_potentials`, `plot_ghk_permeability`, `plot_hill_equation`, `plot_osmotic_pressure`, `plot_punnett_square`, `plot_chromosome_structure`, `plot_hardy_weinberg`, `plot_translation_codons`, `plot_oxygen_dissociation`, `plot_poiseuille_flow`, `plot_michaelis_menten`, `plot_glycolysis_summary`, `plot_homeostasis_feedback`, `plot_lotka_volterra`, `plot_selection_simulation`, `plot_fitness_landscape`, `plot_molecular_clock`, `plot_action_potential`, `plot_light_response_curves`, `plot_photosynthesis_rate`, `plot_water_potential_transpiration`, `plot_bacterial_growth`, `plot_sir_model`, `plot_mic_dilution_series`, `plot_methylation_heatmap`, `plot_logistic_growth`, `plot_allee_threshold_dynamics`, `plot_biodiversity_indices`, `plot_food_web_trophic_levels`, `plot_species_area_relationship`, `plot_biome_distribution`, `plot_genetic_drift_trajectories`, `plot_network_degree_distribution`, `plot_prediction_error_precision`, `plot_biology_milestones`, `plot_electronegativity_bond_energy`, `plot_polymer_hierarchy`, `plot_organelle_size_scale`, `plot_atp_yield_comparison`, `plot_replication_fork_progression`, `plot_mutation_rate_spectrum`, `plot_pollen_tube_growth`.

Cite only **`*_diagram()`** factories that appear in `ALL_BIOLOGY_DIAGRAMS` (see `src/mermaid/biology_diagrams.py`), including: `macromolecule_classification_diagram`, `enzyme_kinetics_diagram`, `organelle_function_diagram`, `membrane_transport_diagram`, `glycolysis_pathway_diagram`, `atp_synthesis_diagram`, `cell_cycle_diagram`, `transcription_translation_diagram`, `mendelian_cross_diagram`, `natural_selection_diagram`, `phylogenetic_tree_diagram`, `viral_replication_cycle_diagram`, `photosynthesis_light_dark_diagram`, `nervous_system_reflex_diagram`, `immune_response_diagram`, `food_web_diagram`, `population_growth_stages_diagram`, `speciation_diagram`, `hormone_signaling_diagram`, `dna_replication_diagram`, `nutrient_cycle_diagram`, `chromosome_inheritance_diagram`, `mirna_biogenesis_diagram`, `x_inactivation_diagram`.

Do **not** reference `*_visualizer.py` paths or plot/diagram names absent from the registries above.

## Mermaid Diagram Insertion

Mermaid diagrams may be written inline in Markdown (recommended for authoring and review). Inline Mermaid in the combined PDF is strict PNG mode: the preprocessor writes deterministic `.mmd` and `.png` files under `output/figures/mermaid_inline/`, removes stale inline artifacts before rendering, and fails instead of dropping diagrams. If a diagram should be reusable across chapters, use the registered PNG workflow:

1. Author diagram function in `src/mermaid/biology_diagrams.py` → add to `ALL_BIOLOGY_DIAGRAMS`.
2. Run `uv run python scripts/generate_diagrams.py --strict-png` → exports PNGs under `output/figures/mermaid/` and rejects `.mmd` fallback output.
3. Reference the generated image in the chapter using standard Markdown image syntax with a correct relative path.

## American English

Prose, learning objectives, alt text, Mermaid labels, and generator strings under `src/biology/` use **American English** spellings (`behavior`, `organization`, `signaling`, `color`, `center`, …). **`references.bib` keeps published title spellings** (original UK spellings in citation titles, journal names, URLs). Figure and diagram conventions: [../docs/visualization_guide.md](../docs/visualization_guide.md).

- Gate: `uv run pytest tests/test_american_english.py`
- Batch rewrite: `uv run python scripts/normalize_american_english.py` (mapping in `src/biology/maintenance/data/british_to_american.yaml`; skips `references.bib`, `preamble.md`, and code fences)
- Optional LO Bloom HTML comments use American **`analyze`**, not `analyse` (see [../docs/pedagogy_objectives_mapping.md](../docs/pedagogy_objectives_mapping.md))
- After editing enrichment or curriculum generators, run normalize, then `scripts/sync_curriculum_materials.py` and `scripts/enrich_embedded_textbook.py` so synced blocks stay aligned.

## Print density (PDF)

The textbook PDF is tuned for **dense letter-size pages**: 2 mm margins (`geometry` in [preamble.md](preamble.md)), **9 pt** body (`\normalsize` in preamble), `setstretch` **1.28**, and slightly smaller section headings (`titlesec`). Changing margins or body size requires editing **both** [config.yaml](config.yaml) (`layout.*`, `typography.base_font_size_pt`, `layout.line_height`) and the LaTeX blocks in `preamble.md` so the build stays self-consistent.

## Labs, question banks, and figures

- **Labs** (`labs/unit_*/*.md`) and **question banks** (`questions/unit_*/*.md`) are listed in `config.yaml` → `appendices`. Toggle `include_labs` / `include_questions` there.
- **Current claims** are registered in `current_claims.yaml`; every fast-moving claim needs a source, source tier, checked date, refresh trigger, and manuscript anchor. Run `uv run python scripts/audit_current_claims.py --check` after edits.
- **Assessment metadata** for question items and lab alignment is maintained by `uv run python scripts/sync_assessment_metadata.py --dry-run` to preview drift and `uv run python scripts/sync_assessment_metadata.py --check` to gate; verify with `tests/test_assessment_metadata.py` and `tests/test_lab_pedagogy_alignment.py`.
- **Reference appendices** (`appendices/*.md`) are maintained separately from lab/question banks and are rendered when `appendices.include_reference: true`; ordering comes from `appendices.reference[]` in `config.yaml`.
- Optional regeneration of matplotlib assets: from project root, `uv run python scripts/generate_figures.py` (see [labs/README.md](labs/README.md)).
- Mermaid PNGs: `uv run python scripts/generate_diagrams.py --strict-png` when PDF must embed static registered diagrams.

## Quality Standards

- Every quantitative claim must be verifiable from the src module output or from a cited reference (author, year, journal).
- Mathematical equations must be correct, self-consistent, and use LaTeX notation.
- Each chapter must contain: **Learning Objectives** · **Section headings (level 2–3)** · **Worked Examples** · **Review Questions** · **Key Terms** · **Summary**.
- No Mocks: all code examples reference real `src/biology/` modules.
- Nobel Prize attribution and primary literature citations for landmark results.
