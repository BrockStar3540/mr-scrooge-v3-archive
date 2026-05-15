# Hybrid class-island shaver — summary (filtered)

**Generated:** 2026-05-15T18:11:12.991961+00:00
**Engine:** band-grammar + beam(top-30) up to depth-4 + per-parent factor priors (test3) + MAX_PARENT_FRAC=0.40
**Loser-side post-filter:** loss_rate > parent_loss_rate + 0.15  AND  top-1 per parent cell

## Counts

| target | window | islands | false-friends |
|---|---|---:|---:|
| winner | 6yr | 438 | 2,344 |
| winner | 6mo | 13 | 1,964 |
| loser | 6yr | 150 | 446 |
| loser | 6mo | 113 | 192 |

## Cell overlap winner vs loser

- **6yr**: both = 52 | winner-only = 8 | loser-only = 98
- **6mo**: both = 3 | winner-only = 1 | loser-only = 110

## Persistence 6yr vs 6mo

- **winner**: durable=1 | only_6yr=59 | only_6mo=3
- **loser**: durable=100 | only_6yr=50 | only_6mo=13

## Top 10 winner islands per window

### 6yr

| strategy_id | pair | direction | technical_regime_53 | parent_n | n | wins | losses | wr | mean_R | hold_wins | hold_losses | depth | rule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TF6_ma_ribbon_long | AUD_USD | long | C02 | 1699 | 11 | 11 | 0 | 1.0 | 1.8943278943278947 | 4 | 0 | 4 | RSI14>73.24 AND BB_compress>0.1742 AND BB_compress<=0.200982 AND RSI14<=74.6344 |
| TF6_ma_ribbon_short | GBP_CAD | short | C02 | 768 | 11 | 11 | 0 | 1.0 | 1.743720218936587 | 1 | 0 | 7 | RSI14<=31.24 AND ATR_ratio>0.1096 AND RSI14>=23.3082 AND RSI14<=28.5995 AND volume_ratio>=0.934359 AND volume_ratio<=1.07855 AND session_bucket==london |
| TF6_ma_ribbon_short | GBP_CAD | short | C02 | 768 | 11 | 11 | 0 | 1.0 | 1.617437471139894 | 1 | 0 | 7 | RSI14<=31.24 AND ATR_ratio>0.1096 AND volume_ratio>=0.895399 AND volume_ratio<=1.10017 AND RSI14>=25.4838 AND RSI14<=28.3815 AND session_bucket==london |
| TF3_supertrend_long | EUR_GBP | long | C02 | 3076 | 10 | 10 | 0 | 1.0 | 1.523070182255974 | 3 | 0 | 5 | price_pos>=0.721748 AND price_pos<=0.792889 AND ATR_ratio>=0.0999225 AND ATR_ratio<=0.118201 AND BB_compress>=0.137142 |
| TF3_supertrend_long | GBP_CAD | long | C01 | 3210 | 10 | 10 | 0 | 1.0 | 1.8168574279449836 | 2 | 0 | 7 | ATR_ratio>0.06152 AND ATR_ratio>0.08849 AND BB_compress>=0.0822818 AND BB_compress<=0.114646 AND ATR_ratio<=0.0933625 AND volume_ratio>=0.820518 AND session_bucket==london |
| TF6_ma_ribbon_short | EUR_CAD | short | C02 | 508 | 10 | 10 | 0 | 1.0 | 1.014186468887195 | 1 | 0 | 4 | BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=23.1409 AND session_bucket==london |
| TF6_ma_ribbon_long | USD_JPY | long | C02 | 1018 | 10 | 10 | 0 | 1.0 | 1.0883125739171875 | 0 | 0 | 5 | volume_ratio>1.414 AND RSI14>72.08 AND RSI14>=85.1045 AND BB_compress>=0.150814 AND session_bucket==london |
| TF6_ma_ribbon_short | EUR_CAD | short | C02 | 508 | 16 | 15 | 1 | 0.9375 | 0.742658158432111 | 1 | 0 | 4 | BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=17.6477 AND session_bucket==london |
| TF6_ma_ribbon_short | EUR_CAD | short | C02 | 508 | 16 | 15 | 1 | 0.9375 | 0.742658158432111 | 1 | 0 | 4 | BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=16.8873 AND session_bucket==london |
| TF6_ma_ribbon_short | EUR_CAD | short | C02 | 508 | 15 | 14 | 1 | 0.9333333333333332 | 0.7897168634484261 | 1 | 0 | 4 | BB_compress>=0.327614 AND price_pos<=0.0970971 AND RSI14>=18.9398 AND session_bucket==london |

### 6mo

| strategy_id | pair | direction | technical_regime_53 | parent_n | n | wins | losses | wr | mean_R | hold_wins | hold_losses | depth | rule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TF4_sar_long | AUD_USD | long | C02 | 600 | 13 | 11 | 2 | 0.8461538461538461 | 1.3854293854293909 | 11 | 2 | 6 | BB_compress>=0.152363 AND BB_compress<=0.224116 AND price_pos>=0.305177 AND price_pos<=0.784999 AND ATR_ratio<=0.10992 AND session_bucket==london |
| TF4_sar_long | AUD_USD | long | C02 | 600 | 14 | 11 | 3 | 0.7857142857142857 | 1.2150415721844343 | 11 | 3 | 6 | BB_compress>=0.152363 AND BB_compress<=0.224116 AND price_pos>=0.305177 AND price_pos<=0.784999 AND ATR_ratio<=0.113244 AND session_bucket==london |
| TF3_supertrend_long | GBP_USD | long | C02 | 265 | 14 | 11 | 3 | 0.7857142857142857 | 1.0294186184165497 | 11 | 3 | 2 | ATR_ratio>=0.0804165 AND ADX14<=22.1303 |
| TF3_supertrend_long | GBP_USD | long | C02 | 265 | 14 | 11 | 3 | 0.7857142857142857 | 1.0294186184165497 | 11 | 3 | 2 | ADX14<=22.0909 AND ATR_ratio>=0.080747 |
| TF3_supertrend_long | GBP_USD | long | C02 | 265 | 14 | 11 | 3 | 0.7857142857142857 | 0.9632430555520374 | 11 | 3 | 2 | BB_compress>=0.0903144 AND ADX14<=22.5405 |
| TF3_supertrend_long | NZD_JPY | long | C02 | 227 | 13 | 10 | 3 | 0.7692307692307693 | 1.1554298000913668 | 10 | 3 | 2 | ATR_ratio>=0.0798848 AND hour_utc<=5 |
| TF3_supertrend_long | GBP_USD | long | C02 | 265 | 13 | 10 | 3 | 0.7692307692307693 | 1.1035636426922757 | 10 | 3 | 4 | ATR_ratio>0.05492 AND BB_compress>0.05152 AND ATR_ratio>=0.080246 AND ADX14<=22.0527 |
| TF4_sar_long | USD_CHF | long | C02 | 671 | 17 | 13 | 4 | 0.7647058823529411 | 1.1225727494855908 | 13 | 4 | 5 | ATR_ratio>=0.0949268 AND ATR_ratio<=0.120088 AND hour_utc>=12.2 AND hour_utc<=14 AND BB_compress<=0.244665 |
| TF4_sar_long | USD_CHF | long | C02 | 671 | 17 | 13 | 4 | 0.7647058823529411 | 1.1225727494855908 | 13 | 4 | 6 | ATR_ratio>=0.0949268 AND ATR_ratio<=0.120088 AND hour_utc>=12.2 AND hour_utc<=14 AND BB_compress<=0.244665 AND session_bucket==london |
| TF4_sar_long | USD_CHF | long | C02 | 671 | 16 | 12 | 4 | 0.75 | 1.0677335463284403 | 12 | 4 | 5 | ATR_ratio>=0.0949268 AND ATR_ratio<=0.120088 AND hour_utc>=12.2 AND hour_utc<=14 AND BB_compress<=0.225925 |

## Top 10 loser islands per window (top1-per-parent, purest)

### 6yr

| strategy_id | pair | direction | technical_regime_53 | parent_n | parent_wr | n | wins | losses | loss_rate | hold_wins | hold_losses | depth | rule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TF4_sar_long | EUR_JPY | long | C02 | 8468 | 0.1523382144544166 | 126 | 0 | 126 | 1.0 | 0 | 16 | 4 | hour_utc>=16 AND hour_utc<=19 AND ATR_ratio<=0.0353684 AND BB_compress<=0.0319272 |
| TF3_supertrend_short | AUD_NZD | short | C02 | 2909 | 0.1540048126503953 | 123 | 0 | 123 | 1.0 | 0 | 40 | 3 | session_bucket==ny AND volume_ratio<=0.207825 AND ATR_ratio<=0.0903492 |
| TF4_sar_long | GBP_USD | long | C02 | 8524 | 0.1587282965743782 | 118 | 0 | 118 | 1.0 | 0 | 17 | 3 | BB_compress<=0.0398198 AND ATR_ratio<=0.0274519 AND hour_utc<=21 |
| TF3_supertrend_short | GBP_NZD | short | C01 | 3296 | 0.1516990291262135 | 99 | 0 | 99 | 1.0 | 0 | 26 | 4 | BB_compress<=0.0317863 AND hour_utc>=19 AND hour_utc<=21 AND ATR_ratio<=0.0529595 |
| TF3_supertrend_short | EUR_CHF | short | C01 | 3459 | 0.1575599884359641 | 93 | 0 | 93 | 1.0 | 0 | 18 | 4 | BB_compress>=0.0218568 AND BB_compress<=0.0282137 AND session_bucket==ny AND ATR_ratio<=0.0512037 |
| TF3_supertrend_long | USD_MXN | long | C02 | 4036 | 0.1595639246778989 | 86 | 0 | 86 | 1.0 | 0 | 12 | 3 | hour_utc>=19.5 AND ATR_ratio<=0.0366651 AND BB_compress>=0.0179318 |
| TF4_sar_short | USD_MXN | short | C02 | 8818 | 0.1538897709231118 | 80 | 0 | 80 | 1.0 | 0 | 18 | 3 | price_pos>=0.746951 AND ATR_ratio<=0.0412816 AND BB_compress>=0.0203103 |
| TF3_supertrend_short | EUR_CAD | short | C01 | 3144 | 0.1822519083969465 | 78 | 0 | 78 | 1.0 | 0 | 10 | 4 | ATR_ratio>=0.0304338 AND ATR_ratio<=0.0358432 AND BB_compress>=0.0223176 AND BB_compress<=0.0290644 |
| TF3_supertrend_long | EUR_GBP | long | C01 | 3188 | 0.1577791718946047 | 76 | 0 | 76 | 1.0 | 0 | 17 | 4 | session_bucket==ny AND ATR_ratio>=0.0326429 AND ATR_ratio<=0.0372083 AND ADX14<=18.4856 |
| TF4_sar_short | EUR_USD | short | C02 | 8473 | 0.1537826035642629 | 76 | 0 | 76 | 1.0 | 0 | 13 | 4 | ATR_ratio<=0.0391424 AND price_pos>=0.705752 AND price_pos<=0.783818 AND BB_compress>=0.0166824 |

### 6mo

| strategy_id | pair | direction | technical_regime_53 | parent_n | parent_wr | n | wins | losses | loss_rate | hold_wins | hold_losses | depth | rule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TF4_sar_long | USD_JPY | long | C02 | 625 | 0.1584 | 64 | 0 | 64 | 1.0 | 0 | 64 | 3 | hour_utc>=20 AND hour_utc<=21 AND ATR_ratio<=0.0535082 |
| MR2_bb_reversion_long | AUD_JPY | long | C01 | 389 | 0.1542416452442159 | 63 | 0 | 63 | 1.0 | 0 | 63 | 2 | BB_compress<=0.025276 AND hour_utc<=21 |
| TF4_sar_long | GBP_USD | long | C02 | 626 | 0.1517571884984025 | 55 | 0 | 55 | 1.0 | 0 | 55 | 3 | BB_compress>=0.028029 AND BB_compress<=0.0408643 AND ATR_ratio<=0.0714201 |
| TF3_supertrend_long | EUR_NZD | long | C01 | 288 | 0.1666666666666666 | 51 | 0 | 51 | 1.0 | 0 | 51 | 1 | hour_utc>=20 |
| TF3_supertrend_short | GBP_JPY | short | C02 | 224 | 0.1517857142857142 | 51 | 0 | 51 | 1.0 | 0 | 51 | 3 | volume_ratio>=0.971989 AND volume_ratio<=1.42991 AND ATR_ratio<=0.0679838 |
| MR2_bb_reversion_long | GBP_JPY | long | C01 | 375 | 0.1626666666666666 | 48 | 0 | 48 | 1.0 | 0 | 48 | 2 | hour_utc>=19.9 AND BB_compress<=0.0588399 |
| TF3_supertrend_short | NZD_JPY | short | C02 | 218 | 0.1605504587155963 | 43 | 0 | 43 | 1.0 | 0 | 43 | 2 | hour_utc>=18 AND hour_utc<=22 |
| TF3_supertrend_long | AUD_CAD | long | C01 | 250 | 0.156 | 43 | 0 | 43 | 1.0 | 0 | 43 | 2 | hour_utc>=17 AND BB_compress<=0.0603071 |
| TF3_supertrend_short | CHF_JPY | short | C01 | 256 | 0.16015625 | 43 | 0 | 43 | 1.0 | 0 | 43 | 2 | BB_compress<=0.0304103 AND hour_utc>=6.79 |
| TF4_sar_short | EUR_USD | short | C01 | 440 | 0.1522727272727272 | 43 | 0 | 43 | 1.0 | 0 | 43 | 3 | hour_utc>=19 AND hour_utc<=21 AND BB_compress>=0.0281022 |
