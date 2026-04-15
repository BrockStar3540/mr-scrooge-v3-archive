# gates/zone_proximity — Dev Log

> Zone proximity gate: validates that price is close enough to a liquidity zone to warrant entry.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — JPY pairs need 2x proximity tolerance
**Source:** gates/zone_gate/NOTES.md
**Type:** rule
**Detail:** Standard pairs use 0.25% (0.0025). JPY crosses should use 0.50% proximity due to wider normal trading range.

### [2026-04-15] [V1 LIVE] — Wall proximity shows 0% delta (W=0.39, L=0.39)
**Source:** Raw OANDA candle analysis, docs/FACTOR_BIBLE.md
**Type:** correction
**Detail:** V2 practice data showed -70% delta (strong signal). V1 live data shows averages are IDENTICAL (W=0.39, L=0.39). Distribution has pockets (0.15-0.30 = 29% WR danger, 0.30-0.50 = 80% WR) but averages don't differentiate. Reduce scoring weight from ±15 to ±5. The signal is inconsistent between datasets and likely overfitting.
