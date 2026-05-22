# Missing Strategy Gap: Box Theory + Double Bollinger Band

## What's missing

- **Box Theory**: zero strategy_ids in the trade_log corpus match. The corpus is 56 strategies; Brock's spec was 66 (gap of 10).
- **True Double Bollinger Band**: the corpus has only `MR2_bb_reversion` (single BB mean-reversion). The Double-BB strategy uses TWO BB bands (typically 1σ + 2σ) and a different entry logic — that is not in this corpus.

## What IS in the corpus that resembles Box Theory

- `RG1_range_bound_scalp_*`: range-bound scalping — Darvas-style box trading
- `RG2_range_support_bounce_long`, `RG3_midrange_drift_fade_short`
- `BR1_range_breakout_*`, `BR5_opening_range_breakout_*`
- `SS1_asian_range_breakout_*`
- `FB1_false_breakout_reversal_*`

These are *related* but not Box Theory as a distinct named strategy.

## Sourcing plan (parallel, non-blocking)

1. Identify the original Box Theory and Double-BB strategy definitions (where are they specified?)
2. Add them to the strategy library / replay engine
3. Re-run the 10/12/ratchet relabel including the new strategies
4. Merge supplemental cells into the next routing-table build (v2.0+)

Tracking: this gap should not block v1.9 deployment. The 56 strategies we have already produce 38 parent seeds with positive expectancy.
