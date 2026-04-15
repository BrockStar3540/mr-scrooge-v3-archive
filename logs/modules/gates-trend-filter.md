# gates/trend_filter — Dev Log

> Trend filter gate: EMA-based trend detection with tier-aware override logic.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — EMA slope threshold calibrated to 0.0005/10 bars
**Source:** gates/trend_gate/NOTES.md
**Type:** lesson
**Detail:** Original 0.001 over 5 bars missed slow EUR downtrends. Switched to 0.0005 over 10 bars (approx 10 hours of EMA history).

### [2026-03-11] [V2] — Tier-aware blocking: box extremes override trend
**Source:** DAILY_NOTES_2026-03-11
**Type:** rule
**Detail:** Tier 1/2 zones OVERRIDE trend block — per MASTER_THEORY "because we're at the lower part of the box I would prefer to trade long." Tier 3/4 counter-trend entries still blocked.
