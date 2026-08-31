# Composable Authoring: Stable IDs, Modules, and References

> [!NOTE]
> This document is the **structural** counterpart to [agent_instructions.md](agent_instructions.md) (editorial voice) and [docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md) (enforced manuscript contract). It describes **stable identifiers**, **workflows** for adding content without breaking invariants, and **which tests** catch common mistakes. For LaTeX patterns and the equation-form decision tree, see [manuscript_guide.md](manuscript_guide.md).

---

## Table of contents

- [Source of truth](#source-of-truth)
- [Identifier schema](#identifier-schema)
- [Reference surfaces](#reference-surfaces)
- [Workflows](#workflows)
- [Validation commands](#validation-commands)
- [Flow: config to PDF](#flow-config-to-pdf)
- [See also](#see-also)

---

## Source of truth

| Layer | Role |
| ----- | ---- |
| [docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md) | Path conventions, allowlists, cross-ref rules |
| [../tests/test_build_invariants.py](../tests/test_build_invariants.py) | Chapters, badges, labs, figure generators |
| [../tests/test_chapter_metadata.py](../tests/test_chapter_metadata.py) | `config.yaml` ↔ `ChapterMeta` |
| [../tests/test_curriculum_metadata.py](../tests/test_curriculum_metadata.py) | `config.yaml` ↔ `CurriculumRecord` / `AlignmentRecord` ↔ chapter/lab/question/appendix blocks |
| [../tests/test_bibliography_closure.py](../tests/test_bibliography_closure.py) | `references.bib` ↔ `\cite` |
| [../tests/test_accessibility.py](../tests/test_accessibility.py) | Alt-text quality, LaTeX/Mermaid in chapters + labs + questions |
| [../tests/test_crossref_validator\*.py](../tests/) | `@fig:` / `@eq:`, `{#fig:...}`, `\label{...}` consistency |

> [!IMPORTANT]
> When a guide and a test disagree, **the test wins**. Update the guide and ensure the script that auto-fixes the violation (e.g. `scripts/insert_crossref_labels.py`) is idempotent.

---

## Identifier schema

Chapters, figures, equations, and tables use **semantic** labels. Rendered "Chapter 12" / "Figure 3.2" numbers are assigned at PDF build from [../docs/manuscript/config.yaml](../docs/manuscript/config.yaml) order — **never** encode them in filenames or in prose as hard-coded ordinals.

### Chapters

| Slot | Rule | Example |
| ---- | ---- | ------- |
| Filename | descriptive, lowercase, underscores, no chapter number | `water_and_life.md` |
| `chapter_id` | `unit_<X>_<stem>` matching filename | `unit_I_water_and_life` |
| `\label` | `\label{sec:<chapter_id>}` on the line after the H1 | `\label{sec:unit_I_water_and_life}` |
| `\cref` reference | `\cref{sec:<chapter_id>}` from any chapter | `see \cref{sec:unit_I_water_and_life}` |

**Prerequisites:** in `src/biology/chapter_metadata.py`, `prerequisites` is a tuple of **chapter_id strings** (same as without the `sec:` prefix). Badges and inserts turn these into `\cref{sec:...}` links in the metadata block.

**Title and curriculum metadata:** `src/biology/toc.py` derives unit-intro,
chapter, lab, question-bank, reference appendix, front-matter navigation, and
Course Planning Grid display names from `docs/manuscript/config.yaml` plus
`ChapterMeta`. Do not hand-maintain lab or question titles in `config.yaml`;
list only their `file:` entries. In `src/biology/curriculum.py`, each
`CurriculumRecord` uses the same `chapter_id` to align a chapter with its lab,
question bank, model/data skill, misconception probe, and transfer task.
`src/biology/alignment.py` layers framework metadata on top: Vision & Change
concepts/competencies, AP Biology big ideas/practices, NGSS-style topics,
BioSkills categories, and instructor orchestration moves. Run
`scripts/sync_curriculum_materials.py` after changing title, curriculum, or
alignment sources; it rewrites renderable H1s, chapter Study Blueprints, lab
evidence checklists, question-bank coverage notes, front-matter navigation,
Appendix A's curriculum map, Appendix B's instructor orchestration guide, and
ToC-safe heading attributes. Do not hand-prefix headings with section numbers;
Pandoc/LaTeX supplies numbering for body chapters, while front matter, unit
intros, labs, question banks, and reference appendices are synchronized as
unnumbered ToC entries.

**PDF opening and cover:** the cover title, subtitle, author block, publishing
page, and page-3 Contents are generated from `docs/manuscript/config.yaml`.
`book.cover.image` points to a text-free reusable image asset. Regenerate the
current integrated biology montage with `uv run python scripts/generate_cover_art.py`.

### Figures (matplotlib PNGs)

| Slot | Rule | Example |
| ---- | ---- | ------- |
| `\label` | `\label{fig:unit_X_<descriptor>}` inside `\begin{figure}…\end{figure}`; globally unique descriptor | `\label{fig:unit_I_michaelis_menten}` |
| Path | `\includegraphics{../figures/<name>.png}` — relative to **`output/manuscript/`** at render time | `../figures/michaelis_menten.png` |
| Reference | `\cref{fig:unit_X_<descriptor>}` | `\cref{fig:unit_I_michaelis_menten}` |
| Registry | Generator must appear in `src/visualization/plots.py::ALL_FIGURE_GENERATORS` | `plot_michaelis_menten` |

> [!WARNING]
> Every generator in `ALL_FIGURE_GENERATORS` **must** be referenced from at least one chapter. `tests/test_build_invariants.py::test_every_registered_figure_is_referenced` enforces this. Use `scripts/insert_orphan_figures.py --dry-run` to scaffold a missing block.

### Inline Mermaid diagrams

Inline Mermaid fences are allowed in manuscript Markdown when a process diagram
is clearer than prose. Add a descriptive `<!-- alt: ... -->` comment immediately
after each fence. During PDF rendering, infrastructure converts each fence into
a deterministic PNG under `output/figures/mermaid_inline/` and replaces the
fence with a normal Pandoc image reference; missing or failing `mmdc` is a hard
PDF-render failure so diagrams are never silently dropped.

### Equations

| Pattern | Use | Cross-reference? |
| ------- | --- | ---------------- |
| `\begin{equation}\label{eq:unit_X_<descriptor>}…\end{equation}` | Anything you `\cref{...}` | **Yes** |
| `\begin{align}\label{eq:unit_X_<descriptor>}…\end{align}` | Multi-line cross-referenced derivation | **Yes** |
| `$$ … $$` (plain) | Display math without numbering or reference | No |
| `$ … $` | Inline math | No |

> [!WARNING]
> Do not use manual equation-number tags in manuscript prose. Use labeled `equation` or `align` environments for numbered display equations; use plain `$$ … $$` only for unnumbered display math.

`pandoc-crossref` attributes like `{#eq:myid}` on display math are validated by [../src/biology/crossref_validator.py](../src/biology/crossref_validator.py).

### Mermaid (inline) and unit concept maps

- After each `mermaid` fence, write an *italic* line that **describes** the diagram (≥ 10 words; no "Figure N.M").
- Unit intro "concept map" images: use a **bold** descriptive title (e.g. **Unit V concept map — …**), not hand figure indices.

---

## Reference surfaces

| Mechanism | Use in this project |
| --------- | ------------------- |
| **cleveref** | `\cref{sec:...}`, `\cref{fig:...}`, `\cref{eq:...}`, `\cref{tbl:...}` in prose (primary) |
| **natbib** | Prefer `\citep{key}` and `\citet{key}`; documented rare forms include `\citealt`, `\citealp`, `\citeauthor`, `\citeyear`, and optional arguments such as `\citet[p.~12]{key}`. All keys live in [../docs/manuscript/references.bib](../docs/manuscript/references.bib). See [manuscript_guide.md#citations-and-references](manuscript_guide.md#citations-and-references) for command-by-command guidance. |
| **pandoc-crossref** | `@fig:`, `@eq:`, `@tbl:`, `@sec:` in prose, and `{#fig:...}` / `{#eq:...}` on assets — **must** resolve; [crossref_validator](../src/biology/crossref_validator.py) + tests enforce. |

Raw LaTeX figure/table environments with `\label{fig:...}` are scanned by the validator; markdown images use `![alt](path){#fig:...}` when using crossref-style IDs.

---

## Workflows

### 1) New core chapter

1. Create `docs/manuscript/unit_<X>/<stem>.md` (descriptive `stem`, no chapter number in filename).
2. Add chapter entry under the correct `units[]` in [../docs/manuscript/config.yaml](../docs/manuscript/config.yaml).
3. Add `ChapterMeta("unit_<X>_<stem>", ...)` in [../src/biology/chapter_metadata.py](../src/biology/chapter_metadata.py) (order follows `config.yaml`).
4. Add `CurriculumRecord` data in [../src/biology/curriculum/](../src/biology/curriculum/) with a real `bridge_api` from `src/biology`.
5. Check [../src/biology/alignment.py](../src/biology/alignment.py) unit defaults. If the new chapter needs a different standards/skills profile than its unit, add an override or update the unit alignment deliberately.
6. Add lab + question files if required by your appendices plan; list only their `file:` names under `config.yaml` `appendices.labs/questions`. Their H1 titles are derived by `biology.toc`.
7. Run idempotent scripts (from project directory):

   ```bash
   uv run python scripts/insert_crossref_labels.py
   uv run python scripts/insert_chapter_metadata.py
   uv run python scripts/sync_curriculum_materials.py
   uv run python scripts/link_labs_to_chapters.py
   uv run python scripts/link_glossary.py
   ```

8. Run gates (see [Validation commands](#validation-commands)).

Details match [../manuscript/AGENTS.md — Adding a New Chapter](../docs/manuscript/AGENTS.md#adding-a-new-chapter).

### 2) New `plot_*` figure

1. Implement generator in [../src/visualization/plots.py](../src/visualization/plots.py) and register in `ALL_FIGURE_GENERATORS` (naming on [../manuscript/AGENTS.md allowlist](../docs/manuscript/AGENTS.md)).
2. `uv run python scripts/generate_figures.py` (from project directory).
3. Add `\begin{figure}...\includegraphics{../figures/...}\caption{...}\label{fig:unit_X_...}\end{figure}` in the chapter; reference with `\cref{fig:...}`.
4. Add `<!-- alt: ... -->` HTML comment immediately after `\end{figure}` (see [accessibility.md#alt-text-writing-guide](accessibility.md#alt-text-writing-guide)).
5. Invariant: `test_every_registered_figure_is_referenced` in [../tests/test_build_invariants.py](../tests/test_build_invariants.py).

### 3) New registered Mermaid diagram

1. Add factory in [../src/mermaid/biology_diagrams.py](../src/mermaid/biology_diagrams.py) and list in `ALL_BIOLOGY_DIAGRAMS` (naming on allowlist in [docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md)).
2. `uv run python scripts/generate_diagrams.py`.
3. [../tests/test_mermaid_and_visualization.py](../tests/test_mermaid_and_visualization.py) covers registry and renderer.

### 4) New `src/biology` API used in a chapter

- Imports use `from biology.<pkg> import ...` with **real** signatures; code blocks are exercised by tests indirectly via coverage expectations — add or extend tests in `tests/test_*.py` when you add public functions.
- Reconcile [api_reference.md](api_reference.md) so the new function appears in the appropriate table.

---

## Validation commands

From the active project root:

```bash
uv run python -m pytest tests/ --cov=src --cov-fail-under=90
```

From **template repository root**:

```bash
uv run python -m infrastructure.validation.cli markdown /path/to/biology_textbook/manuscript/
uv run python -m infrastructure.validation.cli prerender /path/to/biology_textbook/manuscript/ --repo-root .
```

> [!TIP]
> Run `markdown` after every bulk edit; add `prerender` before relying on a clean PDF (same gate as the renderer's source check).

---

## Flow: config to PDF

```mermaid
flowchart LR
  config[config_yaml_order]
  labels[sec_fig_eq_labels]
  refs[cref_and_cite]
  pdf[pdf_build]
  config --> labels
  labels --> refs
  refs --> pdf
```

**pytest** invariant modules validate labels, metadata, bibliography, and crossrefs **in parallel** with this chain — run them after any structural manuscript or `ChapterMeta` change.

---

## See also

- [../AGENTS.md](../AGENTS.md) — project root: validation CLI, invariant table, AI protocol
- [docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md) — chapter file contract, allowlists, paths
- [manuscript_guide.md](manuscript_guide.md) — templates, LaTeX patterns, equation decision tree
- [pipeline_guide.md](pipeline_guide.md) — full pipeline and maintenance script table
- [visualization_guide.md](visualization_guide.md) — matplotlib and Mermaid conventions
- [testing_guide.md](testing_guide.md) — zero-mock policy, "what test catches what mistake"
- [api_reference.md](api_reference.md) — `ChapterMeta` and `crossref_validator` entry points
- [accessibility.md](accessibility.md) — `config.yaml` flags advisory vs test-enforced; reader PDF profile
- [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md) — Bloom's taxonomy and LO ↔ question-bank mapping
