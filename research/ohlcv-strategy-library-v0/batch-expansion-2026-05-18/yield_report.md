# Batch expansion yield report

Source: `research/ohlcv-strategy-library-v0/batch-expansion-2026-05-18/winners`
v9_observe baseline: `data/routing_table_v9_observe.parquet`

## 1. Yield by queue type

| queue | targets | strict | near_miss | dead | hit_rate | avg_n | avg_wr | avg_lb |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| session_sibling | 582 | 5 | 34 | 543 | 6.7% | 13.4 | 0.630 | 0.449 |
| boundary_thin | 1320 | 996 | 221 | 103 | 92.2% | 15.4 | 0.749 | 0.587 |
| live_gap | 200 | 0 | 0 | 200 | 0.0% | 0.0 | 0.000 | 0.000 |

**Most productive queue (by strict+near count)**: `boundary_thin` (1217 productive cells)

## 2. Direct-family breakdown

- **strict winners**: 214
- **near misses**:   50
- **dead**:          235

### Top pairs (productive only)

- `GBP_USD`: 17
- `EUR_NZD`: 17
- `EUR_GBP`: 17
- `EUR_AUD`: 17
- `USD_JPY`: 16
- `EUR_JPY`: 15
- `USD_CHF`: 13
- `EUR_USD`: 12
- `AUD_NZD`: 12
- `GBP_AUD`: 11

### Top regimes

- `C02`: 143
- `C01`: 121

### Top sessions

- `asia`: 254
- `london_open`: 3
- `asia_late`: 3
- `ny_mid`: 2
- `ny_close`: 1
- `off_hours`: 1

### Top cell strategies

- `charlie_compression_breakout`: 146
- `alpha_breakout_retest_v2`: 118

### Productive direct cells by queue type

- `boundary_thin`: 254
- `session_sibling`: 10

## 3. Ranked top-25 candidates

| rank | regime53 | pair | family | cell_strategy | direction | session_bucket | queue | outcome_tier | n_unique | wr_unique | wilson_lb | source_strategy | child_rule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C01 | NZD_JPY | direct | alpha_breakout_retest_v2 | long | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `ATR_ratio>=0.0795071 AND ADX14<=14.4275 AND hour_utc>=1.89` |
| 2 | C01 | USD_JPY | direct | charlie_compression_breakout | short | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `hour_utc>=4 AND hour_utc<=10.55 AND ATR_ratio<=0.0333133` |
| 3 | C01 | USD_JPY | direct | charlie_compression_breakout | short | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `hour_utc>=3.78 AND hour_utc<=10 AND ATR_ratio<=0.0333133` |
| 4 | C02 | GBP_AUD | direct | alpha_breakout_retest_v2 | short | asia | boundary_thin | strict_winner | 10 | 1.000 | 0.859 | boundary_widen | `RSI14<=30.8271 AND session_bucket==ny_open AND ATR_ratio<=0.…` |
| 5 | C01 | NZD_USD | dbb_trend | bravo_expansion_continuation | long | asia | boundary_thin | strict_winner | 14 | 1.000 | 0.895 | boundary_widen | `ATR_ratio>=0.0667639 AND BB_compress>=0.10618209` |
| 6 | C02 | GBP_USD | reversal | echo_box_fade_v2 | long | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `BB_compress>=0.049135 AND BB_compress<=0.0805629 AND volume_…` |
| 7 | C01 | CAD_JPY | reversal | echo_box_fade_v2 | short | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `BB_compress<=0.0358488 AND ATR_ratio>=0.0493784 AND ATR_rati…` |
| 8 | C02 | EUR_AUD | reversal | echo_box_fade_v2 | short | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `BB_compress<=0.0422981149999999 AND session_bucket==ny_mid A…` |
| 9 | C02 | CAD_JPY | reversal | bravo_failed_momentum | long | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `RSI14>=57.0209 AND RSI14<=61.7798 AND volume_ratio<=1.09394 …` |
| 10 | C02 | EUR_USD | direct | alpha_breakout_retest_v2 | long | asia | boundary_thin | strict_winner | 16 | 0.938 | 0.813 | boundary_widen | `hour_utc>=15.12 AND ATR_ratio>=0.100682` |
| 11 | C01 | USD_CAD | direct | charlie_compression_breakout | long | asia | boundary_thin | strict_winner | 16 | 0.938 | 0.813 | boundary_widen | `volume_ratio>=0.2967092099999999 AND volume_ratio<=0.45837 A…` |
| 12 | C02 | EUR_NZD | direct | charlie_compression_breakout | long | asia | boundary_thin | strict_winner | 16 | 0.938 | 0.813 | boundary_widen | `ADX14<=22.8286 AND BB_compress>=0.0610085385` |
| 13 | C02 | NZD_USD | dbb_trend | alpha_pullback_v2 | long | asia | boundary_thin | strict_winner | 13 | 1.000 | 0.888 | boundary_widen | `BB_compress>=0.128105 AND ADX14>=25.2606 AND ADX14<=31.08483…` |
| 14 | C02 | NZD_USD | dbb_trend | alpha_pullback_v2 | long | asia | boundary_thin | strict_winner | 13 | 1.000 | 0.888 | boundary_widen | `BB_compress>=0.12105922499999999 AND ADX14>=25.2606 AND ADX1…` |
| 15 | C02 | USD_MXN | dbb_trend | alpha_pullback_v2 | long | asia | boundary_thin | strict_winner | 13 | 1.000 | 0.888 | boundary_widen | `volume_ratio>=0.781696 AND volume_ratio<=1.01429 AND ATR_rat…` |
| 16 | C02 | EUR_GBP | reversal | echo_box_fade_v2 | long | asia | boundary_thin | strict_winner | 10 | 1.000 | 0.859 | boundary_widen | `ATR_ratio>=0.0576702315 AND BB_compress>=0.103965 AND BB_com…` |
| 17 | C02 | EUR_AUD | reversal | echo_box_fade_v2 | short | asia | boundary_thin | strict_winner | 10 | 1.000 | 0.859 | boundary_widen | `BB_compress<=0.040093 AND session_bucket==ny_mid AND ATR_rat…` |
| 18 | C02 | GBP_USD | reversal | echo_box_fade_v2 | long | asia | boundary_thin | strict_winner | 10 | 1.000 | 0.859 | boundary_widen | `BB_compress>=0.046432575 AND BB_compress<=0.0805629 AND volu…` |
| 19 | C02 | GBP_USD | reversal | echo_box_fade_v2 | long | asia | boundary_thin | strict_winner | 10 | 1.000 | 0.859 | boundary_widen | `BB_compress>=0.049135 AND BB_compress<=0.0805629 AND volume_…` |
| 20 | C01 | CAD_JPY | reversal | echo_box_fade_v2 | short | asia | boundary_thin | strict_winner | 10 | 1.000 | 0.859 | boundary_widen | `BB_compress<=0.037820484 AND ATR_ratio>=0.0493784 AND ATR_ra…` |
| 21 | C02 | EUR_GBP | reversal | echo_box_fade_v2 | long | asia | boundary_thin | strict_winner | 10 | 1.000 | 0.859 | boundary_widen | `ATR_ratio>=0.0610267 AND BB_compress>=0.103965 AND BB_compre…` |
| 22 | C02 | USD_JPY | dbb_trend | alpha_pullback_v2 | long | asia | boundary_thin | strict_winner | 12 | 1.000 | 0.880 | boundary_widen | `hour_utc>=9.45 AND ATR_ratio>=0.0771933 AND ATR_ratio<=0.093…` |
| 23 | C01 | USD_MXN | dbb_trend | charlie_pullback_continuation_v2 | short | asia | boundary_thin | strict_winner | 12 | 1.000 | 0.880 | boundary_widen | `volume_ratio>=1.41321 AND ATR_ratio>=0.014181993 AND ATR_rat…` |
| 24 | C02 | GBP_AUD | dbb_trend | bravo_expansion_continuation | short | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `ATR_ratio>=0.0809412 AND ATR_ratio<=0.0907879 AND hour_utc>=…` |
| 25 | C02 | GBP_AUD | dbb_trend | bravo_expansion_continuation | short | asia | boundary_thin | strict_winner | 11 | 1.000 | 0.870 | boundary_widen | `ATR_ratio>=0.0809412 AND ATR_ratio<=0.0907879 AND hour_utc>=…` |

## 4. Coverage impact (strict + near vs v9_observe)

### By family

| family | v9 cells | new productive | delta |
|---|---:|---:|---:|
| dbb_trend | 693 | 662 | +662 |
| direct | 511 | 264 | +264 |
| reversal | 602 | 330 | +330 |

### By pair

| pair | v9 cells | new productive | delta |
|---|---:|---:|---:|
| AUD_CAD | 63 | 45 | +45 |
| AUD_CHF | 63 | 32 | +32 |
| AUD_JPY | 70 | 45 | +45 |
| AUD_NZD | 63 | 31 | +31 |
| AUD_USD | 70 | 43 | +43 |
| CAD_JPY | 77 | 49 | +49 |
| CHF_JPY | 63 | 36 | +36 |
| EUR_AUD | 70 | 52 | +52 |
| EUR_CAD | 84 | 59 | +59 |
| EUR_CHF | 56 | 20 | +20 |
| EUR_GBP | 84 | 50 | +50 |
| EUR_JPY | 70 | 62 | +62 |
| EUR_NZD | 77 | 56 | +56 |
| EUR_USD | 70 | 57 | +57 |
| GBP_AUD | 56 | 47 | +47 |
| GBP_CAD | 56 | 49 | +49 |
| GBP_CHF | 63 | 29 | +29 |
| GBP_JPY | 63 | 28 | +28 |
| GBP_NZD | 70 | 62 | +62 |
| GBP_USD | 77 | 61 | +61 |
| NZD_JPY | 63 | 48 | +48 |
| NZD_USD | 70 | 56 | +56 |
| USD_CAD | 70 | 52 | +52 |
| USD_CHF | 84 | 59 | +59 |
| USD_JPY | 77 | 67 | +67 |
| USD_MXN | 77 | 61 | +61 |

### By regime

| regime | v9 cells | new productive | delta |
|---|---:|---:|---:|
| C01 | 868 | 522 | +522 |
| C02 | 938 | 734 | +734 |

### By direction

| direction | v9 cells | new productive | delta |
|---|---:|---:|---:|
| long | 882 | 649 | +649 |
| short | 924 | 607 | +607 |

### By session

| session | v9 cells | new productive | delta |
|---|---:|---:|---:|
| asia | 258 | 1221 | +1221 |
| asia_late | 258 | 4 | +4 |
| london_open | 258 | 8 | +8 |
| ny_close | 258 | 5 | +5 |
| ny_mid | 258 | 8 | +8 |
| ny_open | 258 | 7 | +7 |
| off_hours | 258 | 3 | +3 |

## 5. Session-sibling focus

- targets: 582
- strict winners: 5
- near misses: 34

### Productive transitions

| transition | count | avg_wr | avg_lb |
|---|---:|---:|---:|
| asia -> asia_late | 1 | 0.556 | 0.352 |
| asia -> london_open | 4 | 0.644 | 0.457 |
| asia -> ny_mid | 1 | 0.583 | 0.402 |
| asia -> off_hours | 1 | 0.556 | 0.352 |
| asia_late -> off_hours | 2 | 0.729 | 0.557 |
| london_open -> asia | 1 | 0.571 | 0.404 |
| london_open -> ny_close | 1 | 0.600 | 0.402 |
| london_open -> ny_mid | 1 | 0.625 | 0.403 |
| london_open -> ny_open | 2 | 0.597 | 0.431 |
| ny_close -> asia | 1 | 0.625 | 0.403 |
| ny_close -> london_open | 1 | 0.625 | 0.403 |
| ny_close -> ny_mid | 3 | 0.601 | 0.459 |
| ny_close -> ny_open | 1 | 0.588 | 0.434 |
| ny_mid -> asia | 1 | 0.615 | 0.439 |
| ny_mid -> asia_late | 1 | 0.615 | 0.439 |
| ny_mid -> london_open | 1 | 0.778 | 0.566 |
| ny_mid -> ny_close | 1 | 0.579 | 0.433 |
| ny_mid -> ny_open | 3 | 0.762 | 0.579 |
| ny_open -> asia_late | 1 | 0.625 | 0.403 |
| ny_open -> london_open | 1 | 0.556 | 0.352 |
| ny_open -> ny_close | 2 | 0.652 | 0.486 |
| ny_open -> ny_mid | 3 | 0.604 | 0.419 |
| off_hours -> asia | 1 | 0.571 | 0.404 |
| off_hours -> asia_late | 1 | 0.600 | 0.402 |
| off_hours -> london_open | 1 | 0.600 | 0.402 |
| off_hours -> ny_close | 1 | 0.643 | 0.472 |
| off_hours -> ny_open | 1 | 0.640 | 0.512 |

## 6. Boundary-thin focus

- targets: 1320
- strict winners: 996
- near misses: 221

### By widen_pct

| widen_pct | count | avg_wr | avg_lb |
|---|---:|---:|---:|
| 0.05 | 1140 | 0.758 | 0.594 |
| 0.1 | 47 | 0.618 | 0.473 |
| 0.15 | 30 | 0.632 | 0.488 |

### By widened factor (parsed from child_rule)

| factor | count | avg_wr | avg_lb |
|---|---:|---:|---:|
| ADX14 | 183 | 0.748 | 0.585 |
| ATR_ratio | 355 | 0.746 | 0.583 |
| BB_compress | 291 | 0.762 | 0.601 |
| RSI14 | 218 | 0.734 | 0.575 |
| volume_ratio | 164 | 0.757 | 0.592 |

## 7. Decision recommendation

- **Most productive queue → scale next**: `boundary_thin` (1217 productive)
- **Least productive queue → deprioritize**: `session_sibling` (39 productive)

- **Direct-family recovery**: 214 strict + 50 near = 264 new productive direct cells (v9 had 0 Pro+)

- **v10 build recommendation**: Build v10_trade from **strict winners only** — sample size already meaningful.