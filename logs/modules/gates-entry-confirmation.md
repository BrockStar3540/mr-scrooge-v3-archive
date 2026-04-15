# gates/entry_confirmation — Dev Log

> Entry confirmation gate: validates signal candle patterns, stop placement, and trigger prices.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — Stop at signal candle extreme, not box wall
**Source:** gates/pitchfork_gate/NOTES.md
**Type:** lesson
**Detail:** Stop placement changed from mixed box-wall/candle-extreme to signal candle extreme ONLY. Per MASTER_THEORY: stop goes at the extreme of the signal candle. Long: low * (1 - sl_floor_pct). Short: high * (1 + sl_floor_pct).

### [2026-03-11] [V2] — Trigger prices use candle extreme, not zone price
**Source:** gates/pitchfork_gate/NOTES.md
**Type:** rule
**Detail:** All entry triggers use candle high/low (h * 1.0001 / l * 0.9999), not zone_price. Per MASTER_THEORY: "Entry above the high of that candle."

### [2026-03-11] [V2] — Timeframe switching on high volatility
**Source:** gates/pitchfork_gate/NOTES.md
**Type:** rule
**Detail:** Normal: 5M bars. High volatility (last 1H range > 2x hourly ATR): switch to 1H bars. Prevents false breakouts during violent sessions.

### [2026-03-26] [BOTH] — SL floor was too wide at 0.50%
**Source:** NOTES.md
**Type:** bug
**Detail:** sl_floor_pct = 0.0050 (0.50%) enforced ~54 pip minimum stop on EUR pairs at 1.08. Inflated RR denominator — 1.6x reward nearly unreachable. Lowered to 0.0025 (0.25%), making ~27 pip minimum. Monitor stop-hit rate.

### [2026-04-09] [BOTH] — wick_rejection profitable, engulfing_reversal bleeds
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** discovery
**Detail:** wick_rejection (john_wick): +$1,267 V2, near breakeven V1. engulfing_reversal (power_of_towers): -$4,086 V2, -$288 V1. Score wick_rejection +15 pts, engulfing_reversal +5 pts. CT + engulfing_reversal = -15 pts penalty.

### [2026-04-15] [BOTH] — Wick ratio INCONSISTENT between V1 and V2
**Source:** Raw OANDA candle analysis, docs/MASTER_FINDINGS.md
**Type:** warning
**Detail:** V2 practice: wick ratio W=2.19, L=2.16 (0% delta, no signal). V1 live: W=1.07, L=0.55 (+94% delta, strong signal). The finding FLIPS between datasets. Cannot rely on wick ratio as a scoring factor. Keep existing detection logic for pattern classification but DO NOT weight wick_ratio in scoring.

### [2026-04-15] [BOTH] — Signal type (JW vs PoT) REVERSES between V1 and V2
**Source:** Raw OANDA candle analysis, docs/MASTER_FINDINGS.md
**Type:** warning
**Detail:** V2: wick_rejection profitable (+$1,267), engulfing bleeds (-$4,086). V1 live: wick_rejection = 44% WR (bad), engulfing = 75% WR (good). Completely reversed. Use April 9 audit weights (511 V1 + 58 V2 trades) as the larger sample, not either 50-trade sample alone.
