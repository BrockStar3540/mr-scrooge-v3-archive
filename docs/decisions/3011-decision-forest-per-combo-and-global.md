# 3011. Decision forest — per-combo + global decision trees

**Status:** Accepted
**Date:** 2026-05-23
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

Single-factor lift values are necessary but not sufficient. Two factors that each show +0.05 lift may interact destructively (e.g., HTF-aligned LONG with RSI > 70 isn't additive — it's mean-reversion territory). The matrix factor_lift table aggregates per-factor but doesn't capture pairwise / N-way interactions.

## Decision

Build a decision_forest layer with two outputs:
1. **Per-combo trees:** one tree per (pair × family × direction × session) cell. Trained against realized R on the matrix's optimized cohort. Captures cell-specific factor interactions.
2. **Global tree:** one tree across all cohorts. Used as a sanity-check ranker and as the fallback when a cell has insufficient samples for its own tree.

Stored at `data/decision_forest.json` (21MB).

## Alternatives considered

- **Single global tree only** — rejected. Loses cell-specific microstructure (CAD_JPY box vs EUR_USD reversal have different king factors).
- **Per-pair only (no per-family split)** — rejected. Family interactions are too strong to merge.
- **Random forest instead of single tree per cell** — rejected. Sample sizes per cell don't justify forest depth; single shallow tree per cell is the right resolution.

## Consequences

- Adds an explainable layer on top of factor_lift. Each cell has a tree you can read.
- Feeds the loser-veto policy (ADR 3012) and the LightGBM training set.
- Sample sizes per cell limit tree depth — many cells fall back to the global tree.

## Cross-references

- Task #36
- Artifact: `data/decision_forest.json`
