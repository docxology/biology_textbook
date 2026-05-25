# Figure Expansion Research Memo (2026-05-23)

Prioritization input for the biology textbook matplotlib expansion pass. Perplexity
(`llm -m sonar`) queries on pedagogical ROI, WCAG/CVD norms, and dual-pipeline
(static matplotlib + inline Mermaid) practice were cross-checked against the
chapter gap matrix and existing `src/biology/*` APIs.

## Ranked figure types (pedagogical ROI)

| Rank | Plot type | Rationale |
| --- | --- | --- |
| 1 | Hardy–Weinberg genotype/allele curves | Foundational null model; bridges Mendelian counts to population genetics |
| 2 | Hill / receptor-occupancy curves | Quantitative signaling; cooperativity is invisible in prose alone |
| 3 | SIR epidemic trajectories | Connects microbiology to public-health reasoning; R₀ intuition |
| 4 | Glycolysis ATP/NADH yield summary | Energy accounting anchor for respiration chapters |
| 5 | Poiseuille r⁴ flow sensitivity | Cardiovascular physiology; explains radius as dominant lever |
| 6 | Wright–Fisher drift / fitness landscape | Evolutionary stochasticity and selection on mean fitness |
| 7 | Molecular-clock divergence | Phylogenetics time estimation; pairs with neutral theory |
| 8 | Shannon/Simpson diversity bars | Community ecology; compares assemblages directly |
| 9 | Photosynthesis light-response (net rate) | Plant physiology; complements existing C3/C4/CAM figure |
| 10 | Osmotic pressure (van 't Hoff) | Water relations; pairs with Goldman/Nernst membrane thread |

## Accessibility (WCAG / CVD)

- Use the project `visualization.cvd` palette (Okabe–Ito–inspired hues; no red/green-only pairs).
- Pair color with line style or hatching for multi-series curves.
- Every `\includegraphics` block carries a substantive `<!-- alt: … -->` comment (not filename echo).
- Target ≥4.5:1 contrast for text on figure backgrounds where labels are rendered.

## When to add matplotlib vs keep inline Mermaid

| Add matplotlib | Keep inline Mermaid |
| --- | --- |
| Quantitative API exists in `src/biology/` | Pathway topology with named steps (glycolysis map, Krebs cycle) |
| Parameter sweep or time series | One-off conceptual schematics |
| Chapter has ≥2 worked examples with numbers | Unit 0 philosophy / history chapters |
| Duplicate would restate an existing registered diagram | Dense inline fence already covers the concept |

## Skip / defer rules

- **Unit 0** (`history_of_biology`, `active_inference`, `systems_science`, `complex_adaptive_systems`): prose-first; no APIs — defer unless a single systems diagram is added later.
- **Chapters with registered matplotlib already**: do not duplicate (e.g. second Michaelis plot).
- **Chapters with ≥3 inline Mermaid pathway diagrams**: prefer one quantitative companion plot, not another topology diagram.
- **API absent**: document deferral in gap matrix rather than inventing ad hoc math.

## Gap matrix summary

See `docs/figure_gap_matrix.md` for the full scored table. Tier 1 implements
existing APIs with clear chapter homes; Tier 2 covers remaining quantitative
chapters until the matrix is exhausted or publication gates block further PNGs.
