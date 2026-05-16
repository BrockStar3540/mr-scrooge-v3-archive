# routing_table_v7 summary

**Built:** 2026-05-16T04:32:09.379480+00:00
**Source:** sub_regime_islands.csv (Option B per-sub-regime mining)
**Selection:** winner_wr >= 0.33 (2:1 R break-even) AND winner_n >= 30 (sample-size floor)
**Cell key:** (sub_regime, pair, strategy, direction)  -- session_bucket dropped
**Rows:** 126

## Compared to v5

- v5: 306 rows / 60 unique winner cells / keyed on (regime53, pair, session, strategy)
- v7: 126 rows / 126 unique winner cells / keyed on (sub_regime, pair, strategy, direction)

## Family composition

- **dbb_trend**: 54 cells
- **direct**: 48 cells
- **reversal**: 24 cells

## Top sub-regimes by winner cells

- C02_32: 9 cells
- C01_35: 7 cells
- C01_34: 6 cells
- C01_38: 6 cells
- C01_27: 6 cells
- C02_27: 6 cells
- C01_39: 5 cells
- C01_29: 5 cells
- C01_26: 4 cells
- C02_30: 4 cells
- C02_39: 4 cells
- C02_25: 4 cells
- C02_35: 4 cells
- C02_24: 4 cells
- C01_23: 3 cells

## Top strategies by winner cells

- TF4_sar_long: 13 cells
- BR2_vcb_long: 11 cells
- TF2_pullback_EMA20_long: 11 cells
- TF4_sar_short: 10 cells
- TF3_supertrend_long: 7 cells
- CP1_coil_breakout_long: 6 cells
- CP1_coil_breakout_short: 6 cells
- TF2_pullback_EMA20_short: 6 cells
- MR2_bb_reversion_short: 5 cells
- TF3_supertrend_short: 5 cells
- BR2_vcb_short: 5 cells
- MR4_zscore_extreme_short: 4 cells
- MR5_williams_extreme_short: 4 cells
- MR4_zscore_extreme_long: 3 cells
- RG2_range_support_bounce_long: 3 cells

## Cells with loser_skip_rule attached

- 82 of 126 (65.1%)