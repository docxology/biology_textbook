# Biology Textbook — Agent Documentation

## Location and pipeline status

This project is currently maintained as an active standalone checkout; run project-local commands from this directory so `pyproject.toml` applies. Template-hosted render entry points still use `--project biology_textbook` and resolve the project through the template infrastructure when available. **Publication:** `docs/manuscript/config.yaml` → `publication.doi` and `publication.repository_url` (Zenodo + GitHub).

Work here uses the same patterns as active template projects: thin orchestrators in `scripts/`, computation in `src/`, manuscript in `docs/manuscript/`, tests in `tests/` (zero mocks, ≥90% line coverage on `src/`).

**Composable authoring (stable `sec:` / `fig:` / `eq:` IDs, script order, which tests fail when):** [docs/composable_authoring.md](docs/composable_authoring.md). **Editorial** style for agents: [docs/agent_instructions.md](docs/agent_instructions.md). **Accessibility / config enforcement vs advisory:** [docs/accessibility.md](docs/accessibility.md). **Doc index:** [docs/README.md](docs/README.md).

## Manuscript Source Contract

Introductory biology textbook content is driven by **`docs/manuscript/config.yaml`**: unit ordering, chapter files, front matter, appendices (labs and question banks), and render metadata. Nine domain subpackages under `src/biology/` implement quantitative models. Mermaid diagrams are declared in **`src/mermaid/diagram_specs.yaml`** and built via `src/mermaid/diagram_spec_loader.py`; matplotlib figures live in **`src/visualization/plots_*.py`** modules and register through `plots.py` → `ALL_FIGURE_GENERATORS`.

Canonical chapter counts and filenames are **only** in `config.yaml` (currently Unit 0 plus Units I–X, **44 core chapter files**, 44 paper-based labs, and 44 question banks of 30 questions each). All 44 chapters carry:

- `\label{sec:unit_X_<stem>}` immediately after the H1 title (for `\cref{}` cross-referencing)
- A `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites
- An Opening Vignette, Learning Objectives, and a Summary block

Current-claim and assessment surfaces are first-class maintenance workflows: `docs/manuscript/current_claims.yaml` is parsed by `src/biology/current_claims.py` and checked by `scripts/audit_current_claims.py --check`; question-bank item metadata and lab outcome/rubric alignment are parsed by `src/biology/assessment.py`, synchronized by `scripts/sync_assessment_metadata.py` (`--dry-run` previews drift; `--check` gates), and checked by `tests/test_assessment_metadata.py` plus `tests/test_lab_pedagogy_alignment.py`.

---

## PDF typography and page layout

Student PDFs are built **compact** by default:

| Setting | `docs/manuscript/config.yaml` | `docs/manuscript/preamble.md` (LaTeX) |
| ------- | ------------------------ | -------------------------------- |
| Margins | `layout.margin_*_mm` → **2** | `geometry` → **2 mm** all sides, `headheight=12pt` |
| Body size | `typography.base_font_size_pt` → **9** | `\renewcommand{\normalsize}{...9}{10.8}...` |
| Line spacing | `layout.line_height` → **1.28** | `\setstretch{1.28}` |
| Headings / captions | (metadata only) | `titlesec` sizes; `caption` → `footnotesize`; header/footer → `footnotesize` |

**Rule:** Changing density requires editing **both** files so YAML comments and the rendered PDF stay aligned. Full authoring rules (figure/diagram allowlists, footers) are in [docs/manuscript/AGENTS.md](docs/manuscript/AGENTS.md).

---

## Domain modules (`src/biology/`)

| Subpackage | Typical manuscript topics |
| ---------- | ------------------------- |
| `biochemistry/` | Enzyme kinetics, ΔG, pathways |
| `cell/` | Organelles, Nernst/Goldman, transport, signaling |
| `genetics/` | DNA/RNA, Punnett, Hardy–Weinberg, genomics |
| `evolution/` | Selection, drift, clock, speciation |
| `ecology/` | Growth models, Lotka–Volterra, diversity |
| `physiology/` | Circulation, gas transport, homeostasis |
| `microbiology/` | Growth curves, MIC, viral parameters |
| `botany/` | Water relations, photosynthesis pathways |
| `neuroscience/` | Hodgkin–Huxley, passive cable, synaptic transmission, Hebbian plasticity |

Shared utilities: `numerics.py` (Euler integration), `constants.py` (physical constants), `assessment.py`, `chapter_metadata.py`, `current_claims.py`, `toc.py`.

Maintenance packages (logic in `src/`, thin CLIs in `scripts/`):

| Package | Script | Role |
| --- | --- | --- |
| `crossref/` | — | Manuscript `\label`/`\cref` scanner (re-exported as `crossref_validator.py`) |
| `quality/` | `audit_textbook_quality.py` | Umbrella quality audit + advisory ledger |
| `enrichment/` | `enrich_embedded_textbook.py` | Frontier boxes, companion modules, audit matrix |
| `answer_refinement/` | `refine_generated_answers.py` | Question-bank answer heuristics |
| `curriculum_sync/` | `sync_curriculum_materials.py` | Curriculum scaffolds + front matter |
| `visual_contracts.py` | `audit_visual_contracts.py` | Figure/diagram manifest gate |

Root I/O: `textbook_io.py` (`write_text_atomic`); `textbook_paths.py` for shared path helpers.

---

## Source layout

```text
src/
├── __init__.py
├── textbook_io.py              # atomic write/replace for maintenance scripts
├── biology/
│   ├── numerics.py             # euler_integrate_scalar()
│   ├── constants.py            # FARADAY, GAS_CONSTANT, …
│   ├── assessment.py           # question/lab metadata parser + enum enforcement
│   ├── chapter_metadata.py     # CHAPTERS_BY_ID, difficulty/time badges
│   ├── crossref_validator.py   # thin re-export shim → crossref/
│   ├── crossref/               # scan_file, validate (see crossref/AGENTS.md)
│   ├── quality/                # audit engine (see quality/AGENTS.md)
│   ├── enrichment/             # embedded enrichment (see enrichment/AGENTS.md)
│   ├── answer_refinement/
│   ├── curriculum_sync/
│   ├── visual_contracts.py
│   ├── biochemistry/ … neuroscience/   # nine domain subpackages
│   └── …
├── mermaid/
│   ├── diagram_specs.yaml      # declarative nodes/edges for 24 biology diagrams
│   ├── diagram_spec_loader.py  # YAML → MermaidDiagram builders
│   ├── biology_diagrams.py     # factory registry + ALL_BIOLOGY_DIAGRAMS
│   ├── diagrams.py             # flowchart, sequence, state builders
│   └── renderer.py
└── visualization/
    ├── _scaffold.py            # Agg backend, _save_figure, palette constants
    ├── plots.py                # ALL_FIGURE_GENERATORS registry (~50 lines)
    ├── plots_cell.py           # domain figure generators
    ├── plots_genetics.py
    ├── plots_ecology.py
    ├── plots_physiology.py
    ├── plots_botany.py
    └── plots_microbiology.py
```

### Mermaid CLI and `.puppeteer.json`

Optional repo file **`.puppeteer.json`** (project root) is passed to `mmdc --puppeteerConfigFile` when present so diagram rendering can use a system Chrome install. Adjust or remove it on non-macOS hosts. If `mmdc` is missing, the renderer writes `.mmd` sources only.

---

## Directory structure

```text
biology_textbook/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── .puppeteer.json          # optional; for mmdc + system Chrome
├── src/                     # biology, mermaid, visualization
├── scripts/                          # 36 Python files — core build vs. content maintenance
│   ├── add_mermaid_alt_text.py        # audit/normalize Mermaid alt text + captions; --check gate
│   ├── atomic_io.py                   # atomic write/replace helper for mutating scripts
│   ├── audit_current_claims.py        # current-claims ledger and stale-phrase gate
│   ├── audit_publication_readiness.py # project-local publication-readiness gate
├── annotate_table_captions.py         # insert Table: … {#tbl:…} captions before pipe tables
├── polish_table_captions.py           # polish existing pandoc table captions
├── normalize_american_english.py      # British → American spelling normalizer
├── repair_split_chapter_shells.py     # repair pedagogy shells on split chapters
│   ├── audit_textbook_quality.py       # umbrella docs/manuscript/lab/question/current-claim quality gate; --check gate plus quality_advisories.yaml
│   ├── audit_visual_contracts.py       # visual manifest gate
│   ├── biology_analysis.py            # config-driven full-textbook collect + analysis JSON; copies references.bib + preamble → output/manuscript/
│   ├── bold_glossary_first_use.py     # bold + link glossary terms on first use in chapters
│   ├── check_pdf_log.py               # fail undefined refs + severe overfull boxes in XeLaTeX logs
│   ├── extract_glossary_cards.py       # export glossary cards for study/review workflows
│   ├── fill_answer_scaffolds.py      # fill remaining instructor scaffolds in question banks
│   ├── fix_greek_math_prose.py        # replace $\greek$ in prose with Unicode
│   ├── enrich_embedded_textbook.py      # embedded frontier boxes, lab upgrades, answer-key refinement, audit matrix
│   ├── generate_cover_art.py          # deterministic text-free cover montage asset
│   ├── generate_diagrams.py         # 24 mermaid → PNG (or .mmd)
│   ├── generate_figures.py            # 42 matplotlib figure generators
│   ├── insert_answer_keys.py         # answer-key blocks in question banks
│   ├── insert_chapter_metadata.py    # metadata badges + Course Planning Grid
│   ├── insert_crossref_labels.py     # \label{sec:…} + rewrite legacy chapter prose → \cref
│   ├── insert_further_reading.py     # add ## Further Reading from citations
│   ├── insert_orphan_figures.py      # LaTeX figure blocks for unreferenced generators
│   ├── integrate_orphan_citations.py # weave orphan BibTeX keys into narrative
│   ├── link_glossary.py              # {#gl:…} anchors; semantic \cref back-reference check
│   ├── link_labs_to_chapters.py      # \cref to parent chapter in labs + question banks
│   ├── normalize_lab_computational_workflows.py # self-contained optional lab snippets
│   ├── normalize_typography.py        # ASCII arrows → Unicode, HTML-comment-safe
│   ├── pad_short_labs.py              # extend very short lab files
│   ├── refine_generated_answers.py    # rewrites legacy/generated answer scaffolds; --dry-run should be clean
│   └── sync_assessment_metadata.py     # question-item metadata and lab outcome/rubric alignment
├── tests/                            # 70 test_*.py modules; run pytest for current count and coverage
│   ├── conftest.py
│   ├── test_accessibility.py          # alt text + mermaid accessibility contract
│   ├── test_assessment_metadata.py    # item-level question metadata
│   ├── test_atomic_io.py              # atomic write/replace helpers
│   ├── test_audit_v3_and_crossref_gate.py # generic-answer + broken-cref detector regressions
│   ├── test_bibliography_closure.py  # {cited} == {defined} in references.bib
│   ├── test_build_invariants.py      # \label, badges, lab/q cref, figure registry refs
│   ├── test_chapter_metadata.py
│   ├── test_cell_biology.py
│   ├── test_coverage_gap.py
│   ├── test_crossref_validator.py
│   ├── test_crossref_validator_edges.py
│   ├── test_crossref_validator_internals.py
│   ├── test_current_claims_ledger.py
│   ├── test_curriculum_metadata.py
│   ├── test_ecology_evolution_physiology_biochemistry.py
│   ├── test_enrichment_substance_gate.py # boilerplate/duplicate enrichment detector regressions
│   ├── test_lab_integrity.py
│   ├── test_lab_pedagogy_alignment.py
│   ├── test_mermaid_and_visualization.py
│   ├── test_microbiology_botany_neuroscience.py
│   ├── test_pdf_log_quality.py
│   ├── test_pdf_opening_and_mermaid.py
│   ├── test_question_answer_refinement.py
│   ├── test_chapter_pedagogy_coverage.py # REVIEW §7 pedagogy regression locks
│   ├── test_logging_compat.py
│   ├── test_maintenance_engine_smoke.py
│   ├── test_script_quality.py
│   ├── test_textbook_paths.py           # checkout path discovery + bootstrap helpers
│   ├── test_textbook_quality_audit.py # umbrella stale-claim/copyedit/enrichment quality audit
│   ├── test_american_english.py            # American English spelling gate
│   ├── test_answer_refinement_modules.py   # answer-refinement helper modules
│   ├── test_answer_scaffolds.py            # answer scaffold filling + enrichment answer keys
│   ├── test_assessment_sync.py             # biology.assessment_sync
│   ├── test_chapter_badges.py              # biology.maintenance.chapter_badges
│   ├── test_chapter_shells.py              # biology.maintenance.chapter_shells
│   ├── test_citations.py                   # shared natbib citation parsing helpers
│   ├── test_cover_art.py                   # cover art generation
│   ├── test_crossref_label_insertion.py    # biology.crossref.label_insertion
│   ├── test_diagram_spec_loader.py         # declarative Mermaid diagram specs
│   ├── test_enrichment_catalog_loader.py   # enrichment catalog YAML loader
│   ├── test_foundations.py                 # biology.foundations domain helpers
│   ├── test_further_reading.py             # biology.maintenance.further_reading
│   ├── test_genetics_distance.py           # Hamming + Jukes–Cantor distances
│   ├── test_genetics_epigenetics.py        # CpG methylation decay, histone marks
│   ├── test_genetics_linkage.py            # recombination, map distance, three-point order
│   ├── test_genetics_mendelian.py          # Punnett squares, gametes
│   ├── test_genetics_mutation.py           # mutation-rate spectrum reference data
│   ├── test_genetics_population.py         # Hardy–Weinberg, χ²
│   ├── test_genetics_replication.py        # replication-fork progression
│   ├── test_genetics_sequence.py           # genetic code, transcription, translation, GC
│   ├── test_glossary_cards.py              # glossary card parsing
│   ├── test_glossary_first_use.py          # first-use glossary linking
│   ├── test_lab_padding.py                 # short-lab debrief padding
│   ├── test_lab_workflows.py               # lab computational workflow normalization
│   ├── test_manuscript_spans.py            # protected-span scanning
│   ├── test_numerics.py                    # shared numerical integration helpers
│   ├── test_orphan_citations.py            # orphan citation YAML loader
│   ├── test_orphan_figures.py              # biology.pipeline.orphan_figures
│   ├── test_parent_chapter_links.py        # parent-chapter cross-reference insertion
│   ├── test_pipeline.py                    # biology.pipeline manuscript injection/numbering
│   ├── test_publication_gate.py            # publication gate step graph
│   ├── test_solution_scaffolds.py          # biology.answer_refinement.solution_scaffolds
│   ├── test_table_captions.py              # table caption annotation helpers
│   ├── test_text_normalize.py              # shared Mermaid metadata normalization
│   ├── test_textbook_io.py                 # shared textbook_io helpers
│   ├── test_textbook_visuals.py            # shared figure post-processing helpers
│   ├── test_typography.py                  # manuscript typography normalization
│   ├── test_visual_contracts_audit.py      # visual contract audit helpers
│   ├── test_wip_resolver_smoke.py          # template WIP resolver smoke gate
│   └── test_toc_consistency.py
├── docs/manuscript/
│   ├── config.yaml            # single source of truth for order and units
│   ├── front_matter.md, preface.md, preamble.md, glossary.md, references.bib
│   ├── unit_0/ … unit_X/
│   ├── labs/                  # 44 labs across 11 unit_*/ subdirs
│   └── questions/             # 44 question banks across 11 unit_*/ subdirs
├── docs/                      # architecture, pipeline, testing, API, accessibility, pedagogy
└── output/                    # generated (disposable)
```

---

## Testing

From this project directory:

```bash
uv run python -m pytest tests/ --cov=src --cov-report=html --cov-fail-under=90
```

Run `uv run python -m pytest tests/ --cov=src --cov-fail-under=90` from this project directory so this `pyproject.toml` applies the 90 % gate (repo-root pytest may use the root config). Zero-mock policy — no `MagicMock`, `mocker.patch`, or `unittest.mock` for behavior under test. Invariant-style tests for manuscript quality:

- `test_build_invariants.py` — every chapter has `\label{sec:…}` and a metadata badge; every lab and question bank links back via `\cref{}`; every registered figure generator is referenced
- `test_bibliography_closure.py` — `{cited} == {defined}` in `references.bib`
- `test_crossref_validator*.py` — pandoc-crossref / cleveref label state
- `test_chapter_metadata.py` — `src/biology/chapter_metadata.py` covers every chapter in `config.yaml` with valid difficulty / prerequisites
- `test_accessibility.py` — LaTeX figures and mermaid blocks meet alt/caption contract
- `test_lab_integrity.py` — optional lab computation snippets resolve project modules and do not depend on hidden notebooks or CSVs
- `test_question_answer_refinement.py` — generated answer heuristics stay idempotent and preserve hand-written solutions
- `test_chapter_pedagogy_coverage.py` — REVIEW §7 pedagogy locks: worked-example floor, Concept-Check density, Bloom diversity, LO count floor
- `test_script_quality.py` — project scripts parse and avoid hard-coded checkout paths or obsolete maintenance clones

## Manuscript validation

From a template repository root with infrastructure available, pass the current manuscript path:

```bash
uv run python -m infrastructure.validation.cli markdown /path/to/biology_textbook/manuscript/
uv run python -m infrastructure.validation.cli prerender /path/to/biology_textbook/manuscript/ --repo-root .
```

Use `markdown` after bulk edits; add `prerender` before relying on a clean PDF (same gate as the renderer’s source check).

## Manuscript-wide conventions (enforced by tests)

Every change that adds or renames a chapter, lab, question bank, figure, or BibTeX entry must preserve these invariants:

| Convention | Enforced by | Fix with |
|---|---|---|
| Chapter H1 is followed by `\label{sec:unit_X_<stem>}` | `test_build_invariants.test_every_chapter_has_section_label` | `scripts/insert_crossref_labels.py` |
| Chapter-metadata badge with level / time / prereqs | `test_build_invariants.test_every_chapter_has_metadata_badge` | `scripts/insert_chapter_metadata.py` (data in `src/biology/chapter_metadata.py`) |
| Lab and question files `\cref{sec:unit_X_<stem>}` their parent chapter | `test_build_invariants.test_every_{lab,question}_links_to_parent_chapter` | `scripts/link_labs_to_chapters.py` |
| Every `\citep{…}` / `\citet{…}` resolves; every bib entry is cited | `test_bibliography_closure` | `scripts/integrate_orphan_citations.py` |
| Every figure generator referenced in manuscript | `test_build_invariants.test_every_registered_figure_is_referenced` | `scripts/insert_orphan_figures.py` |
| Registered Mermaid publication output is PNG, not `.mmd` fallback | manual publication gate / renderer strict mode | `scripts/generate_diagrams.py --strict-png` |
| 197 inline Mermaid fences (196 outside README/AGENTS docs) each have one alt comment and one italic caption; PDF preprocessing renders them to PNG | `test_accessibility.py` + `test_pdf_opening_and_mermaid.py` | `scripts/add_mermaid_alt_text.py --check` and install `mmdc` |
| Visual manifest is derived from figures, registered Mermaid, and inline Mermaid; generated manifest lives under `output/figures/` | `audit_visual_contracts.py --check` / publication readiness | `scripts/audit_visual_contracts.py --check` |
| Fast-moving claims carry source, anchor, tier, checked date, and refresh trigger | `test_current_claims_ledger.py` | `scripts/audit_current_claims.py --check` and update `docs/manuscript/current_claims.yaml` |
| Question-bank items and labs carry assessment metadata | `test_assessment_metadata.py` / `test_lab_pedagogy_alignment.py` | `scripts/sync_assessment_metadata.py --dry-run` to preview, then `--check` |
| Glossary terms carry `{#gl:<slug>}` anchors and semantic `\cref{sec:…}` back-references | `test_build_invariants.test_glossary_and_index_use_semantic_chapter_links` + `scripts/link_glossary.py --check` | `scripts/link_glossary.py` |
| Prose uses `\cref{sec:…}` not hand-typed chapter / figure / equation / section numbers | `test_crossref_validator.py::test_no_plain_text_numbered_crossrefs` | `scripts/insert_crossref_labels.py` |
| No ASCII `-->` in prose (use `→`), no `$\greek$` in table cells | (re-run normalizers) | `scripts/normalize_typography.py`, `scripts/fix_greek_math_prose.py` |

The LaTeX preamble (`docs/manuscript/preamble.md`) now loads **cleveref** (after `hyperref` and `amsmath`) so `\cref{sec:foo}` renders as "section 3" and `\Cref{fig:foo}` as "Figure 3.2". Do **not** re-declare `\bibliographystyle{plainnat}` in the preamble — pandoc auto-injects it and a double declaration aborts bibtex.

## Protocol for AI agents

1. For **new chapters, new `plot_*` / `*_diagram()` registrations, or cross-reference refactors**, read [docs/composable_authoring.md](docs/composable_authoring.md) first, then [docs/manuscript/AGENTS.md](docs/manuscript/AGENTS.md).
2. Read [docs/agent_instructions.md](docs/agent_instructions.md) for editorial voice and chapter structure targets.
3. Read [docs/testing_guide.md](docs/testing_guide.md) before changing tests.
4. Read [docs/architecture.md](docs/architecture.md) before changing `scripts/` vs `src/` boundaries.
5. New quantitative claims in prose should map to tested code in the appropriate `src/biology/` module when feasible.
6. Prefer `textbook_logging.get_logger(__name__)` in Python entrypoints; it uses template infrastructure logging when available and falls back to stdlib logging in standalone checkouts.
7. Treat `ALL_FIGURE_GENERATORS` and `ALL_BIOLOGY_DIAGRAMS` as visual manifests: add the generator/factory to the registry, reference it from manuscript prose, keep alt/caption text nearby, and verify the corresponding tests before relying on the visual.
8. After any manuscript edit that adds chapters, figures, diagrams, citations, current claims, labs, or question banks, re-run the relevant `scripts/insert_*` / `scripts/link_*` / `scripts/integrate_*` / audit helper and verify invariant tests still pass (see [docs/testing_guide.md](docs/testing_guide.md) failure-to-fix table).

## See also

- [docs/composable_authoring.md](docs/composable_authoring.md) — stable labels, workflows, validation commands
- [docs/accessibility.md](docs/accessibility.md) — `config.yaml` vs pytest enforcement; CVD; reader profile
- [docs/pedagogy_objectives_mapping.md](docs/pedagogy_objectives_mapping.md) — LO ↔ question-bank comments (optional)
- [docs/README.md](docs/README.md) — documentation index (architecture, pipeline, testing, API, visualization)
- [docs/manuscript/AGENTS.md](docs/manuscript/AGENTS.md) — chapter conventions, `plot_*` / `*_diagram()` allowlist
- [docs/manuscript/README.md](docs/manuscript/README.md) — author quick reference and course pathways
- [Root AGENTS.md](../../AGENTS.md)
- Template exemplar layout: `projects/templates/template_code_project/` in the template repository (this standalone checkout does not embed those paths)
- Template infrastructure: `infrastructure/` in the template repository (`uv run python -m infrastructure.validation.cli …` when run from the template root)
