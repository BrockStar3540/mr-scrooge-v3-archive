# JPY Pair-Grain Recovery Check

This report answers the concern that the blind tests found no JPY winners. The broad 53-regime / 62-strategy library produced no JPY survivor cells, but the stronger raw-M5 v2 search did.

## Verdict

- Raw-M5 v2 JPY pair-grain rows inspected: 10,137

- Strict JPY double-survivor cells: 209

- Gate used here: `n_disc >= 50`, `n_hold >= 20`, `mean_R_2r_disc > 0`, `mean_R_2r_hold > 0`.

- Conclusion: JPY was not absent. It was hidden by the broader formula-library aggregation and strategy set.

## Why the confusion happened

The 53-regime formula library summarized candidates at broad regime/strategy/family/session grain and found only 6 survivors overall. That sweep is useful as a challenger, but its exact textbook formulas are too coarse for JPY. The raw-M5 v2 factory uses structural M5 triggers plus M15/H1 context and finds many JPY pockets.

## Survivor Count by Pair

| pair    |   cells |   best_hold |   best_disc |   n_disc |   n_hold |
|:--------|--------:|------------:|------------:|---------:|---------:|
| USD_JPY |      66 |    1.36415  |    1.08833  |    11641 |     3279 |
| EUR_JPY |      43 |    1.03724  |    0.965379 |     5770 |     2055 |
| GBP_JPY |      38 |    1.14235  |    0.800327 |     4645 |     1600 |
| AUD_JPY |      27 |    0.71219  |    0.78448  |     3251 |     1100 |
| CHF_JPY |      22 |    0.700359 |    0.457386 |     2295 |      874 |
| CAD_JPY |      12 |    0.653957 |    0.487818 |     1090 |      330 |
| NZD_JPY |       1 |    0.127668 |    0.113434 |       97 |       27 |

## Survivor Count by Trigger

| trigger_type              |   cells |
|:--------------------------|--------:|
| T1_bb_lower_reclaim       |      47 |
| T7_pdh_proximity_reversal |      43 |
| T2_bb_upper_reject        |      36 |
| T7_pdl_proximity_reversal |      34 |
| T3_band_reentry_long      |      16 |
| T4_band_reentry_short     |      14 |
| T8_pdh_failed_breakout    |      10 |
| T8_pdl_failed_breakdown   |       9 |

## Dominant Contexts

|                               |   cells |
|:------------------------------|--------:|
| ('breakout', 'flat', 'short') |      51 |
| ('breakout', 'flat', 'long')  |      47 |
| ('breakout', 'down', 'short') |      34 |
| ('in_range', 'flat', 'long')  |      23 |
| ('breakout', 'up', 'long')    |      22 |
| ('in_range', 'flat', 'short') |      10 |
| ('in_range', 'up', 'long')    |       6 |
| ('in_range', 'down', 'long')  |       4 |
| ('breakout', 'up', 'short')   |       3 |
| ('breakout', 'down', 'long')  |       3 |
| ('in_range', 'down', 'short') |       2 |
| ('in_range', 'up', 'short')   |       2 |

## Top JPY Survivors

| trigger_type              | pair_family      | pair    | direction   | session_quarter   | m15_trend   | h1_regime   |   n_disc |   mean_R_2r_disc |   n_hold |   mean_R_2r_hold |   clean_2r_rate_disc |   clean_2r_rate_hold |   gave_back_rate_disc |   gave_back_rate_hold |
|:--------------------------|:-----------------|:--------|:------------|:------------------|:------------|:------------|---------:|-----------------:|---------:|-----------------:|---------------------:|---------------------:|----------------------:|----------------------:|
| T2_bb_upper_reject        | usd_base         | USD_JPY | short       | overlap_q4        | down        | breakout    |       61 |        0.437385  |       20 |         1.36415  |             0.377049 |             0.7      |              0.311475 |             0.05      |
| T8_pdl_failed_breakdown   | gbp_cross        | GBP_JPY | long        | overlap_q2        | up          | breakout    |       61 |        0.162768  |       27 |         1.14235  |             0.295082 |             0.518519 |              0.377049 |             0.185185  |
| T1_bb_lower_reclaim       | usd_base         | USD_JPY | long        | asia_q2           | up          | breakout    |       71 |        0.721212  |       33 |         1.13305  |             0.464789 |             0.545455 |              0.140845 |             0.181818  |
| T7_pdl_proximity_reversal | usd_base         | USD_JPY | long        | asia_q2           | up          | breakout    |      107 |        1.08833   |       25 |         1.11766  |             0.579439 |             0.68     |              0.168224 |             0.24      |
| T8_pdh_failed_breakout    | eur_cross        | EUR_JPY | short       | london_q1         | flat        | breakout    |       68 |        0.414909  |       24 |         1.03724  |             0.382353 |             0.583333 |              0.176471 |             0.125     |
| T7_pdh_proximity_reversal | usd_base         | USD_JPY | short       | asia_q3           | flat        | breakout    |      126 |        0.279074  |       41 |         0.992619 |             0.325397 |             0.487805 |              0.246032 |             0.146341  |
| T8_pdl_failed_breakdown   | usd_base         | USD_JPY | long        | asia_q2           | flat        | breakout    |      128 |        0.21949   |       33 |         0.957774 |             0.289062 |             0.575758 |              0.242188 |             0.181818  |
| T7_pdl_proximity_reversal | usd_base         | USD_JPY | long        | overlap_q2        | up          | breakout    |      125 |        0.243407  |       24 |         0.947653 |             0.28     |             0.666667 |              0.256    |             0.125     |
| T2_bb_upper_reject        | usd_base         | USD_JPY | short       | overlap_q2        | down        | breakout    |       57 |        0.641586  |       23 |         0.922483 |             0.438596 |             0.521739 |              0.280702 |             0.173913  |
| T7_pdh_proximity_reversal | usd_base         | USD_JPY | short       | overlap_q3        | down        | breakout    |      217 |        0.208447  |       20 |         0.920682 |             0.345622 |             0.5      |              0.294931 |             0.35      |
| T7_pdh_proximity_reversal | usd_base         | USD_JPY | short       | london_q2         | down        | breakout    |      183 |        0.178242  |       35 |         0.839452 |             0.311475 |             0.571429 |              0.322404 |             0.257143  |
| T7_pdl_proximity_reversal | eur_cross        | EUR_JPY | long        | overlap_q3        | up          | breakout    |      111 |        0.138852  |       26 |         0.781176 |             0.279279 |             0.461538 |              0.288288 |             0.192308  |
| T1_bb_lower_reclaim       | usd_base         | USD_JPY | long        | overlap_q1        | up          | breakout    |      114 |        0.587816  |       20 |         0.76232  |             0.464912 |             0.45     |              0.280702 |             0.15      |
| T4_band_reentry_short     | usd_base         | USD_JPY | short       | london_q1         | flat        | breakout    |       65 |        0.0779031 |       20 |         0.751404 |             0.338462 |             0.55     |              0.230769 |             0.2       |
| T1_bb_lower_reclaim       | eur_cross        | EUR_JPY | long        | london_q1         | up          | breakout    |       53 |        0.965379  |       23 |         0.74584  |             0.566038 |             0.478261 |              0.113208 |             0.130435  |
| T7_pdl_proximity_reversal | antipodean_cross | AUD_JPY | long        | asia_q2           | up          | breakout    |       99 |        0.486615  |       25 |         0.71219  |             0.333333 |             0.4      |              0.262626 |             0.28      |
| T1_bb_lower_reclaim       | antipodean_cross | CHF_JPY | long        | overlap_q3        | up          | breakout    |       65 |        0.0749751 |       27 |         0.700359 |             0.276923 |             0.481481 |              0.338462 |             0.222222  |
| T3_band_reentry_long      | eur_cross        | EUR_JPY | long        | ny_pm_q2          | down        | in_range    |       81 |        0.0925082 |       27 |         0.697485 |             0.234568 |             0.333333 |              0.148148 |             0.185185  |
| T7_pdh_proximity_reversal | usd_base         | USD_JPY | short       | asia_q2           | down        | breakout    |      155 |        0.882662  |       31 |         0.69743  |             0.503226 |             0.419355 |              0.212903 |             0.290323  |
| T8_pdh_failed_breakout    | gbp_cross        | GBP_JPY | short       | london_q1         | flat        | breakout    |       70 |        0.0696255 |       27 |         0.690492 |             0.242857 |             0.407407 |              0.257143 |             0.148148  |
| T7_pdh_proximity_reversal | gbp_cross        | GBP_JPY | short       | london_q3         | flat        | breakout    |      105 |        0.015228  |       27 |         0.69031  |             0.238095 |             0.444444 |              0.2      |             0.185185  |
| T2_bb_upper_reject        | gbp_cross        | GBP_JPY | short       | london_q1         | down        | in_range    |       64 |        0.603792  |       22 |         0.68919  |             0.484375 |             0.363636 |              0.25     |             0.0909091 |
| T7_pdl_proximity_reversal | gbp_cross        | GBP_JPY | long        | london_q3         | flat        | breakout    |      125 |        0.368884  |       27 |         0.682355 |             0.328    |             0.444444 |              0.184    |             0.111111  |
| T7_pdl_proximity_reversal | gbp_cross        | GBP_JPY | long        | overlap_q2        | up          | breakout    |       89 |        0.207632  |       41 |         0.67276  |             0.292135 |             0.463415 |              0.269663 |             0.243902  |
| T1_bb_lower_reclaim       | usd_base         | USD_JPY | long        | london_q2         | flat        | breakout    |      279 |        0.216245  |       63 |         0.664813 |             0.301075 |             0.52381  |              0.243728 |             0.174603  |
| T7_pdl_proximity_reversal | antipodean_cross | CHF_JPY | long        | overlap_q3        | up          | breakout    |      114 |        0.0178536 |       26 |         0.654928 |             0.201754 |             0.384615 |              0.315789 |             0.192308  |
| T7_pdh_proximity_reversal | antipodean_cross | CAD_JPY | short       | overlap_q4        | down        | breakout    |      106 |        0.208458  |       31 |         0.653957 |             0.264151 |             0.419355 |              0.264151 |             0.129032  |
| T8_pdl_failed_breakdown   | eur_cross        | EUR_JPY | long        | london_q1         | flat        | breakout    |       51 |        0.0361089 |       35 |         0.637637 |             0.333333 |             0.371429 |              0.235294 |             0.114286  |
| T7_pdl_proximity_reversal | gbp_cross        | GBP_JPY | long        | ny_pm_q1          | down        | breakout    |       61 |        0.295518  |       32 |         0.618997 |             0.278689 |             0.40625  |              0.131148 |             0.15625   |
| T1_bb_lower_reclaim       | antipodean_cross | CHF_JPY | long        | london_q2         | up          | breakout    |       65 |        0.448191  |       23 |         0.614095 |             0.369231 |             0.434783 |              0.261538 |             0.347826  |

## Research Implication

Do not use the broad formula-library result to conclude JPY is dead. For JPY, the correct lead is the raw-M5 v2 cell map: `H1 breakout` plus M5 rail/reclaim/failed-breakout triggers, often with M15 alignment but not always. These cells need the same synchrony and order-of-events treatment as the top family-grain survivors.
