# Live-validated parent cells

Built from 9,792 ledger rows (150 shave-passes, 4056 shave-vetos).
Filter: shave_rule_satisfied >= 2

| regime | pair | family | strategy | dir | session | passes | vetos | pass_rate | v9_tier | v9_n | v9_wr | v9_lb | current_live_block | shave_rule |
|---|---|---|---|---|---|---:|---:|---:|---|---:|---:|---:|---|---|
| C02 | EUR_CAD | direct | charlie_compression_breakout | long | ny_mid | 41 | 4 | 0.911 | Seed | 13 | 0.923 | 0.775 | below_min_tier:Seed_rank1<3 | `hour_utc>=12 AND hour_utc<=19 AND ATR_ratio>=0.0615569 AND ATR_ratio<=0.0783838 AND session_bucket==...` |
| C01 | EUR_GBP | direct | charlie_compression_breakout | long | ny_open | 37 | 0 | 1.000 | Seed | 11 | 0.818 | 0.632 | below_min_tier:Seed_rank1<3 | `ATR_ratio>=0.0644183 AND ATR_ratio<=0.0776277 AND hour_utc>=9.6 AND hour_utc<=16 AND volume_ratio<=0...` |
| C02 | USD_CHF | direct | alpha_breakout_retest_v2 | long | ny_mid | 36 | 32 | 0.529 | Seed-Pro | 17 | 0.882 | 0.747 | shave_rule_satisfied | `ADX14<=23.7788 AND session_bucket==ny_mid` |
| C01 | USD_CHF | direct | alpha_breakout_retest_v2 | short | ny_open | 24 | 6 | 0.800 | Seed | 11 | 0.818 | 0.632 | below_min_tier:Seed_rank1<3 | `ADX14>=18.0726 AND ATR_ratio<=0.0469802` |
| C02 | GBP_CHF | direct | alpha_breakout_retest_v2 | short | ny_open | 6 | 146 | 0.039 | Seed | 10 | 0.900 | 0.718 | below_min_tier:Seed_rank1<3 | `ADX14>=37.7796 AND volume_ratio<=0.826075` |
| C02 | EUR_NZD | dbb_trend | charlie_pullback_continuation_v2 | short | ny_open | 2 | 10 | 0.167 | Seed | 11 | 0.818 | 0.632 | below_min_tier:Seed_rank1<3 | `ATR_ratio>=0.0665839 AND ATR_ratio<=0.0785241 AND volume_ratio>=1.28597` |
| C01 | EUR_CHF | direct | charlie_compression_breakout | long | ny_open | 2 | 50 | 0.038 | Seed | 17 | 0.706 | 0.551 | below_min_tier:Seed_rank1<3 | `BB_compress<=0.0353186 AND RSI14>=51.2284 AND RSI14<=52.7285` |