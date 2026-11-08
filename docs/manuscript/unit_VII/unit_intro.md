# Unit VII — Microbiology: Introduction {#sec:unit_VII_unit_intro .unnumbered}


## Why This Unit Matters {.unnumbered}

Microorganisms are extraordinarily abundant as cells, metabolically diverse, and central to life's evolutionary history; numerical abundance is not carbon-mass dominance. Global prokaryotic abundance is of order $10^{30}$ cells. The 2018 biomass synthesis estimates plants at about 450 of 550 Gt C globally, compared with bacteria at 70 and archaea at 7 Gt C \citep{baron2018biomass}. These are extrapolated carbon-stock estimates, not cell counts: microbial uncertainty is large, especially in the deep subsurface (reported multiplicative uncertainty factors about 10 for bacteria and 13 for archaea). Bacteria and archaea occupy deep branches of the tree of life. Oxygenic photosynthesis — the ultimate energy source for most ecosystems — arose in cyanobacterial ancestry.
Nitrogen fixation, without which terrestrial
agriculture would collapse, is performed exclusively by bacteria and archaea. The atmosphere itself
was transformed by microbial metabolism long before any animal breathed it.

Medical microbiology became possible primarily after Robert Koch's postulates (1877–1884) established the
germ theory of disease — the revolutionary idea that specific microorganisms cause specific infections.
Alexander Fleming's observation in 1928 that *Penicillium* mould killed staphylococcal colonies
contributed to the development of the antibiotic era and its major therapeutic benefits. But
pathogens evolve. The emergence of multidrug-resistant organisms (MRSA, XDR-TB, carbapenem-resistant
*Enterobacteriaceae*) represents one of the most urgent public health crises of the 21st century:
an estimated 1.27 million deaths were attributable to antimicrobial resistance in 2019 (Murray et al.,
2022, *The Lancet*).

This unit combines cell biology (structure of bacteria, archaea, and viruses), quantitative
microbiology (growth curves, MIC calculations, viral replication kinetics), and ecology (the microbiome,
biogeochemical cycles, infectious disease dynamics). You will apply the S-I-R epidemiological model
and calculate R₀ under stated incidence and susceptibility assumptions; model bacterial growth and
antibiotic kill curves; and examine microbiomes as ecological communities. Distinguish community
associations with disease from evidence that a particular disruption causes a particular outcome.

---

## Landmark Discoveries {.unnumbered}

| Discoverer(s) | Year | Journal / Source | Discovery | Significance |
| ------------- | ---- | ---------------- | --------- | ------------ |
| Antoni van Leeuwenhoek | 1676 | \citep{leeuwenhoek1676} | First observation of bacteria (\"animalcules\") | Founded microbiology; showed microorganisms are everywhere |
| Louis Pasteur | 1859–1861 | \citep{pasteur1861} | Disproof of spontaneous generation | Established germ theory; revolutionised medicine and food safety |
| Robert Koch | 1876–1884 | \citep{koch1884} | Koch's postulates; anthrax, TB, cholera | Rigorous criteria for linking pathogen to disease |
| Alexander Fleming | 1928 | \citep{fleming1929} | Penicillin discovery | Launched the antibiotic era; Nobel Prize 1945 |
| Carl Woese & George Fox | 1977 | \citep{woese1977} | rRNA evidence distinguishing archaeal lineages | Changed interpretations of deep relationships; the evidence and later domain classifications are distinct |
| Eckburg, Lepp & Relman; Human Microbiome Project Consortium | 2003 review; 2012 consortium studies | \citep{relman1999,hmp2012structure} | Archaeal colonization questions and sequence-based human-community characterization | Presence is not proof of pathogenicity; community surveys are not a census establishing one universal microbial cell count |
| Murray et al. | 2022 | \citep{murray2022amr} | Global mortality from antimicrobial resistance (1.27 million deaths, 2019) | Quantified the scale of the AMR crisis as a call to action |

---

## Microbial diversity, communities, and host interactions {.unnumbered}

```mermaid
---
config:
  layout: dagre
---
graph TD
    subgraph D["Diversity and replication"]
        B["Bacteria and archaea"]
        V["Viral replication"]
        G["Growth models"]
    end
    subgraph C["Communities"]
        M["Microbiomes"]
        F["Biofilms and interactions"]
    end
    subgraph H["Host and health questions"]
        I["Immunity and vaccines"]
        R["Antimicrobial resistance"]
        T["Transmission models"]
    end
    B ---|"organism and conditions"| G
    B ---|"community membership"| M
    M ---|"community organization"| F
    M ---|"host interaction context"| I
    V ---|"host defense context"| I
    B ---|"selection and gene transfer"| R
    R ---|"distinct population processes"| T
    I ---|"endpoint-specific protection"| T
    classDef default fill:#f4f5f6,stroke:#59636e,color:#17212b
    style D fill:#fafafa,stroke:#526777,color:#17212b
    style C fill:#fafafa,stroke:#526777,color:#17212b
    style H fill:#fafafa,stroke:#526777,color:#17212b
```
<!-- alt: Graph showing microbial diversity, community interactions, and health questions are related without equating microbes with disease. Growth and viral replication require organism and host context; lytic/lysogenic alternatives are phage examples, not universal viral fates. Transmission requires stated model assumptions. Immunity and vaccines are part of this unit, not only later physiology. -->

*Microbial diversity, community interactions, and health questions are related without equating microbes with disease. Growth and viral replication require organism and host context; lytic/lysogenic alternatives are phage examples, not universal viral fates. Transmission requires stated model assumptions. Immunity and vaccines are part of this unit, not only later physiology.*

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

Microbial interactions in \nameref{sec:unit_VII_unit_intro} provide context for plant defense in \nameref{sec:unit_VIII_unit_intro}. Plants use surface recognition, intracellular defense proteins, systemic signaling, and chemical defenses without circulating immune cells. Compare these mechanisms with the host-immunity examples in this unit and the animal organization in \nameref{sec:unit_IX_unit_intro}. Similar recognition or coordination functions do not establish a single evolutionary origin, or convergent origin, for every mechanism being compared.
