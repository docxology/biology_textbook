# Appendix C — Mathematical Review for Biology {.unnumbered}

\label{sec:appendix_math_review}


<!-- chapter-metadata-badge -->
> **\cref{sec:appendix_math_review}** · Level 1/3 · 45 min read · Prerequisites: none · Use as reference

This appendix collects the mathematics a reader needs to work through the quantitative chapters of this textbook. It is not a course in mathematics — it is a compact reference for the specific tools used in the chapters. Each section is self-contained; dip in as needed.

---

## C.1 Logarithms and the Natural Log {.unnumbered}

### Definition {.unnumbered}

\begin{equation}
\log_b(x) = y \iff b^y = x
\label{eq:appendices_appendix_math_review_item_1}
\end{equation}


Biology uses two bases heavily:

- **Base 10** ($\log_{10}$) — pH, sound intensity, earthquake magnitude, powers-of-ten units (nM, μM, mM).
- **Base $e$** ($\ln$, natural log) — most first-order kinetics (exponential growth, decay, enzyme kinetics), where $e \approx 2.71828$.

Conversion: $\log_{10}(x) = \ln(x) / \ln(10) \approx \ln(x) / 2.303$.

### Key identities {.unnumbered}

| Identity | Biological application |
| -------- | ---------------------- |
| $\log(ab) = \log a + \log b$ | Combining probabilities across linked loci |
| $\log(a/b) = \log a - \log b$ | Henderson-Hasselbalch $\text{pH} = \text{p}K_a + \log([\text{A}^-]/[\text{HA}])$ |
| $\log(a^n) = n \log a$ | Hill equation — slope in log-log plot |
| $\log_b(b^x) = x$ | Inverting exponential growth: $t = \ln(N/N_0)/r$ |

### Worked example — doubling time {.unnumbered}

A bacterial culture grows at $r = 0.5$ h$^{-1}$. When does the population double?

\begin{equation}
N(t) = N_0 e^{rt} = 2 N_0 \implies e^{rt} = 2 \implies t = \frac{\ln 2}{r} = \frac{0.693}{0.5} \approx 1.39 \text{ h}
\label{eq:appendices_appendix_math_review_item_2}
\end{equation}


The **"ln 2 trick"** recurs throughout biology: half-life $t_{1/2} = \ln 2 / k$ (decay); doubling time $t_d = \ln 2 / r$ (growth). Memorise $\ln 2 \approx 0.693$.

---

## C.2 Differential and Integral Calculus {.unnumbered}

Biology rarely requires advanced calculus, but the reader must be comfortable with:

### Derivatives as rates {.unnumbered}

\begin{equation}
\frac{dN}{dt} = \text{rate of change of } N \text{ over time}
\label{eq:appendices_appendix_math_review_item_3}
\end{equation}


In population ecology, $dN/dt > 0$ means the population is growing; $dN/dt = 0$ is equilibrium; $dN/dt < 0$ is decline. In enzyme kinetics, $d[P]/dt$ = reaction velocity $v$.

### Integration as accumulation {.unnumbered}

\begin{equation}
\int_0^T \frac{dN}{dt} dt = N(T) - N(0)
\label{eq:appendices_appendix_math_review_item_4}
\end{equation}


The integral sums up infinitesimal contributions. Examples:

- Total drug dose delivered by an infusion: $\text{Dose} = \int_0^T (\text{infusion rate}) dt$.
- Net photosynthesis over a day: $\int_0^{24\text{h}} P(t) dt$.

### First-order ODE: exponential growth and decay {.unnumbered}

\begin{equation}
\frac{dN}{dt} = kN \implies N(t) = N_0 e^{kt}
\label{eq:appendices_appendix_math_review_item_5}
\end{equation}


- $k > 0$: growth with doubling time $t_d = \ln 2 / k$.
- $k < 0$: decay with half-life $t_{1/2} = \ln 2 / |k|$.

### Logistic growth (nonlinear) {.unnumbered}

\begin{equation}
\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)
\label{eq:appendices_appendix_math_review_item_6}
\end{equation}


The closed-form solution is:

\begin{equation}
N(t) = \frac{K}{1 + \left(\frac{K-N_0}{N_0}\right) e^{-rt}}
\label{eq:appendices_appendix_math_review_item_7}
\end{equation}


Inflection (maximum rate) at $N = K/2$, giving the sigmoid shape.

---

## C.3 Basic Probability {.unnumbered}

### Independent events {.unnumbered}

$P(A \cap B) = P(A) \cdot P(B)$ when events are independent. Example: the probability that both parents transmit the recessive allele at a locus ($Aa \times Aa$) is $(1/2)(1/2) = 1/4$.

### Conditional probability and Bayes' theorem {.unnumbered}

\begin{equation}
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
\label{eq:appendices_appendix_math_review_item_8}
\end{equation}


Bayes' theorem — central to \cref{sec:unit_0_active_inference} and to medical testing:

\begin{equation}
P(\text{disease} \mid +) = \frac{P(+ \mid \text{disease}) \cdot P(\text{disease})}{P(+)}
\label{eq:appendices_appendix_math_review_item_9}
\end{equation}


A highly sensitive test can still have a low positive predictive value if the disease is rare — a counterintuitive result with major clinical consequences.

### Binomial distribution {.unnumbered}

Number of successes in $n$ independent trials, each with probability $p$:

\begin{equation}
P(k \text{ successes}) = \binom{n}{k} p^k (1-p)^{n-k}
\label{eq:appendices_appendix_math_review_item_10}
\end{equation}


Used for Punnett-square ratios, mark-recapture statistics, and Hardy-Weinberg proportion testing.

### Poisson distribution {.unnumbered}

For rare events at mean rate λ per interval:

\begin{equation}
P(k) = \frac{\lambda^k e^{-\lambda}}{k!}
\label{eq:appendices_appendix_math_review_item_11}
\end{equation}


Used for spontaneous mutation counts per locus, bacterial cell counts in Petri dishes (when plates are not overgrown), rare-disease incidence.

---

## C.4 Dimensional Analysis {.unnumbered}

Every physical quantity carries **units**. Units must balance on both sides of every equation — if they don't, the equation is wrong.

### Example — diffusion distance {.unnumbered}

Fick's rule for mean diffusion distance:

\begin{equation}
x = \sqrt{2Dt}
\label{eq:appendices_appendix_math_review_item_12}
\end{equation}


Check units: $D$ has units of m² s⁻¹; $t$ has units of s; so $\sqrt{2Dt}$ has units of $\sqrt{\text{m}^2} = \text{m}$. ✓

If a student wrote $x = Dt$, units would be m² s⁻¹ · s = m² — dimensionally wrong.

### Standard SI units used in this book {.unnumbered}

| Quantity | Symbol | SI unit | Typical biological magnitude |
| -------- | ------ | ------- | --------------------------- |
| Length | $l$ | m | cell: 10 μm; neuron: 1 m |
| Mass | $m$ | kg | ribosome: 3 × 10⁻²¹ kg; cell: 10⁻¹² kg |
| Time | $t$ | s | AP: 1 ms; cell cycle: 24 h |
| Amount | $n$ | mol | ATP in a cell: 10⁻¹⁵ mol |
| Concentration | $[X]$ | mol L⁻¹ = M | cytoplasmic ATP: 5 × 10⁻³ M |
| Energy | $E$ | J | ATP hydrolysis: 5 × 10⁻²⁰ J per molecule, ≈30.5 kJ mol⁻¹ |
| Force | $F$ | N | myosin step force: 5 × 10⁻¹² N = 5 pN |
| Electric potential | $V$ | V | resting membrane: −0.07 V = −70 mV |

### Non-SI units common in biology {.unnumbered}

| Unit | SI equivalent | Use |
| ---- | ------------- | --- |
| mmHg (Torr) | 133.322 Pa | blood pressure, gas partial pressures |
| cal | 4.184 J | nutrition ("Calorie" = kcal) |
| pH unit | $-\log_{10}[\text{H}^+]$ in M | acidity |
| Da (dalton) | 1.661 × 10⁻²⁷ kg | molecular mass |
| Kelvin (K) | °C + 273.15 | thermodynamics requires K, not °C |

---

## C.5 Linear Algebra Miniature {.unnumbered}

Primarily trace knowledge is required for this book, but the two ideas below recur.

### Matrices as transitions {.unnumbered}

Allele-frequency change under migration between two populations is a 2 × 2 matrix multiplication. Markov transition matrices describe stochastic gene expression (lac operon), state transitions in ion channels, and Wright-Fisher drift.

### Eigenvalues and equilibrium {.unnumbered}

The dominant eigenvalue $\lambda_1$ of a Leslie matrix equals the long-term finite rate of increase. Eigenvectors give the stable age distribution. This is the formal underpinning of \cref{sec:unit_X_population_ecology}'s demographic analysis.

---

## C.6 Common Pitfalls in Biological Math {.unnumbered}

1. **Confusing concentration and amount.** 1 nM is a concentration; 1 nmol is an amount. A picomole of hormone in 5 L of blood is 0.2 pM.
2. **Units of rate constants.** First-order: s⁻¹. Second-order: M⁻¹ s⁻¹. Third-order: M⁻² s⁻¹. Dimensional analysis typically exposes an order-of-magnitude error.
3. **Exponents and prefixes.** Milli- (10⁻³), micro- (10⁻⁶), nano- (10⁻⁹), pico- (10⁻¹²), femto- (10⁻¹⁵), atto- (10⁻¹⁸). Shifting by three orders of magnitude is common in biology; single errors are catastrophic.
4. **Logarithmic vs linear differences.** A tenfold change in [H⁺] is a one-pH-unit change. "Twice the acidity" means $0.3$ pH unit down, not $2$ pH units.
5. **Error propagation.** Small errors in input variables compound through multi-step calculations. The textbook flags this at thermodynamics, kinetics, and evolutionary rate estimation in particular.

---

## C.7 Key Equations Quick Reference {.unnumbered}

\label{sec:appendix_math_review_key_equations}

These equations recur throughout the textbook. Each entry gives the equation, the variable definitions, and the chapter where it first appears.

### Michaelis-Menten equation {.unnumbered}

\begin{equation}
v = \frac{V_{\max} [S]}{K_m + [S]}
\label{eq:appendices_appendix_math_review_mm}
\end{equation}

- $v$ = reaction velocity (mol L$^{-1}$ s$^{-1}$); $V_{\max}$ = maximum velocity; $[S]$ = substrate concentration; $K_m$ = substrate concentration at half-maximal velocity.
- When $[S] = K_m$, $v = V_{\max}/2$. At $[S] \ll K_m$, $v \approx (V_{\max}/K_m)[S]$ (first-order). At $[S] \gg K_m$, $v \approx V_{\max}$ (zero-order).
- **Competitive inhibitor** raises apparent $K_m$ by factor $(1 + [I]/K_i)$; $V_{\max}$ unchanged.
- First appears in \cref{sec:unit_I_enzymes_and_kinetics}.

### Hill equation (cooperative binding) {.unnumbered}

\begin{equation}
\theta = \frac{[L]^n}{K_d^n + [L]^n}
\label{eq:appendices_appendix_math_review_hill}
\end{equation}

- $\theta$ = fractional saturation; $[L]$ = ligand concentration; $K_d$ = dissociation constant at half-maximal saturation; $n$ = Hill coefficient (cooperativity).
- $n = 1$: independent (Michaelis-Menten-like, hyperbolic). $n > 1$: positive cooperativity (sigmoidal, switch-like). $n < 1$: negative cooperativity.
- Haemoglobin: $n \approx 2.8$, $K_d \approx 26$ mmHg (P50). Phosphofructokinase-1: $n \approx 4$ for fructose-6-phosphate.
- **Switch sharpness:** fold-change in $\theta$ from $0.1K_d$ to $10K_d$ is $100^n$; for $n=1$ this is 100-fold; for $n=4$ it is $10^8$-fold — explaining why cooperative enzymes function as on/off switches.
- First appears in \cref{sec:unit_I_enzymes_and_kinetics}.

### Nernst equation {.unnumbered}

\begin{equation}
E_{ion} = \frac{RT}{zF} \ln\frac{[X]_o}{[X]_i}
\label{eq:appendices_appendix_math_review_nernst}
\end{equation}

- $E_{ion}$ = equilibrium (reversal) potential for the ion; $R = 8.314$ J mol$^{-1}$ K$^{-1}$; $T$ = temperature in K; $z$ = ion valence (charge); $F = 96485$ C mol$^{-1}$; $[X]_o / [X]_i$ = extracellular/intracellular concentration ratio.
- At 37°C: $RT/F \approx 26.7$ mV, so $E_{ion} \approx (26.7/z) \ln([X]_o/[X]_i)$ mV.
- For Na$^+$ ($z=+1$, $[Na]_o/[Na]_i \approx 145/12$): $E_{Na} \approx +67$ mV. For K$^+$ ($z=+1$, $[K]_o/[K]_i \approx 5/140$): $E_K \approx -90$ mV.
- First appears in \cref{sec:unit_IX_action_potential_synapses}.

### Goldman-Hodgkin-Katz equation {.unnumbered}

\begin{equation}
V_m = \frac{RT}{F} \ln \frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}
\label{eq:appendices_appendix_math_review_ghk}
\end{equation}

- Extends the Nernst equation when multiple ions contribute. $P_K$, $P_{Na}$, $P_{Cl}$ = membrane permeabilities. At rest: $P_K : P_{Na} : P_{Cl} \approx 1 : 0.04 : 0.45$, giving $V_m \approx -70$ mV.
- During action potential peak: $P_{Na}$ rises 500-fold, shifting $V_m$ toward $E_{Na}$.
- First appears in \cref{sec:unit_IX_action_potential_synapses}.

### Henderson-Hasselbalch equation {.unnumbered}

\begin{equation}
\text{pH} = \text{p}K_a + \log_{10} \frac{[\text{A}^-]}{[\text{HA}]}
\label{eq:appendices_appendix_math_review_hh}
\end{equation}

- $[A^-]$ = conjugate base concentration; $[HA]$ = weak acid concentration.
- At pH = p$K_a$: $[A^-]/[HA] = 1$ (half-dissociated). Bicarbonate buffer: p$K_a = 6.1$; at pH 7.4, $[HCO_3^-]/[CO_2] \approx 20$.
- Buffer capacity is greatest within ±1 pH unit of p$K_a$.
- First appears in \cref{sec:unit_I_atoms_molecules}.

### Water potential {.unnumbered}

\begin{equation}
\Psi = \Psi_s + \Psi_p
\label{eq:appendices_appendix_math_review_water_potential}
\end{equation}

- $\Psi$ = total water potential (MPa); $\Psi_s$ = solute (osmotic) potential ($\leq 0$); $\Psi_p$ = pressure potential (turgor; can be positive or negative).
- Water moves from high to low $\Psi$. Wilted cell: $\Psi_p \approx 0$, $\Psi = \Psi_s < 0$. Turgid cell: $\Psi_p > 0$ partially offsets $\Psi_s$.
- Xylem tension: $\Psi_p < 0$ (negative pressure) drives cohesion-tension in tall trees.
- First appears in \cref{sec:unit_VIII_plant_structure_and_water}.

---

## Further Reading and Source Notes {.unnumbered}

- Keener, J. & Sneyd, J. (2009). *Mathematical Physiology* (2nd ed.). Springer. — comprehensive biological math.
- Otto, S. P. & Day, T. (2007). *A Biologist's Guide to Mathematical Modeling in Ecology and Evolution*. Princeton. — accessible entry point.
- Strogatz, S. H. (2018). *Nonlinear Dynamics and Chaos* (2nd ed.). Westview. — the bifurcation and limit-cycle literature.

*Module: reference only (no code)*
