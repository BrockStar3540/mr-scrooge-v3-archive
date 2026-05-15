# Raw class-islands summary

**Generated:** 2026-05-15T17:16:10.518588+00:00

## Counts per (target, window)

| target | window | islands | parent cells qualifying | min leaf | min cell n |
|---|---|---:|---|---:|---:|
| win | 6yr | 137 | n>=200 | 20 | 200 |
| loss | 6yr | 159 | n>=200 | 20 | 200 |
| win | 6mo | 387 | n>=50 | 10 | 50 |
| loss | 6mo | 113 | n>=50 | 10 | 50 |

### 6yr winner-vs-loser cell overlap

- cells with BOTH a winner island and a loser island: **95**
- cells with only a winner island: 42
- cells with only a loser island: 64

### 6mo winner-vs-loser cell overlap

- cells with BOTH a winner island and a loser island: **90**
- cells with only a winner island: 297
- cells with only a loser island: 23

### win islands: 6yr vs 6mo cell persistence

- cells with an island in BOTH windows: **79** (durable)
- only 6yr (no longer present in last 6mo): 58
- only 6mo (new in last 6mo): 308

### loss islands: 6yr vs 6mo cell persistence

- cells with an island in BOTH windows: **98** (durable)
- only 6yr (no longer present in last 6mo): 61
- only 6mo (new in last 6mo): 15

## Top 15 winner islands per window (by target_rate then n)

### 6yr

| strategy | pair | dir | regime | parent | leaf n | W | L | wr | lift |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| TF6_ma_ribbon_short | GBP_USD | short | C02 | 1213 | 23 | 19 | 4 | 0.826 | 3.05 |
| TF6_ma_ribbon_long | EUR_JPY | long | C02 | 972 | 20 | 16 | 4 | 0.800 | 2.79 |
| TF6_ma_ribbon_long | GBP_CAD | long | C02 | 746 | 20 | 16 | 4 | 0.800 | 2.94 |
| TF3_supertrend_short | GBP_NZD | short | C02 | 2901 | 20 | 16 | 4 | 0.800 | 4.46 |
| TF6_ma_ribbon_short | USD_CHF | short | C02 | 855 | 26 | 20 | 6 | 0.769 | 2.37 |
| TF3_supertrend_short | EUR_CAD | short | C01 | 3144 | 21 | 16 | 5 | 0.762 | 4.18 |
| TF3_supertrend_short | USD_CAD | short | C01 | 3585 | 21 | 16 | 5 | 0.762 | 4.31 |
| TF6_ma_ribbon_long | USD_JPY | long | C02 | 1018 | 21 | 16 | 5 | 0.762 | 2.45 |
| TF3_supertrend_long | EUR_JPY | long | C01 | 3242 | 28 | 21 | 7 | 0.750 | 3.48 |
| TF3_supertrend_long | EUR_AUD | long | C02 | 3029 | 24 | 18 | 6 | 0.750 | 3.66 |
| TF6_ma_ribbon_short | NZD_USD | short | C02 | 1862 | 24 | 18 | 6 | 0.750 | 3.05 |
| TF6_ma_ribbon_long | USD_CHF | long | C02 | 766 | 24 | 18 | 6 | 0.750 | 3.02 |
| TF6_ma_ribbon_short | USD_JPY | short | C02 | 1279 | 24 | 18 | 6 | 0.750 | 3.03 |
| TF3_supertrend_short | AUD_USD | short | C01 | 3466 | 20 | 15 | 5 | 0.750 | 4.13 |
| TF6_ma_ribbon_short | EUR_CHF | short | C02 | 300 | 20 | 15 | 5 | 0.750 | 2.85 |

### 6mo

| strategy | pair | dir | regime | parent | leaf n | W | L | wr | lift |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| MO2_momentum_divergence_short | USD_JPY | short | C02 | 2833 | 12 | 12 | 0 | 1.000 | 11.15 |
| BR2_vcb_short | USD_CAD | short | C02 | 1727 | 10 | 10 | 0 | 1.000 | 11.67 |
| TF3_supertrend_short | EUR_AUD | short | C01 | 239 | 12 | 11 | 1 | 0.917 | 4.38 |
| TF3_supertrend_long | USD_CAD | long | C02 | 249 | 11 | 10 | 1 | 0.909 | 4.53 |
| MR4_zscore_extreme_short | EUR_AUD | short | C01 | 537 | 10 | 9 | 1 | 0.900 | 9.67 |
| MR2_bb_reversion_short | EUR_JPY | short | C02 | 513 | 10 | 9 | 1 | 0.900 | 7.70 |
| TF3_supertrend_long | NZD_JPY | long | C02 | 227 | 10 | 9 | 1 | 0.900 | 3.46 |
| TF6_ma_ribbon_short | USD_MXN | short | C02 | 89 | 10 | 9 | 1 | 0.900 | 3.34 |
| TF3_supertrend_long | AUD_NZD | long | C01 | 222 | 16 | 14 | 2 | 0.875 | 4.74 |
| TF3_supertrend_short | AUD_CAD | short | C02 | 227 | 15 | 13 | 2 | 0.867 | 4.68 |
| MR2_bb_reversion_short | EUR_USD | short | C01 | 408 | 13 | 11 | 2 | 0.846 | 5.85 |
| TF3_supertrend_long | USD_CHF | long | C02 | 257 | 13 | 11 | 2 | 0.846 | 3.88 |
| TF6_ma_ribbon_short | USD_CHF | short | C02 | 73 | 12 | 10 | 2 | 0.833 | 2.54 |
| TF3_supertrend_long | AUD_JPY | long | C02 | 225 | 17 | 14 | 3 | 0.824 | 2.29 |
| TF6_ma_ribbon_long | AUD_JPY | long | C02 | 92 | 11 | 9 | 2 | 0.818 | 2.51 |

## Top 15 loser islands per window (by target_rate then n)

### 6yr

| strategy | pair | dir | regime | parent | leaf n | W | L | loss_rate | lift |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| TF3_supertrend_short | GBP_CHF | short | C01 | 3190 | 231 | 0 | 231 | 1.000 | 1.18 |
| TF3_supertrend_long | EUR_CHF | long | C02 | 3326 | 191 | 0 | 191 | 1.000 | 1.21 |
| TF3_supertrend_short | AUD_CAD | short | C01 | 3174 | 188 | 0 | 188 | 1.000 | 1.19 |
| TF3_supertrend_long | CHF_JPY | long | C01 | 3318 | 175 | 0 | 175 | 1.000 | 1.23 |
| TF3_supertrend_long | CHF_JPY | long | C02 | 2945 | 171 | 0 | 171 | 1.000 | 1.27 |
| TF4_sar_short | USD_MXN | short | C02 | 8818 | 141 | 0 | 141 | 1.000 | 1.18 |
| TF3_supertrend_short | GBP_CHF | short | C02 | 2974 | 137 | 0 | 137 | 1.000 | 1.22 |
| TF6_ma_ribbon_short | AUD_JPY | short | C02 | 2349 | 134 | 0 | 134 | 1.000 | 1.29 |
| TF3_supertrend_long | USD_CHF | long | C01 | 3459 | 134 | 0 | 134 | 1.000 | 1.21 |
| TF3_supertrend_short | AUD_USD | short | C02 | 3355 | 129 | 0 | 129 | 1.000 | 1.25 |
| TF3_supertrend_short | AUD_NZD | short | C02 | 2909 | 128 | 0 | 128 | 1.000 | 1.18 |
| TF3_supertrend_long | EUR_GBP | long | C01 | 3188 | 127 | 0 | 127 | 1.000 | 1.19 |
| TF3_supertrend_long | GBP_CHF | long | C02 | 2981 | 122 | 0 | 122 | 1.000 | 1.24 |
| TF3_supertrend_short | EUR_GBP | short | C01 | 3208 | 121 | 0 | 121 | 1.000 | 1.21 |
| TF3_supertrend_long | GBP_AUD | long | C02 | 2806 | 121 | 0 | 121 | 1.000 | 1.26 |

### 6mo

| strategy | pair | dir | regime | parent | leaf n | W | L | loss_rate | lift |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| TF4_sar_long | GBP_JPY | long | C02 | 649 | 103 | 0 | 103 | 1.000 | 1.18 |
| TF4_sar_long | GBP_USD | long | C02 | 626 | 78 | 0 | 78 | 1.000 | 1.18 |
| TF4_sar_short | EUR_USD | short | C01 | 440 | 76 | 0 | 76 | 1.000 | 1.18 |
| MR2_bb_reversion_long | AUD_JPY | long | C01 | 389 | 74 | 0 | 74 | 1.000 | 1.18 |
| TF3_supertrend_long | EUR_GBP | long | C01 | 215 | 69 | 0 | 69 | 1.000 | 1.18 |
| MR2_bb_reversion_short | EUR_USD | short | C02 | 471 | 66 | 0 | 66 | 1.000 | 1.19 |
| TF3_supertrend_short | GBP_JPY | short | C02 | 224 | 65 | 0 | 65 | 1.000 | 1.18 |
| TF3_supertrend_long | USD_MXN | long | C02 | 291 | 65 | 0 | 65 | 1.000 | 1.18 |
| TF3_supertrend_long | GBP_CAD | long | C02 | 214 | 64 | 0 | 64 | 1.000 | 1.26 |
| TF3_supertrend_short | USD_CAD | short | C01 | 238 | 64 | 0 | 64 | 1.000 | 1.23 |
| TF3_supertrend_short | EUR_CHF | short | C02 | 239 | 63 | 0 | 63 | 1.000 | 1.23 |
| TF3_supertrend_short | AUD_CAD | short | C02 | 227 | 61 | 0 | 61 | 1.000 | 1.23 |
| MR2_bb_reversion_long | EUR_JPY | long | C01 | 387 | 60 | 0 | 60 | 1.000 | 1.19 |
| TF3_supertrend_long | AUD_CAD | long | C01 | 250 | 59 | 0 | 59 | 1.000 | 1.19 |
| TF3_supertrend_short | CHF_JPY | short | C01 | 256 | 59 | 0 | 59 | 1.000 | 1.19 |
