# Raw-M5 Winner Factory v1 — Verdict

**Date:** 2026-05-13
**Pair scope:** 8 USD-base pairs (EUR_USD, GBP_USD, AUD_USD, NZD_USD, USD_JPY, USD_CHF, USD_CAD, USD_MXN)
**Period:** Dukascopy M5, 2019-07-01 → 2026-04-22
**Discovery / Holdout split:** 2025-01-01

## What this build was

Per Brock's Option A directive (2026-05-13): replace the Codex winner factory's
probe-fired corpus mining with **raw-chart candidate generation**. No probe filter.
Forward-walk every candidate from chart primitives. Cluster the winners.

Six of the ten specified triggers implemented in v1:

| Code | Trigger | Direction |
|------|---------|-----------|
| T1 | BB lower band reclaim | long |
| T2 | BB upper band reject | short |
| T3 | Band reentry (prev close < lower, now back inside) | long |
| T4 | Band reentry (prev close > upper, now back inside) | short |
| T5 | EMA20 reclaim | long |
| T6 | EMA20 reject | short |

Forward-walk: 1×ATR stop, multi-target (1R / 1.5R / 2R), max 300 bars (~25h).
9-axis cell key: trigger × pair_family × direction × session_quarter ×
bb_pos_bin × rsi_bin × ema20_dist_bin × bbw_bin × echo_ratio_bin.

## Numbers

- **Total candidates:** 1,004,233 (813,229 discovery / 191,004 holdout)
- **Unique cells:** 17,486
- **Cells passing promise gate** (disc n≥50, clean_2r≥40%, hold n≥20, hold clean_2r≥30%): **19**
- **Highest-n cell:** T2_bb_upper_reject / short / asia_q1 / upper_rail / bbw_mid / echo_compressed — n=1,768 discovery, clean_2r = 32.7% discovery / 32.1% holdout, mean_R@2 = +0.176

## Verdict: NO ROBUST MICROSTRATEGY

The promising gate fires only on thin-liquidity rollover candidates.

- **18 of 19 promising cells are `rollover_q*`** (UTC 21-22, the daily thin-window).
  M5 mid-price hides the spread blowup that occurs at rollover. Any clean_2R rate
  there is suspect until realistic transaction cost is applied.
- **The single non-rollover survivor:** T3_band_reentry_long / usd_base / asia_q4 /
  lower_band / mid RSI / ema_near / bbw_mid / echo_mid — n=94 discovery, clean_2r =
  40.4% discovery / 30.0% holdout, **mean_R@2 = +0.20**. Marginal at best.
- **At meaningful n (≥500 discovery, ≥100 holdout):** zero cells hit 40% clean_2R.
  Best is asia_q4 T4 short at 34.4% discovery / 28.8% holdout.

The bins themselves (bb_pos / rsi / ema_dist / bbw / echo) do not carve out a
sharp winner pocket once probe-fired contamination is removed and meaningful n
is required. The earlier MS-001..MS-025 microstrategies' clean_2R lift came from
the probe-trigger conjunction, not from the chart-primitive bins.

## Read-through

This is the third independent confirmation that V3's strategy edge does NOT
come from a discoverable chart-pattern bin combination:

1. Step 8 era-split factor synchrony: only 1 factor (usd_base/short spread_pips)
   survives daily-cache + V3-era split.
2. Geometry layer audit: no smoking-gun bug in V3 box code.
3. Raw-M5 Winner Factory v1: 1M candidates / 17K cells, no robust microstrategy
   at meaningful n.

The implication: raw chart-shape mining at the M5 grain — using BB / RSI / EMA /
BBW / echo bins as the carving axes — is **not** where the next lever lives.

## What's NOT yet ruled out

- The remaining 4 triggers (middle-band rejection, EMA20/50 compression+expansion,
  range/echo failed breakout, session-quarter opening impulse/fade, PDH/PDL rail
  proximity reversal). T5/T6 were already weak in v1 (≪0.1% of total candidates),
  suggesting EMA-cross primitives are noise at M5 grain. The structural triggers
  (compression+expansion, PDH/PDL proximity) may be different, but the pattern
  here suggests the carving axes are wrong, not the triggers.
- Non-USD-base pair families (antipodean_cross, eur_cross, gbp_cross). v1 stayed
  on USD-base; expanding to 26 pairs may surface family-conditional edges.
- Different grain entirely (M15, H1 multi-bar setups). Raw M5 may be too fine
  for genuine chart-pattern edges to survive.
- Different management (trailing, partials, time exits) layered on top of these
  weak entries.

## Recommendation

Do **not** promote any v1 cell to live trading. The 19 promising cells fail the
liquidity-realism test. The non-rollover survivor is a coin flip.

Pause the "find raw-M5 microstrategies" research arc. Three independent confirmations
that V3's edge is not a discoverable chart-pattern bin combination is enough signal
to redirect.

Next research candidate (Brock to authorize):
- Apply realistic spread/slippage to the 19 promising cells and see what survives.
- OR expand triggers (compression+expansion, PDH/PDL proximity) and family scope
  before declaring raw-M5 dead.
- OR shift to a different grain (M15/H1) entirely.

## Outputs

```
/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v1/
  raw_m5_winner_factory.py            (script)
  raw_m5_candidate_events.parquet     (1M trades, 28 cols, 95MB)
  raw_m5_winner_clusters.csv          (17,486 cells, 4.5MB)
  raw_m5_microstrategy_candidates.csv (19 promising cells)
  verdict.md                          (this file)
```
