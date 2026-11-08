# Lab — Microbial Ecology and the Microbiome {#sec:lab_unit_VII_microbial_ecology .unnumbered}

*This activity accompanies \cref{sec:unit_VII_microbial_ecology}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO2):** Compute diversity from the supplied ten-taxon counts and compare independent source replicates.
- **Outcome 2 (LO3):** Apply the printed subsampling manifest and distinguish read-depth control from bias correction.
- **Outcome 3 (LO2):** Contrast community richness and connectance changes with measured product output to delimit diversity-based functional claims.
- **Chapter LO coverage:** LO2, LO3
- **Coverage limit:** The network provides a composition-versus-function comparison for interpreting diversity. It supplies no biofilm, quorum-sensing or bioremediation observations and therefore does not claim LO8 coverage.
- **Rubric (20 points):** Score the following categories separately; composition, relative reads and product flux are different observables.
  - **Evidence (8 points; LO2, LO3):** Award 3 for richness/H/inverse-Simpson values across all 12 source rows, source means and a stated replicate-variability summary (1 each); 1 for the H-versus-A diversity contrast; 2 for the 7:1:1:1 subsample and its proportions/diversity (1 each); 2 for baseline/removal connectance and the three product means with units (1 each).
  - **Controls (3 points; LO2, LO3):** Award 1 for equal read depth/taxon scoring across source rows while retaining three biological replicates per source; 1 for using the extraction blank and defined community to distinguish contamination checks from demonstrated composition bias; 1 for comparing removal with both baseline and A rescue at the same measured product endpoint.
  - **Uncertainty (3 points; LO2, LO3):** Award 1 for recognizing that 100 reads are not 100 biological samples; 1 for limiting the manifest result to one realized draw rather than an expected rarefaction curve; 1 for identifying an unmeasured manipulation effect or absent H/A functional endpoint that prevents a broader causal/function claim.
  - **Mechanism (4 points; LO2, LO3):** Award 1 for explaining why richness can stay 10 while H/evenness falls; 1 for explaining why equalizing read depth cannot correct the defined-community measurement bias; 1 for distinguishing 1% cell-to-colony recovery from a fraction of species; 1 for interpreting A removal/rescue as function-specific evidence, not a causal claim from a co-occurrence edge.
  - **Transfer (2 points; LO2):** In the analysis prompt, award 1 for rejecting unchanged connectance as evidence of unchanged function and 1 for using the product/rescue comparison while withholding an H/A functional conclusion. A diversity ranking alone earns no transfer credit.
<!-- lab-alignment-end -->

## Lab Context: Microbial Ecology and the Microbiome {.unnumbered}

Composition, richness, function and causal interaction are different quantities. All four source labels below are synthetic teaching conditions, not claims about the typical ranking of real habitats.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Ten-taxon source counts,100 reads per independent biological teaching replicate; columnsT1–T10 have identical scoring definitions across rows. {#tbl:unit_VII_microbial_ecology_alignment_and_rubric_map}
| Sample | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Soil1 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| Soil2 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| Soil3 | 19 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| Skin1 | 91 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Skin2 | 82 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Skin3 | 73 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Water1 | 50 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Water2 | 60 | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Water3 | 70 | 30 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Gut1 | 40 | 30 | 20 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| Gut2 | 25 | 25 | 25 | 25 | 0 | 0 | 0 | 0 | 0 | 0 |
| Gut3 | 70 | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |

: Paired host perturbation benchmark and controls, separate from habitat samples. {#tbl:unit_VII_microbial_ecology_part_3_microbial_interaction_network_analysis}
| Card | Complete evidence |
| --- | --- |
| Healthy H | T1–T10 counts10 each, n100; newly authored benchmark |
| Antibiotic A | T1 count91, T2–T10 count1 each, n100; newly authored matched benchmark |
| Extraction blank | Zero amplified reads after threshold; does not rule out all contamination |
| Defined community | Four taxa expected 25% each; observed 40, 30, 20, 10 of 100 reads; indicates measurement bias despite known composition |
| Culture comparison | From 1000 microscopically counted cells only 10 colonies grow under one medium condition; no claim that each cell is a distinct taxon |

: Finite subsampling exercise with its complete20-read library and draw manifest. {#tbl:unit_VII_microbial_ecology_part_3_microbial_interaction_network_analysis_2}
| Object | Printed values |
| --- | --- |
| Read labels1–20 | A,A,A,A,A,A,A,A,A,A,A,A,A,A,B,B,C,C,D,D |
| Illustrative without-replacement permutation | 2,4,6,8,10,12,14,16,18,20,1,3,5,7,9,11,13,15,17,19 |
| Rule | Use the first10 indices, count taxa and calculate proportions. This one realized draw is not an expected rarefaction curve; multiple draws would quantify subsampling uncertainty. |
| Formulas | H=−Σp ln p,0ln0=0;inverseSimpson=1/Σp²;evenness=H/lnS forS>1 |

: Directed metabolic network and perturbation observations. {#tbl:unit_VII_microbial_ecology_part_3_microbial_interaction_network_analysis_13}
| Condition | Printed edges and endpoint |
| --- | --- |
| Baseline | NodesA,B,C,D; edgesA→B,A→C,B→D,C→D; no self-links; n3 microcosms, product9,10,11µmol/day |
| Remove A | Remaining nodesB,C,D; edgesB→D,C→D; n3 microcosms, product1,2,3µmol/day |
| Rescue A | Original nodes/edges restored; n3 microcosms, product8,10,12µmol/day |
| Definitions | Directed connectance=L/[S(S−1)]; these edges are stipulated metabolite transfers, not inferred correlations |


## Paper-Based Investigation {.unnumbered}

1. Calculate richness, H and inverse Simpson for every row, then report source means and variability. Compare H versus A and distinguish a functional prediction from measured function.
2. Apply the finite subsampling manifest. Explain why equalizing read depth does not remove the defined-community bias or turn relative reads into absolute cell counts; interpret the culture comparison.
3. Calculate baseline/removal connectance and product means, then evaluate A's role using removal and rescue. State which causal conclusions would fail if the edges were only co-occurrence correlations.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Sorg/Sonenshein 2008 (DOI 10.1128/JB.01765-07 \citep{sorg2008bilesalts}) experimentally distinguished bile-acid effects on spore germination and vegetative growth; deoxycholate could stimulate the former and inhibit the latter. The current GTDB R11-RS232 snapshot is April 15, 2026; a release 10 publication alone does not substantiate release 11 counts. This packet's taxa/counts/network are synthetic. Revise conclusions with extraction controls, functional assays or a changed taxonomy version, not by silently updating labels. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain what the blank, defined community and equal-depth comparison each control, and name a bias they do not remove. Then assess the proposed transfer “Because connectance remains 1/3 after A removal, product function is unchanged, and antibiotic A's lower diversity proves the same product loss in the host.” Use the network's measured products/rescue and the separate H/A composition cards to separate supported from unsupported conclusions. No host product assay is stipulated.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: H values: Soil 1/2=2.302585, Soil 3=2.265975; Skin 1=.500288, Skin 2=.866894, Skin 3=1.176509; Water=.693147, .673012, .610864; Gut=1.279854, 1.386294, .940448. Source means are approximately 2.290382, .847897, .659008, 1.202199 nats. Inverse-Simpson values in the same row order are: Soil 10, 10, 9.174312; Skin 1.206273, 1.479290, 1.848429; Water 2, 1.923077, 1.724138; Gut 3.333333, 4, 1.923077. Richness is 10 for soil/skin, 2 for water and 4 for gut; evenness is each H divided by the natural log of its richness. Report three biological replicates per condition rather than treating 100 reads as 100 independent habitats. H versus A retains richness 10 but loses evenness: H 2.302585→.500288; inverse Simpson 10→1.206273. No SCFA endpoint is supplied for that pair.
Task2: the ten selected reads contain7A,1B,1C,1D, proportions.7,.1,.1,.1; H=.940448 and inverse Simpson1.923077. The defined-community distortion remains despite n100. Culture recovery10/1000=1% describes this medium's cell-to-colony recovery, not the fraction of species existing or a universal unculturable fraction.
Task3: baseline connectance4/12=1/3; removal2/6=1/3. Edge number falls but connectance need not. Product means10,2,10µmol/day support a function-specific role forA with rescue, subject to manipulation controls. Do not infer that all diversity loss proportionally lowers function or that a correlation network establishes directed metabolite transfer.

Transfer benchmark: Connectance remains 4/12=2/6=1/3, but mean product changes 10→2→10 µmol/day across baseline/removal/rescue. Constant connectance therefore does not imply constant function. This supports A's role for that product under the stated manipulation, subject to manipulation controls; it does not establish universal diversity–function scaling. H/A supplies a composition/evenness contrast without a product or SCFA endpoint, so the network's functional effect cannot be assigned to that host comparison.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
