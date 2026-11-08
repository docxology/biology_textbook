# Lab — Action Potentials and Synaptic Transmission {#sec:lab_unit_IX_action_potential_synapses .unnumbered}

*This activity accompanies \cref{sec:unit_IX_action_potential_synapses}.*

## Learning Objectives {.unnumbered}

- Compute CAP conduction velocities.
- Compare empirical quantal statistics with specified models.
- Calculate GABA conductance currents and shunting.
- Evaluate replicated input-specific plasticity.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO4):** Compute CAP conduction velocities.
- **Outcome 2 (LO5):** Compare empirical quantal statistics with specified models.
- **Outcome 3 (LO6):** Calculate GABA conductance currents and shunting.
- **Outcome 4 (LO7):** Evaluate replicated input-specific plasticity.



: Alignment and evidence-specific scoring. {#tbl:unit_IX_action_potential_synapses_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | velocity/quantal/current/LTP computations |
| Controls | blank, paired pathway, AP5 and no-HFS controls |
| Uncertainty | release assumptions, threshold and three-slice limitations |
| Mechanism | driving force, conductance and NMDA-receptor plasticity mechanisms |
| Transfer | timing-specific experiment and evidence-limited safety argument |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All recordings below are synthetic. CAPs are population signals; release models have distinct assumptions.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: CAP and quantal packet. {#tbl:unit_IX_action_potential_synapses_alignment_and_rubric_map_2}
| Record | Data | Control |
| --- | --- | --- |
| Electrode separation | 30 mm | common stimulus/recording delay subtracted |
| Fast peak | 0.29/0.30/0.31 ms in independent preparations | saline blank lacks a peak |
| Intermediate | 2.9/3/3.1 ms | same geometry |
| Slow | 29/30/31 ms | same geometry |
| Histogram | quanta 0, 1, 2, 3, 4, 5; counts 8, 20, 30, 25, 12, 5 | 100 independent stimuli, stable detection |
| Sites | $n=15$ identical independent sites hypothesized; $q=0.5$ mV | linear summation assumed |


: GABA current inputs. {#tbl:unit_IX_action_potential_synapses_alignment_and_rubric_map_3}
| Condition | Conductance (nS) | Vm (mV) | ECl (mV) |
| --- | --- | --- | --- |
| Control | 10 | -60 | -70 |
| Benzodiazepine illustration | 15 | -60 | -70 |
| Barbiturate illustration | 20 | -60 | -70 |
| At reversal | 20 | -70 | -70 |
| Depolarized chloride gradient | 10 | -70 | -50 |


: LTP normalized fEPSP slopes. {#tbl:unit_IX_action_potential_synapses_packet_4}
| Group | Baseline at −10/−5 min | At 30 min, slices 1/2/3 | At 45 min | At 60 min |
| --- | --- | --- | --- | --- |
| HFS pathway | 100/100 | 145/150/155 | 143/148/153 | 140/145/150 |
| Unstimulated pathway, same slices | 100/100 | 99/100/101 | 100/101/99 | 100/99/101 |
| HFS plus AP5, independent slices | 100/100 | 99/100/101 | 98/100/102 | 99/100/101 |
| No HFS, independent slices | 100/100 | 100/101/99 | 99/100/101 | 98/100/102 |

Reference rules: speed = distance/latency. Larger myelinated fibers generally conduct faster than small unmyelinated fibers, but CAP speed alone does not identify a unique species-specific fiber class. For histogram value $k$ with count $n_k$, use mean $=\sum k n_k/100$ and population variance $=\sum k^2 n_k/100-\mathrm{mean}^2$. Poisson has mean $m$ and $P_0=\exp(-m)$; a homogeneous finite-binomial model has mean $15p$ and $P_0=(1-p)^{15}$. A Hebbian timing rule potentiates a specified input when presynaptic activity precedes postsynaptic firing; an anti-Hebbian rule reverses that sign under the same timing protocol. Flumazenil antagonizes benzodiazepine-site effects but can precipitate seizures in dependence or certain mixed/cyclic-antidepressant overdoses; absence of co-ingestion and dependence evidence does not establish universal rescue safety. No dose or administration follows from this card.

## Paper-Based Investigation {.unnumbered}

1. Compute speeds at mean latencies and means of individual speeds; explain their difference. Relate peaks to fiber classes with species/diameter qualifications.
2. Calculate histogram mean, population variance and failure fraction. Compare the empirical mean with Poisson $m=-\ln P_0$. For 15 sites, report empirical $p=\mathrm{mean}/15$ and the Poisson-based approximation $p=m/15$; contrast these with exact binomial $p=1-P_0^{1/15}$. Evaluate heterogeneity, detection and independence alternatives rather than declaring a best model from one mismatch.
3. Calculate outward-positive $I=g(V_m-E_{Cl})$ in pA. Explain zero current versus nonzero conductance and shunting. Effective conductance values are illustrative, not drug doses or unique kinetic signatures.
4. Calculate the 60-min LTP mean and sample SD. Compare the paired unstimulated pathway, AP5 and no-HFS controls. Design a pre/post timing-order test distinguishing Hebbian from anti-Hebbian plasticity; acute LTD is not chronic homeostatic scaling.
5. Evaluate a proposed universal flumazenil rescue in mixed overdose: identify dependence/co-ingestion evidence and seizure risk. No dosing or administration.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sample SD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

For n=10 and q=.5 mV, EPSP≥6 mV is impossible because the finite maximum is 5 mV. Check this before any Poisson or Gaussian approximation.

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

Speeds at mean latencies are 100, 10 and 1 m/s. Mean quantal count is 2.28, $E[k^2]=6.82$ and population variance is 1.6216 (sample variance approximately 1.6380). $P_0=0.08$ gives Poisson $m=2.52573$ and $p=m/15=0.168382$, versus empirical $p=0.152$. Currents are 100, 150, 200, 0 and −200 pA. Reversal removes driving force, not conductance. The HFS 60-min mean is 145%, with sample SD 5 percentage points; other means are 100%. A slice is the independent replicate; pathways within it are paired. Poisson requires small independent release probabilities; a finite-binomial model at larger $p$ has a finite bound and variance $np(1-p)$. Flumazenil can precipitate seizures with benzodiazepine dependence or certain mixed/cyclic-antidepressant overdoses; clinical indication and label warnings matter \citep{fda2025flumazenil}.

Means of the three individual speeds are approximately 100.0742, 10.00742, 1.000742 m/s, slightly above speeds at mean latency because inversion is nonlinear. The failure-based exact binomial p=1−.08^(1/15) is distinct from the Poisson approximation. At empirical p=.152, the homogeneous-binomial variance 15p(1−p)=1.93344 exceeds the observed 1.6216; this discrepancy alone does not select a unique explanation. HFS raises the 60 min slope by 45 percentage points above 100% baseline; AP5 blocks that effect in this synthetic comparison but does not prove every form of plasticity requires NMDARs.

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
