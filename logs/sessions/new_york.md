# New York Session — Dev Log

**Window:** 13:00 - 22:00 UTC
**Primary Pairs:** EUR_USD, GBP_USD, USD_JPY, USD_CAD, USD_CHF, AUD_USD, NZD_USD, EUR_JPY, GBP_JPY, EUR_GBP, CAD_JPY, EUR_CAD, GBP_CAD
**Liquidity:** High (peak during London overlap 13:00-16:00, thins after 20:00)

---

## Historical Lessons (V1/V2)

### [UNDATED] [BOTH] — Peak liquidity during London-New York overlap
**Source:** session config, MASTER_THEORY
**Type:** rule
**Detail:** 13:00-16:00 UTC is the highest-liquidity window. Tightest spreads, most volume. Best conditions for entries. After 16:00 (London close), liquidity thins and spreads widen.

### [UNDATED] [BOTH] — Market closes Friday 22:00 UTC
**Source:** screener.py
**Type:** rule
**Detail:** Forex market closes Friday ~22:00 UTC, opens Sunday ~22:00 UTC. The bot must detect weekend and suspend scanning. V2 bug: is_weekend() check was in the run loop but some edge cases around Friday close were handled late.

### [UNDATED] [BOTH] — New York open can create opening gaps
**Source:** MASTER_THEORY Section 15
**Type:** rule
**Detail:** Gap behavior at New York open: gap up above PDH → usually retests gap area before continuing. Gap down below PDL → usually retests. Dead-center open → wait for edge test. Do not blindly buy/short the open.
