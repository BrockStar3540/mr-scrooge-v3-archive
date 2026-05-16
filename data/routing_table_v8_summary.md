# routing_table_v8 summary

**Built:** 2026-05-16T06:32:56.312628+00:00
**Source:** routing_table_v7 + sub_regime tier classification
**Rows:** 882  |  Unique cells: 126

## Tier breakdown

| tier | cells | mean_wr | mean_n | mean_R/trade | %/trade @ 80% margin |
|---|---:|---:|---:|---:|---:|
| Elite | 3 | 0.7587 | 45.3 | +1.276R | +2.30% |
| Pro | 23 | 0.5487 | 40.0 | +0.646R | +1.16% |
| Standard | 50 | 0.4349 | 41.9 | +0.305R | +0.55% |
| Probationary | 50 | 0.3570 | 40.9 | +0.071R | +0.13% |

## Brock target: +2% per trade

At 80% margin + 50:1 leverage, 2% per trade requires +1R per trade.
Math: WR x 2R - (1-WR) x 1R = 1.0R  →  WR = 66.7 percent

**The Elite tier (wr>=65% and n>=30) is the path to the 2% per-trade target.**

Config flip to make the bot trade Elite-only:
```
gates.entry_filter.min_tier = "Elite"   # default Probationary
```

Trade-off: Elite tier fires far less often than the full v7 surface (1-5 trades/week vs 25-35).