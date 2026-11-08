# Appendix C — Mathematical Review for Biology {#sec:appendix_math_review .unnumbered}



<!-- chapter-metadata-badge -->
> **\nameref{sec:appendix_math_review}** · Level 1/3 · 45 min read · Prerequisites: none · Use as reference

This appendix collects the mathematics a reader needs to work through the quantitative chapters of this textbook. It is not a course in mathematics — it is a compact reference for the specific tools used in the chapters. Each section is self-contained; dip in as needed.

---

## C.1 Logarithms and the Natural Log {.unnumbered}

### Definition {.unnumbered}

\begin{equation}
\log_b(x) = y \iff b^y = x
\label{eq:appendices_appendix_math_review_item_1}
\end{equation}


For real logarithms, the argument is positive and the base is positive and not 1. Biology uses two bases heavily:

- **Base 10** ($\log_{10}$) — pH, sound intensity, earthquake magnitude, powers-of-ten units (nM, μM, mM).
- **Base $e$** ($\ln$, natural log) — most first-order kinetics (exponential growth, decay, enzyme kinetics), where $e \approx 2.71828$.

Conversion: $\log_{10}(x) = \ln(x) / \ln(10) \approx \ln(x) / 2.303$.

### Key identities {.unnumbered}

| Identity | Biological application |
| -------- | ---------------------- |
| $\log(ab) = \log a + \log b$ | Converting probability products into sums; use conditional factors for dependent events |
| $\log(a/b) = \log a - \log b$ | Henderson-Hasselbalch $\text{pH} = \text{p}K_a + \log([\text{A}^-]/[\text{HA}])$ |
| $\log(a^n) = n \log a$ | Hill equation — slope of log odds versus log ligand concentration |
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


In population ecology, $dN/dt>0$ means growth and $dN/dt<0$ means decline. A zero derivative means no instantaneous change; an equilibrium additionally requires the state to remain stationary under the model dynamics. In enzyme kinetics, $d[P]/dt$ is product-formation velocity.

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


For $r>0$, $K>0$, and $0<N_0<K/2$, the growing trajectory passes through an inflection at $N=K/2$, where $dN/dt=rK/4$ is maximal. Starting above $K/2$ gives no later accelerating phase; starting above $K$ gives decline toward $K$. The formula is analytic, whereas `biology.ecology.ecology.logistic_growth` uses forward Euler steps and requires an adequate time grid.

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

For independent events occurring at a constant rate, let λ be the expected count in the specified interval:

\begin{equation}
P(k) = \frac{\lambda^k e^{-\lambda}}{k!}
\label{eq:appendices_appendix_math_review_item_11}
\end{equation}


Used for spontaneous mutation counts per locus, bacterial cell counts in Petri dishes (when plates are not overgrown), rare-disease incidence.

---

## C.4 Dimensional Analysis {.unnumbered}

Every physical quantity carries **units**. Units must balance on both sides of every equation — if they don't, the equation is wrong.

### Example — diffusion distance {.unnumbered}

For unbounded one-dimensional diffusion with constant diffusion coefficient $D$ and no drift, the root-mean-square displacement is:

\begin{equation}
x_{\mathrm{rms}} = \sqrt{\langle(\Delta x)^2\rangle} = \sqrt{2Dt}
\label{eq:appendices_appendix_math_review_item_12}
\end{equation}


Check units: $D$ has units of m² s⁻¹; $t$ has units of s; so $\sqrt{2Dt}$ has units of $\sqrt{\text{m}^2} = \text{m}$. ✓

The signed mean displacement is zero under these assumptions. In $d$ independent spatial dimensions, the radial mean-square displacement is $\langle r^2\rangle=2dDt$; the one-dimensional expression is not a general mean travel distance or Fick's flux law.

If a student wrote $x = Dt$, units would be m² s⁻¹ · s = m² — dimensionally wrong.

### Standard SI units used in this book {.unnumbered}

| Quantity | Symbol | SI unit | Typical biological magnitude |
| -------- | ------ | ------- | --------------------------- |
| Length | $l$ | m | cell: 10 μm; neuron: 1 m |
| Mass | $m$ | kg | ribosome: 3 × 10⁻²¹ kg; cell: 10⁻¹² kg |
| Time | $t$ | s | AP: 1 ms; cell cycle: 24 h |
| Amount | $n$ | mol | ATP in a cell: 10⁻¹⁵ mol |
| Concentration | $[X]$ | mol m⁻³ (SI); mol L⁻¹ = M | 1 M = 1000 mol m⁻³; an illustrative ATP concentration is 5 mM |
| Energy | $E$ | J | Standard ATP-hydrolysis free-energy change: approximately −5 × 10⁻²⁰ J per molecule, or −30.5 kJ mol⁻¹ |
| Force | $F$ | N | myosin step force: 5 × 10⁻¹² N = 5 pN |
| Electric potential | $V$ | V | resting membrane: −0.07 V = −70 mV |

### Non-SI units common in biology {.unnumbered}

| Unit | SI equivalent | Use |
| ---- | ------------- | --- |
| mmHg (Torr) | 133.322 Pa | blood pressure, gas partial pressures |
| cal | 4.184 J | nutrition ("Calorie" = kcal) |
| pH | $-\log_{10} a_{\mathrm{H}^+}$ | dimensionless hydrogen-ion activity; dilute-solution approximation: $a_{\mathrm{H}^+}\approx[\mathrm{H}^+]/(1\ \mathrm{mol\ L}^{-1})$ |
| Da (dalton) | 1.661 × 10⁻²⁷ kg | molecular mass |
| Celsius temperature | $T/\mathrm{K}=t/{}^\circ\mathrm{C}+273.15$ | thermodynamic formulas use absolute temperature in K |

---

## C.5 Linear Algebra Miniature {.unnumbered}

Primarily trace knowledge is required for this book, but the two ideas below recur.

### Matrices as transitions {.unnumbered}

Allele-frequency change under migration between two populations is a 2 × 2 matrix multiplication. Markov transition matrices describe stochastic gene expression (lac operon), state transitions in ion channels, and Wright-Fisher drift.

### Eigenvalues and equilibrium {.unnumbered}

For a fixed, nonnegative, primitive Leslie matrix, the dominant eigenvalue $\lambda_1$ gives the asymptotic finite population multiplier per projection interval. Its positive right eigenvector, normalized to sum to one, gives the stable age distribution. Transient growth depends on initial age structure; changing vital rates or nonprimitive matrices require separate analysis. This is the formal underpinning of \cref{sec:unit_X_population_ecology}'s demographic analysis.

---

## C.6 Common Pitfalls in Biological Math {.unnumbered}

1. **Confusing concentration and amount.** 1 nM is a concentration; 1 nmol is an amount. A picomole of hormone in 5 L of blood is 0.2 pM.
2. **Units of rate constants.** First-order: s⁻¹. Second-order: M⁻¹ s⁻¹. Third-order: M⁻² s⁻¹. Dimensional analysis typically exposes an order-of-magnitude error.
3. **Exponents and prefixes.** Milli- (10⁻³), micro- (10⁻⁶), nano- (10⁻⁹), pico- (10⁻¹²), femto- (10⁻¹⁵), atto- (10⁻¹⁸). Shifting by three orders of magnitude is common in biology; single errors are catastrophic.
4. **Logarithmic versus linear differences.** A one-unit pH decrease is a tenfold hydrogen-ion activity increase; it gives the same concentration ratio if the activity coefficient is unchanged. Doubling activity lowers pH by $\log_{10}2\approx0.301$, not two units, and does not imply doubled total acid content or titrant \citep{buck2002phdefinition}.
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
- The simple reversible competitive-inhibition model describes a kinetic pattern; that pattern alone does not locate the inhibitor's physical binding site. `biology.biochemistry.michaelis_menten` and `competitive_inhibition` use μM for concentrations and μmol min⁻¹ for rates; do not mix those numerical inputs with mol L⁻¹ s⁻¹ without conversion.
- First appears in \cref{sec:unit_I_enzymes_and_kinetics}.

### Hill equation (phenomenological binding or response) {.unnumbered}

\begin{equation}
\theta = \frac{[L]^n}{K_d^n + [L]^n}
\label{eq:appendices_appendix_math_review_hill}
\end{equation}

- $\theta$ = fractional saturation; $[L]$ = ligand concentration; $K_d$ here denotes an effective half-saturation concentration; $n$ is the phenomenological Hill slope, not necessarily a microscopic binding-site count.
- $n=1$ gives a hyperbola; $n>1$ gives a steeper response; $n<1$ gives a shallower response. A fitted slope alone does not establish a unique molecular mechanism.
- The illustrative hemoglobin model uses $n=2.7$ and $P_{50}=26$ mmHg, matching the default `oxygen_saturation` inputs. These are selected model parameters, not a new fit to patient data.
- **Switch sharpness:** $\theta(10K_d)/\theta(0.1K_d)=10^n$: 10-fold for $n=1$ and $10^4$-fold for $n=4$. The **odds** $\theta/(1-\theta)$ change by $100^n$ over that interval; confusing odds with fractional occupancy produces the larger, incorrect saturation ratio.
- First appears in \cref{sec:unit_I_enzymes_and_kinetics}.

### Nernst equation {.unnumbered}

\begin{equation}
E_{ion} = \frac{RT}{zF} \ln\frac{[X]_o}{[X]_i}
\label{eq:appendices_appendix_math_review_nernst}
\end{equation}

- $E_{ion}$ = equilibrium potential for the ion; $R=8.314$ J mol$^{-1}$ K$^{-1}$; $T$ is absolute temperature in K; $z$ is ion valence; $F=96485$ C mol$^{-1}$. The displayed concentration ratio approximates an activity ratio; reversal of a mixed-ion channel need not equal any single-ion Nernst potential.
- At 37°C: $RT/F \approx 26.7$ mV, so $E_{ion} \approx (26.7/z) \ln([X]_o/[X]_i)$ mV.
- For Na$^+$ ($z=+1$, $[Na]_o/[Na]_i = 145/12$): $E_{Na} \approx +66.6$ mV. For K$^+$ ($z=+1$, $[K]_o/[K]_i = 5/140$): $E_K \approx -89.0$ mV. These are selected concentrations, not universal cellular values; `biology.cell.nernst_potential` returns mV and defaults to 310 K.
- Developed in \cref{sec:unit_II_membrane_transport} and applied to excitability in \cref{sec:unit_IX_action_potential_synapses}.

### Goldman-Hodgkin-Katz equation {.unnumbered}

\begin{equation}
V_m = \frac{RT}{F} \ln \frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}
\label{eq:appendices_appendix_math_review_ghk}
\end{equation}

- This constant-field, zero-net-current voltage equation applies to the specified monovalent ions, not arbitrary mixtures containing divalent calcium. $P_K$, $P_{Na}$, and $P_{Cl}$ are relative permeabilities.
- With $P_K:P_{Na}:P_{Cl}=1:0.04:0.45$ and inside/outside concentrations K$^+$ 140/5, Na$^+$ 12/145, and Cl$^-$ 4/110 mM at 310 K, the ratio is $12.6/189.98$ and $V_m\approx-72.5$ mV when rounded only at the end. These stipulated reference inputs match the worked example and `biology.cell.goldman_equation`; changing permeability changes this model prediction, not a universal action-potential peak.
- Developed in \cref{sec:unit_II_membrane_transport} and applied in \cref{sec:unit_IX_action_potential_synapses}.

### Henderson-Hasselbalch equation {.unnumbered}

\begin{equation}
\text{pH} = \text{p}K_a + \log_{10} \frac{[\text{A}^-]}{[\text{HA}]}
\label{eq:appendices_appendix_math_review_hh}
\end{equation}

- Concentration ratios require ideal dilute behavior or an apparent pKa appropriate to the specified medium; thermodynamic ratios use activities.
- In that approximation pH=pKa gives equal conjugate concentrations. For the stipulated lumped CO$_2$/bicarbonate system, apparent pKa=6.1 and pH 7.4 give a ratio near 20; 6.1 is not the dissociation pKa of intact H$_2$CO$_3$.
- A simple closed buffer's pair contribution is maximal near pKa at fixed total concentration and varies continuously with pH. Open CO$_2$ exchange imposes a different capacity constraint; ±1 is not an on/off boundary.
- First appears in \cref{sec:unit_I_atoms_molecules}.

### Water potential {.unnumbered}

\begin{equation}
\Psi = \Psi_s + \Psi_p
\label{eq:appendices_appendix_math_review_water_potential}
\end{equation}

- $\Psi$ = water potential (MPa); $\Psi_s$ = solute potential ($\leq0$); $\Psi_p$ = pressure potential. This two-component approximation neglects gravitational and matric contributions. `biology.botany.water_potential` uses ideal non-electrolyte $\Psi_s=-CRT$, accepts concentration in M and pressure in MPa, and returns MPa.
- Across a water-permeable path, water moves down the total water-potential gradient; pressure can oppose the solute contribution. In a stipulated wilted-cell case with $\Psi_p\approx0$, $\Psi\approx\Psi_s<0$. Turgor can partially offset $\Psi_s$.
- Xylem tension: $\Psi_p < 0$ (negative pressure) drives cohesion-tension in tall trees.
- First appears in \cref{sec:unit_VIII_plant_structure_and_water}.

---

## Further Reading and Source Notes {.unnumbered}

- Keener, J. & Sneyd, J. (2009). *Mathematical Physiology* (2nd ed.). Springer. — comprehensive biological math.
- Otto, S. P. & Day, T. (2007). *A Biologist's Guide to Mathematical Modeling in Ecology and Evolution*. Princeton. — accessible entry point.
- Strogatz, S. H. (2018). *Nonlinear Dynamics and Chaos* (2nd ed.). Westview. — the bifurcation and limit-cycle literature.

*Module: reference only (no code)*
