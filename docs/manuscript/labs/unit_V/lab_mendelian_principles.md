# Lab — Mendelian Principles and Probability {#sec:lab_unit_V_mendelian_principles .unnumbered}

*This activity accompanies \cref{sec:unit_V_mendelian_principles}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO3):** Derive monohybrid and trihybrid genotype and phenotype probabilities.
- **Outcome 2 (LO6):** Compute a fixed-ratio chi-square test and distinguish consistency from proof.
- **Outcome 3 (LO7):** Infer obligate carriers and conditional recurrence risk from the printed pedigree.
- **Chapter LO coverage:** LO3, LO6, LO7
- **Rubric (20 points):** Score the following categories separately; preserve the distinction between fixed-ratio testing and conditional family risk.
  - **Evidence (8 points; LO3, LO6, LO7):** Award 2 for P1 expected counts, chi-square and correct comparison with 3.841; 1 for P4's binomial probability; 3 for T's eight probabilities summing to 1, 27 genotype classes and n≥320 with df7 (1 each); 2 for a correctly connected Family F drawing/genotypes and the pre-birth 1/6 risk with its 2/3 conditional denominator (1 each).
  - **Controls (3 points; LO3, LO6):** Award 1 each for explaining P2's dominance reference and P3's recessive scoring control; award 1 for stating that those controls do not establish independent assortment at T's three loci. Naming the cards without their roles earns no control credit.
  - **Uncertainty (3 points; LO3, LO6):** Award 1 for interpreting P1 as failure to reject rather than proof; 1 for using P4 to explain finite-sample variation under a 1:1 model; 1 for distinguishing T's minimum expected-count rule from adequate power or guaranteed model validity.
  - **Mechanism (4 points; LO3, LO7):** Award 1 for deriving 3:1 phenotypes from 1:2:1 genotypes; 1 for multiplying unlinked-locus probabilities in T; 1 for showing why unaffected II-2 excludes aa but retains AA and Aa; 1 for explaining that III-1's unaffected phenotype does not prove II-2 is AA.
  - **Transfer (2 points; LO7):** In the analysis prompt, award 1 for updating II-2's carrier probability to 3/5 after III-1 is known unaffected and 1 for the next-child risk 3/20, explicitly distinguished from pre-birth 1/6. Repeating 1/6 without recognizing the new conditioning earns no transfer credit.
<!-- lab-alignment-end -->

## Lab Context: Mendelian Principles and Probability {.unnumbered}

Segregation predicts probability distributions, not exact ratios in each small family. Independent assortment and complete penetrance are stipulated unless a card says otherwise.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Cross observations and reference controls. {#tbl:unit_V_mendelian_principles_example_pedigree_autosomal_recessive_trait_cystic_fibrosis}
| Card | Cross | Observations | Sample |
| --- | --- | --- | --- |
| P1 | Aa×Aa |450 dominant,130 recessive |580 independent offspring |
| P2 | AA×aa |40 dominant,0 recessive |40 offspring; dominance reference |
| P3 | aa×aa |0 dominant,40 recessive |40 offspring; recessive scoring control |
| P4 | Rr×rr |3 round,1 wrinkled |4 offspring |

: Three-generation recessive pedigree and supplied decision constants. {#tbl:unit_V_mendelian_principles_source_governance_checkpoint}
| Card | Printed evidence |
| --- | --- |
| Family F | I-1 unaffected male and I-2 unaffected female have II-1 affected daughter and II-2 unaffected son. II-2 mates with II-3, a molecularly confirmed Aa carrier; their III-1 child is unaffected. Affected=aa; complete penetrance; no new mutation. |
| T | AaBbCc×AaBbCc; unlinked loci, complete dominance; no viability differences. |
| C | Chi-square=sum(O−E)^2/E; fixed2-class df1 critical3.841 atα=.05; fixed8-class df7. Binomial P(k)=choose(n,k)p^k(1−p)^(n−k). |

## Paper-Based Investigation {.unnumbered}

1. Compute P1 expectations and chi-square; use P2/P3 to explain what scoring/dominance controls establish. For P4 calculate the probability of 3 round under 1:1.
2. For T list eight phenotype probabilities, count genotype classes, and find n for the rarest expected phenotype count≥5. State df and approximation limits.
3. Draw Family F using its IDs. Infer generation-I genotypes, II-2 carrier probability conditional on being unaffected, and the pre-birth affected risk for a child of II-2×II-3. Explain why an unaffected III-1 does not remove future risk.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Mendel1866 reports controlled pea crosses; the packet uses newly stipulated counts to teach those probability models, not a transcription of his raw observations. The inference assumes correctly identified parents, complete penetrance, independent offspring and no differential viability. Refresh the model if a controlled testcross shows reproducible genotype-specific survival or scoring errors. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain why P2/P3 cannot rule out linkage in T and identify a model assumption the P1 test does not verify. Then transfer Family F's calculation to the next-child question: after observing unaffected III-1, weight the AA and Aa possibilities for II-2 by their likelihood of producing an unaffected child with Aa II-3. Normalize those weights and compute the next-child affected risk. Explain why this differs from the original pre-birth question without making successive conceptions causally dependent.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: P1 expects 435,145; χ²=60/29≈2.069<3.841, so do not reject. P2/P3 check scoring under stipulated genotype controls, not linkage across all loci. P4 probability=4/16=.25; a 3:1 four-child sample is possible under 1:1.
Task 2: probabilities are 27/64 for A_B_C_; 9/64 each for aaB_C_,A_bbC_,A_B_cc; 3/64 each for aabbC_,aaB_cc,A_bbcc; 1/64 aabbcc. Sum=1; 27 genotypes, 8 phenotypes; n≥320; df=7. The expected-count criterion is not a power guarantee.
Task3: I-1/I-2 are Aa. II-2 has P(Aa|unaffected)=2/3, giving child affected risk(2/3)(1/4)=1/6 before conditioning on any child's outcome. III-1's unaffected status does not prove a parent's genotype. If that child's outcome is used to update the next-child risk, P(II-2=Aa|III-1 unaffected)=[(2/3)(3/4)]/[(2/3)(3/4)+(1/3)]=3/5, giving 3/20 affected risk for the next child; distinguish that posterior question from the requested pre-birth 1/6. Credit a correctly connected three-generation drawing and conditional denominator.

Transfer benchmark: Prior weights AA=1/3 and Aa=2/3 become (1/3)×1 and (2/3)×3/4 after an unaffected child. Normalizing gives carrier probability 3/5 and next-child affected risk (3/5)×1/4=3/20. The observation updates uncertainty about the parent's fixed genotype; it does not change Mendelian transmission probabilities conditional on that genotype.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
