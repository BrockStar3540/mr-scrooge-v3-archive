# gates/spread — Dev Log

> Spread gate: monitors bid-ask spread and pauses trading during abnormal spread conditions.

---

## Historical Lessons (V1/V2)

### [2026-03-31] [V2] — Spread consistency: 2 consecutive scans
**Source:** NOTES.md
**Type:** lesson
**Detail:** Spread must exceed threshold on 2 CONSECUTIVE scans (10 minutes) before pausing. Single-candle spread spikes (common in Sydney/Sunday) should not block valid setups.

### [2026-03-31] [V2] — Spread spike definition: 4x London baseline
**Source:** ORIGINAL_CONFIG.md
**Type:** rule
**Detail:** spread_spike_threshold = 4.0. Spike = spread > 4x London baseline.
