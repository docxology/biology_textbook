# Unit IV — Molecular Genetics: AGENTS.md

## Source Module

`src/biology/genetics/genetics.py`:
- `dna_complement()` — DNA strand complement
- `transcribe_dna_to_mrna()` — template strand → mRNA
- `translate_mrna()` — mRNA → amino acid sequence
- `GENETIC_CODE` — 64-codon lookup table
- `gc_content()` — sequence analysis

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Semiconservative replication: Meselson-Stahl protocol (¹⁵N/¹⁴N density centrifugation)
- One-dimensional root-mean-square displacement: √(2Dt), not the mean signed displacement; assumptions and application belong in the chapter.
- Genetic code: 64 codons → 20 amino acids + 3 stop codons

## Diagrams

- `src/mermaid/biology_diagrams.py` — `transcription_translation_diagram()` (the common gene-expression pathway, not Crick's complete sequence-transfer restriction), `cell_cycle_diagram()`, `dna_replication_diagram()`, `mirna_biogenesis_diagram()`, `x_inactivation_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
