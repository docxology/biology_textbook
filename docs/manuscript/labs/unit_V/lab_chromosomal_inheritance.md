# Lab — Chromosomal Inheritance and Linkage {#sec:lab_unit_V_chromosomal_inheritance .unnumbered}

*This activity accompanies \cref{sec:unit_V_chromosomal_inheritance}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO9):** Assign phase-aware crossover classes, interval distances and interference.
- **Outcome 2 (LO7):** Distinguish karyotype dosage from evidence about nondisjunction stage.
- **Outcome 3 (LO6):** Calculate conditional X-linked risk and the effect of cis versus trans phase.
- **Chapter LO coverage:** LO9, LO7, LO6
- **Rubric (20 points):** Score the following categories separately; arithmetic credit requires the relevant offspring, sex or culture denominator.
  - **Evidence (8 points; LO9, LO7, LO6):** Award 3 for both interval RFs (0.5 each), summed map length and outer RF (0.5 each), and DCO expectation/CoC/interference (1); 2 for correct count-versus-dosage classifications of K1–K4 (0.5 each); 3 for H, C and cis/trans sex-conditioned risks (1 per card).
  - **Controls (3 points; LO9, LO7):** Award 1 for explaining how the abc/abc tester reveals maternal gametes; 1 for using untreated cultures as the spindle-perturbation baseline; 1 for comparing culture-level rates/means rather than treating all cells as independent treatments.
  - **Uncertainty (3 points; LO9, LO7):** Award 1 for identifying the six DCOs as a sparse sample, not proof of a universal negative-interference rule; 1 for explaining why chromosome counts cannot identify MI versus MII; 1 for a concrete unmeasured limitation such as viability distortion, marker informativeness or mosaicism and its effect on inference.
  - **Mechanism (4 points; LO9, LO7, LO6):** Award 1 for locating B by the parental/DCO allele change; 1 for explaining why DCOs enter both intervals but not outer RF; 1 for connecting centromeric isodisomy/distal heterodisomy to recombination plus a compatible MII-error/rescue history without calling it unique; 1 for tracing paternal X transmission and maternal phase to the different risks.
  - **Transfer (2 points; LO6):** In the analysis prompt, award 1 for rejecting a phase-specific two-condition risk from H's one-locus record and 1 for identifying the additional phase/RF information needed. A one-locus risk alone earns neither transfer point.
<!-- lab-alignment-end -->

## Lab Context: Chromosomal Inheritance and Linkage {.unnumbered}

Printed chromosome inventories substitute for images without losing dosage evidence. Chromosome number alone does not identify the meiotic division of origin.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Eight-class three-point testcross; counts are offspring and haplotypes are maternal gametes. {#tbl:unit_V_chromosomal_inheritance_alignment_and_rubric_map}
| Haplotype | ABC | abc | Abc | aBC | ABc | abC | AbC | aBc | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Count | 440 | 435 | 48 | 45 | 14 | 12 | 4 | 2 | 1000 |

Testcross assumptions: maternal phase ABC/abc, tester abc/abc; offspring reveal maternal gametes without scoring error or viability distortion. Treat the two largest classes as parentals and the two smallest as candidate double crossovers under the short-interval three-point model. Counts are one synthetic cross, not replicate crosses.

: Four complete chromosome-inventory cards (diploid human metaphase). {#tbl:unit_V_chromosomal_inheritance_part_3_karyotype_analysis}
| Case | Printed inventory |
| --- | --- |
| K1 | Autosomes1–22 each2 copies;X2,Y0;total46 |
| K2 | Autosomes1–22 each2 copies;X1,Y0;total45 |
| K3 | Autosomes 1–20 and 22 each 2 copies; 21 has 3; X2,Y0; total 47 |
| K4 | Autosomes 1–13,15–20,22 each 2 copies; one free 14, one free 21 and one fused rob(14;21); X2,Y0; total 45; two copies each of 14q/21q |

: Pedigree and linked-marker cards. {#tbl:unit_V_chromosomal_inheritance_part_3_karyotype_analysis_2}
| Card | Genotypes/evidence |
| --- | --- |
| H | I unaffected male X^HY ×carrier female X^HX^h have II affected male X^hY. II mates with a known carrier X^HX^h; consider III daughters andsons separately. |
| C | Color-vision locus: carrier X^CX^c mother ×X^CY father; complete penetrance; no mutation |
| Phase | Independent of H/C: maternal X loci h,c with RF=.06;compare hc/HC versus hC/Hc |
| UPD | Mother has centromeric alleles M1/M2,distal D1/D2. Child receives maternal M1/M1 andD1/D2, no paternal copy; marker typing is reliable. |

: Spindle-perturbation archived teaching counts and formulas. {#tbl:unit_V_chromosomal_inheritance_part_3_karyotype_analysis_3}
| Replicate | Untreated abnormal/total | Perturbed abnormal/total |
| --- | --- | --- |
| 1 | 2/100 | 18/100 |
| 2 | 3/100 | 20/100 |
| 3 | 1/100 | 22/100 |
| Rule | RF=interval recombinants/n;expected DCO=n×r1×r2 | CoC=observed/expected;I=1−CoC |

Each spindle row is an independently prepared synthetic culture per arm; the 100 cells are subsamples. H/C and phase-card risks are conditional on the stated sex, with full penetrance, equal transmission and no new mutation. For the phase comparison, assume sons receive Y from the father. The phase card is a separate hypothetical cross, not evidence inferred from H's one-locus pedigree.

## Paper-Based Investigation {.unnumbered}

1. Infer gene order from parentals/DCOs before computing both interval RFs, their summed map length, outer RF and interference. Compare the expectation under independent intervals with observed DCOs.
2. Classify K1–K4 by count and dosage. Calculate abnormality rates in each archived replicate and compare treatments without assuming chromosome morphology was measured. Interpret the UPD marker pattern.
3. Compute H daughter/son risks, C risks and phase-card proportions of sons with both conditions. State which baseline and uncertain assumptions each inference uses.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Sturtevant1913 uses recombination to order genes. The packet is a new illustrative testcross, not his original dataset. Short-interval RF approximates map distance; map distance is not physical length, and DCO sampling uncertainty matters. The toy inventories do not establish a clinical prognosis or parent-of-origin. Refresh a dosage interpretation with breakpoint, mosaicism or informative marker evidence. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Use the printed controls and replicate rates to explain what the spindle comparison supports and what it cannot identify about meiotic stage. Then assess this proposed transfer: “H's pedigree establishes that 47% of sons will have both h and c conditions.” State whether that inference is licensed and identify the missing information using the separate phase card. No additional family observations are stipulated.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task1: middleB; A–B=(48+45+4+2)/1000=.099; B–C=(14+12+4+2)/1000=.032. Map length13.1cM;outer RF=(48+45+14+12)/1000=.119. Expected DCO3.168,observed6;CoC1.89394,I≈−.89394. Negative interference here is a sample summary, not proof of a general biological rule; do not force apositive result.
Task 2: K1 typical 46,XX; K2 45,X; K3 trisomy 21; K4 balanced rob(14;21) carrier. Counts do not distinguish MI/MII. Untreated rates 2%,3%,1% versus 18%,20%,22%; mean 2% versus 20%. Three replicate units, not 600 independent experimental treatments. UPD has centromeric isodisomy but distal heterodisomy, compatible with prophase-I recombination before MII error/rescue.
Task 3: H half daughters carrier, half affected; half sons affected. Every daughter receives paternal X^h, not half. C half sons affected, half daughters carriers. Cis hc/HC gives 47% sons both, 47% neither, 3% each single; trans hC/Hc gives 3% both, 3% neither, 47% each single. Credit conditioning on sex and phase.

Transfer benchmark: H supplies no c-locus genotype, two-locus maternal phase or recombination fraction. The separate phase card gives 47% in cis versus 3% in trans under its own assumptions; neither value can be assigned to H without the corresponding two-locus evidence. Score this boundary separately from correct H arithmetic.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
