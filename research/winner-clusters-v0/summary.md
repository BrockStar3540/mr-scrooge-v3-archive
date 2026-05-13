# Winner-Cluster Discovery v0 — trade-film ledger

Per 2026-05-13 direction:
- Clustered ACTUAL WINNERS only (n=110: 64 broker + 46 manual)
- Old regime labels NOT used as clustering drivers
- candidate_new_regime + candidate_strategy stay null (your call to name)
- ready_for_backtest stays FALSE for v0

## Clustering result

- Total winners: 110
- Cells with ≥2 winners: 23
- Singleton cells: 33

## Top clusters (≥2 winners)

| cluster_id    | strategy   | pair_family      | session           | direction   |   n_winners |   median_realized_r |   median_mfe_r | pairs                                                   | exit_reasons                              | winner_source_mix                  |
|:--------------|:-----------|:-----------------|:------------------|:------------|------------:|--------------------:|---------------:|:--------------------------------------------------------|:------------------------------------------|:-----------------------------------|
| unk_ant_asi_s | unknown    | antipodean_cross | asia              | short       |           8 |                0.22 |         nan    | ['AUD_CAD', 'AUD_CHF', 'AUD_JPY', 'CAD_JPY', 'NZD_JPY'] |                                           | {'bot_actual_winner': np.int64(8)} |
| unk_usd_lon_s | unknown    | usd_base         | london            | short       |           7 |                0.11 |         nan    | ['GBP_USD', 'USD_CHF']                                  |                                           | {'bot_actual_winner': np.int64(7)} |
| dir_ant_tok_s | direct     | antipodean_cross | tokyo_only        | short       |           6 |                0.92 |           1.36 | ['AUD_CAD', 'CAD_JPY', 'NZD_JPY']                       | {'stop': np.int64(6)}                     | {'manual_ai_curated': np.int64(6)} |
| dir_usd_tok_l | direct     | usd_base         | tokyo_only        | long        |           6 |                0.87 |           1.53 | ['AUD_USD', 'EUR_USD', 'GBP_USD', 'NZD_USD']            | {'stop': np.int64(5), 'tp2': np.int64(1)} | {'manual_ai_curated': np.int64(6)} |
| dir_usd_tok_s | direct     | usd_base         | tokyo_only        | short       |           5 |                0.88 |           1.32 | ['EUR_USD', 'NZD_USD', 'USD_MXN']                       | {'stop': np.int64(5)}                     | {'manual_ai_curated': np.int64(5)} |
| unk_usd_asi_l | unknown    | usd_base         | asia              | long        |           5 |                0.21 |         nan    | ['AUD_USD', 'EUR_USD', 'USD_JPY']                       |                                           | {'bot_actual_winner': np.int64(5)} |
| unk_usd_asi_s | unknown    | usd_base         | asia              | short       |           5 |                0.57 |         nan    | ['AUD_USD', 'NZD_USD', 'USD_JPY', 'USD_MXN']            |                                           | {'bot_actual_winner': np.int64(5)} |
| dbb_usd_lon_s | dbb_trend  | usd_base         | london_ny_overlap | short       |           3 |                0.97 |           1.54 | ['AUD_USD', 'USD_CHF', 'USD_JPY']                       | {'stop': np.int64(3)}                     | {'manual_human': np.int64(3)}      |
| dir_ant_tok_l | direct     | antipodean_cross | tokyo_only        | long        |           3 |                1.50 |           2.07 | ['AUD_JPY', 'NZD_JPY']                                  | {'tp2': np.int64(3)}                      | {'manual_ai_curated': np.int64(3)} |
| unk_ant_lon_s | unknown    | antipodean_cross | london            | short       |           3 |                0.80 |         nan    | ['AUD_JPY', 'NZD_JPY']                                  |                                           | {'bot_actual_winner': np.int64(3)} |
| dir_eur_tok_l | direct     | eur_cross        | tokyo_only        | long        |           2 |                0.89 |           1.12 | ['EUR_AUD', 'EUR_GBP']                                  | {'stop': np.int64(2)}                     | {'manual_ai_curated': np.int64(2)} |
| dir_gbp_asi_l | direct     | gbp_cross        | asia              | long        |           2 |                0.08 |         nan    | ['GBP_JPY']                                             |                                           | {'bot_actual_winner': np.int64(2)} |
| unk_usd_lon_l | unknown    | usd_base         | london            | long        |           2 |                0.08 |         nan    | ['GBP_USD', 'USD_MXN']                                  |                                           | {'bot_actual_winner': np.int64(2)} |
| unk_gbp_asi_s | unknown    | gbp_cross        | asia              | short       |           2 |                0.11 |         nan    | ['GBP_JPY']                                             |                                           | {'bot_actual_winner': np.int64(2)} |
| unk_ant_asi_l | unknown    | antipodean_cross | asia              | long        |           2 |                0.42 |         nan    | ['AUD_CAD', 'NZD_JPY']                                  |                                           | {'bot_actual_winner': np.int64(2)} |
| unk_eur_lon_l | unknown    | eur_cross        | london            | long        |           2 |                1.16 |         nan    | ['EUR_CHF', 'EUR_JPY']                                  |                                           | {'bot_actual_winner': np.int64(2)} |
| unk_ant_lon_l | unknown    | antipodean_cross | london            | long        |           2 |                0.28 |         nan    | ['AUD_CHF', 'AUD_JPY']                                  |                                           | {'bot_actual_winner': np.int64(2)} |
| dbb_ant_ny__s | dbb_trend  | antipodean_cross | ny_only           | short       |           2 |                0.71 |           1.10 | ['AUD_CAD', 'CAD_JPY']                                  | {'stop': np.int64(2)}                     | {'manual_human': np.int64(2)}      |
| unk_eur_asi_l | unknown    | eur_cross        | asia              | long        |           2 |                1.21 |         nan    | ['EUR_JPY', 'EUR_NZD']                                  |                                           | {'bot_actual_winner': np.int64(2)} |
| box_eur_lon_s | box        | eur_cross        | london_only       | short       |           2 |                0.86 |           1.31 | ['EUR_CAD']                                             | {'stop': np.int64(2)}                     | {'manual_human': np.int64(2)}      |
| dbb_usd_asi_s | dbb_trend  | usd_base         | asia              | short       |           2 |                0.80 |         nan    | ['USD_JPY']                                             |                                           | {'bot_actual_winner': np.int64(2)} |
| dir_ant_lon_l | direct     | antipodean_cross | london_ny_overlap | long        |           2 |                0.73 |           1.02 | ['CAD_JPY', 'NZD_JPY']                                  | {'stop': np.int64(2)}                     | {'manual_human': np.int64(2)}      |
| box_usd_ny__s | box        | usd_base         | ny_only           | short       |           2 |                1.18 |           1.63 | ['AUD_USD', 'USD_CAD']                                  | {'stop': np.int64(1), 'tp2': np.int64(1)} | {'manual_human': np.int64(2)}      |

## Singleton winners (one-off, may indicate sparse cell or unusual pair)

| cluster_id    | strategy   | pair_family      | session           | direction   | pairs       |   median_realized_r | winner_source_mix                  |
|:--------------|:-----------|:-----------------|:------------------|:------------|:------------|--------------------:|:-----------------------------------|
| box_gbp_ny__s | box        | gbp_cross        | ny_only           | short       | ['GBP_CHF'] |                1.50 | {'manual_human': np.int64(1)}      |
| dir_eur_lon_s | direct     | eur_cross        | london            | short       | ['EUR_GBP'] |                0.14 | {'bot_actual_winner': np.int64(1)} |
| dir_eur_lon_l | direct     | eur_cross        | london            | long        | ['EUR_JPY'] |                0.11 | {'bot_actual_winner': np.int64(1)} |
| dir_ant_asi_s | direct     | antipodean_cross | asia              | short       | ['AUD_NZD'] |                0.51 | {'bot_actual_winner': np.int64(1)} |
| dir_ant_lon_l | direct     | antipodean_cross | london_only       | long        | ['AUD_JPY'] |                2.00 | {'manual_human': np.int64(1)}      |
| dbb_gbp_ny__l | dbb_trend  | gbp_cross        | ny_only           | long        | ['GBP_CHF'] |                2.00 | {'manual_human': np.int64(1)}      |
| dbb_usd_lon_s | dbb_trend  | usd_base         | london            | short       | ['USD_JPY'] |                1.07 | {'bot_actual_winner': np.int64(1)} |
| dbb_usd_ny__s | dbb_trend  | usd_base         | ny_only           | short       | ['USD_CHF'] |                1.50 | {'manual_human': np.int64(1)}      |
| dir_ant_asi_l | direct     | antipodean_cross | asia              | long        | ['AUD_JPY'] |                0.10 | {'bot_actual_winner': np.int64(1)} |
| dbb_eur_asi_s | dbb_trend  | eur_cross        | asia              | short       | ['EUR_JPY'] |                3.01 | {'bot_actual_winner': np.int64(1)} |
| dbb_gbp_lon_s | dbb_trend  | gbp_cross        | london_only       | short       | ['GBP_CHF'] |                0.86 | {'manual_human': np.int64(1)}      |
| box_usd_lon_l | box        | usd_base         | london_ny_overlap | long        | ['USD_CHF'] |                0.97 | {'manual_human': np.int64(1)}      |
| box_ant_lon_l | box        | antipodean_cross | london_ny_overlap | long        | ['CAD_JPY'] |                0.86 | {'manual_human': np.int64(1)}      |
| box_eur_ny__s | box        | eur_cross        | ny_only           | short       | ['EUR_JPY'] |                1.50 | {'manual_human': np.int64(1)}      |
| box_ant_lon_s | box        | antipodean_cross | london_ny_overlap | short       | ['AUD_JPY'] |                1.00 | {'manual_human': np.int64(1)}      |

## Cross-reference: most-represented pair families in winning

| pair_family      |   count |
|:-----------------|--------:|
| usd_base         |      45 |
| antipodean_cross |      35 |
| eur_cross        |      17 |
| gbp_cross        |      13 |

## Cross-reference: most-represented sessions in winning

| _cluster_session   |   count |
|:-------------------|--------:|
| asia               |      34 |
| tokyo_only         |      22 |
| london             |      21 |
| ny_only            |       9 |
| london_ny_overlap  |       8 |
| london_only        |       5 |
| ny_pm              |       5 |
| overlap            |       4 |
| asia_only          |       2 |

## Cross-reference: direction split

| direction   |   count |
|:------------|--------:|
| short       |      68 |
| long        |      42 |

## What's missing for v1 winner-cluster work

- Factor-snapshot join: broker winners have `factor_snapshot_id` but the
  factor values aren't joined into the ledger (deferred per scope rule).
  v1 should join `live_broker_factor_snapshots.jsonl` to attach the 47 factors.
- Same-time opposite-direction lookup for direction_repair candidates
  (88 rows currently marked `direction_repair_or_skip`). v1 should query the
  factor file at entry_ts ± 30min for opposite-direction candidates and check
  if any won, to distinguish true direction_repair from skip_required.
- Local box-state lookup for box_geometry_repair (87 rows). v1 should compute
  what the corrected box would have been on the entry day and identify the
  legitimate entry point.

## Constraints (per direction 2026-05-13)

- We are NOT trying to save the bot's bad entry. The 87 box_geometry_repair
  rows + 88 direction_repair candidates are NOT yet promoted to 'salvageable'.
  Each needs a local price-action investigation to determine the legitimate
  winning expression that existed at the time.
- The 2 management_repair rows have TBD save_method because the management
  atlas cell mapped to 'needs_investigation' — not enough signal for an
  automatic save_method assignment.
- Clusters are factual groupings of actual winners, not strategy proposals.