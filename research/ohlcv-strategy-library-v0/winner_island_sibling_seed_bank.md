# Winner Island Sibling Seed Bank

This bank keeps multiple distinct winner-island descendants per mixed parent instead of collapsing immediately to one best seed. The goal is to preserve sibling micro-bots when the factor recipe materially differs.

- Raw island variants available: 438
- Diversified sibling-bank seeds kept: 141
- Parents represented: 60
- Pure sibling seeds: 6
- Holdout-clean sibling seeds: 31

## Top Seed Families By Count
| strategy_id | pair | direction | seed_count |
| --- | --- | --- | --- |
| TF3_supertrend_long | EUR_JPY | long | 6 |
| TF3_supertrend_short | USD_CAD | short | 5 |
| TF3_supertrend_long | GBP_CAD | long | 4 |
| TF3_supertrend_long | USD_MXN | long | 4 |
| TF3_supertrend_long | NZD_JPY | long | 4 |
| TF6_ma_ribbon_long | EUR_CAD | long | 4 |
| TF6_ma_ribbon_long | GBP_JPY | long | 4 |
| TF6_ma_ribbon_long | AUD_USD | long | 4 |
| TF6_ma_ribbon_long | USD_JPY | long | 4 |
| TF6_ma_ribbon_long | USD_CHF | long | 4 |
| TF6_ma_ribbon_short | EUR_CAD | short | 4 |
| TF6_ma_ribbon_short | USD_CHF | short | 4 |
| TF6_ma_ribbon_short | USD_CAD | short | 4 |
| TF6_ma_ribbon_short | GBP_USD | short | 4 |
| TF6_ma_ribbon_short | GBP_NZD | short | 4 |
| TF6_ma_ribbon_short | GBP_CHF | short | 4 |
| TF6_ma_ribbon_long | CHF_JPY | long | 4 |
| TF6_ma_ribbon_long | EUR_USD | long | 4 |
| TF6_ma_ribbon_long | CAD_JPY | long | 3 |
| TF4_sar_short | USD_MXN | short | 3 |

## Top Sibling Seeds
- mixed parent TF6_ma_ribbon_long / AUD_USD / long / C02 (399W/1300L) -> factor shave RSI14>73.24 AND BB_compress>0.1742 AND BB_compress<=0.200982 AND RSI14<=74.6344 -> seed 11W/0L (holdout 4W/0L, mean_R 1.89)
- mixed parent TF6_ma_ribbon_short / GBP_CAD / short / C02 (194W/574L) -> factor shave RSI14<=31.24 AND ATR_ratio>0.1096 AND RSI14>=23.3082 AND RSI14<=28.5995 AND volume_ratio>=0.934359 AND volume_ratio<=1.07855 AND session_bucket==london -> seed 11W/0L (holdout 1W/0L, mean_R 1.74)
- mixed parent TF3_supertrend_long / EUR_GBP / long / C02 (570W/2506L) -> factor shave price_pos>=0.721748 AND price_pos<=0.792889 AND ATR_ratio>=0.0999225 AND ATR_ratio<=0.118201 AND BB_compress>=0.137142 -> seed 10W/0L (holdout 3W/0L, mean_R 1.52)
- mixed parent TF3_supertrend_long / GBP_CAD / long / C01 (526W/2684L) -> factor shave ATR_ratio>0.06152 AND ATR_ratio>0.08849 AND BB_compress>=0.0822818 AND BB_compress<=0.114646 AND ATR_ratio<=0.0933625 AND volume_ratio>=0.820518 AND session_bucket==london -> seed 10W/0L (holdout 2W/0L, mean_R 1.82)
- mixed parent TF6_ma_ribbon_short / EUR_CAD / short / C02 (138W/370L) -> factor shave BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=23.1409 AND session_bucket==london -> seed 10W/0L (holdout 1W/0L, mean_R 1.01)
- mixed parent TF6_ma_ribbon_long / USD_JPY / long / C02 (317W/701L) -> factor shave volume_ratio>1.414 AND RSI14>72.08 AND RSI14>=85.1045 AND BB_compress>=0.150814 AND session_bucket==london -> seed 10W/0L (holdout 0W/0L, mean_R 1.09)
- mixed parent TF6_ma_ribbon_short / EUR_CAD / short / C02 (138W/370L) -> factor shave BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=17.6477 AND session_bucket==london -> seed 15W/1L (holdout 1W/0L, mean_R 0.74)
- mixed parent TF6_ma_ribbon_short / EUR_CAD / short / C02 (138W/370L) -> factor shave BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=18.9398 AND session_bucket==london -> seed 14W/1L (holdout 1W/0L, mean_R 0.79)
- mixed parent TF3_supertrend_long / GBP_CAD / long / C01 (526W/2684L) -> factor shave ATR_ratio>0.06152 AND ATR_ratio>0.08849 AND BB_compress>=0.0822818 AND BB_compress<=0.114646 AND ATR_ratio<=0.0945429 AND volume_ratio>=0.81152 AND session_bucket==london -> seed 13W/1L (holdout 2W/0L, mean_R 1.58)
- mixed parent TF3_supertrend_long / USD_MXN / long / C01 (519W/2962L) -> factor shave BB_compress>=0.0823884 AND BB_compress<=0.119532 AND hour_utc>=14 AND hour_utc<=17 AND ATR_ratio>=0.127596 -> seed 13W/1L (holdout 0W/0L, mean_R 1.44)
- mixed parent TF6_ma_ribbon_long / GBP_JPY / long / C02 (387W/1016L) -> factor shave RSI14>75.44 AND hour_utc<=16.5 AND price_pos>=0.995562 AND BB_compress>=0.121411 -> seed 13W/1L (holdout 1W/1L, mean_R 0.94)
- mixed parent TF6_ma_ribbon_short / EUR_CAD / short / C02 (138W/370L) -> factor shave BB_compress>0.2112 AND RSI14<=29.93 AND BB_compress>=0.38826 AND price_pos<=0.088569 -> seed 12W/1L (holdout 3W/0L, mean_R 0.83)
- mixed parent TF6_ma_ribbon_long / GBP_JPY / long / C02 (387W/1016L) -> factor shave BB_compress>=0.211111 AND RSI14>=75.9468 AND RSI14<=78.6866 AND session_bucket==london -> seed 12W/1L (holdout 1W/0L, mean_R 0.93)
- mixed parent TF6_ma_ribbon_long / USD_JPY / long / C02 (317W/701L) -> factor shave volume_ratio>1.414 AND RSI14>72.08 AND RSI14>=85.1045 AND BB_compress>=0.150814 -> seed 12W/1L (holdout 0W/0L, mean_R 1.07)
- mixed parent TF6_ma_ribbon_long / EUR_CAD / long / C02 (175W/443L) -> factor shave BB_compress>0.2658 AND hour_utc<=14.5 AND price_pos>=0.788814 AND BB_compress<=0.281872 -> seed 11W/1L (holdout 1W/0L, mean_R 1.07)
- mixed parent TF6_ma_ribbon_short / USD_CHF / short / C02 (278W/577L) -> factor shave BB_compress>0.1086 AND ADX14<=44 AND BB_compress>=0.331059 AND volume_ratio>=0.840106 AND volume_ratio<=1.06083 -> seed 10W/1L (holdout 4W/0L, mean_R 0.98)
- mixed parent TF3_supertrend_long / AUD_CAD / long / C02 (554W/2309L) -> factor shave BB_compress>0.08308 AND volume_ratio>0.6594 AND hour_utc>=2 AND hour_utc<=6 AND ATR_ratio>=0.0945357 AND ATR_ratio<=0.114458 -> seed 10W/1L (holdout 3W/0L, mean_R 1.28)
- mixed parent TF3_supertrend_long / AUD_CAD / long / C02 (554W/2309L) -> factor shave BB_compress>0.08308 AND volume_ratio>0.6594 AND hour_utc>=2 AND hour_utc<=6 AND ATR_ratio>=0.0945357 AND ATR_ratio<=0.114458 AND session_bucket==asia -> seed 10W/1L (holdout 3W/0L, mean_R 1.28)
- mixed parent TF3_supertrend_short / USD_MXN / short / C01 (616W/2768L) -> factor shave BB_compress>=0.0942467 AND ATR_ratio>=0.128233 AND ATR_ratio<=0.153631 AND hour_utc>=15 AND hour_utc<=16.7 -> seed 10W/1L (holdout 3W/0L, mean_R 1.20)
- mixed parent TF6_ma_ribbon_long / USD_CHF / long / C02 (190W/576L) -> factor shave RSI14>76.2 AND RSI14>82.55 AND hour_utc>=8 AND hour_utc<=13 AND RSI14>=85.8443 -> seed 10W/1L (holdout 2W/0L, mean_R 0.77)
- mixed parent TF6_ma_ribbon_long / USD_CHF / long / C02 (190W/576L) -> factor shave RSI14>76.2 AND RSI14>82.55 AND hour_utc>=8 AND hour_utc<=13 AND RSI14>=85.8443 AND session_bucket==london -> seed 10W/1L (holdout 2W/0L, mean_R 0.77)
- mixed parent TF6_ma_ribbon_long / EUR_CAD / long / C02 (175W/443L) -> factor shave BB_compress>0.2658 AND hour_utc<=14.5 AND price_pos>=0.788814 AND BB_compress<=0.281872 AND session_bucket==london -> seed 10W/1L (holdout 1W/0L, mean_R 0.98)
- mixed parent TF6_ma_ribbon_short / GBP_USD / short / C02 (329W/884L) -> factor shave BB_compress>=0.246076 AND volume_ratio>=1.81351 AND session_bucket==london -> seed 10W/1L (holdout 1W/0L, mean_R 0.76)
- mixed parent TF4_sar_long / CAD_JPY / long / C01 (820W/5343L) -> factor shave hour_utc<=17.5 AND BB_compress>0.06966 AND ATR_ratio>=0.116452 AND ATR_ratio<=0.147686 AND BB_compress>=0.102157 AND BB_compress<=0.129548 AND hour_utc>=14 AND hour_utc<=15 -> seed 10W/1L (holdout 0W/0L, mean_R 1.44)
- mixed parent TF4_sar_long / CAD_JPY / long / C01 (820W/5343L) -> factor shave hour_utc<=17.5 AND BB_compress>0.06966 AND ATR_ratio>=0.116452 AND ATR_ratio<=0.147686 AND BB_compress>=0.102157 AND BB_compress<=0.129548 AND hour_utc>=14 AND hour_utc<=15 AND session_bucket==london -> seed 10W/1L (holdout 0W/0L, mean_R 1.44)
- mixed parent TF3_supertrend_long / USD_MXN / long / C01 (519W/2962L) -> factor shave hour_utc>=11 AND hour_utc<=17 AND BB_compress>=0.0986055 AND BB_compress<=0.123381 AND ATR_ratio>=0.134696 -> seed 10W/1L (holdout 0W/0L, mean_R 1.40)
- mixed parent TF6_ma_ribbon_long / USD_JPY / long / C02 (317W/701L) -> factor shave volume_ratio>1.414 AND RSI14>72.08 AND RSI14>=86.0487 AND session_bucket==london -> seed 10W/1L (holdout 0W/0L, mean_R 0.78)
- mixed parent TF6_ma_ribbon_long / AUD_USD / long / C02 (399W/1300L) -> factor shave RSI14>=74.1631 AND BB_compress>=0.178026 AND BB_compress<=0.211574 AND session_bucket==london AND price_pos<=0.966034 -> seed 15W/2L (holdout 3W/0L, mean_R 1.27)
- mixed parent TF6_ma_ribbon_long / EUR_USD / long / C02 (252W/562L) -> factor shave volume_ratio>0.8421 AND ATR_ratio>0.1056 AND RSI14>=80.3951 AND session_bucket==london AND price_pos<=0.993847 -> seed 15W/2L (holdout 3W/1L, mean_R 0.57)
- mixed parent TF6_ma_ribbon_long / CHF_JPY / long / C02 (211W/554L) -> factor shave RSI14>69.79 AND ATR_ratio>0.08828 AND volume_ratio>=1.84027 AND RSI14<=84.3824 -> seed 13W/2L (holdout 1W/0L, mean_R 0.99)

## Ranked Sibling Table
| seed_bank_rank | strategy_id | pair | direction | technical_regime_53 | factor_signature | rule | wins | losses | wr | hold_wins | hold_losses | mean_R |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TF6_ma_ribbon_long | AUD_USD | long | C02 | RSI14 + BB_compress | RSI14>73.24 AND BB_compress>0.1742 AND BB_compress<=0.200982 AND RSI14<=74.6344 | 11 | 0 | 1 | 4 | 0 | 1.89433 |
| 2 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | RSI14 + ATR_ratio + volume_ratio + session_bucket | RSI14<=31.24 AND ATR_ratio>0.1096 AND RSI14>=23.3082 AND RSI14<=28.5995 AND volume_ratio>=0.934359 AND volume_ratio<=1.07855 AND session_bucket==london | 11 | 0 | 1 | 1 | 0 | 1.74372 |
| 3 | TF3_supertrend_long | EUR_GBP | long | C02 | price_pos + ATR_ratio + BB_compress | price_pos>=0.721748 AND price_pos<=0.792889 AND ATR_ratio>=0.0999225 AND ATR_ratio<=0.118201 AND BB_compress>=0.137142 | 10 | 0 | 1 | 3 | 0 | 1.52307 |
| 4 | TF3_supertrend_long | GBP_CAD | long | C01 | ATR_ratio + BB_compress + volume_ratio + session_bucket | ATR_ratio>0.06152 AND ATR_ratio>0.08849 AND BB_compress>=0.0822818 AND BB_compress<=0.114646 AND ATR_ratio<=0.0933625 AND volume_ratio>=0.820518 AND session_bucket==london | 10 | 0 | 1 | 2 | 0 | 1.81686 |
| 5 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | BB_compress + price_pos + RSI14 + session_bucket | BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=23.1409 AND session_bucket==london | 10 | 0 | 1 | 1 | 0 | 1.01419 |
| 6 | TF6_ma_ribbon_long | USD_JPY | long | C02 | volume_ratio + RSI14 + BB_compress + session_bucket | volume_ratio>1.414 AND RSI14>72.08 AND RSI14>=85.1045 AND BB_compress>=0.150814 AND session_bucket==london | 10 | 0 | 1 | 0 | 0 | 1.08831 |
| 7 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | BB_compress + price_pos + RSI14 + session_bucket | BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=17.6477 AND session_bucket==london | 15 | 1 | 0.9375 | 1 | 0 | 0.742658 |
| 8 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | BB_compress + price_pos + RSI14 + session_bucket | BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=18.9398 AND session_bucket==london | 14 | 1 | 0.933333 | 1 | 0 | 0.789717 |
| 9 | TF3_supertrend_long | GBP_CAD | long | C01 | ATR_ratio + BB_compress + volume_ratio + session_bucket | ATR_ratio>0.06152 AND ATR_ratio>0.08849 AND BB_compress>=0.0822818 AND BB_compress<=0.114646 AND ATR_ratio<=0.0945429 AND volume_ratio>=0.81152 AND session_bucket==london | 13 | 1 | 0.928571 | 2 | 0 | 1.58383 |
| 10 | TF3_supertrend_long | USD_MXN | long | C01 | BB_compress + hour_utc + ATR_ratio | BB_compress>=0.0823884 AND BB_compress<=0.119532 AND hour_utc>=14 AND hour_utc<=17 AND ATR_ratio>=0.127596 | 13 | 1 | 0.928571 | 0 | 0 | 1.44152 |
| 11 | TF6_ma_ribbon_long | GBP_JPY | long | C02 | RSI14 + hour_utc + price_pos + BB_compress | RSI14>75.44 AND hour_utc<=16.5 AND price_pos>=0.995562 AND BB_compress>=0.121411 | 13 | 1 | 0.928571 | 1 | 1 | 0.938836 |
| 12 | TF6_ma_ribbon_short | EUR_CAD | short | C02 | BB_compress + RSI14 + price_pos | BB_compress>0.2112 AND RSI14<=29.93 AND BB_compress>=0.38826 AND price_pos<=0.088569 | 12 | 1 | 0.923077 | 3 | 0 | 0.834522 |
| 13 | TF6_ma_ribbon_long | GBP_JPY | long | C02 | BB_compress + RSI14 + session_bucket | BB_compress>=0.211111 AND RSI14>=75.9468 AND RSI14<=78.6866 AND session_bucket==london | 12 | 1 | 0.923077 | 1 | 0 | 0.931432 |
| 14 | TF6_ma_ribbon_long | USD_JPY | long | C02 | volume_ratio + RSI14 + BB_compress | volume_ratio>1.414 AND RSI14>72.08 AND RSI14>=85.1045 AND BB_compress>=0.150814 | 12 | 1 | 0.923077 | 0 | 0 | 1.06793 |
| 15 | TF6_ma_ribbon_long | EUR_CAD | long | C02 | BB_compress + hour_utc + price_pos | BB_compress>0.2658 AND hour_utc<=14.5 AND price_pos>=0.788814 AND BB_compress<=0.281872 | 11 | 1 | 0.916667 | 1 | 0 | 1.06526 |
| 16 | TF6_ma_ribbon_short | USD_CHF | short | C02 | BB_compress + ADX14 + volume_ratio | BB_compress>0.1086 AND ADX14<=44 AND BB_compress>=0.331059 AND volume_ratio>=0.840106 AND volume_ratio<=1.06083 | 10 | 1 | 0.909091 | 4 | 0 | 0.982004 |
| 17 | TF3_supertrend_long | AUD_CAD | long | C02 | BB_compress + volume_ratio + hour_utc + ATR_ratio | BB_compress>0.08308 AND volume_ratio>0.6594 AND hour_utc>=2 AND hour_utc<=6 AND ATR_ratio>=0.0945357 AND ATR_ratio<=0.114458 | 10 | 1 | 0.909091 | 3 | 0 | 1.28002 |
| 18 | TF3_supertrend_long | AUD_CAD | long | C02 | BB_compress + volume_ratio + hour_utc + ATR_ratio + session_bucket | BB_compress>0.08308 AND volume_ratio>0.6594 AND hour_utc>=2 AND hour_utc<=6 AND ATR_ratio>=0.0945357 AND ATR_ratio<=0.114458 AND session_bucket==asia | 10 | 1 | 0.909091 | 3 | 0 | 1.28002 |
| 19 | TF3_supertrend_short | USD_MXN | short | C01 | BB_compress + ATR_ratio + hour_utc | BB_compress>=0.0942467 AND ATR_ratio>=0.128233 AND ATR_ratio<=0.153631 AND hour_utc>=15 AND hour_utc<=16.7 | 10 | 1 | 0.909091 | 3 | 0 | 1.20014 |
| 20 | TF6_ma_ribbon_long | USD_CHF | long | C02 | RSI14 + hour_utc | RSI14>76.2 AND RSI14>82.55 AND hour_utc>=8 AND hour_utc<=13 AND RSI14>=85.8443 | 10 | 1 | 0.909091 | 2 | 0 | 0.766141 |
| 21 | TF6_ma_ribbon_long | USD_CHF | long | C02 | RSI14 + hour_utc + session_bucket | RSI14>76.2 AND RSI14>82.55 AND hour_utc>=8 AND hour_utc<=13 AND RSI14>=85.8443 AND session_bucket==london | 10 | 1 | 0.909091 | 2 | 0 | 0.766141 |
| 22 | TF6_ma_ribbon_long | EUR_CAD | long | C02 | BB_compress + hour_utc + price_pos + session_bucket | BB_compress>0.2658 AND hour_utc<=14.5 AND price_pos>=0.788814 AND BB_compress<=0.281872 AND session_bucket==london | 10 | 1 | 0.909091 | 1 | 0 | 0.98028 |
| 23 | TF6_ma_ribbon_short | GBP_USD | short | C02 | BB_compress + volume_ratio + session_bucket | BB_compress>=0.246076 AND volume_ratio>=1.81351 AND session_bucket==london | 10 | 1 | 0.909091 | 1 | 0 | 0.76044 |
| 24 | TF4_sar_long | CAD_JPY | long | C01 | hour_utc + BB_compress + ATR_ratio | hour_utc<=17.5 AND BB_compress>0.06966 AND ATR_ratio>=0.116452 AND ATR_ratio<=0.147686 AND BB_compress>=0.102157 AND BB_compress<=0.129548 AND hour_utc>=14 AND hour_utc<=15 | 10 | 1 | 0.909091 | 0 | 0 | 1.4377 |
| 25 | TF4_sar_long | CAD_JPY | long | C01 | hour_utc + BB_compress + ATR_ratio + session_bucket | hour_utc<=17.5 AND BB_compress>0.06966 AND ATR_ratio>=0.116452 AND ATR_ratio<=0.147686 AND BB_compress>=0.102157 AND BB_compress<=0.129548 AND hour_utc>=14 AND hour_utc<=15 AND session_bucket==london | 10 | 1 | 0.909091 | 0 | 0 | 1.4377 |
| 26 | TF3_supertrend_long | USD_MXN | long | C01 | hour_utc + BB_compress + ATR_ratio | hour_utc>=11 AND hour_utc<=17 AND BB_compress>=0.0986055 AND BB_compress<=0.123381 AND ATR_ratio>=0.134696 | 10 | 1 | 0.909091 | 0 | 0 | 1.39835 |
| 27 | TF6_ma_ribbon_long | USD_JPY | long | C02 | volume_ratio + RSI14 + session_bucket | volume_ratio>1.414 AND RSI14>72.08 AND RSI14>=86.0487 AND session_bucket==london | 10 | 1 | 0.909091 | 0 | 0 | 0.776069 |
| 28 | TF6_ma_ribbon_long | AUD_USD | long | C02 | RSI14 + BB_compress + session_bucket + price_pos | RSI14>=74.1631 AND BB_compress>=0.178026 AND BB_compress<=0.211574 AND session_bucket==london AND price_pos<=0.966034 | 15 | 2 | 0.882353 | 3 | 0 | 1.26842 |
| 29 | TF6_ma_ribbon_long | EUR_USD | long | C02 | volume_ratio + ATR_ratio + RSI14 + session_bucket + price_pos | volume_ratio>0.8421 AND ATR_ratio>0.1056 AND RSI14>=80.3951 AND session_bucket==london AND price_pos<=0.993847 | 15 | 2 | 0.882353 | 3 | 1 | 0.571068 |
| 30 | TF6_ma_ribbon_long | CHF_JPY | long | C02 | RSI14 + ATR_ratio + volume_ratio | RSI14>69.79 AND ATR_ratio>0.08828 AND volume_ratio>=1.84027 AND RSI14<=84.3824 | 13 | 2 | 0.866667 | 1 | 0 | 0.985753 |
| 31 | TF6_ma_ribbon_long | GBP_JPY | long | C02 | RSI14 + price_pos + BB_compress | RSI14>=76.3831 AND price_pos>=0.995549 AND BB_compress>=0.137306 | 13 | 2 | 0.866667 | 1 | 1 | 0.951205 |
| 32 | TF6_ma_ribbon_long | GBP_JPY | long | C02 | RSI14 + hour_utc + price_pos | RSI14>75.44 AND hour_utc<=16.5 AND RSI14<=79.3886 AND price_pos<=0.866648 | 12 | 2 | 0.857143 | 3 | 0 | 0.860108 |
| 33 | TF6_ma_ribbon_short | GBP_CAD | short | C02 | RSI14 + ATR_ratio + volume_ratio | RSI14<=31.24 AND ATR_ratio>0.1096 AND volume_ratio>=0.895399 AND volume_ratio<=1.10017 AND RSI14>=25.4838 AND RSI14<=28.3815 | 12 | 2 | 0.857143 | 1 | 0 | 1.16259 |
| 34 | TF3_supertrend_long | EUR_CAD | long | C02 | ATR_ratio + RSI14 + volume_ratio + BB_compress | ATR_ratio>0.05833 AND RSI14>56.8 AND volume_ratio>=1.13699 AND volume_ratio<=1.50361 AND BB_compress>=0.0954077 AND BB_compress<=0.11537 AND ATR_ratio>=0.0930968 | 11 | 2 | 0.846154 | 4 | 0 | 1.44881 |
| 35 | TF6_ma_ribbon_long | EUR_USD | long | C02 | volume_ratio + ATR_ratio + RSI14 + session_bucket + BB_compress | volume_ratio>0.8421 AND ATR_ratio>0.1056 AND RSI14>=80.3951 AND session_bucket==london AND BB_compress<=0.283972 | 11 | 2 | 0.846154 | 3 | 0 | 0.496271 |
| 36 | TF3_supertrend_long | USD_CHF | long | C01 | ATR_ratio + hour_utc + BB_compress | ATR_ratio>0.05495 AND hour_utc<=16.5 AND hour_utc>=5 AND hour_utc<=8 AND ATR_ratio<=0.0568528 AND BB_compress<=0.0522465 | 11 | 2 | 0.846154 | 1 | 0 | 1.53846 |
| 37 | TF6_ma_ribbon_long | CHF_JPY | long | C02 | RSI14 + ATR_ratio + volume_ratio + price_pos | RSI14>69.79 AND ATR_ratio>0.08828 AND volume_ratio>=1.84027 AND price_pos>=0.893577 | 11 | 2 | 0.846154 | 1 | 0 | 0.866681 |
| 38 | TF6_ma_ribbon_long | CHF_JPY | long | C02 | RSI14 + ATR_ratio + price_pos | RSI14>69.79 AND ATR_ratio>0.08828 AND price_pos>=0.970936 AND RSI14>=80.9626 | 11 | 2 | 0.846154 | 1 | 0 | 0.846809 |
| 39 | TF3_supertrend_short | USD_CAD | short | C02 | ATR_ratio + ADX14 + BB_compress | ATR_ratio>0.07832 AND ADX14>38.7 AND BB_compress<=0.103283 AND ATR_ratio>=0.087109 | 11 | 2 | 0.846154 | 0 | 0 | 1.26984 |
| 40 | TF3_supertrend_long | GBP_CAD | long | C01 | ATR_ratio + BB_compress + volume_ratio | ATR_ratio>0.06152 AND ATR_ratio>0.08849 AND BB_compress>=0.0822818 AND BB_compress<=0.114646 AND ATR_ratio<=0.0933625 AND volume_ratio>=0.820518 | 11 | 2 | 0.846154 | 2 | 1 | 1.39758 |