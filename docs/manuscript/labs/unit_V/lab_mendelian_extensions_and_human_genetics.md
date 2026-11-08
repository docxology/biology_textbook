# Lab — Mendelian Extensions and Human Genetics {#sec:lab_unit_V_mendelian_extensions_and_human_genetics .unnumbered}

*This activity accompanies \cref{sec:unit_V_mendelian_extensions_and_human_genetics}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Derive modified ratios for epistasis and lethal alleles.
- **Outcome 2 (LO3):** Test the supplied cross counts and estimate age-specific penetrance.
- **Outcome 3 (LO5):** Compare X-linked and autosomal models across the three-generation case.
- **Chapter LO coverage:** LO1, LO3, LO5
- **Rubric (20 points):** Score the following categories separately; show genotype rules, expected counts and conditional denominators.
  - **Evidence (8 points; LO1, LO3, LO5):** Award 2 for E's 9:3:4 and L's living-offspring 2:1 derivations (1 each); 2 for C1 and pooled-monohybrid expectations, chi-square and decisions (1 each); 2 for P's 48/80 proportion and SE (1 each); 2 for F1's two compatible models and F2's per-child 1/8 risk (1 each).
  - **Controls (3 points; LO1, LO3):** Award 1 for using tt viability as L's baseline while excluding prenatal TT only from the living denominator; 1 for comparing 48/80 carriers with 8/80 genotype-negative people without claiming causation; 1 for distinguishing a fixed-ratio pooled test from a between-replicate homogeneity test.
  - **Uncertainty (3 points; LO3, LO5):** Award 1 for limiting .60 to the ascertained age-40 sample; 1 for explaining that binomial SE assumes independent sampling and does not repair ascertainment; 1 for retaining F1's unknown partner genotype rather than declaring a unique inheritance model.
  - **Mechanism (4 points; LO1, LO5):** Award 1 for explaining ee masking at E; 1 for explaining survival-based ratio change at L without altered allele segregation; 1 for the affected XLR father's transmission to every daughter; 1 for multiplying independent autosomal and sex-linked probabilities in F2, with the sex factor included.
  - **Transfer (2 points; LO5):** In the analysis prompt, award 1 for choosing an informative observation within F1 and 1 for stating contrasting AR/XLR predictions. Merely requesting “more family data” earns neither point.
<!-- lab-alignment-end -->

## Lab Context: Mendelian Extensions and Human Genetics {.unnumbered}

Phenotype mapping can change while alleles continue to segregate. Small pedigrees may leave more than one inheritance model compatible.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Independent cross replicates. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map}
| Replicate | Stipulated AaBb self: A_B_,A_bb,aaB_,aabb | Dominant,recessive Aa self |
| --- | --- | --- |
| C1 |92,28,29,11 (n160) |74,26 (n100) |
| C2 |88,32,31,9 (n160) |77,23 (n100) |
| C3 |90,30,30,10 (n160) |75,25 (n100) |

: Genotype-to-phenotype cards. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map_2}
| Model | Rule and controls |
| --- | --- |
| E |B_E_=black,bbE_=chocolate,ee=yellow; BbEe self; loci independent |
| L |Tt self;TT dies before birth,Tt tailless,tt tailed; viability of tt=1 baseline |
| P | 80 people carry variant V; 48 meet phenotype definition at age 40; genotype-negative comparison 8/80; ascertainment otherwise unspecified |

: Linked family records, with independent autosomal and X loci. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map_3}
| Family | Evidence |
| --- | --- |
| F1 |Unaffected I-1 male/I-2 female have affected II-1 andII-2 sons, unaffected II-3 son andII-4–II-6 daughters. II-1 has unaffected III-1 daughter with an unaffected partner whose genotype is unknown. |
| F2 |I father X^aY,Aa and mother X^AX^a,Aa; their II daughter X^AX^a,Aa mates with X^AY,aa. Full penetrance at both loci. |

For F1, stipulate full penetrance, no new mutation and correct parentage under each candidate model. Use equally likely X/Y-bearing sperm (sex probability 1/2) for F2's per-child calculation; loci segregate independently.

: Decision constants and disclosure case. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map_4}
| Card | Inputs |
| --- | --- |
| Test | χ²=sum(O−E)^2/E; df=3 critical 7.815 for 9:3:3:1; df=1 critical 3.841 for 3:1, α=.05 |
| Counseling |An unvalidated PRS assigns10% risk to100 people;20 later meet the endpoint. No age horizon or discovery cohort supplied. No participant consent for family disclosure. |

## Paper-Based Investigation {.unnumbered}

1. Derive E and living-offspring L ratios. Test C1 against9:3:3:1 and the pooled monohybrid replicates against3:1; distinguish pooling from a between-replicate test.
2. Estimate P's age-40 phenotype proportion among variant carriers and its binomial SE $\sqrt{\hat p(1-\hat p)/80}$ under independent sampling. Compare the genotype-negative proportion, then evaluate PRS calibration and missing disclosure permissions. Ascertainment is unspecified, so the proportion is not an established population penetrance estimate.
3. Compare AR versus XLR for F1 without assuming an unaffected partner is a noncarrier. For F2 compute the generation-III risk of a child affected at both independent loci. Propose one additional informative genetic observation.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Richards2015 ACMG/AMP consensus combines population, segregation, computational and functional evidence for variant classification; Martin2019 is a perspective warning about unequal PRS performance in available cohorts, not a2026 universal accuracy ratio. These paraphrases support evidence standards, not diagnosis of the synthetic families. Update a clinical interpretation when variant evidence, classification guidance or score-specific external validation changes. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain which printed comparison supplies a baseline for P and why it cannot resolve causation or population penetrance. For a concrete transfer of the F1 model comparison, suppose a reliable test of III-1 at the candidate disease locus were available: which result would contradict the fully penetrant, no-new-mutation XLR model, and could AR still accommodate it? Use the existing family only; do not assume the unaffected partner is a noncarrier.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: E=9 black:3 chocolate:4 yellow. L conceptions 1 TT:2 Tt:1 tt; surviving 2 Tt:1 tt. C1 expectations 90,30,30,10 give χ²=.3111, df=3, do not reject. Monohybrid pooled 226:74, n=300, expected 225:75 gives χ²=1/225+1/75=.01778, df=1. Pooling tests aggregate ratio, not replicate homogeneity.
Task 2: estimated carrier phenotype proportion 48/80=.60, SE=sqrt(.24/80)=.0548; unspecified ascertainment prevents an established population penetrance estimate. Genotype-negative proportion=.10 is a comparison, not proof of causality. PRS observed 20% versus 10% predicted shows miscalibration for this cohort; missing endpoint horizon/cohort and consent prevent responsible individual/family disclosure.
Task3: both Aa×Aa AR and carrier-mother XLR fit F1. An unaffected daughter of an affected XLR father is an obligate carrier under full penetrance; maternal genotype remains unknown. F2 affected-son probability1/4 per child ×autosomal aa probability1/2=1/8. Credit phase/sex-specific transmission and an informative genotype proposal, not a uniquely asserted diagnosis.

Transfer benchmark: Under XLR, affected II-1 must transmit X^a to III-1, who is an unaffected obligate carrier. A reliable absence of that allele in III-1 contradicts the stipulated XLR model. Under AR, an aa father can have an unaffected Aa daughter with a partner carrying A, so absence of the candidate X-linked allele need not contradict AR. A positive X-linked allele result alone does not exclude AR at an independent autosomal locus.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
