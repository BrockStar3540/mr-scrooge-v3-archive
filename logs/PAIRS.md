# Currency Pair Log Index

> Master index for per-pair dev logs. When a pair-specific change, lesson, or bug is found, update the pair's log and add a brief here.
>
> Format: `[DATE] [PAIR] — one-line summary -> logs/pairs/PAIR.md`

---

## Execution Profile Categories

| Category | Pairs | Trigger (pips) | Offset | Fallback | Fast Mult | Green Offset |
|----------|-------|---------------|--------|----------|-----------|-------------|
| Tight | EUR_USD, AUD_USD, EUR_CAD | 2 | 1.0 | 3.0 | 2.5x | 0.5 |
| Medium | GBP_USD, USD_JPY, NZD_USD, USD_CHF, USD_CAD, EUR_JPY | 4 | 1.5 | 5.0 | 2.0x | 1.0 |
| Wide | GBP_JPY, CHF_JPY, NZD_JPY, AUD_JPY, AUD_CHF | 6 | 2.0 | 7.0 | 1.8x | 1.5 |

---

## Pair-Specific Findings

- `[2026-04-09] [USD_MXN]` — Effectively choked by spread pause + OTR gate + score floor. Marginal pair, observe during beta -> [logs/pairs/USD_MXN.md](pairs/USD_MXN.md)
- `[2026-04-09] [AUD_CAD]` — BASE_PAIRS member, +$0.80 historical edge. Best day trade (March 24) had box_contained + compression = NORMAL regime -> [logs/pairs/AUD_CAD.md](pairs/AUD_CAD.md)
- `[2026-04-09] [AUD_CHF]` — BASE_PAIRS member, wide execution profile. +$0.17 edge -> [logs/pairs/AUD_CHF.md](pairs/AUD_CHF.md)
- `[2026-04-09] [USD_JPY]` — BASE_PAIRS member, medium execution profile. +$0.87 edge -> [logs/pairs/USD_JPY.md](pairs/USD_JPY.md)
- `[2026-04-09] [EUR_CAD]` — BASE_PAIRS member, tight execution profile. +$0.83 edge -> [logs/pairs/EUR_CAD.md](pairs/EUR_CAD.md)
- `[2026-04-09] [CHF_JPY]` — BASE_PAIRS member, wide execution profile. +$0.18 edge -> [logs/pairs/CHF_JPY.md](pairs/CHF_JPY.md)
- `[2026-04-07] [GBP_USD]` — Trade 4 postmortem: 3rd CT short at PDH in one day, -$65 V1 / -$2,031 V2 -> [logs/pairs/GBP_USD.md](pairs/GBP_USD.md)
- `[2026-03-25] [USD_CHF]` — 5 MARKET order rejections from TP2 at/below current ask -> [logs/pairs/USD_CHF.md](pairs/USD_CHF.md)
