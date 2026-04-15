# classifiers/regime — Dev Log

> Regime classifier: scores market conditions (NORMAL, CAUTION, RESTRICTED, BLOCKED) to gate entries and adjust sizing.

---

## Historical Lessons (V1/V2)

### [2026-03-31] [V2] — Entry requires regime score >= +1, not just "not BLOCKED"
**Source:** NOTES.md
**Type:** lesson
**Detail:** Old: only BLOCKED (score <= -3) suppressed. New: entry requires score >= +1. CAUTION (score = 0) = wait. At least one positive signal must be present.

### [2026-03-31] [V2] — Hysteresis: 2-scan lookback for recovery confirmation
**Source:** NOTES.md
**Type:** lesson
**Detail:** If regime score was <= -2 in either of the last 2 scans (10 min), entry blocked until score >= +1 confirmed. Implemented via deque(maxlen=2). Addresses USD/MXN incident where one-candle improvement allowed entry into hostile regime.

### [2026-04-09] [BOTH] — NORMAL regime is the edge: 77.8% WR, +$5,037
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** discovery
**Detail:** 511 V1 trades + 58 V2: NORMAL regime 77.8% WR, +$5,037 P&L. CAUTION: 57.9% WR, -$5,719. RESTRICTED: 50% WR. Regime score reliably predicts outcomes. Must be a hard blocker.

### [2026-04-13] [V2] — box_contained lookback was too short (30 min)
**Source:** known-defects.md, Defect 2
**Type:** bug
**Detail:** _ACCEPTANCE_LOOKBACK = 6 (30 minutes of M5 candles). Price dipping briefly inside the range reset score to +1.0 despite pressing PDH for 9 hours. Regime only caught the problem after SL hit. Increase lookback or add daily zone-touch counter.

### [2026-04-09] [BOTH] — Regime feeds scoring: NORMAL +10, CAUTION -10
**Source:** NOTES.md
**Type:** rule
**Detail:** Regime score now feeds the scoring system itself, not just as a blocker. NORMAL: +10 pts to signal score. CAUTION/RESTRICTED: -10 pts.

### [2026-04-09] [BOTH] — Size halving on RESTRICTED state
**Source:** regime/NOTES.md
**Type:** rule
**Detail:** BLOCKED -> suppress entry. Score < +1 -> suppress entry. RESTRICTED -> allows entry but halves position size (50%).
