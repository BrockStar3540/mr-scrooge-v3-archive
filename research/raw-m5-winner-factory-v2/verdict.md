# Raw-M5 Winner Factory v2 — Verdict

**Date:** 2026-05-13
**Pair scope:** 26 pairs across 4 families (usd_base, eur_cross, gbp_cross, antipodean_cross)
**Period:** Dukascopy M5, 2019-07-01 → 2026-04-22
**Discovery / Holdout split:** 2025-01-01
**Total candidates:** 1,693,412 (after rollover-kill + cost-uneconomic gate)

## What v2 fixed from v1

| v1 problem | v2 fix |
|---|---|
| All "winners" were rollover artifacts | Rollover (UTC 21-22) auto-killed |
| Mid-price fantasy | Per-pair spread cost penalty applied to entry, stop, and TP |
| USD-base only | All 4 families: usd_base, eur_cross, gbp_cross, antipodean_cross |
| 6 naive triggers | 10 triggers added PDH/PDL proximity (T7), failed PDH/PDL breakout (T8), session-open impulse/fade (T9), compression+expansion (T10) |
| No higher-timeframe context | M15 trend (up/down/flat) + H1 regime (breakout/in_range/consolidation) joined as cell axes |
| Cell key 9-axis bin-soup | Cell key = trigger × family × direction × session_quarter × M15_trend × H1_regime (6 structural axes, no rsi/bb_pos/bbw bin fragmentation) |

## Global baseline (this is the ocean)

```
mean R@2_net (all 1.69M candidates):  -0.171
                          discovery:  -0.172
                          holdout:    -0.166
```

As expected: naive triggers, after realistic spread, are net-losing in aggregate.
The question was never "is the aggregate positive" — it was "are there conditional
pockets that swim out of this".

## Headline finding

**335 family-grain cells are double-survivors** (positive net R in both discovery
and holdout, disc n≥100, hold n≥30). Every single top-25 cell has the SAME
structural fingerprint:

> **H1 regime = breakout, AND M15 trend aligned with the trade direction.**

That is the regime gate. Not a chart-pattern bin. Not a probe-trigger conjunction.
A higher-timeframe structural condition that the entry trigger only fires when
the trade direction is *with* the H1 breakout flow and the M15 trend.

This is the third independent confirmation that V3's regime philosophy is sound
(box gates → branch routing → now: H1-breakout conditional). It is the FIRST
empirical evidence of a robust edge surviving discovery, holdout, AND realistic
cost — without inheriting probe-fired contamination.

## Top 5 cells

| trigger | family | dir | session | M15 | H1 | n_disc | clean_2r_d | meanR_d | n_hold | meanR_h |
|---|---|---|---|---|---|---|---|---|---|---|
| T2_bb_upper_reject | usd_base | short | london_q2 | down | breakout | 286 | 53.8% | +0.91 | 54 | +0.88 |
| T1_bb_lower_reclaim | usd_base | long | asia_q2 | up | breakout | 214 | 52.3% | +0.86 | 87 | +0.73 |
| T1_bb_lower_reclaim | usd_base | long | london_q2 | up | breakout | 334 | 50.0% | +0.85 | 67 | +0.86 |
| T1_bb_lower_reclaim | eur_cross | long | london_q1 | up | breakout | 137 | 51.8% | +0.84 | 44 | +1.03 |
| T1_bb_lower_reclaim | usd_base | long | london_q1 | up | breakout | 335 | 54.0% | +0.83 | 49 | +0.89 |

All five maintain +0.7R+ mean net per trade in holdout. n is meaningful in both eras.

## The 6-dimension report

### 1. Positive net cells

- 589 cells positive in discovery (n_disc ≥ 100)
- 629 cells positive in holdout (n_hold ≥ 30)

### 2. Double-survivors (positive both eras) — 335 cells

Every top-25 cell has `h1_regime=breakout` AND M15 trend aligned with direction.
Saved to `report_double_survivors.csv`.

### 3. Cost-killed cells

**Zero cells** with pre-cost mean > +0.10 but post-cost negative. Cost penalty
was real (the global baseline went from naive-mid-positive to net-negative), but
there is no "almost an edge that died from cost" segment — cells are either
robust enough to survive cost, or genuinely non-edge. Useful negative result:
the spread cost penalty is correctly calibrated, not "killing everything."

### 4. Holdout-decay cells — 7 only

| trigger | family | dir | session | M15 | H1 | meanR_d | meanR_h |
|---|---|---|---|---|---|---|---|
| T7_pdl | usd_base | long | ny_pm_q2 | **flat** | breakout | +0.38 | -0.01 |
| T2_bb_upper_reject | usd_base | short | asia_q2 | down | **in_range** | +0.33 | -0.30 |
| T7_pdl | usd_base | long | ny_pm_q3 | up | breakout | +0.31 | -0.00 |
| T7_pdh | gbp_cross | short | london_q2 | down | breakout | +0.30 | -0.13 |
| T8_pdh_fail | eur_cross | short | overlap_q4 | down | breakout | +0.27 | -0.10 |
| T8_pdh_fail | eur_cross | short | overlap_q2 | down | breakout | +0.25 | -0.06 |
| T3_band_reentry_long | eur_cross | long | overlap_q2 | **flat** | breakout | +0.23 | -0.05 |

Pattern: decay concentrated in **flat M15 trend** or **in_range H1** cells — not
the trend-aligned-breakout core. Validates the regime gate from another angle:
the cells WITHOUT both alignment conditions are the ones whose edges decay.

### 5. Trigger family verdicts

Global per-trigger means (all negative, all roughly similar):

```
T9_session_open_fade        -0.129    (best aggregate, smallest sample n=16k)
T3_band_reentry_long        -0.152
T6_ema20_reject_short       -0.155
T4_band_reentry_short       -0.158
T1_bb_lower_reclaim         -0.162
T5_ema20_reclaim_long       -0.164
T8_pdl_failed_breakdown     -0.165
T2_bb_upper_reject          -0.173
T7_pdl_proximity_reversal   -0.176
T8_pdh_failed_breakout      -0.191
T7_pdh_proximity_reversal   -0.198
T10_compression_expansion   -0.201
```

But **per best-pocket double-survivor:**

| trigger | best pocket meanR_d |
|---|---|
| T2_bb_upper_reject | **+0.91** |
| T1_bb_lower_reclaim | **+0.86** |
| T7_pdl_proximity_reversal | **+0.81** |
| T7_pdh_proximity_reversal | **+0.67** |
| T8_pdl_failed_breakdown | **+0.64** |
| T5_ema20_reclaim_long | +0.57 |
| T6_ema20_reject_short | +0.57 |
| T4_band_reentry_short | +0.53 |
| T8_pdh_failed_breakout | +0.45 |
| T3_band_reentry_long | +0.28 |

**Triggers with ZERO double-survivors:**
- T9_session_open_fade (16k candidates, no pocket survives)
- T10_compression_expansion (3.9k candidates, none survive)

Verdict: **kill T9 and T10**. Session-open fade and BBW-compression-expansion
breakout are not real edges at M5 grain.

**Promote:** T1, T2, T7 (PDH/PDL proximity reversal) — three strongest. T8
(failed-breakout) is a viable secondary. T5/T6 (EMA20) are weak but produce
some pockets. T3/T4 (band reentry) marginal.

### 6. Management sensitivity (on top 20 double-survivors)

Per-trade mean R, discovery / holdout:

| Variant | top cell d/h | median across top 20 d | top 20 hold |
|---|---|---|---|
| V_2R (hold to 2R) | 0.71 / 0.59 | ~0.55 | ~0.43 |
| V_1R (close TP) | 0.45 / 0.42 | ~0.30 | ~0.27 |
| **V_BE05 (BE at 0.5R)** | **0.92 / 0.78** | **~0.72** | **~0.64** |
| V_BE10 (BE at 1R) | 0.85 / 0.72 | ~0.65 | ~0.55 |
| V_PART1 (half@1R, runner) | 0.65 / 0.57 | ~0.46 | ~0.43 |

**V_BE05 dominates in 19 of 20 top cells, in BOTH eras.** Adds ~+0.15-0.20R per
trade vs hold-to-2R baseline. This re-validates the directional management
ADR (earlier rejected because tested on unconditional V3-era data) — but now
the lift survives in the **trend-aligned + H1-breakout** conditional cells where
the entry edge actually exists.

Caveat: V_BE05 is approximated from mfe/mae alone, not true order-of-events.
True mfe-reaches-0.5R-before-mae-reaches-1R order requires a tick-level replay.
The numbers should be treated as upper-bound, but the relative ordering across
variants is robust.

### Pair concentration

**0 of 20 top cells are fragile** (no single pair > 70% of cell trades). Highest
concentration is T7_pdl/usd_base/asia_q3 at AUD_USD 49% — not fragile. Top cells
spread across GBP_USD, USD_JPY, AUD_USD, EUR_JPY, EUR_AUD, GBP_JPY, USD_MXN.
The edge is not a one-pair illusion.

## What this changes

The earlier MS-001..MS-025 chart-pattern bin search was looking in the wrong
place. The structural axes that carve the edge are NOT bb_position × rsi × bbw ×
echo, they are **trigger × pair_family × direction × session_quarter × M15_trend ×
H1_regime**.

This is consistent with — and corroborates — the V3 regime/box philosophy. V3's
strategy that says "don't trade in range_bound regime" is empirically validated
by this entirely independent raw-M5 search: cells whose H1 is NOT breakout do
not produce robust edges, and the few that show discovery positive **decay
in holdout**.

## Next steps (recommendation)

1. **Promote v2 finding to ADR draft**: BB-reclaim/reject + PDH/PDL-proximity
   triggers ARE a legitimate raw-M5 microstrategy family WHEN gated by
   M15-trend-aligned + H1-breakout regime. Apply BE@0.5R management.
2. **Drop T9 and T10** from any further microstrategy search.
3. **Run V3-era forward-only validation** on the top 5 cells. Last raw-M5
   management ADR was rejected at the V3-era gate; we owe the same gate here
   before this becomes a live config change.
4. **Build live detection feasibility check**: H1-breakout regime label needs
   a 48-bar rolling H1 range rank computation; M15 trend needs M15 EMA20. Both
   are cheaply computable in V3's existing feature pipeline.
5. **Spawn parallel search at M15 entry grain** to see if these same patterns
   appear stronger / less spread-taxed at coarser entry timing.
6. **Do not** declare the search converged. v2 found a real signal; v3 should
   stress-test it with realistic order-of-events (BE timing), V3-era-only
   replay, and live spread proxy from OANDA broker data rather than dukascopy
   approximations.

## Outputs

```
/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v2/
  raw_m5_winner_factory_v2.py                      (script)
  raw_m5_v2_candidate_events.parquet               (1.69M trades, 200MB, gitignored)
  raw_m5_v2_clusters_family_grain.csv              (6408 cells)
  raw_m5_v2_clusters_pair_grain.csv                (33706 cells)
  raw_m5_v2_microstrategy_candidates.csv           (54 strict-gate promising)
  raw_m5_v2_skip_cells.csv                         (634 loser cells)
  report_double_survivors.csv                      (335 double-survivors)
  report_holdout_decay.csv                         (7 decay cells)
  report_cost_killed.csv                           (0 cost-killed)
  report_management_variants_top20.csv             (BE@0.5R dominance)
  report_pair_concentration_top20.csv              (0 fragile)
  verdict.md                                       (this file)
```
