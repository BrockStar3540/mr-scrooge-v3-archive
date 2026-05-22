# Scalper Bank Summary — 10-pip SL / 12-pip TP1 / ratchet

Built 2026-05-21 from `scalper_corpus_10sl_12tp_ratchet.parquet` (416,113 rows, 355 weeks).

Objective: `clean_fires_per_week × expected_pips_per_trade` with depth-1 / depth-2 factor splits.
Bars: n_clean>=13, pop_kept>=5%, expected_pips_per_trade>0.

**Total cells: 77**

## Frequency class distribution

```
            cells  median_fpw  median_clean_wr  median_ev_pips_per_trade  median_ev_pips_per_week
freq_class                                                                                       
REGULAR         2    4.233803         0.391295                  0.647206                 0.854930
MODERATE       10    1.392958         0.388385                  0.941539                 0.330986
RARE           28    0.581690         0.379808                  0.665633                 0.078873
GHOST          37    0.118310         0.461538                  2.882353                 0.135211
```

## Top 25 cells (by expected_pips_per_week)

| pair | regime | dir | family | rule | depth | n_clean | WR | E[pips]/trade | fires/wk | E[pips]/wk | amb_rate | wilson_lb |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| USD_JPY | C01 | long | dbb_trend | `ATR_ratio>=0.0393952 AND volume_ratio<=1.70255` | 2 | 486 | 0.395 | +0.70 | 4.75 | +0.95 | 0.71 | 0.367 |
| EUR_USD | C01 | short | dbb_trend | `price_pos<=0.060241 AND volume_ratio>=0.811624` | 2 | 449 | 0.388 | +0.60 | 3.71 | +0.75 | 0.66 | 0.359 |
| USD_MXN | C01 | short | dbb_trend | `ATR_ratio>=0.0590704 AND RSI14>=41.7337` | 2 | 199 | 0.362 | +1.09 | 0.78 | +0.61 | 0.28 | 0.320 |
| GBP_USD | C02 | long | dbb_trend | `BB_compress>=0.0481313 AND RSI14<=56.2417` | 2 | 138 | 0.464 | +1.54 | 1.76 | +0.60 | 0.78 | 0.410 |
| USD_JPY | C02 | long | dbb_trend | `BB_compress>=0.109443 AND RSI14>=60.7773` | 2 | 118 | 0.449 | +1.65 | 1.59 | +0.55 | 0.79 | 0.392 |
| EUR_JPY | C02 | long | dbb_trend | `BB_compress>=0.0530532 AND ADX14<=22.2375` | 2 | 76 | 0.474 | +2.33 | 1.12 | +0.50 | 0.81 | 0.402 |
| GBP_USD | C01 | long | dbb_trend | `ADX14>=18.5838 AND RSI14<=58.6516` | 2 | 44 | 0.545 | +3.95 | 0.51 | +0.49 | 0.76 | 0.449 |
| AUD_JPY | C02 | long | dbb_trend | `ATR_ratio<=0.0587555 AND BB_compress>=0.0590479` | 2 | 122 | 0.402 | +1.20 | 1.62 | +0.41 | 0.79 | 0.346 |
| NZD_USD | R04 | short | dbb_trend | `ADX14>=13.5188 AND volume_ratio>=0.796898` | 2 | 23 | 0.652 | +5.43 | 0.10 | +0.35 | 0.38 | 0.519 |
| EUR_USD | C02 | long | dbb_trend | `RSI14<=60.6003 AND price_pos>=0.937771` | 2 | 174 | 0.391 | +0.68 | 1.38 | +0.33 | 0.65 | 0.345 |
| CAD_JPY | C02 | long | dbb_trend | `BB_compress>=0.13006 AND price_pos>=0.839937` | 2 | 96 | 0.385 | +1.22 | 1.40 | +0.33 | 0.81 | 0.324 |
| USD_MXN | C02 | long | direct | `ATR_ratio>=0.131832 AND RSI14>=64.708` | 2 | 39 | 0.538 | +2.90 | 0.17 | +0.32 | 0.35 | 0.437 |
| EUR_GBP | C02 | long | direct | `price_pos<=0.790923` | 1 | 19 | 0.579 | +5.79 | 0.17 | +0.31 | 0.68 | 0.433 |
| CAD_JPY | C01 | long | dbb_trend | `ADX14<=15.0465 AND RSI14<=58.9877` | 2 | 54 | 0.463 | +1.87 | 0.52 | +0.28 | 0.71 | 0.378 |
| NZD_JPY | R04 | short | dbb_trend | `ADX14>=14.9987 AND volume_ratio>=0.896829` | 2 | 13 | 0.769 | +7.69 | 0.08 | +0.28 | 0.54 | 0.595 |
| AUD_USD | R04 | short | dbb_trend | `ADX14>=16.0087 AND volume_ratio<=1.57725` | 2 | 16 | 0.688 | +5.81 | 0.07 | +0.26 | 0.36 | 0.528 |
| AUD_JPY | R04 | short | dbb_trend | `price_pos>=0.0146667 AND volume_ratio>=0.81887` | 2 | 13 | 0.692 | +6.85 | 0.11 | +0.25 | 0.67 | 0.515 |
| EUR_GBP | C01 | short | dbb_trend | `BB_compress<=0.0278105 AND price_pos<=0.0353576` | 2 | 104 | 0.413 | +0.86 | 0.57 | +0.25 | 0.49 | 0.353 |
| AUD_USD | C01 | short | dbb_trend | `ATR_ratio>=0.0603301 AND ADX14<=13.7209` | 2 | 52 | 0.423 | +1.62 | 0.56 | +0.24 | 0.74 | 0.339 |
| EUR_USD | R04 | short | dbb_trend | `volume_ratio<=1.45926` | 1 | 14 | 0.643 | +5.93 | 0.12 | +0.23 | 0.67 | 0.472 |
| USD_MXN | Z01 | long | dbb_trend | `volume_ratio>=1.2026` | 1 | 21 | 0.476 | +3.86 | 0.08 | +0.23 | 0.22 | 0.344 |
| GBP_USD | R04 | short | dbb_trend | `ADX14<=16.4824` | 1 | 13 | 0.692 | +6.08 | 0.09 | +0.22 | 0.58 | 0.515 |
| USD_JPY | R04 | short | dbb_trend | `ADX14<=17.7426` | 1 | 14 | 0.643 | +5.36 | 0.11 | +0.21 | 0.65 | 0.472 |
| NZD_USD | C02 | long | direct | `ATR_ratio<=0.0728414 AND ADX14<=27.1838` | 2 | 13 | 0.615 | +5.38 | 0.12 | +0.20 | 0.69 | 0.439 |
| GBP_USD | C02 | short | dbb_trend | `ATR_ratio>=0.100194 AND RSI14<=32.8325` | 2 | 63 | 0.397 | +1.05 | 0.84 | +0.19 | 0.79 | 0.322 |

## Caveats

- Ambiguous bin (~69%) was excluded from the per-cell WR; cells with low ambiguity rate are more trustworthy.
- Ratchet `_likely` outcomes assume favorable MFE happened before adverse MAE; OHLC refinement is the next pass.
- Frequency class uses `fires_per_week` (total kept, including ambiguous) not clean-only. The bot will actually see all the rows; the ambiguous ones won't reliably win or lose.
