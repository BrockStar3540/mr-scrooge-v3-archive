# gates/overhead_ratio — Dev Log

> Overhead-to-reward ratio gate: measures how much price must travel through resistance versus potential reward.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — OTR thresholds with zone tier interaction
**Source:** gates/otr_gate/NOTES.md
**Type:** rule
**Detail:** Excellent (<5%), acceptable (5-15%), marginal (15-25%), skip (>=25%). Marginal allowed ONLY when zone tier <= 2 AND (pressure_strength == 'strong' OR confirmation_type in ('wick_rejection', 'engulfing_reversal')).

### [2026-04-15] [V1 LIVE] — OTR scoring INVERTED: low OTR = 17% WR (worst bracket)
**Source:** Raw OANDA candle analysis, docs/FACTOR_BIBLE.md
**Type:** correction
**Detail:** OTR was scored positively for low values (excellent <5%, acceptable <15%). V1 live data shows OTR <8% = 17% WR — the WORST bracket. 24% of all losers cluster at low OTR. Low OTR means tight spread + huge box = unfocused wide structure. OTR 8-18% = 63-68% WR (sweet spot). Action: INVERT scoring — low OTR gets penalty, 8-18% gets bonus.
