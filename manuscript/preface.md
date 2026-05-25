# Preface {.unnumbered}

## A Textbook Built With Code {.unnumbered}

Welcome to *Introduction to Biology: A Generative Approach* — an open-source textbook covering introductory biology across **\nameref{sec:unit_0_unit_intro}**, the thematic sequence from **\nameref{sec:unit_I_unit_intro}** through **\nameref{sec:unit_X_unit_intro}**, and **44 core chapters**, plus optional **laboratories** and **question banks** in the appendices. Where this text uses quantitative models, the corresponding computations are implemented as tested Python modules.

Whether we examine Michaelis–Menten enzyme kinetics, Lotka–Volterra predator–prey dynamics, or Hodgkin–Huxley action potentials, the underlying mathematical model exists as a working module in the accompanying codebase. Many figures are generated programmatically. Process diagrams are expressed using Mermaid where it improves clarity. For instructors and independent learners, this supports inspection, extension, and reproducible re-generation of results.

The philosophy is: **understand biology by computing biology**.

**How to read this book digitally:** The reference build is a compact **PDF** with LaTeX typesetting. Not all screen readers handle mathematical notation the same way in PDF; the same sources also produce **HTML** for some workflows. The [biology textbook source repository](https://github.com/docxology/biology_textbook) contains the manuscript, figures, tests, and code; the [Zenodo archival DOI record](https://doi.org/10.5281/zenodo.20286478) identifies a fixed edition snapshot. If you need larger type or margins, a **reader** typography profile is documented (paired edits to `manuscript/config.yaml` and `manuscript/preamble.md` — see `docs/accessibility.md` in the project tree). The book does not re-express every formula in natural language; where precision matters, work through the worked examples and the linked `src/biology` modules.

**Accessible formats:** The compact PDF is optimized for print density, not for every reader. For screen-reader review, HTML/MathJax workflows usually preserve reading order and mathematical navigation better than a dense PDF. Figures and Mermaid diagrams include alt text plus captions, and the large-type reader profile increases margins, font size, and line spacing without changing chapter order or cross-reference IDs.

---

## Five Big Ideas in Biology {.unnumbered}

Biology is a vast and diverse science, but a small set of orienting themes recurs across its subdisciplines.
This book groups them as **Five Big Ideas** (Evolution; Information; Structure and function; Systems and emergence; Cells).
They map pedagogically to the five **core concepts** in AAAS *Vision and Change in Undergraduate Biology Education* \citep{visionandchange2011};
that report also defines six **core competencies** (quantitative reasoning, modeling, data interpretation, and related practice skills),
which this text addresses through labs, models, and inquiry—not as a sixth numbered “big idea” heading.
\nameref{sec:unit_0_unit_intro} adds an optional systems orientation: active inference and the free energy principle are graduate-depth lenses for connecting feedback, prediction, and behavior \citep{friston2017,parr2022activeinference}, not part of the introductory-biology canon that Vision & Change defines for the core undergraduate sequence.
The themes below recur across the units that follow.

### Evolution: the unifying theory of life {.unnumbered}

*\"Nothing in biology makes sense except in the light of evolution.\"* — Theodosius \citet{dobzhansky1973}

Evolution by natural selection explains the origin of species, the genetic code being nearly universal,
the homology between a human arm and a bat wing, and why influenza vaccines must be redesigned every
year. \nameref{sec:unit_VI_unit_intro}, \nameref{sec:unit_V_unit_intro}, and \nameref{sec:unit_IV_unit_intro} develop this idea from population
genetics algorithms to phylogenetic tree reconstruction.

### Structure and function are inseparable {.unnumbered}

A phospholipid bilayer is 7 nm thick and amphipathic — and those two structural facts explain every
property of biological membranes (\nameref{sec:unit_I_unit_intro} and \nameref{sec:unit_II_unit_intro}). The α-helix of hemoglobin's subunits explains its
cooperativity and the Bohr effect (\nameref{sec:unit_I_unit_intro} and \nameref{sec:unit_IX_unit_intro}). The T-shaped architecture of the mitochondrial
ATP synthase explains rotary catalysis (\nameref{sec:unit_III_unit_intro}). In biology, whenever you ask *how*, the answer is
typically embedded in *shape*.

### Information — storage, transfer, expression {.unnumbered}

DNA is not merely a chemical; it is a **code**. An alphabet of four nucleotides encodes a program
of 20 amino acids, creating an effectively unlimited diversity of proteins. \nameref{sec:unit_IV_unit_intro} (Molecular Genetics)
examines the molecular machinery that reads this code — from DNA helicases to ribosomes — and how
errors in the code drive disease and evolution. \nameref{sec:unit_V_unit_intro} (Classical Genetics) examines how the code is
transmitted between generations. \nameref{sec:unit_VII_unit_intro} (Microbiology) shows how viruses inject their own code into
host cells.

### Emergent properties: the whole exceeds the parts {.unnumbered}

A single neuron can fire or remain silent. A brain can think. A single predator can collapse an entire
intertidal community (\nameref{sec:unit_X_unit_intro}). A slight imbalance in NAD⁺/NADH ratio shunts metabolism from aerobic
to anaerobic (\nameref{sec:unit_III_unit_intro}). Emergence — complex behavior arising from simple rules — is everywhere in
biology, and understanding it requires systems thinking: tracking flows, feedback loops, and
nonlinear dynamics, not just cataloguing parts.

### Cells: the universal unit of life {.unnumbered}

Every living organism is composed of one or more cells, sharing a common molecular toolkit:
phospholipid membranes, DNA, ribosomes, ATP. \nameref{sec:unit_II_unit_intro} examines the cell as a physical and computational
system. \nameref{sec:unit_VII_unit_intro} through \nameref{sec:unit_IX_unit_intro} extend this to specialized cells: bacteria, plant cells, neurons, immune cells.
Understanding the cell is not a module to be completed — it is a perspective to carry through every
subsequent chapter.

---

## How Science Actually Works {.unnumbered}

This textbook presents science not as a collection of established facts but as a dynamic, self-correcting
process of inquiry. Understanding how scientific knowledge is generated, tested, and revised is as
important as knowing what is currently accepted.

**The hypothetico-deductive method.** A hypothesis is a testable, falsifiable prediction. Barry
Marshall and Robin Warren's hypothesis that bacteria cause peptic ulcers (not stress) was so contrary
to medical consensus that Marshall famously drank a *Helicobacter pylori* culture to demonstrate the
relationship \citep{marshall1985koch}. Their Nobel Prize-winning work illustrates how a single decisive
experiment can overturn decades of received wisdom.

**Models and computation as scientific tools.** Modern biology is inseparable from mathematical
modeling. The Michaelis-Menten equation (1913) is a model. The Hardy-Weinberg principle is a model.
The Hodgkin-Huxley equations (1952) were Nobel Prize-winning models. A model is not a simplification
that sacrifices truth; it is a commitment to precision — stating *exactly* what you are and are not
claiming. The Python modules in this textbook implement these models so that you can inspect their
assumptions, vary their parameters, and see where they break.

**Primary literature vs. textbook synthesis.** This textbook cites primary papers at point of use.
When you see \"(Author et al., Year, *Journal*)\" inline, that citation points to the experiment or
calculation that established the claim. Science journalism, textbooks, and Wikipedia involve more
layers of interpretation. Primary papers are the ultimate authority — and learning to read them is a
core competency this textbook aims to develop.

**Revision is not failure.** Every chapter in this book contains examples of ideas revised or
overturned: the flat earth was replaced by a spherical one; Lamarckian inheritance was replaced by
Darwinian selection; the DNA double helix replaced protein as the genetic material; the \"lock-and-key\"
enzyme model was replaced by \"induced fit\". A willingness to revise beliefs on evidence is not
weakness — it is the engine of scientific progress.

---

## How to Use the Unit Introductions {.unnumbered}

Each unit begins with a `unit_intro.md` page containing:

- **A narrative hook** explaining why this area of biology matters and what surprises it holds
- **A landmark discoveries table** citing the experiments that established the field
- **A concept map** (Mermaid diagram) showing how the chapters connect to each other and to other units
- **A chapter roadmap** mapping each chapter to its core question and key equation

Use these pages as **advance organisers** — read them before starting the unit and return to them
when you feel you have lost the conceptual thread. The best moment to understand how a jigsaw piece
fits is before you lose sight of the box.

---

## Scope and Organization {.unnumbered}

The textbook proceeds from atoms to ecosystems, following the standard introductory course arc.
The table below is generated from `manuscript/config.yaml`; unit and chapter titles are
semantic references resolved from the canonical manuscript labels.

<!-- preface-scope-start -->
| Instructional block | Core chapters |
| ---- | ------------- |
| **\nameref{sec:unit_0_unit_intro}** | \nameref{sec:unit_0_systems_science}; \nameref{sec:unit_0_complex_adaptive_systems}; \nameref{sec:unit_0_active_inference}; \nameref{sec:unit_0_history_philosophy_biology} |
| **\nameref{sec:unit_I_unit_intro}** | \nameref{sec:unit_I_atoms_molecules}; \nameref{sec:unit_I_water_and_life}; \nameref{sec:unit_I_macromolecules}; \nameref{sec:unit_I_enzymes_and_kinetics} |
| **\nameref{sec:unit_II_unit_intro}** | \nameref{sec:unit_II_cell_theory}; \nameref{sec:unit_II_cell_structure}; \nameref{sec:unit_II_membrane_transport}; \nameref{sec:unit_II_cell_signaling} |
| **\nameref{sec:unit_III_unit_intro}** | \nameref{sec:unit_III_bioenergetics_and_respiration}; \nameref{sec:unit_III_photosynthesis}; \nameref{sec:unit_III_metabolic_integration} |
| **\nameref{sec:unit_IV_unit_intro}** | \nameref{sec:unit_IV_dna_replication_and_cell_cycle}; \nameref{sec:unit_IV_gene_expression}; \nameref{sec:unit_IV_mutations_and_genomics}; \nameref{sec:unit_IV_chromatin_and_epigenetic_mechanisms}; \nameref{sec:unit_IV_epigenetic_inheritance_and_disease} |
| **\nameref{sec:unit_V_unit_intro}** | \nameref{sec:unit_V_mendelian_principles}; \nameref{sec:unit_V_mendelian_extensions_and_human_genetics}; \nameref{sec:unit_V_chromosomal_inheritance}; \nameref{sec:unit_V_population_genetics} |
| **\nameref{sec:unit_VI_unit_intro}** | \nameref{sec:unit_VI_evolution_and_selection}; \nameref{sec:unit_VI_genetic_drift_and_speciation}; \nameref{sec:unit_VI_phylogenetics} |
| **\nameref{sec:unit_VII_unit_intro}** | \nameref{sec:unit_VII_bacteria_archaea_viruses}; \nameref{sec:unit_VII_microbial_ecology}; \nameref{sec:unit_VII_host_immunity_and_vaccines}; \nameref{sec:unit_VII_antimicrobial_resistance_and_epidemiology} |
| **\nameref{sec:unit_VIII_unit_intro}** | \nameref{sec:unit_VIII_plant_structure_and_water}; \nameref{sec:unit_VIII_plant_reproduction}; \nameref{sec:unit_VIII_plant_responses} |
| **\nameref{sec:unit_IX_unit_intro}** | \nameref{sec:unit_IX_circulation_respiration_homeostasis}; \nameref{sec:unit_IX_nervous_system}; \nameref{sec:unit_IX_action_potential_synapses}; \nameref{sec:unit_IX_endocrine_signaling}; \nameref{sec:unit_IX_immune_system_defense} |
| **\nameref{sec:unit_X_unit_intro}** | \nameref{sec:unit_X_population_ecology}; \nameref{sec:unit_X_community_interactions}; \nameref{sec:unit_X_biodiversity_and_food_webs}; \nameref{sec:unit_X_ecosystem_ecology}; \nameref{sec:unit_X_biomes_and_conservation} |
<!-- preface-scope-end -->

---

## Reading paths by goal {.unnumbered}

| Goal | Where to start | How to use the code |
| ---- | -------------- | ------------------- |
| **Exam / course survey** | Unit intros + chapter summaries + the companion question bank that follows each chapter | Answer odd-numbered questions first; check module footers for `biology.*` imports. |
| **Wet-lab or clinical bridge** | \nameref{sec:unit_II_unit_intro}, \nameref{sec:unit_IV_unit_intro}, \nameref{sec:unit_VII_unit_intro}, and \nameref{sec:unit_IX_unit_intro} | Read boxed clinical / systems notes; pair with labs in the same unit. |
| **Modeling / CS** | \nameref{sec:unit_0_unit_intro}, then any unit’s “Bridge to computation” | Run examples with `uv run python` from the project root; regenerate figures with `scripts/generate_figures.py`. |
| **Ecology / field biology** | \nameref{sec:unit_VI_unit_intro} and \nameref{sec:unit_X_unit_intro}, plus \cref{sec:unit_III_photosynthesis} | Focus on `ecology.py` functions cited in chapter footers; work Lotka–Volterra and logistic examples by hand then in Python. |

---

## How to Use This Book {.unnumbered}

Each chapter is designed for introductory biology learners and can be read in two modes:

1. **Concept-first**: Read the narrative, work the examples, and do the questions.
2. **Model-first**: Run the companion modules and treat the text as interpretation of model behavior.

**For each concept, the integrated approach is:**

1. **Conceptual narrative** — the biological story and mechanism in plain language with precise vocabulary.
2. **Quantitative framework** — equations, derivations, and worked numerical examples.
3. **Primary citations** — key papers (author, year, journal) supporting mechanisms; citations are included where used.
4. **Python source** — model code in the project’s biology modules (importable and runnable).
5. **Figures** — generated by `src/visualization/plots.py` (`ALL_FIGURE_GENERATORS`) and `src/mermaid/biology_diagrams.py`.
6. **Clinical connections** — boxed examples connecting molecular mechanisms to human disease, therapy, and public health.
7. **Review and discussion questions** — a 30-item companion question bank per chapter, plus end-of-chapter review questions, from calculation to synthesis (\nameref{sec:unit_0_unit_intro} uses discussion prompts; other units mix numeric and conceptual items).

---

## Computational Infrastructure {.unnumbered}

The project’s biology code is organized by domain:

```text
src/biology/
├── biochemistry/    — Enzyme kinetics, macromolecule analysis
├── cell/            — Membrane biophysics, signaling, organelles
├── genetics/        — Mendelian ratios, Hardy-Weinberg, linkage mapping
├── physiology/      — Homeostasis, hemoglobin, cardiac models
├── ecology/         — Population dynamics, community models
├── evolution/       — Drift simulation, fitness landscapes
├── microbiology/    — Growth curves, MIC, viral cycles
├── botany/          — Water potential, transpiration, photosynthesis pathways
└── neuroscience/    — Action potentials, synapse models
```

**Diagram generation:**

```text
src/mermaid/biology_diagrams.py  — diagram factories registered in ALL_BIOLOGY_DIAGRAMS
src/visualization/plots.py    — matplotlib figure generators (ALL_FIGURE_GENERATORS)
```

Most code conforms to the project’s **no-mocks policy**: tests use real computations.

---

## Pedagogical Standards {.unnumbered}

**What this book assumes:** basic chemistry (atomic structure, covalent bonds, pH), basic algebra, and optional access to Python. No prior biology is required.

**Mathematical notation** is standard across most chapters:

- Concentrations in mol/L (M) or mmol/L (mM) as context requires
- Reaction rates in M·s⁻¹ or μmol·min⁻¹·mg protein⁻¹
- Genetic distances in centimorgans (cM)
- Most physiological parameters indexed to standard conditions (37 °C, pH 7.4, sea level) unless stated

**Primary citations** follow the format Author (year), *Journal*, and are embedded inline. They are selective: landmark results and a small number of current references where they materially clarify the consensus.

---

## Open Science Commitment {.unnumbered}

This book is released under the Creative Commons Attribution 4.0 International Licence (CC BY 4.0): you may freely use, adapt, and redistribute it with attribution. Most accompanying source code is released under the Apache-2.0 Licence.

The entire textbook — source markdown files, Python modules, figure scripts, and the build pipeline — is publicly available. The intent is for this resource to be a living, improvable document rather than a static product. Pull requests are welcome.

---

## Acknowledgements {.unnumbered}

This textbook was developed as part of the Research Project Template infrastructure for open, reproducible science education. Gratitude to the open-source communities behind [Pandoc](https://pandoc.org/), [LaTeX](https://www.latex-project.org/), [Mermaid](https://mermaid.js.org/), and [matplotlib](https://matplotlib.org/).

---

*Author:* **Daniel Ari Friedman**, Active Inference Institute
*ORCID:* [0000-0001-6232-9096](https://orcid.org/0000-0001-6232-9096)
*Edition 1.0, 2026*
*Licence: CC BY 4.0 (content) · Apache-2.0 (code)*
