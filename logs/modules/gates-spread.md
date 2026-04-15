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

### [2026-04-15] [V1 LIVE] — Spread must be checked against natural stop
**Source:** Raw OANDA candle analysis, docs/FACTOR_BIBLE.md
**Type:** discovery
**Detail:** When spread exceeds the natural stop distance, the trade is mechanically broken — spread eats the entire risk. Spread/SL ratio >100% = 50% WR, -$110. Added as hard block: if spread > natural_stop, REJECT.

### [2026-04-15] [V1 LIVE] — Fixed pip threshold replaced with % of half box
**Source:** Raw OANDA candle analysis, docs/FACTOR_BIBLE.md
**Type:** correction
**Detail:** Old: fixed pip thresholds (2.0 default, 5.0 JPY). New: spread as percentage of half box, threshold at 10%. Spread >10% of half box = 20% WR. The % approach scales with box size — 2 pips on a 200-pip box is fine, 2 pips on a 20-pip box is 10%.
