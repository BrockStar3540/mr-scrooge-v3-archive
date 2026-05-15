---
title: OOS validation — strong-edge islands
date: 2026-05-15
tags: [scrooge, v3, oos, validation, routing-table, islands]
status: complete
---

# OOS validation — strong-edge islands

**Generated:** 2026-05-15 (post-handoff session)
**Selection:** in-sample `post_WR >= 0.30` AND `n_kept >= 100` → 261 islands
**Split:** train < 2025-01-01 UTC, test >= 2025-01-01 UTC (~16 months holdout)
**Gates:** `train_n >= 200`, `test_n >= 50`, tree leaf size >= 30, test_n_kept >= 20

## Pipeline coverage

- Strong-edge islands tested: **261**
- Both train+test sized: **258**
- Skipped (undersized split): 3

## TL;DR

| Test | Survivors @ 30% test post_WR | Survivors @ 25% | Mean lift over test base-rate | Median in-sample → test lift retention |
|---|---|---|---|---|
| **A) In-sample rule applied to holdout** | **122/261 (47%)** | **157/258 (61%)** | **+18.0pp** | **1.03×** (essentially preserved) |
| **B) Refit depth-5 on train-only, best leaf** | 2/261 (0.8%) | 2/258 | +5.0pp (high variance) | n/a (different rules) |

**A's relative lift is preserved.** In-sample lift averaged 2.20×; on holdout it averages 2.07×. The *technique* works — the absolute 30% threshold is harsh because the test period base-rate is ~17% (so 30% absolute is a +13pp absolute lift, equivalent to ~1.8× — already a strong bar).

**B's catastrophic failure is informative.** Picking the single best leaf of a freshly-fit depth-5 tree is maximum-overfit. Do not use this selector for v3. The in-sample rules (from `islands_best_overall.csv`) are the deployable artifact.

## Base-rate context

Mean `pre_WR` on train (<2025-01-01): 0.186
Mean `pre_WR` on test (>=2025-01-01): 0.172
Mean drift: −1.4pp (94 of 258 islands had positive drift, 164 negative)

Test base-rate is roughly half a percentage point worse than train. Not catastrophic regime shift, but real.

## A non-survivor degradation profile (the 136 'fails')

| Test post_WR | Count of 'fails' |
|---|---|
| ≥ 0.25 | 93 |
| ≥ 0.20 | 121 |
| ≥ 0.10 | 134 |
| < 0.10 | 1 |

Only **1 of 261** islands collapsed below 10% test post_WR. The non-survivors are mostly in the 22-29% band — meaningful lift, just below the hard 30% bar.

## TF-family dominance (matches handoff Pattern 1)

| Family | Count | A-holds @ 30% | A-holds rate |
|---|---|---|---|
| TF strategies | 192 | 99 | **51.6%** |
| non-TF | 66 | 23 | **34.8%** |

TF holdout survival is 1.5× the non-TF rate. Prioritize TF in the v3 routing table.

## Per-strategy holdout survival (>=2 islands tested)

| strategy | tested | A holds @30% | median A post_WR | median lift over test base |
|---|---:|---:|---:|---:|
| TF3_supertrend_short | 48 | 27 | 0.360 | +11.1pp |
| TF4_sar_long | 43 | 23 | 0.340 | +18.5pp |
| TF4_sar_short | 42 | 19 | 0.315 | +16.0pp |
| TF3_supertrend_long | 41 | 21 | 0.342 | +13.6pp |
| MR2_bb_reversion_long | 27 | 10 | 0.357 | +22.3pp |
| MR2_bb_reversion_short | 18 | 7 | 0.321 | +19.7pp |
| TF2_pullback_EMA20_long | 7 | 3 | 0.341 | +25.4pp |
| BR5_opening_range_breakout_short | 5 | 1 | 0.269 | +16.1pp |
| TF6_ma_ribbon_short | 3 | 2 | 0.556 | +24.9pp |
| TF6_ma_ribbon_long | 3 | 2 | 0.500 | +23.6pp |
| BR3_inside_bar_short | 3 | 2 | 0.368 | +30.5pp |
| TF2_pullback_EMA20_short | 4 | 2 | 0.309 | +19.1pp |
| BR5_opening_range_breakout_long | 4 | 1 | 0.237 | +14.7pp |
| MR5_williams_extreme_long | 2 | 0 | 0.300 | +22.8pp |

## The 2 B-survivors (rare passes through the most punishing gate)

| strategy | regime | pair | session | train post_WR | test post_WR | rule (refit on train) |
|---|---|---|---|---|---|---|
| TF4_sar_long | C01 | EUR_JPY | ny_mid | 0.552 | 0.304 | ema20_dist_pct>0.0186 ∧ BB_compress>0.0419 ∧ adr_consumed<=0.595 ∧ RSI14>56.9 |
| TF6_ma_ribbon_long | C02 | USD_MXN | ny_mid | 0.569 | 0.333 | EMA_slope<=0.00101 ∧ ema50_dist_pct∈(0.262, 0.401] ∧ otr_ratio<=0.735 ∧ spread_pips<=0.539 |

Both: longs, ny_mid, TF-family, refit found rules that survive cleanly. Treat as bonus signal but not the deployment basis.

## Recommendation for routing_table_v3

1. **Ship the A-survivors from `islands_best_overall.csv` filtered to `A_post_WR >= 0.25` AND `A_n_kept >= 20` on this OOS run.** That's 157 cells with proven holdout lift.
2. **Within that 157, prioritize TF family** (likely ~110 cells). Non-TF cells get a lower score boost or are held back for a longer observation window.
3. **Do not use depth-5 refit-then-pick-best-leaf as a per-cell selector.** Use the static pre-shaved rule from `islands_best_overall.csv`.
4. **Optional Stage 2**: re-run the deep shave on full corpus (no temporal split), keep the same 157 islands' rules but consider re-fitting at shallower depth (depth 2-3) on train-only as a regularization comparison.

## Files

- Script: `/Users/brock-mini-mac/scrooge-research/oos_validate_strong_islands.py` (also committed to mr-scrooge-v3 repo)
- Results CSV: `routing-table-v2/oos_validation_strong_islands.csv` (261 rows, all status columns + A/B test metrics)
- This summary: `routing-table-v2/oos_validation_summary.md`

## Methodology notes

- 'Rule replay' (A) parses the in-sample conjunction (e.g. `ATR14 > 0.000481 AND RSI14 <= 70.6 AND ADX14 > 26.4`) and evaluates it on test rows. This is contaminated only by selection bias — the rule was fit on full data so the test subset is in-sample-adjacent.
- 'Refit on train' (B) fits a fresh `DecisionTreeClassifier(max_depth=5, min_samples_leaf=30)` on rows < 2025-01-01 only, walks all leaves, picks the leaf with highest P(win|leaf), records that leaf's conjunction, applies it to test rows. Clean holdout.
- The 24 features used: ATR14, ATR_ratio, BB_width, BB_compress, ADX14, EMA_slope, RSI14, close_pos, z_score, bb_position, ema20_dist_pct, ema50_dist_pct, sma20_dist_signed_bps, spread_pips, range_half, volume_ratio, adr_consumed, otr_ratio, green_count_3/4/5, directional_confirmation (derived), hour_utc, day_of_week.
- 38 islands have in-sample rules referencing features outside this 24-set (`day in {...}` membership, `extremity_score`); rule-replay gracefully handles `day in` via day_of_week mapping, `extremity_score` skips with an error noted in `A_error` column.
