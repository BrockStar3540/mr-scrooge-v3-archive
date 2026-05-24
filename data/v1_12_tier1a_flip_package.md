# v1.12_TIER1A Flip Package
**Staged:** 2026-05-24 UTC  
**For flip:** Monday 2026-05-25, after asia + london_open windows are clean  
**Commit:** `00cc624df734943fd70da1a36a45d7d8e8dde33a`

---

## Flip Command

```bash
# On mr-scrooge-v3, after confirming Monday morning telemetry is clean:
cd ~/mr-scrooge-v3

# Edit config to point to TIER1A
# In openclaw.json or bot config, change routing_table path from:
#   routing_table_v10_fast_current_regime.parquet  (10 cells)
# to:
#   routing_table_v10_fast_v1_12_tier1a.parquet    (20 cells)

# Then hot-reload or restart the bot via systemctl
```

---

## Exact Keep / Add / Drop Slate

### KEEP (10 — from v1.11.5, not dropped)
| sub_regime | session | pair | strategy | dir | WR | WLB | tier |
|-----------|---------|------|----------|-----|-----|-----|------|
| C01 | asia | EUR_USD | RG1_range_bound_scalp_short | short | 0.388 | 0.373 | Elite |
| C01 | asia | EUR_USD | MR5_williams_extreme_short | short | 0.387 | 0.371 | Elite |
| C01 | asia | USD_JPY | BR2_vcb_long | long | 0.379 | 0.364 | Elite |
| C02 | asia | USD_JPY | SS1_asian_range_breakout_long | long | 0.444 | 0.405 | Pro |
| C02 | asia | EUR_USD | MTB_S3W0M35P20_long | long | 0.390 | 0.367 | Elite |
| MTB_C01_3 | asia | EUR_GBP | MTB1_pitchfork_long_strict | long | 0.433 | 0.396 | Pro |
| C02 | london_open | USD_JPY | MR2_bb_reversion_long | long | 0.389 | 0.367 | Elite |
| C02 | london_open | AUD_JPY | MTB_S4W30M35P20_long | long | 0.438 | 0.395 | Pro |
| MTB_C02_6 | london_open | EUR_GBP | MTB1_pitchfork_short_strict | short | 0.424 | 0.395 | Pro |
| MTB_C02_9 | london_open | EUR_JPY | MTB1_pitchfork_long_strict | long | 0.465 | 0.424 | Pro |

### DROP (10 — removed from v1.11.5 candidate bank)
| sub_regime | session | pair | strategy | dir | WLB | Reason |
|-----------|---------|------|----------|-----|-----|--------|
| C01 | asia | EUR_CHF | MTB1_pitchfork_short_strict | short | 0.337 | Weakest MTB |
| MTB_C01_6 | ny_mid | USD_MXN | MTB1_pitchfork_long_strict | long | 0.339 | 0% recent WR |
| C01 | asia | AUD_JPY | RG2_range_support_bounce_long | long | 0.341 | Weak 6m |
| C02 | asia | EUR_CHF | MTB_S3W0M30P30_short | short | 0.342 | WR 36.3% |
| C01 | asia | EUR_USD | CP3_vol_coil_fade_short | short | 0.347 | Thin 6m |
| C02 | asia | EUR_USD | MTB_S2W0M30P20_short | short | 0.349 | WR 36.9% |
| C02 | london_open | AUD_JPY | MTB2_pitchfork_long_with_wick | long | 0.355 | Thin variant |
| C01 | london_open | USD_JPY | MTB_S2W0M30P20_long | long | 0.359 | Marginal |
| C01 | asia | EUR_GBP | MTB1_pitchfork_short_strict | short | 0.362 | Thin n=412 |
| C01 | asia | EUR_JPY | SS1_asian_range_breakout_long | long | 0.363 | Low n=155 |

### ADD (10 — dbb_trend from corrected 6m rebuild)
| sub_regime | session | pair | strategy | dir | 6m WR | 6m WLB | shave_rule |
|-----------|---------|------|----------|-----|-------|--------|-----------|
| C02 | asia | EUR_USD | MR2_bb_reversion_long | long | 0.571 | 0.451 | RSI14≤59.6 |
| C02 | asia | USD_CHF | MR2_bb_reversion_short | short | 0.436 | 0.339 | ADX14≥37.9 |
| C02 | asia | AUD_USD | MR2_bb_reversion_long | long | 0.419 | 0.327 | vol_ratio≥1.08 |
| C02 | asia | GBP_USD | MR2_bb_reversion_long | long | 0.478 | 0.351 | vol_ratio≥0.94 |
| C02 | asia | USD_JPY | MR2_bb_reversion_long | long | 0.480 | 0.357 | ATR_ratio≥0.06 |
| C01 | london_open | USD_CHF | MR2_bb_reversion_long | long | 0.452 | 0.358 | RSI14≤60.6 |
| C02 | london_open | AUD_JPY | MR2_bb_reversion_long | long | 0.407 | 0.295 | (none) |
| C02 | london_open | GBP_USD | MR2_bb_reversion_long | long | 0.412 | 0.310 | (none) |
| C01 | ny_mid | EUR_USD | MR2_bb_reversion_short | short | 0.500 | 0.294 | (none) |
| C01 | ny_mid | AUD_USD | MR2_bb_reversion_short | short | 0.400 | 0.230 | (none) |

---

## Routing Table Stats

| Metric | v1.11.5 (live) | v1.12_TIER1A |
|--------|---------------|--------------|
| Total rows | 20 | 20 |
| Unique leaves | varies | 16 |
| asia cells | 13 | 11 |
| london_open cells | 6 | 7 |
| ny_mid cells | 1 | 2 |
| ny_open cells | 0 | 0 |
| Families | MTB(12), direct(4), reversal(4) | MTB(5), dbb_trend(10), direct(2), reversal(3) |

## Session Coverage Delta

```
             v1.11.5    v1.12_TIER1A   delta
asia:            13           11          -2  (dropped weak MTB)
london_open:      6            7          +1  (USD_CHF added)
ny_mid:           1            2          +1  (EUR_USD + AUD_USD)
ny_open:          0            0           0
ny_close:         0            0           0
```

## Commit Hash

`00cc624df734943fd70da1a36a45d7d8e8dde33a`

## Boot Confirmation

```
Rows loaded: 20
Unique leaves: 16
C02|EUR_USD|asia|long: 2 decisions [MTB_S3W0M35P20_long + MR2_bb_reversion_long]
C01|USD_JPY|asia|long: 1 decision  [BR2_vcb_long]
BOOT TEST PASS
```

---

## Monday Flip Procedure

1. Wait for asia window (00:00–06:00 UTC) — confirm v1.11.5 fires normally
2. Wait for london_open (06:00–09:00 UTC) — confirm no anomalies
3. If clean: update config routing_table path to `v1_12_tier1a`
4. Hot-reload or restart bot
5. Monitor ny_mid (13:00+ UTC) — first session with new dbb_trend cells

DO NOT FLIP if:
- Any of the 10 keep cells misbehave in asia
- Bot shows silence across full london_open window
- Any anomaly in telemetry log

---

## What v1.12_TIER1A does NOT include

- The 24 textbook ADD cells (TF2/BR2/CP3/MR5) — no live probes yet
- MTB3 extension cells — TIER1B work in progress
- ny_open cells — none cleared corrected 6m bar
- Darvas — not in scalper corpus
