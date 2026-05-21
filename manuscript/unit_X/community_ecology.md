# Community Ecology and Species Interactions

\label{sec:unit_X_community_ecology}


<!-- chapter-metadata-badge -->
> **Ch 33** · Level 2/3 · 80 min read · 100 min lecture · Prerequisites: \cref{sec:unit_X_population_ecology}

## Learning Objectives

By the end of this chapter, you should be able to:

1. Define a community and categorise the six types of biotic interactions with examples.
2. Apply Lotka-Volterra competition equations to predict competitive outcomes and explain the [**competitive exclusion**](#gl:competitive-exclusion) principle and [**niche**](#gl:niche) theory.
3. Explain [**trophic cascade**](#gl:trophic-cascade)s and keystone \citep{paine1966} species with quantitative examples.
4. Compare primary and [**secondary succession**](#gl:secondary-succession) and explain the intermediate disturbance \citep{connell1978} hypothesis.
5. Calculate Shannon diversity (H'), Simpson index, and species evenness and explain what each measures.
6. Apply [**island biogeography**](#gl:island-biogeography) theory, the [**species-area relationship**](#gl:species-area-relationship), and SLOSS debate to conservation design.
7. Describe the role of disturbance, facilitation, and alternative stable states in shaping communities.
8. Explain food web topology, connectance, network robustness, and the relationship between complexity and stability.
9. Compare niche-based and neutral theories of biodiversity, and explain when each null model is appropriate.
10. Use functional traits (CSR strategies, leaf economics spectrum) to predict community assembly and ecosystem function beyond species lists.
11. Distinguish classical, augmentative, and conservation biological control, and evaluate their risk profiles using community ecology principles.

<!-- curriculum-scaffold-start -->
### Study Blueprint

- **Big idea:** Communities are structured by interactions among species and by the context of those interactions.
- **Core concepts:** competition, predation, mutualism, succession.
- **Framework alignment:** Vision & Change: Systems, Evolution, Pathways and transformations of energy and matter; AP Biology: Systems Interactions, Evolution, Energetics; NGSS-style topics: Interdependent Relationships in Ecosystems, Matter and Energy in Organisms and Ecosystems, Natural Selection and Evolution.
- **Model or quantitative lens:** Lotka-Volterra-style interaction and diversity-pattern reasoning.
- **Data skill:** Interpret abundance, interaction, or disturbance data from communities.
- **Practice cadence:** Representing and Describing Data, Statistical Tests and Data Analysis, Argumentation.
- **Common misconception to repair:** A species interaction is not permanently good or bad; the sign can change with context.
- **Primary lab:** \cref{sec:lab_unit_X_community_ecology}.
- **Question bank:** \cref{sec:q_unit_X_community_ecology}.
- **Transfer task:** Transfer interaction reasoning to restoration, disease ecology, agriculture, and invasion biology.
- **Bridge to computation:** `biology.ecology.ecology.biodiversity_indices`.
<!-- curriculum-scaffold-end -->

---

> **Opening Vignette — How Wolves Changed Rivers**
> 
> In 1995, 14 gray wolves were reintroduced to Yellowstone National Park after a 70-year absence. What happened next has become one of ecology's most vivid demonstrations of a trophic cascade. With predators back, elk avoided grazing in valleys and riverside areas where they were vulnerable. Vegetation in those areas — willows, aspens, cottonwoods — rebounded within years. With trees stabilising river banks, erosion slowed. Beaver colonies, dependent on willows, increased sixfold. Beaver dams created wetlands that supported fish, otters, ducks, and amphibians. River channels narrowed and meandered, becoming more complex. The wolves, through fear alone — the "landscape of fear" effect documented by William Ripple — had changed the physical geography of the park. The Yellowstone study has been cited thousands of times, popularised by a viral YouTube video with 40 million views, and debated (some effects took decades to show). But it remains the canonical example that removing or restoring apex predators cascades through every [**trophic level**](#gl:trophic-level) of a community.

### Chapter Roadmap

This is a long chapter that covers eight closely-related but distinguishable topics. Read it as *two halves*:

- **Part A — Local interactions between species:** what happens when two or a few species meet. The chapter begins with community definitions, then develops competition, predation and trophic cascades, [**mutualism**](#gl:mutualism), and parasitism.
- **Part B — Community-scale patterns and assembly:** what emerges when you scale up. Succession, diversity measurement, island biogeography, and food-web network structure become the organising themes.
- **Part C — Process-level theory and applications:** neutral theory supplies a null model for biodiversity; trait-based ecology (CSR, leaf economics) predicts ecosystem function; biological control applies the entire chapter to pests and disease vectors.

If you are reading for a one-semester survey, Part A supplies the mechanistic vocabulary and Part B supplies the integrative patterns. Part C provides the modern frameworks and applied translations. Instructors wanting to split the chapter over two lectures can use the Part-A/Part-B boundary; a third lecture can cover Part C.

## Community Ecology Fundamentals

An **ecological community** is an assemblage of populations of different species occupying the same region and time, interacting with each other and their [**abiotic**](#gl:abiotic) environment. Community ecology analyses the **biotic interactions** among species and their effects on community structure — species composition and relative abundance — as well as the processes driving community assembly and succession.

### Emergent Properties of Communities

Communities possess properties that cannot be predicted from studying individual species in isolation:

| Property | Definition | Measurement |
| -------- | ---------- | ----------- |
| **Species richness ($S$)** | Number of species present | Count of unique species |
| **Species evenness** | How equal are species abundances? | Pielou's $J'$ |
| **Diversity** | Combined richness and evenness | Shannon $H'$, Simpson $1-D$ |
| **Community structure** | Food web topology, trophic levels, functional groups | Network analysis, connectance |
| **Resistance** | Ability to withstand perturbation without change | Deviation from baseline after disturbance |
| **Resilience** | Speed of return to baseline after perturbation | Recovery time |
| **Rank-abundance distribution** | Pattern of relative abundance across species | Log-normal, geometric series, broken stick |

### Rank-Abundance Models

The distribution of individuals among species in a community follows predictable patterns:

| Model | Pattern | Interpretation | Typical community |
| ----- | ------- | -------------- | ----------------- |
| **Geometric series** | Steep, convex | Strong dominance; niche pre-emption | Species-poor, harsh environments |
| **Log-series** | Moderate slope | Many rare species, few common | Island faunas, successional communities |
| **Log-normal** | Moderate, symmetric bell curve on log scale | Most natural communities | Large, undisturbed communities |
| **Broken stick** | Shallow, even | Resources divided equally | Species-poor, saturated communities |

**Preston's canonical log-normal** (1962): In most large communities, when species are binned by abundance in octaves (doublings), the distribution is approximately log-normal. This has deep connections to the species-area relationship.

### Types of Biotic Interactions

```mermaid
graph TD
    subgraph "Species Interactions Matrix"
        MUT["<b>Mutualism (+/+)</b><br/>Both benefit<br/>Mycorrhizae, fig-wasp,<br/>cleaner fish, coral-zooxanthellae"]
        COM["<b>Commensalism (+/0)</b><br/>One benefits, other unaffected<br/>Cattle egret + cattle,<br/>barnacles on whale"]
        PAR["<b>Parasitism (+/−)</b><br/>Parasite benefits, host harmed<br/>Tapeworm, mistletoe,<br/>Toxoplasma, malaria"]
        PRE["<b>Predation (+/−)</b><br/>Predator benefits, prey killed<br/>Wolf-moose, owl-mouse,<br/>spider-fly"]
        COMP["<b>Competition (−/−)</b><br/>Both harmed<br/>Warblers in same tree,<br/>plants competing for light"]
        AME["<b>Amensalism (0/−)</b><br/>One unaffected, other harmed<br/>Black walnut juglone,<br/>elephant trampling"]
    end
    MUT --> OBL["Obligate vs.<br/>Facultative"]
    PAR --> COEV["Coevolutionary<br/>Arms Race"]
    PRE --> COEV
    COMP --> CE["Competitive<br/>Exclusion or<br/>Coexistence"]
```
<!-- alt: Flowchart for Types of Biotic Interactions: Mutualism (+/+) Both benefit Mycorrhizae, fig-wasp, cleaner fish, coral-zooxanthellae, Parasitism (+/−) Parasite benefits, host harmed Tapeworm, mistletoe, Toxoplasma, malaria, Predation (+/−) Predator benefits, prey killed Wolf-moose, owl-mouse, spider-fly, and Competition (−/−) Both harmed Warblers in same tree, plants competing for light form the diagram's primary path or branches. -->

*Flowchart for Types of Biotic Interactions: Mutualism (+/+) Both benefit Mycorrhizae, fig-wasp, cleaner fish, coral-zooxanthellae, Parasitism (+/−) Parasite benefits, host harmed Tapeworm, mistletoe, Toxoplasma, malaria, Predation (+/−) Predator benefits, prey killed Wolf-moose, owl-mouse, spider-fly, and Competition (−/−) Both harmed Warblers in same tree, plants competing for light form the diagram's primary path or branches.*

| Interaction | Species A effect | Species B effect | Mechanism | Example |
| ----------- | --------------- | --------------- | --------- | ------- |
| Mutualism (+/+) | Benefits | Benefits | Direct reciprocal benefit | Mycorrhizae (+plant, +fungus); fig-wasp pollination; cleaner fish |
| Commensalism (+/0) | Benefits | Neutral | One benefits, other unaffected | Cattle egret + cattle (cattle disturb insects); barnacles on whale |
| Parasitism (+/-) | Benefits ([**parasite**](#gl:parasite)) | Harmed (host) | Partial exploitation; usually not lethal | Tapeworm + human; mistletoe + tree; *Toxoplasma* + rodent |
| Predation (+/-) | Benefits (predator) | Harmed (prey) | Prey consumed; drives prey adaptation | Wolf + moose; *Daphnia* + [**phytoplankton**](#gl:phytoplankton) |
| Competition (-/-) | Harmed | Harmed | Shared resource demand | Two warbler species in same niche; plants competing for light |
| Amensalism (0/-) | Neutral | Harmed | Inhibitory compounds; physical suppression | Juglone from black walnut; [**biofilm**](#gl:biofilm) quorum quenching |

> **Concept Check:** A remora fish attaches to a shark, feeding on scraps from the shark's meals. Is this mutualism, commensalism, or parasitism? What additional information would you need to determine the exact interaction type?

---

## Competition Theory

### Lotka-Volterra Interspecific Competition

Two competing species $N_1$ and $N_2$ with shared resources are modelled by:

\begin{equation}
\frac{dN_1}{dt} = r_1 N_1 \left(1 - \frac{N_1 + \alpha_{12} N_2}{K_1}\right)
\label{eq:community_ecology_1}
\end{equation}

\begin{equation}
\frac{dN_2}{dt} = r_2 N_2 \left(1 - \frac{N_2 + \alpha_{21} N_1}{K_2}\right)
\label{eq:community_ecology_2}
\end{equation}

where:
- $\alpha_{12}$ = competitive effect of species 2 on species 1 (per individual)
- $\alpha_{21}$ = competitive effect of species 1 on species 2
- $K_1$, $K_2$ = carrying capacities of each species

**Isocline analysis:** Four outcomes depending on isocline intersections:
1. **Species 1 wins:** $K_1 > K_2/\alpha_{12}$ AND $K_1/\alpha_{21} > K_2$
2. **Species 2 wins:** $K_2 > K_1/\alpha_{21}$ AND $K_2/\alpha_{12} > K_1$ (symmetric case)
3. **Unstable equilibrium (priority effect):** $K_1 > K_2/\alpha_{12}$ AND $K_2 > K_1/\alpha_{21}$ — whoever starts higher wins
4. **Stable coexistence:** $K_1 < K_2/\alpha_{12}$ AND $K_2 < K_1/\alpha_{21}$ — interspecific competition weaker than intraspecific

### Competitive Exclusion Principle (Gause's Law)

**\citet{gause1934}:** Two species competing for the same limiting resource cannot stably coexist; the superior competitor excludes the other. Demonstrated with *Paramecium aurelia* vs. *P. caudatum* grown together on a single bacterial food source — *P. aurelia* consistently drove *P. caudatum* to extinction within 20 days.

**Important qualifications:** Competitive exclusion requires (1) complete niche overlap, (2) constant environment, (3) no spatial refugia, and (4) sufficient time. In nature, these conditions are rarely fully met.

### Hutchinson's Niche Concept

**Fundamental niche** \citep{hutchinson1957}: the n-dimensional hypervolume of environmental conditions and resources permitting a species to maintain $r \geq 0$.

**Realised niche:** the subset of the fundamental niche actually occupied after accounting for interspecific competition, predation, and other biotic interactions. Typically smaller than or equal to the fundamental niche.

\begin{equation}
\text{Realised niche} = \text{Fundamental niche} - \text{Competitive exclusion zone}
\label{eq:community_ecology_3}
\end{equation}

**Hutchinson's paradox of the plankton** (1961): Why do hundreds of phytoplankton species coexist in the apparently homogeneous water column, most competing for the same light and nutrients? Violates competitive exclusion. Solutions:

1. **Temporal niche partitioning** — seasonal turnover, disturbance prevents equilibrium
2. **Spatial heterogeneity** — microscale gradients in light, nutrients, turbulence
3. **Predation (selective grazing)** — zooplankton preferentially graze [**dominant**](#gl:dominant) species
4. **Allelopathy** — chemical warfare among phytoplankton
5. **Non-equilibrium dynamics** — the system rarely reaches competitive exclusion

### Modern Coexistence Theory \citep{chesson2000}

Coexistence requires that **intraspecific competition > interspecific competition** for both species. This is enabled by two classes of mechanisms:

**Stabilising mechanisms** (niche differences):
- **Resource partitioning:** different foods, microhabitats, activity times
- **Janzen-Connell effect:** species-specific enemies concentrate near conspecifics, giving heterospecifics an advantage
- **Storage effect:** temporal environmental variation favours different species at different times; long-lived adults "store" good years
- **Relative nonlinearity:** species respond differently to resource fluctuations

**Equalising mechanisms** (fitness similarity):
- Trade-offs between competitive ability and other traits (dispersal, stress tolerance)
- Similar per-capita growth rates at low density

The mathematical condition for coexistence is:

\begin{equation}
\rho < \frac{\kappa_j}{\kappa_i} < \frac{1}{\rho}
\label{eq:community_ecology_4}
\end{equation}

where ρ = niche overlap (0 to 1) and $\kappa_i/\kappa_j$ = fitness ratio. Lower ρ (more niche differentiation) allows greater fitness inequality.

```python
from biology.ecology.ecology import lotka_volterra

result = lotka_volterra(
    N1_0=100, N2_0=100,
    r1=0.5, r2=0.5,
    K1=500, K2=500,
    alpha12=0.6,   # species 2 slightly suppresses species 1
    alpha21=0.8,   # species 1 strongly suppresses species 2
    t_end=100
)
print(f"Final N1: {result.N1[-1]:.0f}, N2: {result.N2[-1]:.0f}")
# Expected: species 1 wins (lower alpha12 means less impact from competitor)
```

> 🔬 **Clinical Connection — Competitive Exclusion in the [**Microbiome**](#gl:microbiome):** The competitive exclusion principle operates within the human gut microbiome. **Clostridium difficile** infection (CDI) typically occurs after antibiotic treatment eliminates normal gut flora, removing competitive exclusion and allowing *C. difficile* to proliferate unopposed. **Fecal [**microbiota**](#gl:microbiota) transplantation (FMT)** restores competitive exclusion by reintroducing a diverse microbial community, achieving ~90% cure rates for recurrent CDI. This is Gause's principle applied to clinical medicine.

> **Concept Check:** Two species of Paramecium (*P. aurelia* and *P. bursaria*) coexist in the same pond. *P. aurelia* feeds on bacteria in open water; *P. bursaria* harbours symbiotic algae and feeds near the bottom. Explain their coexistence using Chesson's framework: what is the stabilising mechanism?

---

## Predation, Keystone Species, and Trophic Cascades

### Predator-Prey Arms Races

[**Coevolution**](#gl:coevolution) \citep{ehrlich1964} between predators and prey drives a Red Queen dynamic of escalating adaptations:

**Anti-predator defences:**

| Strategy | Mechanism | Example |
| -------- | --------- | ------- |
| **Crypsis** | Match background appearance | *Biston betularia* (peppered moth) — industrial melanism |
| **Aposematism** | Bright warning colours advertise toxicity | Poison dart frogs (*Dendrobates*) — alkaloid warning |
| **Mullerian mimicry** | Two toxic species converge on same warning signal | *Heliconius* butterflies sharing wing patterns |
| **Batesian mimicry** | Palatable species mimics toxic model | Viceroy (*Limenitis archippus*) mimics monarch |
| **Chemical defence** | Toxic compounds deter predators | Monarch butterflies sequester cardenolide glycosides |
| **Startle display** | Sudden reveal of eyespots or bright colours | Io moth (*Automeris io*) eyespot flash |
| **Behavioural** | Alarm calls, mobbing, confusion effect | Starling murmurations confuse raptors |
| **Morphological** | Spines, shells, armour | Porcupine quills; turtle shells; hedgehog spines |

**Counter-adaptations in predators:**
- **Kingsnakes** (*Lampropeltis*) evolved resistance to rattlesnake venom
- **Rough-skinned newt** (*Taricha granulosa*) vs. **garter snake** (*Thamnophis sirtalis*): escalating toxin (tetrodotoxin) and resistance — one of the best-documented coevolutionary arms races \citep{brodie1999}
- **Cuckoo** (*Cuculus canorus*) egg mimicry vs. host egg discrimination — classic parasitic arms race

### Hare-Lynx Cycle

*Lepus americanus* (snowshoe hare) and *Lynx canadensis* show coupled ~10-year population cycles in boreal Canada. Hudson's Bay Company fur trading records from 1736-1940 reveal the cycle. Modern analysis:

\begin{equation}
\frac{dH}{dt} = r_{max}H - aPH \qquad \frac{dP}{dt} = b \cdot a \cdot P \cdot H - dP
\label{eq:community_ecology_5}
\end{equation}

The cycle is driven by multiple feedback loops:
1. **Predation** (~60% of cycle) — lynx consumption drives hare decline
2. **Food quality** (~20%) — hare overgrazing induces phenolic toughening of willow/birch browse
3. **Stress physiology** (~20%) — predation risk elevates [**cortisol**](#gl:cortisol), suppressing reproduction
4. True cycles require **tri-trophic** feedbacks; purely Lotka-Volterra predation alone is insufficient (Krebs et al. 2001, *Science*)

### Keystone Species

A **[keystone species](#gl:keystone-species)** (Paine 1966, 1969) has disproportionately large effects on community structure relative to its abundance. Removal of the keystone causes dramatic community reorganisation.

**Types of keystone effects:**

| Type | Mechanism | Example |
| ---- | --------- | ------- |
| **Keystone predator** | Prevents competitive exclusion by suppressing dominant prey | *Pisaster ochraceus* (sea star) → prevents mussel monopoly |
| **Keystone herbivore** | Controls dominant plant, maintaining diversity | African elephant → prevents woodland encroachment on savanna |
| **Keystone mutualist** | Supports many other species through interaction network | Fig trees → fruit for 1,200+ vertebrate species in tropical forests |
| **Ecosystem engineer** | Physically modifies habitat | Beaver dams create wetland habitat for diverse communities |

### Trophic Cascades

A **trophic cascade** occurs when changes at one trophic level ripple through the food web to affect non-adjacent levels:

**Top-down cascade** (predator-driven):
- Sea otter → sea urchin → kelp cascade \citep{estes1974}
- Wolf → elk → willow cascade in Yellowstone \citep{ripple2012}

**Bottom-up cascade** (resource-driven):
- Nutrient enrichment → phytoplankton → zooplankton → fish

```mermaid
sequenceDiagram
    participant W as Wolves (reintroduced 1995)
    participant E as Elk
    participant V as Willows/Cottonwoods
    participant B as Beavers
    participant S as Stream Morphology
    participant Bio as Biodiversity

    W->>E: Predation + landscape of fear
    Note over E: Elk avoid riverbanks<br/>(behavioural trophic cascade)
    E->>V: Reduced browsing
    Note over V: Willows and cottonwoods<br/>recover along streams
    V->>B: Beaver food/dam material returns
    Note over B: Beaver population increases<br/>Dam building resumes
    B->>S: Dam pools, channel complexity
    Note over S: Stream morphology transforms<br/>Deeper pools, slower flow
    S->>Bio: Habitat diversity increases
    Note over Bio: Songbirds, fish, amphibians,<br/>insects all increase
```
<!-- alt: Sequence diagram for Trophic Cascades showing ordered interaction among Wolves (reintroduced 1995), Elk, Willows/Cottonwoods, and Beavers. -->

*Sequence diagram for Trophic Cascades showing ordered interaction among Wolves (reintroduced 1995), Elk, Willows/Cottonwoods, and Beavers.*

**Quantitative trophic cascade — Sea Otter example:**
- 1 sea otter consumes ~10 kg sea urchin/day
- Each urchin removed protects ~1 m$^2$ of kelp
- Kelp productivity: ~300 g C/m$^2$/yr
- Therefore: 1 otter → ~3,650 m$^2$ kelp protected → ~1,095 kg C/yr sequestered
- Kelp forests also attenuate wave energy by 60-70%, providing coastal protection valued at about \$10,000/km/yr

**Mesopredator release:** removal of apex predators → explosion of medium-sized predators → disproportionate prey decline. Example: coyote increase after wolf removal → ground-nesting bird decline in North America.

> 🔬 **Clinical Connection — Trophic Cascades and Lyme Disease:** The decline of apex predators in eastern North America has contributed to a trophic cascade affecting human health. Wolf and cougar removal → deer population explosion → increased tick-deer encounters → increased *Borrelia burgdorferi* transmission → Lyme disease incidence increased 25-fold from 1990 to 2020 in the northeastern USA. Deer also browse forest understory, reducing small mammal habitat diversity, which concentrates ticks on the most competent reservoir hosts (white-footed mice), further amplifying transmission. Predator restoration could reduce disease burden — a health-relevant trophic cascade.

> **Concept Check:** In Yellowstone, wolves primarily cause a "behavioural trophic cascade" rather than a purely numerical one. What is the difference? How does the "landscape of fear" concept explain why elk behaviour change (avoiding riverbanks) may be more important than elk population reduction?

---

## Mutualism, Parasitism, and Facilitation

### Mutualism

**Obligate mutualism:** neither partner can survive without the other (e.g., fig-wasp pollination; lichens = fungus + alga/cyanobacterium).

**Facultative mutualism:** both benefit but can survive independently (e.g., seed-dispersing birds and fruiting trees).

**Mycorrhizal networks:**
- **Arbuscular mycorrhizae (AM, Glomeromycota):** obligate symbionts; hyphae form arbuscules inside root cortex cells; deliver P and micronutrients; receive up to 30% of plant photosynthate; present in ~80% of land plant species
- **Ectomycorrhizae (EM, Basidiomycota + Ascomycota):** hyphae form Hartig net around root cells; dominant in temperate/boreal forests (*Pinus*, *Betula*, *Fagus*); provide N via proteolytic [**enzyme**](#gl:enzyme)s
- **Common mycorrhizal networks (CMNs) — "Wood Wide Web":** CMNs transfer carbon, water, and nutrient signals between plants of same and different species; large "mother trees" supply carbon to understory seedlings (Simard et al. 1997, *Nature*). Contested: whether transfer is truly adaptive signalling or passive diffusion remains debated (Karst et al. 2023, *Nature Ecology & Evolution*)

### Parasitism and Disease Ecology

Parasites regulate host populations and can function as keystone species:

| Parasite type | Example | Ecological effect |
| ------------- | ------- | ----------------- |
| **Macroparasite** | Intestinal helminths, ticks, lice | Reduce host fitness; can regulate population size |
| **Microparasite** | *Batrachochytrium dendrobatidis* (Bd) | Chytrid fungus: >90 amphibian species extinctions since 1970 |
| **Parasitoid** | *Cotesia glomerata* (braconid wasp) | Lays eggs inside caterpillars; larvae consume host |
| **Social parasite** | Cuckoo (*Cuculus canorus*) | Brood parasitism; reduces host reproductive output |
| **Manipulative parasite** | *Toxoplasma gondii* | Alters rodent behaviour (decreased fear of cats) to facilitate transmission |

**The parasite-mediated competition hypothesis:** parasites can determine competitive outcomes between host species, effectively functioning as "hidden" keystone species.

### Facilitation

**Facilitation** occurs when one species improves the survival or reproduction of another. Unlike mutualism, facilitation can be unidirectional:

- **Nurse plants** in deserts: cacti establish under the shade of nurse shrubs (*Larrea*, *Ambrosia*)
- **Foundation species:** create habitat structure (e.g., corals, kelp, *Spartina* grass in salt marshes)
- **Nitrogen fixers:** *Lupinus* colonises volcanic substrates, enriching soil N for later successional species (Mount St. Helens [**primary succession**](#gl:primary-succession))

> **Concept Check:** The relationship between clownfish and sea anemones is often described as mutualism. The clownfish gains protection from predators; the anemone may benefit from clownfish defending against butterfly fish that eat anemone tentacles. How would you design an experiment to determine whether this interaction is truly mutualism (+/+) or commensalism (+/0)?

---

## Ecological Succession

**Succession** = directional, generally predictable change in community composition over time after disturbance or on newly available substrate.

Contemporary succession ecology is less deterministic than the classical "march to climax" story. Recovery trajectories depend on surviving legacies, seed banks, dispersal corridors, disturbance severity, herbivory, invasive species, soil microbes, and climate conditions during recovery. The practical question is not only which stage comes next, but which intervention would change the trajectory: protecting refuges, adding propagules, removing barriers, or accepting a novel stable state.

| Feature | Primary succession | Secondary succession |
| ------- | ----------------- | -------------------- |
| Starting substrate | Bare rock/sterile substrate (no soil) | Disturbed community with soil intact |
| Typical rate | Centuries to millennia | Decades to centuries |
| Pioneer species | Cyanobacteria, lichens, mosses | Annual weeds, grasses |
| Soil development | Must form from scratch (weathering + organic accumulation) | Already present; seed bank may survive |
| Example | Krakatoa (1883); Surtsey, Iceland (1963); Mount St. Helens (1980) | Old-field succession (abandoned farmland); post-fire forest regrowth |

### Mechanisms of Succession

**\citet{connell1977}** proposed three mechanisms:

| Model | Mechanism | Example |
| ----- | --------- | ------- |
| **Facilitation** | Early species modify environment to favour later species | Nitrogen-fixing *Alnus* (alder) enriches soil, enabling spruce colonisation (Glacier Bay, Alaska) |
| **Tolerance** | Later species can establish regardless of early species but grow more slowly | Shade-tolerant species slowly replace shade-intolerant pioneers |
| **Inhibition** | Early colonists resist replacement; succession proceeds primarily when pioneers die | *Cladonia* lichen crusts inhibit vascular plant establishment on sand dunes |

```mermaid
flowchart TD
    A{Disturbance Type?} -->|"Bare substrate\n(no soil)"| B["Primary Succession\n(centuries)"]
    A -->|"Soil intact\n(seed bank present)"| C["Secondary Succession\n(decades)"]

    B --> D["Pioneer Community\nLichens, cyanobacteria, mosses\nWeathering begins"]
    C --> E["Pioneer Community\nAnnual weeds, grasses\nSeed bank germinates"]

    D --> F{Mechanism?}
    E --> F

    F -->|"Facilitation\n(Connell-Slatyer)"| G["Early species improve\nconditions for later species\n(N-fixation, soil building)"]
    F -->|"Tolerance"| H["Later species establish\nindependently; outcompete\npioneers via shade tolerance"]
    F -->|"Inhibition"| I["Pioneers resist replacement;\nsuccession only when\npioneers die or are removed"]

    G --> J["Intermediate Community\nShrubs, shade-intolerant trees\nIncreasing soil depth"]
    H --> J
    I --> J

    J --> K["Late-Successional Community\nShade-tolerant canopy species\nComplex vertical structure\nHigh biomass, low NPP/biomass"]

    K --> L{Disturbance?}
    L -->|"Fire, storm,\nhuman clearing"| C
    L -->|"Stable"| M["Dynamic Equilibrium\n(not a fixed 'climax')"]

    style D fill:#f0ad4e,color:#000
    style E fill:#f0ad4e,color:#000
    style K fill:#5cb85c,color:#fff
    style M fill:#4a90d9,color:#fff
```
<!-- alt: Flowchart showing ecological succession pathways. Primary succession begins on bare substrate and takes centuries; secondary succession begins with intact soil and proceeds in decades. Three mechanisms (facilitation, tolerance, inhibition) operate at transition points. Modern ecology views the endpoint as a dynamic equilibrium rather than a fixed climax state. -->

*Ecological succession pathways. Primary succession begins on bare substrate and takes centuries; secondary succession begins with intact soil and proceeds in decades. Three mechanisms (facilitation, tolerance, inhibition) operate at transition points. Modern ecology views the endpoint as a dynamic equilibrium rather than a fixed climax state.*

In reality, most successional sequences involve most three mechanisms operating simultaneously at different stages and spatial scales.

### Climax Community Concept

**Classical view \citep{clements1916}:** Succession proceeds toward a single, deterministic climax community determined by regional climate (the "organismal" model — community as superorganism).

**Modern view (Gleason 1926; Whittaker 1953):** Communities are assemblages of individually distributed species (the "individualistic" model). Multiple stable endpoints possible; disturbance history, stochastic colonisation, and priority effects most influence trajectory. The concept of a single climax is largely abandoned.

### Intermediate Disturbance Hypothesis (IDH)

**Connell (1978):** Communities at intermediate levels of disturbance frequency and intensity show maximum species diversity:

- **Low disturbance** → competitive exclusion → low diversity (dominant competitor wins)
- **High disturbance** → primarily r-selected pioneers survive → low diversity
- **Intermediate** → prevents competitive dominance while enabling diverse colonisation

\begin{equation}
H' = f(\text{disturbance frequency, intensity})
\label{eq:community_ecology_6}
\end{equation}

**Evidence:** Coral reefs, tropical forests, stream invertebrate communities — moderate disturbance (hurricanes, floods, fires) increases diversity.

**Criticisms:** The IDH has been challenged as overly simplistic (Fox 2013, *Ecology*). Some communities show monotonic diversity-disturbance relationships. The hypothesis also assumes a competition-colonisation trade-off that is not comprehensive.

### Alternative Stable States and Regime Shifts

**Alternative stable states** (Lewontin 1969; Scheffer et al. 2001): Some ecosystems can exist in multiple stable configurations under the same environmental conditions. Transitions between states (**regime shifts**) can be triggered by small perturbations near **tipping points**:

| System | State 1 | State 2 | Tipping mechanism |
| ------ | ------- | ------- | ----------------- |
| Shallow lake | Clear water (macrophytes dominant) | Turbid (algal bloom) | Nutrient loading exceeds P threshold |
| Coral reef | Coral dominated | Macroalgae dominated | Overfishing of herbivorous fish |
| Savanna | Grassland with scattered trees | Closed-canopy forest | Fire suppression |
| Arctic | Perennial sea ice | Seasonal/ice-free | Ocean warming threshold |

**Early warning signals** of approaching tipping points:
- Increased temporal variance (flickering)
- **Critical slowing down** — recovery from perturbation becomes slower
- Increased spatial correlation
- Skewed distribution of system state

These early warning indicators are being applied to monitor reef, lake, and climate system stability.

> 🔬 **Clinical Connection — Microbiome Regime Shifts:** The human gut microbiome exhibits alternative stable states analogous to ecological regime shifts. A healthy, diverse microbiome represents one stable state. Antibiotic treatment or *C. difficile* infection can trigger a regime shift to an impoverished, pathogenic state. Once established, the unhealthy state resists return to the diverse state (hysteresis) — explaining why probiotics alone are often insufficient and why fecal microbiota transplantation (which provides a complete microbial community) is more effective.

> **Concept Check:** After the 1980 eruption of Mount St. Helens, ecologists observed primary succession proceeding much faster than predicted. Surviving pocket gophers, ants, and lupine plants in patches of surviving soil created nuclei of rapid recovery. Which successional mechanism(s) does this illustrate, and why does it challenge Clements' classical model?

---

## Measuring Biodiversity

### Alpha, Beta, and Gamma Diversity

**\citet{whittaker1960}** distinguished three scales of diversity:

These scales also clarify what modern biodiversity tools can and cannot show. Environmental DNA, acoustic monitoring, camera traps, remote sensing, and citizen-science records can reveal turnover across space faster than classical plots alone, but each method has detection bias, taxonomic gaps, and scale limits. A credible diversity comparison states the sampling unit, detection method, taxonomic resolution, and whether the result is richness, evenness, composition, or functional change.

| Scale | Definition | Metric |
| ----- | ---------- | ------ |
| **Alpha (α) diversity** | Species richness within a single community/habitat | $H'$, Simpson's, species count |
| **Beta (β) diversity** | Turnover in species composition between communities | Jaccard index, Bray-Curtis dissimilarity |
| **Gamma (γ) diversity** | Total diversity across most communities in a landscape | $\gamma = \bar{\alpha} \times \beta$ (multiplicative) |

### Shannon-Wiener Diversity Index ($H'$)

\begin{equation}
H' = -\sum_{i=1}^{S} p_i \ln p_i
\label{eq:community_ecology_7}
\end{equation}

where $p_i$ = proportion of individuals belonging to species $i$.

- Range: $H' = 0$ (monoculture) to $H' = \ln(S)$ (perfectly even)
- Sensitive to rare species
- Typical values: 1.5-3.5 for most communities; >4.0 for extremely diverse tropical communities

### Simpson Diversity Index ($1-D$)

\begin{equation}
D = \sum_{i=1}^{S} p_i^2 \qquad \text{Simpson's diversity} = 1 - D
\label{eq:community_ecology_8}
\end{equation}

- Range: 0-1; probability that two randomly selected individuals are from **different** species
- Weighted toward dominant species (less affected by rare species than $H'$)
- Also expressed as reciprocal: Simpson's reciprocal $= 1/D$ (effective number of species)

### Pielou's Evenness ($J'$)

\begin{equation}
J' = \frac{H'}{\ln S} \in [0, 1]
\label{eq:community_ecology_9}
\end{equation}

$J' = 1$ means most species equally abundant; $J' \to 0$ means dominated by one species.

### Worked Example

| Species | Abundance | $p_i$ | $p_i \ln p_i$ | $p_i^2$ |
| ------- | --------- | ----- | -------------- | ------- |
| A | 50 | 0.500 | -0.347 | 0.250 |
| B | 30 | 0.300 | -0.361 | 0.090 |
| C | 15 | 0.150 | -0.285 | 0.023 |
| D | 4 | 0.040 | -0.129 | 0.002 |
| E | 1 | 0.010 | -0.046 | 0.000 |
| **Total** | **100** | **1.000** | **-1.167** | **0.364** |

$H' = 1.167$; $H'_{max} = \ln 5 = 1.609$; $J' = 1.167/1.609 = 0.725$

Simpson's $D = 0.364$; Simpson's diversity $= 1 - 0.364 = 0.636$

### Beta Diversity: Measuring Turnover

**Jaccard similarity index:**

\begin{equation}
J = \frac{|A \cap B|}{|A \cup B|}
\label{eq:community_ecology_10}
\end{equation}

where $A$ and $B$ are species sets from two communities. $J = 1$ means identical composition; $J = 0$ means no shared species.

**Bray-Curtis dissimilarity** (incorporates abundance):

\begin{equation}
BC = 1 - \frac{2 \sum_i \min(a_i, b_i)}{\sum_i (a_i + b_i)}
\label{eq:community_ecology_11}
\end{equation}

```python
from biology.ecology.ecology import biodiversity_indices

# Community counts (array of species abundances)
counts = [50, 30, 15, 4, 1]    # 5 species; very uneven
result = biodiversity_indices(counts)
print(f"Species richness: {result.species_richness}")
print(f"Shannon H': {result.shannon_index:.3f}")
print(f"Simpson 1-D: {result.simpson_index:.3f}")
print(f"Evenness J': {result.evenness:.3f}")
```

> **Concept Check:** Community X has 4 species with abundances [100, 100, 100, 100]. Community Y has 4 species with abundances [394, 2, 2, 2]. Both have $S = 4$. Calculate $H'$ and $J'$ for each. Which community is more "diverse" and why does evenness matter as much as richness?

---

## Island Biogeography Theory

### MacArthur-Wilson Equilibrium Model

**\citet{macarthur1967}:** *The Theory of Island Biogeography* — equilibrium species richness on islands balances immigration (colonisation) rate and extinction rate:

- **Immigration rate** decreases as $S$ increases (fewer uncolonised species remain in the mainland pool)
- **Extinction rate** increases as $S$ increases (more species present means more potential extinctions)
- At **equilibrium** ($\hat{S}$): immigration rate = extinction rate

**Effects of island characteristics:**

| Factor | Effect on $\hat{S}$ | Mechanism |
| ------ | ------------------- | --------- |
| **Larger area** | Higher $\hat{S}$ | Lower extinction rate (larger populations, more habitats) |
| **Closer to mainland** | Higher $\hat{S}$ | Higher immigration rate (easier colonisation) |
| **Small + far** | Lowest $\hat{S}$ | High extinction, low immigration |
| **Large + near** | Highest $\hat{S}$ | Low extinction, high immigration |

---

### Visualizing Food Web Connectance and Modularity

```mermaid
graph TD
    subgraph "High Connectance Web"
        A1((S1)) --- A2((S2))
        A1 --- A3((S3))
        A1 --- A4((S4))
        A2 --- A3
        A2 --- A4
        A3 --- A4
        noteA["<b>High C = L/S²</b><br/>Robust to single extinctions<br/>Rapid perturbation spread"]
    end

    subgraph "Modular Web"
        B1((M1)) --- B2((M2))
        B1 --- B3((M3))
        B2 --- B3
        
        C1((M4)) --- C2((M5))
        C1 --- C3((M6))
        C2 --- C3
        
        B2 ---|Bridge Link| C1
        noteB["<b>High Modularity</b><br/>Compartmentalised links<br/>Contains perturbations<br/>Typical of large ecosystems"]
    end

    style A1 fill:#e2e3e5,stroke:#383d41
    style B1 fill:#cfe2ff,stroke:#084298
    style C1 fill:#d1e7dd,stroke:#0f5132
```
<!-- alt: Flowchart for Visualizing Food Web Connectance and Modularity: High C = L/S² Robust to single extinctions Rapid perturbation spread and High Modularity Compartmentalised links Contains perturbations Typical of large ecosystems form the diagram's primary path or branches. -->

*Flowchart for Visualizing Food Web Connectance and Modularity: High C = L/S² Robust to single extinctions Rapid perturbation spread and High Modularity Compartmentalised links Contains perturbations Typical of large ecosystems form the diagram's primary path or branches.*

---

### Species-Area Relationship

\begin{equation}
S = cA^z
\label{eq:community_ecology_12}
\end{equation}

Log-transformed: $\log S = \log c + z \log A$

| Context | Typical $z$ | Interpretation |
| ------- | ----------- | -------------- |
| True islands | 0.20-0.35 | Higher $z$ because islands are more isolated |
| Mainland habitat fragments | 0.12-0.17 | Lower $z$ due to rescue effect from surrounding matrix |
| Archipelagoes | 0.25-0.33 | Standard island prediction |

**Practical calculation:** Doubling area increases $S$ by $\approx 19\%$ (when $z = 0.25$, since $2^{0.25} - 1 = 0.189$).

```python
import math

def species_area(c, A, z):
    return c * (A ** z)

# Old-growth forest fragment richness predictions
for area_ha in [1, 10, 100, 1000, 10000]:
    S = species_area(c=5, A=area_ha, z=0.25)
    print(f"Area = {area_ha:>6} ha → S = {S:.1f} bird species")
```

### Empirical Tests

- **Post-Krakatoa recolonisation** (1883-1983): After complete sterilisation by eruption, species accumulated toward equilibrium; initial overshoot then relaxation \citep{whittaker1975}
- **Florida Keys experiment** \citep{simberloff1969}: Fumigated small mangrove islands → recolonisation to predicted equilibrium within 2 years; confirmed immigration-extinction dynamics
- **Habitat fragments as islands:** Biological Dynamics of Forest Fragments Project (BDFFP, Amazonia; Laurance et al. 2011) — 40 years of data on isolated 1-100 ha fragments showing predictable species loss following species-area relationship

### SLOSS Debate

**Single Large Or Several Small** — for conservation, which reserve design maximises biodiversity?

| Design | Advantages | Disadvantages |
| ------ | ---------- | ------------- |
| **Single large** | Lower edge-to-interior ratio; larger MVPs; protects area-demanding species | Vulnerability to single catastrophe; may miss regional habitat diversity |
| **Several small** | Redundancy against disaster; covers more habitat types; protects local endemics | Edge effects dominant; lower $S$ per patch; connectivity problems |

**Modern consensus: Core-corridor-matrix design:**
- Large core reserves (the "single large" benefit)
- Habitat corridors or stepping stones connecting reserves
- Matrix land uses compatible with wildlife movement (agroforestry, wildlife-friendly farming)
- Example initiatives: Yellowstone-to-Yukon (Y2Y, 3,200 km); Florida Wildlife Corridor (1,000+ miles)

### Extinction Debt

**Extinction debt** (Tilman et al. 1994, *Nature*): Species currently present in degraded/fragmented habitats may be committed to future extinction — but the extinction is **delayed** by decades to centuries as existing individuals slowly die without replacement.

\begin{equation}
\text{Species committed to extinction} = S_{\text{pre-fragmentation}} - c \cdot A_{\text{remaining}}^z
\label{eq:community_ecology_13}
\end{equation}

**Implications:**
- Present-day species richness **overestimates** long-term viability
- Conservation assessments based on current presence may be dangerously optimistic
- European calcareous grasslands: 20-50% of plant species face committed extinction due to historical fragmentation \citep{lindborg2004}
- Amazon deforestation: 25-year extinction debt means current biodiversity surveys underestimate eventual losses

### Metapopulation Dynamics (Levins, 1969; Hanski, 1994)

A patchwork of habitat fragments connected by dispersal — local extinctions offset by recolonisation. Metapopulation persistence requires fraction of occupied patches to exceed extinction threshold:

\begin{equation}
\hat{p} = 1 - \frac{e}{c}
\label{eq:community_ecology_14}
\end{equation}

where $e$ = extinction rate per patch, $c$ = colonisation rate; metapopulation persists if $e/c < 1$.

**Hanski's incidence function model** extends this by incorporating patch area (affects extinction rate) and isolation (affects colonisation rate):

\begin{equation}
J_i = \frac{1}{1 + (e_i/c_i)^2}
\label{eq:community_ecology_15}
\end{equation}

where $J_i$ = probability that patch $i$ is occupied, $e_i \propto A_i^{-x}$, and $c_i$ depends on distance to occupied patches.

> 🔬 **Clinical Connection — Habitat Fragmentation and Zoonotic Disease:** As forests are fragmented into small patches, edge effects increase human-wildlife contact, facilitating zoonotic pathogen spillover. The emergence of Nipah virus in Malaysia (1998-99) was linked to bat habitat loss: displaced fruit bats (*Pteropus* spp.) moved to pig farms near forest fragments, facilitating transmission to livestock and then humans. Similarly, Ebola outbreaks correlate spatially with deforestation frontiers. Island biogeography theory predicts that small fragments lose apex predators first (mesopredator release), increasing populations of rodents and bats that serve as pathogen reservoirs.

> **Concept Check:** A national park of 10,000 km$^2$ is split by a highway into two fragments of 6,000 km$^2$ and 4,000 km$^2$. Using $S = 50A^{0.25}$, calculate species richness for: (a) the intact park, (b) each fragment separately, (c) both fragments combined assuming no species overlap. How does a wildlife corridor change your prediction?

---

## Food Web Structure and Network Ecology

### Food Web Topology

Food webs are network representations of feeding relationships in communities — a graph where nodes are species (or trophic units) and directed edges encode "$i$ eats $j$." Treating the community as a graph unlocks the entire toolbox of network science (degree distributions, clustering, modularity, motif analysis), which has reshaped community ecology over the past two decades. Key metrics:

| Metric | Definition | Typical value |
| ------ | ---------- | ------------- |
| **Connectance ($C$)** | $C = L/S^2$ (or $L/[S(S-1)/2]$); fraction of possible links realised | 0.05-0.30 |
| **Links per species ($L/S$)** | Average number of trophic links per species | ~2 for most food webs |
| **Chain length** | Number of links from base to top | 3-5 typically |
| **Omnivory** | Fraction of species feeding at >1 trophic level | ~50% in many webs |
| **Mean trophic level** | Average path length from primary producers | 2.5–3.5 typical |
| **Generality** | Mean number of resources per consumer | Skewed: most consumers specialised |
| **Vulnerability** | Mean number of consumers per resource | Skewed: most prey have few predators |
| **Nestedness** | Specialists' diets are subsets of generalists' diets | High in mutualistic networks |

```python
# Minimal food-web statistics from an adjacency dictionary
def web_stats(web):
    species = set(web).union({p for prey in web.values() for p in prey})
    S = len(species)
    L = sum(len(v) for v in web.values())
    C = L / (S * S)
    return {"S": S, "L": L, "L/S": L / S, "connectance": C}

example = {
    "phyto": [], "zoo": ["phyto"], "shrimp": ["phyto"],
    "minnow": ["zoo", "shrimp"], "bass": ["minnow", "shrimp"],
}
print(web_stats(example))
```

### Cascade Effects and Robustness

Food webs are not just descriptive: their topology predicts how perturbations propagate. Removal experiments (real or simulated) reveal three classes of network response:

| Response | Mechanism | Topological signature |
| -------- | --------- | --------------------- |
| **Bottom-up cascade** | Loss of a producer ripples upward through consumers | Few generalist consumers; long chains |
| **Top-down cascade** (\cref{eq:community_ecology_5} system) | Loss of a top predator releases mesopredators or herbivores | Strong vertical interaction strengths |
| **Horizontal cascade** | Loss of one prey shifts predator to alternative prey, harming it indirectly | Apparent competition; shared predators |

**Robustness analysis** (Dunne et al. 2002, *Ecol. Lett.*) sequentially removes species (random order, most-connected first, or rarest first) and tracks the fraction of secondary extinctions. Results across 16 well-resolved food webs:

- Random removal: ~50% of species can disappear before web collapse
- **Most-connected-first removal: collapse after about 20% of species removed** — hubs (highly connected generalists) are disproportionately important
- Rarest-first: minimal cascade — rare species are weakly embedded

This is a striking parallel to the **scale-free network** robustness literature (Barabási & Albert 1999): tolerance to random failure but vulnerability to targeted attack. For conservation, hub species are ecological-network analogues of keystone species, identifiable from topology alone.

### Complexity-Stability Debate

**May (1972, *Nature*):** Mathematical analysis of random community matrices showed that complexity (high $S$, high $C$, strong interaction strengths) **destabilises** communities — contradicting the intuitive "diversity begets stability" hypothesis. The May criterion: a random Jacobian is locally stable primarily if $\sigma\sqrt{SC} < 1$ (with σ = standard deviation of interaction strengths).

**Resolution (McCann 2000, *Nature*; Allesina & Tang 2012, *Nature*):**
- Weak interactions stabilise food webs (dampen oscillations)
- Non-random interaction structure (modularity, nestedness) promotes stability
- Real food webs are not random — they have specific architectures that enhance stability
- **Weak-interaction dominance:** most interactions are weak; few are strong. The many weak links act as stabilisers.

**Modularity:** food webs are organised into modules (compartments) with strong within-module interactions and weak between-module interactions. This structure limits the spread of perturbations — a forest pathogen outbreak in one module rarely cascades into the aquatic module of the same landscape food web.

---

## Neutral Theory of Biodiversity

The competition-coexistence theory developed earlier explains community structure through **niches** — species coexist because they differ. **Hubbell's unified neutral theory of biodiversity and biogeography (UNTB; Hubbell 2001)** proposes the radical alternative: at the scale of trophically similar species (e.g., canopy trees in a tropical forest), **most individuals are demographically equivalent** regardless of species, and observed community patterns emerge from random birth–death–dispersal–speciation alone.

### The Neutral Assumption

Each individual, regardless of species, has the same per-capita probabilities of:
- Birth (replacement of a vacancy by an offspring)
- Death (creation of a vacancy)
- Immigration $m$ from a regional **metacommunity** (replaces local community via dispersal)
- Speciation (rate ν in the metacommunity)

The local community has fixed size $J$ (zero-sum constraint — every death is replaced); dynamics are pure ecological drift, mathematically isomorphic to neutral [**genetic drift**](#gl:genetic-drift) (\cref{sec:unit_V_population_genetics}). Two parameters do most of the work:

\begin{equation}
\theta = 2 J_M \nu \qquad \text{(fundamental biodiversity number)}
\label{eq:unit_X_neutral_theta}
\end{equation}

\begin{equation}
m = \text{immigration probability per local death}
\label{eq:unit_X_neutral_m}
\end{equation}

The metacommunity size is $J_M$. Together, θ and $m$ predict species abundance distributions, species–area curves, and beta diversity — without invoking niche differences at most.

### Predictions and Empirical Successes

UNTB predicts:
- **Species abundance distribution** follows a zero-sum multinomial (very close to the rank-abundance pattern introduced earlier, but with a heavier tail of rare species)
- **Species–area relationships** with $z \approx 0.20$–0.30 (matching empirical island values, \cref{eq:community_ecology_12})
- **Beta diversity** declines with geographic distance even in homogeneous habitat (purely from limited dispersal)

Hubbell's analysis of the Barro Colorado Island 50-ha forest plot (Panama, > 200 tree species) showed UNTB fit the species abundance distribution as well as niche-based models. Volkov et al. (2003, *Nature*) confirmed neutral fits across forests in Panama, Ecuador, India, and Malaysia.

### Limits and Synthesis

UNTB has been heavily criticised: real species are *not* equivalent (massive trait variation; clear niche differences in measured demographic rates), and dynamic predictions (e.g., extinction times) often fail. The modern view, following Adler, HilleRisLambers & Levine (2007, *Ecol. Lett.*), is that **niche and neutral processes co-occur**: Chesson-style niche differences stabilise coexistence, while neutral drift adds stochastic variation in relative abundance. UNTB is the null model — if your data look neutral, you have not yet found the ecology that distinguishes species.

> **Concept Check:** Two tropical forest plots have nearly identical species-abundance distributions. The first sits in a homogeneous lowland habitat; the second spans a steep elevation gradient. Why is the *neutral* explanation of the species-abundance pattern more plausible for the first plot than the second, and what additional data would discriminate the two hypotheses?

---

## Trait-Based Community Ecology

Counting species ignores that a 1 mm aphid and a 10 m oak both add "+1" to richness. **Trait-based ecology** replaces (or complements) species lists with measured **functional traits** — morphological, physiological, or phenological attributes that influence performance. This shifts community ecology from a taxonomic enterprise to a quantitative, predictive one.

### Grime's CSR Triangle

Grime's CSR scheme (1977, 2001) classifies plant strategies along two stress axes — disturbance and stress (resource limitation) — yielding three primary strategies and the gradients between them:

| Strategy | Conditions | Trait syndrome | Examples |
| -------- | ---------- | -------------- | -------- |
| **C — Competitor** | Low stress, low disturbance | Tall, fast-growing, high biomass, deep roots; leaves long-lived but expensive | Mature forest dominants (oak, beech, *Eucalyptus*) |
| **S — Stress-tolerator** | High stress, low disturbance | Slow growth, evergreen, sclerophyllous leaves, conservative resource use | Desert succulents, alpine cushion plants, lichens, conifers in nutrient-poor soils |
| **R — Ruderal** | Low stress, high disturbance | Short-lived, high seed output, rapid maturation, weak competitors | Annual weeds (*Senecio*, *Capsella*); pioneer trees |

Most species fall along intermediates (CR, CS, SR, CSR). Crucially, the CSR axes capture independent gradients to the [**r-strategist**](#gl:r-strategist)/[**K-strategist**](#gl:k-strategist) axis of population ecology — a stress-tolerator is K-like in longevity but slow-growing, not high-fecundity.

### The Leaf Economics Spectrum

Wright et al. (2004, *Nature*) analysed > 2,500 plant species globally and uncovered a stunningly tight axis along which leaf traits co-vary — the **leaf economics spectrum (LES)**:

| Acquisitive (fast) end | Conservative (slow) end |
| ---------------------- | ----------------------- |
| High specific leaf area (SLA, m$^2$ kg$^{-1}$) | Low SLA (thick, dense leaves) |
| High mass-based photosynthetic rate ($A_{\text{mass}}$) | Low $A_{\text{mass}}$ |
| High leaf N concentration (Rubisco-rich) | Low leaf N |
| Short leaf lifespan (months) | Long leaf lifespan (years; evergreen) |
| Low construction cost per unit area | High construction cost; defended |

The LES is widely observed across biomes — tropical pioneer trees and desert annuals can occupy the same acquisitive end of the axis despite very different evolutionary histories. The axis captures a major trade-off between rapid resource capture and resource conservation, but local exceptions occur because water stress, herbivory, nutrient limitation, and phylogeny can bend the relationship. Analogous spectra exist for roots (Bergmann et al. 2020, *Sci. Adv.*) and for whole-plant strategy axes (Diaz et al. 2016, *Nature*).

### Functional Diversity and Community Assembly

Trait data enable **functional diversity** indices (functional richness, evenness, divergence; Villéger, Mason & Mouillot 2008, *Ecology*) that detect community assembly mechanisms invisible to species lists:

- **Functional clustering** (traits more similar than expected by chance) → *environmental filtering* (primarily some strategies tolerate the local abiotic conditions)
- **Functional overdispersion** (traits more different than expected) → *competitive exclusion* via limiting similarity and Chesson-style stabilising mechanisms.

A community of 30 alpine cushion plants and a community of 30 tropical canopy trees both have $S = 30$, but their trait spreads on the LES are wildly different — and that difference predicts ecosystem function (productivity, decomposition, drought response) far better than richness alone.

> **Concept Check:** Two grassland plots have identical Shannon diversity $H' = 2.5$. Plot A's plants cluster tightly on the conservative end of the LES; plot B's plants span the entire LES. Which plot is more productive on average, which is more drought-resilient, and which would you predict has stronger competitive interactions?

---

## Biological Control

The competition, predation, and parasitism theory developed above has direct translational application: **biological control** uses natural enemies to suppress pest populations, replacing or reducing chemical pesticides. It is community ecology deployed for agriculture, public health, and invasive-species management.

### Three Classical Strategies

| Strategy | Approach | Time scale | Risk profile |
| -------- | -------- | ---------- | ------------ |
| **Classical (importation)** | Import a specialist natural enemy from the pest's native range; expect it to establish and self-perpetuate | Years to decades; one-shot release | High — non-target effects if enemy is not specialist enough |
| **Augmentative** | Mass-rear and release natural enemies repeatedly to suppress current outbreak | Weeks to months; greenhouse, glasshouse | Low — released organisms typically fail to overwinter |
| **Conservation** | Modify habitat to favour resident natural enemies (hedgerows, beetle banks, insectary plants, reduced pesticide use) | Continuous | Lowest — uses native species |

### Classical Successes and Failures

**Cottony cushion scale (*Icerya purchasi*) and the vedalia beetle (*Rodolia cardinalis*).** Imported in 1888 from Australia to California citrus groves — within two years the citrus industry was saved. This is the textbook success and the prototype for most subsequent classical biocontrol programs.

**Prickly pear (*Opuntia stricta*) and *Cactoblastis cactorum*.** Released in 1925 in Australia, the moth larvae cleared 25 million ha of invasive cactus by 1940 — one of the largest-scale ecological interventions in history.

**Cane toad (*Rhinella marina*).** Released in 1935 in Queensland to control sugarcane beetles; the toads ignored the beetles, ate everything else, and are now an invasive plague across northern Australia. Classical biocontrol's most-cited cautionary tale: a generalist natural enemy will eat non-target species, and the lesson cost ecologists decades of credibility.

### Risk Assessment and Modern Practice

After the cane-toad era, regulatory frameworks (e.g., the FAO **Code of Conduct for the Import and Release of Exotic Biological Control Agents**, 1996) require:

1. **Host-specificity testing** — quarantine trials against native non-target species
2. **Climate matching** — does the agent's native climate predict its spread in the target range?
3. **Population modelling** — Lotka–Volterra or matrix projection of agent and target dynamics; predicted suppression vs. escape
4. **Reversibility analysis** — can the agent be eradicated if it causes damage? (Almost typically: no.)

Modern programs increasingly favour **conservation biological control**, which avoids introducing non-native species entirely. Field margins of insectary plants (e.g., *Phacelia*, *Fagopyrum*) increase syrphid and parasitoid wasp populations that suppress aphids in adjacent crops by 30–50 % (Tscharntke et al. 2007, *Biol. Control*). This connects directly to ecosystem-services valuation (\cref{sec:unit_X_ecosystem_ecology}).

> 🔬 **Clinical Connection — *Wolbachia* and Mosquito-Borne Disease.** Conservation biological control extends to public health. *Wolbachia* is an intracellular bacterium that, when introduced into *Aedes aegypti* mosquitoes, blocks dengue, Zika, and chikungunya virus transmission. Field trials in Yogyakarta (Indonesia) and Niterói (Brazil) released *Wolbachia*-carrying mosquitoes that spread the bacterium through the wild population via cytoplasmic incompatibility. Within 27 months of release in Yogyakarta, dengue incidence dropped 77% in treated neighbourhoods (Utarini et al. 2021, *N. Engl. J. Med.*). This is biological control of disease vectors via a manipulative endosymbiont — community ecology in service of pandemic prevention.

> **Concept Check:** A regulator must approve or reject a proposed classical biocontrol release of a parasitoid wasp against an invasive moth pest. (a) What three host-specificity tests would you require? (b) Why is "the agent attacks the target moth in the lab" insufficient evidence for safety? (c) How does a sound elasticity analysis (\cref{eq:unit_X_sensitivity_elasticity}) of the *target's* matrix model help you predict whether the release will succeed?

---

## Worked Example

**Problem:**
An ecologist surveys a small forest patch and identifies three species of trees:
- Species A: 50 individuals
- Species B: 30 individuals
- Species C: 20 individuals

Calculate the Shannon Diversity Index ($H$) for this tree community. The formula is:
$$H = -\sum (p_i \ln p_i) \label{eq:unit_X_community_ecology_item_1}$$

where $p_i$ is the proportion of total individuals belonging to the $i$-th species.

**Solution:**

**Step 1. Calculate the total number of individuals ($N$).**
$$N = 50 + 30 + 20 = 100 \label{eq:unit_X_community_ecology_item_2}$$


**Step 2. Calculate the proportion ($p_i$) for each species.**
- $p_A = 50 / 100 = 0.50$
- $p_B = 30 / 100 = 0.30$
- $p_C = 20 / 100 = 0.20$

**Step 3. Calculate $p_i \ln p_i$ for each species.**
- Species A: $0.50 \times \ln(0.50) \approx 0.50 \times (-0.693) \approx -0.347$
- Species B: $0.30 \times \ln(0.30) \approx 0.30 \times (-1.204) \approx -0.361$
- Species C: $0.20 \times \ln(0.20) \approx 0.20 \times (-1.609) \approx -0.322$

**Step 4. Sum the values and multiply by $-1$.**
$$H = - (-0.347 + -0.361 + -0.322) = - (-1.030) = 1.030 \label{eq:unit_X_community_ecology_item_3}$$


**Answer:**
The Shannon Diversity Index for this tree community is approximately **1.03**.

---

### Worked Example 2 — Intermediate Disturbance Hypothesis Quantified

**Problem:**
The intermediate disturbance hypothesis predicts a unimodal relationship between disturbance frequency $f \in [0, 1]$ and species richness $S$. A simple closed-form parameterization is

$$S(f) = S_{\max} \times 4 f (1 - f)$$

which peaks at $f = 0.5$ and falls to zero at the endpoints. For a temperate rocky-intertidal community, $S_{\max} = 25$ species. Calculate $S$ at $f = 0.2$, $f = 0.5$, and $f = 0.8$, and interpret each regime ecologically.

**Solution:**

**Step 1. Evaluate the unimodal kernel $4 f (1 - f)$.**

- $f = 0.2$: $4 \times 0.2 \times 0.8 = 0.64$, so $S = 25 \times 0.64 = 16$ species.
- $f = 0.5$: $4 \times 0.5 \times 0.5 = 1.00$, so $S = 25 \times 1.00 = 25$ species (maximum).
- $f = 0.8$: $4 \times 0.8 \times 0.2 = 0.64$, so $S = 25 \times 0.64 = 16$ species.

**Step 2. Interpret each regime ecologically.**

- *Low disturbance ($f = 0.2$, $S = 16$).* The community is on a trajectory toward competitive exclusion; dominants accumulate biomass and crowd out subordinates. Diversity is depressed not by lack of colonizers but by interspecific competition winnowing the assemblage toward the climax dominant.
- *Intermediate disturbance ($f = 0.5$, $S = 25$).* The disturbance interval is short enough to interrupt competitive exclusion but long enough to permit colonization and recruitment. This is the regime in which Paine's classic *Pisaster* removal experiments revealed predator-mediated coexistence; mussel monoculture appears once the keystone is removed and the system slides toward the low-$f$ endpoint.
- *High disturbance ($f = 0.8$, $S = 16$).* Primarily disturbance-tolerant pioneer species persist; communities are repeatedly reset before competitive sorting can proceed. Diversity is depressed by a colonization-rate bottleneck rather than by competitive exclusion.

**Step 3. Field calibration.**

The model is an idealization: real communities show asymmetric curves (skewed toward high $f$ when colonization is the limiting step) and the location of the peak shifts with productivity (Huston's dynamic equilibrium model). The qualitative prediction — that diversity is maximized at intermediate, not minimum, disturbance — is what management exploits when prescribing controlled burns, mowing regimes, or pulsed flows below dams.

**Answer:** $S(0.2) = S(0.8) = 16$, $S(0.5) = 25$. The symmetric drop on either side of $f = 0.5$ is the mathematical fingerprint of two distinct ecological mechanisms — competitive exclusion at low $f$, colonization failure at high $f$ — that look identical in a richness count but differ in management response.

---

### Concept Check (Analyze) — Trophic Cascades, Efficiency, and Eutrophication

A pelagic food web has the following annual production (kcal/m²/yr) at a baseline 10% trophic transfer efficiency: phytoplankton $= 10^6$, zooplankton $= 10^5$, planktivorous fish $= 10^4$, tuna $= 10^3$.

(a) An orca population collapse removes apex predation on tuna. Tuna biomass increases 5-fold; planktivorous fish decline by 50% (predation release from tuna); zooplankton increases by roughly 50%; phytoplankton declines. Sketch the qualitative cascade and identify which links are top-down and which are bottom-up.

(b) Now overlay agricultural nutrient loading. Nitrogen runoff increases phytoplankton production by 3×. Analyze how this bottom-up perturbation interacts with the top-down cascade in (a): does eutrophication amplify or dampen the cascade signature in zooplankton biomass? Reason explicitly about whether the limiting variable for zooplankton is now food supply or predation pressure.

(c) Predict the sign of the change in community Shannon diversity at the phytoplankton trophic level under sustained eutrophication. Reason about competitive exclusion among phytoplankton functional groups (large diatoms vs. bloom-forming cyanobacteria) at high $N$, and compare to your reasoning for the intermediate-disturbance worked example above.

---

### Concept Check (Evaluate) — Biotic Resistance and Invasive Species

Elton's diversity-resistance hypothesis predicts that high-diversity communities are harder to invade because resident species preempt resources and natural enemies are more diverse. The empirical record is split:

- **Hawaiian terrestrial bird communities** (low native diversity, severe historical isolation) were catastrophically invaded once introduced species (rats, mosquitoes, mongoose, alien plants) arrived. Tens of native bird species have gone extinct or are critically endangered.
- **Cedar Creek grassland experiments** (Tilman and collaborators) show that experimental plots seeded with higher native species richness resist exotic seedling establishment more strongly than monocultures.

(a) Evaluate which mechanism — resource preemption, enemy release, or propagule pressure — best explains the Hawaiian outcome, and which best explains the Cedar Creek outcome. Justify with at least one ecological feature of each system (isolation history, propagule supply, soil-resource limitation, herbivore community).

(b) Critique the simple Elton hypothesis: under what conditions does the diversity-resistance relationship reverse (i.e., diverse communities are *more* invasible)? Hint: consider productivity gradients and the scale at which diversity is measured (local plot vs. regional pool).

(c) Recommend a single conservation intervention for each system (Hawaii vs. Cedar Creek-type grassland) consistent with your mechanistic diagnosis, and explain why a "one-size-fits-all" invasive species strategy fails when the underlying mechanisms differ.

---

## Current Evidence and Frontier Biology

For **Community Ecology and Species Interactions**, frontier biology belongs inside the evidence logic of
the chapter. Ecology and conservation decisions increasingly combine field data, remote sensing, community knowledge, model uncertainty, and explicit values. The core reading question is this: community claims should identify interaction type, network position, disturbance regime, and observational limits.

- **What to verify:** identify the observation, model, assay, or dataset that
  would make the claim stronger or weaker.
- **What to qualify:** state the scale, organism, cell type, environmental
  condition, or population where the claim is expected to hold.
- **What to compare:** test at least one alternative explanation, baseline, or
  null model before treating the pattern as causal.
- **What to cite:** distinguish primary evidence, review synthesis, public
  dataset, and institutional guidance; for recent or numeric claims, prefer
  the source closest to the measurement and state what has changed since it was
  published.

Use biodiversity metrics carefully: population indices, extinction risk categories, ecosystem services, and management targets answer different questions \citep{ipbes2019global,ipbes2024transformative,wwf2024livingplanet,iucn2025redlist,fao2024sofia}.

**Source practice:** For conservation claims, cite assessment sources and state whether the evidence is a population index, extinction-risk assessment, ecosystem-service valuation, satellite product, or policy synthesis \citep{ipbes2024transformative,noaa2025coralbleaching,fao2025sofi}.

## Key Terms

| Term | Definition |
| ---- | ---------- |
| **Competitive exclusion principle** | Two species cannot stably coexist if they occupy the exact same niche; the superior competitor excludes the other |
| **Keystone species** | Species with disproportionately large effects on community structure relative to its abundance |
| **Trophic cascade** | Indirect effect of apex predator on plant biomass via suppressing herbivores; top-down regulation |
| **Succession** | Directional change in community composition over time; primary (bare substrate) or secondary (after disturbance) |
| **Intermediate Disturbance Hypothesis** | Moderate disturbance frequency/intensity maximises species diversity by preventing competitive exclusion |
| **Shannon diversity ($H'$)** | $H' = -\sum p_i \ln p_i$; quantifies species richness and evenness simultaneously |
| **Simpson index ($1-D$)** | Probability that two random individuals are from different species; weighted toward dominant species |
| **Species-area relationship** | $S = cA^z$; species richness increases with area; $z \approx 0.25$ for habitat islands |
| **SLOSS** | Single Large Or Several Small reserves debate in conservation biology |
| **Extinction debt** | Species present today but predicted to go extinct based on current habitat loss; time-delayed response |
| **Metapopulation** | Network of semi-isolated subpopulations connected by dispersal; local extinctions offset by recolonisation |
| **Alternative stable states** | Multiple stable community configurations under the same environmental conditions; regime shifts between states |
| **Niche differentiation** | Process by which competing species evolve to use different resources, reducing niche overlap |
| **Fundamental niche** | Full range of environmental conditions where a species can maintain $r \geq 0$ (Hutchinson) |
| **Realised niche** | Subset of fundamental niche actually occupied after biotic interactions |
| **Connectance** | Proportion of possible trophic links that are realised in a food web |
| **Facilitation** | One species improves survival or reproduction of another; mechanism of succession |
| **Beta diversity** | Species turnover between communities; measured by Jaccard or Bray-Curtis indices |
| **Neutral theory (UNTB)** | Hubbell's framework: per-capita demographic equivalence; biodiversity arises from drift, dispersal, and speciation |
| **Fundamental biodiversity number (θ)** | $\theta = 2J_M\nu$; controls species richness in the metacommunity under UNTB |
| **CSR strategies** | Grime's competitor / stress-tolerator / ruderal classification of plant strategies |
| **Leaf economics spectrum (LES)** | Comprehensive axis from acquisitive (high SLA, short-lived leaves) to conservative (thick, long-lived) leaves |
| **Functional diversity** | Trait-based diversity metric; clustering vs. overdispersion diagnoses assembly mechanism |
| **Classical biological control** | Importation of a specialist natural enemy from a pest's native range |
| **Conservation biological control** | Habitat modification to favour resident natural enemies; lowest-risk strategy |
| **Network robustness** | Resilience of a food web to species removal; collapses fastest under most-connected-first deletion |

---

## Review Questions

1. Two warbler species (*Dendroica castanea* and *D. fusca*) share a boreal spruce tree habitat. MacArthur (1958) showed they coexist by partitioning the tree into feeding zones. Using Chesson's modern coexistence theory: (a) Which of Chesson's two mechanisms (equalising vs. stabilising) enables their coexistence? (b) Write [**Lotka-Volterra equations**](#gl:lotka-volterra-equations) and specify the condition for stable coexistence in terms of $\alpha_{12}$ and $\alpha_{21}$.

2. A trophic cascade operates in Yellowstone: wolves → elk → willows → beavers → altered stream morphology. (a) Is this a bottom-up or top-down cascade? (b) Predict what happens to each level if chronic wasting disease eliminates 90% of the elk population. (c) How does the "landscape of fear" concept modify purely density-mediated cascade predictions?

3. A tropical rainforest island (area = 500 km$^2$) currently has $S = 200$ bird species. Deforestation reduces area to 125 km$^2$ (25% of original). (a) Using the species-area relationship with $z = 0.25$ and appropriate $c$, predict the final equilibrium species richness. (b) If the extinction debt takes 50 years to fully manifest, what is the expected species number at year 10 assuming linear debt decay?

4. Compare the Shannon diversity index ($H'$) for three communities:
   - Community A: 4 species, abundances = [25, 25, 25, 25]
   - Community B: 4 species, abundances = [97, 1, 1, 1]
   - Community C: 8 species, abundances = [50, 20, 10, 8, 5, 4, 2, 1]
   Calculate $H'$ and $J'$ for each. Which community shows: highest richness? highest evenness? highest $H'$?

5. Explain Hutchinson's "paradox of the plankton." Why does the coexistence of hundreds of phytoplankton species apparently violate competitive exclusion, and what are three mechanisms that resolve the paradox?

6. The Biological Dynamics of Forest Fragments Project (BDFFP) in Amazonia found that 1-ha fragments lost 50% of their bird species within 15 years, while 100-ha fragments lost 10%. (a) Calculate $z$ from these two data points. (b) Predict the species richness of a 10-ha fragment relative to a 100-ha fragment. (c) What role do edge effects play beyond the simple species-area prediction?

7. A shallow lake in the Netherlands exists in a clear-water state with abundant macrophytes. Nutrient loading from agriculture gradually increases. Describe the regime shift to the turbid, algal-dominated state using the framework of alternative stable states. Why is reducing nutrients back to the original level insufficient to restore the clear-water state (hysteresis)?

8. Design a reserve system for a large mammal species (home range = 100 km$^2$, $N_e$ requirement = 500) in a landscape of forest fragments. Use island biogeography principles to specify: (a) minimum total reserve area, (b) number and size of core reserves, (c) corridor design, (d) matrix management. Justify each design element.

9. The rough-skinned newt and common garter snake represent one of the best-documented coevolutionary arms races. Describe the escalation: what toxin does the newt produce, what resistance mechanism has the snake evolved, and what geographic mosaic pattern is observed? How does this relate to Red Queen dynamics?

10. Explain how the competitive exclusion principle applies to *Clostridium difficile* infection and its treatment by fecal microbiota transplantation. What ecological principles make FMT more effective than antibiotic treatment for recurrent CDI?
11. Using `lotka_volterra`, estimate whether predator peak **lags** prey peak for default parameters (inspect time series qualitatively).
12. How does **connectance** $C=L/S^2$ relate to stability arguments in diverse food webs?
13. Hubbell's neutral theory predicts a species-abundance distribution from drift and dispersal alone. (a) Why is UNTB best regarded as a *null model* rather than a competitor to niche theory? (b) If a community fits UNTB perfectly, what does that *not* prove about the underlying ecology? Cite the Adler, HilleRisLambers & Levine (2007) synthesis.
14. Two oak forests share identical species lists ($S = 30$, $H' = 2.8$) but differ markedly in leaf economics: forest A's species cluster on the conservative end of the LES; forest B's species span the entire spectrum. (a) Which forest is more functionally diverse? (b) Predict relative productivity, decomposition rate, and drought-resilience for each. (c) Why do two communities with identical Shannon diversity behave differently?
15. A food-web robustness analysis simulates extinctions in random vs. most-connected-first orders. The web collapses after 50% removal under random deletion but after 18% removal under most-connected-first deletion. (a) Explain the asymmetry using network topology. (b) Translate the result into a conservation prioritisation rule for hub species (analogous to keystone identification but topological).
16. A government agency proposes releasing a parasitoid wasp from East Asia to control an invasive aphid species in California. (a) Outline the host-specificity testing required before approval. (b) Why is the cane toad disaster relevant precedent? (c) Sketch how the agent and aphid populations would interact in a coupled Lotka-Volterra model — and what condition supports long-term aphid suppression rather than coexistence?

---


## Further Reading and Source Notes

- Paine (1966). Food Web Complexity and Species Diversity. *The American Naturalist*, 100.
- Connell (1978). Diversity in tropical rain forests and coral reefs. *Science*, 199.
- Gause (1934). *The Struggle for Existence*. Williams \& Wilkins.
- Hutchinson (1957). Concluding remarks. *Cold Spring Harbor Symposia on Quantitative Biology*, 22.
- Chesson (2000). Mechanisms of maintenance of species diversity. *Annual Review of Ecology and Systematics*, 31.
- Ehrlich & Raven (1964). Butterflies and plants: A study in coevolution. *Evolution*, 18.

---

## Computational Bridge

Predator--prey cycles from the chapter are reproduced by numerical integration:

```python
from biology.ecology import lotka_volterra

lv = lotka_volterra(40.0, 9.0, 0.5, 0.02, 0.01, 0.2, t_end=80.0)
print(len(lv.times), round(lv.prey[-1], 2))
```

> **Clinical / systems note:** FMT restores diversity and colonisation resistance --- an ecological intervention for a microbiome community treated as a competitive network.

---

## Summary

- **Biotic interactions:** mutualism (+/+), commensalism (+/0), parasitism (+/-), predation (+/-), competition (-/-), amensalism (0/-) — shape community composition and evolution.
- **Competition:** Lotka-Volterra equations; competitive exclusion if niches overlap completely; stable coexistence if intraspecific > interspecific effects. Modern coexistence theory \citep{chesson2000}: stabilising + equalising mechanisms.
- **Niche theory:** Hutchinson's n-dimensional hypervolume; fundamental vs. realised niche; paradox of the plankton resolved by non-equilibrium dynamics and niche partitioning.
- **Trophic cascades:** keystone predators suppress herbivores → plant biomass increases (wolves→elk→willows; sea otters→urchins→kelp). Behavioural cascades via "landscape of fear."
- **Succession:** primary (bare substrate, slow) vs. secondary (disturbed community, faster); facilitation/tolerance/inhibition mechanisms; IDH: intermediate disturbance maximises diversity; alternative stable states and regime shifts with hysteresis.
- **Diversity indices:** $H'$ (Shannon) combines richness + evenness; Simpson $1-D$ = probability of inter-specific encounter; $J'$ (evenness) = $H'/\ln S$. Alpha, beta, gamma diversity at different spatial scales.
- **Island biogeography:** $S = cA^z$; equilibrium balances colonisation and extinction; SLOSS debate resolved toward core-corridor-matrix design; extinction debt warns of delayed species loss.
- **Food web structure:** connectance, modularity, weak-interaction dominance stabilise complex communities. **Network robustness** under targeted (most-connected-first) deletion collapses faster than under random deletion — hub species are topological keystones.
- **Neutral theory (UNTB):** Hubbell's per-capita-equivalence framework; two parameters θ and $m$ predict species-abundance distributions and species–area relationships from drift, dispersal, and speciation alone. Best treated as a null model that niche-based theory must beat.
- **Trait-based ecology:** Grime's CSR triangle; the leaf economics spectrum (LES) is a widely observed acquisitive↔conservative axis with local exceptions. Functional diversity diagnoses assembly mechanisms (clustering = environmental filtering; overdispersion = limiting similarity) that species lists miss.
- **Biological control:** classical importation (vedalia beetle success; cane toad disaster), augmentative releases, and conservation biological control. *Wolbachia*-loaded *Aedes aegypti* extends the framework to vector-borne disease.
- **Connections:** See \cref{sec:unit_X_population_ecology} for consumer-resource oscillations, \cref{sec:unit_X_ecosystem_ecology} for energy flux, and \cref{sec:unit_VII_microbial_ecology} for microbial communities.

---

### Companion Source Module

**Community Ecology and Species Interactions** should leave a reproducible trail from a biological claim to
the code, figure, diagram, or paper-based activity that can test it. Use the
surfaces below to inspect the chapter's assumptions, rerun the relevant model,
or compare the manuscript explanation with companion labs and figures.

| Surface | Use it for |
| --- | --- |
| `src/biology/ecology/ecology.py` (`lotka_volterra`, `connectance`, `biodiversity_indices`) | Quantify interactions, network structure, and community diversity. |
| `src/visualization/plots.py` (`plot_lotka_volterra`, `plot_species_area_relationship`) | Inspect dynamics and richness-area patterns. |
| `src/mermaid/biology_diagrams.py` (`food_web_diagram`) | Keep trophic links and interaction signs explicit. |

**Reproducibility check:** define interaction sign, spatial scale, sampling effort, disturbance history, and network boundary before interpreting community patterns. **Cross-reference:** use \cref{sec:unit_X_population_ecology}, \cref{sec:unit_X_ecosystem_ecology}, and \cref{sec:unit_VII_microbial_ecology}.
