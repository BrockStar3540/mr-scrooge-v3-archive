# Microstrategy Winner Factory v0

Generated: 2026-05-13T04:25:58.451423+00:00
Corpus filled trades: 2,543,184 from 208 chunks

## Frame

This is winner-first mining. Old regime/probe labels are demoted to annotations. The miner asks: which repeated entry-state shapes produced clean 2R winners on old chart data?

## Base Rates

- Clean 2R winners: 573,800 / 2,543,184 = 22.56%
- Potential 2R reachers: 688,546 / 2,543,184 = 27.07%
- Gave-back green: 450,998 / 2,543,184 = 17.73%

## Candidate Microstrategy Cells

Criteria: n>=100, clean_2R>=20, Wilson lower bound above baseline, clean2 enrichment >=1.5x.

| pair_family      | direction   | session_bucket   | session_quarter   | bb_pos_bin   | rsi_bin   | ema20_dist_bin   | bbw_bin   | echo_ratio_bin   |   n |   clean_2r |   clean_2r_rate |   clean_2r_wilson_low |   clean2_enrichment |   potential_2r_rate |   gave_back_rate |   mean_mfe_r |   mean_mae_r |   mean_realized_r |
|:-----------------|:------------|:-----------------|:------------------|:-------------|:----------|:-----------------|:----------|:-----------------|----:|-----------:|----------------:|----------------------:|--------------------:|--------------------:|-----------------:|-------------:|-------------:|------------------:|
| usd_base         | short       | overlap          | overlap_q2        | lower_band   | low       | ema_mid          | bbw_mid   | echo_expanded    | 134 |         66 |           0.493 |                 0.409 |               2.183 |               0.522 |            0.119 |        1.451 |        0.621 |             0.591 |
| usd_base         | long        | asia             | asia_q3           | upper_band   | mid       | ema_mid          | bbw_wide  | echo_expanded    | 104 |         52 |           0.500 |                 0.406 |               2.216 |               0.519 |            0.192 |        1.427 |        0.726 |             0.494 |
| usd_base         | short       | london           | london_q1         | middle       | low       | ema_near         | bbw_wide  | echo_explosive   | 132 |         64 |           0.485 |                 0.401 |               2.149 |               0.515 |            0.212 |        1.641 |        0.594 |             0.775 |
| usd_base         | long        | london           | london_q1         | middle       | high      | ema_near         | bbw_wide  | echo_explosive   | 114 |         54 |           0.474 |                 0.384 |               2.099 |               0.491 |            0.202 |        1.567 |        0.639 |             0.569 |
| usd_base         | short       | london           | london_q2         | upper_rail   | mid       | ema_mid          | bbw_wide  | echo_compressed  | 106 |         50 |           0.472 |                 0.379 |               2.091 |               0.491 |            0.189 |        1.463 |        0.780 |             0.440 |
| usd_base         | short       | asia             | asia_q2           | lower_band   | low       | ema_mid          | bbw_wide  | echo_compressed  | 164 |         74 |           0.451 |                 0.377 |               2.000 |               0.512 |            0.171 |        1.405 |        0.700 |             0.469 |
| usd_base         | short       | asia             | asia_q2           | upper_band   | low       | ema_near         | bbw_wide  | echo_explosive   | 122 |         56 |           0.459 |                 0.373 |               2.034 |               0.508 |            0.246 |        1.578 |        0.691 |             0.544 |
| usd_base         | short       | asia             | asia_q4           | upper_band   | low       | ema_far          | bbw_mid   | echo_compressed  | 128 |         56 |           0.438 |                 0.355 |               1.939 |               0.469 |            0.125 |        1.334 |        0.839 |             0.372 |
| usd_base         | short       | overlap          | overlap_q1        | middle       | low       | ema_near         | bbw_wide  | echo_explosive   | 124 |         54 |           0.435 |                 0.351 |               1.930 |               0.468 |            0.185 |        1.561 |        0.625 |             0.657 |
| gbp_cross        | short       | london           | london_q1         | lower_band   | low       | ema_mid          | bbw_mid   | echo_explosive   | 238 |         98 |           0.412 |                 0.351 |               1.825 |               0.471 |            0.126 |        1.399 |        0.747 |             0.488 |
| antipodean_cross | short       | london           | london_q2         | lower_band   | low       | ema_mid          | bbw_wide  | echo_explosive   | 130 |         56 |           0.431 |                 0.349 |               1.909 |               0.462 |            0.146 |        1.386 |        0.761 |             0.426 |
| eur_cross        | long        | overlap          | overlap_q2        | upper_band   | high      | ema_mid          | bbw_wide  | echo_mid         | 136 |         58 |           0.426 |                 0.346 |               1.890 |               0.441 |            0.199 |        1.484 |        0.666 |             0.533 |
| antipodean_cross | short       | asia             | asia_q1           | lower_band   | low       | ema_mid          | bbw_wide  | echo_mid         | 178 |         74 |           0.416 |                 0.346 |               1.843 |               0.461 |            0.096 |        1.291 |        0.694 |             0.358 |
| usd_base         | long        | asia             | asia_q2           | lower_band   | high      | ema_near         | bbw_wide  | echo_explosive   | 126 |         54 |           0.429 |                 0.346 |               1.900 |               0.476 |            0.135 |        1.477 |        0.653 |             0.511 |
| usd_base         | short       | london           | london_q2         | lower_rail   | low       | ema_mid          | bbw_wide  | echo_expanded    | 180 |         74 |           0.411 |                 0.342 |               1.822 |               0.489 |            0.189 |        1.472 |        0.795 |             0.492 |
| antipodean_cross | long        | london           | london_q1         | lower_band   | high      | ema_near         | bbw_wide  | echo_explosive   | 102 |         44 |           0.431 |                 0.339 |               1.912 |               0.451 |            0.265 |        1.549 |        0.639 |             0.547 |
| antipodean_cross | short       | london           | london_q4         | upper_rail   | high      | ema_mid          | bbw_wide  | echo_compressed  | 114 |         48 |           0.421 |                 0.334 |               1.866 |               0.456 |            0.088 |        1.332 |        0.774 |             0.425 |
| antipodean_cross | short       | asia             | asia_q1           | upper_band   | low       | ema_far          | bbw_mid   | echo_compressed  | 174 |         70 |           0.402 |                 0.332 |               1.783 |               0.460 |            0.161 |        1.302 |        0.793 |             0.303 |
| antipodean_cross | long        | london           | london_q1         | upper_band   | high      | ema_mid          | bbw_wide  | echo_explosive   | 262 |        102 |           0.389 |                 0.332 |               1.726 |               0.458 |            0.137 |        1.416 |        0.712 |             0.522 |
| eur_cross        | long        | london           | london_q1         | middle       | high      | ema_mid          | bbw_mid   | echo_expanded    | 186 |         74 |           0.398 |                 0.330 |               1.763 |               0.419 |            0.210 |        1.331 |        0.738 |             0.301 |
| usd_base         | long        | london           | london_q1         | lower_rail   | mid       | ema_mid          | bbw_mid   | echo_mid         | 116 |         48 |           0.414 |                 0.328 |               1.834 |               0.500 |            0.155 |        1.465 |        0.766 |             0.418 |
| usd_base         | long        | asia             | asia_q2           | middle       | high      | ema_mid          | bbw_mid   | echo_compressed  | 210 |         82 |           0.390 |                 0.327 |               1.731 |               0.448 |            0.143 |        1.383 |        0.754 |             0.398 |
| eur_cross        | short       | london           | london_q2         | lower_band   | low       | ema_mid          | bbw_mid   | echo_compressed  | 122 |         50 |           0.410 |                 0.327 |               1.816 |               0.426 |            0.221 |        1.378 |        0.759 |             0.341 |
| usd_base         | short       | asia             | asia_q2           | upper_rail   | high      | ema_far          | bbw_wide  | echo_compressed  | 106 |         44 |           0.415 |                 0.326 |               1.840 |               0.472 |            0.142 |        1.341 |        0.782 |             0.321 |
| antipodean_cross | short       | asia             | asia_q1           | middle       | low       | ema_far          | bbw_mid   | echo_expanded    | 128 |         52 |           0.406 |                 0.325 |               1.801 |               0.438 |            0.094 |        1.166 |        0.725 |             0.282 |
| antipodean_cross | short       | asia             | asia_q3           | upper_rail   | high      | ema_far          | bbw_mid   | echo_mid         | 200 |         78 |           0.390 |                 0.325 |               1.729 |               0.430 |            0.185 |        1.318 |        0.793 |             0.297 |
| eur_cross        | long        | asia             | asia_q2           | upper_band   | high      | ema_far          | bbw_wide  | echo_explosive   | 118 |         48 |           0.407 |                 0.322 |               1.803 |               0.424 |            0.169 |        1.330 |        0.726 |             0.361 |
| usd_base         | long        | asia             | asia_q3           | lower_rail   | high      | ema_mid          | bbw_mid   | echo_mid         | 118 |         48 |           0.407 |                 0.322 |               1.803 |               0.441 |            0.212 |        1.351 |        0.793 |             0.270 |
| eur_cross        | long        | asia             | asia_q2           | upper_band   | high      | ema_mid          | bbw_wide  | echo_expanded    | 174 |         68 |           0.391 |                 0.321 |               1.732 |               0.414 |            0.080 |        1.230 |        0.762 |             0.299 |
| eur_cross        | short       | asia             | asia_q1           | lower_band   | high      | ema_mid          | bbw_tight | echo_compressed  | 102 |         42 |           0.412 |                 0.321 |               1.825 |               0.451 |            0.167 |        1.417 |        0.757 |             0.474 |

## Coarse Winner Pockets

| pair_family      | direction   | session_bucket   |      n |   clean_2r |   clean_2r_rate |   potential_2r_rate |   gave_back_rate |   mean_mfe_r |   mean_mae_r |   mean_realized_r |
|:-----------------|:------------|:-----------------|-------:|-----------:|----------------:|--------------------:|-----------------:|-------------:|-------------:|------------------:|
| usd_base         | short       | asia             | 148560 |      37546 |           0.253 |               0.302 |            0.197 |        1.122 |        0.905 |            -0.025 |
| antipodean_cross | short       | asia             | 131592 |      31980 |           0.243 |               0.290 |            0.186 |        1.089 |        0.887 |            -0.041 |
| usd_base         | short       | london           | 118168 |      28614 |           0.242 |               0.289 |            0.188 |        1.109 |        0.907 |            -0.018 |
| usd_base         | long        | asia             | 110598 |      28166 |           0.255 |               0.308 |            0.190 |        1.126 |        0.901 |            -0.009 |
| antipodean_cross | long        | asia             | 108538 |      27512 |           0.253 |               0.301 |            0.183 |        1.118 |        0.876 |             0.019 |
| eur_cross        | short       | asia             | 109100 |      27288 |           0.250 |               0.301 |            0.188 |        1.112 |        0.889 |            -0.012 |
| gbp_cross        | short       | asia             |  90978 |      23050 |           0.253 |               0.302 |            0.192 |        1.114 |        0.887 |            -0.016 |
| antipodean_cross | short       | london           |  97454 |      22650 |           0.232 |               0.276 |            0.189 |        1.091 |        0.880 |            -0.036 |
| usd_base         | long        | london           |  88668 |      21048 |           0.237 |               0.285 |            0.186 |        1.098 |        0.915 |            -0.035 |
| eur_cross        | short       | london           |  85362 |      19944 |           0.234 |               0.276 |            0.176 |        1.075 |        0.881 |            -0.034 |
| eur_cross        | long        | asia             |  78402 |      19278 |           0.246 |               0.294 |            0.190 |        1.094 |        0.897 |            -0.038 |
| antipodean_cross | long        | london           |  80360 |      18932 |           0.236 |               0.281 |            0.176 |        1.092 |        0.874 |             0.005 |
| usd_base         | short       | ny_pm            |  88168 |      17394 |           0.197 |               0.241 |            0.161 |        0.984 |        0.809 |            -0.021 |
| usd_base         | short       | overlap          |  79566 |      17236 |           0.217 |               0.256 |            0.166 |        1.047 |        0.863 |            -0.022 |
| gbp_cross        | long        | asia             |  68746 |      17184 |           0.250 |               0.299 |            0.182 |        1.098 |        0.890 |            -0.016 |
| gbp_cross        | short       | london           |  72290 |      16298 |           0.225 |               0.270 |            0.184 |        1.063 |        0.890 |            -0.063 |
| eur_cross        | long        | london           |  62490 |      14448 |           0.231 |               0.276 |            0.174 |        1.073 |        0.888 |            -0.031 |
| antipodean_cross | short       | ny_pm            |  75054 |      14190 |           0.189 |               0.233 |            0.174 |        0.979 |        0.821 |            -0.049 |
| antipodean_cross | short       | overlap          |  67152 |      13570 |           0.202 |               0.243 |            0.168 |        1.025 |        0.856 |            -0.059 |
| gbp_cross        | long        | london           |  56426 |      13310 |           0.236 |               0.280 |            0.180 |        1.089 |        0.879 |            -0.005 |
| usd_base         | long        | overlap          |  61408 |      13184 |           0.215 |               0.256 |            0.162 |        1.046 |        0.867 |            -0.021 |
| usd_base         | long        | ny_pm            |  64664 |      13072 |           0.202 |               0.244 |            0.155 |        0.989 |        0.804 |            -0.013 |
| eur_cross        | short       | ny_pm            |  66116 |      12280 |           0.186 |               0.229 |            0.164 |        0.961 |        0.812 |            -0.052 |
| eur_cross        | short       | overlap          |  57472 |      11924 |           0.207 |               0.244 |            0.164 |        1.025 |        0.850 |            -0.035 |
| antipodean_cross | long        | overlap          |  55010 |      11370 |           0.207 |               0.248 |            0.160 |        1.028 |        0.856 |            -0.017 |

## Next Step

Take the top candidate cells and build standalone microstrategy specs: entry definition, invalidation, management, and kill tests across discovery/holdout. v1 should generate entries directly from raw M5 bars, not inherited probe candidates.
