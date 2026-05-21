# Moderate-State Mining Summary — 2026-05-20

## Headline result

**Zero qualifying cells.** Across 1,129 (regime, pair, direction, family) signatures in the corpus (1.17M deduped trades over 26 weeks), **none** clear the bar:

- n ≥ 26 (≥ 1 fire/week)
- WR ≥ 40% (breakeven at the bot's `r_target=1.5R`)
- No extreme-percentile clamps (≥10% of population must satisfy the rule)

## Why this matters

The bot's current strategy/R-target framework appears structurally incapable of producing moderate-frequency profitable cells in this corpus. The 26 trade-tier cells in `v9_observe` reached their advertised 65-93% WRs only by **extreme-percentile clamping** — which shrunk samples to the point that they fire less than once per week (15 of 26 are GHOSTs at < 0.25 fires/week).

## The corpus baseline reality

```
1,129 signatures total
Median WR across signatures:    0.0%   (most generate losing-bias trades)
75th percentile WR:             12.5%
Top WR with n≥26:               21.2%  (AUD_JPY C02 long dbb_trend, n=3,311)
Signatures with n≥26 AND WR≥30%:  0
Signatures with n≥26 AND WR≥40%:  0
```

At `r_target=1.5R` the breakeven WR is **40%**. The corpus has zero high-frequency signatures meeting it. The v9 bank reached 65-93% only by clamping into very rare conditions.

## The 11 cells that actually fire

From `deployable_bank_with_frequency.csv`, non-GHOST cells (≥0.25 fires/week):

| pair | regime | dir | strategy | family | fires/wk | corpus WR | r_target=1.5R breakeven |
|---|---|---|---|---|---:|---:|---|
| USD_JPY | C01 | short | echo_box_fade_v2 | reversal | **9.59** | 40.3% | borderline |
| NZD_USD | C01 | long | alpha_pullback_v2 | dbb_trend | 0.73 | 57.9% | ✓ |
| AUD_JPY | C02 | long | TF6_ma_ribbon_long | dbb_trend | 0.62 | 43.8% | ✓ |
| USD_CHF | C01 | long | echo_box_fade_v2 | reversal | 0.62 | 62.5% | ✓ |
| EUR_NZD | C02 | long | charlie_pullback_continuation_v2 | dbb_trend | 0.58 | 66.7% | ✓ |
| USD_MXN | C01 | short | alpha_pullback_v2 | dbb_trend | 0.50 | 53.8% | ✓ |
| EUR_AUD | C01 | short | alpha_pullback_v2 | dbb_trend | 0.43 | 100.0% | ✓ |
| CHF_JPY | C02 | long | TF6_ma_ribbon_long | dbb_trend | 0.43 | 9.1% | ✗ (busted cell) |
| GBP_NZD | C02 | long | charlie_pullback_continuation_v2 | dbb_trend | 0.35 | 66.7% | ✓ |
| USD_CHF | C02 | long | alpha_breakout_retest_v2 | direct | 1.66 | 51.2% | ✓ |
| GBP_NZD | C01 | long | alpha_breakout_retest_v2 | direct | 1.16 | 46.7% | ✓ |

**Of 26 trade-tier cells, only ~9 are both repeatable AND profitable at the bot's R-target.**

## Three structural conclusions

### 1. The strategy library is the bottleneck

The underlying direct/dbb_trend/reversal signal generators produce 6-21% WR baselines across all pairs/regimes/directions. This is below the bot's 40% breakeven threshold. The only way to get profitable cells is to filter aggressively → rare events.

### 2. R-target tuning is the missing degree of freedom

Cells could be tradable at lower R-targets (e.g., 0.5R or 1R, breakeven at 67% or 50%) with **less aggressive** shave_rule clamping, producing more moderate-frequency winners. The current `r_target: 1.5` for every cell is a one-size-fits-all assumption that doesn't match the corpus reality.

### 3. The bot's actual tradable surface is ~9 cells

Not 26. Not 36. **About 9 cells** that fire more than once per week AND have positive expectancy at 1.5R. Most of those need to be hunted actively (bank-first generation, see `bank_first_strategy_queue.json`).

## Recommended next moves

1. **Ship bank-first generation** (`bank_first_strategy_queue.json` is ready) — make the bot actively hunt these 9 cells in their right sessions instead of relying on BB->direct emission to stumble into them.

2. **Re-mine with per-cell R-target** — instead of fixing `r_target=1.5` for all, let the miner find (shave_rule, R-target) pairs that maximize `expectancy × frequency`. This may surface cells the WR-only optimizer missed.

3. **Audit the GHOST cells out of live deployment** — remove the 15 GHOST cells from v10_fast_v1.6 so the live surface is honest. Keeping them just clutters routing without practical fires.

4. **Investigate strategy library extensions** — the 1,129 signature × 26 weeks corpus may be saturated for this strategy family. Adding new strategy primitives (e.g., higher-timeframe filters, intermarket signals, news-event windows) is the only path to a meaningfully broader bank.

## Files

- `deployable_bank_with_frequency.csv` — per-cell frequency stats
- `current_session_bank_priority.csv` — ordered priority list per session
- `data/bank_first_strategy_queue.json` — runtime config for bank-first generation
- `moderate_state_cells.csv` — would have contained mining winners; empty because none qualify
- `bank_strict_audit_2026-05-20.py` — the strict narrowness audit that surfaced the GHOST problem
