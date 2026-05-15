# seed_family_children_loser_contrast_bank

**Built:** 2026-05-15T16:59:57.729230+00:00
**Row count:** 6,040,324
**Size on disk:** ~2.38 GB  (Mini-only; gitignored from EC2 commit)

## Bucket counts

- **rejected_by_shave**: 5,764,161
- **parent**: 254,068
- **false_friend_sibling**: 17,456
- **residual**: 4,639

## Loser session distribution (rejected_by_shave + residual + false_friend_sibling)

- london: 2,499,419
- ny: 1,846,745
- asia: 1,440,092

## Top loser-heavy parent cells (rejected_by_shave + residual)

| strategy | pair | dir | regime | loser rows |
|---|---|---|---|---:|
| TF4_sar_short | USD_MXN | short | C01 | 346,940 |
| TF3_supertrend_long | GBP_CAD | long | C01 | 296,884 |
| TF4_sar_long | CAD_JPY | long | C01 | 283,057 |
| TF3_supertrend_long | USD_MXN | long | C01 | 259,573 |
| TF4_sar_long | EUR_USD | long | C02 | 259,565 |
| TF3_supertrend_short | USD_CAD | short | C02 | 242,891 |
| TF3_supertrend_long | NZD_JPY | long | C02 | 226,039 |
| TF4_sar_long | USD_JPY | long | C01 | 221,826 |
| TF4_sar_long | GBP_USD | long | C01 | 207,651 |
| TF3_supertrend_long | EUR_JPY | long | C02 | 205,428 |
| TF4_sar_long | USD_CAD | long | C02 | 186,919 |
| TF3_supertrend_long | EUR_CAD | long | C02 | 180,114 |
| TF3_supertrend_short | EUR_JPY | short | C01 | 137,065 |
| TF3_supertrend_short | EUR_CAD | short | C02 | 122,936 |
| TF3_supertrend_short | NZD_JPY | short | C02 | 117,606 |

## Loser hot zones by factor median (residual rows only)

| factor | median | p25 | p75 |
|---|---:|---:|---:|
| ATR_ratio | 0.1035 | 0.08516 | 0.1316 |
| RSI14 | 57.64 | 28.73 | 74.07 |
| BB_compress | 0.1656 | 0.111 | 0.2558 |
| price_pos | 0.7401 | 0.08082 | 0.9463 |
| volume_ratio | 1.283 | 1.021 | 1.82 |
| ADX14 | 31.84 | 25.39 | 40.45 |
| hour_utc | 13 | 8 | 14 |