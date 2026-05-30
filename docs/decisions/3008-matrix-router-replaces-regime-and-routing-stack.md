# 3008. MatrixRouter replaces regime + routing-table gate stack

**Status:** Superseded by 3017 + 3019
**Date:** 2026-05-14
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

By mid-May the live gate pipeline had accumulated:
- `RegimeFloorGate` (score ≥ −4)
- `RegimeCompatGate` (observe-only classifier)
- `RegimeStrategyRouterGate` (allow-list router)
- `SubRegimeFilterGate` (bottom-MTB veto)
- `EntryFilterGate` (per-cell shave_rule)
- `HTFTrendFilterGate` (daily directional bias)
- `EntryFilterShadowGate` (parallel shadow routing)

Seven gates encoding overlapping slices of the same per-(pair × family × direction × session) decision. Each had its own bucketing, its own log format, its own audit trail. A single candidate could be evaluated against the same factual question 4× under 4 different rule sets, with diverging verdicts.

The lab matrix (3,879 optimized cells + 162 factor_lift keys) already encodes this decision in one place, learned from the 838k corpus. The gate proliferation was duplicating it in code.

## Decision

Replace all seven gates with a single `MatrixRouterGate` reading the canonical routing table parquet. Each cell (pair × family × direction × session) carries:
- WIN/LOSE rule (matrix-mined)
- shave_rule (band rule from hybrid shaver)
- factor_lift signal (top-K aggregated)
- assigned tier (Seed / Seed-Pro / etc.)

Per-cell decisions become one parquet lookup. Routing version is bumped on every matrix rebuild.

This was Brock's 2026-05-14 architecture decision; the implementation landed across the next two weeks.

## Alternatives considered

- **Keep all 7 gates, add an "explain" mode for audit** — rejected. Doesn't fix the duplication; just makes it more visible.
- **Fold subset (RegimeCompat + RegimeStrategyRouter + EntryFilter) but keep HTF + SubRegime separate** — rejected. HTF alignment and sub-regime filtering are *exactly* the kind of signal the matrix already encodes per cell. Splitting them out re-introduces the duplication.
- **Move decision to ml_router only, no parquet table** — rejected at decision time. The parquet table is the audit-trail artifact; without it we lose the per-cell explainability.

## Consequences

- `bootstrap.py` shrinks dramatically — 7 gate registrations collapse to 1.
- One audit log per cell decision instead of 7.
- Routing version is now the single source of truth for "what's tradable today."
- Locks the system into a parquet-mining cycle: rebuilds happen when matrix is rebuilt, not on hotpatch.
- Superseded in part by ADR 3017 (V3HybridScorer disabled + LightGBM primary) and 3019 (matrix shadow as separate cross-val) — the matrix's role split into "router enforcement" + "advisor cross-val."

## Cross-references

- Routing table: `data/routing_table_v10_fast_v1_*.parquet`
- Vault: `wiki/projects/scrooge-v3-matrix-integration-arc.md` (pending)
- Tasks: #29 (MatrixRouter build), #35 (loser-veto upgrade — ADR 3012)
