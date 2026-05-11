# 1008. Fixed-pip stops + 50% ratchet (the profitable config)

**Status:** Accepted; preserved in `ORIGINAL_CONFIG.md` as rollback target
**Date:** 2026-03-20 (after the 30m box experiment revert)
**Version scope:** V1
**Backfilled:** 2026-05-11

## Context

The 30m box experiment (Mar 19) introduced 23 commits exploring rolling boxes, zone-anchored stops, equity-% sizing, etc. It broke profitability. The Mar 20 revert restored commit `1c99ae2` ("original profitable version") as the baseline.

During the revert, 17 incidental fixes were kept. The cumulative configuration after the revert + fixes was the empirically-best V1 state. `ORIGINAL_CONFIG.md` preserves it as the explicit rollback target.

## Decision

The V1 profitable configuration:

| Parameter | Value |
|---|---|
| `margin_utilization_pct` | 0.50 (50% equity as margin per trade) |
| `max_concurrent_positions` | 1 |
| `min_risk_reward` | 1.60 |
| `max_eur_positions` | 2 (EUR concentration cap) |
| `zone_proximity_pct` | 0.0025 (0.25% of PDH/PDL) |
| `sl_floor_pct` | 0.0050 (0.50% minimum SL distance) |
| `sl_pips` | 10 (fixed pip stop) |
| `tp1_pips` | 10 (fixed pip TP1) |
| `tp2_pips` | 30 (fixed pip TP2) |
| Harvester T1 | 1.5% equity (~4.5 pips), close 25% |
| Harvester T2 | 3.0% equity (~9 pips), close 25%, SL → +1.5% |
| Harvester T3 | 4.5% equity (~13 pips), close 25%, SL → +3.0% |
| Runner | 25% rides to TP2 (OANDA native) |
| Ratchet Stage 0 | Reconciled trade +5 pips → SL to entry |
| Ratchet Stage 1 | 50% of way to TP1 → SL to entry (breakeven) |
| Ratchet Stage 2 | Price passes TP1 → SL to TP1 level |
| Ratchet Stage 3 | After BE → `max(1H candle_low, entry + 80% × peak, peak − 1.5×ATR)` |

Key principle: **stops and TPs are fixed pips from FILL price**, not zone price. Recalculated post-fill via `modify_trade_stop()` / `modify_trade_tp()`.

## Alternatives considered

- **Equity-%-based stops** — rejected. Drifted across pair classes (JPY vs non-JPY). Pip-normalization gives consistent risk.
- **Zone-anchored stops** — rejected (per ADR 1005). Stop placement must match signal candle anatomy, not arbitrary zone.
- **Wider TPs (e.g. TP1=30, TP2=60)** — rejected. Empirically the 10/30 pip pair was the profitable configuration. Tinkering past the revert point regressed.

## Consequences

**Enabled:**
- A documented, replayable "known good" V1 configuration. If V2/V3 work goes off the rails, `ORIGINAL_CONFIG.md` is the literal rollback target.
- Per-pair consistency in pip-normalized risk.

**Closed:**
- Equity-%-as-primary stop sizing.

## Costs

The fixed-pip approach doesn't adapt to volatility. JPY pair with 50-pip ATR vs EUR/CHF with 8-pip ATR both get SL=10 → very different probabilities of stop-out. Mitigated partly by `sl_floor_pct` (0.50% minimum), but a true volatility-adaptive stop would be a separate ADR (deferred).

V3's `simulate_trade_multi` uses structure-relative stops (`stop_distance = max(structure_offset + 0.25×ATR_pips, spread_floor)`) — a more adaptive approach. The V1 fixed-pip target is preserved as evidence of an empirical sweet spot.

## Cross-references

- `ORIGINAL_CONFIG.md` in `BrockStar3540/mr-scrooge`
- `AUDIT.md` 2026-03-19/20 (overhaul section)
- `[[scrooge-bug-catalog]]` B-040, B-052
- ADR `1005-master-theory-realignment.md` — stop placement at signal candle extreme
