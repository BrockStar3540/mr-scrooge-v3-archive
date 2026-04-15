# broker/oanda — Dev Log

> OANDA broker integration: API client, P/L calculation, margin rates, and error handling.

---

## Historical Lessons (V1/V2)

### [2026-04-09] [BOTH] — P/L calculation wrong for 17/21 non-USD-quote pairs
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** bug
**Detail:** CRITICAL: _calculate_partial_pnl() returned pnl in quote currency, not USD. All JPY, CAD, GBP, EUR, CHF pairs affected. Fixed: convert using pip_value_per_unit. This affected ALL P&L tracking.

### [2026-04-09] [BOTH] — OANDA 404 fallback for closed trade data
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** bug
**Detail:** get_trade_realized_pl(trade_id) falls back to transactions API when trade returns 404. Some trades vanish from /trades after close but appear in /transactions.

### [2026-04-12] [V2] — OANDA 502 errors: cache fallback
**Source:** NOTES.md
**Type:** lesson
**Detail:** Practice API returns 502s intermittently. Bar cache fallback prevents pair skipping — uses stale data but continues trading. Monitor accuracy impact.

### [2026-04-09] [BOTH] — Margin rates vary by instrument — fetch from broker on boot
**Source:** SCROOGE.md
**Type:** rule
**Detail:** JPY: 5% (20:1), CHF: ~3% (33:1), EUR/GBP: 2% (50:1). Must use broker's actual per-instrument margin rate, not a fixed leverage.
