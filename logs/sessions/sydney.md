# Sydney Session — Dev Log

**Window:** 21:00 - 06:00 UTC (crosses midnight)
**Primary Pairs:** AUD_USD, NZD_USD, AUD_NZD, AUD_CAD, AUD_JPY, NZD_JPY
**Liquidity:** Thin

---

## Historical Lessons (V1/V2)

### [2026-03-31] [V2] — Spread spikes common on Sunday open
**Source:** NOTES.md
**Type:** lesson
**Detail:** Single-candle spread spikes are common when Sydney opens on Sunday. These are transient and do NOT indicate hostile market conditions. The 2-scan consistency gate (spread must exceed threshold on 2 consecutive scans = 10 minutes) prevents false blocks from these spikes.

### [2026-03-31] [V2] — Off-peak session: 50% size reduction applied
**Source:** NOTES.md, config
**Type:** rule
**Detail:** Sydney is classified as off-peak (thin session). Entry planner applies 50% size reduction for all entries during Sydney-only hours. When London or New York are also open (overlap periods), full sizing resumes.

### [2026-03-31] [V2] — Probation pairs suppressed in balanced mode
**Source:** NOTES.md
**Type:** rule
**Detail:** In balanced screener mode, probation pairs (AUD_USD, NZD_USD, etc.) are suppressed when only thin sessions (Sydney/Tokyo) are open. This was later replaced by aggressive mode + regime scoring, but the lesson remains: thin-session pairs need extra filtering.
