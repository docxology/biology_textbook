# Lab — Phylogenetics and the Tree of Life {#sec:lab_unit_VI_phylogenetics .unnumbered}

*This activity accompanies \cref{sec:unit_VI_phylogenetics}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO3):** Use the full character matrix to compare equally weighted parsimony hypotheses and report ties.
- **Outcome 2 (LO4):** Compute strict-clock dates and an explicit rate-sensitivity range without fabricating posterior intervals.
- **Outcome 3 (LO9):** Distinguish rooted topology, resampling support and alternative sources of gene-tree conflict.
- **Chapter LO coverage:** LO3, LO4, LO9
- **Rubric (20 points):** Score the following categories separately; retain ties and unsupported resolution rather than supplying familiar textbook relationships.
  - **Evidence (8 points; LO3, LO4, LO9):** Award 2 for the full nested tree and ten one-step character counts; 2 for the six-taxon nested score 10 versus constrained score 16 with c3–c8 extra steps identified; 2 for JC distance/date and the rate-sensitivity endpoints (1 each); 2 for tree M's root/outgroup, AB MRCA, polytomy, longest terminal branch and printed support plus the Domains1/2 nesting contrast (1 for M, 1 for domains).
  - **Controls (3 points; LO3, LO4, LO9):** Award 1 for comparing hypotheses on the same six taxa, all ten characters and equal weights; 1 for using C01/O as stipulated outgroups rather than midpoint-rooting by appearance; 1 for varying only the clock rate in the sensitivity comparison while holding observed differences and correction fixed.
  - **Uncertainty (3 points; LO4, LO9):** Award 1 for distinguishing the 3.38–5.64 Ma sensitivity range from a posterior interval; 1 for interpreting 95/100 bootstrap recovery as resampling support, not 95% truth probability; 1 for explaining why identical C11/C12 states and M's polytomy do not resolve ancestry or an additional split.
  - **Mechanism (4 points; LO3, LO9):** Award 1 for a correct Fitch intersection/union explanation of extra steps; 1 for distinguishing rapid branching from ancestral-polymorphism sorting; 1 for distinguishing introgression from ILS; 1 for explaining why the 40/30/30 counts alone cannot uniquely select among these compatible histories or exclude estimation error.
  - **Transfer (2 points; LO9):** In the analysis prompt, award 1 for specifying an additional locus/taxon/model comparison and 1 for explaining what result would favor a gene-flow account over a no-gene-flow coalescent account. “Collect more loci” without a contrasting prediction earns at most 1 point.
<!-- lab-alignment-end -->

## Lab Context: Phylogenetics and the Tree of Life {.unnumbered}

Each complete card is a stated inference problem, not a request to reconstruct a familiar textbook tree from insufficient characters.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Complete synthetic 12-taxon by 10-character matrix; C01 is the outgroup, 0 is ancestral, and characters are stipulated independent and equally weighted. {#tbl:unit_VI_phylogenetics_alignment_and_rubric_map}
| Taxon | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8 | c9 | c10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C02 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C03 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C04 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C05 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| C06 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| C07 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| C08 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| C09 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| C10 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| C11 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| C12 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

: Printed molecular-tree evidence and topology comparison (Newick-like,rootonO). {#tbl:unit_VI_phylogenetics_alignment_and_rubric_map_2}
| Card | Evidence |
| --- | --- |
| M | Root(O:0.10,((A:0.01,B:0.01):0.02,C:0.03,D:0.03):0.07); branch lengths are substitutions/site. AB is recovered in 95/100 site-bootstrap replicates; the ingroup in 80/100. C,D and AB meet at one unresolved node. |
| Domains1 | (Bacteria,(Archaea,Eukarya));Archaea is monophyletic |
| Domains2 | (Bacteria,(Archaea1,(Archaea2,Eukarya)));named archaeal taxa form a paraphyletic grade if Eukarya is excluded |
| Conflict | 100 independent loci: candidate splitAB/CD recovered40 times, AC/BD30 andAD/BC30; branch lengths and calibration not provided |

: Clock and parsimony constants. {#tbl:unit_VI_phylogenetics_alignment_and_rubric_map_3}
| Card | Inputs |
| --- | --- |
| Clock | Synthetic1000-nucleotide alignment:80 differences; JC distance=−.75ln(1−4p/3);lineage-summedrate.02substitutions/site/Myr,sensitivity.015–.025 |
| Fitch | Internal set=child intersection; empty intersection→union and add1 step. Root state is unfixed except for outgroup orientation. |
| Smallsubset | For C01,C03,C05,C07,C09,C11 compare the nested order with C03/C09 as forced sisters; use all10 characters. Identical terminal states do not identify direction of descent. |
| Conflict definitions | Radiation means rapid successive branching; ILS means sorting of ancestral polymorphism across descendant lineages; introgression means gene exchange after divergence. These mechanisms can coexist. |

## Paper-Based Investigation {.unnumbered}

1. Draw the nested12-taxon cladogram and count changes for each character. Compare the forced C03/C09 sister hypothesis on the six-taxon subset; report unresolved ties instead of inventing characters.
2. Calculate the JC clock date and rate-sensitivity range. State why a sensitivity range is not a posterior interval.
3. Read tree M: identify the root, outgroup, MRCA of A/B, polytomy, longest terminal branch and highest printed bootstrap support. Compare Domains1/2 for actual nesting. Evaluate whether the 40/30/30 locus counts uniquely identify radiation, ILS or introgression; design one additional comparison.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Redmond/McLysaght2021 (NatureCommunications,DOI10.1038/s41467-021-22074-7 \citep{redmond2021sponges}) reanalyzed phylogenomicdatasets withmixturemodels/recoding andsupportedsponges-sister,not a long-read proof ofctenophores-first. Thispacketcontains syntheticcharacters/branchlengths,not thatstudy'salignment. Calibrationsandmodels mustaccompanytimeorposteriorclaims;refreshwithnewdata/modeladequacy evidence. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain why the parsimony comparison must use the same characters and weights. Then transfer the Conflict card to a model-design decision: could 40/30/30 split counts alone justify an introgression claim? Specify one additional comparison using locus branch lengths, additional taxa and/or explicit coalescent-with-versus-without-gene-flow models, and state what kind of result would favor gene flow over an ILS-only account. These data are not printed, so propose the comparison without reporting a test result.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: The nested ladder C01,(C02,(C03,(C04,(C05,(C06,(C07,(C08,(C09,(C10,(C11,C12)))))))))) fits all 10 characters with one gain each, totaling 10 steps. On the six-taxon subset, the ladder also costs 10; forcing C03/C09 as sisters conflicts with the derived-state splits in characters 3–8, requiring at least one extra step for each of those six characters. The candidate (C01,(C05,(C07,((C03,C09),C11)))) attains 16 steps: characters 1–2 and 9–10 cost 1 each; characters 3–8 cost 2 each. Thus the constrained minimum is 16, not 10. C11/C12 are identical; neither is identified as the ancestor of the other.
Task2: JC≈0.08459 and the date is≈4.23Ma. Rate sensitivity is≈3.38–5.64Ma, not an HPD interval: only the assumed rate was varied, without a posterior distribution or calibration uncertainty.
Task3: O is the outgroup. The A/B MRCA is the small internal node with a0.02 stem; C,D andAB meet at the polytomy. O has the longest terminal branch,0.10 substitutions/site. AB95% is the highest printed resampling support, not a95% probability that the clade is true. Domains1 makes monophyletic Archaea/Eukarya sisters; Domains2 nests Eukarya within the archaeal radiation. Short successive internodes can produce both a real radiation and ILS; these are not mutually exclusive. Locus counts also depend on estimation error, gene flow and locus independence. Credit coalescent/introgression model comparisons and improved taxon sampling rather than a uniquely asserted cause.

Transfer benchmark: Fit comparable no-gene-flow coalescent and gene-flow models to independent loci with branch lengths and suitable taxon sampling; ask whether gene flow explains topology/coalescence patterns beyond the ILS-only model's expectations. An excess of particular shared-history patterns supported by that comparison could favor introgression, but 40/30/30 counts alone, without error and independence checks, do not. Rapid radiation and ILS can coexist; neither is excluded simply by proposing gene flow.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
