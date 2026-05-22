# Scalper Relabeling Summary (6 pip SL / 12 pip TP)

Generated 2026-05-21 (streaming pass over 26 per-pair trade_log files).

**Total events after sanity filters**: 14,928,094

## Outcome distribution under 6/12 first-touch

| outcome | count | pct |
|---|---:|---:|
| **clean_win** (touched +12 before -6) | 982,105 | 6.6% |
| **clean_loss** (touched -6 before +12) | 3,617,892 | 24.2% |
| ambiguous (both touched, order unknown) | 10,238,860 | 68.6% |
| neither (trade closed inside the band) | 89,237 | 0.6% |

## Win-rate bounds

- **Clean-only WR**: 0.214
- **Worst-case WR**: 0.066
- **Best-case WR**: 0.752
- **Old `is_win` WR**: 0.067

**Scalper resolution lifts clean WR from 0.067 to 0.214 (+14.7 pts)**

## Top signatures by n (clean-only) — sneak peek

| regime | pair | dir | family | n | wins | WR |
|---|---|---|---|---:|---:|---:|
| C02 | USD_MXN | short | other | 104128 | 27279 | 0.262 |
| C02 | USD_MXN | long | other | 80178 | 22016 | 0.275 |
| C01 | USD_MXN | long | other | 79907 | 21285 | 0.266 |
| C01 | USD_MXN | short | other | 76366 | 20619 | 0.270 |
| C01 | EUR_GBP | long | other | 71513 | 14824 | 0.207 |
| C02 | EUR_GBP | short | other | 70504 | 17737 | 0.252 |
| C01 | EUR_CHF | long | other | 69666 | 14112 | 0.203 |
| C01 | EUR_GBP | short | other | 69266 | 17281 | 0.249 |
| C01 | EUR_CHF | short | other | 68801 | 14697 | 0.214 |
| C02 | EUR_CHF | short | other | 68302 | 15747 | 0.231 |
| C02 | AUD_CHF | short | other | 64661 | 11371 | 0.176 |
| C01 | AUD_NZD | short | other | 63918 | 8158 | 0.128 |
| C02 | AUD_NZD | short | other | 62373 | 7860 | 0.126 |
| C01 | AUD_NZD | long | other | 60704 | 8705 | 0.143 |
| C01 | AUD_CHF | long | other | 59087 | 9814 | 0.166 |
| C01 | AUD_CHF | short | other | 59002 | 10638 | 0.180 |
| C02 | NZD_USD | short | other | 58997 | 15107 | 0.256 |
| C02 | USD_CHF | short | other | 58736 | 14594 | 0.248 |
| C02 | AUD_USD | short | other | 56863 | 14690 | 0.258 |
| C02 | AUD_CAD | short | other | 54650 | 9255 | 0.169 |
| C02 | EUR_GBP | long | other | 54593 | 12101 | 0.222 |
| C01 | AUD_CAD | short | other | 53814 | 8621 | 0.160 |
| C02 | EUR_CHF | long | other | 52156 | 10722 | 0.206 |
| C02 | EUR_USD | short | other | 51513 | 16283 | 0.316 |
| C01 | AUD_CAD | long | other | 50386 | 8348 | 0.166 |
