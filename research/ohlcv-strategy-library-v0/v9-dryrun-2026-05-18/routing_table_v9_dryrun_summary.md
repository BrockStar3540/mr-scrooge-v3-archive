# routing_table_v9 dry-run summary

**Generated**: 2026-05-18T03:59:30.945423+00:00

## Inputs

- Probe seed-family children: **7,572** rows (2x correction applied for V3 probes)
- Textbook seed-family children: **883** rows (after dropping **610** with legacy session-bucket vocabulary)
- Combined candidate universe: **8,455** child rules
- Unique cells after best-per-cell aggregation: **759**

## Tier distribution (v9 dry-run vs v8)

| Tier | v9 dry-run cells | v8 cells (parent-regime) | Delta |
|---|---:|---:|---:|
| Elite | 6 | 1 | +5 |
| Pro | 3 | 21 | -18 |
| Seed-Pro | 17 | 0 | +17 |
| Standard | 0 | 46 | -46 |
| Seed | 413 | 0 | +413 |
| Probationary | 320 | 50 | +270 |

## Family × Tier (v9)

| Family | Elite | Pro | Seed-Pro | Standard | Seed | Probationary | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| dbb_trend | 6 | 1 | 11 | 0 | 204 | 122 | 344 |
| direct | 0 | 1 | 3 | 0 | 96 | 99 | 199 |
| reversal | 0 | 1 | 3 | 0 | 113 | 99 | 216 |

## Parent regime × Tier

| Regime | Elite | Pro | Seed-Pro | Standard | Seed | Probationary | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| C01 | 1 | 3 | 6 | 0 | 178 | 127 | 315 |
| C02 | 5 | 0 | 11 | 0 | 235 | 193 | 444 |

## Coverage

- Pairs covered: **26** — AUD_CAD, AUD_CHF, AUD_JPY, AUD_NZD, AUD_USD, CAD_JPY, CHF_JPY, EUR_AUD, EUR_CAD, EUR_CHF, EUR_GBP, EUR_JPY, EUR_NZD, EUR_USD, GBP_AUD, GBP_CAD, GBP_CHF, GBP_JPY, GBP_NZD, GBP_USD, NZD_JPY, NZD_USD, USD_CAD, USD_CHF, USD_JPY, USD_MXN
- Strategies covered: **15**

## Threshold sensitivity

How many unique cells survive at different `(min_n_unique, min_wr_raw, min_wr_lb)` triplets?

### Wilson LB = 0 (raw threshold only)

| min_n_unique \ min_wr | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 |
|---|---:|---:|---:|---:|---:|
| 10 | 511 | 511 | 437 | 255 | 117 |
| 15 | 196 | 196 | 126 | 50 | 2 |
| 20 | 85 | 85 | 39 | 5 | 0 |
| 25 | 32 | 32 | 11 | 0 | 0 |
| 30 | 9 | 9 | 1 | 0 | 0 |
| 40 | 5 | 5 | 0 | 0 | 0 |

### Wilson LB >= 0.40 (evidence-adjusted, the proposed Pro bar)

| min_n_unique \ min_wr | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 |
|---|---:|---:|---:|---:|---:|
| 10 | 511 | 511 | 437 | 255 | 117 |
| 15 | 196 | 196 | 126 | 50 | 2 |
| 20 | 85 | 85 | 39 | 5 | 0 |
| 25 | 32 | 32 | 11 | 0 | 0 |
| 30 | 9 | 9 | 1 | 0 | 0 |
| 40 | 5 | 5 | 0 | 0 | 0 |

## Tier rule used

```
Elite         wr_lb >= 0.55 AND n_unique >= 30
Pro           wr_lb >= 0.45 AND n_unique >= 30
Seed-Pro      wr_raw >= 0.85 AND n_unique >= 15   (small-but-pure)
Standard      wr_lb >= 0.35 AND n_unique >= 30
Seed          wr_raw >= 0.70 AND n_unique >= 10   (promising)
Probationary  rest

(wr_lb = Wilson 80% lower bound on raw WR)
```

## Notes

- This is a DRY RUN. No `routing_table_v9.parquet` is written. The cells CSV
  is informational, not deployable.
- Aggregation is at parent-regime granularity (C01/C02/etc.), NOT sub-regime.
  The seed-family children were mined at parent-regime grain. Sub-regime
  cell granularity would require re-mining or sub-regime classifier replay.
- OOS validation has NOT been applied. Cells shown are in-sample purity only.
  The next pass before deploying anything as Pro+ should replay the rules on
  a held-out time window and recompute Wilson LBs from holdout WR.