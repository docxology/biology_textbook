# Unit VI — Evolution: AGENTS.md

## Source Module

`src/biology/evolution/evolution.py`:
- `simulate_selection()` — allele frequency change over generations
- `simulate_drift(p, N, generations, rng_seed=42)` — stochastic diploid Wright–Fisher drift trajectory
- `fitness_landscape_1d()` — mean genotype fitness versus allele frequency under supplied AA/Aa/aa fitnesses, not a two-locus epistatic surface
- `molecular_clock_divergence_time()` — t = d_JC / (2μ)
- `biology.genetics.jukes_cantor_distance(p_distance)` — corrected sequence divergence; exported by genetics, not evolution
- `isolation_index()` — unvalidated teaching ratio μ/(μ+m), not reproductive isolation, F_ST or a speciation probability; both-zero rates are undefined

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Use the chapter's genotype-fitness recurrence for the stated selection model; Δq = −spq²/W̄ is a special-case expression, not a general selection law.
- Drift variance: σ²(Δp) = pq / (2N_e)
- Gene flow: p₁' = (1 − m)p₁ + mp₂
- Jukes-Cantor: d_JC = −(3/4) ln(1 − 4d/3)
- Molecular clock: t = d_JC / (2μ)

## Figures and Diagrams

- `plot_selection_simulation()` identifies supplied genotype fitnesses and initial p; heterozygote advantage/disadvantage panels are not phenotypic stabilizing/disruptive selection models. See [visual conventions](../../visualization_guide.md).
- `src/mermaid/biology_diagrams.py` — `natural_selection_diagram()`, `phylogenetic_tree_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
