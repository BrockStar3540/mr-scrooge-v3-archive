# gates/zone_proximity — Dev Log

> Zone proximity gate: validates that price is close enough to a liquidity zone to warrant entry.

---

## Historical Lessons (V1/V2)

### [2026-03-11] [V2] — JPY pairs need 2x proximity tolerance
**Source:** gates/zone_gate/NOTES.md
**Type:** rule
**Detail:** Standard pairs use 0.25% (0.0025). JPY crosses should use 0.50% proximity due to wider normal trading range.
