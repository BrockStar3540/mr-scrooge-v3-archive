# Loser Contrast Bank

Mirrored archive of losing trades for every seed in the winner sibling bank, plus false-friend sibling traps.
Built from `winner_island_sibling_seed_bank.csv`, `fast_targeted_false_friend_siblings.csv`, and `all_strategies_all_pairs_trades.parquet`.
Per Brock 2026-05-14 doctrine: keep losers as contrast inventory, not noise.

## Summary
- Seeds processed: 141
- Distinct parent cells: 60
- Parent losers: 132,907 rows
- Rejected-by-shave losers: 253,851 rows
- Residual losers: 217 rows
- False-friend sibling losers: 17,667 rows

## Files
- `loser_contrast_bank.csv` — full row-level loser archive (404,642 rows)
- `loser_contrast_bank_seed_index.csv` — per-seed loser counts + purity class
- `loser_contrast_bank_false_friend_index.csv` — per-false-friend trap counts

## Purity class distribution
```
purity_class
exploratory      63
near_pure        43
holdout_clean    29
pure              6
```

## Schema (loser_contrast_bank.csv)
```
seed_id / false_friend_id  — one is populated depending on artifact lineage
bucket                     — 'parent' | 'rejected_by_shave' | 'residual' | 'false_friend_sibling'
matched_rule               — rule that defined the winner seed or false-friend trap
parent_strategy, parent_pair, parent_direction, parent_regime
entry_ts, realized_R, mfe_R, mae_R, exit_reason
session_bucket, hour_utc, weekday
ADX14, ATR_ratio, BB_compress, RSI14, price_pos, volume_ratio
```