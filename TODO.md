# TODO — biology_textbook

Agent-ergonomics pass 2026-08-31 findings. Sections: Minor / Medium / Major.
Mark items `- [x]` when done; keep this file the single backlog home.

## Minor

- [x] README.md "Project layout" said "47 test modules"; disk has 70 `test_*.py` modules. Replaced with a verification command (fixed 2026-08-31).
- [x] Broken relative link in scripts/README.md -> `../src/biology/curriculum.py` (module is a package, `curriculum/`). Fixed to the package path (2026-08-31).
- [x] Broken relative links in docs/manuscript/{README,AGENTS}.md -> `../docs/...` should be `../...`. Fixed (2026-08-31).
- [x] docs/manuscript/MANUSCRIPT_STATUS.md had a self-contradictory location parenthetical ("docs/manuscript/ ... legacy docs/manuscript/"). Reworded to the actual legacy fallback `manuscript/` (fixed 2026-08-31).
- [ ] README/AGENTS hard-code volatile counts (36 scripts, 70 test modules, 360 bib entries, 225 glossary terms, 263 visual-manifest records, 42 figures, 24 diagrams, 197 inline fences). Each carries a verification command nearby, but treat them as "as of 2026-08-31, verified by <command>" and re-derive rather than edit-by-hand.

## Medium

- [x] 24 broken `../manuscript/AGENTS.md` links across 10 files in `docs/` (plus docs/AGENTS.md) — should be `../docs/manuscript/AGENTS.md`. All fixed (2026-08-31); re-check with a link sweep after any future path move.
- [x] No backlog file existed; TODO.md created (2026-08-31).
- [ ] README "Build health" paragraph is a 12-line wall of prose mixing build status, gates, and conventions. Split into a short status line + bullet list of gates with their commands.

## Major

- [ ] UNCOMMITTED TREE MIGRATION (pre-existing at 2026-08-31 dispatch, not this pass): `manuscript/` files are deleted on disk and the full tree now lives in untracked `docs/manuscript/`. Prose references were updated in tracked files, but a fresh clone of HEAD still has the old layout. A future commit must stage the `manuscript/` deletions + `docs/manuscript/` additions as one atomic move (owner decision; not done here to avoid committing files this pass did not author).

- [x] Entry-doc orientation ladder: README now has a Status section (verified 2026-08-31 via pytest) and Next actions pointing at this TODO.md and docs/composable_authoring.md.
