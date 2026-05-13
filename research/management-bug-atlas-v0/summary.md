# Management-Bug Atlas v0

Generated: 2026-05-13T01:22:23.107679+00:00

## Premise

**47.8% of all filled trades go meaningfully green, then give it all back.**

This atlas asks: for which (strategy, pair_family, session, direction) cells is
the gave-back-green pattern dominant, and what management change does the data
suggest? Comparison is INTRA-CELL between full_tp and gave_back_green — same
entry signal, different management outcome.

## Scope

- Source: live-epoch atlas v0 (30 days, V1/V2 live era)
- Cells analyzed: 64
- Total trades covered: 90,024
- Total gave_back: 43,068
- Total full_tp: 8,160

## Recommendation distribution

| recommended_action   |   n_cells |   pct_of_trades |
|:---------------------|----------:|----------------:|
| earlier_ratchet      |        20 |            23.1 |
| insufficient_data    |        16 |             0.1 |
| needs_investigation  |        24 |            70.6 |
| skip_cell            |         4 |             6.2 |

## Worst gave-back cells (top 10 by absolute n_gave_back)

| strategy   | pair_family      | session   | direction   |   n_total |   gave_back_pct |   full_tp_pct |   mfe_median_giveback | recommended_action   | top_separator_1                                |
|:-----------|:-----------------|:----------|:------------|----------:|----------------:|--------------:|----------------------:|:---------------------|:-----------------------------------------------|
| direct     | gbp_cross        | asia      | short       |      4105 |           60.68 |         10.89 |                  0.92 | earlier_ratchet      | current_volume(higher_in_giveback, d=-0.55)    |
| direct     | usd_base         | asia      | short       |      4166 |           54.80 |          8.23 |                  0.87 | earlier_ratchet      | ema20_dist_pct(higher_in_fulltp, d=+0.66)      |
| direct     | eur_cross        | asia      | short       |      3478 |           59.55 |          7.88 |                  0.86 | earlier_ratchet      | ema20_dist_pct(higher_in_fulltp, d=+1.31)      |
| direct     | antipodean_cross | asia      | short       |      4403 |           43.29 |         13.45 |                  0.97 | needs_investigation  | regime_id(higher_in_giveback, d=-0.71)         |
| direct     | usd_base         | asia      | long        |      4685 |           40.23 |         17.37 |                  0.85 | needs_investigation  | adr_consumed(higher_in_fulltp, d=+0.66)        |
| direct     | antipodean_cross | asia      | long        |      3584 |           43.78 |         15.68 |                  0.92 | needs_investigation  | range_half(higher_in_fulltp, d=+0.72)          |
| direct     | usd_base         | ny_pm     | short       |      3144 |           49.36 |          4.64 |                  1.02 | needs_investigation  | rsi(higher_in_giveback, d=-1.20)               |
| direct     | usd_base         | london    | short       |      3457 |           44.72 |          7.43 |                  0.80 | needs_investigation  | regime_score(higher_in_fulltp, d=+0.54)        |
| direct     | gbp_cross        | ny_pm     | short       |      2678 |           55.45 |          3.40 |                  0.99 | skip_cell            | volume_ratio(higher_in_fulltp, d=+1.12)        |
| direct     | antipodean_cross | london    | short       |      3276 |           45.05 |         11.69 |                  0.97 | needs_investigation  | regime_confidence(higher_in_giveback, d=-1.16) |

## Cells with highest full_tp_pct (the cells where the bot does work)

| strategy   | pair_family      | session   | direction   |   n_total |   full_tp_pct |   gave_back_pct |   mfe_median_fulltp | recommended_action   |
|:-----------|:-----------------|:----------|:------------|----------:|--------------:|----------------:|--------------------:|:---------------------|
| direct     | usd_base         | asia      | long        |      4685 |         17.37 |           40.23 |                2.80 | needs_investigation  |
| direct     | antipodean_cross | asia      | long        |      3584 |         15.68 |           43.78 |                3.42 | needs_investigation  |
| direct     | gbp_cross        | london    | long        |      1727 |         14.36 |           45.05 |                3.89 | needs_investigation  |
| direct     | antipodean_cross | asia      | short       |      4403 |         13.45 |           43.29 |                3.49 | needs_investigation  |
| dbb_trend  | usd_base         | london    | short       |       235 |         13.19 |           58.72 |                4.92 | earlier_ratchet      |
| dbb_trend  | usd_base         | overlap   | short       |       153 |         13.07 |           56.86 |                3.57 | earlier_ratchet      |
| dbb_trend  | eur_cross        | asia      | short       |       231 |         12.99 |           69.70 |                7.35 | earlier_ratchet      |
| direct     | usd_base         | london    | long        |      2981 |         12.48 |           39.05 |                3.51 | needs_investigation  |
| dbb_trend  | gbp_cross        | asia      | short       |       179 |         12.29 |           70.39 |                5.64 | earlier_ratchet      |
| direct     | eur_cross        | asia      | long        |      3216 |         11.91 |           41.67 |                3.28 | needs_investigation  |

## skip_cell candidates (structural failure)

| strategy   | pair_family      | session   | direction   |   n_total |   full_tp_pct |   gave_back_pct |   clean_stop_pct | recommendation_basis                               |
|:-----------|:-----------------|:----------|:------------|----------:|--------------:|----------------:|-----------------:|:---------------------------------------------------|
| dbb_trend  | gbp_cross        | ny_pm     | short       |       113 |           2.7 |            79.6 |              4.4 | structural failure (full_tp 2.7%, gave_back 79.6%) |
| dbb_trend  | eur_cross        | ny_pm     | short       |       130 |           4.6 |            74.6 |              3.8 | structural failure (full_tp 4.6%, gave_back 74.6%) |
| direct     | gbp_cross        | ny_pm     | short       |      2678 |           3.4 |            55.5 |              5.9 | structural failure (full_tp 3.4%, gave_back 55.5%) |
| direct     | antipodean_cross | ny_pm     | long        |      2668 |           3.7 |            52.9 |              4.8 | structural failure (full_tp 3.7%, gave_back 52.9%) |

## earlier_ratchet candidates

| strategy   | pair_family      | session   | direction   |   n_total |   gave_back_pct |   mfe_median_giveback | top_separator_1                             | top_separator_2                           |
|:-----------|:-----------------|:----------|:------------|----------:|----------------:|----------------------:|:--------------------------------------------|:------------------------------------------|
| dbb_trend  | gbp_cross        | london    | short       |       169 |           71.01 |                  1.03 |                                             |                                           |
| dbb_trend  | gbp_cross        | asia      | short       |       179 |           70.39 |                  1.16 | v3_pairs_total(higher_in_fulltp, d=+1.39)   | adr_consumed(higher_in_fulltp, d=+1.10)   |
| dbb_trend  | antipodean_cross | ny_pm     | short       |       164 |           70.12 |                  1.16 |                                             |                                           |
| dbb_trend  | antipodean_cross | asia      | short       |       208 |           69.71 |                  0.88 |                                             |                                           |
| dbb_trend  | eur_cross        | asia      | short       |       231 |           69.70 |                  0.93 | adr_consumed(higher_in_fulltp, d=+0.58)     |                                           |
| dbb_trend  | usd_base         | asia      | short       |       315 |           69.52 |                  1.08 | atr(higher_in_fulltp, d=+0.87)              | adr_consumed(higher_in_fulltp, d=+0.83)   |
| dbb_trend  | antipodean_cross | london    | short       |       218 |           67.43 |                  1.09 |                                             |                                           |
| dbb_trend  | eur_cross        | london    | short       |       213 |           67.14 |                  1.11 | rsi(higher_in_giveback, d=-0.65)            | rr_ratio(higher_in_giveback, d=-0.50)     |
| dbb_trend  | usd_base         | ny_pm     | short       |       181 |           65.75 |                  1.17 | volume_ratio(higher_in_fulltp, d=+1.00)     | hour_utc(higher_in_giveback, d=-0.75)     |
| dbb_trend  | gbp_cross        | overlap   | short       |        98 |           64.29 |                  0.94 |                                             |                                           |
| dbb_trend  | eur_cross        | overlap   | short       |       112 |           60.71 |                  0.81 |                                             |                                           |
| direct     | gbp_cross        | asia      | short       |      4105 |           60.68 |                  0.92 | current_volume(higher_in_giveback, d=-0.55) | adr_consumed(higher_in_fulltp, d=+0.54)   |
| dbb_trend  | antipodean_cross | overlap   | short       |       130 |           60.00 |                  1.03 |                                             |                                           |
| direct     | eur_cross        | asia      | short       |      3478 |           59.55 |                  0.86 | ema20_dist_pct(higher_in_fulltp, d=+1.31)   | ema50_dist_pct(higher_in_fulltp, d=+0.83) |
| dbb_trend  | usd_base         | london    | short       |       235 |           58.72 |                  0.93 | otr_ratio(higher_in_fulltp, d=+0.52)        | avg_volume(higher_in_giveback, d=-0.44)   |

## tighter_be candidates

(none)

## quick_partial / lower_tp candidates

(none)

## entry_quality_review (entries are bad, not management)


## What the recommendations are NOT

- NOT a config change list. These are HYPOTHESES.
- NOT validated against the corpus or any holdout.
- NOT a license to change live management. Each hypothesis needs:
  - Cluster the cell's trades
  - Confirm the separator is causal, not coincidental
  - Design the deterministic rule
  - Backtest on the live-epoch data first, then corpus
  - Only then propose a config change with a clear A/B comparison

## Next branch

With this atlas as input, the trade-film ledger's `can_be_legitimately_saved`
field can now be filled for the broker-truth `bot_actual_loser` rows whose
(strategy, pair_family, session, direction) falls in an `earlier_ratchet`,
`tighter_be`, or `quick_partial` cell. The save_method captures which
recommendation applies. This is the bridge to winner-cluster discovery.