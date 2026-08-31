# Agent Instructions (biology_textbook)

> [!NOTE]
> **See also:** [manuscript_guide.md](manuscript_guide.md) for LaTeX patterns; [composable_authoring.md](composable_authoring.md) for stable IDs and workflows; [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md) for objective-question mapping. **This file is editorial** (voice, narrative arc, clinical boxes); the structural contract is in [../manuscript/AGENTS.md](../manuscript/AGENTS.md).

---

## Table of contents

- [Scope](#scope)
- [Editorial voice guide](#editorial-voice-guide)
- [Inclusive and global context](#inclusive-and-global-context)
- [Non-negotiables](#non-negotiables)
- [Scientific writing standards](#scientific-writing-standards)
- [How to write opening vignettes](#how-to-write-opening-vignettes)
- [How to write concept checks](#how-to-write-concept-checks)
- [How to write clinical connections](#how-to-write-clinical-connections)
- [Chapter structure checklist](#chapter-structure-checklist)
- [Manuscript conventions](#manuscript-conventions)
- [Before editing](#before-editing)
- [Quick troubleshooting](#quick-troubleshooting)
- [Commands](#commands)

---

## Scope

These instructions apply when modifying the active `biology_textbook` project directory. Template-hosted render and validation entry points still use `--project biology_textbook` when the template infrastructure is available.

> [!IMPORTANT]
> **Source of truth (mechanical rules):** If anything here disagrees with [../manuscript/AGENTS.md](../manuscript/AGENTS.md) or the test suite, **the manuscript contract and tests win** — especially for `\label` / `\cref` naming, figure paths, and cross-references. This file is **editorial** (voice, structure, teaching style); [../manuscript/AGENTS.md](../manuscript/AGENTS.md) and [composable_authoring.md](composable_authoring.md) are **composable / structural** (how to add chapters, modules, and figures without breaking the build).

End-to-end checklists: [composable_authoring.md](composable_authoring.md).

---

## Editorial voice guide

The textbook reads as a **single, calm, expert voice** — quantitative where biology is quantitative, narrative where biology is historical. Drift between contributors is the most common quality regression; the rules below collapse that drift.

### Tone

| Property | Target | Example |
| -------- | ------ | ------- |
| Register | Educated reader (advanced undergraduate / early graduate); no jargon without unpack | "Phosphorylation cascade" → first usage glossed; later usage assumed |
| Confidence | Assert what is known; cite what is uncertain; flag what is contested | "The mitochondrial membrane potential typically sits near $-150$ mV \citep{nicholls2013}." |
| Warmth | Briefly warm in vignettes and clinical boxes; neutral in body text | Vignette OK: "Hodgkin and Huxley sat in a small Plymouth lab in 1949..." |
| Humour | Sparing, dry, never at the expense of a community | A single ironic aside per chapter at most |
| Authority | Earned through specifics, not claimed | Avoid "obviously", "clearly", "trivially" |

### Person and number

> [!TIP]
> **Rule of thumb:** **second-person ("you")** for *instructions* (worked examples, concept checks, lab procedures); **third-person** for *description* (body text, vignettes, summaries). Never first-person plural ("we") in body text — it suggests the author and reader are co-experimenting, which collapses authority.

| Context | Use | Avoid |
| ------- | --- | ----- |
| Body text (description) | Third person ("the cell hydrolyses ATP") | First person ("we hydrolyse ATP") |
| Worked examples (instruction) | Implicit second person ("To compute $K_m$, divide...") | First person ("I compute...") |
| Vignettes (description) | Third person about the historical figure | First person ("I will tell you a story...") |
| Concept Checks (instruction) | Second person, present tense ("You measure...") | Past tense, conditional ("One would have measured...") |
| Lab procedures (instruction) | Imperative second person ("Add 5 mL of buffer...") | Passive ("5 mL of buffer should be added...") |
| Summaries (description) | Third person, declarative ("ATP hydrolysis releases ~30 kJ/mol") | Second person ("You learned that ATP...") |

### Active vs passive voice

> [!TIP]
> Default to **active voice**. Use passive only when the agent is unknown or irrelevant.

| Active (preferred) | Passive (acceptable when agent is unknown) |
| ------------------ | ------------------------------------------ |
| "Hexokinase phosphorylates glucose." | "Glucose is phosphorylated at C6." (when the enzyme is the topic two paragraphs later) |
| "The Krebs cycle releases two CO₂ per acetyl-CoA." | "Two CO₂ are released per turn of the cycle." |
| "Watson and Crick proposed the double helix." | "The double helix was proposed in 1953." (only if the contributors are not the focus) |

### Precision of language

| Imprecise | Precise |
| --------- | ------- |
| "lots of ATP" | "30–32 ATP per glucose under aerobic conditions" |
| "the enzyme is fast" | "$k_{\text{cat}} = 1400$ s$^{-1}$" |
| "many neurons" | "≈ 86 billion neurons in the adult human brain \citep{azevedo2009}" |
| "high temperature" | "37°C" or "near body temperature" |
| "very small" | "10–100 nm in diameter" |
| "could affect" | Either "increases X by Y%" or omit |
| "it is thought" | "Researchers in the 1980s proposed..." or cite specific authors |

### Word choices

| Avoid | Prefer |
| ----- | ------ |
| "obviously", "clearly", "trivially" | (delete; let the reader judge) |
| "very", "really", "quite" | (delete; specifics replace intensifiers) |
| "in order to" | "to" |
| "due to the fact that" | "because" |
| "utilize" | "use" |
| "demonstrate" (overused) | "show" |
| "revolutionized" (overused) | "transformed" or specifics: "raised yields by 4-fold" |
| "the central dogma" (overused) | "the DNA → mRNA → protein flow" (and use sparingly) |

---

## Inclusive and global context

- **Vignettes and clinical boxes:** use **varied** names, settings, and conditions where it serves the science (no tokenism; avoid stereotype as shorthand). Primary literature and landmark examples remain the default anchor.
- Cite **non-Western** discoveries by their original authors and contexts where applicable (e.g. Ibn al-Nafis on pulmonary circulation; Rosalind Franklin on the X-ray data underlying the double helix).
- For named diseases, use the name preferred by current professional medical bodies (e.g. "Wegener's granulomatosis" → "granulomatosis with polyangiitis").

---

## Non-negotiables

- **Thin orchestrators**: keep computation in `src/`; scripts in `scripts/` orchestrate I/O only.
- **No mocks**: do not use `MagicMock`, `mocker.patch`, or `unittest.mock` in tests.
- **Deterministic outputs**: fixed RNG seeds for simulations/plots; headless matplotlib (`MPLBACKEND=Agg`).
- **No generated outputs committed**: treat `output/` as disposable.
- **Real data only**: all tests use real algorithms and numerical data; no stub returns.

---

## Scientific writing standards

When writing or editing manuscript chapters:

1. **Quantitative claims require values.** Do not write "enzymes lower activation energy" — write "lactate dehydrogenase ($K_m = 0.8$ mM; $k_{\text{cat}} = 1400$ s$^{-1}$) lowers activation energy from ~80 to ~40 kJ/mol."
2. **Citation format:** author(s) year in parentheses for inline (e.g. *(Hodgkin & Huxley, 1952)*); use full journal name in landmark tables.
3. **LaTeX math:** `$...$` for inline, `$$...$$` for display. Prefer descriptive names: `$K_m$` not just `$K$`. See [manuscript_guide.md#equations](manuscript_guide.md#equations) for the cross-reference decision tree.
4. **Figures (LaTeX):** raw `\begin{figure}...\end{figure}` with `\caption{...}` and `\label{fig:unit_X_<descriptor>}`; refer in prose with `\cref{fig:...}`. **Do not** hand-type "Figure 4.2" in prose. After each figure block, an `<!-- alt: ... -->` HTML comment is **required** ([test_accessibility.py](../tests/test_accessibility.py)).
5. **Figures (Mermaid):** after each ` ```mermaid ` block, include exactly one `<!-- alt: ... -->` comment and one *italic* descriptive caption; no hand-numbered "Figure N.M" in prose. The manuscript currently contains 197 inline Mermaid fences (196 outside README/AGENTS documentation files), including current-evidence maps; keep captions specific enough that a reader can interpret the figure without color.
6. **Mermaid types:** `flowchart LR` (pathways), `sequenceDiagram` (signal cascades), `flowchart TD` / `graph TD` (hierarchies). Node labels in sentence case, < 30 characters; wrap labels with parentheses or colons in `"..."`.
7. **Clinical Connection:** blockquote `> **Clinical Connection:**`. One per major section. Reference drug names with class, mechanism, and approval status.
8. **Concept Check:** one per major section (not per subsection). Format: `> **Concept Check:** \<integrative question\>`.
9. **SI units:** always use SI (kJ/mol, Pa, mol/L or mM, s or ms). Non-SI where biologically conventional (mmHg for blood pressure; mV for membrane potential).
10. **Embedded additions:** preserve the 44-chapter / 39-lab / 39-question-bank structure. Add current biology, accessibility, and pedagogy upgrades inside existing sections unless the user explicitly asks for a structural change.
11. **Question banks:** keep exactly 30 questions and 30 solution blocks per bank. Answers should name the chapter-specific mechanism, evidence, common pitfall, and scoring expectation; do not leave generic rubrics or old generator labels such as `Expected reasoning:`, `Key answer:`, `Mechanistic answer:`, or `Chapter evidence:`.
12. **Paper-based labs:** required lab work must run with printed datasets, cards, diagrams, tables, decision matrices, and ordinary discussion tools. Wet or equipment-based versions belong only in clearly optional extension sections.
13. **Current-science claims:** cite or qualify recent claims, especially clinical approvals, disease-burden numbers, AI biomolecular modeling, pangenome/long-read genomics, AMR, biodiversity, fisheries, and conservation assessments.
14. **Scholarship intake:** use current web or Perplexity-style discovery only as an intake layer. Before adding manuscript prose, verify the final claim against an authoritative institutional or primary source such as WHO, CDC, FDA, UNAIDS, NIH/HPRC, NAR, Nature, Blood, IPBES, IUCN, WWF, FAO, NOAA, or IPCC.
15. **Recent frontier topics:** when editing the current-science surfaces, check for relevant updates in AlphaFold/AFDB interaction models, pangenome graph reasoning, approved or investigational genome editing, BPaL/BPaLM tuberculosis regimens, fungal AMR including *Candida auris*, malaria vector-control tools, PrEP modalities, Long COVID mechanisms, coral heat tolerance, and food-system biodiversity links.

---

## How to write opening vignettes

The Opening Vignette is a **historically grounded narrative** (**150–300 words**, hard target) that opens each chapter. It earns reader trust by anchoring abstract content in real people, places, and tools.

### Structure (four-beat arc: hook → context → significance → connection)

| Beat | Purpose | Word budget |
| ---- | ------- | ----------- |
| **1. Hook (setting)** | Concrete sensory image — time, place, characters, instrument-of-the-era. Pulls the reader in. | 30–60 words |
| **2. Historical context (the puzzle)** | The specific question or anomaly that drove the work; what was known and unknown then. | 30–60 words |
| **3. Significance (the pivotal observation / experiment)** | What they actually did or saw, and why it mattered as a *first*: what changed in the field. | 50–100 words |
| **4. Connection to chapter** | Why this transforms what the reader is about to learn — explicit hand-off to the body of the chapter. | 30–60 words |

### Sourcing requirement

> [!IMPORTANT]
> Every vignette **must cite at least one primary source** via `\citet{}` or `\citep{}`. Wikipedia, textbook re-tellings, and unsourced legend are not acceptable anchors. Where the historical record is contested (e.g. Franklin's role in the helix discovery), acknowledge the contest with a one-line caveat and cite both sides.

### Additional sourcing tips

- Use **named instruments and locations** ("the squid giant axon at the Marine Biological Association lab in Plymouth", not "a lab").
- Quote sparingly (one short quote at most); paraphrase otherwise.
- Prefer **specific dates** ("In June 1953…") over vague timeframes ("In the early 1950s…") when the primary source supports it.

### Example (~220 words)

```markdown
> **Opening Vignette — The Squid Giant Axon**
>
> In the summer of 1949, Alan Hodgkin and Andrew Huxley returned to the Marine
> Biological Association laboratory in Plymouth, three years after war work had
> interrupted their pre-war experiments. Their target was the giant axon of the
> squid *Loligo forbesii* — a single nerve fiber nearly half a millimetre thick,
> wide enough to thread with a thin glass capillary electrode.
>
> The puzzle was sharp: nerve impulses propagated faithfully over meters, but
> nobody knew how a cell membrane could *generate* the brief reversal of voltage
> that constituted a spike. Was the membrane simply leaking, or was it actively
> driving current?
>
> Hodgkin and Huxley refined a "voltage clamp" that held the membrane potential
> at a chosen value while measuring the current required to do so. Across hundreds
> of trials they isolated two ionic conductances — one fast and inward, one slow
> and outward — that obeyed kinetics they could fit with a few coupled
> differential equations \citep{hodgkin1952quantitative}. The fit was so precise that the
> equations could *predict* the action potential's shape from first principles.
>
> Within a decade, this framework reshaped neurophysiology, electrocardiology,
> and ion-channel pharmacology. We will reconstruct it from the same starting
> point — Ohm's law, the Nernst equation, and a careful budget of currents
> across a small piece of membrane.
```

### Anti-patterns

- ❌ "Imagine you are a tiny molecule travelling through a cell..." (juvenile framing)
- ❌ "Did you know that..." (rhetorical question)
- ❌ "Throughout history, scientists have..." (sweeping, content-free)
- ❌ Pure plot summary with no setting or instrument
- ❌ Citing a Wikipedia article instead of primary literature

---

## How to write concept checks

A **Concept Check** is a short integrative question that asks the reader to *apply* the section's idea, not just recall it.

### Cognitive levels to span across a chapter

A chapter's three Concept Checks should not all sit at the same Bloom level. Aim for at least one at **Apply** and one at **Analyze**, with optional **Evaluate** or **Synthesis** on capstone sections. See [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md) for the verb tables.

| Level | Concept-check archetype | Example stem |
| ----- | ----------------------- | ------------ |
| **Recall** (rare; usually too shallow) | "List…", "Name…" | "List the four nucleotide bases." (avoid as a Concept Check) |
| **Apply** | "Compute…", "Predict…", "Use … to calculate…" | "Given $K_m$ and $V_{\max}$, compute $v_0$ at $[S]$ = 0.5 mM." |
| **Analyze** | "Identify which term…", "Distinguish…", "Diagram…" | "Identify which Goldman-equation term drives a 20 mV depolarization." |
| **Evaluate / synthesis** | "Justify…", "Choose between…", "Sketch and explain…" | "Two species share intrinsic growth rate but differ in $K$. Sketch their trajectories and identify the time of maximal divergence." |

### Good question design

| Property | Detail |
| -------- | ------ |
| **Integrative** | Pulls together at least two ideas from the section |
| **Computable or reasoned** | The reader can answer with pencil + the section's content; no outside lookup |
| **Diagnostic** | Wrong answer reveals a specific misconception |
| **One sentence** | Long set-ups belong in worked examples, not Concept Checks |
| **Not yes/no** | "Why" / "Which" / "Compute" / "Predict" beats "Is it true that..." |

### Templates

```markdown
> **Concept Check:** Given $K_m = 2$ mM and $V_{\max} = 8$ µmol min$^{-1}$, what
> is the initial rate when $[S] = 0.5$ mM, and how does it compare with the rate
> at saturating substrate?
```

```markdown
> **Concept Check:** A cell loses 30% of its K⁺ pumps. Predict the direction
> and order-of-magnitude change in the resting membrane potential, and explain
> which term in the Goldman equation drives that change.
```

```markdown
> **Concept Check:** Two species with identical intrinsic growth rates differ
> only in carrying capacity. Sketch their logistic trajectories starting from
> the same $N_0$, and identify the time at which their populations diverge most
> sharply.
```

### Anti-patterns

- ❌ "Is the membrane potential negative?" (closed yes/no)
- ❌ "Define $K_m$." (recall, not application)
- ❌ Multi-part questions with five sub-questions (move to a worked example or end-of-chapter problem set)
- ❌ Questions whose answer is the next sentence in the body text

---

## How to write clinical connections

A **Clinical Connection** is a blockquote that links the section's biology to a medical phenomenon, drug, diagnostic, or public-health context.

### Structure (clinical connection format)

The four-beat skeleton: **drug name → mechanism → clinical indication → side effects**. Skipping any beat weakens the box.

| Beat | Purpose | Example fragment |
| ---- | ------- | ---------------- |
| **1. Drug name (or condition)** | One-sentence framing — generic name, class, brief context | "Digoxin (cardiac-glycoside class), a refined extract of *Digitalis lanata*…" |
| **2. Mechanism** | Why does the section's biology cause / treat / diagnose this? | "…blocks the Na⁺/K⁺-ATPase. The resulting elevation of intracellular Na⁺ reduces the driving force for the Na⁺/Ca²⁺ exchanger, leaving more cytosolic Ca²⁺…" |
| **3. Clinical indication + numbers** | What is it used to treat, at what dose, in what population? At least one quantitative anchor (dose, prevalence, sensitivity / specificity, therapeutic range) | "At therapeutic doses (0.5–2.0 ng/mL serum), this strengthens systolic ejection in heart failure with reduced ejection fraction…" |
| **4. Side effects / caveat** | When does this break? What is contested? Common adverse events; therapeutic-index warnings | "…at higher doses the same mechanism causes the arrhythmias for which digoxin toxicity is notorious." |

### Drug-name conventions

| Element | Example |
| ------- | ------- |
| Generic name | vorinostat |
| Class in parentheses on first use | (HDAC inhibitor) |
| Mechanism in one phrase | "blocks histone deacetylases, restoring transcription at silenced loci" |
| Approval status (FDA / EMA) | "approved by the FDA in 2006 for cutaneous T-cell lymphoma" |
| Dose if relevant | "400 mg orally once daily" |

### Example

```markdown
> **Clinical Connection: Cardiac Glycosides**
>
> Digoxin (cardiac-glycoside class), a refined extract of *Digitalis lanata*,
> blocks the Na⁺/K⁺-ATPase. The resulting elevation of intracellular Na⁺
> reduces the driving force for the Na⁺/Ca²⁺ exchanger, leaving more cytosolic
> Ca²⁺ available for cardiac contraction. At therapeutic doses (0.5–2.0 ng/mL
> serum), this strengthens systolic ejection in heart failure with reduced
> ejection fraction; at higher doses the same mechanism causes the
> arrhythmias for which digoxin toxicity is notorious. The therapeutic index
> is narrow enough that serum monitoring is standard \citep{digitalis_inv_group_1997}.
```

### Anti-patterns

- ❌ "This is important in medicine." (vague; no mechanism)
- ❌ Listing five drugs without picking one to anchor on
- ❌ Citing a tertiary source (textbook, Wikipedia) for a clinical claim
- ❌ Forgetting the dose or prevalence number — Clinical Connections must carry at least one quantitative anchor

---

## Chapter structure checklist

Every chapter must have, in this order:

- [ ] `# Chapter Title` heading (the chapter NUMBER is injected automatically at render time from `config.yaml` order)
- [ ] `\label{sec:unit_X_<stem>}` immediately after the title (inserted by `scripts/insert_crossref_labels.py`). Refer via `\cref{sec:unit_X_<stem>}` — **never** hand-type chapter numbers in prose.
- [ ] `<!-- chapter-metadata-badge -->` blockquote (inserted by `scripts/insert_chapter_metadata.py` from `src/biology/chapter_metadata.py`) showing difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites
- [ ] `## Learning Objectives` — 7–9 numbered items; each begins with an action verb (Describe, Explain, Apply, Calculate, Compare, Evaluate). See [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md) for Bloom's-taxonomy guidance.
- [ ] `---` horizontal rule
- [ ] `> **Opening Vignette — [Historical Figure/Discovery]**` — 150–300 words; historically grounded; shows quantitative reasoning in discovery
- [ ] `## N First section` through `## N.M Last section` — section numbers are auto-assigned by pandoc; keep `##` level for sections
- [ ] At least 2 mermaid diagrams with figure captions
- [ ] At least 1 worked numerical example (`$$...$$` calculation with step-by-step solution)
- [ ] At least 3 `> **Clinical Connection:**` boxes
- [ ] At least 2 `> **Concept Check:**` questions
- [ ] `## Summary` — bullet list of all key points, one bullet per major section
- [ ] `## Key Terms` — markdown table with two columns: Term (bold) | Definition. Terms that appear in `manuscript/glossary.md` should be linked on first use as `[**term**](#gl:term-slug)`
- [ ] `## Review Questions` — 8–10 numbered questions mixing quantitative calculation, conceptual explanation, and clinical application
- [ ] Module reference footer: ``*Module: `src/biology/<domain>/<file>.py` (functions: ...)*``

> [!IMPORTANT]
> **Invariants vs authoring targets:** counts above (e.g. Mermaid ≥ 2, clinical boxes ≥ 3) are **pedagogical targets**. Only what **invariant tests** assert (see `tests/test_build_invariants.py`, `test_accessibility.py`) is fail-on-CI. A methods-heavy or narrative-only chapter may **reduce** callouts *after* a note in the opening metadata or a maintainer review — do not strip `\label` / `\cref` / module footers.

**Optional** `> **Common confusion:**` (one per chapter at most): a short contrast between a frequent misconception and the definition used in the text — **not** a duplicate Concept Check.

**Glossary density:** limit **new** glossary-linked terms to roughly **three per major section** where possible, so paragraphs do not become a "link wall." Technical density may exceed this in a few cataloguing sections (e.g. metabolism lists); use judgment.

**Objectives ↔ questions:** optional HTML comment mapping in question banks: [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md).

---

## Manuscript conventions

| Element | Convention | Example |
| ------- | ---------- | ------- |
| Section numbering | Auto at render; source uses `##` titles (optional numeric style in source is for author readability only) | `## DNA Methylation` (not "Chapter 14" in prose) |
| Figure identity | Semantic `\label{fig:unit_X_<descriptor>}`; refer with `\cref{fig:...}`; no "Figure N.M" in prose | `\cref{fig:unit_I_michaelis_menten}` |
| Equation identity | `\label{eq:unit_X_<descriptor>}` in `\begin{equation}...\end{equation}` (or approved pandoc `{#eq:...}` per validator) | `\cref{eq:unit_V_hardy_weinberg}` |
| Subsection | `###` under chapter sections | `### CpG islands` |
| Cross-references (chapter) | `\cref{sec:unit_X_<stem>}` — `stem` matches chapter filename stem | `see \cref{sec:unit_VI_evolution_and_selection}` |
| Cross-references (figure / equation / table) | `\cref{fig:…}` / `\cref{eq:…}` / `\cref{tbl:…}` | `as shown in \cref{fig:unit_I_michaelis_menten}` |
| Citations | Prefer `\citep{…}` (parenthetical) or `\citet{…}` (textual); documented natbib rare forms and optional arguments are parsed by the same citation helper | `\citet{darwin1858}` / `\citep{hodgkin1952quantitative}` |
| Glossary term on first use | `[**term**](#gl:term-slug)` | `[**chemiosmosis**](#gl:chemiosmosis)` |
| Vignette block | `> **Opening Vignette — ...**` using `>` blockquote | — |
| Terms on first use | **Bold** | "**chromatin**" |
| Taxon names | *Italic* | *Drosophila melanogaster* |
| Gene names | *Italic* | *BRCA1*, *TP53* |
| Protein names | Regular (roman) | BRCA1, EZH2 |
| Gene product abbreviations | ALL-CAPS | DNMT1, PRC2 |
| Clinical drug names | Regular + class in parentheses | vorinostat (HDAC inhibitor) |

---

## Before editing

- Read `AGENTS.md` (project overview and module boundaries).
- If changing tests: read [testing_guide.md](testing_guide.md).
- If changing pipeline flow: read [pipeline_guide.md](pipeline_guide.md).
- If adding/editing chapters: read [../manuscript/AGENTS.md](../manuscript/AGENTS.md), [composable_authoring.md](composable_authoring.md), and this file.
- Confirm the chapter file is listed in `manuscript/config.yaml` under the correct unit.

---

## Quick troubleshooting

| Problem | Solution |
| ------- | -------- |
| LaTeX compilation fails on `??` | Unresolved cross-reference; check `\label{}` / `\ref{}` spelling |
| Mermaid diagram not rendering | Check for special characters in node labels; wrap in `"..."`; avoid `(`, `)` outside quotes |
| Coverage gate fails (< 90%) | Add tests in `tests/test_*.py`; no mocks; use real numerical inputs |
| `MPLBACKEND` error | Set `import matplotlib; matplotlib.use("Agg")` before any `pyplot` import |
| Multiple blank lines lint warning | Use single blank line between sections; avoid double-blank |
| Vignette trailing space (MD009) | Ensure `> ` line has no trailing spaces; use `> ` not `>  ` |
| `xelatex` aborts on a `$$` block | Likely manual numbering mixed with a label — see [manuscript_guide.md#equations](manuscript_guide.md#equations) |
| `bibtex` aborts on "Illegal `\bibstyle`" | `\bibliographystyle{plainnat}` was redeclared in `preamble.md` — remove it |

---

## Commands

```bash
# Tests (from the active project directory)
uv run python -m pytest tests/ --cov=src --cov-fail-under=90        # full suite + coverage gate

# Validate manuscript markdown (from template repository root)
uv run python -m infrastructure.validation.cli markdown /path/to/biology_textbook/manuscript/

# Strict source gate (template root): same pitfalls + undefined citations as the PDF prerender
uv run python -m infrastructure.validation.cli prerender /path/to/biology_textbook/manuscript/ --repo-root .

# Full analysis + render (template root)
uv run python scripts/02_run_analysis.py --project biology_textbook
uv run python scripts/03_render_pdf.py --project biology_textbook

# Regenerate figures / diagrams directly (from project directory)
uv run python scripts/generate_figures.py       # 42 square-padded matplotlib generators
uv run python scripts/generate_diagrams.py      # 24 mermaid diagrams

# Manuscript maintenance (idempotent; each supports --dry-run)
uv run python scripts/insert_crossref_labels.py      # \label{sec:…} + prose → \cref{}
uv run python scripts/sync_curriculum_materials.py   # canonical H1s, appendices, front-matter navigation
uv run python scripts/insert_chapter_metadata.py     # badges + Course Planning Grid
uv run python scripts/integrate_orphan_citations.py  # weave unused references.bib entries
uv run python scripts/link_glossary.py               # glossary anchors + verify chapter numbers
uv run python scripts/link_labs_to_chapters.py       # \cref from every lab/question to parent
uv run python scripts/insert_orphan_figures.py       # add \begin{figure}…\end{figure} for unused generators
uv run python scripts/normalize_typography.py        # ASCII arrows → Unicode (prose only)
uv run python scripts/fix_greek_math_prose.py        # $\greek$ → Unicode (prose only; sidesteps pandoc quirk)
```

---

## Editorial spot-check (2026-04-23)

Four chapters were sampled against the **Chapter Structure Checklist** above: `unit_0/systems_science.md`, `unit_IV/dna_replication_and_cell_cycle.md`, `unit_IX/nervous_system.md`, `unit_X/biomes_and_conservation.md`.

- All four include Learning Objectives, an opening vignette, multiple Mermaid diagrams, and concept checks.
- `systems_science.md` uses a `## Opening Vignette` section heading; other samples use blockquote vignettes — both are acceptable if the publisher style is consistent.
- `systems_science.md` has no literal `**Clinical Connection:**` boxes; prelude material sometimes uses integrative "Concept Check" items instead. The checklist targets (e.g. ≥3 clinical boxes per chapter) are **aspirational** for discipline-spanning units — apply them to new and revised chapters where they fit.

---

## See also

- [manuscript_guide.md](manuscript_guide.md) — LaTeX patterns, equation decision tree, citation commands
- [composable_authoring.md](composable_authoring.md) — stable IDs and workflows
- [pedagogy_objectives_mapping.md](pedagogy_objectives_mapping.md) — Bloom's taxonomy, objective-question mapping
- [testing_guide.md](testing_guide.md) — what test catches what mistake
- [accessibility.md](accessibility.md) — alt-text writing guide, CVD checklist
- [../manuscript/AGENTS.md](../manuscript/AGENTS.md) — manuscript contract
