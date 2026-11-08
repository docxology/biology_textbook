# Lab — Endocrine Signaling and Homeostasis {#sec:lab_unit_IX_endocrine_signaling .unnumbered}

*This activity accompanies \cref{sec:unit_IX_endocrine_signaling}.*

## Learning Objectives {.unnumbered}

- Trace HPT feedback and primary-versus-central patterns.
- Interpret paired hormone panels without overdiagnosis.
- Quantify insulin-sensitive uptake with explicit normalization.
- Explain reproductive feedback from supplied life-stage cards.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO3):** Trace HPT feedback and primary-versus-central patterns.
- **Outcome 2 (LO3):** Interpret paired hormone panels without overdiagnosis.
- **Outcome 3 (LO4):** Quantify insulin-sensitive uptake with explicit normalization.
- **Outcome 4 (LO3):** Explain reproductive feedback from supplied life-stage cards.



: Alignment and evidence-specific scoring. {#tbl:unit_IX_endocrine_signaling_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | paneldirections,uptake,clearance andTSH arithmetic |
| Controls | pairedaxes,vehicle/timezero andmatchedmetabolicconditions |
| Uncertainty | toyinterval,one-cortisol andconstant-rate limitations |
| Mechanism | HPT/insulin/reproductive receptorfeedback mechanisms |
| Transfer | cautious endocrine report with discriminating follow-up |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All panels, uptake values and people are synthetic. Toy intervals apply only here; real diagnosis needs clinical context and validated methods. This endocrine-only lab does not import TLR/cytokine exercises.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: Hormone panels. {#tbl:unit_IX_endocrine_signaling_source_governance_checkpoint}
| Person | TSH(mIU/L) | FreeT4(pmol/L) | Fastingglucose(mmol/L) | Morningcortisol(nmol/L) |
| --- | --- | --- | --- | --- |
| Toyinterval | .4–4 | 10–22 | 3.9–5.5 | 140–690 |
| A | 12 | 6 | 4.8 | 400 |
| B | 0.05 | 32 | 5 | 420 |
| C | 2 | 7 | 4.9 | 380 |
| D | 1.5 | 16 | 9 | 720 |


: Insulin and clearance inputs. {#tbl:unit_IX_endocrine_signaling_packet_3}
| Record | Time0/15/30/60min | Assumption |
| --- | --- | --- |
| Controlglucose | 8/8.2/8.1/8mmol/L | matched meal/vehicle arm |
| Insulinglucose | 8/7/6/5mmol/L | same timing |
| Vehicleuptake | 2/2/2/2mgkg−1min−1 | whole-body-normalized toy value |
| Insulinuptake | 2/8/8/8mgkg−1min−1 | not liver-specific |
| Clearance | 80mIU/Lat0;half-life5min | no production/distribution change |
| HPTmodel | TSH∝freeT4^−2;baselineTSH2,T410;newT44 | dimensionless-ratio prediction |


: HPT diagram edges. {#tbl:unit_IX_endocrine_signaling_packet_4}
| Connection | Sign | Location |
| --- | --- | --- |
| TRH→TSH | + | hypothalamus→pituitary |
| TSH→T4/T3 | + | pituitary→thyroid |
| T4/T3→TRHandTSH | − | feedback |
| Pituitarylesion→TSHresponse | reduced | normal-range TSH can be inappropriately low |


: Reproductive endocrine cards. {#tbl:unit_IX_endocrine_signaling_packet_5}
| Stage | Given relationship | Task |
| --- | --- | --- |
| Puberty | pulsatileGnRH→LH/FSH | target and timing |
| Follicular | estradiol usually givesnegativefeedback | follicle growth |
| Sustainedhighestradiol | positive-feedback LH surge | ovulation |
| Earlypregnancy | hCG maintains corpus luteum | progesterone |
| Lactation | suckling→prolactin/oxytocin; GnRH suppression possible | production versus ejection |
| Infertility | low estradiol/high FSH versus low estradiol/low FSH | gonadal versus central |

Target/mechanism reference: insulin binding activates its receptor tyrosine-kinase pathway and promotes GLUT4 translocation in responsive skeletal muscle/adipose cells; not all glucose uptake is GLUT4-mediated. GnRH acts on pituitary gonadotrophs; LH/FSH act on gonadal target cells supporting steroid production and gamete development. Gonadal steroids feed back to hypothalamus/pituitary, with sustained high estradiol producing the stipulated positive-feedback phase. hCG acts at luteal LH receptors to maintain progesterone output. Prolactin acts on mammary secretory cells for milk production; oxytocin acts on myoepithelial cells for ejection. Low estradiol removes negative feedback, so high FSH favors a gonadal problem, whereas low FSH suggests deficient central drive; receptor responsiveness and clinical context remain unmeasured. For clearance use C(t)=C0×2^(−t/half-life), not a linear subtraction.

## Paper-Based Investigation {.unnumbered}

1. Annotate all HPT arrows and classify A/B/C feedback patterns. For B, distinguish thyrotoxicosis (excess circulating thyroid hormone) from proven thyroid overproduction: what etiological evidence is missing? Why is normal-range TSH not reassuring with low T4? For D propose repeat glucose assessment and explain why one morning cortisol cannot diagnose Cushing syndrome.
2. Plot glucose/uptake arms. Calculate uptake at 8 mg kg−1 min−1 for 70 kg over 30 min and the fraction of 75 g glucose, assuming constant rate. Trace insulin-receptor/GLUT4 signaling; blood disappearance is not identical to total uptake.
3. Compute clearance-only concentrations at 5 and 15 min and the HPT algebraic prediction for a 10→4 free-T4 change. Distinguish an illustrative sensitivity model from a patient forecast.
4. Draw a receptor-bearing target and feedback relationship for every reproductive card. Separate secretion defects, receptor resistance and central deficiency; distinguish prolactin from oxytocin.
5. Write an endocrine interpretation of one panel with evidence, alternative cause, confirmatory measurement and no treatment recommendation.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sampleSD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

Degludec half-life≈25h and duration≥42h are different label-defined quantities;plasma decline alone is not an effect profile.\cite{fda2026degludec}

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

A is consistent with primary hypothyroidism; B shows thyrotoxicosis with suppressed TSH (0.05 mIU/L) and high free T4 (32 pmol/L) relative to the supplied toy intervals, with source unresolved; C suggests possible central deficiency with inappropriately normal TSH. B could reflect increased synthesis, destructive thyroiditis releasing stored hormone, or exogenous hormone; the panel alone does not discriminate them. Clinical/medication history, appropriately selected antibodies and uptake evidence can distinguish causes; no treatment follows from this synthetic panel. Destructive thyroiditis illustrates excess circulating hormone without an overactive gland \citep{atathyroiditis}. D requires validated repeat glucose assessment; one cortisol value is nonspecific. Uptake=8×70×30=16800 mg=16.8 g=22.4% of 75 g. Clearance: 80→40 mIU/L at 5 min→10 at 15 min. A free-T4 ratio .4 gives TSH ratio 6.25 and new TSH 12.5 mIU/L, not 20. This model does not predict an individual’s response time. Reproductive feedback is phase-dependent and requires responsive target receptors.

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
