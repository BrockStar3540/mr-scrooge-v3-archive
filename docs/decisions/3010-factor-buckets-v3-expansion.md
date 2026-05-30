# 3010. factor_buckets v3 — expand RSI / BBP / ZS / ADR resolution

**Status:** Accepted
**Date:** 2026-05-22
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

The original 14-bucket signature was at a resolution that grouped meaningful sub-states. Specifically:
- `RSI` had 4 buckets — RSI0 conflated "extreme oversold (<20)" with "moderately oversold (20-30)"
- `BBP` had 4 buckets — middle was a flat 40-60 range
- `ZS` had 4 buckets — extremes >+2 and >+3 were the same bucket
- `ADR` had 4 buckets — "fresh" vs "moderate ADR consumed" weren't separable

Neighbor-WR analysis (Task #33) showed that splitting these factors at finer thresholds produced sub-buckets with materially different sim_WR.

## Decision

Promote to `factor_buckets_v3`:
- `RSI` 4 → 8 buckets (split at 20/30/40/50/60/70/80)
- `BBP` 4 → 7 buckets (split middle 40-60 into 40-50 / 50-60)
- `ZS` 4 → 7 buckets (separate >+2 / >+3, <-2 / <-3)
- `ADR` 4 → 6 buckets (fresh / 25% / 50% / 75% / shock-day / extreme-shock)

Other buckets unchanged (BB, A5, A1, EMA, SPR, HTF20, HTF60, T1, T4) — they were already at adequate resolution per the WR analysis.

## Alternatives considered

- **Continuous factors (no bucketing)** — rejected. Loses the per-cell mining framework; matrix factor_lift requires discrete buckets to compute lift.
- **Uniform expansion across all 14 factors** — rejected. Most factors don't gain from finer buckets; would 4× cluster count without 4× signal.
- **Expand only RSI + BBP** — rejected. The neighbor-WR data was clear on all four.

## Consequences

- Cluster count grew with the bucket expansion (specific numbers in vault project page).
- Forced a matrix rebuild + observer retrain cycle.
- Net signal improvement validated via held-out neighbor-WR.

## Cross-references

- Task #32 (ship), #33 (neighbor-WR validation)
- Module: `src/scrooge_v3/features/factor_buckets.py`
