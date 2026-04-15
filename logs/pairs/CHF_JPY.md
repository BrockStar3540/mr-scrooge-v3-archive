# CHF_JPY — Pair Dev Log

**Execution Profile:** Wide (6p trigger, 2.0 offset, 7.0 fallback, 1.8x fast mult, 1.5 green)
**Status:** Active — proven performer
**BASE_PAIRS member:** Yes (+$0.18 historical edge, small sample)

---

## Historical Lessons (V1/V2)

### [2026-04-12] [BOTH] — Parity harness BB position boundary noise
**Source:** NOTES.md
**Type:** warning
**Detail:** V1 and V2 diverge by 4-8 points on CHF_JPY when bb_pos is near 0.85 boundary. Pure timing noise from 30-second fetch gaps — not actionable. Accept small signal divergences from timing, they're not real.

### [2026-04-14] [V2] — Wide spread caused SL inside spread (trigger-side bug)
**Source:** known-defects.md
**Type:** bug
**Detail:** During wide spreads (13-16p on JPY), SL was calculated from mid-price but OANDA triggers shorts on ask. SL placed inside executable spread → instant fill (dead on arrival). Part of the trigger-side validation fix applied to all JPY pairs.
