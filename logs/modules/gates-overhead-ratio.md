# gates/overhead_ratio — Dev Log

> Overhead-to-reward ratio gate: measures how much price must travel through resistance versus potential reward.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — OTR thresholds with zone tier interaction
**Source:** gates/otr_gate/NOTES.md
**Type:** rule
**Detail:** Excellent (<5%), acceptable (5-15%), marginal (15-25%), skip (>=25%). Marginal allowed ONLY when zone tier <= 2 AND (pressure_strength == 'strong' OR confirmation_type in ('wick_rejection', 'engulfing_reversal')).
