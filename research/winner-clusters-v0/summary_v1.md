# Winner-Cluster Discovery v1 (normalized + factor-enriched)

Generated: 2026-05-13T01:49:40.128372+00:00

## What changed from v0

1. `box_geometry_repair` renamed → `correct_box_replay_required`
   (rename reflects: contamination proven, repair not yet proven)
2. Session labels normalized: tokyo_only→asia, asia_only→asia,
   london_only→london, ny_only→ny_pm, london_ny_overlap→overlap
3. 79-key factor snapshots joined to all 196 broker rows
4. Winner clusters rerun on normalized + enriched data

Ledger now has 149 columns (up from 69) — 79 factor_* + the same identity / outcome / repair columns.

## Repair taxonomy distribution (unchanged from v0)

| repair_taxonomy             |   count |
|:----------------------------|--------:|
| actual_winner               |     110 |
| direction_repair_or_skip    |      88 |
| correct_box_replay_required |      87 |
| not_salvageable             |       3 |
| management_repair           |       2 |

## Cluster outcomes

- Total winners: 110
- Cells with ≥2 winners: 23
- Singletons: 29

## Top 15 clusters

| cluster_id     | strategy   | pair_family      | session   | direction   |   n_winners |   n_broker |   n_human |   n_ai_curated |   median_realized_r |   median_mfe_r | pairs                                   |
|:---------------|:-----------|:-----------------|:----------|:------------|------------:|-----------:|----------:|---------------:|--------------------:|---------------:|:----------------------------------------|
| unkn_ant_asi_s | unknown    | antipodean_cross | asia      | short       |           8 |          8 |         0 |              0 |                0.22 |         nan    | AUD_CAD,AUD_CHF,AUD_JPY,CAD_JPY,NZD_JPY |
| dire_ant_asi_s | direct     | antipodean_cross | asia      | short       |           7 |          1 |         0 |              6 |                0.91 |           1.36 | AUD_CAD,AUD_NZD,CAD_JPY,NZD_JPY         |
| unkn_usd_lon_s | unknown    | usd_base         | london    | short       |           7 |          7 |         0 |              0 |                0.11 |         nan    | GBP_USD,USD_CHF                         |
| dire_usd_asi_l | direct     | usd_base         | asia      | long        |           6 |          0 |         0 |              6 |                0.87 |           1.53 | AUD_USD,EUR_USD,GBP_USD,NZD_USD         |
| dire_usd_asi_s | direct     | usd_base         | asia      | short       |           6 |          1 |         0 |              5 |                0.89 |           1.32 | EUR_USD,NZD_USD,USD_JPY,USD_MXN         |
| unkn_usd_asi_l | unknown    | usd_base         | asia      | long        |           5 |          5 |         0 |              0 |                0.21 |         nan    | AUD_USD,EUR_USD,USD_JPY                 |
| unkn_usd_asi_s | unknown    | usd_base         | asia      | short       |           5 |          5 |         0 |              0 |                0.57 |         nan    | AUD_USD,NZD_USD,USD_JPY,USD_MXN         |
| dire_ant_asi_l | direct     | antipodean_cross | asia      | long        |           4 |          1 |         0 |              3 |                1.50 |           2.07 | AUD_JPY,NZD_JPY                         |
| dire_gbp_asi_l | direct     | gbp_cross        | asia      | long        |           3 |          2 |         1 |              0 |                0.08 |           1.33 | GBP_JPY,GBP_NZD                         |
| unkn_ant_lon_s | unknown    | antipodean_cross | london    | short       |           3 |          3 |         0 |              0 |                0.80 |         nan    | AUD_JPY,NZD_JPY                         |
| dbb__usd_ove_s | dbb_trend  | usd_base         | overlap   | short       |           3 |          0 |         3 |              0 |                0.97 |           1.54 | AUD_USD,USD_CHF,USD_JPY                 |
| unkn_eur_lon_l | unknown    | eur_cross        | london    | long        |           2 |          2 |         0 |              0 |                1.16 |         nan    | EUR_CHF,EUR_JPY                         |
| dire_ant_ove_l | direct     | antipodean_cross | overlap   | long        |           2 |          0 |         2 |              0 |                0.73 |           1.02 | CAD_JPY,NZD_JPY                         |
| dbb__ant_ny__s | dbb_trend  | antipodean_cross | ny_pm     | short       |           2 |          0 |         2 |              0 |                0.71 |           1.10 | AUD_CAD,CAD_JPY                         |
| dbb__usd_asi_s | dbb_trend  | usd_base         | asia      | short       |           2 |          2 |         0 |              0 |                0.80 |         nan    | USD_JPY                                 |

## Cross-trust validation cells (broker + theory both have winners here)

Cells where BOTH broker_winner AND (human OR ai_curated) winners exist —
the strongest evidence that the cell is a real winner pocket, not a theory artifact.

| cluster_id     | strategy   | pair_family      | session   | direction   |   n_winners |   n_broker |   n_human |   n_ai_curated |   median_realized_r |   median_mfe_r |
|:---------------|:-----------|:-----------------|:----------|:------------|------------:|-----------:|----------:|---------------:|--------------------:|---------------:|
| dire_ant_asi_s | direct     | antipodean_cross | asia      | short       |           7 |          1 |         0 |              6 |                0.91 |           1.36 |
| dire_usd_asi_s | direct     | usd_base         | asia      | short       |           6 |          1 |         0 |              5 |                0.89 |           1.32 |
| dire_ant_asi_l | direct     | antipodean_cross | asia      | long        |           4 |          1 |         0 |              3 |                1.50 |           2.07 |
| dire_gbp_asi_l | direct     | gbp_cross        | asia      | long        |           3 |          2 |         1 |              0 |                0.08 |           1.33 |

## Best clusters by realized R (top 10 by median, n_winners >= 3)

| cluster_id     | strategy   | pair_family      | session   | direction   |   n_winners |   median_realized_r |   median_mfe_r | pairs                                   |
|:---------------|:-----------|:-----------------|:----------|:------------|------------:|--------------------:|---------------:|:----------------------------------------|
| dire_ant_asi_l | direct     | antipodean_cross | asia      | long        |           4 |                1.50 |           2.07 | AUD_JPY,NZD_JPY                         |
| dbb__usd_ove_s | dbb_trend  | usd_base         | overlap   | short       |           3 |                0.97 |           1.54 | AUD_USD,USD_CHF,USD_JPY                 |
| dire_ant_asi_s | direct     | antipodean_cross | asia      | short       |           7 |                0.91 |           1.36 | AUD_CAD,AUD_NZD,CAD_JPY,NZD_JPY         |
| dire_usd_asi_s | direct     | usd_base         | asia      | short       |           6 |                0.89 |           1.32 | EUR_USD,NZD_USD,USD_JPY,USD_MXN         |
| dire_usd_asi_l | direct     | usd_base         | asia      | long        |           6 |                0.87 |           1.53 | AUD_USD,EUR_USD,GBP_USD,NZD_USD         |
| unkn_ant_lon_s | unknown    | antipodean_cross | london    | short       |           3 |                0.80 |         nan    | AUD_JPY,NZD_JPY                         |
| unkn_usd_asi_s | unknown    | usd_base         | asia      | short       |           5 |                0.57 |         nan    | AUD_USD,NZD_USD,USD_JPY,USD_MXN         |
| unkn_ant_asi_s | unknown    | antipodean_cross | asia      | short       |           8 |                0.22 |         nan    | AUD_CAD,AUD_CHF,AUD_JPY,CAD_JPY,NZD_JPY |
| unkn_usd_asi_l | unknown    | usd_base         | asia      | long        |           5 |                0.21 |         nan    | AUD_USD,EUR_USD,USD_JPY                 |
| unkn_usd_lon_s | unknown    | usd_base         | london    | short       |           7 |                0.11 |         nan    | GBP_USD,USD_CHF                         |

## Distribution by axis after normalization

### Pair family among winners

| pair_family      |   count |
|:-----------------|--------:|
| usd_base         |      45 |
| antipodean_cross |      35 |
| eur_cross        |      17 |
| gbp_cross        |      13 |

### Session among winners

| session_bucket   |   count |
|:-----------------|--------:|
| asia             |      58 |
| london           |      26 |
| ny_pm            |      14 |
| overlap          |      12 |

### Direction among winners

| direction   |   count |
|:------------|--------:|
| short       |      68 |
| long        |      42 |

## Factor signatures for the largest cross-trust clusters

Median factor values across BROKER winners in each cluster (manual rows lack the 47+ factor set).

### dire_gbp_asi_l

| factor              |   median |     q25 |     q75 |   n |
|:--------------------|---------:|--------:|--------:|----:|
| adr_consumed        |    0.206 |   0.206 |   0.206 |   2 |
| atr                 |    1.006 |   1.006 |   1.006 |   2 |
| bb_band_width_a_bps |    3.857 |   3.857 |   3.857 |   2 |
| bb_position         |    0.811 |   0.811 |   0.811 |   2 |
| box_age_hours       |  411.940 | 411.625 | 412.255 |   2 |
| ema20_dist_pct      |   18.380 |  18.380 |  18.380 |   2 |
| ema50_dist_pct      |   14.610 |  14.610 |  14.610 |   2 |
| otr_ratio           |    0.073 |   0.073 |   0.073 |   2 |
| regime_confidence   |    2.000 |   2.000 |   2.000 |   2 |
| regime_score        |    2.000 |   2.000 |   2.000 |   2 |
| rr_ratio            |    0.000 |   0.000 |   0.000 |   2 |
| rsi                 |   56.690 |  56.690 |  56.690 |   2 |
| spread_pips         |    1.700 |   1.700 |   1.700 |   2 |
| volume_ratio        |    0.564 |   0.564 |   0.564 |   2 |
| wall_proximity      |    0.090 |   0.090 |   0.090 |   2 |
| z_score             |    1.243 |   1.243 |   1.243 |   2 |

## Next steps (per direction 2026-05-13)

Step 5 (next turn): box-geometry forensic for 87 `correct_box_replay_required` rows.
Replay each contaminated entry's date+pair with correct PDH/PDL, identify the
legitimate winning entry that existed at the time.

Step 6 (after step 5): direction-repair forensic for 88 `direction_repair_or_skip`.
Query factor file at entry_ts ± 30min for opposite-direction candidates.

Still not yet: candidate_new_regime naming, candidate_strategy naming, ready_for_backtest.
Clusters are visible but synchrony work continues.