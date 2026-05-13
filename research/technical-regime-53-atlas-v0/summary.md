# Technical Regime 53 Atlas v0

Generated: 2026-05-13T17:32:45.192870+00:00

## What This Is

Brock provided a 53-regime OHLCV decision tree. This v0 attaches a mutually exclusive technical_regime_53 label to every row in the Daily Textbook Trade Encyclopedia, then summarizes which repaired-winning strategies cluster inside which regimes.

## Important v0 Caveat

This first pass uses event-level OHLCV-derived proxies already present in the raw-M5 v2 ledger: BB/RSI/EMA/BBW/echo, M15 trend, H1 regime, session, and trigger type. It preserves the priority structure and regime semantics, but it is not yet a full bar-by-bar ADX/ATR-ratio recomputation. That can be v1.

## Coverage

- Ledger rows labeled: 63,339
- Repaired winners labeled: 23,094
- Regimes represented: 37

## Top Repaired Winner Synchrony

| technical_regime_53   | technical_regime_desc      | strategy_name                       | pair_family      | direction   |   repaired_winners |   median_R |   median_mfe |   median_mae |
|:----------------------|:---------------------------|:------------------------------------|:-----------------|:------------|-------------------:|-----------:|-------------:|-------------:|
| T03                   | strong_downtrend_extended  | lower_band_reclaim_snapback_long    | usd_base         | long        |                939 |      1.932 |        2.335 |        0.395 |
| T01                   | strong_uptrend_extended    | upper_band_rejection_snapback_short | usd_base         | short       |                881 |      1.927 |        2.379 |        0.395 |
| M03                   | stop_hunt_dn_high_adx      | pdh_rail_reversal_short             | usd_base         | short       |                828 |      1.919 |        2.539 |        0.406 |
| M01                   | stop_hunt_up_high_adx      | pdl_rail_reversal_long              | usd_base         | long        |                824 |      1.921 |        2.478 |        0.422 |
| T01                   | strong_uptrend_extended    | upper_band_rejection_snapback_short | eur_cross        | short       |                626 |      1.912 |        2.260 |        0.469 |
| T06                   | moderate_downtrend         | lower_band_reclaim_snapback_long    | usd_base         | long        |                579 |      1.916 |        2.273 |        0.467 |
| T03                   | strong_downtrend_extended  | lower_band_reclaim_snapback_long    | eur_cross        | long        |                576 |      1.912 |        2.251 |        0.443 |
| T05                   | moderate_uptrend           | upper_band_rejection_snapback_short | usd_base         | short       |                565 |      1.917 |        2.352 |        0.504 |
| T03                   | strong_downtrend_extended  | lower_band_reclaim_snapback_long    | antipodean_cross | long        |                535 |      1.913 |        2.200 |        0.436 |
| T03                   | strong_downtrend_extended  | lower_band_reclaim_snapback_long    | gbp_cross        | long        |                524 |      1.907 |        2.208 |        0.444 |
| T01                   | strong_uptrend_extended    | upper_band_rejection_snapback_short | gbp_cross        | short       |                499 |      1.909 |        2.236 |        0.409 |
| T01                   | strong_uptrend_extended    | upper_band_rejection_snapback_short | antipodean_cross | short       |                447 |      1.904 |        2.268 |        0.449 |
| T07                   | directional_drift_flat     | lower_band_reclaim_snapback_long    | usd_base         | long        |                418 |      1.919 |        2.406 |        0.364 |
| M01                   | stop_hunt_up_high_adx      | pdl_rail_reversal_long              | eur_cross        | long        |                388 |      1.905 |        2.383 |        0.443 |
| T07                   | directional_drift_flat     | upper_band_rejection_snapback_short | usd_base         | short       |                375 |      1.921 |        2.545 |        0.378 |
| M03                   | stop_hunt_dn_high_adx      | pdh_rail_reversal_short             | eur_cross        | short       |                370 |      1.900 |        2.367 |        0.474 |
| M01                   | stop_hunt_up_high_adx      | pdl_rail_reversal_long              | antipodean_cross | long        |                306 |      1.899 |        2.273 |        0.467 |
| M03                   | stop_hunt_dn_high_adx      | pdh_rail_reversal_short             | antipodean_cross | short       |                299 |      1.896 |        2.351 |        0.471 |
| T05                   | moderate_uptrend           | upper_band_rejection_snapback_short | eur_cross        | short       |                286 |      1.904 |        2.248 |        0.474 |
| T07                   | directional_drift_flat     | upper_band_rejection_snapback_short | eur_cross        | short       |                280 |      1.902 |        2.318 |        0.398 |
| X04                   | expansion_moderate_trend   | lower_band_reclaim_snapback_long    | usd_base         | long        |                273 |      1.918 |        2.468 |        0.437 |
| T07                   | directional_drift_flat     | lower_band_reclaim_snapback_long    | eur_cross        | long        |                273 |      1.904 |        2.343 |        0.407 |
| T06                   | moderate_downtrend         | lower_band_reclaim_snapback_long    | eur_cross        | long        |                263 |      1.902 |        2.240 |        0.476 |
| T06                   | moderate_downtrend         | lower_band_reclaim_snapback_long    | antipodean_cross | long        |                253 |      1.901 |        2.231 |        0.495 |
| T06                   | moderate_downtrend         | lower_band_reclaim_snapback_long    | gbp_cross        | long        |                227 |      1.895 |        2.139 |        0.492 |
| T05                   | moderate_uptrend           | upper_band_rejection_snapback_short | antipodean_cross | short       |                225 |      1.898 |        2.213 |        0.523 |
| X04                   | expansion_moderate_trend   | upper_band_rejection_snapback_short | usd_base         | short       |                224 |      1.919 |        2.371 |        0.404 |
| M03                   | stop_hunt_dn_high_adx      | pdh_rail_reversal_short             | gbp_cross        | short       |                223 |      1.901 |        2.370 |        0.475 |
| X02                   | expansion_strong_downtrend | lower_band_reclaim_snapback_long    | usd_base         | long        |                220 |      1.933 |        2.342 |        0.385 |
| M01                   | stop_hunt_up_high_adx      | pdl_rail_reversal_long              | gbp_cross        | long        |                207 |      1.899 |        2.389 |        0.483 |

## First-Pass Strategy x Regime

| technical_regime_53   | technical_regime_desc       | strategy_name             | pair_family      | direction   |   first_pass_n |   first_pass_win_rate |   mean_R |
|:----------------------|:----------------------------|:--------------------------|:-----------------|:------------|---------------:|----------------------:|---------:|
| F03                   | false_break_dn_strong_trend | failed_pdl_breakdown_long | usd_base         | long        |           2411 |                 0.332 |   -0.073 |
| F01                   | false_break_up_strong_trend | failed_pdh_breakout_short | usd_base         | short       |           2350 |                 0.322 |   -0.103 |
| M03                   | stop_hunt_dn_high_adx       | pdh_rail_reversal_short   | usd_base         | short       |           1653 |                 0.283 |   -0.237 |
| F01                   | false_break_up_strong_trend | failed_pdh_breakout_short | eur_cross        | short       |           1629 |                 0.335 |   -0.079 |
| M01                   | stop_hunt_up_high_adx       | pdl_rail_reversal_long    | usd_base         | long        |           1594 |                 0.292 |   -0.210 |
| F03                   | false_break_dn_strong_trend | failed_pdl_breakdown_long | eur_cross        | long        |           1573 |                 0.316 |   -0.137 |
| F03                   | false_break_dn_strong_trend | failed_pdl_breakdown_long | antipodean_cross | long        |           1426 |                 0.309 |   -0.157 |
| F04                   | false_break_dn              | failed_pdl_breakdown_long | usd_base         | long        |           1425 |                 0.240 |   -0.361 |
| F02                   | false_break_up              | failed_pdh_breakout_short | usd_base         | short       |           1405 |                 0.223 |   -0.412 |
| F01                   | false_break_up_strong_trend | failed_pdh_breakout_short | antipodean_cross | short       |           1395 |                 0.287 |   -0.226 |
| F03                   | false_break_dn_strong_trend | failed_pdl_breakdown_long | gbp_cross        | long        |           1299 |                 0.316 |   -0.138 |
| F01                   | false_break_up_strong_trend | failed_pdh_breakout_short | gbp_cross        | short       |           1284 |                 0.295 |   -0.202 |
| M01                   | stop_hunt_up_high_adx       | pdl_rail_reversal_long    | eur_cross        | long        |            923 |                 0.293 |   -0.222 |
| M03                   | stop_hunt_dn_high_adx       | pdh_rail_reversal_short   | eur_cross        | short       |            871 |                 0.304 |   -0.186 |
| M03                   | stop_hunt_dn_high_adx       | pdh_rail_reversal_short   | antipodean_cross | short       |            809 |                 0.232 |   -0.405 |
| M01                   | stop_hunt_up_high_adx       | pdl_rail_reversal_long    | antipodean_cross | long        |            772 |                 0.312 |   -0.163 |
| F04                   | false_break_dn              | failed_pdl_breakdown_long | eur_cross        | long        |            711 |                 0.257 |   -0.319 |
| F02                   | false_break_up              | failed_pdh_breakout_short | eur_cross        | short       |            690 |                 0.235 |   -0.388 |
| F02                   | false_break_up              | failed_pdh_breakout_short | antipodean_cross | short       |            645 |                 0.209 |   -0.468 |
| F02                   | false_break_up              | failed_pdh_breakout_short | gbp_cross        | short       |            584 |                 0.219 |   -0.436 |

## Next Step

Use the top strategy/regime clusters as named technique candidates, then run deterministic raw-M5 backtests per cluster. v1 should recompute full ADX14/ATR_ratio/BB_compress from bars and compare labels against this proxy v0.
