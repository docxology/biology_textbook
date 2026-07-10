# Current Source Refresh Matrix

This matrix records the config-driven source sweep for the renderable
manuscript surface defined by `manuscript/config.yaml`: 2 front-matter files,
11 unit intros, 44 chapters, 44 labs, 44 question banks, and 7 reference
appendices. Perplexity may be used for discovery, but adopted claims require
direct official or peer-reviewed verification before they enter prose,
`references.bib`, or `current_claims.yaml`.

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
  `manuscript/unit_IV/mutations_and_genomics.md`,
  `manuscript/unit_VII/bacteria_archaea_viruses.md`, `references.bib`
  (`fda2026casgevy`), and both `casgevy-*` ledger rows.
- **GTDB R10-RS226 → R11-RS232** (15 Apr 2026) — genome/species/genus
  counts in `manuscript/unit_VII/microbial_ecology.md` and the
  `gtdb-r10-rs226-2025` ledger row updated to the live release figures
  (901,341 total genomes; 878,998 bacterial / 22,343 archaeal).
- **IUCN Red List 2025-2 → 2026-1** (9 Jul 2026) — assessed/threatened
  counts in `manuscript/unit_X/biomes_and_conservation.md` (two sites)
  and the `iucn-red-list-2025-2` ledger row updated (172,620→175,909
  assessed; 48,646→49,505 threatened); `references.bib` `iucn2025redlist`
  entry re-pointed to the live summary-statistics page.
- **BRENDA Release 2026.1** (4 Mar 2026) — `brenda-2026-enzyme-resource`
  ledger row's `evidence_date`/`checked_as_of` bumped; prose makes no
  version-specific claim so was left untouched (nothing to correct).
- **UniProtKB reference-proteome restructuring** (underway, release
  2026_02) — added one hedged caveat sentence to
  `manuscript/unit_I/macromolecules.md` noting the restructuring without
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

- **Lab materials strengthened:** all 39 config-registered labs now include a
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

- **Scope checked:** all 137 config-registered manuscript surfaces. The quality
  audit now gates those counts directly, so missing front matter, unit intros,
  chapters, labs, question banks, or reference appendices fail before render.
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

| Surface | Files | Refresh focus | Current pass outcome |
| --- | ---: | --- | --- |
| Front matter and preface | 2 | Reader contract, source-governed claims, semantic navigation | No new current-science claim needed; retain generated navigation checks. |
| Unit intros | 11 | Current Evidence Thread language, cross-unit references, Mermaid metadata | Retain evidence-thread structure; Mermaid metadata normalized by `scripts/add_mermaid_alt_text.py --check`. |
| Core chapters | 44 | Fast-moving examples, citation closure, current-claim ledger anchors | Retain refreshed pangenome, AlphaFold, AMR, malaria, IUCN, CITES, climate, conservation, RNAcentral, GTDB, plant-pangenome, brain-cell-atlas, and human-genetics evidence lanes. |
| Labs | 44 | Paper-based evidence work, source cards, no hidden data/notebook dependency | Keep source-governance cards and table captions synchronized with the chapter evidence lanes. |
| Question banks | 44 | Chapter-grounded answers, no generated scaffolds, current-source transfer | Keep assessment transfer grounded in chapter evidence without changing the 30-question invariant. |
| Reference appendices | 7 | Glossary/index links, semantic appendix references, no hard-coded rendered numbers | No content refresh needed; keep `link_glossary.py --check` and crossref gates authoritative. |

## Directly Verified Priority Sources

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
