# Lab — Bacteria, Archaea, and Viruses {#sec:lab_unit_VII_bacteria_archaea_viruses .unnumbered}

*This activity accompanies \cref{sec:unit_VII_bacteria_archaea_viruses}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO2):** Classify printed stain observations using positive, negative and uninterpretable controls.
- **Outcome 2 (LO10):** Calculate CFU per milliliter and infer exponential growth only within its valid interval.
- **Outcome 3 (LO5):** Distinguish clonal spread from mobile-element sharing and delimit transfer-route/direction claims from the supplied genomes.
- **Chapter LO coverage:** LO2, LO10, LO5
- **Rubric (20 points):** Score the following categories separately; label the assay or genome evidence supporting each inference.
  - **Evidence (8 points; LO2, LO10, LO5):** Award 2 for X1–X4 classifications with shape/arrangement and X3 explicitly uninterpretable; 3 for choosing 10^-5, the three volume-corrected CFU/mL values and their mean (1 each); 2 for inferring 0.5 h doubling from all three cultures' 1–3 h intervals and excluding lag/plateau (1 each); 1 for separating the K1/K2 core-genome match from W's distinct-core/shared-plasmid evidence.
  - **Controls (3 points; LO2, LO10):** Award 1 for explaining the G+/G− differential-stain references; 1 for using zero sterile-medium colonies as a contamination check without calling the plates independent patients; 1 for comparing growing cultures with the no-carbon baseline without treating that baseline as a substitute for a growth-interval check.
  - **Uncertainty (3 points; LO2, LO10, LO5):** Award 1 for explaining why identical X1/X4 descriptors are not a blinded reliability estimate; 1 for distinguishing technical plate variation and dilution error from biological sampling variation; 1 for acknowledging that shared plasmid sequence/dates alone do not establish who transferred it to whom.
  - **Mechanism (4 points; LO2, LO10, LO5):** Award 1 for distinguishing stain outcome from species identity or susceptibility; 1 for explaining four doublings in two hours rather than fitting lag/plateau; 1 for distinguishing clonal spread from possible mobile-element sharing across lineages; 1 for stating why neither clone nor HGT evidence identifies the particular transformation/transduction/conjugation route in this packet.
  - **Transfer (2 points; LO5):** In the analysis prompt, award 1 for rejecting a proven wastewater-to-ward transfer direction and 1 for proposing directional exposure/longitudinal genome evidence with a contrasting prediction. Merely drawing an arrow from W to K1 earns no transfer credit.
<!-- lab-alignment-end -->

## Lab Context: Bacteria, Archaea, and Viruses {.unnumbered}

An observation must be matched to its assay. A stain description, a colony count, a growth curve and a genome-context record answer different questions.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Complete stain-observation cards; each scored field contains40 visible cells and a stated calibrated2µm reference. {#tbl:unit_VII_bacteria_archaea_viruses_alignment_and_rubric_map}
| Card | Observed color and shape | Quality/control information |
| --- | --- | --- |
| G+ | Purple rods in chains | Known Gram-positive control |
| G− | Pink rods, mostly single | Known Gram-negative control |
| X1 | Purple cocci in clusters | Focus and contrast adequate |
| X2 | Pink rods and purple cocci in separate groups | Both groups visible |
| X3 | No resolved cell outlines | Overexposed field; color unreliable |
| X4 | Purple cocci in clusters | Same descriptor asX1; printed repeat comparison, not a blinded reliability test |

: Colony-count observations; three technical plates from one sample,0.1mL plated per tube. {#tbl:unit_VII_bacteria_archaea_viruses_part_4_amr_network_and_fungal_triage_cards}
| Dilution | Plate1 colonies | Plate2 | Plate3 |
| --- | --- | --- | --- |
| 10^-4 | Too numerous to count | Too numerous | Too numerous |
| 10^-5 | 150 | 160 | 140 |
| 10^-6 | 15 | 16 | 14 |
| Sterile medium | 0 | 0 | 0 |
| Rule | Use30–300 colonies per plate | CFU/mL=colonies/(dilution×mL) | Technical repeats are not three patient samples |

: Printed synthetic growth curves, cell counts; each row is a separate starting culture with no death process. {#tbl:unit_VII_bacteria_archaea_viruses_part_4_amr_network_and_fungal_triage_cards_2}
| Culture | 0h | 1h | 2h | 3h | 4h |
| --- | --- | --- | --- | --- | --- |
| A | 1000 | 1000 | 4000 | 16000 | 16000 |
| B | 980 | 980 | 3920 | 15680 | 15680 |
| C | 1020 | 1020 | 4080 | 16320 | 16320 |
| No-carbon baseline | 1000 | 1000 | 1000 | 1000 | 1000 |
| Model | Lag1h | Doubling time0.5h | Exponential interval | Stationary onset3h | Plateau is population reached, not an injected capacity |

: Molecular/context and fungal triage evidence cards. {#tbl:unit_VII_bacteria_archaea_viruses_part_4_amr_network_and_fungal_triage_cards_3}
| Card | Complete evidence |
| --- | --- |
| K1/K2 | Ward 1 and Ward 2 isolates have near-identical core genomes and plasmid P carrying a carbapenemase; sampled on days 1 and 3. |
| W | Wastewater isolate onday3 has a distinct core genome but the same fully resolved plasmidP sequence; no directional exposure record. |
| C1 | Adult, positive C.auris skin screen, no infection symptoms or sterile-site isolate. |
| C2 | Adult, C.auris in blood plus signs of infection; susceptibility testing available, treatment response requires monitoring. |
| C3 | Yeast reported only by an identification method not validated to distinguish C.auris from related species; no confirmatory result. |

## Paper-Based Investigation {.unnumbered}

1. Classify X1–X4 as Gram-positive, negative, mixed or uninterpretable; record shape, arrangement and confidence. Compare the two identical X1/X4 descriptors without claiming blinding or an independent reliability estimate. Explain what the controls do not establish about species or drug susceptibility.
2. Choose the countable dilution, calculate each CFU/mL and the mean, then infer doubling time from 1–3 h in each culture. Explain why 0–1 h or 3–4 h cannot be fitted as the same exponential interval.
3. Draw separate arrows for clone transmission, possible plasmid transfer and sampling. For C1–C3 choose infection-control, treatment assessment and/or confirmatory identification, with reasons. Do not infer a proven transfer direction or prescribe a patient regimen.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** CDC C.auris clinical overview/care guidance distinguishes colonization from infection and advises against treating colonization alone; adults with invasive infection are assessed for initial echinocandin therapy and susceptibility/response monitoring. These are official guidance summaries, not quotations or dosing instructions. Ferry2022 reports a personalized adjunctive phage case with surgery and antibiotics, not standalone efficacy. The packet observations are synthetic; refresh guidance and identification methods when official recommendations or susceptibility evidence changes. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

For a source whose exact publication date is not printed, record “date not supplied”; the year in Ferry2022 is the available date precision. Identify the endpoint from the printed summary rather than inventing a date or requiring a live lookup.

## Analysis Questions {.unnumbered}

Explain why the stain controls cannot establish drug susceptibility and why technical plates are not independent patient samples. Then assess the proposed transfer “W proves wastewater donated plasmid P to the ward.” Use sampling dates, core genomes and plasmid identity to identify what is supported and what is missing. Propose one longitudinal exposure/genome comparison that could distinguish this direction from the reverse or a shared unsampled source; specify a predicted pattern without inventing new observations. Keep C1–C3's fungal colonization/infection decisions separate from bacterial HGT.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task1: X1/X4 are Gram-positive cocci in clusters; X2 mixed; X3 uninterpretable, not a negative stain. G+/G− validate differential staining in this packet; no species-specific or susceptibility conclusion follows. The one identical descriptor pair should agree, but that is not an empirical estimate of observer reliability and was not blinded.
Task 2: 10^-5 yields 1.5, 1.6, 1.4×10^8 CFU/mL; mean 1.5×10^8. Count SD is 10 colonies, corresponding to 1×10^7 CFU/mL across technical plates; dilution and sampling error remain. From 1–3 h, sixteenfold increase means four doublings in 2 h, or 0.5 h each. Lag and plateau are continuous; the model has no death phase.
Task3: K1/K2 support clonal spread as a candidate; W makes mobile-element sharing plausible but does not establish where or when transfer occurred. C1 calls for infection-control action, not automatic antifungal treatment. C2 requires clinical treatment assessment plus infection control and monitoring. C3 needs reliable confirmation and context-appropriate precautions; ambiguous identification is not confirmed infection. Credit explicit uncertainty and the distinction between bacterial HGT and fungal persistence.

Transfer benchmark: W and K2 were sampled on day 3 and K1 on day 1, but sampling dates are not acquisition dates. Shared P supports mobile-element sharing across lineages, not W→ward direction or a particular transfer route. Time-resolved recipient-before/after sampling, donor/exposure records and informative plasmid variants could discriminate histories; the alternative of a shared unsampled source must remain. C.auris detection is not evidence of bacterial plasmid transfer.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
