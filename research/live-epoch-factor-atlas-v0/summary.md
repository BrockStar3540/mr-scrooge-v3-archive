# Live-Epoch Conditional Factor Atlas v0

Generated: 2026-05-13T00:09:23.213910+00:00

## Design

**Old regime labels are METADATA, not clustering drivers.** The atlas
discovers what winners synchronize around without pre-imposing regime structure.

Primary grain: `strategy_branch × pair_family × session × direction × outcome_type`

Old regime labels (V1/V2 CAUTION/NORMAL/RESTRICTED) preserved in
`old_regime_annotation.csv` as annotation; not used to define cells.

## Scope (live epoch only — by design)

- Source: per_trade_factors_filled.csv.gz — 90,024 filled trades
- Time: 2026-03-15 → 2026-04-13 (30 days, all post-2024 — the current live epoch)
- Strategies: ['dbb_trend', 'direct']
- Pair families: ['antipodean_cross', 'eur_cross', 'gbp_cross', 'usd_base']
- Sessions: ['asia', 'london', 'ny_pm', 'overlap']
- Factor columns: 46

## Outcome taxonomy distribution

| outcome_type    |        n |   pct |
|:----------------|---------:|------:|
| gave_back_green | 43068.00 | 47.84 |
| timed_exit      | 13623.00 | 15.13 |
| unclear         | 11024.00 | 12.25 |
| full_tp         |  8160.00 |  9.06 |
| partial_loss    |  7759.00 |  8.62 |
| clean_stop      |  6390.00 |  7.10 |

## Files (this is the discovery substrate; act on it, don't summarize it)

| File | Purpose |
|---|---|
| `outcome_composition_per_cell.csv` | What share of trades in each geom cell ended in each outcome |
| `factor_profile_per_cell_outcome.csv/parquet` | Per-factor median/IQR per cell per outcome |
| `winner_vs_loser_contrast.csv/parquet` | Factor signal: full_tp+quick_tp+ratchet_save vs clean_stop+partial_loss+gave_back |
| `management_contrast_fulltp_vs_giveback.csv` | SAME entry quality, different management — isolates management failure factors |
| `inversion_report.csv` | Per (strategy, factor): does sign vary across cells? |
| `headline_inversions.csv` | Just the INVERTED factors |
| `old_regime_annotation.csv` | METADATA only — old V1/V2 regime labels by cell |

## Inversion headline (winner vs loser contrast)

Across primary geometric cells (strategy × pair_family × session × direction):

| strategy   |   INVERTED |   loser_positive |   neutral_only |   winner_positive |
|:-----------|-----------:|-----------------:|---------------:|------------------:|
| dbb_trend  |          5 |               16 |             16 |                 9 |
| direct     |         29 |                2 |             15 |                 0 |

### Most-inverted factors

| strategy   | factor                |   n_cells_total |   n_cells_non_neutral |   n_winner_positive |   n_loser_positive | consensus   |   stability_score |
|:-----------|:----------------------|----------------:|----------------------:|--------------------:|-------------------:|:------------|------------------:|
| dbb_trend  | atr                   |               7 |                     2 |                   1 |                  1 | INVERTED    |             0.500 |
| dbb_trend  | otr_ratio             |               7 |                     2 |                   1 |                  1 | INVERTED    |             0.500 |
| direct     | hour_utc              |              32 |                    18 |                   9 |                  9 | INVERTED    |             0.500 |
| direct     | bb_band_width_b_bps   |              32 |                    16 |                   8 |                  8 | INVERTED    |             0.500 |
| direct     | atr                   |              32 |                    25 |                  13 |                 12 | INVERTED    |             0.520 |
| direct     | total_overhead        |              32 |                    19 |                  10 |                  9 | INVERTED    |             0.526 |
| direct     | v3_pairs_total        |              32 |                    15 |                   8 |                  7 | INVERTED    |             0.533 |
| direct     | ema20_dist_pct        |              32 |                    22 |                  10 |                 12 | INVERTED    |             0.545 |
| direct     | rsi                   |              32 |                    27 |                  12 |                 15 | INVERTED    |             0.556 |
| direct     | minute_of_day         |              32 |                    18 |                  10 |                  8 | INVERTED    |             0.556 |
| direct     | spread_pips           |              32 |                    23 |                  10 |                 13 | INVERTED    |             0.565 |
| direct     | regime_id             |              32 |                    23 |                  10 |                 13 | INVERTED    |             0.565 |
| direct     | sma20_dist_signed_bps |              32 |                    19 |                  11 |                  8 | INVERTED    |             0.579 |
| direct     | range_half            |              32 |                    24 |                  10 |                 14 | INVERTED    |             0.583 |
| direct     | regime_confidence     |              32 |                    20 |                   8 |                 12 | INVERTED    |             0.600 |
| direct     | volume_ratio          |              32 |                    20 |                  12 |                  8 | INVERTED    |             0.600 |
| direct     | regime_score          |              32 |                    21 |                  13 |                  8 | INVERTED    |             0.619 |
| direct     | bb_position           |              32 |                    16 |                  10 |                  6 | INVERTED    |             0.625 |
| direct     | z_score               |              32 |                    16 |                  10 |                  6 | INVERTED    |             0.625 |
| direct     | ema50_dist_pct        |              32 |                    22 |                  14 |                  8 | INVERTED    |             0.636 |

### Universal winner-positive (across all non-neutral cells)

| strategy   | factor                |   n_cells_total |   n_cells_non_neutral |   n_winner_positive |   n_loser_positive | consensus       |   stability_score |
|:-----------|:----------------------|----------------:|----------------------:|--------------------:|-------------------:|:----------------|------------------:|
| dbb_trend  | adr_consumed          |               7 |                     4 |                   4 |                  0 | winner_positive |             1.000 |
| dbb_trend  | bb_state_id           |               7 |                     2 |                   2 |                  0 | winner_positive |             1.000 |
| dbb_trend  | volume_ratio          |               7 |                     2 |                   2 |                  0 | winner_positive |             1.000 |
| dbb_trend  | score                 |               7 |                     1 |                   1 |                  0 | winner_positive |             1.000 |
| dbb_trend  | regime_score          |               7 |                     1 |                   1 |                  0 | winner_positive |             1.000 |
| dbb_trend  | sma20_dist_signed_bps |               7 |                     1 |                   1 |                  0 | winner_positive |             1.000 |
| dbb_trend  | tier_a_flag           |               7 |                     1 |                   1 |                  0 | winner_positive |             1.000 |
| dbb_trend  | tier_b_flag           |               7 |                     1 |                   1 |                  0 | winner_positive |             1.000 |
| dbb_trend  | v3_pairs_total        |               7 |                     1 |                   1 |                  0 | winner_positive |             1.000 |

### Universal loser-positive

| strategy   | factor              |   n_cells_total |   n_cells_non_neutral |   n_winner_positive |   n_loser_positive | consensus      |   stability_score |
|:-----------|:--------------------|----------------:|----------------------:|--------------------:|-------------------:|:---------------|------------------:|
| direct     | rr_ratio            |              32 |                    28 |                   0 |                 28 | loser_positive |             1.000 |
| direct     | bb_state_id         |              32 |                     7 |                   0 |                  7 | loser_positive |             1.000 |
| dbb_trend  | rr_ratio            |               7 |                     4 |                   0 |                  4 | loser_positive |             1.000 |
| dbb_trend  | minute_of_day       |               7 |                     3 |                   0 |                  3 | loser_positive |             1.000 |
| dbb_trend  | rsi                 |               7 |                     3 |                   0 |                  3 | loser_positive |             1.000 |
| dbb_trend  | hour_utc            |               7 |                     3 |                   0 |                  3 | loser_positive |             1.000 |
| dbb_trend  | ema50_dist_pct      |               7 |                     3 |                   0 |                  3 | loser_positive |             1.000 |
| dbb_trend  | avg_volume          |               7 |                     2 |                   0 |                  2 | loser_positive |             1.000 |
| dbb_trend  | spread_pips         |               7 |                     2 |                   0 |                  2 | loser_positive |             1.000 |
| dbb_trend  | ema20_dist_pct      |               7 |                     2 |                   0 |                  2 | loser_positive |             1.000 |
| dbb_trend  | range_half          |               7 |                     2 |                   0 |                  2 | loser_positive |             1.000 |
| dbb_trend  | regime_id           |               7 |                     2 |                   0 |                  2 | loser_positive |             1.000 |
| dbb_trend  | day_of_week         |               7 |                     2 |                   0 |                  2 | loser_positive |             1.000 |
| dbb_trend  | bb_band_width_a_bps |               7 |                     1 |                   0 |                  1 | loser_positive |             1.000 |
| dbb_trend  | bb_position         |               7 |                     1 |                   0 |                  1 | loser_positive |             1.000 |

## How to use

1. `outcome_composition_per_cell.csv` — find cells with high `full_tp_pct` and/or low `clean_stop_pct`.
   These are the cells where the bot's current entry+management actually works.
2. `winner_vs_loser_contrast.csv` — for each such cell, look up which factors define winners vs losers.
3. `management_contrast_fulltp_vs_giveback.csv` — for cells with high `gave_back_green` share,
   compare factor signature to `full_tp` to identify management bugs.
4. `headline_inversions.csv` — these are the factors where conditional logic matters most.
   Same factor flips meaning across cells. Do NOT score them globally.
5. Cluster naming comes from looking at OUTCOME-WINNER signatures (full_tp full_tp full_tp
   patterns across geometric cells), not from the old V1/V2 regime labels.

## Constraints (per direction 2026-05-13)

- Do NOT collapse into one global score
- Do NOT use V1/V2 regime labels as clustering drivers (they're annotations)
- Discovery period is 30 days = the current live epoch. Treat findings as describing
  this epoch, not validated across history
- v1 should extend corpus feature extraction so this same workflow runs at corpus scale