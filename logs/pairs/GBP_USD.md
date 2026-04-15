# GBP_USD — Pair Dev Log

**Execution Profile:** Medium (4p trigger, 1.5 offset, 5.0 fallback, 2.0x fast mult, 1.0 green)
**Status:** Active
**BASE_PAIRS member:** No (probation)

---

## Historical Lessons (V1/V2)

### [2026-04-07] [BOTH] — Trade 4 postmortem: 3rd CT short at PDH, -$65 V1 / -$2,031 V2
**Source:** known-defects.md, Defect 1
**Type:** bug
**Detail:** GBP_USD pressed PDH for 9 hours. Bot entered 3rd counter-trend short at same zone in one day — first two only hit TP1 partials (reversal never materialized to TP2). Tier 1/2 override had zero memory of prior failures. Led to Defect 1 (CT override no memory), Defect 2 (box_contained lookback too short), and Defect 3 (no daily same-zone entry cap). Post-breakout at 20:02, regime score dropped to -5.0. Regime only caught the problem after the SL hit.
