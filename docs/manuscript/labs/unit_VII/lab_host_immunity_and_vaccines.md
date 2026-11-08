# Lab — Host Immunity and Vaccines {#sec:lab_unit_VII_host_immunity_and_vaccines .unnumbered}

*This activity accompanies \cref{sec:unit_VII_host_immunity_and_vaccines}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO8):** Plot the complete outbreak curve and compute exposure-specific attack rates without overidentifying R0.
- **Outcome 2 (LO5):** Separate disease protection from transmission efficacy in vaccine-coverage calculations.
- **Outcome 3 (LO7):** Interpret replicate susceptibility observations under explicitly synthetic breakpoints and relate them to mechanism evidence.
- **Chapter LO coverage:** LO8, LO5, LO7
- **Rubric (20 points):** Score the following categories separately; keep disease, neutralization, transmission and susceptibility endpoints explicit.
  - **Evidence (8 points; LO8, LO5, LO7):** Award 2 for all 36 onset bins/24–28 h highest bins and the four attack-rate comparisons (1 each); 3 for pc=.75, V1 Re=4 and V2 Re=2.2 with unattainable Vc=1.5 (1 per group); 3 for all X/Y disk categories, the ≤2 mm within-pair differences and unchanged replicate categories (1 each). Show attendee/exposure denominators and label technical repeats.
  - **Controls (3 points; LO8, LO5, LO7):** Award 1 for comparing food eaters with other attendees while distinguishing the nonrandom external comparison; 1 for using baseline/placebo titers to interpret the vaccine-associated neutralization rise; 1 for explaining why growing no-drug lawns and a clear sterile control support assay interpretation but do not establish clinical breakpoints.
  - **Uncertainty (3 points; LO8, LO5, LO7):** Award 1 for a compatible, not proven, point source and missing secondary-transmission/generation-interval evidence for R0; 1 for the lack of an observed infection/transmission endpoint or validated titer threshold; 1 for distinguishing technical-repeat agreement from clinical validation or independent patient replication.
  - **Mechanism (4 points; LO5, LO7, LO8):** Award 1 for explaining why ET=0 cannot reduce Re despite disease protection; 1 for separating the Re=1 equality boundary from declining transmission; 1 for linking Y's ampicillin phenotype specifically to hydrolysis plus bla rather than assigning that mechanism to all drugs; 1 for correctly connecting each source-card intervention to its printed broad mechanism without supplying doses or unsupported efficacy.
  - **Transfer (2 points; LO7):** In the analysis prompt, award 1 for rejecting clinical application of the teaching cutoffs alone and 1 for naming organism/method/drug/current-breakpoint and exposure evidence required. A proposed patient regimen earns no transfer credit.
<!-- lab-alignment-end -->

## Lab Context: Host Immunity and Vaccines {.unnumbered}

Protection against symptomatic disease, infection and onward transmission are different endpoints. Epidemic curves and susceptibility assays likewise require their own denominators and controls.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Complete 72-hour synthetic norovirus-like curve; intervals are left-closed 2-hour bins; all 500 event attendees were exposed at hour 0 and followed completely. {#tbl:unit_VII_host_immunity_and_vaccines_alignment_and_rubric_map}
| Bin numbers (bin j spans 2j to 2j+2 hours) | New cases in bin order |
| --- | --- |
|0–7|0,0,0,0,0,0,0,0|
|8–17|5,10,15,20,25,25,20,15,10,5|
|18–35|0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0|
| Food comparison within event | Food A eaters: 140/400 cases; other attendees: 10/100 cases; total: 150/500 |
| External comparison |3/100 nonattendees meet the same symptom definition; not randomized |

: Vaccine model and immune-response evidence, all synthetic and endpoint-specific. {#tbl:unit_VII_host_immunity_and_vaccines_source_governance_checkpoint}
| Card | Supplied evidence |
| --- | --- |
| V1 | R0=4; coverage V=0.90; vaccine efficacy against disease is 95%, with zero effect on infection/infectiousness |
| V2 | Same R0 and V; stipulated transmission-blocking efficacy ET=0.50, with no waning or mixing heterogeneity |
| Immune response | Three vaccinated individuals have baseline/4-week neutralization titers of 0/80, 0/160 and 0/80; three placebo participants have 0/0, 0/0 and 0/0. No infection or transmission outcome was observed. |
| Formula | $R_e=R_0(1-VE_T)$; $p_c=1-1/R_0$ and $V_c=p_c/E_T$ mark $R_e=1$ under homogeneous durable transmission protection. Declining transmission requires exceeding the boundary; disease efficacy cannot replace $E_T$. |

: Synthetic disk-diffusion measurements (mm); two technical repeats per strain, not two patients. Teaching cutoffs are S ≥20 mm, I 15–19 mm and R ≤14 mm; these are not clinical breakpoints. {#tbl:unit_VII_host_immunity_and_vaccines_packet_3}
| Drug | Strain X repeats | Strain Y repeats |
| --- | --- | --- |
| Ampicillin |22,24|10,12|
| Kanamycin |25,24|23,22|
| Tetracycline |18,17|13,12|
| Chloramphenicol |21,22|16,17|
| Ciprofloxacin |27,26|11,13|
| Controls |No-drug lawns grow for both|Sterile control clear; organism/drug clinical breakpoint not supplied|
| Mechanism card | Y has a functional beta-lactam hydrolysis assay and a bla determinant | No mechanistic assay supplied for other drugs |

: Printed intervention/source comparison cards (paraphrases, not treatment instructions). {#tbl:unit_VII_host_immunity_and_vaccines_packet_4}
| Context | Evidence needed and limits |
| --- | --- |
| TB | WHO 2025: RR/MDR treatment selection uses susceptibility and eligibility. Fluoroquinolone resistance must not route to moxifloxacin-containing BPaLM; BPaL or alternatives require their own review. |
| HIV PrEP |Oral options require regimen-specific eligibility/adherence; long-acting cabotegravir and twice-yearly lenacapavir reduce daily pill demands but require testing, follow-up and access. Suspected established infection is not a routine prevention-only decision. |
| Malaria | WHO August 2025: indoor spatial emanators can supplement insecticide-treated nets in appropriate ongoing-transmission settings; not an outdoor or standalone substitute. Monitor vector behavior/resistance. |

Mechanism reference for the intervention task: TB drugs target bacterial processes, with susceptibility determining whether a drug remains active; HIV PrEP prevents establishment of infection when an eligible HIV-negative person has protective drug exposure; nets and spatial emanators reduce indoor mosquito contact through physical and insecticide-mediated protection. These broad mechanisms do not supply a dose, regimen or efficacy for a particular person. If an exact source date or product-specific eligibility criterion is absent from a card, mark it as not supplied and name the evidence needed rather than inventing it.


## Paper-Based Investigation {.unnumbered}

1. Plot all 36 bins, identify the highest bins and compute overall, food-specific and external attack rates. State whether the curve is compatible with point-source exposure and whether R0 is identifiable from this curve alone.
2. Compute $p_c$ and $R_e$ for V1/V2; identify the equality boundary versus $R_e<1$ and distinguish neutralization from disease protection or transmission. For the source cards name one mechanism, eligibility evidence and equity constraint for each intervention.
3. Classify every disk result using the printed teaching cutoffs, compare technical-repeat agreement and decide which resistance mechanism is actually supported. Explain what clinical information would be needed before translating the synthetic cutoffs to patient care.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** CDC Pink Book poliomyelitis chapter, May 1, 2024, distinguishes IPV protection against paralytic disease from intestinal immunity and stool shedding. Therefore a paralysis-protection percentage cannot establish a transmission-coverage threshold. The intervention cards summarize WHO 2025 TB/vector guidance and CDC 2025 lenacapavir-PrEP guidance discussed in the parent chapter; none substitutes for current patient-specific care. All numeric observations here are synthetic; refresh guidance and endpoint definitions when official recommendations change. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain which controls support the titer and disk observations and why neither establishes transmission protection or patient benefit. Then assess the proposed transfer “Strain Y is clinically resistant to ciprofloxacin because both teaching zones are ≤14 mm.” State the conclusion allowed within the packet, the organism/method/drug/exposure and current-breakpoint information needed before patient interpretation, and why Y's beta-lactam hydrolysis result does not supply a ciprofloxacin mechanism.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: 150 cases/500 attendees=30%; Food A 140/400=35%, others 10/100=10%, external 3/100=3%. Peak bins 12 and 13 cover 24–28 h, with 25 cases each; a midpoint estimate is 26 h, not an exact individual incubation time. A common source is compatible with this evidence, not proven. A point-source onset curve does not identify R0 without secondary-transmission and generation-interval evidence.
Task 2: $p_c=.75$ is the $R_e=1$ boundary, not guaranteed elimination. V1 has $R_e=4$ at every coverage because $E_T=0$; V2 has $R_e=4(1-.9\times.5)=2.2$. V2 would need $V_c=.75/.5=1.5$, unattainable even at equality. Neutralization rises after vaccination, but no supplied titer threshold or outcome trial converts it into 95% infection prevention. TB review needs resistance/eligibility; PrEP needs HIV testing and feasible follow-up; malaria needs indoor vector/exposure evidence. Credit one specific access barrier per case, such as diagnostic access, clinic travel or equitable net/emanator distribution.
Task 3: X results are S, S, I, S, S; Y results are R, S, R, I, R in the listed drug order. Each technical pair differs by at most 2 mm and retains its category. Ampicillin hydrolysis plus bla supports enzymatic inactivation for Y, but does not identify mechanisms for its other phenotypes. Clinical interpretation requires organism, method, drug, dose/exposure context and a current breakpoint standard.

Transfer benchmark: Y's 11/13 mm ciprofloxacin zones are R only under the stipulated synthetic rule. Clinical interpretation needs the identified organism, standardized method/quality assurance, drug and exposure context, and a current applicable breakpoint standard. Ampicillin hydrolysis plus bla supports beta-lactam inactivation, not a ciprofloxacin mechanism or a treatment choice. Concordant technical repeats do not close these evidence gaps.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
