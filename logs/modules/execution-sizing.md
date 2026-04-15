# execution/sizing — Dev Log

> Position sizing: calculates units from margin, risk cap, and instrument-specific parameters.

---

## Historical Lessons (V1/V2)

### [2026-04-09] [BOTH] — JPY sizing formula was wrong (cross-pair base price)
**Source:** AUDIT.md
**Type:** bug
**Detail:** Formula used current_price x margin_rate (wrong for cross pairs). Fixed to base_price_usd derived from pip_value. JPY pairs: 5% margin (20:1), CHF: ~3% (33:1), EUR/GBP: 2% (50:1).

### [2026-03-25] [V2] — Risk-capped sizing: 4% max loss per trade
**Source:** NOTES.md
**Type:** lesson
**Detail:** Dual-constraint: final_units = min(margin_units, risk_cap_units). max_risk = 4% of equity. Tight SL -> full exposure. Wide SL -> reduced size. Unconstrained risk before this fix: 3.5%-13.5% per trade.

### [2026-03-31] [V2] — Probation pair sizing removed, replaced by regime
**Source:** NOTES.md
**Type:** lesson
**Detail:** Dynamic regime scoring replaces static pair-based probation sizing. All pairs treated equally by sizing. Regime filters the losers.
