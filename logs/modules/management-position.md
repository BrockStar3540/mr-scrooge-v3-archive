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

### [2026-04-10] [BOTH] — Harvester entries are reactive, not proactive
**Source:** Dropbox: 2026-04-10_54314085.md
**Type:** discovery
**Detail:** Harvester places TP1/TP2 limits only AFTER bot detects price passed those levels (polls every 30 sec). By the time the limit is created, price has already moved past — limit fills immediately at market, not at target. Pre-placing harvester limits before entry would capture true TP levels and avoid taker spread.

### [2026-04-10] [BOTH] — Harvester tier transitions not synced to bot
**Source:** Dropbox: 2026-04-10_54314085.md
**Type:** bug
**Detail:** Harvester tracks tiers_hit in its own state file; bot uses partial_1_taken as sentinel for "TP1 passed." If harvester takes T1 before ratchet detects TP1, ratchet's Stage 2 never fires. Breaks staged SL progression. Fix: shared coordination state, not dual-tracking.

### [2026-03-11] [BOTH] — Green exit (TP1) placement timing: FOK rejected
**Source:** Dropbox: 2026-03-11_d66ae964.md
**Type:** bug
**Detail:** Setting TP1 limits reactively after BE achieved — price may have already passed. FOK (fill-or-kill) order rejected with "would trigger immediately." Fix: place TP1 as standing GTC limit at entry time, not reactively after breakeven. Never use FOK for TP orders.

### [2026-04-16] [V3] — Ratchet bypass bug: spread adjustment loosened stops
**Source:** Live trade observation — trade went green then back to red
**Type:** bug
**Detail:** Trail/ratchet correctly proposed a tighter stop, and should_trail() confirmed it was tighter. But validate_stop() then adjusted it for spread safety (no-man's-zone guard), computing min_safe = ask + spread + pip*2. This value fluctuates every tick and could be LOOSER than current_stop. The loosened value was submitted to OANDA, defeating the ratchet. Fix: added final guard in runtime.py after validate_stop() — if the validated stop would loosen the position (lower for longs, higher for shorts vs current_stop), the update is skipped and native SL stays. Confirmed working via logs showing "SL trail SKIPPED (spread adjustment would loosen)" entries.

### [2026-04-16] [V3] — Stop persistence bug: update_stop() didn't persist to disk
**Source:** Code review during ratchet investigation
**Type:** bug
**Detail:** PositionTracker.update_stop() updated pos.current_stop in memory but never called self.persist(). On restart, positions.json had the old stop value. Bot would trail from the stale (worse) stop, potentially re-loosening. Fix: added self.persist() to update_stop(). Now every SL change is immediately written to positions.json.

### [2026-04-16] [V3] — Ratchet and BE thresholds tuned
**Source:** Brock request
**Type:** config
**Detail:** Old defaults: ratchet_min_profit_pips=10, be_trigger_pips=15. Problems: (1) BE at 15 was higher than ratchet at 10, so BE never fired (ratchet already moved SL past entry by then). (2) At +5 pips profit, nothing protected the gain — trade could slide all the way back to original SL. New config (in config/default.json management section): ratchet_min_profit_pips=6, be_trigger_pips=5, be_offset_pips=1. Sequence: at +5 pips BE moves SL to entry+1pip. At +6 pips ratchet locks 50% (SL to entry+3). Continues locking 50% as profit grows, keeping half the room open for the trade to run.
