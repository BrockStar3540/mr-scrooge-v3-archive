# Mr. Scrooge V3 — M1 Backtest (Part B re-run)
Generated: 2026-04-20T19:22:48.257819+00:00

## Purpose
Re-run the management simulation on the 11 V3-accepted trades using **M1** bid+ask candles
instead of M5 mid. M5 under-resolves intrabar motion and may have made current V3 management
look worse than it is — especially for BE/ratchet triggers that depend on catching the +0.5R
favorable extreme before an adverse move trips full SL.

## Environment
- Granularity: **M1**, price=BAM (bid+ask+mid)
- Long SL trigger: bid_low ≤ SL.  Short SL trigger: ask_high ≥ SL.
- Long favorable extreme (MFE/BE trigger): bid_high.  Short: ask_low.
- Window: open_time - 15min → close_time + 5min (48h hard cap)
- Management params same as M5 run (config/default.json Phase-4).
- Part A (scorer tiers) reused from prior run — not re-scored.

## Per-Trade M1 Results

| tid | sym | d | tier | exit | realized_R | MFE_R | MAE_R | tp1 | be | ratchet | be_time | tp1_time |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5873 | AUD_USD | L | B | sl_hit | -1.00 | +0.00 | -1.16 | - | - | - | - | - |
| 5765 | NZD_USD | S | B | invalid_R | +0.00 | +0.00 | +0.00 | - | - | - | - | - |
| 5755 | AUD_USD | L | A | be_hit | +0.20 | +0.98 | -0.48 | - | Y | - | 2026-04-09T06:57:00 | - |
| 5723 | AUD_JPY | S | A | invalid_R | +0.00 | +0.00 | +0.00 | - | - | - | - | - |
| 5713 | AUD_CHF | S | B | be_hit | +0.24 | +0.60 | -0.21 | - | Y | - | 2026-04-08T03:36:00 | - |
| 5591 | AUD_JPY | S | A | sl_hit | -1.00 | +0.00 | -1.04 | - | - | - | - | - |
| 5573 | AUD_CHF | S | A | timeout | +1.12 | +1.54 | -0.53 | Y | Y | Y | 2026-04-08T02:08:00 | 2026-04-08T02:16:00 |
| 5509 | GBP_USD | S | B | sl_hit | -1.00 | +0.34 | -1.41 | - | - | - | - | - |
| 5464 | AUD_CAD | S | B | sl_hit | -1.00 | +0.00 | -1.16 | - | - | - | - | - |
| 5438 | USD_MXN | L | A | sl_hit | -1.00 | +0.00 | -1.12 | - | - | - | - | - |
| 5309 | USD_JPY | S | A | sl_hit | -1.00 | +0.46 | -1.02 | - | - | - | - | - |

## Aggregate — M1 vs M5

| metric | M5 (prior) | M1 (new) | delta |
|---|---|---|---|
| N BE fired | 5 | 3 | -2 |
| N TP1 hit | 1 | 1 | +0 |
| Total R | -2.35 | -4.44 | -2.09 |
| Total $ @ $400 risk | $-942.78 | $-1777.30 | $-834.52 |
| Wins / Losses / BE | (see prior) | 3W / 6L / 2BE | — |

## Side-by-Side Per Trade (M5 vs M1)

| tid | M5 exit | M5 R | M5 MFE | M1 exit | M1 R | M1 MFE | M1 MAE | delta R |
|---|---|---|---|---|---|---|---|---|
| 5873 | sl_hit | -1.00 | +0.47 | sl_hit | -1.00 | +0.00 | -1.16 | -0.00 |
| 5765 | invalid_R | +0.00 | +0.00 | invalid_R | +0.00 | +0.00 | +0.00 | +0.00 |
| 5755 | be_hit | +0.78 | +1.12 | be_hit | +0.20 | +0.98 | -0.48 | -0.58 |
| 5723 | invalid_R | +0.00 | +0.00 | invalid_R | +0.00 | +0.00 | +0.00 | +0.00 |
| 5713 | be_hit | +0.24 | +0.81 | be_hit | +0.24 | +0.60 | -0.21 | -0.00 |
| 5591 | sl_hit | -1.00 | +0.01 | sl_hit | -1.00 | +0.00 | -1.04 | +0.00 |
| 5573 | be_hit | +0.17 | +0.58 | timeout | +1.12 | +1.54 | -0.53 | +0.95 |
| 5509 | sl_hit | -1.00 | +0.47 | sl_hit | -1.00 | +0.34 | -1.41 | +0.00 |
| 5464 | be_hit | +0.27 | +0.57 | sl_hit | -1.00 | +0.00 | -1.16 | -1.27 |
| 5438 | sl_hit | -1.00 | +0.58 | sl_hit | -1.00 | +0.00 | -1.12 | +0.00 |
| 5309 | be_hit | +0.19 | +0.63 | sl_hit | -1.00 | +0.46 | -1.02 | -1.19 |

## Diagnostic: The 4 Prior M5 Full-SL Losers

The key question: on M1 tick-finer data, did these trades reach +0.5R (BE trigger)
**before** the adverse low that would have tripped the original -1R SL?

| tid | sym | reached +0.5R? | BE-trigger time | first adverse -1R time | order | M1 MFE | M1 MAE | M1 exit |
|---|---|---|---|---|---|---|---|---|
| 5873 | AUD_USD | NO | - | 2026-04-09T07:32:00 | SL only (never reached BE trigger) | +0.00 | -1.16 | sl_hit |
| 5591 | AUD_JPY | NO | - | 2026-04-08T02:36:00 | SL only (never reached BE trigger) | +0.00 | -1.04 | sl_hit |
| 5509 | GBP_USD | NO | - | 2026-04-07T08:31:00 | SL only (never reached BE trigger) | +0.34 | -1.41 | sl_hit |
| 5438 | USD_MXN | NO | - | 2026-04-01T06:37:00 | SL only (never reached BE trigger) | +0.00 | -1.12 | sl_hit |

## Conclusion

M1 data does not rescue the losers: 0/4 reached BE trigger before adverse full-SL move. Net realized R change: -2.09. This suggests the current management thresholds (be_trigger_r=0.5, tp1_r=1.0) may be too tight for this dataset's volatility profile, OR the scorer is accepting trades whose structure does not actually produce favorable excursions. Need larger out-of-sample dataset before recalibrating — this dataset is already overfit per prior caveats.

## MFE / MAE Distribution on M1

- MFE_R (n=5): min=+0.34 median=+0.60 p75=+0.98 max=+1.54
- MAE_R (n=9): min=-1.41 p25=-1.16 median=-1.04 max=-0.21
- Trades with MFE ≥ 0.5R (BE trigger reachable): **3/11**
- Trades with MFE ≥ 1.0R (TP1 reachable): **1/11**

## Caveats
- M1 is still a 60s aggregation — not true tick — so intrabar ordering is still an assumption (conservative: SL before TP1 when both in same bar).
- Spread cost not modeled; slippage not modeled (fills at exact SL/TP).
- Same dataset-overfit caveat applies: scorer was calibrated on these 50 trades.
- N=11 accepted; directional signal only.

## CRITICAL FINDING — The Dataset's Stop Distances Are Implausibly Tight

Inspecting actual M1 bid/ask at the opening bars of the 4 SL-hit trades reveals that the
CSV's `ns` (noise) column, used as the effective stop distance in BOTH M5 and M1 sims,
is too tight to survive normal bid/ask spread + sub-minute volatility:

| tid | sym | ns stop | typical spread | bar-1 bid_l-entry (long) or ask_h-entry (short) |
|---|---|---|---|---|
| 5873 | AUD_USD L | 4.3p | 1.4p | bar 07:32 bid_l=0.70263 vs entry 0.70313 → -5.0p (past 4.3p SL) |
| 5591 | AUD_JPY S | 6.7p | 2.6p | bar 02:36 ask_h=111.868 vs entry 111.798 → +7.0p (past 6.7p SL) |
| 5509 | GBP_USD S | 7.0p | 2.2p | bar 08:31 ask_h=1.32627 vs entry 1.32528 → +9.9p (past 7.0p SL) |
| 5438 | USD_MXN L | 74.4p | 45p | bar 06:37 bid_l=17.84780 vs entry 17.85610 → -83p (past 74.4p SL); spread eats 60%+ of stop |

The original dataset records these as WINS (pnl > 0). That's inconsistent with an M1 bid/ask
replay — price objectively trades below/above the nominal stop. Two possibilities:

1. **The original trades used WIDER stops than `ns`.** The CSV `sl` column contains
   clearly corrupted values (e.g. -0.0242 for AUD_USD entry 0.70313) so we can't verify.
   If the real Mantis-bot trades ran with stops set by some other formula (ATR-based,
   fixed pip floor, etc.) those may well have survived the dip and captured the win.

2. **The dataset's pnl labels are not from a real broker replay** — they may be a
   simplified did price eventually hit TP before SL calculation on mid candles with
   no spread. In that case the `won` column systematically overstates profitability.

Either way, **the management-simulation layer cannot be honestly evaluated on this
dataset without a correct stop distance.** The M1 result (-4.44R) is worse than M5
(-2.35R) not because management got worse, but because M1 correctly applies bid/ask-side
stop triggers while M5 used symmetric mid — which hid ~2R of real adverse excursion.

## Revised Conclusion

The original hypothesis — "M5 under-resolution made management look worse than it is"
— is **wrong** in the opposite direction. M5 was LENIENT, not harsh, because it used
symmetric mid candles. M1 with correct bid/ask-side triggers is harsher and realistic.
None of the 4 prior SL losers would have been saved by finer granularity — they never
reached +0.5R favorable excursion on bid/ask side because the `ns` stops are ~2-3x
tighter than typical first-minute noise + half-spread on these pairs.

## Recommendation

1. **Do NOT loosen management thresholds based on this dataset.** The problem is the
   dataset, not the thresholds.
2. **Fix the stop-distance field** before running any further management tuning:
   either reconstruct the actual SL price used in original trades from Mantis-bot logs,
   or parameterize a realistic stop (e.g. `max(ns, 2*atr_14m, 3*spread)`).
3. **Always use bid/ask-side execution** in future sims. Symmetric mid is a known
   bias that makes strategies look more profitable than they are.
4. **Out-of-sample dataset** remains the top priority — the current 50-trade set was
   used for scorer calibration (2026-04-16) AND now has revealed data-quality issues.
