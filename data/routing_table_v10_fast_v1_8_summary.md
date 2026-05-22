# v10_fast_v1.8 Routing Table Summary

Built 2026-05-22T02:55:14.939489+00:00

Source: scalper_bank_cells_10sl_12tp_ratchet.csv (REGULAR + MODERATE only)

**Total cells: 9** (top-session-only, no synthetic fan-out)

## Cells

| # | pair | regime | dir | family | session | tier | rule | n | WR | E[pips]/trade | fires/wk |
|---:|---|---|---|---|---|---|---|---:|---:|---:|---:|
| 1 | USD_JPY | C01 | long | dbb_trend | asia | Elite | `ATR_ratio>=0.0393952 AND volume_ratio<=1.70255` | 486 | 0.395 | +0.70 | 4.75 |
| 2 | EUR_USD | C01 | short | dbb_trend | ? | ? | `price_pos<=0.060241 AND volume_ratio>=0.811624` | 449 | 0.388 | +0.60 | 3.71 |
| 3 | GBP_USD | C02 | long | dbb_trend | asia | Pro | `BB_compress>=0.0481313 AND RSI14<=56.2417` | 138 | 0.464 | +1.54 | 1.76 |
| 4 | USD_JPY | C02 | long | dbb_trend | asia | Pro | `BB_compress>=0.109443 AND RSI14>=60.7773` | 118 | 0.449 | +1.65 | 1.59 |
| 5 | EUR_JPY | C02 | long | dbb_trend | asia | Pro | `BB_compress>=0.0530532 AND ADX14<=22.2375` | 76 | 0.474 | +2.33 | 1.12 |
| 6 | AUD_JPY | C02 | long | dbb_trend | london_open | Pro | `ATR_ratio<=0.0587555 AND BB_compress>=0.0590479` | 122 | 0.402 | +1.20 | 1.62 |
| 7 | EUR_USD | C02 | long | dbb_trend | asia | Pro | `RSI14<=60.6003 AND price_pos>=0.937771` | 174 | 0.391 | +0.68 | 1.38 |
| 8 | CAD_JPY | C02 | long | dbb_trend | asia | Pro | `BB_compress>=0.13006 AND price_pos>=0.839937` | 96 | 0.385 | +1.22 | 1.40 |
| 9 | EUR_USD | C01 | long | dbb_trend | asia | Pro | `RSI14<=62.5347 AND volume_ratio>=1.74966` | 114 | 0.386 | +0.56 | 1.01 |
| 10 | AUD_USD | C02 | long | dbb_trend | london_open | Pro | `ATR_ratio<=0.0559139 AND ADX14>=31.3956` | 129 | 0.380 | +0.50 | 1.17 |
| 11 | EUR_USD | C02 | short | dbb_trend | ? | ? | `BB_compress<=0.0790746 AND price_pos>=0.257832` | 156 | 0.378 | +0.35 | 1.25 |
| 12 | AUD_USD | C02 | short | dbb_trend | ? | ? | `ATR_ratio>=0.0935746 AND price_pos<=0.171981` | 181 | 0.348 | +0.02 | 1.59 |

## Execution truth

- SL = 10 pips (initial)
- TP1 = 12 pips
- Ratchet: +6→SL=-6, +8→SL=-3, +10→SL=BE
