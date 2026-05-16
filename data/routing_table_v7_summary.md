# routing_table_v7 summary

**Built:** 2026-05-16T04:43:28.218711+00:00
**Source:** sub_regime_islands.csv (Option B per-sub-regime mining)
**Selection:** winner_wr >= 0.33 (2:1 R break-even) AND winner_n >= 30 (sample-size floor)
**Cell key:** (sub_regime, pair, strategy, direction)  -- session_bucket dropped
**Rows:** 882

## Compared to v5

- v5: 306 rows / 60 unique winner cells / keyed on (regime53, pair, session, strategy)
- v7: 882 rows / 126 unique winner cells / keyed on (sub_regime, pair, strategy, direction)

## Family composition

- **dbb_trend**: 378 cells
- **direct**: 336 cells
- **reversal**: 168 cells

## Top sub-regimes by winner cells

- C02_32: 63 cells
- C01_35: 49 cells
- C01_34: 42 cells
- C01_38: 42 cells
- C01_27: 42 cells
- C02_27: 42 cells
- C01_39: 35 cells
- C01_29: 35 cells
- C01_26: 28 cells
- C02_30: 28 cells
- C02_39: 28 cells
- C02_25: 28 cells
- C02_35: 28 cells
- C02_24: 28 cells
- C01_23: 21 cells

## Top strategies by winner cells

- TF4_sar_long: 91 cells
- BR2_vcb_long: 77 cells
- TF2_pullback_EMA20_long: 77 cells
- TF4_sar_short: 70 cells
- TF3_supertrend_long: 49 cells
- CP1_coil_breakout_long: 42 cells
- CP1_coil_breakout_short: 42 cells
- TF2_pullback_EMA20_short: 42 cells
- MR2_bb_reversion_short: 35 cells
- TF3_supertrend_short: 35 cells
- BR2_vcb_short: 35 cells
- MR4_zscore_extreme_short: 28 cells
- MR5_williams_extreme_short: 28 cells
- MR4_zscore_extreme_long: 21 cells
- RG2_range_support_bounce_long: 21 cells

## Cells with loser_skip_rule attached

- 574 of 882 (65.1%)