# Tokyo Session — Dev Log

**Window:** 00:00 - 09:00 UTC
**Primary Pairs:** USD_JPY, EUR_JPY, GBP_JPY, AUD_JPY, CAD_JPY, CHF_JPY, NZD_JPY, AUD_USD, NZD_USD, AUD_NZD
**Liquidity:** Thin (moderate for JPY pairs)

---

## Historical Lessons (V1/V2)

### [2026-03-31] [V2] — Off-peak session: 50% size reduction
**Source:** NOTES.md, config
**Type:** rule
**Detail:** Tokyo is classified as off-peak. 50% size reduction applied. Full sizing resumes when London opens (07:00 UTC) creating the London-Tokyo overlap.

### [UNDATED] [BOTH] — JPY pairs need wider execution parameters
**Source:** execution profiles (NOTES.md)
**Type:** rule
**Detail:** JPY crosses (GBP_JPY, CHF_JPY, NZD_JPY, AUD_JPY) use "wide" execution profile: 6 pip trigger, 2.0 offset, 7.0 fallback, 1.8x fast mult, 1.5 green offset. JPY pairs also need 2x proximity tolerance in the zone gate (0.50% vs 0.25% default).
