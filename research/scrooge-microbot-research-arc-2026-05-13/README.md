# Scrooge Microbot Research Arc — 2026-05-13

Two-day research session investigating whether textbook OHLCV strategies on M5 forex have any deployable conditional edge across the 26-pair universe.

## Final outcome

- 2 observe-mode micro-bots shipped to V3 (`TF6_short USD_JPY`, `TF6_long USD_MXN`) — see `docs/MICRO_BOTS.md` and `docs/research_notes_held_back.csv`.
- 1 critical V3 bug fixed: `features/technical_context.py` was reading the still-forming current M15/H1 bar (look-ahead bias).
- Reusable validation pipeline established (look-ahead correction → walk-forward → CI bounds → vol-conditional spread → slippage MC → fire-time concentration → contrast set mining → permutation test).

## Top-level findings

- **Test 1 (factor analysis):** ATR_ratio is the #1 winner/loser discriminator in 773 of 894 cells (86%). 268 cells show strong separation (|d| ≥ 0.5). Winners systematically prefer higher relative volatility than losers.
- **Test 2 (53-regime cross-tab):** 0 of 1,025 mass-data cells have a winner-dominant regime. The 53-regime taxonomy does not separate winners from losers.
- **Test 3 (inside-regime splits):** 293 in-sample decision-tree splits found, 0 survive temporal out-of-sample (CI > 0 on 2024-Apr 2026). Real in-sample structure that does not generalize forward.

## Directory contents

```
scripts/                  Python research scripts (28 files, 276 KB)
reports/                  Detailed per-test result CSVs (36 files, 1 MB)
root-outputs/             Headline output tables (9 files, 3.4 MB)
README.md                 this file
```

## Headline result tables (root-outputs/)

| File | Rows | What |
|---|---:|---|
| strategy_pair_summary.csv | 1,444 | Per (strategy, pair, direction): n, winners, losers, win_rate, mean_R, per-year stats |
| test1_factor_analysis_full.csv | ~6k | Per (cell, factor): Cohen's d + KS p-value |
| test1_top_factor_per_cell.csv | 894 | Per cell: #1 discriminating factor |
| test1_top2_factors_per_cell.csv | ~1.8k | Per cell: top 2 factors |
| test2_regime_crosstab_full.csv | 12,839 | Per (cell × regime): n, wins, losses, win_rate |
| test2_loser_heavy_regimes.csv | 928 | Skip-rules: regimes with WR ≤ 5% and n ≥ 50 |
| test2_regime_separability.csv | 1,025 | Per cell: count of winner/loser/mixed regimes |
| test2_winning_regime_cells.csv | 4 | The only 4 cells with WR ≥ 50% on n ≥ 30 |
| test3_inside_regime_splits.csv | 293 | Decision-tree splits inside mass-mixed regime cells, with train + test stats |

## How to re-run

Foundational dataset: `all_strategies_all_pairs_trades.parquet` (14.9M trades, 26 pairs × 56 strategies, 1.4 GB) — staged on Mac Mini at `~/scrooge-research/`. Regenerable from EC2 dukascopy cache + `research/ohlcv-strategy-library-v0/backtest_ohlcv_strategy_library_v0.py`.

Each test script lives in `scripts/`:
- Test 1 → `test1_factor_analysis.py`
- Test 2 → `test2_regime_analysis.py`
- Test 3 → `test3_inside_regime_split.py`

## Linked
- `docs/MICRO_BOTS.md` — the 2 shipped observers
- `docs/research_notes_held_back.csv` — 5 cells held from shipping
- `research/raw-m5-winner-factory-v2/` — predecessor arc (retracted)
- `research/ohlcv-strategy-library-v0/` — strategy library backtester source
