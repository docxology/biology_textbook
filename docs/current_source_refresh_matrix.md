# Historical source-refresh log and maintenance rules

The dated “verified”, “falsified” and completion statements in the May/July 2026 sections are historical author reports, not this edition's live certification. The November section records a narrower evidence correction with explicit access limits. Historical counts/paths/metrics remain attributed to their dated scope; use current config, claim ledger and exact-source receipts for present state.

This matrix records the config-driven source sweep for the renderable
manuscript surface defined by `docs/manuscript/config.yaml`: 2 front-matter files,
11 unit intros, 44 chapters, 44 labs, 44 question banks, and 7 reference
appendices. Perplexity may be used for discovery, but adopted claims require
direct official or peer-reviewed verification before they enter prose,
`references.bib`, or `current_claims.yaml`.

## 2026-11-09 — Bounded ocean-evidence and assessment correction

This is not a new whole-literature certification. The chapter, Q25 prompt/key/rubric, bibliography and two anchored claim records now distinguish measurements, assumptions and extrapolations:

| Evidence lane | Inspected source and retained boundary | Access limit |
| --- | --- | --- |
| Fish sensing and behavior | [Porteus 2018](https://doi.org/10.1038/s41558-018-0224-8) measures European sea-bass olfactory sensitivity; [Clark 2020](https://doi.org/10.1038/s41586-019-1903-y) reports tested reef-fish behavioral outcomes. The [methods comment](https://doi.org/10.1038/s41586-020-2803-x) and [reply](https://doi.org/10.1038/s41586-020-2804-9) retain the comparability dispute, rather than presenting either paper as a species-independent rule. | Original publisher abstracts, metadata, visible figure captions and accessible comment/reply introductions; no raw-data or full-method reanalysis. |
| Experimental adaptation | [Lohbeck 2012](https://doi.org/10.1038/ngeo1441) reports laboratory selection over approximately 500 asexual generations, higher growth and partial calcification restoration under the tested conditions; not natural reef rescue. The [erratum](https://doi.org/10.1038/ngeo1637) corrects Fig3c–f axis scales. | Corrected article abstract/captions and full visible correction notice; no digitization or reanalysis of the corrected figure. |
| Calculation versus observation/scenario | The pH 8.20→8.05 hydrogen-ion example is explicitly supplied arithmetic, not a global observed time series. The [2007 reef review](https://doi.org/10.1126/science.1152509) supplies historical warming/CO2 scenarios, not a current measured 2050 erosion deadline. Saturation state is separated from biological net shell-growth rates. | Native arithmetic smoke plus original review metadata/abstract; no new global pH dataset or carbonate-growth model. |

Active record IDs are `fish-sensory-behavior-scope` and `coccolithophore-culture-adaptation-boundary` in [the claim ledger](manuscript/current_claims.yaml). The [chapter](manuscript/unit_X/ecosystem_ecology.md) supplies the evidence needed by [Q25](manuscript/questions/unit_X/questions_ecosystem_ecology.md); its four-point rubric separately scores risk context, chemistry/rates, matched empirical endpoints and adaptation limits. Structural gates do not certify scientific causation. Publication and archival deposition still require their independent exact-source workflows.

## 2026-07-10 Coverage-Gap Closure (same-day follow-up)

Closed the "process gap, not remediated" note from the pass below:
ClinVar, dbSNP, RefSeq/MANE, and GBIF previously had only bibliography
"accessed" dates with no `current_claims.yaml` row to diff future drift
against. Added the five listed rows:

- `dbsnp-variant-identifier-resource-2026`, `clinvar-variant-disease-archive-2026`,
  `refseq-mane-transcript-reference-2026` — all anchored in the shared
  `docs/manuscript/unit_IV/mutations_and_genomics.md:845` paragraph (the
  sentence already names each resource individually).
- `acmg-amp-variant-classification-2015` — anchored in
  `docs/manuscript/unit_V/mendelian_extensions_and_human_genetics.md:514`,
  tracking the 2015 ACMG/AMP five-tier framework as the current standard
  (ClinGen SVI Bayesian work remains in specification/expert-panel form,
  not a superseding joint guideline, as of this check).
- `gbif-occurrence-infrastructure-2026` — anchored in
  `docs/manuscript/unit_X/biomes_and_conservation.md:934`.

No new prose claims were introduced beyond what the existing sentences
already stated; this pass only gave those existing claims a tracked
evidence_date/checked_as_of/refresh_trigger they lacked before.
`audit_current_claims.py --check` → `claims=56 issues=0`.

## 2026-07-10 Verified Refresh Pass

Multi-lens review (six independent research agents, each adversarially
re-verified by a second agent) checking every tracked lane against live
primary sources ~6.5 weeks after the 2026-05-24 pass. Every "material
change" below was independently confirmed by a re-check pass before
being adopted; several hypotheses were explicitly **falsified** (checked,
found unchanged) and are recorded as such, not silently dropped.

**Adopted (material change, verified against a live primary source):**

- **Casgevy age-eligibility expansion** — FDA supplemental approval
  (2026-07-01) extended exa-cel from 12+ to **2 years and older** for SCD
  and transfusion-dependent β-thalassemia. Updated
  `docs/manuscript/unit_IV/mutations_and_genomics.md`,
  `docs/manuscript/unit_VII/bacteria_archaea_viruses.md`, `references.bib`
  (`fda2026casgevy`), and both `casgevy-*` ledger rows.
- **GTDB R10-RS226 → R11-RS232** (15 Apr 2026) — genome/species/genus
  counts in `docs/manuscript/unit_VII/microbial_ecology.md` and the
  `gtdb-r10-rs226-2025` ledger row updated to the live release figures
  (901,341 total genomes; 878,998 bacterial / 22,343 archaeal).
- **IUCN Red List 2025-2 → 2026-1** (9 Jul 2026) — assessed/threatened
  counts in `docs/manuscript/unit_X/biomes_and_conservation.md` (two sites)
  and the `iucn-red-list-2025-2` ledger row updated (172,620→175,909
  assessed; 48,646→49,505 threatened); `references.bib` `iucn2025redlist`
  entry re-pointed to the live summary-statistics page.
- **BRENDA Release 2026.1** (4 Mar 2026) — `brenda-2026-enzyme-resource`
  ledger row's `evidence_date`/`checked_as_of` bumped; prose makes no
  version-specific claim so was left untouched (nothing to correct).
- **UniProtKB reference-proteome restructuring** (underway, release
  2026_02) — added one hedged caveat sentence to
  `docs/manuscript/unit_I/macromolecules.md` noting the restructuring without
  asserting the unconfirmed completion date or accession counts a first
  draft of this finding claimed (adversarial re-check downgraded
  "finalized... 253M→141M" to "in progress, magnitude unverified" — the
  corrected, hedged version is what shipped).

**Checked and falsified (hypothesis explicitly rejected — no edit):**
AlphaFold DB complexes, wwPDB/PDBe/EMDB entry counts, WHO BPPL 2024, WHO
GLASS 2025, CITES CoP20 (already covered by evidence_date), IPBES
(2016 pollinator + 2019 global) estimates, Lyfgenia, HPRC Release 3
(not yet published), RNAcentral release 26, NAR Database Issue 2026,
ClinVar/dbSNP/RefSeq/MANE, ACMG/AMP (Richards 2015), KEGG and BioCyc
(newer releases exist but no version-specific manuscript claim to
correct).

**Process gaps found, not remediated this pass (recorded for a
follow-up, not invented as new ledger scope today):** ClinVar/dbSNP/
RefSeq/MANE/ACMG-AMP variant-interpretation claims and GBIF have no
dedicated `current_claims.yaml` rows — only bibliography "accessed"
dates — so future drift on those lanes has nothing to diff against.

**Test-infrastructure fix (root cause, not content):**
`tests/test_current_claims_ledger.py::test_current_claims_ledger_is_valid`
hardcoded `today=date(2026, 5, 25)`, freezing the freshness gate to the
v1.0 release date so it could never again detect real staleness. Changed
to `today=date.today()`, matching the production script's own default
(`scripts/audit_current_claims.py` already called
`validate_current_claims()` with no `today` override).

## 2026-05-24 Section-Title and Scholarship Pass

- **Source-section heading contract tightened:** all 44 configured chapters now
  use chapter-specific source H2s: `## Current Evidence and Frontier Biology:
  <Chapter Title>`, `## Further Reading and Source Notes: <Chapter Title>`,
  and `## Companion Source Module: <Chapter Title>`. The quality audit fails
  if any bare generic source H2 returns in a configured chapter.

**Current contract, 2026-11-08:** ordinary authored section titles should describe their actual content. The three source-section heading prefixes above are still consumed as ownership/identity by enrichment, audits, and tests; preserve them and their canonical chapter-title suffixes until an explicit atomic protocol migration updates every consumer. Canonical H1s and semantic IDs remain stable. Mechanical normalization is not semantic editorial review.

- **Six targeted scholarship lanes added:** protein/structure provenance
  (UniProt, wwPDB, PDBe, EMDB), enzyme/pathway governance (BRENDA 2026, KEGG,
  BioCyc), clinical variant interpretation (ClinVar, dbSNP, RefSeq, MANE),
  AMR surveillance (WHO GLASS 2025 plus BPPL), biodiversity occurrence data
  (GBIF plus IUCN/IPBES), and clinical-trial translation (ClinicalTrials.gov
  plus FDA Casgevy/Lyfgenia).
- **Ledger scope kept narrow:** new current-claim rows were added only for
  `brenda-2026-enzyme-resource`, `who-glass-2025-amr-surveillance`, and
  `lyfgenia-gene-therapy-approval`; static database-homepage descriptions were
  cited without adding numeric homepage counts.
- **Assessment and lab surfaces refreshed in place:** targeted source-card
  materials and existing question prompts were upgraded without adding new
  labs, question items, chapters, registered figures, or registered Mermaid
  factories.
- **Follow-up guardrails added:** configured labs use chapter-specific `Lab
  Context: <Chapter Title>` headings, the legacy further-reading inserter emits
  the specialized source-note H2, and the aggregate readiness check uses
  temporary visual artifacts for default review runs.

## 2026-05-23 Implementation Pass

- **Reported historical lab scope:** the 2026-05-23 account below described 39 labs; this is not the current 44-lab inventory. Those reported materials include a
  paper source-governance card and a source-governance checkpoint that asks
  students to record source type or model snapshot, evidence date/version,
  stability, and a refresh trigger before writing conclusions.
- **Source anchors aligned:** the HPRC Release II current claim now points to
  the direct HPRC Data Release 2 page, and the AlphaFold complex-release claim
  now points to the direct EMBL-EBI technology article. Both bibliography rows
  carry 2026-05-23 access dates.
- **Visual policy preserved:** no new `ALL_FIGURE_GENERATORS` entries or
  registered Mermaid factories were added. Existing inline Mermaid captions and
  alt text were tightened where they were generic, duplicative, or missing
  decision provenance.
- **Diagram-count reconciliation:** the renderable manuscript surface contains
  196 inline Mermaid fences when README/AGENTS files are excluded; this pass
  keeps visual-manifest totals derived from the live figure and diagram scan.

## 2026-05-22 Completion Pass

- **Reported historical scope:** the 2026-05-22 account described 137 surfaces and asserted inventory gating. Do not reinterpret that dated count as the present configured inventory; current source admission and tests must use current config.
- **Scholarship defects fixed:** moved the Casgevy 15-year monitoring citation
  into the paragraph that makes the claim; moved the IPBES 1-million-species
  citation into the table row that makes the claim; refreshed the Casgevy
  current-claim URL to the FDA CASGEVY product page and aligned the evidence
  date with the page's 2026-03-26 current-as-of date.
- **Durable gates added:** `validate_current_claims()` now requires each
  ledger citekey to appear in the same paragraph or table block as its
  `anchor_text`; `audit_textbook_quality.py` now catches bare `\ref{...}`,
  `\eqref{...}`, and `\autoref{...}` rendered-reference commands and verifies
  the whole registered surface inventory.
- **Cross-reference result:** no hard-coded student-facing section, figure, or
  equation references were left in prose; generated titles, metadata badges,
  and marker-owned planning tables remain governed by the synchronization
  scripts rather than hand-authored prose.
- **Deferred questions:** no new biology claims were added in this pass. A
  future release-readiness pass may add live URL checking for every
  `current_claims.yaml` URL, but this pass kept network-dependent checks out of
  the test suite.

| Surface | Files | Refresh focus | Reported historical outcome |
| --- | ---: | --- | --- |
| Front matter and preface | 2 | Reader contract, source-governed claims, semantic navigation | No new current-science claim needed; retain generated navigation checks. |
| Unit intros | 11 | Current Evidence Thread language, cross-unit references, Mermaid metadata | Retain evidence-thread structure; Mermaid metadata normalized by `scripts/add_mermaid_alt_text.py --check`. |
| Core chapters | 44 | Fast-moving examples, citation closure, current-claim ledger anchors | Retain refreshed pangenome, AlphaFold, AMR, malaria, IUCN, CITES, climate, conservation, RNAcentral, GTDB, plant-pangenome, brain-cell-atlas, and human-genetics evidence lanes. |
| Labs | 44 | Paper-based evidence work, source cards, no hidden data/notebook dependency | Keep source-governance cards and table captions synchronized with the chapter evidence lanes. |
| Question banks | 44 | Chapter-grounded answers, no generated scaffolds, current-source transfer | Keep assessment transfer grounded in chapter evidence without changing the 30-question invariant. |
| Reference appendices | 7 | Glossary/index links, semantic appendix references, no hard-coded rendered numbers | No content refresh needed; keep `link_glossary.py --check` and crossref gates authoritative. |

## Priority sources reported directly verified in the dated pass

| Lane | Source used | Manuscript handling |
| --- | --- | --- |
| Molecular databases and omics | 2026 *Nucleic Acids Research* Database Issue introduction (`10.1093/nar/gkaf1427`) | New Unit IV source-governance paragraph, lab card, question-bank reasoning, BibTeX entry, and current-claim ledger row. |
| RNA databases | RNAcentral in 2026 (`10.1093/nar/gkaf1329`) | New Unit IV non-coding-RNA database-governance paragraph, gene-expression question-bank reasoning, BibTeX entry, and current-claim ledger row. |
| Microbial taxonomy and MAGs | GTDB R10-RS226 (`10.1093/nar/gkaf1040`) | New Unit VII microbial-taxonomy release paragraph, resistome question-bank reasoning, BibTeX entry, and current-claim ledger row. |
| Plant pangenomics | Plant pangenomes for crop improvement, biodiversity and evolution (`10.1038/s41576-024-00691-4`) | New Unit VIII crop-breeding pangenome paragraph, plant-reproduction question-bank reasoning, BibTeX entry, and current-claim ledger row. |
| Pollination services and pollinator risk | IPBES pollinators assessment plus wild-pollinator crop synthesis (`10.1126/science.1230200`) | New Unit VIII pollination prose, Unit X conservation interpretation, BibTeX entries, and current-claim ledger row for dated IPBES crop-pollination figures. |
| Systems biology scale checks | Systems biology in the single-cell era (`10.1038/s41576-025-00821-6`) plus scale-free network tests (`10.1038/s41467-019-08746-5`) | Unit 0 systems-science prose now distinguishes hub-heavy structure from strict scale-free claims and ties systems claims to perturbation/validation evidence; no dated current-claim row needed. |
| Homeostasis concepts | Situating homeostasis in organisms (`10.1113/JP286883`) | Unit IX homeostasis prose now frames set points as shorthand within organism-level regulation; no dated current-claim row needed. |
| Global photosynthesis measurement | Terrestrial photosynthesis inferred from plant carbonyl sulfide uptake (`10.1038/s41586-024-08050-3`) | Unit III photosynthesis now distinguishes leaf, canopy, and planetary carbon-flux evidence; no numeric GPP estimate adopted, so no current-claim row needed. |
| Brain cell atlases | NIH BRAIN/BICCN mouse-brain atlas and Nature whole-mouse-brain atlas (`10.1038/s41586-023-06812-z`) | New Unit IX atlas-as-release paragraph, nervous-system question-bank reasoning, BibTeX entries, and current-claim ledger row. |
| Human genetic interpretation | Saturated height-GWAS map (`10.1038/s41586-022-05275-y`), ACMG/AMP variant-interpretation guidance (`10.1038/gim.2015.30`), ClinVar (`10.1093/nar/gkt1113` plus NCBI), OMIM (`10.1093/nar/gky1151`) | Unit V human-genetics prose now separates polygenic maps, variant classification, public clinical archives, and curated Mendelian gene-phenotype resources; the height-GWAS count is tracked in `current_claims.yaml`. |
| Pangenomics | Human Pangenome Reference Consortium Data Release 2 page | Existing Unit IV pangenome prose and claim ledger retained, with the Release II URL and evidence date aligned to the direct release page. |
| Protein resources | AlphaFold DB 2025 NAR update plus 2026 EMBL-EBI complex announcement | Existing Unit I protein-modeling prose and claim ledger retained, with the complex-release URL aligned to the direct EMBL-EBI article. |
| AMR and pathogens | WHO BPPL 2024 and existing CDC/WHO clinical pages | Existing Unit VII AMR/current-claim coverage retained. |
| Conservation and climate | IUCN 2025-2 summary table, CITES appendices, IPCC/IPBES/CBD/FAO sources | Existing Unit X source-governed conservation coverage retained. |
| FDA/CDC/WHO biomedical examples | Existing FDA, CDC, WHO, NCI, and disease-surveillance entries already under current-claim review | No additional biomedical example adopted in this completion pass; the active ledger already covers genome-editing therapies, immunotherapy, fungal AMR, TB, malaria, AMR, PrEP/UNAIDS, and related public-health lanes. |

## Refresh Rules

- Add a current-claim ledger row only when a claim is fast-moving and appears in
  renderable prose with a nearby citation key.
- Prefer descriptive prose and `\cref{...}` over rendered numbers or local
  ordinal references.
- Treat database counts, clinical approvals, surveillance lists, conservation
  counts, and model-resource releases as dated claims with explicit refresh
  triggers.
- Keep generated artifacts under `output/` out of source patches unless a
  publication artifact refresh is explicitly requested.

## 2026-11-09 bounded ecosystem-inference review

This pass independently reviewed the complete ecosystem chapter, paired question bank, finite paper lab and relevant glossary/citation consumers. It is not fresh certification of every neighboring chapter, all cited literature or raw data. The existing finite lab packet is preserved; its combined N+P treatment does not isolate N from P limitation. No new empirical dataset or experimental measurement is claimed.

| Source and access | Supported correction and boundary |
| --- | --- |
| Geider & La Roche (2002), `10.1017/S0967026201003456`: institutional abstract/metadata; full PDF unavailable. Ptacnik et al. (2010), `10.1007/s10021-010-9380-z`: original publisher methods/results | Cellular stoichiometry varies; measured nutrient fractions and response endpoints matter. Bioassay-derived Baltic thresholds are not universal substitutes for 16. The new 8:1/16:1 quota example is explicitly stipulated, not measured taxa. |
| van den Berg et al. (2016), `10.3389/fmicb.2016.01842`: original methods/results/discussion; Duval et al. (2013), `10.1073/pnas.1311218110`: primary abstract and stoichiometry | Available acetate relative to nitrate in a specified anaerobic enrichment supports donor-context guidance, not an invariant sediment C:N rule. Nitrogenase's limiting ATP bookkeeping does not establish an all-reactions energetic ranking. |
| Fowler et al. (2013), `10.1098/rstb.2013.0164`: primary full-text global-budget sections | Biological, industrial and other new reactive-N inputs are separate from transfers and stocks. Its dated synthesis is not adopted as a 2026 measured budget; the diagram drops untraced annual/uptake labels rather than relabeling them as observations. |
| Hupp et al. (2022), `10.1073/pnas.2115561119`: primary methods/results/discussion; Frieling et al. (2016), `10.1073/pnas.1603348113`: independently reviewed original thermogenic-vent study | Benthic extinction differs from local planktic disappearance and migration. Dated thermogenic release supporting modeled PETM prolongation is not evidence of hydrate-driven initiation. No universal modern release forecast is introduced. |
| Costanza et al. (2014), `10.1016/j.gloenvcha.2014.04.002`: institutional accepted manuscript, especially valuation assumptions and limitations | Correct journal and distinguish 2011 ecosystem reference from 2007-dollar/PPP unit-value accounting. Neither observed tripling of physical services nor a nominal-2024 GDP ratio follows. Policy effectiveness needs outcome evidence and a counterfactual. |
| MEA (2005) official Condition and Trends summary; existing IPBES (2019) assessment | MEA's 15/24 examined services degraded or used unsustainably is not a land/ocean-area fraction. The endpoints cannot be read as successive updates to one percentage. Full MEA-volume reanalysis is not claimed. |
| van der Ent et al. (2014), `10.5194/esd-5-471-2014`: original metric definitions, methods and results | Distinguish transpiration, interception/direct evaporation, precipitation-origin and evaporation-destination metrics. Removed untraced oak-day and universal forest-rainfall percentages; no replacement universal fraction or tipping threshold is asserted. |
| USGS *Mineral Commodity Summaries 2026*, `10.3133/mcs2026`: official phosphate sheet, report version history and reserve definitions | World 73 billion metric tons and Morocco table entry 50 billion refer to marketable phosphate rock. Version 1.3 is dated 27 May; the phosphate sheet is dated February and listed revisions concern other commodities. The current-claim row preserves version/date/unit provenance, dynamic reserves and the absence of an exhaustion forecast. |
| Richardson et al. (2023), `10.1126/sciadv.adh2458`: original PMC framework definitions, control-variable table, results and methods; publisher fetch refused | The six-of-nine count is explicitly the 2023 assessment, not current surveillance. The paired question separates annual creation of reactive N from retention/removal of N already fixed, and precautionary boundaries from certain singular tipping thresholds. No current global boundary-count update or raw model rerun is claimed. |
| Barton et al. (2012), `10.4319/lo.2012.57.3.0698`: original full methods, endpoint definitions, results and Figure 5; Barton et al. (2015), `10.5670/oceanog.2015.38`: full original account and treatment/monitoring tables | The 2009 Oregon intake-chemistry association is record-based and endpoint-specific, not a randomized acidification experiment. Figure 5 distinguishes relative production from days-to-size; the original abstract's blanket sign wording is not adopted as one slope for every endpoint. The 2015 account documents local monitoring, timing and sodium-carbonate management with continuing constraints, not a worldwide industry valuation, a 2100 calcification percentage or proven success in natural populations. |
| Pastorello et al. (2020), `10.1038/s41597-020-0534-3`: original CO2-processing, flux-partitioning, technical-validation and usage-limit sections | Turbulent plus storage fluxes contribute to NEE; GPP/respiration are model-derived partitions. Filtering, gap filling, quality flags, method choice and site-specific uncertainties matter. The dated dataset is not a current network census. Untraced tower-count, all-model, and Harvard Forest percentage/duration guarantees are withdrawn rather than replaced with invented measurements. |

The new oxygen calculation is a closed, no-resupply teaching inventory: potential demand exceeds available oxygen, reaching 2 mg/L after 2.25 g C/m³ oxidation and zero after 3 g C/m³. It supplies no kinetics, negative-oxygen state, whole-input aerobic oxidation or empirical hypoxia time. Corresponding LO/review/key/rubric changes preserve stable chapter, equation and table IDs. Actual source, gate and rendered-output results belong in source-bound receipts, not this dated review account.

The printed-page review also corrected trophic energy sources, the nitrification definition, the ocean concept check, and Q3/Q6/Q8/Q16/Q17 question-key-rubric alignment. The replacement NPP-allocation fractions and four-treatment Q16 biomass values are newly stipulated teaching inputs, not relabeled biome measurements or changes to the finite lab packet. Independent refutation also closed the remaining allocation Key Terms/review-question consumers and removed a duplicate eddy-covariance term. Equal ANPP needs a stated allocation fraction to infer NPP; production and a fraction of NPP do not determine soil carbon stocks or a fraction of GPP. The ocean exercise changes specified net uptake within the synthetic budget with other flows held fixed; it does not identify the solubility pump or calculate climate warming. This bounded review does not freshly validate the neighboring FACE percentage/concentration generalization, global hydrological-flux magnitudes, solar/nutrient-recycling percentages, final-summary Hubbard Brook/biological-pump magnitudes, every cited study, or raw observational datasets.

## 2026-11-09 residual solar, watershed and export-boundary review

This targeted read-only research and separate adversarial/completeness pass addressed the previously named efficiency, FACE, nutrient-retention, water-budget and biological-export gaps. It is not a new literature census or a claim that every neighboring percentage was checked. Software 2.0.0 and manuscript 1.1 remain unreleased candidates; actual source/index, gate, print, package and release state belong in fresh receipts.

| Source and actual access | Correction and limit |
| --- | --- |
| Blankenship et al. (2011), `10.1126/science.1200165`: complete author-hosted article | The ideal roughly 12% glucose-production limit is explicitly full-spectrum and free-energy based; a PAR-only correction was rejected. Annual harvestable-biomass combustion energy and the dated component-based HHV PV/electrolysis estimate have different products/time bases. The 54-absorbed-photon and four-electron redox examples are preserved, not overwritten by an older crop model. |
| May et al. (2015), `10.1038/ncomms9286`: complete primary performance, figure captions and methods | Initial 14% unassisted two-electrode STH under stated AM1.5G illumination differs from assisted photoelectrode performance. Separate, partly potentiostatic stability tests do not establish 14% unbiased operation sustained for 16–40 hours, an annual yield or a current class record. Unsupported copper/cyanobacteria/methanol class percentages are withdrawn, not declared impossible or relabeled as measurements. |
| Norby et al. (2005), `10.1073/pnas.0509478102`: full primary methods/results; Norby et al. (2010), `10.1073/pnas.1006463107`: primary abstract | The 2005 response is regression-predicted at median ambient NPP in selected young temperate closed-canopy forests, achieved 550 versus 376 ppm. The 2010 decline is over time at the same 550-ppm treatment, not above a universal concentration threshold. It does not prove that mature forests or all long-term treatments cannot respond. |
| Likens et al. (1970), `10.2307/1942440`: original abstract via OSTI; investigator Watershed 2 chronology | The replacement table reports concentration ratios and relative annual flow, not unavailable original mass-output rows. The site explicitly records cut-and-leave treatment in late 1965 and herbicide seasons 1966–1968; the paper's two-year observation summary does not refute the three treatment seasons. Original absolute export tables were not retrieved, so their numbers are not claimed disproved. |
| Likens et al. (1967), `10.2307/1933735`: primary cation-budget abstract; Bormann & Likens (1967), `10.1126/science.155.3761.424`: original methods record | Precipitation and streamwater budgets have element/year boundaries and weathering contributions. Their counterexample rejects a universal precipitation-input-retention interpretation, not high internal recycling under a separately specified boundary. A residence time alone does not determine internal recycling flux. |
| Trenberth et al. (2007), `10.1175/JHM600.1`: full primary global-budget section | The coherent rounded replacement uses dated precipitation estimates, compiled oceanward discharge and residual evapotranspiration/evaporation. Only the precipitation component is assigned the 1988–2004 GPCP period. Closure and temporal sampling errors are not independent measurement of every row or total uncertainty; the older conserved table was not declared arithmetically false. |
| Henson et al. (2019), `10.1029/2018GB006158`: full primary synthesis/methods; Parekh et al. (2006), `10.1029/2005GL025098`: complete original model paper | Particle export needs depth/area/time matching and is distinct from all-pathway export or durable storage. The retained almost-200-ppm statement is attributed to the idealized-model literature discussed by Parekh, not its own 181-ppmv no-dust case or an observed modern increment. Original 1987 fitted Martin data and full 2022 pump-model methods were not reanalyzed. |
| Driscoll et al. (2001), *Acid Rain Revisited*, investigator-authored Science Links report: chronology/monitoring and the dated effects summary, pp. 2, 4–5 and 7 | Wet-deposition monitoring began in 1963, including rain/snow chemistry; this is not a first-discovery priority or a date inferred from one streamwater calcium trend. The same report distinguishes reduced emissions/deposition from continuing impairment and chemical versus biological recovery. The neighboring unscoped pH cutoff/completed-reversal narrative is replaced with those dated endpoints, not a current recovery claim. These adjacent passages were examined after the independent residual review, not silently included in its earlier clearance. |

Chapter review, Key Terms, summary and concept-check consumers migrate with the corrections. The paired finite synthetic ecosystem lab/question datasets and photosynthesis photon/ATP labs remain intentionally unchanged: they do not reproduce the withdrawn historical or technology-class numbers. The chapter's stipulated Martin exercise asks for flux below a specified depth and the additional evidence needed for duration, not a durable-storage ranking. Historical named cases create no new claim to a current record; existing current-claim anchors remain applicable.

The qualitative acid-deposition Q18 key follows the same condition-dependent fish/soil mechanisms rather than importing fixed rain or species-disappearance cutoffs. Its four-point rubric assigns one point to each asked pathway/consequence; exposure qualifiers are teaching context, not hidden numerical scoring requirements. The nutrient-budget table's inherited acid-rain caption is corrected while retaining its stable table identifier, and its ecosystem examples are explicitly relative-budget illustrations rather than measured zero-exchange classifications.

Still unexamined in this bounded pass: neighboring productivity/fisheries magnitudes, carbonate-compensation depth, global phytoplankton NPP fraction and broader artificial-catalyst performance. No blanket clearance follows from correcting the selected boundaries.

## 2026-11-09 clinical inference and antibiotic-target review

This separately surfaced boundary review was not part of the earlier ecosystem clearance. Two independent clinical/metric lenses, two disjoint biochemical lenses and a separate mitigation/refutation pass examine the affected cell-theory and bacterial chapter boxes, pathway graphic/atlas, summary/terms/review consumers, paired Gram-stain key, glossary and original sources. Scope is mechanism and inference, not a current prescribing formulary, all-species drug census, clinical recommendation or new experimental dataset. Actual native checks and printed/artifact acceptance remain source-bound receipts, not conclusions from source inspection.

| Source and actual access | Correction and limit |
| --- | --- |
| CDC MRSA laboratory page, updated 27 June 2025: official mechanism/testing text | MRSA/PBP2a is a counterexample to Gram-positive susceptibility guarantees. Historical breakpoint tables and a purported exhaustive current exception list are not adopted. Identification, phenotype and susceptibility remain different endpoints. |
| WHO *Guidelines on meningitis diagnosis, treatment and care* (10 April 2025): official scope, CSF-investigation/culture sections and treatment-timing recommendations | The scope is acute community-acquired disease in children older than one month, adolescents and adults. Suggestive diplococci, integrated diagnostics and susceptibility testing do not supply a morphology-only regimen; diagnostic delays must not delay indicated empiric treatment. No guideline table/regimen is reproduced and neonatal/health-care-associated scope is not implied. Two new ledger rows track this guidance and the CDC laboratory boundary. |
| McComas et al. (2003), `10.1021/ja035901x`: original abstract | Defined precursor-analog binding distinguishes hydrogen-bond loss from repulsive lone-pair contributions. It supplies neither a universal MIC fold-change nor a fixed energy for each hydrogen bond; full assay methods were not inspected. |
| Foucault et al. (2010), `10.1073/pnas.1006855107`: original main-text results, competition/colonization tables and discussion | VanB/Tn1549 carriage and induced/constitutive expression have condition- and background-dependent costs. This is not a universal zero-cost statement, a numerical VanA estimate or a human-outcome trial. The previous origin narrative is withdrawn without substituting an unverified first-case history. |
| CUBICIN RF prescribing information, March 2025: official sections 1.1–1.5, 5.9 and 12.4 | Membrane action differs from precursor recognition, but nonsusceptible isolates occur. In-vitro enterococcal activity is not identical to an established clinical indication. No new dose, regimen, prevalence or clinical success rate is asserted. |
| Benson et al. (1997), `10.1021/bi962220o`, and Fenn et al. (2003), `10.1021/bi027022d`: original abstracts; Batson et al. (2017), `10.1038/s41467-017-02118-7`: original structural/solution-phosphorylation results and methods | MurB reduces a sugar-bound enolpyruvyl group, not free lactate. Alr's PLP-derived adduct differs from phosphorylated cycloserine bound in *E. coli* DdlB; neither supports covalent attachment to protein residues of both enzymes. Purified-enzyme endpoints are not clinical potency constants. |
| Chung et al. (2013), `10.1126/science.1236501`, and Hakulinen et al. (2017), `10.1038/nchembio.2270`: original abstracts | MraY transfers phospho-MurNAc-pentapeptide, not merely a free pentapeptide. Tunicamycin is a selected structural research example. No shared MurC–F inhibitor class, unnamed inhibitor or unverified current development inventory is retained. |
| Economou et al. (2013), `10.1073/pnas.1308268110`: original structure, membrane-binding and permeability results/methods | Bacitracin binds the carrier pyrophosphate rather than directly inhibiting a uniquely assigned recycling phosphatase. The crystal uses a shortened ligand and membrane assays include C55-PP; neither establishes a universal binding constant, carrier exhaustion or membrane disruption at each inhibitory dose. |
| Sham et al. (2014), `10.1126/science.1254522`: original main text and ColM/spheroplast control figures; Lee et al. (2016 issue; online 2015), `10.1021/jacs.5b11807`: original main text and cellular/substrate-assay figures | MTSES inhibition of engineered *E. coli* MurJ is a transport experiment, not a general drug. Lysobactin's *S. aureus* results support Lipid II substrate sequestration and impaired surface utilization, not MurJ inhibition or proof of cytoplasmic trapping from total-lipid accumulation. Supporting-information preparations and all-species sidedness were not independently reanalyzed. |

The finite stain/CFU/HGT paper lab, paired pathway-target key and already-qualified MRSA question/key do not contain the false dual-covalency or lysobactin/MurJ claims and remain intentionally unchanged. No reverse Gram-based severity ranking replaces the withdrawn premise. Stable chapter/glossary/table IDs and the thirty-question structure are preserved; current clinical guidance and static historical mechanism experiments remain separate maintenance surfaces. The neighboring scientific gaps explicitly listed above are not cleared by this pass.


## 2026-11-10 (UTC) printed cell-plan, archaeal and cytoskeletal evidence review

A technically passing rendered candidate exposed further scientific inference errors during actual page inspection. Separate RNAP/drug and genome/chromatin lenses, a separate lipid/physiology versus Asgard lens, and independent mitigation/completeness refutation examine the affected cell-theory, gene-expression, phylogenetics and microbiology prose, tables, diagram, glossary and paired keys. Source changes require fresh native technical and printed-output proof; the earlier passing candidate is not evidence for this revision. The adversarial reader can quote authoritative teaching prose or a hidden grading premise without write access; the principal boundary is observation versus a domain-wide or historical inference, not an alleged malicious author.

This log heading uses UTC. Claim-ledger review dates follow the validator's local calendar date (9 November at this review instant); no future-date allowance or clock override is introduced.

| Source and actual access | Correction and limit |
| --- | --- |
| Minakhin et al. (2001), `10.1128/JB.183.1.71-76.2001`: full relevant reconstitution/rifampin results and Fig. 4; `10.1073/pnas.98.3.892`: abstract and introductory evidence; Jun et al. (2014), `10.1038/ncomms6132`: RNAP preparation/structure results and 4QIW assembly | Specify chains, types and preparation. The common omega-containing *E. coli* core has five chains/four types; historical or active omega-free four-chain descriptions are not arithmetically wrong, and sigma forms an initiation holoenzyme. The characterized eleven-chain archaeal enzyme defeats a universal twelve-plus minimum, not every historical twelve-chain preparation. Omega dispensability is condition-dependent; introductory references are not all new experiments in that paper. |
| Fraser et al. (1997), Heidelberg et al. (2000), Matsunaga et al. (2003), Hawkins et al. (2013), Kuhsel et al. (1990), Sugahara et al. (2008): primary abstracts | Named linear/multipartite genomes, single-origin archaeal replication and variable tRNA introns refute universal cell-plan inventories. The engineered origin-deletion strain does not show that wild archaea generally lack origins. Chromosome topology, origin number, genome copy number and plasmid form are distinct variables; the paired binary-fission explanation now specifies *E. coli* and an idealized growth model. |
| Hocher et al. (2023): full main Results/Discussion; Mattiroli et al. (2017): full primary text/figures; Guo et al. (2008): abstract/introduction | Selected bacteria have genuine histones, archaeal chromatin proteins vary, and variable-length archaeal assemblies are not identical conventional eukaryotic nucleosomes. Core H2A/H2B/H3/H4 histone folds and structurally distinct linker H1 must not be conflated. Genomic assignment, DNA geometry, in-vitro assembly and native cellular organization remain separate endpoints; no complete histone-family census is claimed. |
| Mankin and Garrett (1991), Hansen et al. (2003), Lechner et al. (1988): primary abstracts; Hansen's official structural deposition also inspected | Chloramphenicol inhibited a named archaeon and resistant rRNA mutants occurred. Anisomycin's ribosomal binding differs from diphthamide-dependent EF-2 modification by diphtheria toxin; the latter is not a ribosomal target. A purified target, homolog or domain label does not establish intact-cell uptake, growth susceptibility or a clinical regimen. Scanned methods, all-species drug responses and archaeal toxin-entry experiments were not verified. |
| Komatsu and Chong (1998): primary abstract; Zeng et al. (2019): full relevant main text/figures; Quehenberger et al. (2020): relevant cultivation/results; Caforio et al. (2018): primary abstract | One extended GDGT can span a membrane. Defined PLFE liposomes had low but finite proton permeability; dye leakage depends on packing/charge. These are not water/ATP rankings, an intact-cell ATP-at-100-C experiment, a universal thermal switch or a 113-C isolated-membrane guarantee. Cyclization proteins do not establish instantaneous ring removal, and growth rate also affects lipid composition. A viable engineered hybrid membrane does not reconstruct or date LUCA. |
| Spang et al. (2015): relevant primary genomic text; Zaremba-Niedzwiedzka et al. (2017): abstract/metadata/captions; corrected Eme et al. (2023), its 2026 correction, and Zhang et al. (2025): relevant primary placement/model/correction text | Distinguish the 2015 Loki discovery from the 2017 grouping, genomic homology from a complete endomembrane system, and Asgard-related host ancestry from finer model-dependent placement. The correction removes partially redundant markers and retains the overall findings; it is not a retraction. An unanchored genome census, percent identity and discovery superlative are withdrawn without claiming they were numerically disproved. No genome assemblies, alignments, markers or trees were independently rerun. |
| Imachi et al. (2020): original isolation/syntrophy and hypothetical E3 sections; Rodrigues-Oliveira et al. (2023), Radler et al. (2026): relevant primary cellular experiments; Akıl and Robinson (2018): abstract/captions; Surkont and Pereira-Leal (2016), Hatano et al. (2022), Tran et al. (2026): relevant primary analyses/experiments | Amino-acid-degrading MK-D1 produces H2/formate removed by partners; the initial methane-fed enrichment is not the subsequent cultured substrate. Substitutable co-culture partners, protrusions and slow growth are observed, not engulfment or proved hydrogen delivery through tentacles. Genuine actin-associated cellular structure, dynamic protrusions/crawling and recombinant four-protofilament tubulin must not be erased as mere sequence predictions. Selected purified-protein, cultured-cell and inferred-ancestral endpoints remain distinct. Three frontier-ledger rows track fine placement, recombinant tubulin and current-cell motility. |
| Blöchl et al. (1997), Strahl and Greie (2008), Barry et al. (2006), Darland et al. (1970): primary abstracts; Zaparty et al. (2008): original introduction and paired trophic cultures; official DSMZ cultivation records | Preserve real *Pyrolobus fumarii* growth up to 113 C, regulated halobacterial salt-in and approximate hot/acidic examples. Named *S. solfataricus* P2 has reported optima 80 C/pH 3.2; another strain's 70-C recovery instruction is not a contradictory maximum. *T. tenax* supports autotrophic and heterotrophic growth, with reported optima 86 C/pH 5.6. *Thermoplasma*'s near-59-C optimum is not a genus-wide 60-C ceiling. These are dated organism/condition observations, not current records or universal membrane limits. |
| Saiki et al. (1988), Ponder et al. (2005), Macalady et al. (2004): primary abstracts; Ayala-del-Río et al. (2010), Cario et al. (2015), Daly et al. (2007): relevant primary results; named BacDive culture records | The extremophile table retains all eight teaching categories while separating illustrative conditions from cardinal limits. Taq polymerase is demonstrated, whereas reverse-gyrase absence in *T. aquaticus* was not established. Cold growth does not make every *Psychrobacter* a strict psychrophile. Named pressure-dependent archaeal lipid proportions do not establish the membrane location of apolar unsaturated compounds. Ferroplasma lipid/pH measurements do not measure zero leakage or identify a pump. Radiation experiments distinguish protein oxidation/protection from a generic manganese DNA shield. |
| Löwe and Amos (1998), Ausmees et al. (2003), van Teeffelen et al. (2011), Møller-Jensen et al. (2002), Kühn et al. (2010): primary abstracts; recent Asgard tubulin primary results provide an independent inference check | The FtsZ structure used an archaeal protein despite its historical title. Homology does not identify a bacterial donor of the entire mitotic apparatus; crescentin's IF-like shape role does not prove lamin/cytokeratin ancestry. The unanchored 1.5-billion-year event-order claim is withdrawn, not numerically falsified. In studied *E. coli*, MreB rotation required wall assembly, so coordinated movement does not prove that MreB is the motor dragging the synthases. ParM and bactofilin roles are named-system results, not universal prokaryotic machinery. |

The cell-classification diagram now presents scoped traits rather than a diagnostic checklist or resolved tree. Informative headings and stable authored table/chapter IDs are retained; Q2, Q6, Q15 and Q21 prompts/keys and local concept/review/summary consumers follow the corrected evidence boundaries. Already-qualified questions, finite paper packets and unrelated synthetic datasets remain unchanged. Exact DOI-matched metadata is separate from scientific access; candidate DOI identities that did not match the proposed paper were rejected before bibliography integration.

Explicit remaining limits: no primary Natronobacterium antiporter assay was established after targeted source checks, so the table no longer assigns that specific mechanism to the genus; its row states pH/ion homeostasis without pretending to identify a transporter. No complete taxonomic, cytoskeletal, genome, drug-response, membrane-composition or historical methane-production census was performed. The methane synthesis distinguishes gross biological production, oxidation, atmospheric emissions and CO2-equivalent accounting rather than substituting another unsupported global total. Supplements/raw data, unseen species/endpoints, all neighboring physiology and the previously listed ecosystem/technology gaps are not certified by this bounded review. Rendering, installation, exported reproduction and release state must be demonstrated separately for the actual resulting source.

## 2026-11-10 (UTC) printed molecular and clinical endpoint closure

The rebuilt instructor PDF, not a source-count check, exposed residual claims in adjacent printed passages after the prior native full gate passed. The integration owner actually viewed 24 cellular, molecular, microbiological, paired-answer and reference pages, then commissioned separate primary molecular and clinical reviews followed by independent molecular refutation and a clinical/direct-consumer completeness lens. Passing tests do not clear these scientific statements. Review dates below use the local 9 November calendar for ledger consistency; this heading uses UTC.

| Source and actual access | Correction and retained limit |
| --- | --- |
| Fernández-Tornero et al. (2013): original abstract and original PubMed author list; Armache et al. (2003), Hoffmann et al. (2015): relevant full experimental/results text; Bushnell et al. (2002): full relevant structural methods/results | Yeast 14/12/17 assemblies remain valid, but mammalian product/promoter examples are separately scoped. Complete Pol II versus a ten-subunit core preparation are distinct. An amanitin-binding structure is not an activity curve, cellular exposure or universal sensitivity threshold. The original author list corrects a duplicated name in an upstream metadata index. |
| Schultz and Hall (1976): original scanned pages 1029/1032 and Fig. 4, with p1032 independently viewed by the integration owner; Weil and Blatti (1975): experimental abstract | Retain 1.0-μg/mL yeast Pol II and 10-μg/mL calf-thymus Pol III as preparation-specific 50%-activity endpoints, not comparable intrinsic potencies. Yeast Pol III's high-concentration response directly defeats a universal hierarchy. The machine-readable Schultz abstract says II where the original printed high-concentration sentence says III; the original page controls. No living-cell or clinical dosing conclusion follows. |
| Greber et al. (2015): author-deposited experimental assembly and primary abstract; Smirnova et al. (2001): relevant full primary text; Goldbach et al. (1979), Oldenburg and Bendich (2004): detailed experimental abstracts | Mammalian 55S/DRP1 and named linear/branched mitochondrial/plastid DNA refute universal present-day trait bundles, not bacterial ancestry. Division into two is not itself refuted; circular reference maps do not establish physical topology. Membrane count alone cannot assign every bilayer's historical provenance. Raw structures/molecules and every organelle lineage were not independently reanalyzed. |
| Lawrence and Ochman (1998): full original methods/results | Preserve 755/4,288 ORFs (17.6%) in the historical MG1655 dataset, using composition, codon usage, context and comparative evidence. Similar-composition donors may be missed. This is not a typical-genome census or a uniformly built per-gene phylogeny. Already-qualified HGT and organelle keys/finite labs remain unchanged. |
| Atomi et al. (2004): full relevant culture/topology results; Brochier-Armanet and Forterre (2007 issue): relevant full comparative analysis; Takagi et al. (1997), Cline et al. (1996), Kong et al. (1993), Saiki et al. (1988): experimental abstracts; Vlijm et al. (2015): relevant full experimental/results discussion | A viable reverse-gyrase deletion at 90 C with mutant/host growth-rate ratio 0.46 distinguishes contribution from necessity. Growth, plasmid topology, recombinant KOD's 75-C activity optimum, heat survival and PCR error rates are different endpoints. Preserve Cline's named 1.3e-6/8.0e-6 per-base-pair-per-duplication rates and assay dependence; KOD's mutation frequency is not imported into those units. Negative supercoiling can permit local opening under specified conditions. The unsupported 95/87-C genomic comparison and universal charge/fidelity rules are removed, not experimentally measured false. Takagi/Cline full-PDF access failed; no unseen methods or supplements are claimed. |
| Schooley et al. (2017) and 2018 provenance erratum: original relevant clinical/resistance/correction text; Dedrick et al. (2019): original relevant clinical, immune, isolate-specificity and figure text, independently read by the integration owner | Patterson was treated in 2016; Strathdee was his wife/researcher, not the patient. Recovery during combined care, resistance to original cocktails and reformulation do not identify a phage-alone cure or untreated counterfactual. Dedrick reports improvement with positive lesion cultures, weak binding antibodies but no measured serum neutralization, and isolate-specific activity. One purchased component defeats an all-sewage provenance narrative, not every environmental origin. No current trial-stage census or class-wide regulatory approval is asserted. |
| Jefferson et al. (2005), Walters et al. (2003): relevant original preparations, controls, transport, killing, oxygen and discussion text | Preserve named S. aureus MBC ratios 250–600 under protocols with differing exposures, separate from MIC and diffusion. P. aeruginosa penetration without substantial killing and regained dispersed-cell susceptibility support physiological scope, not a fixed persister fraction. The quoted CDC prevalence denominator and universal diffusion/enzyme multipliers were not established; lack of a traceable source is not proof that no historical estimate exists. No patient regimen follows from these assays. |
| CDC Steam Sterilization page dated 28 November 2023, describing the 2008 guideline; CDC acute-care CDI guidance dated 13 May 2026: original official pages actually read by the integration owner | Sterilizer/load/contact/monitoring scope defeats one universal 15–20-minute recipe. CDI prevention combines contact precautions, recommended hygiene, appropriate sporicidal environmental products and stewardship, not unconditional soap/bleach wording. These source-defined conditions are not dismissed as invalid; the textbook is not a validated process instruction. Both guidance surfaces receive refresh-triggered ledger records. |

The phage/biofilm exposition, glossary/key terms, summary, concept/review prompts and Q19 key now share the same causal boundaries. Toy ODE, independence and galU scenarios are explicitly stipulated, not patient observations or proof of synergy. Valid primary quantities, existing finite labs, stable table/chapter identifiers and thirty-item banks are retained. Actual printed findings also drive the narrow split-word header and protected-title fixes; compilation alone cannot accept their typography.

Independent clinical completeness refutation found two surviving portable consumers: the central Biofilm glossary multiplier and unqualified clinical-challenge/key-term phage thresholds. Both are migrated to endpoint-specific and explicit toy-ODE definitions. Component purchase and original ecological isolation are also distinguished: the 2018 erratum identifies a DSMZ purchase rather than Navy-team isolation, not the unknown original environment of every component. Molecular refutation retained the named counts, assays, ratio direction and organelle counterexamples without a new universal opposite claim. These are bounded review judgments, not measured exploitability or a full-corpus scientific certification.

Explicit limits: no full clinical raw-data reanalysis, supplement audit, registry/current-stage or prevalence census, enzyme-product leaderboard, complete promoter/rRNA-processing experiment review, taxonomic survey or general persistence-mechanism census. Neighboring QS circuit inventories, T4 kinetics, secondary-plastid evolutionary details, remaining pathogen/model assumptions and previously recorded ecosystem/technology gaps are not silently certified by this bounded pass. Current-source native checks, downstream package/bundle reproduction and fresh actual-page review remain required after integration; these source-access notes are not a release or publication receipt.

