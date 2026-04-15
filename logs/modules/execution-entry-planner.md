# execution/entry_planner — Dev Log

> Entry planner: validates entry conditions, manages trigger freshness, and reconciles fill prices.

---

## Historical Lessons (V1/V2)

### [2026-03-25] [V2] — TP2 market-price guard: block if within 2 pips of current
**Source:** NOTES.md
**Type:** bug
**Detail:** 5 USD/CHF MARKET order rejections — TP2 was at/below current ask. Signal validated tp2 > entry_price but NOT tp2 > current_ask. Guard: tp2 <= current_price + 2_pips -> reject. Check at signal generation AND pre-submit.

### [2026-04-10] [V2] — Entry safety gates before ranking
**Source:** NOTES.md
**Type:** lesson
**Detail:** 4 hard gates BEFORE ranking: 1) Score >= 20, 2) Spread ratio <= 3.0, 3) Trigger freshness (price not past trigger), 4) Trigger distance <= 0.3 ATR_5m. Prevents chasing and weak entries.

### [2026-04-09] [BOTH] — Reconciliation on fill: recalculate SL/TP from actual fill price
**Source:** AUDIT.md
**Type:** lesson
**Detail:** After broker fill, recalculate SL/TP from actual fill price. Corrects for slippage and ensures risk matches intent. Previously SL/TP calculated at entry time without fill adjustment.

### [2026-04-09] [BOTH] — RR sanity check at current price, not screen time
**Source:** AUDIT.md
**Type:** lesson
**Detail:** Signal may pass at screen time, but price may have moved by execution. Real-time RR check prevents chasing degraded setups.
