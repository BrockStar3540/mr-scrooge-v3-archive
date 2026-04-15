# management/position — Dev Log

> Position management: breakeven logic, trailing stop ratchet, TP harvesting, and multi-actor coordination.

---

## Historical Lessons (V1/V2)

### [2026-03-25] [V2] — Breakeven at +5 pips, not 50% of TP1
**Source:** NOTES.md
**Type:** lesson
**Detail:** Old trigger at TP1=10 meant BE at +2.5 pips — too tight. New: 50% ratchet at +10p triggers BE at +5p. SL target: entry + 1 pip buffer (spread-safe BE).

### [2026-03-25] [V2] — Adaptive ratchet lock: 55% pre-TP1, 75% post-TP1
**Source:** NOTES.md
**Type:** lesson
**Detail:** Fixed 80% -> 55% pre-TP1, 75% post-TP1. Early trades get room to breathe; confirmed moves get tighter protection.

### [2026-03-11] [V2] — Track peak prices every cycle
**Source:** DAILY_NOTES_2026-03-11
**Type:** rule
**Detail:** Added highest_price/lowest_price to OpenPosition. Essential for hybrid trailing stop (profit lock uses peak - entry).

### [2026-04-10] [BOTH] — Four-actor race condition: bot, ratchet, SL-limit, harvester
**Source:** known-defects.md, Defect 16
**Type:** bug
**Detail:** 4 independent actors modifying same trade's SL with no shared state. Contradictory stop movements and hidden P&L distortion. Fixed via TradeCoordinator sl_owner protocol. Harvester owns SL during T1-T3 partial phase, ratchet takes over after.

### [2026-04-14] [V2] — TP1 lost on restart
**Source:** known-defects.md
**Type:** bug
**Detail:** Reconciliation set TP1=0.0 because OANDA doesn't store TP1. Ratchet/BE ran blind. Fixed: persist TP1 in coordination file, recover on reconcile.

### [2026-04-14] [V2] — Harvester crash: trade_state mark_dead() had unquoted variable
**Source:** known-defects.md
**Type:** bug
**Detail:** Used bare client_id instead of "client_id" string in dict.get(). Caused 1900+ NameError crashes over 16 hours, zero profit harvesting.

### [2026-03-12] [V2] — No market exits: SL-advancement only
**Source:** DAILY_NOTES_2026-03-12
**Type:** lesson
**Detail:** Removed all reactive TP-setting and market-order exit logic. Trade management is SL-advancement only. OANDA's native GTC limit TP handles exit. Eliminates spread cost on all exits.

### [2026-04-12] [V2] — Win/loss asymmetry: need 75%+ WR
**Source:** NOTES.md
**Type:** discovery
**Detail:** Harvester takes small partials (1-8 pips), losses hit full stop (10-15 pips). Average loss >> average win. Need 75%+ WR to be net positive.

### [2026-03-12] [V1] — Sentinel field repurposing: partial_1_taken → SL advanced flag
**Source:** DAILY_NOTES_2026-03-12.md
**Type:** warning
**Detail:** Field `partial_1_taken` was repurposed from "partial close tracking" to "SL has been advanced to TP1" flag. No schema change needed but any code reading partial_1_taken must understand it means SL advanced, NOT an actual partial fill. V3 must use explicitly named fields — never repurpose.

### [2026-04-09] [V1] — Native close reconciliation: profitable skips cooldown, losses keep cooldown
**Source:** AUDIT.md
**Type:** rule
**Detail:** When OANDA closes a position natively (SL/TP hit between cycles), profitable closes skip cooldown, losses keep standard cooldown. Prevents punishing winning exits while maintaining protection after losses.

### [UNDATED] [BOTH] — Stagnant position timeout: 6 hours + 2 pip profit minimum
**Source:** harvester-operations.md (vault)
**Type:** rule
**Detail:** After 6 hours, if a position is profitable by at least 2 pips, the harvester sets a limit exit to free capital. Prevents capital lock-up in positions that aren't moving.

### [UNDATED] [BOTH] — Harvester tier configuration: T1=1.5% equity, T2=3.0%, T3=4.5%
**Source:** harvester-operations.md (vault)
**Type:** rule
**Detail:** Equity-percentage-based tiers: T1 closes 25% at 1.5% equity gain, T2 closes 25% at 3.0% (SL locks to T1), T3 closes 25% at 4.5% (SL locks to T2). 25% runner rides to native TP2. State persisted to harvester_state.json to prevent double-close on restart.

### [2026-03-12] [V1] — Hybrid trail formula: max(1H candle, 80% profit lock, 1.5x ATR)
**Source:** DAILY_NOTES_2026-03-12.md
**Type:** rule
**Detail:** Stage 3 trailing after break-even: max(hourly_candle_low, entry + 80% × peak_profit, peak − 1.5×ATR). For shorts: min() of mirror equivalents. Profit-lock + ATR activate only when profit > 1 ATR to avoid tightening early.
