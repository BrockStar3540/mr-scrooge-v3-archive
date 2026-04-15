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

### [2026-03-02] [V1] — CRITICAL: Runaway re-entry bug — 20 identical losses in 3 hours
**Source:** Dropbox: "2026-03-02_Scrooge bot USDJPY runaway re-entry bug.md"
**Type:** bug
**Detail:** Bot entered 20 consecutive identical SELL trades at 110.51, each stopped at 111.49 (98 pips loss), every 10 minutes for 3 hours. Zero trade outcome awareness — no loss memory, no daily loss limit, no cooldown after stop, no signal invalidation. Price was already above the stop at entry time (1-second fills = instant stop). This incident was the foundational reason for ALL circuit breakers: zone entry cap (3/day), cooldown after stop (60 min), daily loss limit (3%), consecutive loss halt, and pre-entry price validation. V3 MUST have all of these from day one.
