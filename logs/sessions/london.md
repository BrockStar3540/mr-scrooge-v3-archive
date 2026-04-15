# London Session — Dev Log

**Window:** 07:00 - 16:00 UTC
**Primary Pairs:** EUR_USD, GBP_USD, EUR_GBP, EUR_JPY, GBP_JPY, EUR_CHF, GBP_CHF, EUR_CAD, EUR_AUD, EUR_NZD, GBP_CAD, GBP_AUD, GBP_NZD, USD_CHF, USD_JPY, AUD_CHF
**Liquidity:** High (peak during London-New York overlap 13:00-16:00)

---

## Historical Lessons (V1/V2)

### [UNDATED] [BOTH] — London spread is the baseline for spike detection
**Source:** ORIGINAL_CONFIG.md
**Type:** rule
**Detail:** Spread spike threshold = 4x London baseline. London session has the tightest spreads — anything 4x above London norms is a spike. This is the reference point for the spread gate's spike detection.

### [UNDATED] [BOTH] — Full sizing during London hours
**Source:** config, NOTES.md
**Type:** rule
**Detail:** London is a liquid session — no off-peak size reduction. When London is open, all pairs run at full position sizing including those that would be suppressed during thin sessions.

### [UNDATED] [BOTH] — First 30 minutes: highest activity
**Source:** MASTER_THEORY.md, Section 15
**Type:** rule
**Detail:** Per source theory: "The first 30 minutes of trading... that's where all the games get played." London open (07:00 UTC) is one of the most active windows. Sucker moves and liquidity sweeps are common. Do not chase the open — wait for confirmation.
