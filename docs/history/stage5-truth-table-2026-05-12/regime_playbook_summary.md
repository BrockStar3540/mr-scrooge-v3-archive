# Regime x Playbook Truth Table (Stage 5)

**Ledgers:** 208; **trades:** 2543184

## Locked thresholds

| Period | min_n | concentration unit | unit cap | pair cap |
|---|---|---|---|---|
| discovery | 75 | year | 50% | 40% |
| holdout | 30 | quarter | 65% | 50% |

Plus: bootstrap 95% CI lower bound of mean(realized_r) > 0 in both periods.

## Verdict

**Surviving cells:** 0
**Milestone 1 trigger (>= 2):** FAIL

## Per-cell results

| regime | probe | discovery | failure | holdout | failure | survives |
|---|---|---|---|---|---|---|
| Alpha-extended | alpha_extended_fade_v2 | FAIL | ci | FAIL | ci | no |
| Alpha-fresh | alpha_breakout_retest_v2 | FAIL | ci | FAIL | ci | no |
| Alpha-fresh | alpha_pullback_v2 | FAIL | ci | FAIL | ci | no |
| Bravo | bravo_expansion_continuation | FAIL | ci | FAIL | ci | no |
| Bravo | bravo_failed_momentum | FAIL | year_concentration | FAIL | ci | no |
| Charlie | charlie_compression_breakout | FAIL | ci | FAIL | ci | no |
| Charlie | charlie_pullback_continuation_v2 | FAIL | ci | FAIL | ci | no |
| Delta | delta_tag_and_go_v2 | FAIL | ci | FAIL | ci | no |
| Echo-explosive | echo_failed_breakout_v2 | FAIL | ci | FAIL | missing_period | no |
| Echo-tight | echo_box_fade_v2 | PASS | - | FAIL | ci,quarter_concentration,pair_concentration | no |

See `regime_playbook_truth_table.csv` for full per-cell stats.