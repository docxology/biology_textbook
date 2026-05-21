# Student Study Guide — *Introduction to Biology*

**How to use this document:** This is a concise, exam-focused study companion to the main textbook. Print it single-sided and annotate freely. It distills each unit to: (1) core concepts, (2) essential equations, (3) key vocabulary, and (4) big-idea questions. Pair with the textbook chapters, labs, and question banks for mastery.

---

## 📊 QUICK REFERENCE TABLES

### Units Overview

| Unit | Title | Chapters | Labs | Questions | Python Domain |
|------|-------|----------|------|-----------|---------------|
| 0 | Systems Science & Complexity | 3 | 3 | 3 | `complex_adaptive_systems` |
| I | Chemistry of Life | 4 | 4 | 4 | `biochemistry`, `cell` |
| II | The Cell | 4 | 4 | 4 | `cell`, `physiology` |
| III | Energy & Metabolism | 3 | 3 | 3 | `biochemistry` |
| IV | Molecular Genetics | 4 | 4 | 4 | `genetics` |
| V | Classical Genetics | 3 | 3 | 3 | `genetics` |
| VI | Evolution | 3 | 3 | 3 | `evolution`, `ecology` |
| VII | Microbiology | 3 | 3 | 3 | `microbiology` |
| VIII | Botany | 3 | 3 | 3 | `botany` |
| IX | Zoology & Physiology | 4 | 4 | 4 | `neuroscience`, `physiology` |
| X | Ecology | 4 | 4 | 4 | `ecology` |
| **Total** | | **38** | **38** | **38** | **9 domains** |

---

## 📚 UNIT SUMMARIES

### Unit 0 — Systems Science & Complexity

**Core themes:**
- Life as an open, far-from-equilibrium system exchanging matter/energy with its environment.
- Hierarchy of biological organization: atoms → molecules → cells → organisms → populations → ecosystems.
- Feedback loops (negative and positive) and homeostasis as dynamic stability.
- Complex adaptive systems: emergent behaviour, self-organisation, robustness, and network thinking.

**Big ideas:**
1. Reductionism vs emergence — both are valid lenses.
2. Biological systems maintain order through constant energy throughput (coupling to metabolism).
3. Networks are the dominant organisational principle (gene regulatory networks, food webs, signalling cascades).

**Key vocabulary:**
- **System** — a set of interacting parts forming a complex whole.
- **Boundary** — semi-permeable demarcation between system and environment.
- **Negative feedback** — response that reduces the initial stimulus (stabilising).
- **Positive feedback** — response that amplifies the initial stimulus (destabilising / switching).
- **Emergence** — properties arising from component interactions not present in parts alone.
- **Self-organisation** — spontaneous formation of ordered structures from local interactions.
- **Homeostasis** — maintenance of a stable internal milieu (body temperature, blood glucose).
- **Open system** — exchanges matter and energy with surroundings (living systems).
- **Far-from-equilibrium** — steady state maintained by continuous energy input (dissipative structures).
- **Network motif** — recurring patterns of interconnections in biological networks.

**Study cards:**
1. Explain why living organisms are "far-from-equilibrium" systems.
2. Give two examples of negative feedback and two of positive feedback.
3. Contrast emergence with reductionism as scientific strategies.
4. How does Active Inference unify perception, action, and learning?

---

### Unit I — Chemistry of Life

**Essential equations:**

1. **Michaelis–Menten equation:**
   
   $$v = \frac{V_{max}[S]}{K_m + [S]}$$
   
   - $v$ = reaction rate (μmol min⁻¹)
   - $V_{max}$ = maximum rate when enzyme saturated
   - $K_m$ = substrate concentration at half $V_{max}$ (enzyme affinity)
   
2. **Lineweaver–Burk:**
   
   $$\frac{1}{v} = \frac{K_m}{V_{max}} \cdot \frac{1}{[S]} + \frac{1}{V_{max}}$$

3. **pH:**
   
   $$pH = -\log_{10}[H^+],\quad [H^+] = 10^{-pH}$$

4. **Henderson–Hasselbalch:**
   
   $$pH = pK_a + \log\frac{[A^-]}{[HA]}$$

**Must-know vocabulary:**
- **Electronegativity** — atom's tendency to attract shared electrons
- **Hydrophobic effect** — nonpolar molecules aggregate in water
- **Functional group** — specific atoms responsible for characteristic reactions
- **Active site** — enzyme region that binds substrate
- **Allosteric regulation** — binding at one site affects activity at another
- **Denaturation** — loss of protein structure/function
- **Micelle** — spherical lipid arrangement in water
- **Phosphodiester bond** — linkage between nucleotides

**Study cards:**
1. Derive and explain $K_m$ and $V_{max}$ significance.
2. How does competitive vs non-competitive inhibition alter the Michaelis–Menten curve?
3. Why is water an excellent solvent for ions and polar molecules?
4. List four functional groups in amino acids and their chemical properties.

---

### Unit II — The Cell

**Essential equations:**

1. **Nernst equation:**
   
   $$E_X = \frac{RT}{zF} \ln\frac{[X]_{out}}{[X]_{in}} \approx 61.5\,\text{mV} \cdot \log\frac{[X]_{out}}{[X]_{in}\text{ at } 37°C}$$

2. **Goldman–Hodgkin–Katz:**
   
   $$V_m = 61.5 \log \frac{P_{K^+}[K^+]_{out} + P_{Na^+}[Na^+]_{out} + P_{Cl^-}[Cl^-]_{in}}{P_{K^+}[K^+]_{in} + P_{Na^+}[Na^+]_{in} + P_{Cl^-}[Cl^-]_{out}}$$

3. **Osmotic pressure:**
   
   $$\Pi = iCRT$$

**Vocabulary highlights:**
- **Selective permeability** — membrane allows some substances to cross more easily
- **Tonicity** — ability of solution to cause water movement
- **Aquaporin** — channel protein specialised for water
- **Secondary active transport** — uses electrochemical gradient established by primary active transport
- **Receptor tyrosine kinase (RTK)** — enzyme-lined receptor phosphorylating tyrosines
- **Endocytosis / exocytosis** — bulk transport via vesicles
- **Lysosome** — organelle containing hydrolytic enzymes
- **Signal transduction cascade** — series amplifying extracellular signal

**Study cards:**
1. Calculate Nernst potential for K⁺ ([K⁺]ₒ=5 mM, [K⁺]ᵢ=150 mM) and Na⁺ ([Na⁺]ₒ=145 mM, [Na⁺]ᵢ=15 mM).
2. Explain why animal cells swell in pure water but plant cells do not.
3. Contrast primary and secondary active transport with examples.
4. Diagram a GPCR signal transduction pathway.

---

### Unit III — Energy and Metabolism

**Essential equations:**

1. **Gibbs free energy change:**
   
   $$\Delta G = \Delta H - T\Delta S,$$
   
   - $\Delta G < 0$ → spontaneous (exergonic); $\Delta G > 0$ → endergonic

2. **ATP hydrolysis:**
   
   $$\Delta G = \Delta G^{\circ'} + RT \ln\frac{[ADP][P_i]}{[ATP]} \approx -50\text{ to }-60\,\text{kJ/mol}$$

3. **Proton-motive force:**
   
   $$\text{PMF} = \Delta \psi - (2.3RT/F) \Delta pH \approx \Delta \psi$$

**Vocabulary highlights:**
- **Exergonic / endergonic** — energy-releasing vs requiring
- **Catabolism / anabolism** — breakdown vs synthesis
- **Redox** — NAD⁺/NADH, FAD/FADH₂ carriers
- **Substrate-level phosphorylation** — direct ATP generation
- **Oxidative phosphorylation** — ATP synthesis using ETC energy
- **Chemiosmosis** — ATP synthesis driven by H⁺ gradient
- **RuBisCO** — Calvin-cycle enzyme; also causes photorespiration

**Study cards:**
1. Balance glucose oxidation: how many ATP produced gross/net?
2. Explain chemiosmosis coupling.
3. Contrast light reactions vs Calvin cycle.
4. What is photorespiration and why does RuBisCO cause it?

---

### Unit IV — Molecular Genetics

**Essential equations:**

1. **Chi-squared test:**
   
   $$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

2. **Hardy–Weinberg equilibrium:**
   
   $$p^2 + 2pq + q^2 = 1,\quad p+q=1$$

**Vocabulary highlights:**
- **Semi-conservative replication** — one parental + one new strand
- **Okazaki fragment** — short, discontinuous lagging-strand segment
- **Telomerase** — reverse transcriptase extending telomeres
- **Promoter / operator** — transcription binding sites
- **Spliceosome** — removes introns, joins exons
- **Poly-A tail** — stability tail on eukaryotic mRNA
- **Wobble hypothesis** — flexible base pairing at codon third position
- **Epigenetics** — heritable expression changes without DNA-alteration

**Study cards:**
1. Derive expected phenotypic ratios for dihybrid cross AaBb × AaBb.
2. Compute χ² for observed 90:30 (expect 1:1).
3. If 16% recessive ($q^2=0.16$), find $p$, $q$, $2pq$.
4. Contrast transcription in prokaryotes vs eukaryotes.

---

### Unit V — Classical Genetics

**Vocabulary highlights:**
- **Allele, genotype, phenotype** — fundamentals
- **Complete/incomplete/codominance** — dominance patterns
- **Polygenic inheritance** — many genes affect one trait
- **Pleiotropy** — one gene → multiple traits
- **Epistasis** — one gene masks another's effect
- **Linkage & crossing over** — genes on same chromosome
- **Genetic map distance** — % recombination = cM
- **Pedigree analysis** — inheritance pattern inference

**Study cards:**
1. Predict X-linked colour-blindness offspring from carrier female × normal male.
2. Explain linkage's effect on 9:3:3:1 and map genes from test crosses.
3. Define nondisjunction; name two human aneuploidy disorders (Down, Turner).

---

### Unit VI — Evolution

**Essential equations:**

1. **Relative fitness:**
   
   $$w_i = \frac{\text{mean offspring of genotype } i}{\text{max mean offspring}}$$

2. **Allele frequency change due to selection:**
   
   $$\Delta p = \frac{p q (w_A - w_a)}{\bar{w}}$$

3. **Genetic drift variance:**
   
   $$\mathrm{Var}(p_{t+1}) = \frac{p_t q_t}{2N_e}$$

4. **Fixation time (neutral):** $t_{\text{fix}} \approx 4N_e$ generations

**Vocabulary highlights:**
- **Adaptation, fitness landscape** — evolutionary optimisation
- **Directional / stabilising / disruptive selection** — shifts in trait distribution
- **Bottleneck / founder effect** — diversity loss
- **Allopatric / sympatric speciation** — by geographic isolation vs within same area
- **Prezygotic / postzygotic isolating mechanisms** — reproductive barriers
- **Homologous vs analogous** — shared ancestry vs convergent function
- **Molecular clock** — roughly constant mutation rate used for dating divergences

**Study cards:**
1. Sketch the three types of selection on a trait histogram.
2. Contrast allopatric vs sympatric speciation (example each).
3. Given genotype offspring counts, compute Δp.

---

### Unit VII — Microbiology

**Essential equations:**

1. **Bacterial exponential growth:**
   
   $$N_t = N_0 \cdot 2^{t / g} = N_0 \cdot e^{\mu t}$$

   where $\mu = \ln 2 / g$ and $g$ = doubling time.

2. **Generation time from data:**
   
   $$g = \frac{t \cdot \log 2}{\log(N_t) - \log(N_0)}$$

3. **MIC** — minimum inhibitory concentration; determined by dilution or Kirby–Bauer.

**Vocabulary highlights:**
- **Peptidoglycan** — bacterial cell wall; penicillin target
- **Endospore** — dormant resistant structure
- **Plasmid** — small circular extrachromosomal DNA (antibiotic resistance common)
- **Conjugation / transformation / transduction** — HGT
- **Lysogenic cycle** — provirus integrates; can later enter lytic
- **Bacteriophage** — virus infecting bacteria
- **Biofilm** — structured bacterial community in EPS
- **Extremophile** — thrives in extremes
- **Facultative / obligate aerobe / anaerobe** — O₂ usage categories

**Study cards:**
1. *E. coli* grows from 10⁵ to 10⁸ CFU/mL in 6 h; compute doubling time.
2. Contrast conjugation, transformation, transduction.
3. What is a prophage vs a virion?

---

### Unit VIII — Botany

**Essential equations:**

1. **Water potential:** $\Psi = \Psi_s + \Psi_p$ (solute negative, pressure positive)
   
2. **Transpiration:** $E \propto VPD / r$ (vapour pressure deficit, total resistance)

**Vocabulary highlights:**
- **Xylem** — water/mineral transport up (dead at maturity)
- **Phloem** — sugar transport by pressure-flow
- **Stomata** — pores regulated by guard cells (turgor)
- **Cohesion-tension theory** — transpiration creates pulling force transmitted by H₂O cohesion
- **Phototropism** — growth toward light via auxin
- **Photoperiodism** — response to day length (short-day vs long-day plants)
- **Phytohormones** — auxin, gibberellin, cytokinin, ethylene, ABA
- **Alternation of generations** — multicellular haploid + diploid stages
- **Double fertilisation** — angiosperm-specific: zygote + endosperm

**Study cards:**
1. Cell Ψ_s = -0.8 MPa, Ψ_p = +0.6 MPa; water direction in pure water?
2. Explain cohesion-tension theory; what is cavitation?
3. Label a flower diagram.
4. Contrast short-day, long-day, day-neutral flowering.

---

### Unit IX — Zoology & Physiology

**Essential equations:**

1. **Hodgkin–Huxley** (action potential):
   
   $$C_m \frac{dV}{dt} = -(g_{Na} m^3 h (V-E_{Na}) + g_K n^4 (V-E_K) + g_L (V-E_L)) + I_{ext}$$

2. **O₂–Hb dissociation (Hill):**
   
   $$\frac{Y}{1-Y} = \left(\frac{pO_2}{P_{50}}\right)^n$$
   
   $P_{50}\approx 26$–$27\,$mmHg; $n\approx 2.8$. Bohr effect: low pH / high $pCO_2$ shifts right.

**Vocabulary highlights:**
- **Neuron / action potential / saltatory conduction** — nerve impulse basics
- **Synapse / neurotransmitter / acetylcholinesterase** — chemical signalling
- **Sliding filament model** — actin sliding past myosin in muscle; Ca²⁺ regulation
- **Sarcoplasmic reticulum** — Ca²⁺ store in muscle
- **Cardiac cycle** — atrial/ventricular systole + diastole
- **Bohr effect** — H⁺/CO₂ facilitate O₂ unloading
- **Negative feedback** — primary homeostatic mechanism

**Study cards:**
1. Sketch action potential: resting, threshold, depolarisation, repolarisation, after-hyperpolarisation.
2. Explain how myelination speeds conduction.
3. Describe sliding filament model + Ca²⁺ role.
4. Right-shifted Hb curve → interpret condition.

---

### Unit X — Ecology

**Essential equations:**

1. **Exponential growth:** $\frac{dN}{dt} = rN \;\Rightarrow\; N_t = N_0 e^{rt}$; doubling time $t_d = \ln 2 / r$.

2. **Logistic growth:** $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$.

3. **Lotka–Volterra predator–prey:**
   
   $$\frac{dN}{dt} = rN - aNP,\quad \frac{dP}{dt} = b a NP - mP$$

4. **Shannon–Wiener diversity:**
   
   $$H' = -\sum_{i=1}^{S} p_i \ln p_i$$

5. **Species–area relationship:** $S = c A^z$, $z \approx 0.2$–$0.35$ continental.

**Vocabulary highlights:**
- **Carrying capacity ($K$)** — max sustainable population
- **Density-dependent/independent** — factors whose effect changes with $N$ or not
- **K- vs r-selection** — quality vs quantity of offspring strategy
- **Trophic level** — position in food chain
- **Niche** — species' role
- **Keystone species** — disproportionate impact
- **Primary / secondary succession** — primary on barren substrate; secondary after disturbance
- **Ecological footprint / biocapacity** — human demand vs nature's supply

**Study cards:**
1. Graph logistic growth; label $K$ and inflection point.
2. Describe Lotka–Volterra cycle; effect of increased predator efficiency?
3. Compare Shannon vs Simpson diversity; which more sensitive to rare species?
4. Define ecological footprint; explain Earth Overshoot Day.

---

## 📖 HOW TO USE THIS TEXTBOOK EFFECTIVELY

1. **First pass (skimming):** Read learning objectives, skim headings, examine figures/diagrams, read summary (~20% of study time).
2. **Second pass (detailed):** Read each section carefully; work through every **Example → Solution → Answer**; derive equations on paper.
3. **Active recall:** After each section, close book, write 3-sentence summary from memory. Use end-of-chapter Review Questions first, then question bank.
4. **Spaced repetition:** Feed glossary terms into Anki; review daily.
5. **Labs:** DO THEM. Treat each as mini-research: hypothesis → data → analysis → interpretation → limitations.
6. **Cross-chapter synthesis:** Draw concept maps linking chapters each unit. Ask: "How does Unit I chemistry enable Unit II cell biology?"
7. **Figure fluency:** Redraw every Mermaid diagram by hand; recreate every matplotlib plot from memory.

---

## 🧠 SELF-ASSESSMENT: BIG QUESTIONS BY UNIT

Answer in 2–3 sentences without consulting text. Struggle → review that chapter.

- **U0:** How do far-from-equilibrium systems maintain order?
- **U1:** Why is water the "universal solvent"?
- **U2:** How can a concentration gradient become an electrical potential?
- **U3:** How does chemiosmosis couple ETC to ATP synthesis?
- **U4:** Describe the central dogma with key enzymes/RNAs.
- **U5:** Distinguish genotype vs phenotype; environment's role?
- **U6:** Is evolution goal-directed? Why not?
- **U7:** Contrast bacteria vs archaea; why are archaea closer to eukaryotes?
- **U8:** How do plants transport water upward without a pump?
- **U9:** Why is vertebrate circulatory system a closed loop?
- **U10:** Compare exponential vs logistic growth; what causes the $1-N/K$ term?

---

## 🔢 EQUATION CHEAT SHEET (ALL UNITS)

| Equation | Variables | Domain | Use case |
|---|---|---|---|
| $v = V_{max}[S]/(K_m+[S])$ | $v$, $V_{max}$, $K_m$, [S] | Enzymes | Reaction rate |
| $pH = -\log[H^+]$ | pH, [H⁺] | Chemistry | Acid–base |
| Nernst $E = 61.5\log([X]_{out}/[X]_{in})$ | $E$, concentrations, $z$ | Cell | Ion equilibrium potential |
| GHK $V_m$ | $P$, concentrations | Cell | Resting potential |
| $\Pi = iCRT$ | $\Pi,i,C,R,T$ | Cell | Osmotic pressure |
| $\Delta G = \Delta H - T\Delta S$ | $\Delta G,H,T,S$ | Metabolism | Reaction spontaneity |
| $N_t = N_0 \cdot 2^{t/g}$ | $N,t,g$ | Microbiology | Bacterial growth |
| $p^2, 2pq, q^2$ | $p,q$ | Genetics | H-W genotype |
| $\Delta p = pq(w_A - w_a)/\bar w$ | $p,q,w,\bar w$ | Evolution | Selection |
| $dN/dt = rN(1-N/K)$ | $N,r,K$ | Ecology | Logistic growth |
| $H' = -\sum p_i \ln p_i$ | $p_i,S$ | Ecology | Shannon diversity |
| $S = c A^z$ | $S,A,c,z$ | Ecology | Species-area |

---

## 📚 GLOSSARY A–Z TOP 50

(matching {#gl:slug} anchors — full definitions in `manuscript/glossary.md`)

1. active transport | 2. allele | 3. autotroph | 4. biodiversity | 5. carbohydrate
6. carrying capacity ($K$) | 7. cell theory | 8. chromosome | 9. codominance | 10. commensalism
11. convergent evolution | 12. diffusion | 13. DNA replication | 14. ecosystem | 15. endocytosis
16. enzyme | 17. evolution | 18. facilitated diffusion | 19. feedback inhibition | 20. gene
21. genetic drift | 22. genotype | 23. habitat | 24. homeostasis | 25. hydrophobic effect
26. immunity | 27. kinetic energy | 28. ligand | 29. meiosis | 30. metabolism
31. mitochondrion | 32. mutation | 33. natural selection | 34. niche | 35. osmosis
36. phenotype | 37. photosynthesis | 38. protein | 39. replication | 40. respiration
41. RNA | 42. selective permeability | 43. speciation | 44. stomata | 45. symbiosis
46. taxonomy | 47. transcription | 48. translation | 49. virus | 50. water potential ($\Psi$)

---

**Good luck! Biology is a language — speak it often, write it deliberately, and let curiosity guide your questions.**
