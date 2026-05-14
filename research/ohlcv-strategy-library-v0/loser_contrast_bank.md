# Loser Contrast Bank

Mirrored archive of losing trades for every seed in the winner sibling bank.
Built from `winner_island_sibling_seed_bank.csv` + `all_strategies_all_pairs_trades.parquet`.
Per Brock 2026-05-14 doctrine: keep losers as contrast inventory, not noise.

## Summary
- Seeds processed: 141
- Distinct parent cells: 60
- Parent losers: 132,907 rows
- Rejected-by-shave losers: 253,458 rows (per seed mirror)
- Residual losers: 610 rows (in-seed failure modes)
- False-friend siblings: NOT YET BUILT — requires re-running shaver with permissive output

## Files
- `loser_contrast_bank.csv` — full row-level loser archive (386,975 rows)
- `loser_contrast_bank_seed_index.csv` — per-seed loser counts + purity class

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
seed_id                — int. -1 = parent-cell loser (pre-seed background)
                        Otherwise refers to a row in loser_contrast_bank_seed_index.csv
bucket                 — 'parent' | 'rejected_by_shave' | 'residual'
parent_strategy        — textbook strategy_id
parent_pair            — currency pair
parent_direction       — long | short
parent_regime          — technical_regime_53 of the parent cell
entry_ts               — UTC timestamp
realized_R             — outcome (always <= 0 here, since this is the loser archive)
mfe_R, mae_R           — within-trade extremes
exit_reason            — stop | time | etc
session_bucket, hour_utc, weekday
ADX14, ATR_ratio, BB_compress, RSI14, price_pos, volume_ratio
```

## Use cases
1. **Skip maps**: aggregate parent + rejected losers by factor combinations → conditions to avoid
2. **Boundary definition**: rejected_by_shave losers per seed = the seed's mirrored exclusion set
3. **Next-pass material**: residual_losers per near-pure seed = inputs for the recursive shave
4. **Anti-regime discovery**: cluster the parent loser population for potential reversal seeds

## Cross-references
- [[seed-factory-doctrine]] — operating doctrine
- [[scrooge-microbot-research-arc]] — research arc
- `research/ohlcv-strategy-library-v0/winner_island_sibling_seed_bank.csv` — paired winner bank