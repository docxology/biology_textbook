# Lab — Nervous System and Neural Signaling {#sec:lab_unit_IX_nervous_system .unnumbered}

*This activity accompanies \cref{sec:unit_IX_nervous_system}.*

## Learning Objectives {.unnumbered}

- Predict passive spread using dimensionally specified cable parameters.
- Relate reflex evidence to circuit organization.
- Separate sensory discrimination from response bias.
- Identify AP phases/refractory recovery and calculate a K+ permeability-induced resting-potential shift.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO4):** Predict passive spread using dimensionally specified cable parameters.
- **Outcome 2 (LO1):** Relate reflex evidence to circuit organization.
- **Outcome 3 (LO7):** Separate sensory discrimination from response bias.
- **Outcome 4 (LO9):** Predict and calculate a resting-potential shift after a specified K+ permeability change.



: Alignment and evidence-specific scoring. {#tbl:unit_IX_nervous_system_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | latency, sensory/cable and GHK calculations with labeled AP phases |
| Controls | catch/randomizedsensory andpairedpulse comparisons |
| Uncertainty | spacing intervals,repeatedwithinperson andtemperature confounding |
| Mechanism | reflex/passivecable/regenerativeAP distinctions |
| Transfer | Tinbergen andBCI evidence boundaries without clinicalclaims |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All neural values are synthetic. Tables replace missing traces/body maps/videos; no contact testing or stimulation is required.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: Reflex and two-point cards. {#tbl:unit_IX_nervous_system_alignment_and_rubric_map_2}
| Card | Values | Interpretation |
| --- | --- | --- |
| Patellarbaseline | latency24/25/23ms;magnitude2/2/2units | three taps in one person |
| Reinforcement | 24/24/25ms;3/4/3units | excitability versus velocity |
| Peripheralneuropathy | 35/37/36ms;1/0/1units | afferent/efferent alternatives |
| Uppermotorlesion | 24/25/24ms;4/4/5units | descending control |
| Fingertip | spacings1,2,5,10,20,40mm;correct2,8,10,10,10,10of10 | threshold first≥8/10 |
| Palm | same spacings;1,3,6,9,10,10 correct | same rule |
| Forearm | 1,2,3,5,8,10 correct | same rule |
| Back | 1,1,2,3,5,8 correct | same rule |
| Onepointcatch | false-two reports1/10eachlocation | responsebias |


: Voltage and paired-pulse records. {#tbl:unit_IX_nervous_system_alignment_and_rubric_map_3}
| Time(ms) | Vm(mV) | Secondpulsedelay(ms) | SecondAP/10 |
| --- | --- | --- | --- |
| 0 | -70 | 0.5 | 0 |
| 0.5 | -70 | 1 | 0 |
| 1 | -55 | 2 | 3 |
| 1.2 | 0 | 3 | 7 |
| 1.5 | 30 | 5 | 10 |
| 2 | 0 | 10 | 10 |
| 3 | -80 | — | — |
| 5 | -72 | — | — |
| 8 | -70 | — | — |


: Cable and localization inputs. {#tbl:unit_IX_nervous_system_alignment_and_rubric_map_4}
| Case | rm(Ωcm) | ri(Ω/cm) | Other |
| --- | --- | --- | --- |
| Unmyelinated | 10000 | 80000000 | x=.1cm |
| Myelinatedinternode | 800000 | 4000000 | λ=sqrt(rm/ri) |
| Medianproximal | — | — | wrist-elbow.2m;latencydifference2ms |
| Distal | — | — | motorlatency4ms;reference3.5ms;temperatureunknown |


: Tinbergen and BCI cards. {#tbl:unit_IX_nervous_system_packet_5}
| Card | Printed evidence | Boundary |
| --- | --- | --- |
| Mechanism | touch→afferent→spinalmotorresponse | proximate |
| Ontogeny | practice changes reaching overweeks | development |
| Function | escape speed predicts survival in specified habitat | adaptivehypothesis |
| Phylogeny | related taxa differ in courtshipsequences | comparativehistory |
| Willett2023 | intracorticalarrays decoded attemptedspeech in oneparticipant;chaptercitation | not scalpEEG |
| Metzger2023 | surfaceECoG decoded attemptedspeech/avatar;chaptercitation | differentimplant;not EEGrobotcontrol |

For the permeability task use the stipulated thermal voltage 26.7 mV (approximately 310 K) and $V_m=26.7\ln\!\left(\frac{P_K[K^+]_o+P_{\mathrm{Na}}[Na^+]_o+P_{\mathrm{Cl}}[Cl^-]_i}{P_K[K^+]_i+P_{\mathrm{Na}}[Na^+]_i+P_{\mathrm{Cl}}[Cl^-]_o}\right)$ in mV. Concentrations (mM): K inside 140/outside 5, Na 15/145, Cl 10/120. Set $P_{\mathrm{Na}}=0.04$ and $P_{\mathrm{Cl}}=0.45$; compare $P_K=1$ with 2. Relative permeabilities are dimensionless; retain the printed rounded thermal factor for the paper calculation.

Circuit/reference card: patellar tendon stretch excites a quadriceps spindle afferent, which excites the spinal quadriceps motor neuron and an inhibitory interneuron suppressing antagonist motor neurons. Descending inputs can alter circuit excitability without changing axonal speed. For a passive cable use V(x)/V(0)=exp(−x/λ); velocity from two recording sites is distance divided by latency difference. The paired-pulse stimulus strength is not supplied, so report absent/partial/full responses under the recorded test condition, not a universal absolute or relative refractory duration. A threshold bracket means the prior tested spacing was below criterion and the first qualifying spacing met it; it is not a continuous psychometric fit.

## Paper-Based Investigation {.unnumbered}

1. Draw patellar afferent/motor connections and antagonist inhibitory interneuron. Compare mean latency/magnitude; why does reinforcement not prove faster axonal conduction?
2. Draw four labeled skin regions and determine thresholds. Include catch-trial rates and intervals bounded by tested spacings. Design randomized order, blinding, equal force and independent-participant controls.
3. Mark voltage threshold, peak, undershoot and recovery. Use the paired-pulse record, not the single waveform, for absent/partial/recovered excitability. State stimulus dependence. Separately calculate the supplied GHK potential before/after doubling PK; predict its direction toward EK before doing arithmetic.
4. Calculate λ and e^(−.1/λ), converting cm→mm. Explain passive spread versus nodal speed. Calculate wrist-elbow velocity and list distal sensory, temperature and reference data needed before localizing carpal-tunnel compression.
5. Match four behavior cards to Tinbergen questions. Contrast actual BCI technologies and propose a later-time holdout with majority baseline and shifted-label control, without treating adjacent rows as independent patients.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sampleSD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

For an optional worked time-holdout example, see the sixteen identified UCI eye-state rows in \cref{sec:unit_IX_action_potential_synapses}, not the accompanying nervous-system chapter. Core Task 5 uses the printed BCI cards to propose a design; no external EEG classification is required. Neither activity establishes clinical decoder performance or online control.

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

Mean latencies: 24, 24.333, 36, 24.333 ms. Sensory thresholds: 2, 10, 20, 40 mm, bounded by prior tested spacing; false-two rate .1. AP peak 30 mV, undershoot −80; delays .5/1 ms fail, 2/3 partially recover, 5/10 recover under this stimulus. Unmyelinated λ=.0111803 cm=.111803 mm, ratio≈.00013048; myelinated λ=.447214 cm=4.47214 mm, ratio≈.79963. Velocity 100 m/s is for the proximal segment and does not alone diagnose distal compression. Slightly long distal latency lacks temperature/quality context. The GHK numerator/denominator are 15.3/194.6 then 20.3/334.6; with 26.7 mV, Vm changes approximately −67.9→−74.8 mV, a hyperpolarizing shift of about −6.9 mV toward EK. Permeability change is not itself an AP phase. BCI studies demonstrate implant/participant-specific capabilities, not general scalp EEG control.

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
