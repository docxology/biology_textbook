# AGENTS — biology_textbook/src/biology/visual_contracts

Status: REAL (doc fleet, 2026-08-30)

Visual-contract system: generate and check the manifest of figure/Mermaid visual contracts.

## Layout
- `models.py` — contract record models.
- `manifest.py` — build and write visual-contract manifests.
- `render.py` — render contract artifacts.
- `scan.py`, `audit.py` — scan manuscript sources; audit contracts and Mermaid sources.
- `helpers.py` — path/dimension/text helpers.

## Invariants
- Contracts gate figures: a figure without a passing contract is an audit failure.
