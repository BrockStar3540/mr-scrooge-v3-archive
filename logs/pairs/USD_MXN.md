# USD_MXN — Pair Dev Log

**Execution Profile:** None assigned (exotic)
**Status:** Probation — observe during beta
**BASE_PAIRS member:** No

---

## Historical Lessons (V1/V2)

### [2026-04-12] [V2] — Effectively choked by multiple gates
**Source:** NOTES.md
**Type:** warning
**Detail:** Choked by spread pause + OTR gate + score floor. Wide spread + high OTR makes it marginal. Needs 100+ trades to determine if worth keeping in universe. Consider removal.

### [2026-03-31] [V2] — Regime hysteresis incident: one-candle recovery allowed entry
**Source:** NOTES.md
**Type:** bug
**Detail:** USD/MXN incident where one-candle improvement allowed entry into 10-week rejection-failure regime. Led to adding 2-scan hysteresis lookback requirement.

### [2026-04-10] [BOTH] — Score=1 entry lost -$40.41 (V1) and -$940.54 (V2)
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** bug
**Detail:** Regime CAUTION penalty pushed score to floor (1) but bot still entered with full sizing. This trade was the primary motivation for adding the minimum score >= 20 gate.
