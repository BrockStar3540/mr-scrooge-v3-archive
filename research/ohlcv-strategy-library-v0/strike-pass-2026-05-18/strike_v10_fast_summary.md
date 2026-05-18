# Current-regime strike pass — v10_fast candidate set

**Generated**: 2026-05-18T16:12:00.491288+00:00
**Ledger span**: 10.4 hours / 9,700 rows / 4,850 live candidates

## Active universe (what the bot is actually seeing)

- regimes: `['C02', 'C01']`
- sessions: `['ny_open', 'ny_mid', 'london_open', 'asia_late']`
- pairs: `['EUR_USD', 'USD_CHF', 'EUR_NZD', 'GBP_USD', 'EUR_CAD', 'EUR_AUD', 'GBP_AUD', 'EUR_GBP', 'GBP_CAD', 'GBP_CHF', 'AUD_USD', 'NZD_USD', 'USD_CAD', 'EUR_CHF', 'GBP_JPY', 'EUR_JPY', 'AUD_NZD', 'GBP_NZD', 'USD_JPY', 'AUD_JPY']`

- families: {'direct': 4752, 'dbb_trend': 98}

## [A] Live-validated cells
Cells where the shadow gate emitted `shave_rule_satisfied` >= 2 times.
These are the strongest live evidence we have — rule fires correctly on live ticks.

| regime | pair | strategy | dir | session | live_passes | v9_tier | v9_n | v9_wr | v9_lb |
|---|---|---|---|---|---:|---|---:|---:|---:|
| C02 | EUR_CAD | charlie_compression_breakout | long | ny_mid | 41 | Seed | 13 | 0.923 | 0.775 |
| C01 | EUR_GBP | charlie_compression_breakout | long | ny_open | 37 | Seed | 11 | 0.818 | 0.632 |
| C02 | USD_CHF | alpha_breakout_retest_v2 | long | ny_mid | 36 | Seed-Pro | 17 | 0.882 | 0.747 |
| C01 | USD_CHF | alpha_breakout_retest_v2 | short | ny_open | 24 | Seed | 11 | 0.818 | 0.632 |
| C02 | GBP_CHF | alpha_breakout_retest_v2 | short | ny_open | 6 | Seed | 10 | 0.900 | 0.718 |
| C01 | EUR_CHF | charlie_compression_breakout | long | ny_open | 2 | Seed | 17 | 0.706 | 0.551 |
| C02 | EUR_NZD | charlie_pullback_continuation_v2 | short | ny_open | 2 | Seed | 11 | 0.818 | 0.632 |

## [B] High-demand Seed cells (top 25)
Cells the bot hit at min_tier=Seed >= 30 times (lots of live candidates,
but blocked at tier check before shave_rule eval). Not live-validated, but high-priority
for promotion *if* in-sample evidence is strong.

| regime | pair | strategy | dir | session | seed_hits | v9_tier | v9_n | v9_wr | v9_lb |
|---|---|---|---|---|---:|---|---:|---:|---:|
| C02 | EUR_NZD | alpha_breakout_retest_v2 | short | ny_open | 200 | Seed | 12 | 0.750 | 0.567 |
| C02 | AUD_USD | alpha_breakout_retest_v2 | long | ny_mid | 190 | Seed | 12 | 0.750 | 0.567 |
| C02 | EUR_AUD | alpha_breakout_retest_v2 | short | ny_mid | 178 | Seed | 10 | 0.800 | 0.602 |
| C02 | EUR_NZD | alpha_breakout_retest_v2 | short | ny_mid | 174 | Seed | 12 | 0.750 | 0.567 |
| C02 | EUR_AUD | alpha_breakout_retest_v2 | short | ny_open | 171 | Seed | 10 | 0.800 | 0.602 |
| C02 | EUR_GBP | alpha_breakout_retest_v2 | long | ny_open | 160 | Seed | 10 | 0.900 | 0.718 |
| C02 | GBP_CHF | alpha_breakout_retest_v2 | short | ny_open | 152 | Seed | 10 | 0.900 | 0.718 |
| C02 | EUR_CAD | alpha_breakout_retest_v2 | short | ny_mid | 144 | Seed | 10 | 0.800 | 0.602 |
| C02 | GBP_USD | charlie_compression_breakout | short | ny_mid | 143 | Seed | 11 | 0.909 | 0.740 |
| C02 | USD_CHF | alpha_breakout_retest_v2 | short | ny_open | 135 | Seed | 14 | 0.857 | 0.700 |
| C02 | EUR_CAD | charlie_compression_breakout | long | ny_open | 130 | Seed | 13 | 0.923 | 0.775 |
| C02 | GBP_USD | alpha_breakout_retest_v2 | long | ny_open | 117 | Seed | 17 | 0.824 | 0.679 |
| C02 | GBP_AUD | alpha_breakout_retest_v2 | short | ny_open | 112 | Seed | 10 | 1.000 | 0.859 |
| C02 | EUR_USD | alpha_breakout_retest_v2 | short | ny_mid | 112 | Seed | 11 | 0.818 | 0.632 |
| C02 | GBP_CAD | alpha_breakout_retest_v2 | short | ny_open | 107 | Seed | 11 | 0.909 | 0.740 |
| C02 | USD_CHF | alpha_breakout_retest_v2 | short | ny_mid | 102 | Seed | 14 | 0.857 | 0.700 |
| C02 | USD_CAD | charlie_compression_breakout | short | ny_mid | 88 | Seed | 12 | 0.750 | 0.567 |
| C02 | GBP_USD | charlie_compression_breakout | short | ny_open | 85 | Seed | 11 | 0.909 | 0.740 |
| C02 | GBP_AUD | alpha_breakout_retest_v2 | short | ny_mid | 76 | Seed | 10 | 1.000 | 0.859 |
| C02 | EUR_GBP | alpha_breakout_retest_v2 | long | ny_mid | 66 | Seed | 10 | 0.900 | 0.718 |
| C01 | USD_CAD | charlie_compression_breakout | short | ny_mid | 59 | Seed | 13 | 0.769 | 0.595 |
| C02 | EUR_CAD | alpha_breakout_retest_v2 | short | ny_open | 58 | Seed | 10 | 0.800 | 0.602 |
| C02 | EUR_JPY | alpha_breakout_retest_v2 | short | ny_open | 54 | Seed | 13 | 0.769 | 0.595 |
| C01 | EUR_CHF | charlie_compression_breakout | long | ny_open | 52 | Seed | 17 | 0.706 | 0.551 |
| C01 | GBP_NZD | charlie_compression_breakout | short | ny_open | 46 | Seed | 11 | 0.818 | 0.632 |

## v10_fast candidate set
Total cells: **10**
  - live_validated path: 7
  - high_demand_strong_in_sample path: 3

By family:
- `direct`: 9
- `dbb_trend`: 1

By cell_strategy:
- `alpha_breakout_retest_v2`: 5
- `charlie_compression_breakout`: 4
- `charlie_pullback_continuation_v2`: 1

By regime:
- `C02`: 7
- `C01`: 3

By session:
- `ny_open`: 7
- `ny_mid`: 3

## Deployment plan

1. Build `routing_table_v10_fast_current_regime.parquet` from these cells with `tier='Fast'`.
2. Add `Fast` to the EntryFilterGate tier rank (between Seed-Pro and Pro).
3. Flip `gates.entry_filter.min_tier = 'Fast'` and `routing_table_path` to the new parquet.
4. Bot resumes live trading with this narrow current-regime surface.

Risk profile: all live-validated cells fired correctly in shadow >= threshold times.
High-demand cells have v9 in-sample wr >= 0.85 / n >= 12. Both bounded by daily-circuit,
cooldown, debounce, and existing zone-blacklist gates. Position sizing unchanged.

Caveat: probe cells lack corpus-OOS evidence. Live deployment IS the OOS test.
Recommend daily-circuit threshold tightened (e.g. 2.5% from 3%) until ~50 cells have
accumulated >= 5 LIMIT placements each, then revert.