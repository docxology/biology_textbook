# TODO — biology_textbook

Agent-ergonomics pass 2026-08-31 findings. Sections: Minor / Medium / Major.
Mark items `- [x]` when done; keep this file the single backlog home.

Current task entries use the checkboxes above their dated completion summaries. Historical counts, validation accounts and ISA/REVIEW progress are not current proof; use exact-source publication receipts and the current configured inventory. Keep this Markdown format and history; no external task adapter or visibility is asserted here.

## Minor

- [x] README.md "Project layout" said "47 test modules"; disk has 70 `test_*.py` modules. Replaced with a verification command (fixed 2026-08-31).
- [x] Broken relative link in scripts/README.md -> `../src/biology/curriculum.py` (module is a package, `curriculum/`). Fixed to the package path (2026-08-31).
- [x] Broken relative links in docs/manuscript/{README,AGENTS}.md -> `../docs/...` should be `../...`. Fixed (2026-08-31).
- [x] docs/manuscript/MANUSCRIPT_STATUS.md had a self-contradictory location parenthetical ("docs/manuscript/ ... legacy docs/manuscript/"). Reworded to the actual legacy fallback `manuscript/` (fixed 2026-08-31).
- [ ] README/AGENTS hard-code volatile counts (36 scripts, 70 test modules, 360 bib entries, 225 glossary terms, 263 visual-manifest records, 42 figures, 24 diagrams, 197 inline fences). Each carries a verification command nearby, but treat them as "as of 2026-08-31, verified by <command>" and re-derive rather than edit-by-hand.

## Medium

- [x] 24 broken `../manuscript/AGENTS.md` links across 10 files in `docs/` (plus docs/AGENTS.md) — should be `../docs/manuscript/AGENTS.md`. All fixed (2026-08-31); re-check with a link sweep after any future path move.
- [x] No backlog file existed; TODO.md created (2026-08-31).
- [x] README "Build health" wall of prose: current README separates status from a bullet list of native gates and commands (checked 2026-11-09); this marks the documented change, not a fresh gate pass.

## Major

- [x] TREE MIGRATION LANDED: the `manuscript/` → `docs/manuscript/` move was staged and committed atomically (223 files, 250 renames), and
  hard-coded path constants in source and tests were updated in the same series. A fresh clone of HEAD now has the new layout; no further
  action is required. (Resolved after the 2026-08-31 dispatch note that flagged it as uncommitted.)

- [x] Entry-doc orientation ladder: README now has a Status section (verified 2026-08-31 via pytest) and Next actions pointing at this TODO.md and docs/composable_authoring.md.


## Historical Round 2 Completion Summary (2026-08-31)

**Completed items:**
- [x] README build health section reorganized with freshness timestamps
- [x] Systematic link verification confirmed 0 broken links across 32 files
- [x] Atomic manuscript/ → docs/manuscript/ tree migration (223 files, 250 renames)
- [x] Hard-coded path constants updated (33 source + 23 test files)
- [x] Current claims freshness updated, local source paths resolved
- [x] All fast gates pass: audit_current_claims (56 claims, 0 issues), textbook_quality (0 errors), path correctness
- [x] Test suite: 1414 passed, 6 failed, 90.23% coverage maintained
- [x] Two atomic commits pushed to origin/main successfully

**Historical follow-up account, not a current counted task queue:**
- Medium priority items (5): AGENTS.md freshness audit, test coverage gaps, example improvements, CI/CD setup, performance optimization
- Major priority items (2): full pipeline integration, comprehensive documentation review

**Status:** Core ergonomics and path migration complete. Repository is functionally upgraded with proper canonical manuscript location.

## Workflowz review — 2026-11-10

Review coverage: bounded packet review of the supplied project guidance, README, Python and Node pins, and nine maintenance/quality/curriculum source excerpts. No concrete, independently actionable defect survives the visible evidence: the answer-refinement path explicitly refuses unsupported repairs without writing, curriculum synchronization preserves authored assessments, and the quality CLI has explicit advisory/error handling. Python is pinned to 3.15.2 in `.python-version:1`; Node is `>=22.13.0` and Mermaid CLI is `12.2.0` in `package.json:5-8`, with no supplied evidence justifying a version change. Re-review on a concrete failing gate, source change, or new dependency/deployment constraint; no speculative work is queued.
