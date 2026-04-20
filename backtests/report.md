# Mr. Scrooge V3 — Historical Backtest on 50-Trade Calibration Dataset
Generated: 2026-04-20T19:13:27.651481+00:00

## Environment
- V3 code: current main (Phase 1+2+3+4)
- Scorer: V3HybridScorer (v3_scorer.py, V3.1 recalibrated 2026-04-16)
- Gates (active): debounce, zone_entry_cap, regime_floor — all vacuously PASS in historical backtest (empty state).
- Cooldown, expiry_backoff, daily_circuit: can't fire historically (no prior trade log).
- Management: TP1 @ 1.0R (50%), BE @ 0.5R trigger with pip floors, Ratchet @ 1.0R / 50% lock on MFE-anchored peak.
- Account equity assumption: $1,000; margin_utilization 0.40 → $400 risked/trade.
- Post-entry candles fetched live from OANDA practice (M5), 48h window cap.

## Part A — Scorer Verdict Per Trade

| # | trade_id | sym | d | hour | won | base | final | tier | session |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6109 | EUR_JPY | S | 23 | 0 | 0 | -4 | REJECT | dead_late |
| 2 | 6100 | EUR_USD | S | 20 | 0 | -31 | -40 | REJECT | dead_late |
| 3 | 6004 | USD_CHF | L | 17 | 0 | 0 | 0 | BLOCKED | ny_active |
| 4 | 5988 | NZD_JPY | S | 15 | 1 | 31 | 31 | REJECT | ny_active |
| 5 | 5978 | AUD_CAD | S | 12 | 1 | 10 | 10 | REJECT | ny_active |
| 6 | 5968 | USD_MXN | L | 5 | 0 | 0 | 0 | BLOCKED | asia_london_open |
| 7 | 5959 | NZD_JPY | S | 22 | 1 | 10 | 10 | REJECT | dead_late |
| 8 | 5944 | GBP_USD | S | 18 | 1 | 38 | 43 | REJECT | late_ny |
| 9 | 5926 | AUD_CAD | S | 17 | 1 | 3 | 3 | REJECT | ny_active |
| 10 | 5915 | EUR_USD | S | 15 | 0 | 0 | 0 | BLOCKED | ny_active |
| 11 | 5909 | USD_MXN | L | 14 | 0 | 5 | -7 | REJECT | ny_active |
| 12 | 5900 | NZD_USD | S | 14 | 0 | 4 | -13 | REJECT | ny_active |
| 13 | 5891 | GBP_USD | S | 12 | 1 | 17 | 17 | REJECT | ny_active |
| 14 | 5873 | AUD_USD | L | 7 | 1 | 36 | 47 | B | asia_london_open |
| 15 | 5775 | AUD_CHF | L | 7 | 0 | 4 | 14 | REJECT | asia_london_open |
| 16 | 5765 | NZD_USD | S | 7 | 1 | 42 | 52 | B | asia_london_open |
| 17 | 5755 | AUD_USD | L | 6 | 1 | 44 | 60 | A | asia_london_open |
| 18 | 5745 | NZD_USD | S | 5 | 1 | 25 | 41 | REJECT | asia_london_open |
| 19 | 5733 | AUD_JPY | L | 0 | 1 | 28 | 44 | REJECT | asia_london_open |
| 20 | 5723 | AUD_JPY | S | 3 | 1 | 48 | 64 | A | asia_london_open |
| 21 | 5713 | AUD_CHF | S | 3 | 1 | 31 | 47 | B | asia_london_open |
| 22 | 5591 | AUD_JPY | S | 2 | 1 | 55 | 71 | A | asia_london_open |
| 23 | 5573 | AUD_CHF | S | 1 | 1 | 57 | 73 | A | asia_london_open |
| 24 | 5559 | AUD_JPY | S | 23 | 1 | 6 | 6 | REJECT | dead_late |
| 25 | 5549 | AUD_JPY | S | 22 | 0 | 9 | 9 | REJECT | dead_late |
| 26 | 5539 | GBP_USD | S | 17 | 0 | 0 | 0 | BLOCKED | ny_active |
| 27 | 5529 | NZD_JPY | S | 14 | 1 | 19 | 24 | REJECT | ny_active |
| 28 | 5519 | GBP_USD | S | 12 | 1 | 18 | 18 | REJECT | ny_active |
| 29 | 5509 | GBP_USD | S | 8 | 1 | 41 | 53 | B | london |
| 30 | 5498 | GBP_USD | L | 20 | 0 | 0 | 0 | BLOCKED | dead_late |
| 31 | 5488 | USD_CHF | S | 16 | 0 | -16 | -25 | REJECT | ny_active |
| 32 | 5480 | AUD_CAD | S | 10 | 1 | 6 | 11 | REJECT | london |
| 33 | 5472 | USD_JPY | S | 8 | 0 | 9 | 14 | REJECT | london |
| 34 | 5464 | AUD_CAD | S | 2 | 1 | 30 | 46 | B | asia_london_open |
| 35 | 5455 | USD_CHF | S | 15 | 0 | 0 | 0 | BLOCKED | ny_active |
| 36 | 5446 | CHF_JPY | S | 15 | 0 | -8 | -14 | REJECT | ny_active |
| 37 | 5438 | USD_MXN | L | 6 | 1 | 47 | 62 | A | asia_london_open |
| 38 | 5429 | NZD_JPY | L | 12 | 0 | -9 | -25 | REJECT | ny_active |
| 39 | 5415 | NZD_JPY | L | 7 | 1 | 9 | 25 | REJECT | asia_london_open |
| 40 | 5406 | USD_MXN | S | 11 | 0 | 5 | 1 | REJECT | london |
| 41 | 5388 | USD_MXN | S | 23 | 1 | 18 | 26 | REJECT | dead_late |
| 42 | 5375 | USD_CHF | S | 19 | 0 | 8 | 9 | REJECT | late_ny |
| 43 | 5368 | USD_JPY | S | 14 | 0 | -12 | -28 | REJECT | ny_active |
| 44 | 5357 | USD_JPY | S | 20 | 0 | 0 | 0 | BLOCKED | dead_late |
| 45 | 5347 | USD_CHF | S | 18 | 1 | -5 | -5 | REJECT | late_ny |
| 46 | 5339 | USD_JPY | S | 18 | 1 | -2 | -6 | REJECT | late_ny |
| 47 | 5333 | USD_CHF | S | 14 | 0 | 5 | -1 | REJECT | ny_active |
| 48 | 5325 | USD_JPY | S | 14 | 1 | 25 | 25 | REJECT | ny_active |
| 49 | 5317 | GBP_USD | L | 7 | 1 | -4 | 0 | REJECT | asia_london_open |
| 50 | 5309 | USD_JPY | S | 4 | 1 | 53 | 69 | A | asia_london_open |

## Part A — Aggregate
- Accepted (tier A or B): **11** / 50
- Rejected (REJECT or BLOCKED): **39** / 50
  - Of rejected: 21 losers filtered out, 18 winners filtered out (false negatives)
- Accepted breakdown: 11 wins / 0 losses (original outcome)
  - Original accept win rate: 100.0%

## Part B — Management Sim On Accepted Trades

| trade_id | sym | d | tier | orig won | exit_reason | realized_R | MFE_R | MAE_R | tp1 | be | realized$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5873 | AUD_USD | L | B | 1 | sl_hit | -1.00 | +0.47 | -1.09 | - | - | $-400.00 |
| 5765 | NZD_USD | S | B | 1 | invalid_R | +0.00 | +0.00 | +0.00 | - | - | $+0.00 |
| 5755 | AUD_USD | L | A | 1 | be_hit | +0.78 | +1.12 | -0.60 | Y | Y | $+312.00 |
| 5723 | AUD_JPY | S | A | 1 | invalid_R | +0.00 | +0.00 | +0.00 | - | - | $+0.00 |
| 5713 | AUD_CHF | S | B | 1 | be_hit | +0.24 | +0.81 | -0.52 | - | Y | $+95.24 |
| 5591 | AUD_JPY | S | A | 1 | sl_hit | -1.00 | +0.01 | -1.19 | - | - | $-400.00 |
| 5573 | AUD_CHF | S | A | 1 | be_hit | +0.17 | +0.58 | -0.66 | - | Y | $+67.80 |
| 5509 | GBP_USD | S | B | 1 | sl_hit | -1.00 | +0.47 | -1.79 | - | - | $-400.00 |
| 5464 | AUD_CAD | S | B | 1 | be_hit | +0.27 | +0.57 | -0.78 | - | Y | $+108.11 |
| 5438 | USD_MXN | L | A | 1 | sl_hit | -1.00 | +0.58 | -1.21 | - | - | $-400.00 |
| 5309 | USD_JPY | S | A | 1 | be_hit | +0.19 | +0.63 | -0.67 | - | Y | $+74.07 |

## Part B — Aggregate
- Simulated trades: 11
- Wins (R > 0.05): 5
- Losses (R < -0.05): 4
- Break-even: 2
- Sim win rate: 45.5%
- Avg R: -0.21
- Total R: -2.36
- Total realized $ @ $400/trade risk: $-942.78

## Part C — Comparison vs Original
- Original: 29/50 wins, gross P&L (broken sizing): $-201.75
- V3 current, applied to same 50: 11 accepted / 39 rejected
- V3 sim total: 5W/4L/2BE, total R -2.36, $-942.78 at Phase-1 sizing
- Direct $ comparison is apples-to-oranges: original sizing was broken (V1/V2 bot-era). R-multiple is the honest measure.

## Part D — Score Distribution Winners vs Losers
- Winners FINAL score:   n=29 min=-6 p25=11 median=31 p75=52 max=73
- Losers  FINAL score:   n=21 min=-40 p25=-13 median=0 p75=0 max=14
- Winners BASE score:    n=29 min=-5 p25=10 median=25 p75=41 max=57
- Losers  BASE score:    n=21 min=-31 p25=0 median=0 p75=5 max=9

| bucket | winners | losers |
|---|---|---|
| -40..-36 |  (0) | # (1) |
| -30..-26 |  (0) | # (1) |
| -25..-21 |  (0) | ## (2) |
| -15..-11 |  (0) | ## (2) |
| -10..-6 | # (1) | # (1) |
| -5..-1 | # (1) | ## (2) |
| 0..4 | ## (2) | ######## (8) |
| 5..9 | # (1) | ## (2) |
| 10..14 | ### (3) | ## (2) |
| 15..19 | ## (2) |  (0) |
| 20..24 | # (1) |  (0) |
| 25..29 | ### (3) |  (0) |
| 30..34 | # (1) |  (0) |
| 40..44 | ### (3) |  (0) |
| 45..49 | ### (3) |  (0) |
| 50..54 | ## (2) |  (0) |
| 60..64 | ### (3) |  (0) |
| 65..69 | # (1) |  (0) |
| 70..74 | ## (2) |  (0) |

## Caveats
- N=50 (25W/25L ~ class-balanced by construction) — directional only, not significant.
- **DATA LEAK**: V3.1 scorer was calibrated against this dataset on 2026-04-16. Part A reject rate reflects that fit — do not interpret as out-of-sample performance.
- Cooldown / expiry / circuit gates can't fire historically (no prior-trade state). They will affect live but not this backtest.
- Debounce / zone_entry_cap / regime_floor gates: evaluated but all pass (empty state), not a meaningful check here.
- Management sim: intrabar worst-case ordering (SL before TP1 in same M5 bar). No slippage, no spread cost applied.
- Post-entry candles fetched from OANDA M5; bars marked incomplete are skipped. If a trade's window exceeds 48h the sim exits at timeout.
- $ realization model is a linear R-to-$ map at $400/trade — real Phase-1 sizing varies by pair notional, this is a first-order approximation.

## Executive Summary
Current V3 scorer rejects 39/50 (78%) of this dataset; of the rejections, 21 are original losers (true negatives) and 18 are winners (false negatives). On the 11 accepted trades the sim realizes -2.36R / $-942.78 under current Phase-1/3 management, vs. an original result of 29/50 wins at broken sizing. Winner/loser final-score medians: 31/0 (separation +31). Given the dataset was used to calibrate this scorer, these numbers are over-fit by construction — the dataset is too small (N=50) and too leaky for further calibration passes; it's only useful now as a regression sanity check that current logic hasn't regressed. Next calibration round needs a held-out test set (trades the 2026-04-16 tuning never saw).