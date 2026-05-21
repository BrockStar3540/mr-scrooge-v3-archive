# Moderate-State Mining Summary — 2026-05-20

## Headline result

**Zero qualifying cells across all attempted constraint relaxations.**

| attempt | bars | result |
|---|---|---|
| v1 (purity bar) | n≥26, WR≥55%, no extreme clamps | 0 winners |
| v1 (lowered)    | n≥26, WR≥40% (breakeven at r=1.5R) | 0 winners |
| v1 (further)    | n≥26, WR≥35% / 30%             | 0 winners |
| v2 (objective)  | n≥13, depth-2 splits, per-cell R-target opt, pop≥10% | 0 winners |
| v2 (relaxed)    | same as above, pop≥5%                              | 0 winners |

Across **1,129** (regime, pair, direction, family) signatures in 1.17M deduped corpus trades (26 weeks), **no rule produces positive expectancy at moderate frequency under the current bot framework.**

## Why — the corpus's structural reality

```
Baseline WR distribution across 1,129 signatures:
  median:           0.0%
  75th percentile: 12.5%
  Top WR with n≥26: 21.2%  (AUD_JPY C02 long dbb_trend, n=3,311)

R-target breakeven thresholds:
  r_target = 1.5R  →  breakeven WR = 40%
  r_target = 1.0R  →  breakeven WR = 50%
  r_target = 0.5R  →  breakeven WR = 67%

Maximum WR achievable by moderate (depth-2, pop≥5%) shave: ~30-35%
```

**At no R-target in [0.5, 1.5] can the corpus produce a profitable cell that fires more than 0.5×/week without extreme-percentile clamping.**

## The implication

The v9 bank's 26 trade-tier cells are the ONLY profitable cells extractable from this corpus under this strategy + R-target framework. Those cells reached 65-93% advertised WR by clamping into <10% of population — which made them GHOSTs (15 of 26 fire <0.25/week).

This isn't a mining bug. It's the framework limit. To get more cells, one of these must change:

1. **R-target as a degree of freedom in mining.** The current builder uses fixed `r_target=1.5`. A miner that finds (rule, R-target) pairs maximizing `expectancy × frequency` might surface cells the WR-only optimizer missed — especially at R<1 where the breakeven threshold is higher but rules are easier to satisfy.

2. **Strategy library extension.** The direct/dbb_trend/reversal generators yield 6-21% baseline WR — too weak. Adding new primitives (HTF filters, intermarket signals, news-event windows, microstructure features) would expand the input population.

3. **Different exit modeling.** The corpus uses fixed-R "is_win" labels. If trades that hit a smaller R first (e.g., 0.5R then reverse) were captured at proper R-multiples, the realized expectancy distribution would shift.

None of these are tonight-fixes. They are real research/architecture programs.

## The 11 non-GHOST cells — the actual tradable surface

From `deployable_bank_with_frequency.csv`:

| pair | regime | dir | strategy | family | fires/wk | corpus WR | tradable at |
|---|---|---|---|---|---:|---:|---|
| USD_JPY | C01 | short | echo_box_fade_v2 | reversal | **9.59** | 40.3% | r ≤ 1.5R (borderline) |
| USD_CHF | C02 | long | alpha_breakout_retest_v2 | direct | 1.66 | 51.2% | r ≤ 1.0R or better |
| GBP_NZD | C01 | long | alpha_breakout_retest_v2 | direct | 1.16 | 46.7% | r ≤ 1.0R or better |
| NZD_USD | C01 | long | alpha_pullback_v2 | dbb_trend | 0.73 | 57.9% | r ≤ 0.75R |
| EUR_NZD | C02 | long | charlie_pullback_continuation_v2 | dbb_trend | 0.58 | 66.7% | r ≤ 0.5R or better |
| USD_CHF | C01 | long | echo_box_fade_v2 | reversal | 0.62 | 62.5% | r ≤ 0.6R |
| EUR_AUD | C01 | short | alpha_pullback_v2 | dbb_trend | 0.43 | 100.0% | (small n=11) any R |
| AUD_JPY | C02 | long | TF6_ma_ribbon_long | dbb_trend | 0.62 | 43.8% | r ≤ 1.25R |
| GBP_NZD | C02 | long | charlie_pullback_continuation_v2 | dbb_trend | 0.35 | 66.7% | r ≤ 0.5R |
| USD_MXN | C01 | short | alpha_pullback_v2 | dbb_trend | 0.50 | 53.8% | r ≤ 1.0R |
| CHF_JPY | C02 | long | TF6_ma_ribbon_long | dbb_trend | 0.43 | 9.1% | NOT tradable (busted cell) |

**Effective tradable bank: 9-10 cells.**

## Deployment rule (proposed)

Per Brock 2026-05-20, hard deployment rule going forward:

| frequency class | fires/wk | live deployment |
|---|---:|---|
| REGULAR | > 3.0 | live, primary |
| MODERATE | 1.0-3.0 | live, supplement |
| RARE | 0.25-1.0 | live, opportunistic |
| GHOST | < 0.25 | observe-only, NOT live |

Cells must clear both: edge threshold AND historical activation threshold.

## Next steps (engineering)

1. **GHOST cleanup**: strip the ~5 GHOST signatures from live v10_fast_v1.6 → v1.7
2. **Bank-first scan hook**: build a `bank_priority` strategy class that directly evaluates the 9-10 non-GHOST cells' shave_rules instead of relying on BB→direct emission
3. **Per-cell R-target re-mining**: introduce R as a degree of freedom in the v9 builder
4. **Strategy library audit**: are direct/dbb_trend/reversal really the right primitives, or is the bot trying to trade off the wrong signal generators?

## Files

- `deployable_bank_with_frequency.csv` — frequency stats per cell
- `current_session_bank_priority.csv` — ordered priority list per session
- `data/bank_first_strategy_queue.json` — runtime config for bank-first generation
- `freq_audit_2026-05-20.py` — frequency audit script
- `moderate_state_mining_v2_2026-05-20.py` — final v2 miner (confirmed zero winners)
- `bank_strict_audit_2026-05-20.py` — strict narrowness audit
