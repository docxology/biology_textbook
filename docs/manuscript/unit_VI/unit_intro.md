# Unit VI — Evolution: Introduction {#sec:unit_VI_unit_intro .unnumbered}


## Why This Unit Matters {.unnumbered}

On 24 November 1859, Charles Darwin published *On the Origin of Species by Means of Natural Selection*.
The book sold out on its first day. Within a decade, the concept of evolution by natural selection had
overturned centuries of natural theology and provided biology with its first unifying theory. Theodosius
Dobzhansky's 1973 essay captured this with a sentence that has become a biologist's creed: *\"Nothing
in biology makes sense except in the light of evolution.\"*

Darwin's central insight — that heritable variation + differential reproductive success produces
cumulative directional change in populations over generations — was elegant but incomplete. He had
no mechanism for inheritance. The Modern Synthesis (1930s–1940s), forged by Fisher, Haldane, Wright,
Dobzhansky, and Mayr, married Darwinian selection to Mendelian genetics and population genetics, giving
evolution a precise mathematical foundation. A further deepening came with the neutral theory (Kimura,
1968): neutral theory emphasizes a role for stochastic genetic drift in molecular evolution.
Selection, drift, mutation, and gene flow can change allele frequencies; nonrandom mating can change
genotype proportions without necessarily changing allele frequencies. These are distinct questions.

This unit treats evolution quantitatively. You will simulate allele frequency trajectories under
selection and drift, derive the molecular clock equation and apply it to evolutionary divergence times,
examine reproductive barriers under specified population conditions, and infer phylogenetic trees using
maximum-likelihood and Bayesian methods. The tools here are the same used in clinical epidemiology
(tracking antibiotic resistance alleles), crop improvement (genomic selection), and forensic genetics
(ancestral inference from SNP profiles).

---

## Landmark Discoveries {.unnumbered}

| Discoverer(s) | Year | Journal / Source | Discovery | Significance |
| ------------- | ---- | ---------------- | --------- | ------------ |
| Darwin & Wallace | 1858–59 | \citep{darwin1858,darwin1859} | Natural selection as mechanism of evolution | Provided the first mechanistic explanation for biological diversity |
| Gregor Mendel (rediscovered) | 1900 | \citep{mendel1866} | Mendelian inheritance = mechanism for variation | Fused genetics with evolution; launched Modern Synthesis |
| Ronald Fisher | 1930 | \citep{fisher1930} | Mathematical synthesis of Darwinism + Mendelism | Developed links between inheritance and selection; do not identify the single-locus expression $\Delta q = spq^2/\bar{W}$ with the fundamental theorem or use it without allele and fitness conventions |
| Sewall Wright | 1931 | \citep{wright1931} | Genetic drift and adaptive landscapes | Showed small populations diverge by chance; $\sigma^2(\Delta p) = pq/2N_e$ |
| Motoo Kimura | 1968 | \citep{kimura1968} | Neutral theory of molecular evolution | Proposed a major role for neutral substitutions and drift; molecular-clock interpretations require rate assumptions |
| Woese & Fox | 1977 | \citep{woese1977} | rRNA evidence distinguishing archaeal lineages | Changed interpretations of deep evolutionary relationships; distinguish this evidence from later domain naming and alternative tree models |
| Svante Pääbo et al. | 2010 | \citep{paabo2010neanderthal} | Neanderthal genome sequencing | Showed interbreeding between modern humans and Neanderthals; Nobel Prize 2022 |

---

## Population change and inference of evolutionary history {.unnumbered}

```mermaid
---
config:
  layout: dagre
---
graph TD
    subgraph P["Population processes"]
        V["Heritable variation"]
        S["Selection"]
        D["Drift"]
        G["Gene flow"]
    end
    subgraph E["Divergence"]
        A["Adaptation"]
        I["Isolation and speciation"]
    end
    subgraph H["Historical inference"]
        F["Sequence and fossil evidence"]
        T["Phylogenetic inference"]
        C["Calibrated clocks"]
    end
    V ---|"heritable differences"| S
    V ---|"stochastic sampling"| D
    S ---|"fitness in context"| A
    P ---|"conditional divergence"| E
    I ---|"historical questions"| H
    F ---|"model-based inference"| T
    C ---|"calibration assumptions"| T
    classDef default fill:#f4f5f6,stroke:#59636e,color:#17212b
    style P fill:#fafafa,stroke:#526777,color:#17212b
    style E fill:#fafafa,stroke:#526777,color:#17212b
    style H fill:#fafafa,stroke:#526777,color:#17212b
```
<!-- alt: Graph showing population processes and historical inference are separate parts of evolutionary reasoning. Connections to divergence are conditional, not sufficient causes of speciation; gene flow can oppose divergence. Phylogenies and clocks depend on evidence, models, and calibration. These selected relationships are not an evolutionary sequence or causal proof. -->

*Population processes and historical inference are separate parts of evolutionary reasoning. Connections to divergence are conditional, not sufficient causes of speciation; gene flow can oppose divergence. Phylogenies and clocks depend on evidence, models, and calibration. These selected relationships are not an evolutionary sequence or causal proof.*

---

## Current Evidence Thread {.unnumbered}

Treat this unit as a converging body of evidence for evolution: the fossil record documenting transitional forms and deep time, comparative genomics revealing shared ancestry and the molecular footprints of selection, real-time selection measured in experimental and wild populations, and phylogenies that reconstruct the branching history those data imply. Evolutionary claims are strongest when they combine mechanism, comparative evidence, population process, and explicit uncertainty. As you
move through the chapters, keep a two-column note: **claim** on the left,
**evidence that would change my confidence** on the right. By the end of the
unit, each major idea should be tied to a measurement, model, citation, or
paper-based lab decision.

## Chapter Roadmap {.unnumbered}

| Chapter | Core question | Quantitative lens |
| --- | --- | --- |
| \cref{sec:unit_VI_evolution_and_selection} | How does inherited variation change under selection? | Specified fitness recurrences; breeder's equation |
| \cref{sec:unit_VI_genetic_drift_and_speciation} | How do chance and barriers affect divergence? | Diploid Wright–Fisher sampling; measured reproductive barriers |
| \cref{sec:unit_VI_phylogenetics} | What history does the evidence support? | Rooted topologies, substitution models and calibrated clocks |

---

## Connections Across the Textbook {.unnumbered}

- **Hardy–Weinberg expectations** in \cref{sec:unit_V_population_genetics} distinguish genotype proportions at specified allele frequencies from changes in those frequencies across generations. A departure in proportions alone does not identify an evolutionary process.
- **Molecular clock** and **Jukes-Cantor distances** connect to \nameref{sec:unit_IV_unit_intro} (mutation rates in DNA replication) and \nameref{sec:unit_VII_unit_intro} (phylogeny of pathogens and antibiotic-resistance evolution).
- **Speciation** links to \nameref{sec:unit_X_unit_intro} (biogeography, island species-area relationship, MacArthur-Wilson model).
- **Adaptive evolution** of immune genes connects to \nameref{sec:unit_IX_unit_intro} (MHC diversity and pathogen immunity), and antibiotic resistance evolution motivates the clinical sections of \nameref{sec:unit_VII_unit_intro}.

> **Key vocabulary introduced here:** fitness, selection coefficient, genetic drift, effective population size ($N_e$), founder effect, bottleneck, molecular clock, phylogeny, clade, synapomorphy, allopatric speciation, sympatric speciation, neutral theory, molecular systematics, maximum likelihood, bootstrap support.


## Computational Toolbox — Unit VI {.unnumbered}

```python
from biology.evolution import simulate_selection, simulate_drift

# Natural selection on a beneficial mutation (s = 0.02, starting frequency p0 = 0.01)
from biology.evolution import Population

initial = Population("beneficial allele", p=0.01, q=0.99, fitness_AA=1.02, fitness_Aa=1.01, fitness_aa=1.0)
trajectory = simulate_selection(initial, generations=200)
print(f"Generation 1:   p = {trajectory[0].p:.4f}")
print(f"Generation 100: p = {trajectory[99].p:.4f}")
print(f"Generation 200: p = {trajectory[199].p:.4f}")

# Genetic drift: small population bottleneck (Ne=50) vs. large (Ne=1000)
# Local RNG seeds are explicit; external random.seed does not seed this API.
small_pop = simulate_drift(p=0.5, N=50, generations=200, rng_seed=42)
large_pop = simulate_drift(p=0.5, N=1000, generations=200, rng_seed=43)
print(f"Ne=50  terminal p:  {small_pop[-1]:.3f}  (fixed={'yes' if small_pop[-1] in (0,1) else 'no'})")
print(f"Ne=1000 terminal p: {large_pop[-1]:.3f}")
# Small populations show large random fluctuations; large populations stay near 0.5.
```

> **Try it yourself:** Use explicit `rng_seed=1000+i` for replicates `i=0,...,99`, each with `p=.5,N=20,generations=200`. Count fixed, lost and still-polymorphic runs separately. Identical seeds replay one trajectory, not independent replication. Eventual fixation probability is 0.5 under neutrality; finite-horizon fixation among all runs need not be 0.5.

---

*Source note: the evolution module supports selection, drift, fitness-landscape, molecular-clock, sequence-distance, and isolation-index examples. Figures and Mermaid diagrams provide the selection and phylogenetic visuals.*

## Cross-Unit Integration {.unnumbered}

The mechanisms of evolution — selection, drift, mutation, gene flow, speciation — that \nameref{sec:unit_VI_unit_intro} develops in eukaryotic and metazoan systems take on a particularly stark form in the microbial world of \nameref{sec:unit_VII_unit_intro}. Bacteria and viruses evolve on timescales of hours to days; horizontal gene transfer, plasmid exchange, and conjugation bypass the vertical-inheritance assumptions that made the population-genetic models tractable; antibiotic resistance is selection-in-real-time, observable in a single hospital ward. As you encounter microbial life histories and pathogen-host coevolution in \nameref{sec:unit_VII_unit_intro}, return to the selection and drift equations of \nameref{sec:unit_VI_unit_intro} and ask what changes when generation time collapses to minutes and the "population" includes a swarm of genomes exchanging parts. The principles persist; the timescales and recombination assumptions do not.
