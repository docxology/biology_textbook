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
| Driscoll et al. (2001), *Acid Rain Revisited*, investigator-authored Science Links report: full chronology/monitoring and effects sections, especially pp. 2 and 7 | Wet-deposition monitoring began in 1963, including rain/snow chemistry. This does not equate a later streamwater calcium trend with discovery or claim a first-discovery priority. The report's historical discussion of 1970/1990 policy is not a current recovery assessment. This adjacent claim was examined after the independent residual review, not silently included in that earlier clearance. |

Chapter review, Key Terms, summary and concept-check consumers migrate with the corrections. The paired finite synthetic ecosystem lab/question datasets and photosynthesis photon/ATP labs remain intentionally unchanged: they do not reproduce the withdrawn historical or technology-class numbers. The chapter's stipulated Martin exercise asks for flux below a specified depth and the additional evidence needed for duration, not a durable-storage ranking. Historical named cases create no new claim to a current record; existing current-claim anchors remain applicable.

Still unexamined in this bounded pass: neighboring productivity/fisheries magnitudes, carbonate-compensation depth, global phytoplankton NPP fraction and broader artificial-catalyst performance. No blanket clearance follows from correcting the selected boundaries.
