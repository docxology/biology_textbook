<!-- render:skip-beamer -->

# Appendix C — Mathematical Review for Biology {.unnumbered}

\label{sec:appendix_math_review}


<!-- chapter-metadata-badge -->
> **Appendix C** · Level 1/3 · 45 min read · Prerequisites: none · Use as reference

This appendix collects the mathematics a reader needs to work through the quantitative chapters of this textbook. It is not a course in mathematics — it is a compact reference for the specific tools used in the chapters. Each section is self-contained; dip in as needed.

---

## C.1 Logarithms and the Natural Log {.unnumbered}

### Definition {.unnumbered}

$$ \log_b(x) = y \iff b^y = x  \label{eq:appendices_appendix_math_review_item_1}$$


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

$$ N(t) = N_0 e^{rt} = 2 N_0 \implies e^{rt} = 2 \implies t = \frac{\ln 2}{r} = \frac{0.693}{0.5} \approx 1.39 \text{ h}  \label{eq:appendices_appendix_math_review_item_2}$$


The **"ln 2 trick"** recurs throughout biology: half-life $t_{1/2} = \ln 2 / k$ (decay); doubling time $t_d = \ln 2 / r$ (growth). Memorise $\ln 2 \approx 0.693$.

---

## C.2 Differential and Integral Calculus {.unnumbered}

Biology rarely requires advanced calculus, but the reader must be comfortable with:

### Derivatives as rates {.unnumbered}

$$ \frac{dN}{dt} = \text{rate of change of } N \text{ over time}  \label{eq:appendices_appendix_math_review_item_3}$$


In population ecology, $dN/dt > 0$ means the population is growing; $dN/dt = 0$ is equilibrium; $dN/dt < 0$ is decline. In enzyme kinetics, $d[P]/dt$ = reaction velocity $v$.

### Integration as accumulation {.unnumbered}

$$ \int_0^T \frac{dN}{dt} dt = N(T) - N(0)  \label{eq:appendices_appendix_math_review_item_4}$$


The integral sums up infinitesimal contributions. Examples:

- Total drug dose delivered by an infusion: $\text{Dose} = \int_0^T (\text{infusion rate}) dt$.
- Net photosynthesis over a day: $\int_0^{24\text{h}} P(t) dt$.

### First-order ODE: exponential growth and decay {.unnumbered}

$$ \frac{dN}{dt} = kN \implies N(t) = N_0 e^{kt}  \label{eq:appendices_appendix_math_review_item_5}$$


- $k > 0$: growth with doubling time $t_d = \ln 2 / k$.
- $k < 0$: decay with half-life $t_{1/2} = \ln 2 / |k|$.

### Logistic growth (nonlinear) {.unnumbered}

$$ \frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)  \label{eq:appendices_appendix_math_review_item_6}$$


The closed-form solution is:

$$ N(t) = \frac{K}{1 + \left(\frac{K-N_0}{N_0}\right) e^{-rt}}  \label{eq:appendices_appendix_math_review_item_7}$$


Inflection (maximum rate) at $N = K/2$, giving the sigmoid shape.

---

## C.3 Basic Probability {.unnumbered}

### Independent events {.unnumbered}

$P(A \cap B) = P(A) \cdot P(B)$ when events are independent. Example: the probability that both parents transmit the recessive allele at a locus ($Aa \times Aa$) is $(1/2)(1/2) = 1/4$.

### Conditional probability and Bayes' theorem {.unnumbered}

$$ P(A \mid B) = \frac{P(A \cap B)}{P(B)}  \label{eq:appendices_appendix_math_review_item_8}$$


Bayes' theorem — central to \cref{sec:unit_0_active_inference} and to medical testing:

$$ P(\text{disease} \mid +) = \frac{P(+ \mid \text{disease}) \cdot P(\text{disease})}{P(+)}  \label{eq:appendices_appendix_math_review_item_9}$$


A highly sensitive test can still have a low positive predictive value if the disease is rare — a counterintuitive result with major clinical consequences.

### Binomial distribution {.unnumbered}

Number of successes in $n$ independent trials, each with probability $p$:

$$ P(k \text{ successes}) = \binom{n}{k} p^k (1-p)^{n-k}  \label{eq:appendices_appendix_math_review_item_10}$$


Used for Punnett-square ratios, mark-recapture statistics, and Hardy-Weinberg proportion testing.

### Poisson distribution {.unnumbered}

For rare events at mean rate λ per interval:

$$ P(k) = \frac{\lambda^k e^{-\lambda}}{k!}  \label{eq:appendices_appendix_math_review_item_11}$$


Used for spontaneous mutation counts per locus, bacterial cell counts in Petri dishes (when plates are not overgrown), rare-disease incidence.

---

## C.4 Dimensional Analysis {.unnumbered}

Every physical quantity carries **units**. Units must balance on both sides of every equation — if they don't, the equation is wrong.

### Example — diffusion distance {.unnumbered}

Fick's rule for mean diffusion distance:

$$ x = \sqrt{2Dt}  \label{eq:appendices_appendix_math_review_item_12}$$


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

## Further Reading and Source Notes {.unnumbered}

- Keener, J. & Sneyd, J. (2009). *Mathematical Physiology* (2nd ed.). Springer. — comprehensive biological math.
- Otto, S. P. & Day, T. (2007). *A Biologist's Guide to Mathematical Modeling in Ecology and Evolution*. Princeton. — accessible entry point.
- Strogatz, S. H. (2018). *Nonlinear Dynamics and Chaos* (2nd ed.). Westview. — the bifurcation and limit-cycle literature.

*Module: reference only (no code)*
