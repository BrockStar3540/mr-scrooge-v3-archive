# gates/directional_pressure — Dev Log

> Directional pressure gate: detects sucker moves and validates directional conviction before entry.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — Flexible candle window, not strict consecutive
**Source:** gates/sucker_move_gate/NOTES.md
**Type:** lesson
**Detail:** Sucker moves can be messy/choppy. Replaced strict consecutive candle counting with flexible window approach. Uses search_window = max_candles + 2, counts directional candles within window, requires >= min_candles AND net price movement in correct direction. Per MASTER_THEORY: "Sometimes it can look a little choppier."

### [2026-03-11] [V2] — Termination zone proximity required
**Source:** gates/sucker_move_gate/NOTES.md
**Type:** rule
**Detail:** Both DETECTED and TERMINATING_AT_ZONE must be True. Move must end within 0.5% of the target liquidity zone. Move must terminate near the zone or it doesn't prove the zone wall was tested.

### [2026-03-11] [BOTH] — net_ok check was filtering valid setups at reversal moment
**Source:** Dropbox: 2026-03-11_d66ae964.md
**Type:** bug (FIXED)
**Detail:** Detection compared "last close vs close 7 bars ago" — but by the time the reversal candle forms, price is already coming back up off support. Last close is no longer below window start, so net_ok=False filters the trade at its most valid moment. Fix: remove net_ok check entirely. Sucker move is defined by 3-5 directional candles INTO the zone, not by net displacement at the moment of evaluation.

### [2026-03-11] [BOTH] — Hourly confirmation gate was NOT in MASTER_THEORY
**Source:** Dropbox: 2026-03-11_d66ae964.md
**Type:** discovery
**Detail:** _hourly_confirms() required 40% rejection wick OR hourly engulfing before 5m patterns counted. This gate blocked valid 5m setups. Not in source theory. Demoted to advisory only — annotates but doesn't block.
