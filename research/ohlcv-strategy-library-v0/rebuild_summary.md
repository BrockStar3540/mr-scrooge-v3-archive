# Full Strategy Library Rebuild — 10sl/12tp/ratchet

Generated 2026-05-22 on Mac Mini (serial CPYQTH294R, 16 GB).

## Inputs
- 26 per-pair trade_log_all_*.parquet files
- Corpus span: 2019-07-01 20:50:00+00:00 → 2026-04-21 02:05:00+00:00 (355 weeks)
- Strategy universe: **56 unique strategy_ids**
  - Box Theory matches: 0
  - Double BB matches: 2

## Execution truth
- SL = 10 pips (initial)
- TP1 = 12 pips
- Ratchet: +6→SL=-6, +8→SL=-3, +10→SL=BE

## Results
- Total cells: 26,084
- Cells with positive expectancy + n_clean≥13: 625
- Parent seeds (≥1 fire/wk + positive ev): 38
- Island candidates (0.25-1 fire/wk + positive ev): 133
- Median ambiguity rate per cell: 76.27%

## Frequency class distribution (all cells)

```
freq_class
GHOST       21227
RARE          731
MODERATE      405
REGULAR      3721
```

## Top 30 parent seeds

| strategy_id | pair | regime | dir | session | n_clean | WR | E[pips]/trade | fires/wk | E[pips]/wk |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| `RG1_range_bound_scalp_short` | EUR_USD | C01 | short | asia | 1519 | 0.388 | +0.68 | 12.38 | +2.90 |
| `MR5_williams_extreme_short` | EUR_USD | C01 | short | asia | 1392 | 0.387 | +0.52 | 11.52 | +2.04 |
| `BR2_vcb_long` | USD_JPY | C01 | long | asia | 1591 | 0.379 | +0.33 | 14.46 | +1.47 |
| `MR2_bb_reversion_long` | USD_JPY | C02 | long | london | 779 | 0.389 | +0.62 | 7.72 | +1.36 |
| `SS1_asian_range_breakout_long` | USD_JPY | C02 | long | asia | 252 | 0.444 | +1.84 | 2.86 | +1.30 |
| `CP3_vol_coil_fade_short` | EUR_USD | C01 | short | asia | 2644 | 0.359 | +0.15 | 21.89 | +1.13 |
| `TF2_pullback_EMA20_long` | USD_JPY | C01 | long | asia | 2160 | 0.375 | +0.18 | 19.21 | +1.11 |
| `CP2_squeeze_momentum_long` | USD_JPY | C02 | long | asia | 376 | 0.394 | +1.01 | 3.62 | +1.07 |
| `MR5_williams_extreme_long` | USD_JPY | C02 | long | london | 1606 | 0.365 | +0.21 | 16.92 | +0.97 |
| `CP2_squeeze_momentum_long` | USD_JPY | C01 | long | asia | 622 | 0.392 | +0.53 | 5.43 | +0.94 |
| `MR5_williams_extreme_long` | EUR_USD | C02 | long | ny | 1374 | 0.354 | +0.23 | 12.60 | +0.89 |
| `MR5_williams_extreme_long` | USD_JPY | C02 | long | ny | 1088 | 0.351 | +0.21 | 12.39 | +0.64 |
| `RG2_range_support_bounce_long` | AUD_JPY | C01 | long | asia | 1151 | 0.359 | +0.18 | 10.73 | +0.59 |
| `MR4_zscore_extreme_short` | EUR_USD | C01 | short | asia | 851 | 0.369 | +0.24 | 7.01 | +0.59 |
| `MR2_bb_reversion_short` | EUR_USD | C01 | short | asia | 607 | 0.372 | +0.33 | 4.92 | +0.56 |
| `BR3_inside_bar_long` | USD_JPY | C01 | long | asia | 747 | 0.380 | +0.26 | 6.85 | +0.55 |
| `MR2_bb_reversion_long` | USD_JPY | C02 | long | ny | 459 | 0.362 | +0.42 | 5.18 | +0.55 |
| `BR5_opening_range_breakout_long` | USD_JPY | C01 | long | london | 538 | 0.370 | +0.30 | 4.73 | +0.46 |
| `SS1_asian_range_breakout_long` | EUR_JPY | C01 | long | asia | 155 | 0.413 | +0.99 | 1.85 | +0.43 |
| `MR4_zscore_extreme_long` | USD_JPY | C02 | long | london | 337 | 0.371 | +0.44 | 3.37 | +0.41 |
| `TF3_supertrend_long` | USD_JPY | C01 | long | london | 315 | 0.384 | +0.43 | 2.88 | +0.38 |
| `TF6_ma_ribbon_long` | USD_JPY | C02 | long | london | 92 | 0.435 | +1.32 | 1.53 | +0.34 |
| `SS1_asian_range_breakout_long` | GBP_USD | C01 | long | asia | 148 | 0.392 | +0.79 | 1.72 | +0.33 |
| `SS1_asian_range_breakout_long` | USD_JPY | C01 | long | asia | 127 | 0.386 | +0.87 | 1.30 | +0.31 |
| `MR5_williams_extreme_long` | EUR_USD | C01 | long | ny | 1341 | 0.346 | +0.07 | 11.97 | +0.26 |
| `MR4_zscore_extreme_long` | USD_JPY | C01 | long | london | 590 | 0.363 | +0.11 | 5.16 | +0.18 |
| `TF2_pullback_EMA20_long` | USD_JPY | C01 | long | london | 2092 | 0.364 | +0.03 | 18.83 | +0.18 |
| `BR3_inside_bar_long` | USD_JPY | C01 | long | london | 656 | 0.367 | +0.09 | 6.05 | +0.17 |
| `SS3_ny_lunch_drift_long` | USD_JPY | C01 | long | ny | 250 | 0.364 | +0.23 | 2.70 | +0.16 |
| `BR5_opening_range_breakout_short` | EUR_USD | C02 | short | london | 656 | 0.363 | +0.09 | 5.87 | +0.16 |

## Top 15 Box Theory cells

(no Box Theory strategy_ids found in corpus -- need to check what naming patterns Box Theory uses)

## Top 15 Double BB cells

| strategy_id | pair | regime | dir | session | n_clean | WR | E[pips]/trade | fires/wk |
|---|---|---|---|---|---:|---:|---:|---:|
| `MR2_bb_reversion_long` | USD_JPY | C02 | long | london | 779 | 0.389 | +0.62 | 7.72 |
| `MR2_bb_reversion_short` | EUR_USD | C01 | short | asia | 607 | 0.372 | +0.33 | 4.92 |
| `MR2_bb_reversion_long` | USD_JPY | C02 | long | ny | 459 | 0.362 | +0.42 | 5.18 |
| `MR2_bb_reversion_short` | AUD_USD | R04 | short | asia | 18 | 0.611 | +5.50 | 0.08 |
| `MR2_bb_reversion_short` | EUR_USD | R04 | short | ny | 10 | 0.800 | +9.60 | 0.09 |
| `MR2_bb_reversion_short` | EUR_USD | R04 | short | london | 16 | 0.625 | +5.50 | 0.07 |
| `MR2_bb_reversion_short` | NZD_USD | R04 | short | asia | 22 | 0.591 | +4.00 | 0.09 |
| `MR2_bb_reversion_short` | AUD_JPY | R04 | short | asia | 14 | 0.643 | +6.14 | 0.10 |
| `MR2_bb_reversion_short` | EUR_CHF | T07 | short | asia | 10 | 0.700 | +7.80 | 0.06 |
| `MR2_bb_reversion_short` | GBP_CHF | R04 | short | asia | 13 | 0.692 | +6.00 | 0.08 |
| `MR2_bb_reversion_short` | CHF_JPY | R04 | short | ny | 19 | 0.474 | +4.05 | 0.11 |
| `MR2_bb_reversion_short` | GBP_USD | Z01 | short | ny | 10 | 0.700 | +7.40 | 0.06 |
| `MR2_bb_reversion_long` | EUR_USD | R04 | long | ny | 17 | 0.588 | +4.18 | 0.10 |
| `MR2_bb_reversion_short` | EUR_CAD | R04 | short | london | 10 | 0.700 | +7.10 | 0.12 |
| `MR2_bb_reversion_short` | AUD_CHF | R04 | short | asia | 12 | 0.667 | +5.83 | 0.08 |
