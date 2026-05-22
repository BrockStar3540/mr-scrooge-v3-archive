# Scalper Bank Summary (built 2026-05-21)

Corpus: scalper_corpus_6x12.parquet, 416,113 rows over 355 weeks, 1192 signatures scanned.

Bars: n_clean>=13, pop_kept>=5%, clean_WR>=0.33 (breakeven at 2:1), positive expectancy.

**Total cells: 53**

## Frequency class distribution

```
            cells  median_fpw  median_clean_wr  median_exp_R_per_wk
freq_class                                                         
REGULAR         3    4.754930         0.393868             0.216901
MODERATE       15    1.622535         0.379845             0.050704
RARE           29    0.611268         0.357143             0.019718
GHOST           6    0.166197         0.492674             0.022535
```

## Top 25 cells (sorted by expected_R_per_week)

| pair | regime | dir | family | rule | depth | n_clean | WR_clean | fires/wk | exp_R/trade | exp_R/wk | prob_WR | wilson_lb |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| USD_JPY | C01 | long | dbb_trend | `ATR_ratio>=0.0393952 AND volume_ratio<=1.70255` | 2 | 486 | 0.395 | 4.75 | 0.185 | 0.25 | 0.470 | 0.367 |
| USD_JPY | C02 | long | dbb_trend | `RSI14>=60.7773 AND volume_ratio>=0.786074` | 2 | 424 | 0.394 | 5.25 | 0.182 | 0.22 | 0.476 | 0.364 |
| EUR_USD | C01 | short | dbb_trend | `price_pos<=0.060241 AND volume_ratio>=0.989201` | 2 | 355 | 0.403 | 2.96 | 0.208 | 0.21 | 0.467 | 0.370 |
| GBP_USD | C02 | long | dbb_trend | `BB_compress>=0.0481313 AND RSI14<=56.2417` | 2 | 138 | 0.464 | 1.76 | 0.391 | 0.15 | 0.492 | 0.410 |
| USD_MXN | C01 | short | dbb_trend | `ATR_ratio>=0.0590704 AND RSI14>=41.7337` | 2 | 174 | 0.414 | 0.78 | 0.241 | 0.12 | 0.437 | 0.367 |
| EUR_JPY | C02 | long | dbb_trend | `BB_compress>=0.0530532 AND ADX14<=26.8435` | 2 | 202 | 0.391 | 3.02 | 0.173 | 0.10 | 0.479 | 0.348 |
| EUR_USD | C02 | long | dbb_trend | `price_pos>=0.937771 AND volume_ratio<=1.38303` | 2 | 332 | 0.364 | 2.96 | 0.093 | 0.09 | 0.457 | 0.331 |
| GBP_USD | C01 | long | dbb_trend | `ADX14>=18.5838 AND RSI14<=58.6516` | 2 | 44 | 0.545 | 0.51 | 0.636 | 0.08 | 0.511 | 0.449 |
| CAD_JPY | C01 | long | dbb_trend | `BB_compress>=0.0429498 AND ADX14<=16.2829` | 2 | 173 | 0.387 | 1.95 | 0.162 | 0.08 | 0.472 | 0.341 |
| EUR_USD | C01 | long | dbb_trend | `RSI14<=62.5347 AND price_pos>=0.960875` | 2 | 202 | 0.376 | 1.78 | 0.129 | 0.07 | 0.460 | 0.334 |
| AUD_JPY | C02 | long | dbb_trend | `ATR_ratio<=0.0587555 AND BB_compress>=0.0590479` | 2 | 122 | 0.402 | 1.62 | 0.205 | 0.07 | 0.479 | 0.346 |
| EUR_GBP | C01 | short | dbb_trend | `BB_compress<=0.0278105 AND price_pos<=0.0353576` | 2 | 104 | 0.413 | 0.57 | 0.240 | 0.07 | 0.455 | 0.353 |
| USD_MXN | C02 | long | direct | `ATR_ratio>=0.131832 AND RSI14>=64.708` | 2 | 39 | 0.538 | 0.17 | 0.615 | 0.07 | 0.525 | 0.437 |
| EUR_USD | C02 | short | dbb_trend | `BB_compress<=0.0790746 AND price_pos>=0.257832` | 2 | 156 | 0.378 | 1.25 | 0.135 | 0.06 | 0.457 | 0.330 |
| CAD_JPY | C01 | short | dbb_trend | `ADX14>=18.486 AND price_pos<=0.0675676` | 2 | 98 | 0.398 | 0.88 | 0.194 | 0.05 | 0.468 | 0.337 |
| AUD_USD | C02 | long | dbb_trend | `ATR_ratio<=0.0559139 AND ADX14>=31.3956` | 2 | 129 | 0.380 | 1.17 | 0.140 | 0.05 | 0.463 | 0.327 |
| CAD_JPY | C02 | long | dbb_trend | `BB_compress>=0.13006 AND price_pos>=0.839937` | 2 | 96 | 0.385 | 1.40 | 0.156 | 0.04 | 0.478 | 0.324 |
| AUD_JPY | C02 | short | dbb_trend | `ATR_ratio>=0.0806066 AND RSI14<=30.9225` | 2 | 102 | 0.382 | 1.25 | 0.147 | 0.04 | 0.473 | 0.323 |
| AUD_JPY | C01 | long | dbb_trend | `ADX14>=17.4559 AND RSI14>=61.7868` | 2 | 145 | 0.366 | 1.65 | 0.097 | 0.04 | 0.467 | 0.316 |
| AUD_USD | C01 | short | dbb_trend | `ATR_ratio>=0.0603301 AND ADX14<=13.7209` | 2 | 52 | 0.423 | 0.56 | 0.269 | 0.04 | 0.480 | 0.339 |
| GBP_USD | C02 | short | dbb_trend | `ATR_ratio>=0.100194 AND ADX14>=30.945` | 2 | 100 | 0.380 | 1.51 | 0.140 | 0.04 | 0.478 | 0.320 |
| EUR_JPY | C01 | long | dbb_trend | `ATR_ratio<=0.0600991 AND BB_compress>=0.0434719` | 2 | 134 | 0.366 | 1.81 | 0.097 | 0.04 | 0.472 | 0.314 |
| USD_CAD | C02 | short | dbb_trend | `ADX14>=28.9932 AND price_pos<=0.0269002` | 2 | 62 | 0.403 | 0.65 | 0.210 | 0.04 | 0.474 | 0.327 |
| USD_MXN | C01 | long | dbb_trend | `ATR_ratio>=0.0776931 AND ADX14>=17.5944` | 2 | 207 | 0.353 | 0.90 | 0.058 | 0.03 | 0.398 | 0.311 |
| NZD_USD | C02 | long | direct | `ATR_ratio<=0.0627232 AND price_pos>=0.7` | 2 | 21 | 0.524 | 0.17 | 0.571 | 0.03 | 0.508 | 0.388 |

## Caveat

Clean WR uses only unambiguous events (28% of total).
The `probable_wr_amb_50` column estimates true WR assuming ambiguous events split 50/50.
OHLC-based resolution of ambiguous events is the natural next step.
