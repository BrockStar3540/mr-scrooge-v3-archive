# Regime × Pair Matrix — Summary

Generated: 2026-05-12T23:55:38.330405+00:00
Corpus: 2,543,184 filled trades from 208 parquet segments

## Files

| File | Grain | Cells |
|---|---|---|
| regime_x_pair_x_period | regime × pair × period | 338 |
| regime_x_pairfamily_x_period | regime × pair_family × period | 52 |
| regime_x_pair_x_session_x_dir_x_period | full grain | 2616 |
| candidates_regime_x_pair_x_period | n≥75 + mean_r>0 + CI_low>0 | 23 |
| candidates_full_grain | n≥30 + mean_r>0 + CI_low>0 (FG) | 229 |

## Candidates — regime × pair × period (n≥75, CI lb > 0)

These are the cells where a real positive edge survives the bootstrap CI gate.
Each row is a candidate behavioral fork — a place where the broad regime label
masks a sharper pocket.

| regime_label   | pair    | period    |     n |   win_rate |   mean_r |    sum_r |   ci_low_95 |   top_year_share |   top_quarter_share |
|:---------------|:--------|:----------|------:|-----------:|---------:|---------:|------------:|-----------------:|--------------------:|
| Alpha-fresh    | AUD_JPY | discovery | 29058 |     0.3932 |   0.0162 | 471.1600 |      0.0018 |           1.0913 |              0.9066 |
| Alpha-fresh    | AUD_JPY | holdout   |  7072 |     0.4054 |   0.0464 | 328.4380 |      0.0169 |           0.7174 |              0.4816 |
| Alpha-fresh    | AUD_USD | holdout   |  6750 |     0.4027 |   0.0551 | 371.9650 |      0.0246 |           0.8986 |              0.9715 |
| Alpha-fresh    | USD_JPY | discovery | 19386 |     0.3912 |   0.0236 | 458.1990 |      0.0058 |           1.0366 |              0.7115 |
| Bravo          | AUD_JPY | holdout   |  3990 |     0.4103 |   0.0473 | 188.7740 |      0.0086 |           1.1329 |              0.4949 |
| Bravo          | AUD_USD | holdout   |  3634 |     0.4095 |   0.0544 | 197.7920 |      0.0132 |           0.8552 |              0.4538 |
| Bravo          | NZD_USD | holdout   |  3938 |     0.4022 |   0.0452 | 177.8180 |      0.0058 |           0.5082 |              0.6200 |
| Charlie        | CAD_JPY | holdout   |  3766 |     0.4246 |   0.1010 | 380.5010 |      0.0607 |           0.7116 |              0.4155 |
| Charlie        | USD_JPY | discovery | 21056 |     0.3949 |   0.0207 | 436.5560 |      0.0039 |           0.8620 |              0.6678 |
| Delta          | AUD_CAD | discovery |   924 |     0.4459 |   0.1628 | 150.3820 |      0.0787 |           0.4084 |              0.3183 |
| Delta          | AUD_JPY | holdout   |    92 |     0.5109 |   0.2532 |  23.2950 |      0.0034 |           0.8602 |              0.6462 |
| Echo-tight     | EUR_CAD | holdout   |  4766 |     0.3999 |   0.0405 | 193.0630 |      0.0044 |           0.6790 |              0.5456 |
| Echo-tight     | EUR_CHF | discovery | 17390 |     0.4040 |   0.0434 | 755.2220 |      0.0245 |           0.3024 |              0.1827 |
| Echo-tight     | EUR_CHF | holdout   |  4236 |     0.4020 |   0.0403 | 170.6640 |      0.0021 |           0.7436 |              0.5246 |
| Echo-tight     | EUR_GBP | discovery | 18376 |     0.3959 |   0.0328 | 602.1980 |      0.0143 |           0.4514 |              0.2639 |
| Echo-tight     | EUR_USD | holdout   |  4416 |     0.4192 |   0.0931 | 411.0150 |      0.0549 |           0.6493 |              0.4521 |
| Echo-tight     | GBP_CAD | discovery | 19004 |     0.3889 |   0.0203 | 385.6860 |      0.0021 |           1.0514 |              0.4795 |
| Echo-tight     | GBP_CHF | discovery | 18654 |     0.3939 |   0.0261 | 487.7080 |      0.0079 |           0.6019 |              0.4077 |
| Echo-tight     | GBP_USD | holdout   |  4540 |     0.3969 |   0.0384 | 174.2640 |      0.0011 |           0.5143 |              0.7090 |
| Echo-tight     | NZD_USD | discovery | 18500 |     0.3896 |   0.0189 | 349.6440 |      0.0005 |           0.5389 |              0.5907 |
| Echo-tight     | USD_CHF | discovery | 18050 |     0.3904 |   0.0215 | 388.3120 |      0.0029 |           0.2943 |              0.3619 |
| Echo-tight     | USD_CHF | holdout   |  4440 |     0.3957 |   0.0394 | 174.7260 |      0.0020 |           0.5057 |              0.3807 |
| Echo-tight     | USD_MXN | discovery | 17088 |     0.3962 |   0.0420 | 717.9170 |      0.0227 |           0.3467 |              0.2008 |

## Distribution of mean_r by regime × period (top-line)

| regime_label   |   discovery |   holdout |
|:---------------|------------:|----------:|
| Alpha-extended |     -0.1373 |   -0.1047 |
| Alpha-fresh    |     -0.0276 |   -0.0387 |
| Bravo          |     -0.0057 |   -0.0118 |
| Charlie        |     -0.0351 |   -0.0414 |
| Delta          |     -0.0186 |   -0.0305 |
| Echo-explosive |     -0.0306 | +nan      |
| Echo-tight     |     +0.0054 |   +0.0033 |

## Discovery → Holdout direction stability

For each (regime, pair) — did the mean_r sign flip between periods?

Sign flips: 56 / 156 = 35.9% of (regime × pair) cells flipped sign in holdout

### Worst sign-flips (discovery WIN → holdout LOSE)

| regime_label   | pair    |    disc |    hold | sign_flip   |   delta |
|:---------------|:--------|--------:|--------:|:------------|--------:|
| Delta          | EUR_JPY | +0.0440 | -0.2440 | True        | -0.2880 |
| Delta          | EUR_NZD | +0.0330 | -0.1904 | True        | -0.2233 |
| Delta          | GBP_USD | +0.0519 | -0.1345 | True        | -0.1864 |
| Delta          | EUR_GBP | +0.0352 | -0.0902 | True        | -0.1253 |
| Bravo          | EUR_GBP | +0.0098 | -0.1139 | True        | -0.1237 |
| Alpha-fresh    | GBP_JPY | +0.0102 | -0.0973 | True        | -0.1075 |
| Delta          | EUR_USD | +0.0149 | -0.0872 | True        | -0.1021 |
| Bravo          | EUR_CAD | +0.0131 | -0.0820 | True        | -0.0950 |
| Delta          | USD_CHF | +0.0343 | -0.0571 | True        | -0.0914 |
| Bravo          | GBP_JPY | +0.0197 | -0.0658 | True        | -0.0855 |
| Echo-tight     | AUD_NZD | +0.0072 | -0.0609 | True        | -0.0681 |
| Bravo          | EUR_JPY | +0.0146 | -0.0532 | True        | -0.0678 |
| Delta          | NZD_USD | +0.0273 | -0.0360 | True        | -0.0633 |
| Alpha-fresh    | USD_MXN | +0.0085 | -0.0446 | True        | -0.0531 |
| Echo-tight     | GBP_CAD | +0.0203 | -0.0304 | True        | -0.0507 |

### Best sign-flips (discovery LOSE → holdout WIN)

| regime_label   | pair    |    disc |    hold | sign_flip   |   delta |
|:---------------|:--------|--------:|--------:|:------------|--------:|
| Delta          | GBP_CHF | -0.0005 | +0.0604 | True        | +0.0609 |
| Bravo          | AUD_USD | -0.0077 | +0.0544 | True        | +0.0621 |
| Bravo          | USD_CAD | -0.0405 | +0.0422 | True        | +0.0827 |
| Alpha-fresh    | AUD_USD | -0.0511 | +0.0551 | True        | +0.1062 |
| Alpha-fresh    | NZD_USD | -0.0863 | +0.0225 | True        | +0.1088 |
| Delta          | USD_JPY | -0.0099 | +0.1066 | True        | +0.1165 |
| Delta          | GBP_NZD | -0.0959 | +0.0392 | True        | +0.1351 |
| Delta          | GBP_AUD | -0.1319 | +0.0055 | True        | +0.1374 |
| Alpha-extended | AUD_NZD | -0.1389 | +0.0051 | True        | +0.1440 |
| Charlie        | CAD_JPY | -0.0432 | +0.1010 | True        | +0.1442 |
| Delta          | CHF_JPY | -0.0955 | +0.0877 | True        | +0.1832 |
| Alpha-extended | GBP_CHF | -0.1501 | +0.0391 | True        | +0.1892 |
| Alpha-extended | EUR_CHF | -0.1635 | +0.0877 | True        | +0.2512 |
| Delta          | AUD_USD | -0.1635 | +0.0884 | True        | +0.2519 |
| Delta          | AUD_JPY | -0.1477 | +0.2532 | True        | +0.4009 |