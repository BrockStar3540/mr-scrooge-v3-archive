# Hybrid class-island shaver — summary

**Generated:** 2026-05-15T20:13:25.900965+00:00
**Engine:** band grammar + beam(top-30) up to depth-4 + per-parent factor priors + MAX_PARENT_FRAC=0.40

## Counts per (target, window)

| target | window | islands | false-friends |
|---|---|---:|---:|
| winner | 6yr | 58,938 | 5,712 |
| loser | 6yr | 674,212 | 5,698 |
| winner | 6mo | 37,850 | 5,650 |
| loser | 6mo | 477,640 | 5,374 |

## Cell overlap winners vs losers

- **6yr**: both = 705 | winner-only = 0 | loser-only = 9
- **6mo**: both = 601 | winner-only = 3 | loser-only = 110

## Cell persistence 6yr vs 6mo

- **winner**: durable (both windows) = 599 | only 6yr = 106 | only 6mo = 5
- **loser**: durable (both windows) = 711 | only 6yr = 3 | only 6mo = 0

## Top 15 per pass (by target rate then count)

### winner / 6yr

| strategy_id | pair | direction | technical_regime_53 | parent_n | parent_wr | n | wins | losses | wr | mean_R | hold_wins | hold_losses | depth | rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alpha_pullback_v2 | NZD_JPY | long | C01 | 846 | 0.450355 | 26 | 26 | 0 | 1 | 1.5 | 4 | 0 | 3 | ATR_ratio>=0.0651411 AND BB_compress>=0.129332 AND volume_ratio>=0.497607 |
| alpha_pullback_v2 | NZD_JPY | long | C01 | 846 | 0.450355 | 26 | 26 | 0 | 1 | 1.5 | 4 | 0 | 4 | nan AND ATR_ratio>=0.0651411 AND BB_compress>=0.129332 AND volume_ratio>=0.497607 |
| alpha_pullback_v2 | NZD_JPY | long | C01 | 846 | 0.450355 | 24 | 24 | 0 | 1 | 1.5 | 2 | 0 | 3 | ATR_ratio>=0.0651411 AND BB_compress>=0.129332 AND volume_ratio>=0.540389 |
| alpha_pullback_v2 | NZD_JPY | long | C01 | 846 | 0.450355 | 24 | 24 | 0 | 1 | 1.5 | 6 | 0 | 3 | ATR_ratio>=0.0736849 AND BB_compress>=0.126516 AND volume_ratio>=0.497607 |
| alpha_pullback_v2 | NZD_JPY | long | C01 | 846 | 0.450355 | 24 | 24 | 0 | 1 | 1.5 | 2 | 0 | 4 | nan AND ATR_ratio>=0.0651411 AND BB_compress>=0.129332 AND volume_ratio>=0.540389 |
| alpha_pullback_v2 | NZD_JPY | long | C01 | 846 | 0.450355 | 24 | 24 | 0 | 1 | 1.5 | 6 | 0 | 4 | nan AND ATR_ratio>=0.0736849 AND BB_compress>=0.126516 AND volume_ratio>=0.497607 |
| bravo_failed_momentum | CAD_JPY | long | C02 | 432 | 0.37963 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 3 | RSI14>=57.0209 AND RSI14<=61.7798 AND volume_ratio<=1.09394 |
| bravo_failed_momentum | CAD_JPY | long | C02 | 432 | 0.37963 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 4 | nan AND RSI14>=57.0209 AND RSI14<=61.7798 AND volume_ratio<=1.09394 |
| echo_box_fade_v2 | EUR_AUD | short | C02 | 1922 | 0.399063 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 3 | BB_compress<=0.040093 AND session_bucket==ny_mid AND ATR_ratio>=0.0536091 |
| echo_box_fade_v2 | EUR_AUD | short | C02 | 1922 | 0.399063 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 4 | nan AND BB_compress<=0.040093 AND session_bucket==ny_mid AND ATR_ratio>=0.0536091 |
| alpha_pullback_v2 | USD_JPY | long | C02 | 982 | 0.428717 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 5 | hour_utc>=10 AND hour_utc<=15 AND ATR_ratio>=0.0771933 AND ATR_ratio<=0.093448 AND ADX14>=21.9093 |
| alpha_pullback_v2 | USD_JPY | long | C02 | 982 | 0.428717 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 5 | hour_utc>=10 AND hour_utc<=15 AND ATR_ratio>=0.0771933 AND ATR_ratio<=0.093448 AND ADX14>=22.0992 |
| alpha_pullback_v2 | USD_JPY | long | C02 | 982 | 0.428717 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 6 | nan AND hour_utc>=10 AND hour_utc<=15 AND ATR_ratio>=0.0771933 AND ATR_ratio<=0.093448 AND ADX14>=21.9093 |
| alpha_pullback_v2 | USD_JPY | long | C02 | 982 | 0.428717 | 22 | 22 | 0 | 1 | 1.5 | 4 | 0 | 6 | nan AND hour_utc>=10 AND hour_utc<=15 AND ATR_ratio>=0.0771933 AND ATR_ratio<=0.093448 AND ADX14>=22.0992 |
| alpha_pullback_v2 | NZD_JPY | long | C01 | 846 | 0.450355 | 22 | 22 | 0 | 1 | 1.5 | 2 | 0 | 4 | volume_ratio>=1.45215 AND volume_ratio<=1.82442 AND ATR_ratio>=0.0592663 AND ATR_ratio<=0.0759931 |

### loser / 6yr

| strategy_id | pair | direction | technical_regime_53 | parent_n | parent_wr | n | wins | losses | loss_rate | mean_R | hold_wins | hold_losses | depth | rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alpha_breakout_retest_v2 | AUD_CHF | short | C01 | 516 | 0.350775 | 46 | 0 | 46 | 1 | -1 | 0 | 6 | 2 | BB_compress>=0.132551 AND volume_ratio>=0.396665 |
| alpha_breakout_retest_v2 | AUD_CHF | short | C01 | 516 | 0.350775 | 46 | 0 | 46 | 1 | -1 | 0 | 6 | 3 | nan AND BB_compress>=0.132551 AND volume_ratio>=0.396665 |
| alpha_extended_fade_v2 | EUR_JPY | long | C02 | 518 | 0.339768 | 46 | 0 | 46 | 1 | -1 | 0 | 2 | 2 | ATR_ratio<=0.0508764 AND BB_compress<=0.107558 |
| alpha_extended_fade_v2 | EUR_JPY | long | C02 | 518 | 0.339768 | 46 | 0 | 46 | 1 | -1 | 0 | 2 | 3 | nan AND ATR_ratio<=0.0508764 AND BB_compress<=0.107558 |
| charlie_pullback_continuation_v2 | USD_CAD | short | C01 | 884 | 0.290724 | 46 | 0 | 46 | 1 | -1 | 0 | 0 | 2 | volume_ratio>=1.61944 AND ATR_ratio<=0.0441437 |
| charlie_pullback_continuation_v2 | USD_CAD | short | C01 | 884 | 0.290724 | 46 | 0 | 46 | 1 | -1 | 0 | 0 | 3 | nan AND volume_ratio>=1.61944 AND ATR_ratio<=0.0441437 |
| alpha_breakout_retest_v2 | AUD_CHF | short | C01 | 516 | 0.350775 | 44 | 0 | 44 | 1 | -1 | 0 | 6 | 2 | BB_compress>=0.132551 AND volume_ratio>=0.425636 |
| alpha_breakout_retest_v2 | AUD_CHF | short | C01 | 516 | 0.350775 | 44 | 0 | 44 | 1 | -1 | 0 | 6 | 3 | nan AND BB_compress>=0.132551 AND volume_ratio>=0.425636 |
| alpha_extended_fade_v2 | EUR_JPY | long | C02 | 518 | 0.339768 | 44 | 0 | 44 | 1 | -1 | 0 | 2 | 2 | ATR_ratio<=0.0508764 AND BB_compress<=0.100654 |
| alpha_extended_fade_v2 | EUR_JPY | long | C02 | 518 | 0.339768 | 44 | 0 | 44 | 1 | -1 | 0 | 2 | 2 | ATR_ratio<=0.0508764 AND volume_ratio>=0.731702 |
| alpha_extended_fade_v2 | EUR_JPY | long | C02 | 518 | 0.339768 | 44 | 0 | 44 | 1 | -1 | 0 | 2 | 3 | nan AND ATR_ratio<=0.0508764 AND BB_compress<=0.100654 |
| alpha_extended_fade_v2 | EUR_JPY | long | C02 | 518 | 0.339768 | 44 | 0 | 44 | 1 | -1 | 0 | 2 | 3 | nan AND ATR_ratio<=0.0508764 AND volume_ratio>=0.731702 |
| charlie_compression_breakout | CHF_JPY | long | C02 | 484 | 0.400826 | 42 | 0 | 42 | 1 | -1 | 0 | 10 | 3 | BB_compress>=0.0313547 AND BB_compress<=0.0431994 AND ADX14>=30.6812 |
| charlie_compression_breakout | CHF_JPY | long | C02 | 484 | 0.400826 | 42 | 0 | 42 | 1 | -1 | 0 | 10 | 4 | nan AND BB_compress>=0.0313547 AND BB_compress<=0.0431994 AND ADX14>=30.6812 |
| charlie_compression_breakout | GBP_JPY | short | C01 | 626 | 0.357827 | 42 | 0 | 42 | 1 | -1 | 0 | 6 | 3 | BB_compress>=0.0406094 AND BB_compress<=0.0488324 AND volume_ratio>=0.778771 |

### winner / 6mo

| strategy_id | pair | direction | technical_regime_53 | parent_n | parent_wr | n | wins | losses | wr | mean_R | hold_wins | hold_losses | depth | rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 28 | 28 | 0 | 1 | 1.5 | 20 | 0 | 2 | ADX14<=13.7726 AND ATR_ratio>=0.0718448 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 28 | 28 | 0 | 1 | 1.5 | 20 | 0 | 3 | nan AND ADX14<=13.7726 AND ATR_ratio>=0.0718448 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 26 | 26 | 0 | 1 | 1.5 | 18 | 0 | 3 | ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress>=0.0503588 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 26 | 26 | 0 | 1 | 1.5 | 20 | 0 | 3 | ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress<=0.0837639 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 26 | 26 | 0 | 1 | 1.5 | 18 | 0 | 4 | nan AND ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress>=0.0503588 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 26 | 26 | 0 | 1 | 1.5 | 20 | 0 | 4 | nan AND ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress<=0.0837639 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 24 | 24 | 0 | 1 | 1.5 | 16 | 0 | 3 | ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress>=0.0516998 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 24 | 24 | 0 | 1 | 1.5 | 18 | 0 | 3 | ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress<=0.0760574 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 24 | 24 | 0 | 1 | 1.5 | 16 | 0 | 4 | nan AND ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress>=0.0516998 |
| alpha_pullback_v2 | EUR_AUD | short | C01 | 270 | 0.466667 | 24 | 24 | 0 | 1 | 1.5 | 18 | 0 | 4 | nan AND ADX14<=13.7726 AND ATR_ratio>=0.0718448 AND BB_compress<=0.0760574 |
| charlie_compression_breakout | GBP_NZD | long | C01 | 210 | 0.485714 | 22 | 22 | 0 | 1 | 1.5 | 14 | 0 | 2 | BB_compress>=0.0553353 AND ADX14<=17.3579 |
| charlie_compression_breakout | GBP_NZD | long | C01 | 210 | 0.485714 | 22 | 22 | 0 | 1 | 1.5 | 14 | 0 | 3 | nan AND BB_compress>=0.0553353 AND ADX14<=17.3579 |
| charlie_compression_breakout | EUR_NZD | short | C01 | 296 | 0.418919 | 22 | 22 | 0 | 1 | 1.5 | 10 | 0 | 2 | ADX14<=11.6573 AND session_bucket==ny_close |
| charlie_compression_breakout | EUR_NZD | short | C01 | 296 | 0.418919 | 22 | 22 | 0 | 1 | 1.5 | 10 | 0 | 3 | nan AND ADX14<=11.6573 AND session_bucket==ny_close |
| bravo_expansion_continuation | USD_JPY | long | C02 | 230 | 0.530435 | 22 | 22 | 0 | 1 | 1.5 | 10 | 0 | 3 | BB_compress>=0.10057 AND BB_compress<=0.137552 AND volume_ratio>=0.827276 |

### loser / 6mo

| strategy_id | pair | direction | technical_regime_53 | parent_n | parent_wr | n | wins | losses | loss_rate | mean_R | hold_wins | hold_losses | depth | rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 58 | 0 | 58 | 1 | -1 | 0 | 30 | 2 | ADX14<=30.2527 AND hour_utc<=16 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 58 | 0 | 58 | 1 | -1 | 0 | 30 | 3 | nan AND ADX14<=30.2527 AND hour_utc<=16 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 54 | 0 | 54 | 1 | -1 | 0 | 26 | 2 | ADX14<=30.2527 AND hour_utc<=15 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 54 | 0 | 54 | 1 | -1 | 0 | 26 | 3 | nan AND ADX14<=30.2527 AND hour_utc<=15 |
| charlie_pullback_continuation_v2 | EUR_USD | long | C01 | 282 | 0.241135 | 52 | 0 | 52 | 1 | -1 | 0 | 32 | 2 | hour_utc>=20 AND hour_utc<=22 |
| charlie_pullback_continuation_v2 | EUR_USD | long | C01 | 282 | 0.241135 | 52 | 0 | 52 | 1 | -1 | 0 | 32 | 3 | nan AND hour_utc>=20 AND hour_utc<=22 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 52 | 0 | 52 | 1 | -1 | 0 | 28 | 3 | ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio<=1.51628 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 52 | 0 | 52 | 1 | -1 | 0 | 28 | 4 | nan AND ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio<=1.51628 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 52 | 0 | 52 | 1 | -1 | 0 | 26 | 3 | ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio>=0.70789 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 52 | 0 | 52 | 1 | -1 | 0 | 26 | 4 | nan AND ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio>=0.70789 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 50 | 0 | 50 | 1 | -1 | 0 | 26 | 3 | ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio<=1.44843 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 50 | 0 | 50 | 1 | -1 | 0 | 26 | 4 | nan AND ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio<=1.44843 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 50 | 0 | 50 | 1 | -1 | 0 | 24 | 3 | ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio>=0.763919 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 50 | 0 | 50 | 1 | -1 | 0 | 24 | 4 | nan AND ADX14<=30.2527 AND hour_utc<=16 AND volume_ratio>=0.763919 |
| alpha_extended_fade_v2 | GBP_AUD | long | C02 | 198 | 0.262626 | 48 | 0 | 48 | 1 | -1 | 0 | 24 | 3 | ADX14<=30.2527 AND hour_utc<=15 AND volume_ratio<=1.57135 |
