# telemetry/quality — Dev Log

> Trade quality telemetry: MFE/MAE analysis, follow-through scoring, and entry context capture.

---

## Historical Lessons (V1/V2)

### [2026-03-24] [V2] — MFE/MAE ratio > 2.5 = clean entry
**Source:** quality/NOTES.md
**Type:** rule
**Detail:** MFE/MAE > 2.5 = market moved with us immediately. < 1.2 = fought us hard.

### [2026-03-24] [V2] — Follow-through score: 30+25+25+20 = 100
**Source:** quality/NOTES.md
**Type:** rule
**Detail:** 30 pts MFE/MAE ratio, 25 pts reached +5 pips in <6 candles, 25 pts MFE >= 80% of TP1, 20 pts final positive result. Wait 50+ trades before using as filter.

### [2026-03-24] [V2] — Entry context: 30+ fields per trade
**Source:** DAILY_NOTES_2026-03-24
**Type:** rule
**Detail:** Every fill records: trade_id, symbol, direction, prices, signal_score, zone tier, gate states, position book, order book imbalance, spread, RSI, MACD, BB Z-score, EMA alignment, realized vol, ADR %, volume ratio, touch count. Outcome patched on close.

### [2026-03-31] [V2] — Quiet inside-box trades outperform edge tests
**Source:** NOTES.md
**Type:** discovery
**Detail:** Best day (March 24): AUD_CAD had box_contained(+1) + compression(+1) = regime score +2 (NORMAL). Quiet range + compressed ATR = highest quality reversal setup. Aggressive edge tests are traps.
