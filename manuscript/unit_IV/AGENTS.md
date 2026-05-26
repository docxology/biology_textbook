# Unit IV — Molecular Genetics: AGENTS.md

## Source Module

`src/biology/genetics/genetics.py`:
- `dna_complement()` — DNA strand complement
- `transcribe_dna_to_mrna()` — template strand → mRNA
- `translate_mrna()` — mRNA → amino acid sequence
- `GENETIC_CODE` — 64-codon lookup table
- `gc_content()` — sequence analysis

## Chapters

1. `dna_replication_and_cell_cycle.md` — DNA Replication and the Cell Cycle
2. `gene_expression.md` — Gene Expression
3. `mutations_and_genomics.md` — Mutations, CRISPR, and Genomics
4. `chromatin_and_epigenetic_mechanisms.md` — Chromatin and Epigenetic Mechanisms
5. `epigenetic_inheritance_and_disease.md` — Epigenetic Inheritance and Disease

## Key Equations

- Semiconservative replication: Meselson-Stahl protocol (¹⁵N/¹⁴N density centrifugation)
- Mean diffusion distance: x̄ = √(2Dt) — limits cell/nucleus size
- Genetic code: 64 codons → 20 amino acids + 3 stop codons

## Diagrams

- `src/mermaid/biology_diagrams.py` — `transcription_translation_diagram()` (central dogma), `cell_cycle_diagram()`, `dna_replication_diagram()`, `mirna_biogenesis_diagram()`, `x_inactivation_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_IV_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_IV_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
