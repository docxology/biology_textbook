# Appendix D — Units, Physical Constants, and Biological Ranges {.unnumbered}

\label{sec:appendix_units_and_constants}


<!-- chapter-metadata-badge -->
> **\cref{sec:appendix_units_and_constants}** · Level 1/3 · 20 min read · Prerequisites: none · Use as reference

A compact reference for units, constants, and characteristic magnitudes encountered throughout the textbook. Use it during worked problems to sanity-check dimensional analysis, convert between unit systems, and verify that numerical answers fall in biologically plausible ranges.

---

## D.1 SI Base and Derived Units {.unnumbered}

| Quantity | SI unit | Symbol | In base units |
| -------- | ------- | ------ | ------------- |
| Length | metre | m | — |
| Mass | kilogram | kg | — |
| Time | second | s | — |
| Amount of substance | mole | mol | — |
| Temperature | kelvin | K | — |
| Electric current | ampere | A | — |
| Force | newton | N | kg · m · s⁻² |
| Energy | joule | J | kg · m² · s⁻² |
| Power | watt | W | J · s⁻¹ |
| Pressure | pascal | Pa | N · m⁻² |
| Electric charge | coulomb | C | A · s |
| Electric potential | volt | V | J · C⁻¹ |
| Electric conductance | siemens | S | Ω⁻¹ |
| Frequency | hertz | Hz | s⁻¹ |

### Metric prefixes {.unnumbered}

| Prefix | Symbol | Factor | Biological use |
| ------ | ------ | ------ | -------------- |
| giga- | G | 10⁹ | Gb base pairs in a genome |
| mega- | M | 10⁶ | MDa protein complex; Mb DNA fragment |
| kilo- | k | 10³ | kJ mol⁻¹ (ΔG); kDa protein mass |
| centi- | c | 10⁻² | cM genetic map distance |
| milli- | m | 10⁻³ | mM intracellular metabolites; ms AP duration |
| micro- | μ | 10⁻⁶ | μm cell size; μM low-abundance metabolite |
| nano- | n | 10⁻⁹ | nm bond length; nM receptor ligand |
| pico- | p | 10⁻¹² | pN molecular motor force; pM low-abundance hormone |
| femto- | f | 10⁻¹⁵ | fmol amount in a single cell |
| atto- | a | 10⁻¹⁸ | amol; approaches single-molecule detection |

---

## D.2 Universal Physical Constants {.unnumbered}

| Constant | Symbol | Value |
| -------- | ------ | ----- |
| Avogadro's number | $N_A$ | $6.022 \times 10^{23}$ mol⁻¹ |
| Boltzmann constant | $k_B$ | $1.381 \times 10^{-23}$ J K⁻¹ = $8.617 \times 10^{-5}$ eV K⁻¹ |
| Gas constant | $R = N_A k_B$ | 8.314 J K⁻¹ mol⁻¹ = 1.987 cal K⁻¹ mol⁻¹ |
| Faraday constant | $F$ | $9.649 \times 10^{4}$ C mol⁻¹ |
| Elementary charge | $e$ | $1.602 \times 10^{-19}$ C |
| Speed of light in vacuum | $c$ | $2.998 \times 10^{8}$ m s⁻¹ |
| Planck constant | $h$ | $6.626 \times 10^{-34}$ J s |
| Permittivity of free space | $\varepsilon_0$ | $8.854 \times 10^{-12}$ F m⁻¹ |
| Standard atmospheric pressure | $P_{\text{atm}}$ | 101,325 Pa = 760 Torr |
| Body temperature | $T_{\text{body}}$ | 310.15 K = 37.00 °C |
| Thermal energy at body T | $k_B T$ | $4.28 \times 10^{-21}$ J ≈ 0.027 eV = 2.57 kJ mol⁻¹ |

The rule "$k_B T \approx \tfrac{1}{40}$ eV $\approx \tfrac{2.5}{1000}$ kJ mol⁻¹ at room temperature" is useful: hydrogen bonds (~20 kJ mol⁻¹) are ~8 $k_B T$, so they survive thermal fluctuations; van der Waals contacts (~1 kJ mol⁻¹) are ~0.4 $k_B T$, so each one is barely stable but collectively numerous contacts summate.

---

## D.3 Energy Conversions {.unnumbered}

| From | To | Factor |
| ---- | -- | ------ |
| 1 J | cal | 0.239 |
| 1 cal | J | 4.184 |
| 1 kcal | kJ | 4.184 |
| 1 eV | J | $1.602 \times 10^{-19}$ |
| 1 eV | kJ mol⁻¹ | 96.485 |
| 1 kJ mol⁻¹ | eV | 0.01036 |
| 1 J | kg⋅m² s⁻² | 1 (definition) |
| 1 $k_B T$ at 37 °C | kJ mol⁻¹ | 2.577 |

### ATP hydrolysis benchmarks {.unnumbered}

- Standard ΔG°′ for ATP → ADP + P$_i$: **−30.5 kJ mol⁻¹**.
- Cellular ΔG (physiological [ATP]/[ADP]): **−57 kJ mol⁻¹**, roughly 22 $k_B T$.
- Number of ATP hydrolyses required to lift a 1 kg mass 1 m: ~300,000 — illustrating why muscle needs 10⁸ ATP molecules consumed per second.

---

## D.4 Pressure Conversions {.unnumbered}

| From | To | Factor |
| ---- | -- | ------ |
| 1 atm | Pa | 101,325 |
| 1 atm | mmHg (Torr) | 760 |
| 1 atm | bar | 1.01325 |
| 1 mmHg | kPa | 0.1333 |
| 1 mmHg | Pa | 133.322 |

**Blood pressure**: systolic 120 mmHg ≈ 16 kPa. **Arterial O₂**: $P_{\text{a}}O_2 \approx 100$ mmHg ≈ 13.3 kPa. **Venous O₂**: $P_{\text{v}}O_2 \approx 40$ mmHg ≈ 5.3 kPa.

---

## D.5 Concentration Conversions {.unnumbered}

1 molar (M) = 1 mol L⁻¹ = 10³ mmol L⁻¹ = 10⁶ μmol L⁻¹ = 10⁹ nmol L⁻¹ = 10¹² pmol L⁻¹.

| Concentration | Example |
| ------------- | ------- |
| pM ($10^{-12}$ M) | Circulating hormones (insulin, oxytocin) |
| nM ($10^{-9}$ M) | Vitamin B₁₂, transcription factor at a target site |
| μM ($10^{-6}$ M) | Glucose in blood (5 × 10⁻³ M = 5 mM, upper end) |
| mM ($10^{-3}$ M) | Major intracellular ions (Na⁺, K⁺), ATP (~5 mM) |
| M | Cytoplasm water (55 M); seawater NaCl (0.5 M) |

Molarity of water: $M_{H_2O} = 1000 \text{ g L}^{-1} / 18 \text{ g mol}^{-1} = 55.5$ M. This is why [H₂O] is treated as constant in biological equilibrium expressions.

---

## D.6 Biological Magnitudes — Quick Reference {.unnumbered}

### Time scales {.unnumbered}

| Event | Time |
| ----- | ---- |
| Bond vibration | 10⁻¹⁴ s |
| Enzyme turnover ($k_{cat}$) | 10⁻³ – 10⁻⁶ s |
| Action potential | 10⁻³ s |
| Synaptic transmission | 10⁻³ s |
| Ribosome peptide-bond formation | 0.1 s (5 aa s⁻¹ per ribosome) |
| Protein folding | 10⁻³ – 1 s |
| Mitosis | 1 h |
| Cell cycle (dividing human cell) | 1 d |
| Hair growth | 1 cm month⁻¹ |
| Human generation time | ~25 yr |
| Mammalian species lifespan | 10⁶ – 10⁷ yr |

### Length scales {.unnumbered}

| Feature | Size |
| ------- | ---- |
| C–C bond | 0.15 nm |
| Protein (average globular) | 3 nm |
| Ribosome | 25 nm |
| Virus (small RNA) | 30 nm |
| Nuclear pore | 100 nm |
| Bacterium (*E. coli*) | 1 μm |
| Mitochondrion | 2 μm |
| Eukaryotic cell (average) | 10–20 μm |
| Neuron axon (giraffe recurrent laryngeal) | 2 m |
| Animal (blue whale) | 30 m |
| Redwood tree | 100 m |

### Energy scales {.unnumbered}

| Interaction / event | Energy |
| ------------------- | ------ |
| Van der Waals contact | ~1 kJ mol⁻¹ |
| Hydrogen bond | ~20 kJ mol⁻¹ |
| C–C covalent bond | ~350 kJ mol⁻¹ |
| ATP hydrolysis (standard) | −30.5 kJ mol⁻¹ |
| ATP hydrolysis (cellular) | −57 kJ mol⁻¹ |
| Glucose complete oxidation | −2870 kJ mol⁻¹ |
| Photosynthesis per photon (680 nm) | 176 kJ mol⁻¹ |
| Daily human basal energy | 7000 kJ d⁻¹ (≈1700 kcal d⁻¹) |

### Organismal physiology reference scales {.unnumbered}

| System | Useful scale | Source-backed context |
| ------ | ------------ | --------------------- |
| Digestive absorption | Small-intestinal villi and microvilli expand absorptive surface | Nutrient uptake depends on epithelial surface area, enzymes, bile, transporters, and gut motility \citep{niddk2024digestivesystem}. |
| Renal excretion | Adult kidneys filter plasma continuously and adjust urine concentration | Filtration, tubular reabsorption, secretion, and collecting-duct water handling set volume, electrolyte, pH, and nitrogen-waste balance \citep{niddk2024kidneys}. |
| Skeletal muscle | Sarcomere force depends on actin-myosin overlap and cross-bridge cycling | Sliding-filament physiology links molecular geometry to organismal movement \citep{huxley1954sliding}. |
| Somatosensation | Receptor density sets spatial resolution | Mechanoreceptor subtype, receptive-field size, and cortical magnification jointly shape touch discrimination \citep{abraira2013somatosensory}. |
| Behaviour | Four explanatory levels | Mechanism, development, function, and phylogeny answer different questions about the same behaviour \citep{tinbergen1963aims}. |
| Reproduction | Infertility triage starts after 12 months, or 6 months at age 35+ | Evaluation separates ovulation, sperm production, anatomy, implantation, endocrine timing, and age-dependent gamete quality \citep{cdc2024reproductivehealth}. |

---

## D.7 Fundamental Biological Constants {.unnumbered}

| Parameter | Value | Source / context |
| --------- | ----- | ---------------- |
| Resting cell membrane potential | ≈ −70 mV | Neurons, muscle cells |
| Intracellular [Na⁺] / [K⁺] | ~10 / 140 mM | Maintained by Na⁺/K⁺-ATPase |
| Extracellular [Na⁺] / [K⁺] | ~145 / 5 mM | Plasma |
| Blood pH | 7.35–7.45 | Tightly regulated |
| Arterial pCO₂ | ~40 mmHg | Regulated by respiration |
| Body-water content | 60 % of body mass | Total body water |
| Haemoglobin O₂ capacity | 1.34 mL O₂ / g Hb | Full saturation |
| Blood volume | ~5 L in adult | 7 % of body mass |
| Body surface area (adult) | ~1.8 m² | DuBois formula |
| Mitochondrial membrane potential | ≈ −180 mV | Drives ATP synthesis |
| Proton gradient ΔpH across inner mito membrane | ~1 unit | Chemiosmosis |
| Genome size (human) | 3 × 10⁹ bp | Haploid |
| Protein-coding genes (human) | ~20,000 | ENCODE estimate |
| Cells in the adult human body | ~3.7 × 10¹³ | Bianconi et al. 2013 |
| Bacteria in human gut | ~10¹⁴ | ~equal to human cell count |
| Species described on Earth | ~2 × 10⁶ | Estimated 10–30× more undescribed |

---

*Module: reference only (no code)*
