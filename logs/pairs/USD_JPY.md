# USD_JPY — Pair Dev Log

**Execution Profile:** Medium (4p trigger, 1.5 offset, 5.0 fallback, 2.0x fast mult, 1.0 green)
**Status:** Active — proven performer
**BASE_PAIRS member:** Yes (+$0.87 historical edge)

---

## Historical Lessons (V1/V2)

### [2026-03-26] [V1] — First successful entry after SL floor fix
**Source:** NOTES.md
**Type:** lesson
**Detail:** First cycle after lowering sl_floor_pct from 0.50% to 0.25%, USD_JPY qualified and V1 entered successfully. The 0.50% floor was creating ~54 pip minimum stops on JPY pairs — too wide for the box size.

### [UNDATED] [BOTH] — JPY pip size = 0.01 (not 0.0001)
**Source:** sizing, execution
**Type:** rule
**Detail:** All JPY pairs use pip_size = 0.01. Affects: sizing formula (base_price_usd), zone proximity tolerance (2x), execution profiles (wide category), and spread kill switch (5 pips vs 2 pips default).

### [UNDATED] [BOTH] — 5% margin rate (20:1 leverage)
**Source:** SCROOGE.md
**Type:** rule
**Detail:** OANDA margin rate for JPY pairs is 5% (20:1). Higher than EUR/GBP (2%, 50:1). Sizing calculator must use per-instrument margin rate from broker, not fixed assumption.
