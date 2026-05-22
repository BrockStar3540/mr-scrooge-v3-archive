# Scalper Relabeling Summary — 10-pip SL / 12-pip TP1 / ratchet

Generated 2026-05-21. 26 per-pair trade_log files, total 14,928,094 events.

## Outcome distribution under 10/12/ratchet

| outcome | count | pct | realized pips |
|---|---:|---:|---:|
| clean_win | 982,105 | 6.6% | +12 |
| full_loss | 2,045,849 | 13.7% | -10 |
| ratchet_neg6_likely | 525,551 | 3.5% | -6 |
| ratchet_neg3_likely | 515,719 | 3.5% | -3 |
| ratchet_BE_likely | 513,593 | 3.4% | +0 |
| neither | 79,368 | 0.5% | +0 |
| ambiguous_win_or_stop | 10,238,860 | 68.6% | — |
| ambiguous_other | 27,049 | 0.2% | — |

## Headline metrics

- **Clean expectancy**: -2.869 pips/trade across 4,662,185 non-ambiguous events
- **Clean WR** (clean_win / clean_total): 21.07%
- **Ambiguity rate**: 68.8% (vs ~69% under flat 6/12 — ratchet narrows ambiguous bin)
- **Old `is_win` rate**: 6.67%

## Caveat

The `_likely` outcomes assume favorable MFE happened before adverse MAE. Without OHLC bar sequence,
this is an estimate. Pure ambiguous bins are separate. OHLC-based resolution refines later.
