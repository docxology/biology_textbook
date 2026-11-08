# Questions — Population Ecology and Growth Models {#sec:q_unit_X_population_ecology .unnumbered}

## Instructor Use and Coverage Notes {.unnumbered}

This bank assesses the numbered learning objectives in \cref{sec:unit_X_population_ecology}. Each mapping is item-specific. Select by objective and task demand, not question-number band. Every item includes a four-point analytic scoring guide; accept scientifically equivalent explanations and explicitly justified assumptions.

## Questions {.unnumbered}

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define population ecology. What are the four demographic parameters that influence population size?

<!-- SOLUTION
**Answer (Q1, Recall).** Population ecology is the study of the factors that determine the size, density, distribution, age structure, and growth of populations over time. The four demographic parameters that change population size are **natality (births)**, **mortality (deaths)**, **immigration (entry)**, and **emigration (exit)**: $\Delta N = (B + I) - (D + E)$. Births and immigration add individuals; deaths and emigration remove them. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: birth/death/immigration/emigration; 2 points: specified population boundary. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. What is the exponential growth model? Write its equation.

<!-- SOLUTION
**Answer (Q2, Recall).** With constant aggregate per-capita net rate r, dN/dt=rN and N(t)=N0 exp(rt); r has units time⁻¹. For r>0, doubling time is ln(2)/r. Constant aggregate rates do not require identical reproductive outcomes for every individual. Validity depends on approximately constant rates over the modeled interval, not exclusively colonization or a bloom. The equation alone supplies no current human growth rate or verified historical population series. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: exponential differential and solution forms; 2 points: constant rate and resource assumptions.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
3. What is the logistic growth model? Write its equation and define K (carrying capacity).

<!-- SOLUTION
**Answer (Q3, Recall).** The **logistic growth model** (Verhulst 1838; rediscovered Pearl & Reed 1920) extends exponential growth by adding density-dependent self-limitation: $\dfrac{dN}{dt} = rN\!\left(1 - \dfrac{N}{K}\right)$, where **K is the carrying capacity** — the equilibrium population size supported by resources in a given environment. When $N \ll K$, the $(1 - N/K)$ term ≈ 1 and growth is near-exponential; as $N \to K$, growth slows; at $N = K$, $dN/dt = 0$. Integrated form: $N(t) = \dfrac{K}{1 + \left(\dfrac{K - N_0}{N_0}\right) e^{-rt}}$, a **sigmoid (S-shaped) curve** with inflection at $N = K/2$ (point of maximum growth rate $dN/dt_{\max} = rK/4$). K is not a physical constant: it reflects the resource ceiling — food, water, nesting sites, disease pressure — and can shift with environmental change. Classical biological example: **yeast in batch culture** (Gause 1934) fit the logistic almost exactly with K ≈ 665 cells/mL and r ≈ 0.22 h⁻¹. Modern fisheries management uses the logistic to define **maximum sustainable yield (MSY)** at N = K/2; harvesting above MSY drives fisheries to collapse (North Atlantic cod, 1992). See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: logistic equation/K; 2 points: intrinsic versus realized growth. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
4. What are r-selected and K-selected species? Give one example of each.

<!-- SOLUTION
**Answer (Q4, Recall).** **r-selected** species maximize the intrinsic rate of increase $r$: many small offspring, little parental care, early reproduction, short lifespan, Type III survivorship — favored in unstable or unpredictable environments (e.g., dandelions, mosquitoes, weedy annual plants). **K-selected** species are adapted to live near carrying capacity $K$: few large offspring, heavy parental investment, late reproduction, long lifespan, Type I survivorship — favored in stable, crowded environments (e.g., elephants, oak trees). See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: life-history tradeoffs; 2 points: continuum, not rigid taxonomy.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
5. Define survivorship curve. Describe Types I, II, and III.

<!-- SOLUTION
**Answer (Q5, Recall).** A **survivorship curve** plots the proportion of an original cohort still alive ($l_x$, log scale) against age. **Type I (late loss):** low juvenile mortality, most deaths in old age (humans, large mammals) — convex curve. **Type II (constant loss):** death probability roughly constant at all ages (many songbirds, rodents, hydra) — straight line. **Type III (early loss):** very high juvenile mortality, survivors are long-lived (oysters, oak trees, sea turtles) — concave curve. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: three survivorship shapes; 2 points: age-specific mortality interpretation. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
6. What is the mark-recapture method? Write the Lincoln-Petersen equation.

<!-- SOLUTION
**Answer (Q6, Recall).** Mark-recapture estimates the size of a mobile population: capture a sample, mark and release them, then later take a second sample and count the marked recaptures. The **Lincoln–Petersen estimator** is $\hat{N} = \dfrac{M \cdot C}{R}$, where $M$ = number marked in the first sample, $C$ = total caught in the second sample, and $R$ = marked individuals recaptured. It assumes a closed population, no mark loss, and equal catchability. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: Petersen estimator $MC/R$; 2 points: closure, mixing and capture assumptions.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
7. What is population density? Distinguish crude density from ecological density.

<!-- SOLUTION
**Answer (Q7, Recall).** Population density is the number of individuals per unit area or volume ($D = N/\text{area}$). **Crude density** uses total habitat area as the denominator, including space the species cannot use. **Ecological (specific) density** uses only the area actually occupied or usable by the species, so it more accurately reflects the local intensity of intraspecific interaction and resource demand. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: crude/ecological density; 2 points: habitable-area denominator. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
8. Define natality, mortality, immigration, and emigration.

<!-- SOLUTION
**Answer (Q8, Recall).** **Natality** is the per-capita birth rate (new individuals produced by reproduction). **Mortality** is the per-capita death rate. **Immigration** is the movement of individuals *into* the population from elsewhere. **Emigration** is the movement of individuals *out* of the population. Natality and immigration increase $N$; mortality and emigration decrease it: $\Delta N = (B+I)-(D+E)$. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: four demographic definitions; 2 points: net size change.
SOLUTION -->

<!-- assess: LO=LO9; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. What is a life table, and how can its survival and fecundity entries inform an age-structured projection matrix?

<!-- SOLUTION
**Answer (Q9, Recall).** A life table records age/stage-specific survival and reproduction. Survival transitions populate subdiagonal entries and fecundities the first row of an age-only Leslie matrix; surviving adults retained in a stage require stage-transition structure. Growth multiplier and stable structure depend on the full matrix, not fecundity alone. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: survival/fecundity table; 2 points: age/stage matrix organization. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
10. In the two-species competition model let K1=K2=100, α12=α21=.5 and both intrinsic growth rates be positive. Can each species invade the other’s monoculture? Calculate the interior equilibrium and state its stability regime.

<!-- SOLUTION
**Answer (Q10, Application).** Both invasion margins are 100−.5×100=50. Solving N1+.5N2=100 and .5N1+N2=100 gives N1=N2=66.6667. Mutual invasibility implies stable coexistence under these specified competition assumptions, not predator-prey cycling. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: both positive invasion margins and mutual invasibility; 2 points: equilibrium 66.6667 per species and stable-coexistence interpretation.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
11. An E. coli population starts with N₀ = 100 cells. The intrinsic rate of increase r = 0.693 h⁻¹ (doubling time = 1 hour). Calculate N_t at t = 5 hours using N_t = N₀e^(rt). At what time would the population reach 10⁶ cells?

<!-- SOLUTION
**Answer (Q11, Application).** Exponential model $N_t = N_0 e^{rt}$ with $N_0 = 100$, $r = 0.693\ \mathrm{h^{-1}}$. At $t = 5$ h: $N_5 = 100\,e^{0.693 \times 5} = 100\,e^{3.465} \approx 100 \times 31.96 \approx \mathbf{3200\ cells}$ (equivalently $100 \times 2^5 = 3200$, since $r$ gives a 1-hour doubling time). Time to reach $10^6$: $t = \dfrac{\ln(10^6/100)}{0.693} = \dfrac{\ln(10^4)}{0.693} = \dfrac{9.21}{0.693} \approx \mathbf{13.3\ hours}$ (≈ 13.3 doublings). See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: about 3200 at 5 h/13.29 h to 1e6; 2 points: rate/unit rounding. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
12. A deer population (K = 1,000) starts at N = 50 and grows logistically with r = 0.3/year. Calculate dN/dt at N = 50, N = 500, and N = 900. At which population size is growth rate highest? What happens to growth rate as N approaches K?

<!-- SOLUTION
**Answer (Q12, Application).** Logistic model $\dfrac{dN}{dt} = rN\!\left(1-\dfrac{N}{K}\right)$, $r = 0.3\ \mathrm{yr^{-1}}$, $K = 1000$. At **N = 50**: $0.3(50)(1-0.05) = 15 \times 0.95 \approx \mathbf{14.3\ ind/yr}$. At **N = 500**: $0.3(500)(1-0.5) = 150 \times 0.5 = \mathbf{75\ ind/yr}$. At **N = 900**: $0.3(900)(1-0.9) = 270 \times 0.1 = \mathbf{27\ ind/yr}$. Absolute growth rate is highest at $N = K/2 = 500$ ($dN/dt_{\max} = rK/4 = 75$). As $N \to K$, the $(1-N/K)$ term $\to 0$, so $dN/dt \to 0$ and the population levels off. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: growth rates of 14.25, 75 and 27 individuals/year; 2 points: maximum at $K/2$.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
13. In a mark-recapture study: 200 butterflies are captured, marked, and released. A week later, 250 butterflies are captured, of which 40 are marked. Estimate population size using the Lincoln-Petersen formula. What assumptions must hold for this estimate to be valid?

<!-- SOLUTION
**Answer (Q13, Application).** **Lincoln–Petersen estimator**: $\hat{N} = \dfrac{M \cdot C}{R}$, where $M$ = first-capture marked (200), $C$ = second-capture total (250), $R$ = recaptured marked (40). Substitute: $\hat{N} = \dfrac{200 \times 250}{40} = \dfrac{50\,000}{40} = \mathbf{1250\ \mathrm{butterflies}}$. More bias-corrected **Chapman estimator** (for small samples): $\hat{N} = \dfrac{(M+1)(C+1)}{R+1} - 1 = \dfrac{201 \times 251}{41} - 1 = 1230 - 1 = 1229$ — about 2 % smaller; use this when $R < 20$ or when sample sizes are uneven. Approximate 95 % confidence interval via $\mathrm{SE}(\hat{N}) \approx \sqrt{\dfrac{M^2 C(C-R)}{R^3}} \approx \sqrt{\dfrac{200^2 \cdot 250 \cdot 210}{40^3}} \approx 181$; CI ≈ 1250 ± 355 → **~[895, 1605] butterflies**. **Assumptions that must hold**: (i) **Closed population** (no births, deaths, immigration, emigration between capture occasions — "closed" to $N$ change); (ii) **marks are not lost or overlooked**; (iii) **marking does not affect recapture probability** (no trap-shyness, mark-induced predation, or reduced fitness); (iv) **every individual has equal capture probability** on both occasions (no sex-, age-, or site-heterogeneity); (v) **sufficient mixing** so that recaptured marked fraction is representative of the marked-to-total ratio in the full population. Violations bias the estimate — typically *upward* with trap-shyness, *downward* with heterogeneity. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: estimate of 1,250 butterflies; 2 points: sampling and mark assumptions.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
14. Can the continuous unharvested equation $dN/dt=rN(1-N/K)$, with fixed positive $r$ and $K$, produce oscillatory overshoot or a crash from below $K$? Contrast a delayed resource model.

<!-- SOLUTION
**Answer (Q14, Application).** No: growth is positive below $K$ and negative above $K$, and a trajectory beginning below $K$ approaches it monotonically without crossing. Delays, changing resources or carrying capacity, harvest and additional species can produce different dynamics but are not in that equation. Coarse Euler overshoot is numerical error, not evidence of a biological delay. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: monotone continuous dynamics with fixed $K$; 2 points: delays and resources distinguished from numerical artifacts.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
15. Compare r-selected (small, many offspring, high mortality, short lifespan) and K-selected (large, few offspring, low mortality, long lifespan) strategies. Place the following organisms on the r-K continuum: elephant, dandelion, oak tree, mosquito, whale, annual grass. Explain why the r/K model is now considered an oversimplification.

<!-- SOLUTION
**Answer (Q15, Application).** r-selected = small body, many offspring, high mortality, short life (fast end); K-selected = large body, few offspring, low mortality, long life (slow end). Ordering from r toward K: **annual grass ≈ dandelion ≈ mosquito (r-end) → oak tree → elephant ≈ whale (K-end)**. The r/K dichotomy is an oversimplification because life-history traits vary continuously and somewhat independently, environments are rarely cleanly stable or unstable, and modern demographic (life-history) theory predicts strategies from age-specific mortality and reproductive value rather than a single r–K axis. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: organism trait placement; 2 points: limits of rK classification. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
16. A Type I survivorship curve (e.g., humans) shows high survival until old age. A Type III curve (e.g., sea turtles) shows high juvenile mortality with high adult survival. Calculate: if a sea turtle lays 100 eggs per year and 2% survive to adulthood, what is the expected number of adult recruits per year? How many years of reproduction are needed to replace a dying adult (assume one-for-one replacement)?

<!-- SOLUTION
**Answer (Q16, Application).** Expected adult recruits are 100×0.02=2 per reproductive year. The stipulated one-for-one expectation corresponds to 1/2=0.5 reproductive year per replacement, not a guaranteed fractional reproductive event or a fixed waiting time to one survivor. Daughter replacement requires sex-ratio and life-history assumptions. These inputs alone provide no stage matrix, intervention effect or costs showing adult protection outperforms egg protection. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: 2 adult recruits/year; 2 points: expected 0.5 reproductive year per replacement, not a guaranteed integer event.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. The Allee effect describes a positive relationship between population density and per capita growth rate at low densities (below a threshold, the population cannot recover). Explain: (a) three mechanisms (mate finding difficulty, loss of cooperative defense, genetic problems from inbreeding); (b) how the Allee effect creates an extinction vortex for small populations; (c) what conservation strategies address the Allee effect.

<!-- SOLUTION
**Answer (Q17, Application).** (a) **Mate-finding** failure (too few encounters at low density), loss of **cooperative behaviors** (group defense, cooperative foraging/hunting, predator dilution), and **inbreeding/genetic** decline (loss of heterozygosity, fixation of deleterious alleles). (b) Below the Allee threshold per-capita growth becomes negative, so small size lowers fitness, which lowers size further — a self-reinforcing **extinction vortex** coupling demographic and genetic decay. (c) Conservation responses raise effective density: translocation/augmentation to push $N$ above threshold, captive breeding and head-starting, habitat consolidation, genetic rescue (introducing unrelated individuals), and protecting aggregation/breeding sites. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: low-density mechanisms; 2 points: strong-versus-weak threshold distinction. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO9; bloom=Analyze; difficulty=Application; format=short-answer; minutes=8 -->
18. For the stage matrix M=[[0,0,2.4],[.5,0,0],[0,.5,.4]], derive its characteristic polynomial and approximate dominant λ. Find the stable stage proportions and explain why this is not a strict age-only Leslie matrix. Compare proportional elasticities of λ to top-right fecundity and adult survival using the polynomial implicitly; identify a management limitation.

<!-- SOLUTION
**Answer (Q18, Application).** The polynomial is λ³−.4λ²−.6=0, with dominant λ=1. A right eigenvector has v2=.5v1/λ and v3=.25v1/[λ(λ−.4)]; normalization gives (12/23,6/23,5/23)≈(.52174,.26087,.21739). Adult survival in the final-stage diagonal makes this a stage/Lefkovitch model rather than strict equal-age transitions. Implicit differentiation gives E_f=(λ−s)/(3λ−2s), and E_s=s/(3λ−2s), with s=.4, so 3/11≈.27273 and 2/11≈.18182, respectively. Each transition-survival elasticity equals E_f; all entries’ elasticities sum to 1. Fecundity has larger proportional elasticity here, but feasibility, costs, covariance and uncertainty still determine intervention choice. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: polynomial, approximate eigenvalue and normalized eigenvector; 2 points: stage distinction, correctly derived elasticity comparison and management qualification.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. Source-sink metapopulation dynamics: a "source" habitat (birth rate > death rate) produces emigrants that maintain a "sink" population (death rate > birth rate). Using a specific example (e.g., wetland birds using good-quality vs poor-quality wetlands), explain: (a) why the sink population would go extinct without immigration from the source; (b) what happens if the source habitat is destroyed; (c) implications for habitat conservation priority.

<!-- SOLUTION
**Answer (Q19, Application).** (a) In a sink, deaths exceed births ($\lambda < 1$), so without a continual inflow of emigrants the local population declines deterministically to extinction. (b) If the source habitat is destroyed, the emigrant subsidy stops; the sink can no longer be propped up and **both** subpopulations decline — overall metapopulation collapse, sometimes after a deceptive lag. (c) Apparent occupancy is misleading: a crowded sink is not a healthy population. Conservation priority should weight **per-capita productivity (source status)**, protecting net exporters even if they hold fewer individuals, and avoiding investment in ecological-trap sinks. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: source export/sink dependence; 2 points: source-loss management consequence. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO10; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
20. Climate change is shifting species' ranges poleward and upslope. Evaluate: (a) the evidence from range shift data (butterflies, birds, trees); (b) why some species cannot keep pace (dispersal limitation, habitat fragmentation); (c) how population viability analysis (PVA) is used to predict extinction risk under different warming scenarios.

<!-- SOLUTION
**Answer (Q20, Synthesis).** (a) Long-term datasets show poleward/upslope range-margin shifts averaging on the order of kilometers per decade and earlier phenology in butterflies, birds, and trees, broadly tracking isotherm movement. (b) Species lag because of limited **dispersal ability**, **habitat fragmentation** blocking movement corridors, slow life cycles (long-lived trees), and dependence on biotic partners that do not move in step. (c) **PVA** projects extinction probability by combining vital rates with climate-driven scenarios for habitat and demographic parameters, comparing persistence under different warming trajectories to rank management options (corridors, assisted migration). The conclusion would change if dispersal or adaptive capacity were higher than assumed. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: range, exposure and detection data; 2 points: scenario-based PVA uncertainty.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
21. Evaluate the applicability of the logistic growth model to real populations: where does it succeed (general S-shaped growth curves in laboratory conditions) and where does it fail (time lags, environmental stochasticity, age structure, Allee effects)? Propose a more realistic model that incorporates at least two of these omitted features.

<!-- SOLUTION
**Answer (Q21, Synthesis).** The logistic **succeeds** as a description of bounded, S-shaped growth in simple, resource-limited settings (lab cultures of yeast, *Paramecium*, flour beetles) and as a management abstraction (MSY at $K/2$). It **fails** when there are reproductive **time lags**, **environmental stochasticity**, **age/stage structure**, or **Allee effects** at low density — all assumed away by instantaneous, deterministic, unstructured density dependence. A more realistic model adds a **delay** and **stochasticity**, e.g. a delayed logistic with environmental noise $\dfrac{dN}{dt} = rN\!\left(1-\dfrac{N(t-\tau)}{K}\right) + \sigma N\,\xi(t)$, or a stochastic stage-structured (Leslie/Lefkovitch) matrix with an Allee threshold. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: specified omitted mechanisms; 2 points: testable model extension. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO10; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
22. Design a long-term population monitoring program for a threatened species (e.g., African wild dog, *Lycaon pictus*). Describe: (a) camera traps, aerial surveys and genetic mark-recapture using fecal DNA; (b) demographic parameters such as finite growth rate, age-specific survival and reproductive output; (c) a PVA and an explicitly chosen persistence probability and time horizon for defining MVP.

<!-- SOLUTION
**Answer (Q22, Synthesis).** (a) Use repeatable camera-trap grids and aerial/transect surveys, plus genetic mark-recapture from fecal DNA to identify individuals and packs. Estimate detection probability rather than equate sightings with census size. (b) Estimate finite growth rate, age/stage-specific survival, reproductive output and dispersal among packs. (c) Build a stochastic age- or stage-structured PVA using these rates, demographic/environmental variation and justified inbreeding effects. Define MVP against a chosen persistence probability and time horizon; 95% over 100 generations is one possible decision criterion, not a universal definition. Sensitivity and elasticity identify model-specific leverage, while feasibility and costs determine management choices. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: repeatable detection/demography design; 2 points: persistence criterion and sensitivity. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
23. Evaluate invasive species population dynamics: the brown tree snake (*Boiga irregularis*) invaded Guam after WWII and caused the extinction of most native forest birds. Using population ecology theory: (a) what growth model best describes the initial invasion (exponential growth in the absence of natural enemies); (b) what new carrying capacity was reached; (c) what control strategies (traps, acetaminophen-laced dead mice) have been attempted, and why are they insufficient?

<!-- SOLUTION
**Answer (Q23, Synthesis).** (a) The initial invasion is **near-exponential** ($dN/dt = rN$): no native predators or competitors and abundant naive bird prey, so per-capita growth is unchecked. (b) Once prey were depleted and intraspecific limitation set in, the snake population settled at a new, prey-poor **carrying capacity** sustained on lizards, small mammals, and birds' eggs. (c) Control (live traps, hand-capture, acetaminophen-baited dead neonatal mice, detector dogs, barriers) is insufficient because the population is large, cryptic, arboreal, and reproduces faster than removal — control suppresses but cannot eradicate, so the realistic goal is interdiction to prevent spread to other islands. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: initial invasion dynamics; 2 points: control evidence, not assumed failure.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
24. Evaluate the concept of "ecological traps" — habitats that appear attractive to organisms but result in reduced fitness (e.g., sea turtles attracted to coastal lights, birds nesting in mowed agricultural fields). How do ecological traps arise (evolutionary mismatch between environmental cues and habitat quality), and how might they contribute to population decline in rapidly changing environments?

<!-- SOLUTION
**Answer (Q24, Synthesis).** An **ecological trap** arises from an **evolutionary mismatch**: animals evolved to use environmental cues (light, vegetation structure, openness) that reliably predicted habitat quality, but human-altered environments decouple the cue from actual fitness, so organisms preferentially settle in low-fitness habitat. Sea turtle hatchlings orient to the brightest horizon (historically the sea, now coastal lighting); birds select tall grass that is now mown mid-nesting. Traps depress population growth more than simple habitat loss because they actively **draw individuals away** from good habitat, and they worsen as the rate of environmental change outpaces the evolution of new cue responses. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: preference-versus-fitness mismatch; 2 points: paired habitat-selection/reproduction evidence. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. The maximum sustainable yield (MSY) of a fishery occurs at N = K/2 in the logistic model. Evaluate: (a) why harvesting at MSY maximizes catch; (b) why MSY is inherently unstable (small perturbations can push the population toward collapse); (c) why modern fisheries management uses precautionary approaches (reference points below MSY, no-take zones) rather than attempting to maintain stocks at MSY.

<!-- SOLUTION
**Answer (Q25, Synthesis).** (a) From the logistic, $dN/dt$ is maximized at $N = K/2$ (yield $= rK/4$), so harvesting that holds the stock at $K/2$ extracts the largest sustainable surplus production. (b) MSY is **unstable** because at $K/2$ the population has no buffer: any overestimate of $K$ or $r$, environmental downturn, or slight over-harvest pushes $N$ below $K/2$ where surplus production *falls*, so a fixed quota then accelerates decline toward collapse. (c) Modern management is therefore **precautionary** — target biomass above $K/2$, set harvest control rules and limit reference points below MSY, and use no-take reserves — to keep a margin against estimation error and stochasticity (cf. North Atlantic cod, 1992). See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: yield $rK/4$ at $K/2$; 2 points: quota, timestep and uncertainty distinctions.
SOLUTION -->

<!-- assess: LO=LO10; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Compare demographic and environmental stochasticity in a PVA. Is $N<50$ a universal boundary, and is the genetic 50/500 guideline an MVP?

<!-- SOLUTION
**Answer (Q26, Synthesis).** Independent individual demographic outcomes have proportionally larger fluctuations at small $N$; environmental shocks can correlate outcomes across many individuals. Their relative importance depends on vital rates and environmental covariance, not a universal threshold at $N=50$. Genetic effective-size guidelines do not specify a census-size persistence probability or time horizon; those require the explicit PVA. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: individual versus correlated shocks; 2 points: effective-size guideline distinguished from census MVP.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. Human population grew exponentially from ~1 billion (1800) to ~8 billion (2024). Evaluate: (a) which technological advances removed carrying capacity limits (agriculture, medicine, energy); (b) the demographic transition model (stages I–IV) and where different countries are; (c) whether global population will stabilize (UN WPP 2024 median projection: peak near 10.3 billion in the mid-2080s, then ~10.2 billion by 2100) or decline, and the assumptions underlying different projections.

<!-- SOLUTION
**Answer (Q27, Synthesis).** (a) The **Agricultural** (Haber–Bosch nitrogen, mechanization, Green Revolution), **medical/sanitation** (vaccines, antibiotics, clean water cutting mortality), and **energy** (fossil fuels for food, transport, fertilizer) revolutions repeatedly raised the effective human $K$. (b) The **demographic transition** moves societies from Stage I (high birth/death), through Stage II (death falls, rapid growth), Stage III (birth falls), to Stage IV (low birth/death, near-stable) — most high-income countries are at IV/V, many low-income countries still in II/III. (c) UN WPP 2024 projects a median peak near 10.3 billion in the mid-2080s and a slight decline toward about 10.2 billion by 2100; outcomes hinge on fertility-decline assumptions — faster decline yields earlier stabilization or decline, slower decline yields continued growth. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: demographic-transition assumptions; 2 points: dated conditional UN projection.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
28. Evaluate the "landscape of fear" concept: predator presence alters prey behavior (reduced foraging time, habitat avoidance), which reduces prey population growth rate even without direct predation. Using the wolf-elk-aspen trophic cascade in Yellowstone as a case study, evaluate the evidence that wolf reintroduction changed elk behavior enough to allow aspen regeneration, and whether this qualifies as a "landscape of fear" effect or simply reduced elk density.

<!-- SOLUTION
**Answer (Q28, Synthesis).** The Yellowstone wolf–elk–aspen case shows aspen recruitment improving after the 1995 wolf reintroduction. The genuine **landscape of fear** claim is that predation *risk* (not just predation mortality) alters elk behavior — less browsing in risky riparian zones — releasing aspen. The empirical difficulty is separating this **trait-mediated** (behavioral) effect from the simple **density-mediated** effect of fewer elk (also driven by hunting, drought, and bears). Evidence that would settle it: aspen release localized to high-risk microhabitats while elk density is statistically controlled. Current data support a contribution from fear but cannot fully isolate it from density reduction. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: behavioral versus density mediation; 2 points: climate/hunting controlled alternatives. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
29. Evaluate the mathematical basis for chaos in ecological populations: discrete-time logistic models (N_{t+1} = rN_t(1 − N_t/K)) with high r (period-doubling accumulation near r≈3.56995 in the normalized standard map, with periodic windows) produce chaotic dynamics where population size is deterministic but unpredictable. What does chaos imply for long-term population prediction, and how can evidence of chaos be detected in real population time series (e.g., flour beetles, *Tribolium*)?

<!-- SOLUTION
**Answer (Q29, Synthesis).** The normalized standard logistic map has a period-doubling accumulation near r≈3.56995, with periodic windows beyond it, not chaos at every larger r. Positive Lyapunov growth amplifies finite-precision initial-state/model errors and limits useful long-term prediction. Exact deterministic inputs still define exact mathematical iterates; unpredictability is not indeterminism. Real-series analysis must distinguish instability from noise, observation error and finite-sample artifacts using explicit model comparisons; the continuous unharvested logistic ODE does not itself generate chaos. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: map parameterization and periodic windows; 2 points: chaos distinguished from noise and continuous logistic dynamics.
SOLUTION -->

<!-- assess: LO=LO10; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
30. Critically evaluate the concept of "planetary boundaries" (Stockholm Resilience Center, 2009) in relation to human population ecology. Of the nine identified boundaries (climate change, biodiversity loss, nitrogen cycling, etc.), which have been transgressed, and how do population density, consumption patterns, and technology interact to determine whether human civilisation is operating within sustainable limits?

<!-- SOLUTION
**Answer (Q30, Synthesis).** **Planetary boundaries** define a 'safe operating space' across nine Earth-system processes; transgression risks abrupt, large-scale change. Boundaries assessed as **crossed** include climate change, biosphere integrity (biodiversity/genetic loss), biogeochemical flows (nitrogen and phosphorus), land-system change, freshwater change, and novel entities. Human impact is the product of **population × per-capita consumption × technology** (the IPAT relation): affluent low-population societies can transgress boundaries through consumption, while technology can raise or lower intensity. Population ecology reframes humanity as a population whose realized impact, not headcount alone, determines whether it operates within environmental limits. See \cref{sec:unit_X_population_ecology}.

**Scoring guide (4 points).** 2 points: consumption/technology/population distinctions; 2 points: dated indicators and value choices. Award partial credit for correct intermediate reasoning; for quantitative work require a stated unit/boundary when applicable.
SOLUTION -->
