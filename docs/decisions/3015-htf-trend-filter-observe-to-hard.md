# 3015. HTF trend filter — observe → HARD

**Status:** Superseded by 3008 (MatrixRouter)
**Date:** 2026-05-27
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

Throughout May the HTF alignment signal repeatedly surfaced as the king factor:
- Matrix factor_lift: `cand_vs_htf20_mismatch` lift +0.177 (dominant single factor)
- Per-pair modules: T1=T1a appearance ratio 132:1 in WIN vs LOSE rules
- LightGBM v0: HTF features in top-5 by gain
- DeepSeek HTF white paper: confirms institutional MTF effectiveness

By 2026-05-27 we had three independent confirmations of the same signal. The `HTFTrendFilterGate` had been running observe-only with logged would-block decisions; review of the would-block set showed it would have caught 12/16 of yesterday's 11/11 long-disaster streak into JPY downtrend.

## Decision

Promote `HTFTrendFilterGate` from `observe` → `HARD`. Block candidates whose direction is misaligned with the daily HTF trend (lookback_periods=20, neutral_pct=0.0).

## Alternatives considered

- **Keep observe-only, encode the signal as a scorer feature only** — rejected. The misaligned slice was producing meaningful live losses; observe-only was costing money to validate something already validated three ways.
- **Promote with `neutral_pct > 0`** — rejected. Neutral zones reintroduce ambiguity at exactly the moments the signal is most useful (trending days).
- **Wait for matrix integration to encode it implicitly** — partially happened; gate was retired same day (ADR 3008) once `MatrixRouterGate` shipped with cell-level HTF rules. The HARD promotion existed for ~hours before being subsumed.

## Consequences

- Gate retired same day in favor of MatrixRouter cell-level enforcement.
- HTF signal now lives at three layers: routing-table cell rules, LightGBM model gain, matrix shadow factor_lift cross-val.

## Cross-references

- Vault: `wiki/postmortems/fixes/scrooge-v3-strategy-promotion-2026-05-27.md`
- Task #21
