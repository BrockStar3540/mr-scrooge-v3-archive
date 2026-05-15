# routing_table_v3 summary

**Built:** 2026-05-15T16:39:22.749998+00:00
**Source:** A-survivors from OOS validation (oos_validation_strong_islands.csv)
**Filter:** oos_status==ok AND A_post_WR>=0.25 AND A_n_kept>=20
**Rows:** 157
**Unique leaves (regime53 x pair x session):** 96

## Compared to v2 (1,881 rows, 528 leaves)

- v3 is **8% the size** — much tighter cell list
- v3 is **OOS-validated**: every cell holds at test post_WR >= 0.25 on the 2025-01-01+ holdout
- v3 carries the deployable **shave_rule** per cell for stage-2 entry filtering

## Family composition

- **dbb_trend**: 125 cells
- **direct**: 9 cells
- **reversal**: 23 cells

## Direction composition

- **long**: 79 cells
- **short**: 78 cells

## Top regimes

| regime | desc | cells |
|---|---|---:|
| C02 | tight_coil_adx | 94 |
| C01 | tight_coil_low_adx | 63 |

## Top sessions

- asia: 16 cells
- london_open: 36 cells
- ny_close: 9 cells
- ny_mid: 68 cells
- ny_open: 28 cells

## Top strategies

| strategy | family | cells |
|---|---|---:|
| TF3_supertrend_short | dbb_trend | 34 |
| TF4_sar_long | dbb_trend | 31 |
| TF3_supertrend_long | dbb_trend | 25 |
| TF4_sar_short | dbb_trend | 23 |
| MR2_bb_reversion_long | reversal | 14 |
| MR2_bb_reversion_short | reversal | 9 |
| TF2_pullback_EMA20_long | dbb_trend | 5 |
| TF2_pullback_EMA20_short | dbb_trend | 3 |
| BR5_opening_range_breakout_short | direct | 2 |
| TF6_ma_ribbon_long | dbb_trend | 2 |
| BR3_inside_bar_short | direct | 2 |
| TF6_ma_ribbon_short | dbb_trend | 2 |
| BR2_vcb_long | direct | 1 |
| CP1_coil_breakout_short | direct | 1 |
| MO2_momentum_divergence_short | direct | 1 |

## To deploy live

1. Verify the parquet loads: `python3 -c "from scrooge_v3.strategies.routing_table import RoutingTable; rt = RoutingTable(); rt.load("data/routing_table_v3.parquet")"`
2. Update config: `strategies.routing_table_path = "data/routing_table_v3.parquet"`  (currently points to v2)
3. Restart `mr-scrooge-v3.service`
4. Confirm `[ROUTING_TABLE] loaded routing_table_v3.parquet — rows=N leaves=M` in journal
5. Existing routing_table_mode=hard will enforce the v3 cell list immediately

## Stage-2 follow-on

The shave_rule column is stored but NOT yet enforced by routing_table.py — it currently only attaches strategies. Stage 2 work: extend RoutingTable lookup to also return the per-cell rule, and add an entry-filter gate that evaluates the rule against current SymbolContext features. That work is independent of this ship.