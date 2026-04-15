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
