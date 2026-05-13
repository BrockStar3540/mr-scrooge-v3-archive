# Technical Regime 53 Atlas v1

Bar-true implementation of Brock's 53-regime OHLCV decision tree, joined to the daily textbook trade encyclopedia.

## Implementation Notes

- M5 indicators: ATR14, BB_width, ADX14, EMA50 slope, RSI14, close_pos.
- Daily baselines: prior completed 20-day average daily ATR14 and daily BB_width.
- Breakout/sweep thresholds use prior 20-bar high/low to avoid current-bar self-reference.
- Priority order follows the supplied 53-regime tree.

## Coverage

- Candidate rows labeled: 1,693,412
- Regimes represented: 34
- Repaired winners represented: 327,770

## Top Repaired Winner Synchrony

| technical_regime_53   | technical_regime_desc   | strategy_name             | pair_family      | direction   |   repaired_winners |   median_R |   median_mfe |   median_mae |   discovery_winners |   holdout_winners |
|:----------------------|:------------------------|:--------------------------|:-----------------|:------------|-------------------:|-----------:|-------------:|-------------:|--------------------:|------------------:|
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | usd_base         | long        |              26307 |    1.93016 |      2.2699  |     0.340901 |               21387 |              4920 |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | usd_base         | short       |              25539 |    1.93033 |      2.28398 |     0.341918 |               20776 |              4763 |
| C02                   | tight_coil_adx          | T7_pdh_proximity_reversal | usd_base         | short       |              14594 |    1.91739 |      2.29167 |     0.348734 |               11818 |              2776 |
| C02                   | tight_coil_adx          | T7_pdl_proximity_reversal | usd_base         | long        |              14561 |    1.91767 |      2.27531 |     0.346355 |               11870 |              2691 |
| C01                   | tight_coil_low_adx      | T1_bb_lower_reclaim       | usd_base         | long        |              11502 |    1.92312 |      2.28971 |     0.344042 |                9202 |              2300 |
| C01                   | tight_coil_low_adx      | T2_bb_upper_reject        | usd_base         | short       |              11464 |    1.92203 |      2.29313 |     0.340388 |                9086 |              2378 |
| C02                   | tight_coil_adx          | T3_band_reentry_long      | usd_base         | long        |               9766 |    1.93042 |      2.26706 |     0.33734  |                7929 |              1837 |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | eur_cross        | short       |               9638 |    1.91028 |      2.24966 |     0.372595 |                7753 |              1885 |
| C02                   | tight_coil_adx          | T4_band_reentry_short     | usd_base         | short       |               9629 |    1.9304  |      2.27765 |     0.340651 |                7853 |              1776 |
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | eur_cross        | long        |               9529 |    1.91149 |      2.24186 |     0.366798 |                7793 |              1736 |
| C01                   | tight_coil_low_adx      | T7_pdh_proximity_reversal | usd_base         | short       |               8138 |    1.91096 |      2.29615 |     0.354689 |                6653 |              1485 |
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | antipodean_cross | long        |               8106 |    1.90746 |      2.23141 |     0.378719 |                6288 |              1818 |
| C01                   | tight_coil_low_adx      | T7_pdl_proximity_reversal | usd_base         | long        |               7772 |    1.91202 |      2.28676 |     0.357714 |                6241 |              1531 |
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | gbp_cross        | long        |               7118 |    1.91043 |      2.23319 |     0.365705 |                5774 |              1344 |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | antipodean_cross | short       |               7043 |    1.90614 |      2.27117 |     0.377197 |                5519 |              1524 |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | gbp_cross        | short       |               6698 |    1.90984 |      2.24575 |     0.367356 |                5550 |              1148 |
| C02                   | tight_coil_adx          | T8_pdl_failed_breakdown   | usd_base         | long        |               5821 |    1.9343  |      2.27325 |     0.344809 |                4768 |              1053 |
| C02                   | tight_coil_adx          | T8_pdh_failed_breakout    | usd_base         | short       |               5719 |    1.93205 |      2.28004 |     0.336317 |                4692 |              1027 |
| C02                   | tight_coil_adx          | T7_pdh_proximity_reversal | eur_cross        | short       |               4624 |    1.90456 |      2.27383 |     0.374364 |                3742 |               882 |
| C02                   | tight_coil_adx          | T7_pdl_proximity_reversal | eur_cross        | long        |               4460 |    1.90371 |      2.25304 |     0.37892  |                3636 |               824 |
| C01                   | tight_coil_low_adx      | T2_bb_upper_reject        | eur_cross        | short       |               4347 |    1.90527 |      2.27026 |     0.382344 |                3492 |               855 |
| C01                   | tight_coil_low_adx      | T1_bb_lower_reclaim       | eur_cross        | long        |               4237 |    1.90517 |      2.26373 |     0.381861 |                3353 |               884 |
| C02                   | tight_coil_adx          | T7_pdh_proximity_reversal | antipodean_cross | short       |               3649 |    1.90188 |      2.26518 |     0.383314 |                2816 |               833 |
| C02                   | tight_coil_adx          | T7_pdl_proximity_reversal | antipodean_cross | long        |               3556 |    1.90295 |      2.2404  |     0.386754 |                2712 |               844 |
| C02                   | tight_coil_adx          | T4_band_reentry_short     | eur_cross        | short       |               3554 |    1.91101 |      2.25006 |     0.368733 |                2869 |               685 |
| C01                   | tight_coil_low_adx      | T3_band_reentry_long      | usd_base         | long        |               3508 |    1.92384 |      2.2816  |     0.34255  |                2833 |               675 |
| C01                   | tight_coil_low_adx      | T4_band_reentry_short     | usd_base         | short       |               3438 |    1.92169 |      2.29298 |     0.34089  |                2739 |               699 |
| C02                   | tight_coil_adx          | T3_band_reentry_long      | eur_cross        | long        |               3423 |    1.91196 |      2.23856 |     0.360669 |                2795 |               628 |
| C01                   | tight_coil_low_adx      | T1_bb_lower_reclaim       | gbp_cross        | long        |               3277 |    1.9051  |      2.25141 |     0.381397 |                2633 |               644 |
| C01                   | tight_coil_low_adx      | T2_bb_upper_reject        | gbp_cross        | short       |               3244 |    1.90513 |      2.25275 |     0.382095 |                2614 |               630 |

## First-Pass Strategy x Regime

| technical_regime_53   | technical_regime_desc   | strategy_name             | pair_family      | direction   |   first_pass_n |   first_pass_win_rate |    mean_R |   median_mfe |
|:----------------------|:------------------------|:--------------------------|:-----------------|:------------|---------------:|----------------------:|----------:|-------------:|
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | usd_base         | long        |         125465 |              0.209676 | -0.126422 |     0.80444  |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | usd_base         | short       |         120500 |              0.211942 | -0.126207 |     0.794998 |
| C02                   | tight_coil_adx          | T7_pdh_proximity_reversal | usd_base         | short       |          74236 |              0.196589 | -0.172663 |     0.744587 |
| C02                   | tight_coil_adx          | T7_pdl_proximity_reversal | usd_base         | long        |          72256 |              0.20152  | -0.146602 |     0.763029 |
| C01                   | tight_coil_low_adx      | T2_bb_upper_reject        | usd_base         | short       |          56399 |              0.203266 | -0.157409 |     0.765827 |
| C01                   | tight_coil_low_adx      | T1_bb_lower_reclaim       | usd_base         | long        |          55873 |              0.20586  | -0.146661 |     0.780563 |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | eur_cross        | short       |          52272 |              0.184382 | -0.194339 |     0.727811 |
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | eur_cross        | long        |          51628 |              0.18457  | -0.192511 |     0.72919  |
| C02                   | tight_coil_adx          | T3_band_reentry_long      | usd_base         | long        |          46258 |              0.21112  | -0.117336 |     0.810556 |
| C02                   | tight_coil_adx          | T4_band_reentry_short     | usd_base         | short       |          44964 |              0.214149 | -0.119815 |     0.804218 |
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | antipodean_cross | long        |          44028 |              0.18411  | -0.16777  |     0.7564   |
| C01                   | tight_coil_low_adx      | T7_pdh_proximity_reversal | usd_base         | short       |          42470 |              0.191618 | -0.194187 |     0.714608 |
| C01                   | tight_coil_low_adx      | T7_pdl_proximity_reversal | usd_base         | long        |          39211 |              0.19821  | -0.158988 |     0.72796  |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | antipodean_cross | short       |          39107 |              0.180096 | -0.209226 |     0.708277 |
| C02                   | tight_coil_adx          | T1_bb_lower_reclaim       | gbp_cross        | long        |          38871 |              0.183119 | -0.180234 |     0.745847 |
| C02                   | tight_coil_adx          | T2_bb_upper_reject        | gbp_cross        | short       |          37435 |              0.178923 | -0.201561 |     0.741174 |
| C02                   | tight_coil_adx          | T8_pdl_failed_breakdown   | usd_base         | long        |          28072 |              0.20736  | -0.143352 |     0.763806 |
| C02                   | tight_coil_adx          | T8_pdh_failed_breakout    | usd_base         | short       |          27788 |              0.205808 | -0.14691  |     0.749561 |
| C02                   | tight_coil_adx          | T7_pdh_proximity_reversal | eur_cross        | short       |          25359 |              0.182342 | -0.19451  |     0.702744 |
| C02                   | tight_coil_adx          | T7_pdl_proximity_reversal | eur_cross        | long        |          25340 |              0.176006 | -0.213087 |     0.697132 |

## Read This Correctly

The repaired-winner table is the strategy-discovery map: it says where the same-day winning trade existed after replay. The first-pass table says what a deterministic selector would have done before repair. A microstrategy candidate needs both: a repeated repaired-winner shape and a first-pass selector that can be made positive without hindsight.
