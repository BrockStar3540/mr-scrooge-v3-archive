# Daily Textbook Trade Encyclopedia v0

Generated: 2026-05-13T17:24:37.890096+00:00
Source: research/raw-m5-winner-factory-v2/raw_m5_v2_candidate_events.parquet

## Frame

For each pair-day, choose a first-pass textbook trade from raw-M5 event candidates using only entry-time quality. If that trade loses, find the same-day repaired winner and log the strategy/factor state. First-pass and repaired winner rows are kept separate so hindsight does not contaminate what was knowable at entry.

## Counts

- First-pass textbook trades: 40,245
- First-pass net winners: 11,913 (29.6%)
- Repaired same-day winners found: 23,094
- Unique pairs: 26
- Unique trade dates: 2129

## Top Repaired Strategies

| trigger_type              | strategy_name                       | description                                          |   first_pass_count |   first_pass_win_rate |   repaired_winner_count |   median_repaired_R |
|:--------------------------|:------------------------------------|:-----------------------------------------------------|-------------------:|----------------------:|------------------------:|--------------------:|
| T1_bb_lower_reclaim       | lower_band_reclaim_snapback_long    | Mean-reversion reclaim after lower-band pressure     |               1084 |                 0.319 |                    8762 |               1.913 |
| T2_bb_upper_reject        | upper_band_rejection_snapback_short | Mean-reversion rejection after upper-band pressure   |                894 |                 0.289 |                    8354 |               1.913 |
| T7_pdl_proximity_reversal | pdl_rail_reversal_long              | Prior-day low rail reversal                          |               3803 |                 0.294 |                    1740 |               1.912 |
| T7_pdh_proximity_reversal | pdh_rail_reversal_short             | Prior-day high rail reversal                         |               3961 |                 0.275 |                    1736 |               1.907 |
| T9_session_open_fade      | session_open_impulse_fade           | Fade early session impulse after extension           |                383 |                 0.295 |                     637 |               1.912 |
| T5_ema20_reclaim_long     | ema20_reclaim_continuation_long     | Reclaim EMA20 after pullback                         |                 43 |                 0.349 |                     576 |               1.925 |
| T6_ema20_reject_short     | ema20_rejection_continuation_short  | Reject EMA20 after pullback                          |                 36 |                 0.111 |                     555 |               1.927 |
| T8_pdl_failed_breakdown   | failed_pdl_breakdown_long           | Failed breakdown below prior-day low                 |               9975 |                 0.294 |                     318 |               1.917 |
| T8_pdh_failed_breakout    | failed_pdh_breakout_short           | Failed breakout above prior-day high                 |               9982 |                 0.283 |                     295 |               1.919 |
| T10_compression_expansion | compression_expansion_breakout      | Compression release / range expansion                |                  6 |                 0.667 |                     121 |               1.912 |
| T4_band_reentry_short     | upper_rail_band_reentry_short       | Failed upside continuation; close back inside band   |               4967 |                 0.316 |                       0 |             nan     |
| T3_band_reentry_long      | lower_rail_band_reentry_long        | Failed downside continuation; close back inside band |               5111 |                 0.322 |                       0 |             nan     |

## Repaired Winners By Pair Family

| pair_family      | strategy_name                       |    n |
|:-----------------|:------------------------------------|-----:|
| usd_base         | lower_band_reclaim_snapback_long    | 3437 |
| usd_base         | upper_band_rejection_snapback_short | 3252 |
| eur_cross        | upper_band_rejection_snapback_short | 2054 |
| eur_cross        | lower_band_reclaim_snapback_long    | 1856 |
| antipodean_cross | lower_band_reclaim_snapback_long    | 1838 |
| gbp_cross        | lower_band_reclaim_snapback_long    | 1631 |
| gbp_cross        | upper_band_rejection_snapback_short | 1552 |
| antipodean_cross | upper_band_rejection_snapback_short | 1496 |
| usd_base         | pdh_rail_reversal_short             |  837 |
| usd_base         | pdl_rail_reversal_long              |  834 |
| eur_cross        | pdl_rail_reversal_long              |  389 |
| eur_cross        | pdh_rail_reversal_short             |  377 |
| antipodean_cross | pdl_rail_reversal_long              |  307 |
| antipodean_cross | pdh_rail_reversal_short             |  299 |
| usd_base         | session_open_impulse_fade           |  228 |
| gbp_cross        | pdh_rail_reversal_short             |  223 |
| gbp_cross        | pdl_rail_reversal_long              |  210 |
| antipodean_cross | ema20_reclaim_continuation_long     |  182 |
| usd_base         | ema20_rejection_continuation_short  |  178 |
| usd_base         | ema20_reclaim_continuation_long     |  177 |
| eur_cross        | session_open_impulse_fade           |  143 |
| antipodean_cross | ema20_rejection_continuation_short  |  141 |
| gbp_cross        | session_open_impulse_fade           |  133 |
| antipodean_cross | session_open_impulse_fade           |  133 |
| gbp_cross        | ema20_rejection_continuation_short  |  131 |
| gbp_cross        | ema20_reclaim_continuation_long     |  124 |
| usd_base         | failed_pdl_breakdown_long           |  108 |
| eur_cross        | ema20_rejection_continuation_short  |  105 |
| usd_base         | failed_pdh_breakout_short           |  102 |
| eur_cross        | ema20_reclaim_continuation_long     |   93 |

## First-Pass vs Repaired Meaning

- first_pass rows represent what the textbook selector would have taken without knowing the future.
- repaired_winner rows represent the same-day trade that would have won after replay. These are supervised examples for extracting strategy/regime synchrony, not claims of live knowability.
- Both row types carry entry-time factor state for later regime classification.

## Next Step

Cluster repaired_winner rows by strategy_name, pair_family, session_quarter, direction, M15/H1 context, and factor bins. Generate named microstrategy techniques from those clusters, then backtest the deterministic rules without hindsight.
