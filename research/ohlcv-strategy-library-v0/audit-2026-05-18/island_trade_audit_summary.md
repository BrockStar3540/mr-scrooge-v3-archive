# Island trade audit summary

**Generated**: 2026-05-18T03:46:31.216701+00:00
**Audited islands**: 133
**Sample rows emitted**: 1762

## Audit status

- **clean**: 6
- **needs_review**: 83
- **suspect**: 44

## Tier breakdown

| Tier | Total | Clean | Needs review | Suspect |
|---|---:|---:|---:|---:|
| T1_echo_elite | 25 | 0 | 24 | 1 |
| T1_probe_alpha_breakout_ret | 4 | 0 | 4 | 0 |
| T1_probe_alpha_extended_fad | 3 | 0 | 2 | 1 |
| T1_probe_alpha_pullback_v2 | 1 | 0 | 1 | 0 |
| T1_probe_bravo_expansion_co | 2 | 0 | 2 | 0 |
| T1_probe_bravo_failed_momen | 4 | 0 | 4 | 0 |
| T1_probe_charlie_compressio | 3 | 0 | 3 | 0 |
| T1_probe_charlie_pullback_c | 2 | 0 | 2 | 0 |
| T1_probe_delta_tag_and_go_v | 3 | 0 | 3 | 0 |
| T1_probe_pure | 26 | 0 | 26 | 0 |
| T1_textbook_pure | 30 | 4 | 0 | 26 |
| T2_textbook_strong | 20 | 2 | 2 | 16 |
| T3_boundary | 10 | 0 | 10 | 0 |

## Flag prevalence

- **flag_parent_membership_mismatch**: 0 / 133
- **flag_rule_membership_mismatch**: 0 / 133
- **flag_duplicate_trade_rows**: 83 / 133
- **flag_era_leakage_suspect**: 0 / 133
- **flag_time_feature_mismatch**: 0 / 133
- **flag_factor_null_or_impossible**: 0 / 133
- **flag_outcome_pattern_suspect**: 0 / 133
- **flag_boundary_fragile**: 10 / 133
- **flag_replay_count_mismatch**: 44 / 133

## Suspect islands (do NOT promote)

| island_id | strategy | pair | dir | regime | n | w | wr | notes |
|---|---|---|---|---|---:|---:|---:|---|
| ISL_0010 | echo_box_fade_v2 | GBP_NZD | short | C01 | 16 | 16 | 1.000 | replay_n=28_claimed_n=16; replay_w=22_claimed_w=16; dup_groups=14 |
| ISL_0051 | alpha_extended_fade_v2 | USD_CHF | short | C02 | 42 | 34 | 0.809 | replay_n=72_claimed_n=42; replay_w=48_claimed_w=34; dup_groups=36; boundary_thin:ATR_ratio |
| ISL_0074 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 11 | 11 | 1.000 | replay_n=0_claimed_n=11; replay_w=0_claimed_w=11 |
| ISL_0075 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 11 | 11 | 1.000 | replay_n=0_claimed_n=11; replay_w=0_claimed_w=11 |
| ISL_0076 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0077 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 13 | 13 | 1.000 | replay_n=0_claimed_n=13; replay_w=0_claimed_w=13 |
| ISL_0078 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0079 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 11 | 11 | 1.000 | replay_n=0_claimed_n=11; replay_w=0_claimed_w=11 |
| ISL_0080 | TF3_supertrend_long | GBP_CAD | long | C01 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0081 | TF3_supertrend_long | GBP_CAD | long | C01 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0082 | TF3_supertrend_long | GBP_CAD | long | C01 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0083 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 11 | 11 | 1.000 | replay_n=0_claimed_n=11; replay_w=0_claimed_w=11 |
| ISL_0084 | TF6_ma_ribbon_long | USD_JPY | long | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0085 | TF6_ma_ribbon_long | USD_JPY | long | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0086 | TF6_ma_ribbon_long | USD_JPY | long | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0087 | TF6_ma_ribbon_long | USD_JPY | long | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0088 | TF6_ma_ribbon_long | USD_JPY | long | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0089 | TF6_ma_ribbon_long | USD_JPY | long | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0090 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 13 | 13 | 1.000 | replay_n=0_claimed_n=13; replay_w=0_claimed_w=13 |
| ISL_0091 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 13 | 13 | 1.000 | replay_n=0_claimed_n=13; replay_w=0_claimed_w=13 |
| ISL_0092 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0093 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 12 | 12 | 1.000 | replay_n=0_claimed_n=12; replay_w=0_claimed_w=12 |
| ISL_0094 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 12 | 12 | 1.000 | replay_n=0_claimed_n=12; replay_w=0_claimed_w=12 |
| ISL_0096 | TF6_ma_ribbon_long | USD_JPY | long | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0097 | TF6_ma_ribbon_short | GBP_USD | short | C02 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0098 | TF6_ma_ribbon_long | AUD_USD | long | C02 | 13 | 13 | 1.000 | replay_n=0_claimed_n=13; replay_w=0_claimed_w=13 |
| ISL_0101 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 11 | 11 | 1.000 | replay_n=0_claimed_n=11; replay_w=0_claimed_w=11 |
| ISL_0102 | TF3_supertrend_long | GBP_CAD | long | C01 | 10 | 10 | 1.000 | replay_n=0_claimed_n=10; replay_w=0_claimed_w=10 |
| ISL_0103 | TF6_ma_ribbon_long | CAD_JPY | long | C02 | 16 | 12 | 0.750 | replay_n=10_claimed_n=16; replay_w=6_claimed_w=12 |
| ISL_0104 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 18 | 16 | 0.889 | replay_n=0_claimed_n=18; replay_w=0_claimed_w=16 |
| ISL_0106 | TF3_supertrend_long | USD_MXN | long | C01 | 16 | 12 | 0.750 | replay_n=0_claimed_n=16; replay_w=0_claimed_w=12 |
| ISL_0109 | TF6_ma_ribbon_long | EUR_USD | long | C02 | 16 | 14 | 0.875 | replay_n=0_claimed_n=16; replay_w=0_claimed_w=14 |
| ISL_0110 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 16 | 15 | 0.938 | replay_n=0_claimed_n=16; replay_w=0_claimed_w=15 |
| ISL_0112 | TF3_supertrend_short | EUR_CAD | short | C02 | 19 | 15 | 0.789 | replay_n=22_claimed_n=19 |
| ISL_0113 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | 17 | 13 | 0.765 | replay_n=6_claimed_n=17; replay_w=6_claimed_w=13; boundary_thin:ATR_ratio |
| ISL_0114 | TF3_supertrend_long | GBP_CAD | long | C01 | 18 | 14 | 0.778 | replay_n=0_claimed_n=18; replay_w=0_claimed_w=14 |
| ISL_0115 | TF6_ma_ribbon_long | EUR_USD | long | C02 | 20 | 16 | 0.800 | replay_n=0_claimed_n=20; replay_w=0_claimed_w=16 |
| ISL_0116 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | 18 | 15 | 0.833 | replay_n=0_claimed_n=18; replay_w=0_claimed_w=15 |
| ISL_0117 | TF3_supertrend_short | EUR_CAD | short | C02 | 18 | 14 | 0.778 | replay_n=21_claimed_n=18 |
| ISL_0118 | TF3_supertrend_long | GBP_CAD | long | C01 | 15 | 12 | 0.800 | replay_n=0_claimed_n=15; replay_w=0_claimed_w=12 |
| ISL_0119 | TF6_ma_ribbon_long | GBP_JPY | long | C02 | 16 | 14 | 0.875 | replay_n=117_claimed_n=16; replay_w=59_claimed_w=14 |
| ISL_0120 | TF6_ma_ribbon_long | GBP_USD | long | C02 | 16 | 13 | 0.812 | replay_n=7_claimed_n=16; replay_w=6_claimed_w=13 |
| ISL_0121 | TF6_ma_ribbon_short | GBP_NZD | short | C02 | 17 | 13 | 0.765 | replay_n=9_claimed_n=17; replay_w=6_claimed_w=13; boundary_thin:volume_ratio |
| ISL_0122 | TF3_supertrend_long | GBP_CAD | long | C01 | 15 | 12 | 0.800 | replay_n=0_claimed_n=15; replay_w=0_claimed_w=12 |

## Needs-review islands (manual eyeball)

| island_id | strategy | pair | dir | regime | n | wr | flags |
|---|---|---|---|---|---:|---:|---|
| ISL_0000 | echo_box_fade_v2 | CAD_JPY | short | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0001 | echo_box_fade_v2 | CAD_JPY | short | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0002 | echo_box_fade_v2 | USD_CAD | short | C01 | 16 | 1.000 | duplicate_trade_rows |
| ISL_0003 | echo_box_fade_v2 | EUR_AUD | short | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0004 | echo_box_fade_v2 | GBP_USD | long | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0005 | echo_box_fade_v2 | GBP_USD | long | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0006 | echo_box_fade_v2 | GBP_AUD | short | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0007 | echo_box_fade_v2 | CHF_JPY | short | C01 | 16 | 1.000 | duplicate_trade_rows |
| ISL_0008 | echo_box_fade_v2 | GBP_NZD | long | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0009 | echo_box_fade_v2 | GBP_NZD | long | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0011 | echo_box_fade_v2 | CAD_JPY | short | C01 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0012 | echo_box_fade_v2 | USD_CHF | short | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0013 | echo_box_fade_v2 | EUR_AUD | short | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0014 | echo_box_fade_v2 | USD_CHF | short | C01 | 16 | 1.000 | duplicate_trade_rows |
| ISL_0015 | echo_box_fade_v2 | USD_CHF | short | C01 | 16 | 1.000 | duplicate_trade_rows |
| ISL_0016 | echo_box_fade_v2 | GBP_USD | short | C01 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0017 | echo_box_fade_v2 | USD_CAD | short | C01 | 14 | 1.000 | duplicate_trade_rows |
| ISL_0018 | echo_box_fade_v2 | EUR_CAD | short | C01 | 16 | 1.000 | duplicate_trade_rows, boundary_fragile |
| ISL_0019 | echo_box_fade_v2 | GBP_USD | long | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0020 | echo_box_fade_v2 | EUR_CHF | short | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0021 | echo_box_fade_v2 | GBP_CAD | long | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0022 | echo_box_fade_v2 | GBP_CAD | long | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0023 | echo_box_fade_v2 | GBP_AUD | short | C02 | 16 | 1.000 | duplicate_trade_rows |
| ISL_0024 | echo_box_fade_v2 | NZD_JPY | long | C02 | 16 | 1.000 | duplicate_trade_rows |
| ISL_0025 | alpha_pullback_v2 | USD_MXN | long | C02 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0026 | alpha_pullback_v2 | USD_MXN | long | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0027 | alpha_pullback_v2 | NZD_USD | long | C02 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0028 | charlie_pullback_continuation_v2 | GBP_NZD | long | C02 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0029 | charlie_compression_breakout | USD_JPY | short | C01 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0030 | bravo_failed_momentum | CAD_JPY | long | C02 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0031 | alpha_pullback_v2 | USD_CAD | short | C01 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0032 | alpha_pullback_v2 | USD_MXN | long | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0033 | bravo_expansion_continuation | GBP_AUD | short | C02 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0034 | bravo_expansion_continuation | GBP_AUD | short | C02 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0035 | alpha_pullback_v2 | NZD_USD | long | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0036 | charlie_pullback_continuation_v2 | EUR_CAD | long | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0037 | charlie_pullback_continuation_v2 | GBP_NZD | long | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0038 | charlie_pullback_continuation_v2 | GBP_NZD | long | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0039 | alpha_extended_fade_v2 | AUD_JPY | long | C02 | 18 | 1.000 | duplicate_trade_rows, boundary_fragile |
| ISL_0040 | charlie_pullback_continuation_v2 | AUD_CAD | long | C01 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0041 | alpha_pullback_v2 | USD_JPY | long | C02 | 24 | 1.000 | duplicate_trade_rows, boundary_fragile |
| ISL_0042 | charlie_pullback_continuation_v2 | EUR_AUD | short | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0043 | alpha_breakout_retest_v2 | GBP_AUD | short | C02 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0044 | alpha_pullback_v2 | NZD_USD | long | C01 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0045 | alpha_pullback_v2 | NZD_USD | long | C01 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0046 | charlie_pullback_continuation_v2 | USD_MXN | short | C01 | 22 | 1.000 | duplicate_trade_rows |
| ISL_0047 | alpha_pullback_v2 | USD_CAD | short | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0048 | charlie_pullback_continuation_v2 | USD_CHF | long | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0049 | charlie_pullback_continuation_v2 | USD_CHF | long | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0050 | alpha_pullback_v2 | USD_JPY | short | C01 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0052 | alpha_extended_fade_v2 | USD_CHF | short | C02 | 32 | 0.875 | duplicate_trade_rows |
| ISL_0053 | alpha_extended_fade_v2 | USD_CHF | short | C02 | 26 | 0.923 | duplicate_trade_rows |
| ISL_0054 | charlie_compression_breakout | EUR_CAD | long | C02 | 26 | 0.923 | duplicate_trade_rows |
| ISL_0055 | charlie_compression_breakout | GBP_USD | short | C02 | 54 | 0.778 | duplicate_trade_rows |
| ISL_0056 | charlie_compression_breakout | EUR_GBP | short | C02 | 28 | 0.893 | duplicate_trade_rows |
| ISL_0057 | delta_tag_and_go_v2 | AUD_NZD | short | C01 | 8 | 1.000 | duplicate_trade_rows |
| ISL_0058 | delta_tag_and_go_v2 | AUD_NZD | short | C01 | 12 | 0.833 | duplicate_trade_rows |
| ISL_0059 | delta_tag_and_go_v2 | AUD_NZD | short | C01 | 12 | 0.667 | duplicate_trade_rows |
| ISL_0060 | alpha_pullback_v2 | NZD_USD | long | C02 | 46 | 0.804 | duplicate_trade_rows |
| ISL_0061 | charlie_pullback_continuation_v2 | EUR_CHF | short | C02 | 26 | 0.885 | duplicate_trade_rows |
| ISL_0062 | charlie_pullback_continuation_v2 | AUD_CAD | long | C01 | 46 | 0.761 | duplicate_trade_rows |
| ISL_0063 | bravo_expansion_continuation | EUR_AUD | short | C02 | 28 | 0.964 | duplicate_trade_rows |
| ISL_0064 | bravo_expansion_continuation | GBP_NZD | short | C01 | 16 | 1.000 | duplicate_trade_rows |
| ISL_0065 | bravo_failed_momentum | NZD_USD | short | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0066 | bravo_failed_momentum | CAD_JPY | long | C02 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0067 | bravo_failed_momentum | CAD_JPY | long | C02 | 42 | 0.786 | duplicate_trade_rows |
| ISL_0068 | bravo_failed_momentum | NZD_USD | short | C01 | 20 | 1.000 | duplicate_trade_rows |
| ISL_0069 | alpha_breakout_retest_v2 | EUR_USD | long | C02 | 32 | 0.906 | duplicate_trade_rows |
| ISL_0070 | alpha_breakout_retest_v2 | CHF_JPY | short | C01 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0071 | alpha_breakout_retest_v2 | CHF_JPY | short | C01 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0072 | alpha_breakout_retest_v2 | CHF_JPY | short | C01 | 18 | 1.000 | duplicate_trade_rows |
| ISL_0105 | TF6_ma_ribbon_short | USD_CAD | short | C02 | 19 | 0.789 | boundary_fragile |
| ISL_0108 | TF6_ma_ribbon_short | USD_CAD | short | C02 | 19 | 0.789 | boundary_fragile |
| ISL_0123 | alpha_pullback_v2 | AUD_JPY | short | C01 | 50 | 0.520 | duplicate_trade_rows |
| ISL_0124 | charlie_pullback_continuation_v2 | GBP_JPY | short | C01 | 32 | 0.531 | duplicate_trade_rows |
| ISL_0125 | bravo_failed_momentum | USD_CHF | long | C02 | 6 | 1.000 | duplicate_trade_rows |
| ISL_0126 | echo_box_fade_v2 | CHF_JPY | short | C02 | 10 | 0.600 | duplicate_trade_rows |
| ISL_0127 | bravo_expansion_continuation | GBP_USD | long | C02 | 36 | 0.472 | duplicate_trade_rows |
| ISL_0128 | echo_box_fade_v2 | EUR_CAD | short | C02 | 6 | 1.000 | duplicate_trade_rows, boundary_fragile |
| ISL_0129 | alpha_breakout_retest_v2 | EUR_GBP | short | C02 | 6 | 1.000 | duplicate_trade_rows |
| ISL_0130 | alpha_pullback_v2 | GBP_AUD | short | C02 | 6 | 1.000 | duplicate_trade_rows |
| ISL_0131 | alpha_pullback_v2 | GBP_NZD | long | C02 | 6 | 1.000 | duplicate_trade_rows, boundary_fragile |
| ISL_0132 | charlie_pullback_continuation_v2 | EUR_JPY | short | C02 | 8 | 0.750 | duplicate_trade_rows |