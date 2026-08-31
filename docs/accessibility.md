# Biology Textbook — Accessibility and Configuration

> [!NOTE]
> **See also:** [manuscript_guide.md](manuscript_guide.md#figures) for alt-text placement; [visualization_guide.md](visualization_guide.md#cvd-friendly-palette-exact-hex) for the CVD palette; [testing_guide.md](testing_guide.md) for the tests that enforce these policies.

---

## Table of contents

- [Enforcement surface (what is actually checked)](#enforcement-surface-what-is-actually-checked)
- [`config.yaml` keys — status](#configyaml-keys--status)
- [Alt text writing guide](#alt-text-writing-guide)
- [Bad → good alt-text rewrites](#bad--good-alt-text-rewrites)
- [Type-specific alt-text playbook](#type-specific-alt-text-playbook)
- [Colorvision-deficiency (CVD) checklist](#colorvision-deficiency-cvd-checklist)
- [HTML and PDF limitations](#html-and-pdf-limitations)
- [Reader / large-type profile (optional)](#reader--large-type-profile-optional)
- [Related](#related)

---

## Enforcement surface (what is actually checked)

| Mechanism | Role |
| --------- | ---- |
| **Pytest invariants** (`tests/test_*.py`) | **Authoritative**: alt text proximity and quality heuristics, build invariants, bibliography, cross-refs, chapter metadata. |
| **`docs/manuscript/config.yaml` — most keys** | Authoring contract and rendering inputs (layout, typography, units, `front_matter`, `appendices`, `rendering`, `llm`). Values must stay aligned with `preamble.md` where the AGENTS table says so. |
| **`config.yaml` — `accessibility`, `content_notes`, `export`, parts of `chapter_metadata`** | See [Status](#configyaml-keys--status) below. Some are **advisory** (documentation intent); figure generation follows **`src/visualization/cvd.py`** (CVD-friendly palette), which **implements** the intent of `accessibility.color_blindness_safe: true` for matplotlib outputs. |

> [!IMPORTANT]
> `accessibility.alt_text_required` is **not** read at PDF build time to fail the build. Alt text is **enforced by tests** (`test_accessibility.py`) and by editorial convention. The YAML flag records the same policy for humans and tools.

---

## `config.yaml` keys — status

### `accessibility`

| Key | Status | Notes |
| --- | ------ | ----- |
| `alt_text_required` | **Advisory (policy)** | **Tests** (`test_accessibility.py`) are the enforcer, not a YAML consumer in the template renderer. |
| `color_blindness_safe` | **Partially implemented** | Matplotlib figures use **`src/visualization/cvd.py`** (distinct hues + line styles / edges / hatch where needed). Mermaid theming in PNG export is not centrally styled here. |
| `dyslexia_friendly_font` | **Not wired** | If set to `true`, authors must also change **`typography.body_font`** in `config.yaml` and the matching `\setmainfont` / `\newfontfamily` in **`docs/manuscript/preamble.md`** to an installed OpenDyslexic (or other) family — same "dual edit" rule as other typography changes. No automated swap yet. |

### `content_notes`

| Key | Status | Notes |
| --- | ------ | ----- |
| `clinical_content` | **Advisory** | Editorial: whether clinical boxes are desired; not read by `biology_analysis.py`. |
| `animal_experiments` | **Advisory** | Editorial disclaimer / scope. |
| `quantitative_depth` | **Advisory** | Tuning guide for author depth (`full` \| `conceptual` \| `advanced`); not read by build scripts. |

### `export`

| Key | Status | Notes |
| --- | ------ | ----- |
| `include_solutions` | **Implemented in `biology_analysis`** | When `true`, `<!-- SOLUTION ... SOLUTION -->` blocks in question banks are revealed as blockquoted instructor answers; the same behavior can be forced with `BIOLOGY_INCLUDE_SOLUTIONS=1`. |
| `include_worked_problems` | **Advisory** | Not read by `biology_analysis.py`; keep `false` until a build hook is implemented. |
| `watermark_instructor` | **Implemented in `biology_analysis`** | Optional diagonal overlay when both `export.watermark_instructor` and `export.include_solutions` are true (`instructor_preamble_text` in `biology.pipeline.injection`). Default publication build keeps instructor answers with `watermark_instructor: false`. |

### `chapter_metadata` (`config.yaml` section)

| Key | Status | Notes |
| --- | ------ | ----- |
| `show_difficulty` | **Advisory** | Badges are produced from `ChapterMeta` in `insert_chapter_metadata.py` / metadata blocks; the flag is not parsed to toggle output in current scripts. |
| `show_prerequisites` | **Advisory** | Same: content comes from `chapter_metadata.py` data, not a YAML boolean reader. |

---

## Alt text writing guide

Alt text serves screen-reader users, low-bandwidth fallback, and search/indexing. **It is not a caption replacement** — captions are also read; alt text is for those who cannot see the image at all.

### Rules

| Rule | Detail |
| ---- | ------ |
| **Placement** | `<!-- alt: ... -->` immediately after `\end{figure}` for LaTeX figures; exactly one `<!-- alt: ... -->` comment plus one *italic* caption immediately after every inline `mermaid` fence. |
| **Length** | One sentence, ~15–35 words. Longer than 50 words is too verbose; shorter than 10 is usually too generic. |
| **Voice** | Describe what is **visually shown**, not the conclusion. The conclusion belongs in the caption and prose. |
| **No redundancy** | Do not repeat the figure number, "shown above", or the caption verbatim. |
| **Mathematical content** | Spell out symbols a screen reader will mispronounce: "K subscript m" instead of "Km"; "V max" instead of `V_{\max}`. |
| **Spatial words** | "Top-left", "diagonal", "vertical bar at x = 5" help readers reconstruct layout. |
| **Cite the units** | "millivolts", "kilopascals", "moles per liter" — write them out, not "mV", "kPa", "mol/L". |

### The three-question test before writing

> [!TIP]
> Before writing an alt-text comment, ask yourself:
>
> 1. **What kind of figure is it?** (line plot, bar chart, schematic, equation image, photograph)
> 2. **What is the salient visual feature?** (a peak, a plateau, a crossover, a labeled cluster)
> 3. **What numbers anchor the reader?** (axis range, threshold value, parameter setting)
>
> The answers, in one sentence, are your alt text.

---

## Bad → good alt-text rewrites

A short rule: **bad** alt text names the figure; **good** alt text describes what's drawn.

| Bad | Good |
| --- | ---- |
| `<!-- alt: A figure -->` | `<!-- alt: Bar chart comparing reaction rates of five enzymes at pH 7.0, with catalase and carbonic anhydrase showing the two highest rates near 10^7 per second. -->` |
| `<!-- alt: Graph -->` | `<!-- alt: Sigmoidal curve showing fractional saturation versus oxygen partial pressure, with Hill coefficient n equals 2.8 labeled near the inflection point at 26 millimetres of mercury. -->` |
| `<!-- alt: Equation 4.7 -->` | `<!-- alt: Michaelis-Menten rate equation: reaction velocity v equals V max times substrate concentration, divided by the sum of K subscript m and substrate concentration. -->` |
| `<!-- alt: Diagram -->` | `<!-- alt: Linear pathway diagram with ten enzymatic steps from glucose at the top-left to pyruvate at the bottom-right, with two ATP-consuming steps in the upper half and two ATP-producing steps in the lower half. -->` |

---

## Type-specific alt-text playbook

### Equations (when the equation is rendered as an image)

> [!TIP]
> Most equations are read aloud by the screen reader directly from the rendered MathJax/LaTeX (where supported). Alt text becomes critical when an equation appears as an **image** (e.g. a screenshot, or PDF without accessible math).

When you must spell out an equation:

| LaTeX | Alt text |
| ----- | -------- |
| `v = V_{\max}[S] / (K_m + [S])` | "The Michaelis–Menten rate equation: reaction velocity equals V max times substrate concentration, divided by the sum of K subscript m and substrate concentration." |
| `\Delta G = \Delta H - T\Delta S` | "The Gibbs free-energy equation: change in G equals change in H minus temperature times change in S." |
| `p^2 + 2pq + q^2 = 1` | "The Hardy–Weinberg equilibrium: p squared plus two p q plus q squared equals one, where p and q are dominant and recessive allele frequencies." |
| `C_m \frac{dV}{dt} = -I_{Na} - I_K + I_{stim}` | "The Hodgkin–Huxley membrane current balance: membrane capacitance times the rate of change of voltage equals minus the sodium current minus the potassium current plus the stimulus current." |

**Rule:** spell out the **structure** ("equals", "divided by", "minus"), name the **symbols** ("K subscript m"), and finish with the **physical meaning** ("…where p is the dominant allele frequency"). Do not just transliterate LaTeX.

### Diagrams (mermaid, schematic)

Describe the **flow** and **relationships** — not just a list of nodes.

| Bad | Good |
| --- | ---- |
| `<!-- alt: Glycolysis diagram -->` | `<!-- alt: Linear pathway diagram showing glucose entering at the top and pyruvate exiting at the bottom, with ATP and NADH cofactor inputs and outputs at each of ten enzymatic steps. -->` |
| `<!-- alt: Cell cycle -->` | `<!-- alt: Circular state diagram of the eukaryotic cell cycle with four labelled phases — G1, S, G2, M — and arrows showing checkpoints between G1/S and G2/M. -->` |
| `<!-- alt: List of nodes: glucose, pyruvate, ATP, NADH -->` | (rewrite to describe **structure**: linear vs branched, top-to-bottom vs cyclic, where the inputs/outputs sit) |

> [!TIP]
> For mermaid diagrams in chapters, use both channels: the `<!-- alt: ... -->` comment gives the screen-reader/fallback description, and the *italic* line gives the visible caption. `scripts/add_mermaid_alt_text.py --check` and `tests/test_accessibility.py` reject missing, duplicated, or generic Mermaid metadata.

### Plots (line, scatter, bar)

Describe the **shape**, the **axes**, and the **salient features** (peaks, plateaus, crossovers).

| Bad | Good |
| --- | ---- |
| `<!-- alt: A graph -->` | `<!-- alt: Logarithmic-scale line plot of bacterial cell density versus time, showing four phases: a flat lag phase for two hours, exponential rise from hours 2 to 8, plateau at carrying capacity from hours 8 to 16, then decline. -->` |
| `<!-- alt: Histogram -->` | `<!-- alt: Right-skewed histogram of allele frequencies in 1000 simulated populations, with median at 0.18 and a long tail extending past 0.6. -->` |
| `<!-- alt: Scatter -->` | `<!-- alt: Scatter plot of body mass versus metabolic rate on log-log axes for 50 mammals, with a linear regression slope of 0.75 (Kleiber's law) drawn through the points. -->` |

### Punnett squares

| Bad | Good |
| --- | ---- |
| `<!-- alt: Punnett -->` | `<!-- alt: Two-by-two Punnett square for an Aa-by-Aa monohybrid cross: top-left AA, top-right Aa, bottom-left Aa, bottom-right aa. Three of the four cells contain the dominant phenotype. -->` |
| `<!-- alt: Genetic cross -->` | (same as above) |

### Action-potential traces

| Bad | Good |
| --- | ---- |
| `<!-- alt: Hodgkin-Huxley -->` | `<!-- alt: Voltage-versus-time line plot of a single action potential: resting at minus seventy millivolts for the first two milliseconds, sharp depolarisation to plus thirty-five millivolts at three milliseconds, repolarisation back to resting by six milliseconds, brief hyperpolarisation, then return to baseline. -->` |

### Phylogenetic trees

| Bad | Good |
| --- | ---- |
| `<!-- alt: Tree of life -->` | `<!-- alt: Three-domain phylogenetic tree with a single root branching into Bacteria on the left, Archaea in the center, and Eukarya on the right. Eukarya nests within an archaeal sister-group, reflecting the two-domain hypothesis. -->` |

### Heatmaps

| Bad | Good |
| --- | ---- |
| `<!-- alt: Heatmap of methylation -->` | `<!-- alt: Viridis-colored heatmap of CpG methylation levels (0 to 1) across one hundred genomic loci on the x-axis and twelve developmental stages on the y-axis, with high methylation (yellow) clustering in the bottom-right quadrant. -->` |

---

## Colorvision-deficiency (CVD) checklist

Use this every time you create or review a figure:

- [ ] Two-series plots use `cvd.SERIES2` (blue + orange) **and** different line styles (solid + dashed).
- [ ] Three-series plots use `cvd.SERIES3` **and** three line styles (`-`, `--`, `:`).
- [ ] Heatmaps use a perceptually uniform colormap (`viridis`, `plasma`, `cividis`); never `RdYlGn`, `jet`, or `rainbow` without a second channel.
- [ ] Categorical coding ≥ 4 categories uses `tab10` **plus direct labels** on the chart (no color-only legend).
- [ ] Punnett squares use `cvd.PUNNETT_DOMINANT` / `cvd.PUNNETT_RECESSIVE` **plus** hatch patterns (`//` and `xx`).
- [ ] Bar charts with positive/negative values use `cvd.BAR_POS` / `cvd.BAR_NEG` **plus** a zero-line and value labels.
- [ ] No red+green as the only two-way distinction.
- [ ] Mermaid `classDef` styling uses Wong/Okabe-Ito hex codes (`#0072B2` blue, `#E69F00` orange, `#009E73` teal, `#D55E00` vermillion). See [visualization_guide.md](visualization_guide.md#wongokabe-ito-reference-palette).

---

## HTML and PDF limitations

- **PDF + LaTeX math**: not fully accessible to all screen readers. Prefer HTML with MathJax for some audiences, or offer the [reader typography profile](#reader--large-type-profile-optional) for print legibility. The preface (*A Textbook Built With Code*) includes "How to read this book digitally".
- **HTML builds**: when generating web output, use a **single** `#` per document where the template allows; keep `##` / `###` in order; set document `lang` in the site template. Preserve image **alt** from `![alt](…)` and from `<!-- alt: ... -->` when the build maps comments into `alt` attributes (depends on the template). See [composable_authoring.md](composable_authoring.md).

---

## Reader / large-type profile (optional)

Default PDF uses compact settings (see [AGENTS.md](../AGENTS.md)). For a more legible print profile, **edit `docs/manuscript/config.yaml` and `docs/manuscript/preamble.md` together** (layout margins, `base_font_size_pt`, `line_height`, and the matching `\geometry`, `\normalsize`, `\setstretch`).

> [!TIP]
> Suggested starting point for a "reader" profile (adjust to taste):
>
> | Setting | Compact (default) | Reader profile |
> | ------- | ----------------- | -------------- |
> | Margins (all sides) | 2 mm | 10–12 mm |
> | Inner-bind extra | — | + 5 mm if printed bound (`margin_inner_extra_mm`) |
> | Body font size | 9 pt | 10.5–11 pt |
> | Line spacing | 1.28 | 1.35–1.4 |

Re-run from the repository root:

```bash
uv run python scripts/03_render_pdf.py --project biology_textbook
```

Document which profile a given PDF build used in release notes or the title page if you distribute multiple editions.

---

## Related

- [docs/manuscript/AGENTS.md](../docs/manuscript/AGENTS.md) — manuscript contract, figure allowlists, print density.
- [../tests/README.md](../tests/README.md) — which tests map to which policies.
- [testing_guide.md](testing_guide.md) — no-mock policy, failure triage, "what test catches what mistake".
- [visualization_guide.md](visualization_guide.md) — figures, CVD defaults for matplotlib, palette hex.
- [manuscript_guide.md](manuscript_guide.md#figures) — alt-text placement and formatting.
