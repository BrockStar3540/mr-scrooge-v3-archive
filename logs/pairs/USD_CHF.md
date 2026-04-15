# USD_CHF — Pair Dev Log

**Execution Profile:** Medium (4p trigger, 1.5 offset, 5.0 fallback, 2.0x fast mult, 1.0 green)
**Status:** Active
**BASE_PAIRS member:** No

---

## Historical Lessons (V1/V2)

### [2026-03-25] [V2] — 5 MARKET order rejections: TP2 at/below current ask
**Source:** NOTES.md
**Type:** bug
**Detail:** 5 USD/CHF MARKET order 400 Bad Request rejections. TP2 (filtered PDH) was at or below current ask price. Signal engine validated tp2 > entry_price but NOT tp2 > current_ask. Led to adding TP2 market-price guard: tp2 <= current_price + 2_pips → reject. Guard applied at both signal generation AND pre-submit in main loop.
