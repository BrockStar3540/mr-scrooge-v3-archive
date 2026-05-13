# Raw-M5 v2 Survivor x Textbook Synchrony

Compares v2 double-survivor cells against the repaired/textbook winner ledger. The shared grain is pair_family x session_quarter x direction, with trigger-to-strategy-family matching where possible.

## Coverage

- v2 double-survivor cells: 335
- cells with any repaired-winner synchrony: 335
- cells with trigger-matched repaired-winner synchrony: 315
- cells with H1-breakout + M15-aligned structural gate: 168

## Top Trigger-Matched Synchrony

| trigger_type              | pair_family      | direction   | session_quarter   | m15_trend   | h1_regime   |   n_disc |   mean_R_2r_disc |   n_hold |   mean_R_2r_hold |   matched_repaired_winners | matched_strategy_examples           |   repaired_winners |
|:--------------------------|:-----------------|:------------|:------------------|:------------|:------------|---------:|-----------------:|---------:|-----------------:|---------------------------:|:------------------------------------|-------------------:|
| T2_bb_upper_reject        | usd_base         | short       | london_q4         | down        | breakout    |      264 |         0.790671 |       39 |         0.394879 |                         83 | upper_band_rejection_snapback_short |                112 |
| T7_pdh_proximity_reversal | usd_base         | short       | london_q4         | down        | breakout    |      624 |         0.441996 |      106 |         0.536883 |                         23 | pdh_rail_reversal_short             |                112 |
| T7_pdl_proximity_reversal | eur_cross        | long        | overlap_q2        | up          | breakout    |      484 |         0.344692 |       60 |         0.949201 |                         57 | pdl_rail_reversal_long              |                348 |
| T1_bb_lower_reclaim       | usd_base         | long        | london_q1         | up          | breakout    |      335 |         0.826579 |       49 |         0.890914 |                        111 | lower_band_reclaim_snapback_long    |                147 |
| T2_bb_upper_reject        | antipodean_cross | short       | overlap_q4        | down        | breakout    |      201 |         0.13667  |       43 |         0.878394 |                        177 | upper_band_rejection_snapback_short |                257 |
| T2_bb_upper_reject        | usd_base         | short       | london_q2         | down        | breakout    |      286 |         0.914772 |       54 |         0.878378 |                        182 | upper_band_rejection_snapback_short |                242 |
| T1_bb_lower_reclaim       | eur_cross        | long        | overlap_q2        | up          | breakout    |      270 |         0.30557  |       48 |         0.863511 |                        260 | lower_band_reclaim_snapback_long    |                348 |
| T1_bb_lower_reclaim       | usd_base         | long        | london_q2         | up          | breakout    |      334 |         0.845203 |       67 |         0.858675 |                        202 | lower_band_reclaim_snapback_long    |                308 |
| T2_bb_upper_reject        | usd_base         | short       | overlap_q4        | down        | breakout    |      428 |         0.289862 |      108 |         0.858542 |                        351 | upper_band_rejection_snapback_short |                474 |
| T2_bb_upper_reject        | eur_cross        | short       | overlap_q4        | down        | breakout    |      220 |         0.459489 |       31 |         0.85185  |                        312 | upper_band_rejection_snapback_short |                381 |
| T1_bb_lower_reclaim       | antipodean_cross | long        | overlap_q3        | up          | breakout    |      286 |         0.423822 |       72 |         0.746608 |                        342 | lower_band_reclaim_snapback_long    |                454 |
| T2_bb_upper_reject        | usd_base         | short       | london_q1         | down        | breakout    |      395 |         0.756322 |       60 |         0.737498 |                         99 | upper_band_rejection_snapback_short |                129 |
| T1_bb_lower_reclaim       | usd_base         | long        | asia_q2           | up          | breakout    |      214 |         0.859555 |       87 |         0.731083 |                         85 | lower_band_reclaim_snapback_long    |                112 |
| T7_pdh_proximity_reversal | usd_base         | short       | london_q3         | down        | breakout    |      800 |         0.381038 |      115 |         0.722524 |                         34 | pdh_rail_reversal_short             |                119 |
| T2_bb_upper_reject        | usd_base         | short       | london_q3         | down        | breakout    |      205 |         0.574557 |       32 |         0.708173 |                         77 | upper_band_rejection_snapback_short |                119 |
| T2_bb_upper_reject        | antipodean_cross | short       | london_q2         | down        | breakout    |      163 |         0.480986 |       47 |         0.693748 |                         84 | upper_band_rejection_snapback_short |                124 |
| T1_bb_lower_reclaim       | eur_cross        | long        | london_q2         | up          | breakout    |      206 |         0.676752 |       51 |         0.68884  |                        128 | lower_band_reclaim_snapback_long    |                191 |
| T2_bb_upper_reject        | gbp_cross        | short       | overlap_q3        | down        | breakout    |      305 |         0.515959 |       34 |         0.68347  |                        272 | upper_band_rejection_snapback_short |                354 |
| T1_bb_lower_reclaim       | eur_cross        | long        | overlap_q4        | up          | breakout    |      233 |         0.220554 |       41 |         0.677874 |                        256 | lower_band_reclaim_snapback_long    |                341 |
| T1_bb_lower_reclaim       | gbp_cross        | long        | overlap_q3        | up          | breakout    |      267 |         0.306607 |       51 |         0.675598 |                        305 | lower_band_reclaim_snapback_long    |                395 |
| T7_pdl_proximity_reversal | antipodean_cross | long        | asia_q2           | up          | breakout    |      198 |         0.395027 |       61 |         0.675265 |                         27 | pdl_rail_reversal_long              |                125 |
| T2_bb_upper_reject        | usd_base         | short       | ny_pm_q3          | down        | breakout    |      186 |         0.514042 |       55 |         0.624628 |                        158 | upper_band_rejection_snapback_short |                208 |
| T2_bb_upper_reject        | eur_cross        | short       | overlap_q3        | down        | breakout    |      320 |         0.400936 |       75 |         0.594885 |                        389 | upper_band_rejection_snapback_short |                492 |
| T7_pdl_proximity_reversal | usd_base         | long        | london_q3         | up          | breakout    |      726 |         0.440369 |      127 |         0.576492 |                         33 | pdl_rail_reversal_long              |                131 |
| T1_bb_lower_reclaim       | antipodean_cross | long        | london_q2         | up          | breakout    |      155 |         0.328235 |       49 |         0.564726 |                        132 | lower_band_reclaim_snapback_long    |                173 |
| T7_pdh_proximity_reversal | usd_base         | short       | ny_pm_q1          | down        | breakout    |      614 |         0.22534  |      150 |         0.558914 |                        120 | pdh_rail_reversal_short             |                441 |
| T7_pdl_proximity_reversal | usd_base         | long        | ny_pm_q1          | up          | breakout    |      558 |         0.208707 |      149 |         0.557106 |                        100 | pdl_rail_reversal_long              |                425 |
| T1_bb_lower_reclaim       | usd_base         | long        | london_q4         | up          | breakout    |      237 |         0.505425 |       37 |         0.550259 |                        100 | lower_band_reclaim_snapback_long    |                122 |
| T2_bb_upper_reject        | gbp_cross        | short       | overlap_q1        | down        | breakout    |      311 |         0.634621 |       41 |         0.532746 |                        125 | upper_band_rejection_snapback_short |                161 |
| T1_bb_lower_reclaim       | gbp_cross        | long        | overlap_q2        | up          | breakout    |      250 |         0.353564 |       39 |         0.532351 |                        222 | lower_band_reclaim_snapback_long    |                282 |

## Top Overall Synchrony

| trigger_type              | pair_family      | direction   | session_quarter   | m15_trend   | h1_regime   |   n_disc |   mean_R_2r_disc |   n_hold |   mean_R_2r_hold |   synchrony_score |   matched_repaired_winners |   repaired_winners |
|:--------------------------|:-----------------|:------------|:------------------|:------------|:------------|---------:|-----------------:|---------:|-----------------:|------------------:|---------------------------:|-------------------:|
| T2_bb_upper_reject        | usd_base         | short       | london_q4         | down        | breakout    |      264 |         0.790671 |       39 |         0.394879 |              8.5  |                         83 |                112 |
| T7_pdh_proximity_reversal | usd_base         | short       | london_q4         | down        | breakout    |      624 |         0.441996 |      106 |         0.536883 |              8.34 |                         23 |                112 |
| T7_pdl_proximity_reversal | eur_cross        | long        | overlap_q2        | up          | breakout    |      484 |         0.344692 |       60 |         0.949201 |              8    |                         57 |                348 |
| T1_bb_lower_reclaim       | usd_base         | long        | london_q1         | up          | breakout    |      335 |         0.826579 |       49 |         0.890914 |              8    |                        111 |                147 |
| T2_bb_upper_reject        | antipodean_cross | short       | overlap_q4        | down        | breakout    |      201 |         0.13667  |       43 |         0.878394 |              8    |                        177 |                257 |
| T2_bb_upper_reject        | usd_base         | short       | london_q2         | down        | breakout    |      286 |         0.914772 |       54 |         0.878378 |              8    |                        182 |                242 |
| T1_bb_lower_reclaim       | eur_cross        | long        | overlap_q2        | up          | breakout    |      270 |         0.30557  |       48 |         0.863511 |              8    |                        260 |                348 |
| T1_bb_lower_reclaim       | usd_base         | long        | london_q2         | up          | breakout    |      334 |         0.845203 |       67 |         0.858675 |              8    |                        202 |                308 |
| T2_bb_upper_reject        | usd_base         | short       | overlap_q4        | down        | breakout    |      428 |         0.289862 |      108 |         0.858542 |              8    |                        351 |                474 |
| T2_bb_upper_reject        | eur_cross        | short       | overlap_q4        | down        | breakout    |      220 |         0.459489 |       31 |         0.85185  |              8    |                        312 |                381 |
| T1_bb_lower_reclaim       | antipodean_cross | long        | overlap_q3        | up          | breakout    |      286 |         0.423822 |       72 |         0.746608 |              8    |                        342 |                454 |
| T2_bb_upper_reject        | usd_base         | short       | london_q1         | down        | breakout    |      395 |         0.756322 |       60 |         0.737498 |              8    |                         99 |                129 |
| T1_bb_lower_reclaim       | usd_base         | long        | asia_q2           | up          | breakout    |      214 |         0.859555 |       87 |         0.731083 |              8    |                         85 |                112 |
| T7_pdh_proximity_reversal | usd_base         | short       | london_q3         | down        | breakout    |      800 |         0.381038 |      115 |         0.722524 |              8    |                         34 |                119 |
| T2_bb_upper_reject        | usd_base         | short       | london_q3         | down        | breakout    |      205 |         0.574557 |       32 |         0.708173 |              8    |                         77 |                119 |
| T2_bb_upper_reject        | antipodean_cross | short       | london_q2         | down        | breakout    |      163 |         0.480986 |       47 |         0.693748 |              8    |                         84 |                124 |
| T1_bb_lower_reclaim       | eur_cross        | long        | london_q2         | up          | breakout    |      206 |         0.676752 |       51 |         0.68884  |              8    |                        128 |                191 |
| T2_bb_upper_reject        | gbp_cross        | short       | overlap_q3        | down        | breakout    |      305 |         0.515959 |       34 |         0.68347  |              8    |                        272 |                354 |
| T1_bb_lower_reclaim       | eur_cross        | long        | overlap_q4        | up          | breakout    |      233 |         0.220554 |       41 |         0.677874 |              8    |                        256 |                341 |
| T1_bb_lower_reclaim       | gbp_cross        | long        | overlap_q3        | up          | breakout    |      267 |         0.306607 |       51 |         0.675598 |              8    |                        305 |                395 |
| T7_pdl_proximity_reversal | antipodean_cross | long        | asia_q2           | up          | breakout    |      198 |         0.395027 |       61 |         0.675265 |              8    |                         27 |                125 |
| T2_bb_upper_reject        | usd_base         | short       | ny_pm_q3          | down        | breakout    |      186 |         0.514042 |       55 |         0.624628 |              8    |                        158 |                208 |
| T2_bb_upper_reject        | eur_cross        | short       | overlap_q3        | down        | breakout    |      320 |         0.400936 |       75 |         0.594885 |              8    |                        389 |                492 |
| T7_pdl_proximity_reversal | usd_base         | long        | london_q3         | up          | breakout    |      726 |         0.440369 |      127 |         0.576492 |              8    |                         33 |                131 |
| T1_bb_lower_reclaim       | antipodean_cross | long        | london_q2         | up          | breakout    |      155 |         0.328235 |       49 |         0.564726 |              8    |                        132 |                173 |
| T7_pdh_proximity_reversal | usd_base         | short       | ny_pm_q1          | down        | breakout    |      614 |         0.22534  |      150 |         0.558914 |              8    |                        120 |                441 |
| T7_pdl_proximity_reversal | usd_base         | long        | ny_pm_q1          | up          | breakout    |      558 |         0.208707 |      149 |         0.557106 |              8    |                        100 |                425 |
| T1_bb_lower_reclaim       | usd_base         | long        | london_q4         | up          | breakout    |      237 |         0.505425 |       37 |         0.550259 |              8    |                        100 |                122 |
| T2_bb_upper_reject        | gbp_cross        | short       | overlap_q1        | down        | breakout    |      311 |         0.634621 |       41 |         0.532746 |              8    |                        125 |                161 |
| T1_bb_lower_reclaim       | gbp_cross        | long        | overlap_q2        | up          | breakout    |      250 |         0.353564 |       39 |         0.532351 |              8    |                        222 |                282 |

## Interpretation

- Trigger-matched synchrony is strongest: blind v2 survivor and repaired winner use the same semantic setup family.
- Any repaired-winner synchrony means the same market-state pocket produced textbook winners even if the exact trigger name differs.
- The daily ledger lacks M15/H1 labels, so the H1-breakout + M15-aligned gate is verified from v2 survivor data, not from manual rows.
