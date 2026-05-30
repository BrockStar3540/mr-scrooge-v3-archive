# 3019. Matrix wired as shadow advisor (not gate) alongside LightGBM

**Status:** Accepted
**Date:** 2026-05-29
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

The lab-mined matrix was already encoded in the routing table (ADR 3008, 3016), but the routing table is a parquet snapshot — once built, it doesn't re-evaluate per candidate. The raw matrix CSVs (`optimized_matrix_by_session.csv`, `factor_lift_table.csv`) contain richer information than the routing snapshot:
- Per-candidate cell lookup (vs. summary admission rule)
- Per-factor lift values
- Cell-level kept/optimized statistics

Wiring the raw matrix into the live path gives us:
1. Per-candidate matrix verdict (`MATRIX_PASS` / `MATRIX_NEG_CELL` / `NO_CELL_FACTOR_ONLY` / `MATRIX_BLIND`)
2. Cross-validation against LightGBM's pick on the same candidate
3. Audit trail for when matrix and LightGBM disagree — that's where the learning signal is

## Decision

Add a `matrix_shadow` advisor at `src/scrooge_v3/advisors/matrix_shadow.py`. At boot, load `data/matrix/optimized_matrix_by_session.csv` (3,879 cells) + `data/matrix/factor_lift_table.csv` (162 pair × strat × dir keys). On every best-candidate selection, the scan coordinator calls `matrix_shadow.observe()` which logs the verdict + cell details + cross-validation against LightGBM to `data/matrix_shadow.jsonl`.

**Never gates. Never raises.** Pure observability.

The matrix shadow runs in parallel to `lightgbm_shadow.observe()` — both shadows fire on the same picked candidate. ml_router is the third shadow.

## Alternatives considered

- **Promote matrix to a gate (e.g., veto when both LightGBM and matrix disagree-down)** — rejected for this version. We need the disagreement log first to understand which side is right when they diverge. Promotion gated on ~30-50 closed-trade comparison.
- **Re-embed raw matrix into the routing table rebuild instead of as a separate advisor** — rejected. The routing table is a snapshot artifact; the advisor lets us cross-check live without forcing a routing rebuild every time the matrix updates.
- **Roll matrix into LightGBM training data instead of as a separate observer** — partially the existing arrangement (LightGBM was trained on matrix-tagged candidates). The advisor adds the *inference-time* cross-check, which is the part LightGBM-only doesn't give us.

## Consequences

- Three parallel observers: LightGBM (primary gate), matrix shadow, ml_router shadow.
- New JSONL: `data/matrix_shadow.jsonl` — one entry per picked candidate with cell + factor_lift + verdict.
- Boot log confirms: `[MATRIX_SHADOW] optimized_matrix: 3879 cells` + `[BOOT] Matrix shadow advisor ENABLED`.
- Supersedes ADR 3012 in policy: loser-veto is now a *shadow signal*, not an admission rule. Routing table still enforces the matrix's admission decision via its snapshot.

## Cross-references

- Module: `src/scrooge_v3/advisors/matrix_shadow.py`
- Wiring: `src/scrooge_v3/core/bootstrap.py` (boot loader) + `src/scrooge_v3/core/scan_coordinator.py` (observe call)
- Matrix CSVs: `data/matrix/optimized_matrix_by_session.csv`, `data/matrix/factor_lift_table.csv`
- Vault: `wiki/projects/scrooge-v3-strategy-promotion-2026-05-27.md` (matrix routing prep)
