# Conditional Factor Atlas v0

Generated: 2026-05-13T00:05:10.660160+00:00

## Scope honesty

- Source: `per_trade_factors_filled.csv.gz` — 90,024 filled trades
- Time window: 2026-03-15 → 2026-04-13 (30 days, all post-2024)
- Strategies: ['dbb_trend', 'direct']
- Regimes (V1/V2 state machine, NOT V2 classifier): ['CAUTION', 'NORMAL', 'RESTRICTED']
- Pair families: ['antipodean_cross', 'eur_cross', 'gbp_cross', 'usd_base']
- Factor columns: 46

## Cells

- Primary grain (strategy × pair_family × direction): 14 cells, 644 (cell, factor) rows
- Full grain (× regime × session): 120 cells, 5,520 (cell, factor) rows

## Inversion headline

Across primary grain cells (strategy × pair_family × direction), how each factor's sign behaves:

| strategy   |   INVERTED |   loser_positive |   neutral_only |   winner_positive |
|:-----------|-----------:|-----------------:|---------------:|------------------:|
| dbb_trend  |          4 |               10 |             18 |                14 |
| direct     |         15 |               11 |             16 |                 4 |

### Most-inverted factors (consensus = INVERTED, sorted by lowest stability)

These factors switch meaning between cells. Same factor is winner-positive in some
(strategy, pair_family, direction) combinations and loser-positive in others.
**This is the structural evidence that the old global 47-factor system was unconditioned.**

| strategy   | factor                |   n_cells_total |   n_cells_non_neutral |   n_winner_positive |   n_loser_positive |   n_neutral | consensus   |   stability_score |
|:-----------|:----------------------|----------------:|----------------------:|--------------------:|-------------------:|------------:|:------------|------------------:|
| direct     | volume_ratio          |               8 |                     6 |                   3 |                  3 |           2 | INVERTED    |             0.500 |
| direct     | rsi                   |               8 |                     8 |                   4 |                  4 |           0 | INVERTED    |             0.500 |
| direct     | adr_consumed          |               8 |                     7 |                   4 |                  3 |           1 | INVERTED    |             0.571 |
| direct     | total_overhead        |               8 |                     5 |                   3 |                  2 |           3 | INVERTED    |             0.600 |
| direct     | atr                   |               8 |                     8 |                   5 |                  3 |           0 | INVERTED    |             0.625 |
| dbb_trend  | tier_b_flag           |               6 |                     3 |                   2 |                  1 |           3 | INVERTED    |             0.667 |
| dbb_trend  | bb_position           |               6 |                     3 |                   1 |                  2 |           3 | INVERTED    |             0.667 |
| dbb_trend  | z_score               |               6 |                     3 |                   1 |                  2 |           3 | INVERTED    |             0.667 |
| direct     | v3_pairs_total        |               8 |                     6 |                   4 |                  2 |           2 | INVERTED    |             0.667 |
| direct     | avg_volume            |               8 |                     6 |                   2 |                  4 |           2 | INVERTED    |             0.667 |
| direct     | bb_band_width_a_bps   |               8 |                     6 |                   2 |                  4 |           2 | INVERTED    |             0.667 |
| direct     | bb_band_width_b_bps   |               8 |                     6 |                   2 |                  4 |           2 | INVERTED    |             0.667 |
| direct     | range_half            |               8 |                     7 |                   5 |                  2 |           1 | INVERTED    |             0.714 |
| direct     | current_volume        |               8 |                     7 |                   2 |                  5 |           1 | INVERTED    |             0.714 |
| direct     | sma20_dist_signed_bps |               8 |                     4 |                   3 |                  1 |           4 | INVERTED    |             0.750 |
| dbb_trend  | rsi                   |               6 |                     5 |                   1 |                  4 |           1 | INVERTED    |             0.800 |
| direct     | hour_utc              |               8 |                     5 |                   1 |                  4 |           3 | INVERTED    |             0.800 |
| direct     | minute_of_day         |               8 |                     5 |                   1 |                  4 |           3 | INVERTED    |             0.800 |
| direct     | day_of_week           |               8 |                     6 |                   5 |                  1 |           2 | INVERTED    |             0.833 |

### Most-stable winner-positive factors (consensus = winner_positive)

These factors consistently mark winners across all cells where the signal is
non-neutral. They're the candidates for 'always-on' winner indicators (within this
30-day window — not yet validated across periods).

| strategy   | factor              |   n_cells_total |   n_cells_non_neutral |   n_winner_positive |   n_loser_positive |   n_neutral | consensus       |   stability_score |
|:-----------|:--------------------|----------------:|----------------------:|--------------------:|-------------------:|------------:|:----------------|------------------:|
| direct     | wall_proximity      |               8 |                     8 |                   8 |                  0 |           0 | winner_positive |             1.000 |
| direct     | regime_score        |               8 |                     5 |                   5 |                  0 |           3 | winner_positive |             1.000 |
| direct     | bb_position         |               8 |                     4 |                   4 |                  0 |           4 | winner_positive |             1.000 |
| dbb_trend  | adr_consumed        |               6 |                     4 |                   4 |                  0 |           2 | winner_positive |             1.000 |
| dbb_trend  | ema20_dist_pct      |               6 |                     4 |                   4 |                  0 |           2 | winner_positive |             1.000 |
| direct     | z_score             |               8 |                     4 |                   4 |                  0 |           4 | winner_positive |             1.000 |
| dbb_trend  | bb_band_width_a_bps |               6 |                     3 |                   3 |                  0 |           3 | winner_positive |             1.000 |
| dbb_trend  | box_age_hours       |               6 |                     3 |                   3 |                  0 |           3 | winner_positive |             1.000 |
| dbb_trend  | tier_a_flag         |               6 |                     3 |                   3 |                  0 |           3 | winner_positive |             1.000 |
| dbb_trend  | volume_ratio        |               6 |                     3 |                   3 |                  0 |           3 | winner_positive |             1.000 |
| dbb_trend  | ema50_dist_pct      |               6 |                     2 |                   2 |                  0 |           4 | winner_positive |             1.000 |
| dbb_trend  | bb_band_width_b_bps |               6 |                     2 |                   2 |                  0 |           4 | winner_positive |             1.000 |
| dbb_trend  | score               |               6 |                     2 |                   2 |                  0 |           4 | winner_positive |             1.000 |
| dbb_trend  | current_volume      |               6 |                     1 |                   1 |                  0 |           5 | winner_positive |             1.000 |
| dbb_trend  | minute_of_day       |               6 |                     1 |                   1 |                  0 |           5 | winner_positive |             1.000 |

### Most-stable loser-positive factors

Consistently mark losers. These are 'do NOT take' signals.

| strategy   | factor                |   n_cells_total |   n_cells_non_neutral |   n_winner_positive |   n_loser_positive |   n_neutral | consensus      |   stability_score |
|:-----------|:----------------------|----------------:|----------------------:|--------------------:|-------------------:|------------:|:---------------|------------------:|
| direct     | ema50_dist_pct        |               8 |                     8 |                   0 |                  8 |           0 | loser_positive |             1.000 |
| direct     | regime_confidence     |               8 |                     8 |                   0 |                  8 |           0 | loser_positive |             1.000 |
| direct     | otr_ratio             |               8 |                     7 |                   0 |                  7 |           1 | loser_positive |             1.000 |
| direct     | regime_id             |               8 |                     7 |                   0 |                  7 |           1 | loser_positive |             1.000 |
| direct     | rr_ratio              |               8 |                     7 |                   0 |                  7 |           1 | loser_positive |             1.000 |
| direct     | spread_pips           |               8 |                     6 |                   0 |                  6 |           2 | loser_positive |             1.000 |
| direct     | ema20_dist_pct        |               8 |                     6 |                   0 |                  6 |           2 | loser_positive |             1.000 |
| direct     | tier_b_flag           |               8 |                     5 |                   0 |                  5 |           3 | loser_positive |             1.000 |
| dbb_trend  | rr_ratio              |               6 |                     5 |                   0 |                  5 |           1 | loser_positive |             1.000 |
| direct     | score                 |               8 |                     5 |                   0 |                  5 |           3 | loser_positive |             1.000 |
| direct     | tier_a_flag           |               8 |                     4 |                   0 |                  4 |           4 | loser_positive |             1.000 |
| direct     | box_age_hours         |               8 |                     3 |                   0 |                  3 |           5 | loser_positive |             1.000 |
| dbb_trend  | sma20_dist_signed_bps |               6 |                     3 |                   0 |                  3 |           3 | loser_positive |             1.000 |
| dbb_trend  | total_overhead        |               6 |                     2 |                   0 |                  2 |           4 | loser_positive |             1.000 |
| dbb_trend  | range_half            |               6 |                     1 |                   0 |                  1 |           5 | loser_positive |             1.000 |

## How to use this atlas

DO NOT collapse into a single score. The point of the atlas is that the same
factor means different things in different cells.

Workflow:
1. Pick a candidate pocket from the regime × pair matrix (e.g. Echo-tight × USD_CHF,
   Charlie × CAD_JPY × holdout).
2. Look up the matching cell in `atlas_full.csv` (strategy × regime × pair_family ×
   session × direction). Note: V2 regime labels are NOT in this v0; use V1/V2 state
   regime as a proxy and cross-reference manually.
3. Identify which factors are winner-positive vs loser-positive in THAT cell.
4. Cross-check the inverted factors — same factor in a neighboring cell may say
   the opposite.
5. The winning factor signature in the cell is one candidate micro-strategy input.

## What v0 cannot do

- No discovery/holdout period split (data is 30 days, all in holdout era)
- No V2 regime labels (corpus join recovered only 7.8%, abandoned)
- No cross-period stability for individual factors (would need same data >12 months)
- No micro-strategy promotion logic (out of scope by direction)

Next iteration v1 should extend feature extraction to corpus (currently 11 features
in `feature_snapshot`; need 47+). Then atlas can run on full V2 regime grain with
real discovery/holdout split.