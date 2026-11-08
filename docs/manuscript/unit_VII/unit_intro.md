# Unit VII — Microbiology: Introduction {#sec:unit_VII_unit_intro .unnumbered}


## Why This Unit Matters {.unnumbered}

Microorganisms are extraordinarily abundant as cells, metabolically diverse, and central to life's evolutionary history; numerical abundance is not carbon-mass dominance. Global prokaryotic abundance is of order $10^{30}$ cells. The 2018 biomass synthesis estimates plants at about 450 of 550 Gt C globally, compared with bacteria at 70 and archaea at 7 Gt C \citep{baron2018biomass}. These are extrapolated carbon-stock estimates, not cell counts: microbial uncertainty is large, especially in the deep subsurface (reported multiplicative uncertainty factors about 10 for bacteria and 13 for archaea). Bacteria and archaea occupy deep branches of the tree of life. Oxygenic photosynthesis — the ultimate energy source for most ecosystems — arose in cyanobacterial ancestry.
Nitrogen fixation, without which terrestrial
agriculture would collapse, is performed exclusively by bacteria and archaea. The atmosphere itself
was transformed by microbial metabolism long before any animal breathed it.

Medical microbiology became possible primarily after Robert Koch's postulates (1877–1884) established the
germ theory of disease — the revolutionary idea that specific microorganisms cause specific infections.
Alexander Fleming's observation in 1928 that *Penicillium* mould killed staphylococcal colonies
initiated the antibiotic era, saving an estimated 200 million lives over the following century. But
pathogens evolve. The emergence of multidrug-resistant organisms (MRSA, XDR-TB, carbapenem-resistant
*Enterobacteriaceae*) represents one of the most urgent public health crises of the 21st century:
an estimated 1.27 million deaths were attributable to antimicrobial resistance in 2019 (Murray et al.,
2022, *The Lancet*).

This unit combines cell biology (structure of bacteria, archaea, and viruses), quantitative
microbiology (growth curves, MIC calculations, viral replication kinetics), and ecology (the microbiome,
biogeochemical cycles, infectious disease dynamics). You will apply the S-I-R epidemiological model
and calculate R₀; model bacterial growth and antibiotic kill curves; and examine the microbiome as a
complex ecological community whose disruption underlies diseases from *C. difficile* colitis to
metabolic syndrome.

---

## Landmark Discoveries {.unnumbered}

| Discoverer(s) | Year | Journal / Source | Discovery | Significance |
| ------------- | ---- | ---------------- | --------- | ------------ |
| Antoni van Leeuwenhoek | 1676 | \citep{leeuwenhoek1676} | First observation of bacteria (\"animalcules\") | Founded microbiology; showed microorganisms are everywhere |
| Louis Pasteur | 1859–1861 | \citep{pasteur1861} | Disproof of spontaneous generation | Established germ theory; revolutionised medicine and food safety |
| Robert Koch | 1876–1884 | \citep{koch1884} | Koch's postulates; anthrax, TB, cholera | Rigorous criteria for linking pathogen to disease |
| Alexander Fleming | 1928 | \citep{fleming1929} | Penicillin discovery | Launched the antibiotic era; Nobel Prize 1945 |
| Carl Woese & George Fox | 1977 | \citep{woese1977} | Archaea as third domain (16S rRNA) | Restructured the comprehensive tree of life; archaea are closer to eukaryotes than to bacteria |
| Eckburg, Lepp & Relman; Human Microbiome Project Consortium | 2003 review; 2012 consortium studies | \citep{relman1999,hmp2012structure} | Archaeal colonization questions and sequence-based human-community characterization | Presence is not proof of pathogenicity; community surveys are not a census establishing one universal microbial cell count |
| Murray et al. | 2022 | \citep{murray2022amr} | Global mortality from antimicrobial resistance (1.27 million deaths, 2019) | Quantified the scale of the AMR crisis as a call to action |

---

## Key Concepts and Connections {.unnumbered}

```mermaid
graph TD
    BACT["🦠 Bacteria<br/>(prokaryote; peptidoglycan;<br/>Gram+/Gram−; flagella)"] --> GROW["📈 Growth Kinetics<br/>(lag, log, stationary, death;<br/>N(t) = N₀ × 2^(t/t_d))"]
    BACT --> ABRES["💊 Antibiotic Resistance<br/>(β-lactamase, efflux,<br/>target modification)"]
    BACT --> BIOFILM["🏗️ Biofilms<br/>(quorum sensing;<br/>matrix formation)"]

    ARCH["🌋 Archaea<br/>(ether lipids; extremophiles;<br/>kin to eukaryotes)"] --> EXTR["❄️🔥 Extremophiles<br/>(thermophiles, halophiles,<br/>acidophiles)"]

    VIR["🔴 Viruses<br/>(acellular; DNA/RNA;<br/>obligate intracellular)"] --> LYCY["⚡ Lytic/Lysogenic<br/>(lysis release vs.<br/>prophage integration)"]
    VIR --> REPRO["🔁 Viral Replication<br/>(attachment → synthesis<br/>→ assembly → release)"]

    MICRO["🌿 Microbiome<br/>(10¹³ cells; Firmicutes,<br/>Bacteroidetes; dysbiosis)"] --> HOST["🤝 Host-Microbe Interactions<br/>(mutualism, commensal,<br/>parasitism)"]

    INFECT["🏥 Infectious Disease<br/>(Koch's postulates;<br/>epidemiology; R₀)"] --> SIR["📊 SIR Model<br/>(dS/dt, dI/dt, dR/dt;<br/>R₀ = β/γ)"]
    INFECT --> IMMUN["🛡️ Host Immunity<br/>(later physiology)"]

    BACT --> INFECT
    VIR --> INFECT
    BACT --> MICRO

    style BACT fill:#e74c3c,color:#fff
    style VIR fill:#8e44ad,color:#fff
    style MICRO fill:#27ae60,color:#fff
    style SIR fill:#f39c12,color:#fff
```
<!-- alt: Graph showing microbiology concept map — red = bacteria; purple = viruses; green = microbiome; orange = epidemiological models. -->

*Microbiology concept map — red = bacteria; purple = viruses; green = microbiome; orange = epidemiological models.*

---

## Current Evidence Thread {.unnumbered}

In microbiology, a claim is primarily as strong as the way the organism was observed: read this unit as an evidence trail in which microbial life is established through culture, sequencing, and surveillance rather than as a list of named taxa and diseases. Microbiology and infectious disease now require One Health reasoning across people, animals, environments, genomics, and antimicrobial stewardship. As you
move through the chapters, keep a two-column note: **claim** on the left,
**evidence that would change my confidence** on the right. By the end of the
unit, each major idea should be tied to a measurement, model, citation, or
paper-based lab decision.

## Chapter Roadmap {.unnumbered}

| Chapter | Core question | Quantitative lens |
| --- | --- | --- |
| \cref{sec:unit_VII_bacteria_archaea_viruses} | How do cell architecture and viral life cycles constrain replication? | Growth, dilution and phage-threshold models |
| \cref{sec:unit_VII_microbial_ecology} | What does community evidence establish? | Diversity, compositional sampling and functional tests |
| \cref{sec:unit_VII_host_immunity_and_vaccines} | How does immune mechanism relate to measured protection? | Endpoint-specific vaccine comparisons |
| \cref{sec:unit_VII_antimicrobial_resistance_and_epidemiology} | How do resistance and transmission respond to interventions? | Organism–drug denominators, selection/HGT and conservative SIR |


---

## Connections Across the Textbook {.unnumbered}

- **Prokaryotic cell structure** in \cref{sec:unit_II_cell_theory} and \cref{sec:unit_II_cell_structure} provides the foundation for understanding antibiotic mechanisms (cell wall, ribosome 70S targets).
- **Viral replication** links to \nameref{sec:unit_IV_unit_intro} (CRISPR discovered as a bacterially-encoded anti-phage defense system; RNA viruses and reverse transcriptase).
- **Antibiotic resistance evolution** is a direct application of \nameref{sec:unit_VI_unit_intro} (natural selection, fitness, molecular clocks on resistance genes).
- **Infectious disease epidemiology** (SIR model) connects to \nameref{sec:unit_X_unit_intro} (disease ecology, parasite-host dynamics in community ecology).
- **Microbiome** connects to \nameref{sec:unit_IX_unit_intro} (gut-brain axis, immune regulation) and \nameref{sec:unit_X_unit_intro} (decomposer role in nutrient cycling).

> **Key vocabulary introduced here:** peptidoglycan, Gram stain, endotoxin (LPS), exotoxin, minimum inhibitory concentration (MIC), basic reproductive number (R₀), prophage, bacteriophage, quorum sensing, biofilm, prion, viroid, microbiome, dysbiosis, Koch's postulates.


## Computational Toolbox — Unit VII {.unnumbered}

```python
from biology.microbiology import bacterial_growth_curve, doubling_time

# Synthetic growth example: doubling time20min; no lag, no stationary onset or capacity ceiling.
growth = bacterial_growth_curve(N0=1e3, doubling_time_hr=1/3, t_end_hr=4, lag_phase_hr=0)
print(f"Start: {growth.populations[0]:.0f} cells")
print(f"After 4 h: {growth.populations[-1]:.2e} cells")
print(f"Growth rate: {growth.growth_rate_per_hr:.2f} h⁻¹")
# Expected:
# Start: 1000 cells
# After 4 h: 4.10e+06 cells
# Growth rate: 2.08 h⁻¹

# Doubling time from two measurements
td = doubling_time(N0=1e3, Nt=4.096e6, elapsed_time_hr=4)
print(f"Estimated doubling time: {td*60:.1f} min")
# Expected: Estimated doubling time: 20.0 min
```

> **Try it yourself:** Change `doubling_time_hr` from `1/3` to `1.0` and compare final population size after 4 hours.

---

*Source modules: `src/biology/microbiology/` — `bacterial_growth_curve()`, `doubling_time()`, `mic_fold_dilution()`, `VIRAL_REPLICATION_CYCLES`.*
*Figures: `src/visualization/` (growth curves, SIR dynamics); `src/mermaid/biology_diagrams.py` (viral replication cycle diagrams).*

## Cross-Unit Integration {.unnumbered}

\nameref{sec:unit_VII_unit_intro}'s microbiology — bacterial growth, viral replication, antimicrobial action, host–pathogen coevolution — sets up an immune-recognition problem that \nameref{sec:unit_VIII_unit_intro} confronts from the plant side first. Plants face a constant assault from microbial and viral pathogens but lack circulating immune cells; instead they deploy pattern-recognition receptors (PRRs) at the cell surface, intracellular NLR proteins, systemic acquired resistance signaling, and chemical defenses (phytoalexins, glucosinolates) that mirror — through convergent evolution — the innate-immune logic of animals. As \nameref{sec:unit_VIII_unit_intro} develops plant biology, recognize the immune-signaling motifs from \nameref{sec:unit_VII_unit_intro} (PAMP recognition, RNA-silencing antiviral defense, quorum-disrupting chemistry) reappearing in a stationary, autotrophic organism. The shared logic is older than the kingdoms.
