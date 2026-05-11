# Trading Bot Exec Summary V11 — Faithful Extraction

**Source:** `/Users/brock-mini-mac/Desktop/trading_bot_exec_summary_v11.docx`
**Recovered:** 2026-05-11
**Original date:** Feb 26, 2026 (per opening line)
**Status:** Historical V1-era doctrine document. Preserved verbatim before original was trashed.

---



## 1. Current Deployment State
As of February 25, 2026, the following table reflects actual live status — which differs from earlier planned states documented during development.






## 2. Box Theory — Core Philosophy
Box theory is built on one observation: price does not move randomly. Every day, price establishes a range based on the prior session's activity. The edges of that range — the prior day's high and low — are not arbitrary. They are levels where the market previously found rejection. Institutional participants remember those levels. Retail participants do not.

The strategy exploits a predictable behavioural pattern: when price reaches the top or bottom of the prior day's range, retail traders see a breakout and chase. Institutional traders see a liquidity zone and fade. The bot enters with the institutions, not against them.


The center of the box has no edge. Price is genuinely uncertain there — it could go either way, overhead costs are not justified, and there is no confluence. Waiting for price to reach a wall is not patience, it is discipline with a mathematical basis.

### 2.1 Why This Works
Prior highs and lows are liquidity magnets. Stop orders cluster just beyond them.
When price reaches those levels, it triggers stops on both sides, creating a brief spike followed by a reversal.
That spike — the sucker move — is the entry signal. It looks like a breakout to retail. It is a liquidity sweep to institutions.
The bot enters the reversal with a defined stop, defined target, and positive expected value because the probability of return-to-centre is statistically significant at these zones.


## 3. Why the Bots Are Not Trading Yet
Both Scrooge and Sprite are running and scanning every 5 minutes. No trades have fired. This is not a malfunction — it is the strategy working correctly. The bots will not trade bad conditions.

### 3.1 Scrooge (Forex) — Status & Trade Audit
After the universe was expanded to 24 pairs, a second diagnostic pass found that the OANDA candle fetcher was filtering out the current forming bar, making ATR consumed always appear 100–120%. Removing that filter made 12/24 pairs viable immediately. Limit orders were also being rejected (WOULD_TRIGGER_IMMEDIATELY) — switched to OANDA market orders with TP+SL on fill. A missing register_entry call caused repeated entries on the same signal each cycle; a duplicate-entry guard was added. The open wait was also resetting on every bot restart (session_start = datetime.now()). A _compute_session_start() function was added to derive the actual session open time from SESSION_WINDOWS.
Further audit of the market order path (referencing Mr. Burns’ working OANDA client) found three more issues: missing timeInForce: FOK and positionFill: DEFAULT fields, units sent as float strings (“-2430.0” vs “-2430”), and clientExtensions used at order level instead of tradeClientExtensions. All three were corrected. OANDA was also rejecting orders with STOP_LOSS_ON_FILL_LOSS when price moved past the stop level between signal fire and order placement — a staleness check was added: if current price is at or beyond the stop, skip entry.

Signal Audit — AUD_USD SHORT (cd3095a5)
All six gates were independently verified using OANDA candle data.

What Actually Happened — Trade Timeline

Issues Found in Audit — All Resolved

### 3.2 Sprite (Crypto) — Status & First Trades
Sprite had a different root cause: zone_proximity_pct was using the forex default of 0.3%. Crypto pairs need 1.5%. ATOM at $1.942 with PDL at $1.929 (0.67% away) was failing the zone gate every cycle. After widening the threshold, a second set of issues appeared: cl_ord_id rejection, position size overflow (tight stops on low-priced coins generating 1,000–3,000 unit orders on a $785 account), post-only orders never filling at zone entry, and Kraken price precision rejection on slippage-buffered prices. All were fixed. See Section 11.2 for full details.


### 3.3 Status as of Feb 26, 2026 ~05:30 UTC


## 4. The Three-Timeframe System
The strategy requires three timeframes simultaneously. Each has a distinct and non-interchangeable role. Using only one or two misses essential context.



### 4.1 High Volatility Exception
During extreme volatility (flash crashes, major news), the 5-minute pitchfork may not be reliable. In these conditions, entering directly on a 1-hour pitchfork is acceptable. Stops are proportionally larger but the signal is cleaner. Position sizing adjusts automatically for the wider stop.


## 5. Magic Lines — The Hourly Zone Map
Within the box there are higher-quality zones where institutional orders concentrate. These are identified on the 1-hour chart and ranked by quality.

### 5.1 Zone Types

### 5.2 Breakout Polarity Flip — The Highest Quality Zone
When price breaks through a prior high, that level flips polarity. What was resistance becomes support. When price returns to test the broken level from above, two independent reasons exist for it to hold: it was prior resistance, AND it was a breakout level. This combination is the strongest possible zone in the system.


### 5.3 Zone Tier Rankings


## 6. The Sucker Move
The sucker move is a behavioural event. It describes what happens when retail traders chase a strong directional move into a zone, becoming the liquidity that institutional orders need to fill their opposing positions. The bot does not enter during the move. It waits for the move to terminate at the zone, then enters the reversal.



### 6.1 ATR Dual-Threshold Logic
Two distinct thresholds. They answer different questions and must not be confused with each other.



## 7. Pitchfork Entry Signals
After the sucker move terminates at a magic line, a reversal candle must appear before entry. Three named variants, in priority order:

### 7.1 John Wick
Wick must be 60%+ of total candle range
Body must be 30% or less of total range
Wick must be at least 2x the size of the body
Long wick points in the direction of the rejected move
What this represents: price moved hard in one direction, completely rejected that move, and closed in the opposite direction. The wick represents trapped traders whose stop losses become fuel for the reversal.

### 7.2 Power of Towers
A full engulfing candle where the second candle completely engulfs the first including the wicks. Not just body-to-body — the wicks must be fully contained.
What this represents: in a single candle, the market erased everything the prior candle did and went further. Institutional volume overwhelmed retail direction completely.

### 7.3 Standard Pitchfork
Three to five strong directional candles in the direction of the sucker move, followed by the first candle that closes in the opposite direction. Valid signal but requires strong zone and ATR backing. Not sufficient alone at marginal OTR levels.

### 7.4 Entry Mechanics



## 8. Six-Gate Signal Confirmation
Every potential trade passes through six sequential gates. A failed gate immediately rejects the setup and logs the reason. No discretion, no overrides.


All six gates are implemented as designed. Gate 4 enforces sucker move termination at a pre-identified zone. Gate 5 uses a waiting limit order that cannot fill unless price subsequently breaks the pitchfork level.


## 9. Session Timing Rules

### 9.1 The Open Market Wait (15–20 Minutes)
No new entries in the first 15–20 minutes after market open. Three reasons:
Spread is elevated. Market makers widen spreads during chaotic open conditions. The OTR ratio fails on setups that would be valid 20 minutes later.
Direction has not been established. Price often moves both ways in the first few minutes as overnight orders clear. A sucker move at open may be genuine continuation.
Volume is asymmetric. Large orders from overnight accumulation clear at open. Price action is not representative of the session's actual supply and demand.

Open Wait Exception
If all six gates align AND the setup is Tier 1 zone + 80%+ ATR + John Wick or Power of Towers, entry is permitted at 50% position size during the open wait window. All other setups are flat-rejected until the wait expires.

### 9.2 Gap Handling at Open
If today's opening price gaps more than 0.5% outside the prior day's box, zone_detector.py redraws the box at boot before the first candle is evaluated:
Gap up above PDH: new ceiling = session high. New floor = PDH (prior resistance becomes new support — polarity flip).
Gap down below PDL: new ceiling = PDL (prior support becomes new resistance). New floor = session low.
Cheat code: Session High to Session Low. Use when both walls are broken or for simplification.


## 10. Trade Management After Entry
Entry is the least important part of the trade. Management determines whether a winning setup produces profit. Core philosophy: pay yourself along the way. Take partial profits at each significant level, reduce risk continuously, let the remaining position trail with no manual intervention.


### 10.1 Scaling-Out Sequence

### 10.2 Time Exit Rule
The 30-minute clock only applies to trades that have not yet reached TP1. If TP1 has been hit, the time exit is disabled for that trade and the trailing stop runs the position to completion.


### 10.3 Re-Entry Protocol
If stopped out at or near break-even at a valid zone, one re-entry is permitted per setup. This handles the institutional stop-hunt pattern: price tags the stop level, triggers a wave of stop losses to provide liquidity, then reverses sharply in the original direction.
Zone must still be valid (same magic line, price has not moved materially past it)
Liquidity sweep pattern must be detectable (the stop-hunt candle is confirmation, not failure)
Maximum one re-entry per setup. If the second entry is also stopped out, the zone has failed. Stand aside.
Re-entry bypasses the concurrent position cap — it is the same setup continuing, not a new one.


## 11. Code Audit — All Items Resolved
A formal code audit against the design specification identified nine items. Seven were code fixes. Two were non-issues on closer inspection — the implementation already matched the spec intent when examined at the code level. All nine are closed.



### 11.1 Summary of Changes
Seven code changes were applied across four files, then both bots restarted and verified clean:
signal_engine.py — Sucker move termination at zone now enforced (fix #2)
zone_detector.py — Tier 1 requires daily alignment only, no test count (fix #5). Gap detection at boot redraws box proactively (fix #7).
trade_manager.py — Time exit only fires before TP1. Trailing winners after TP1 run free (fix #4).
main.py (both bots) — New box trade counter increments on every close (fix #8). Re-entry wired in via assess_reentry() on break-even stops (fix #9). Open wait exception at 50% size for Scrooge (fix #6).

## 11.2 Second Audit — Live Deployment Issues
After deployment, no trades appeared across either bot. A second diagnostic pass traced the full execution path and found 12 additional issues. All are now resolved.


## 11.3 Third Audit — First Live Session Issues
After the first trades were placed, a full trade audit was conducted using live OANDA data. Signal math was confirmed correct across all 6 gates. Several additional execution bugs were found and fixed.



## 12. Trading Overhead & the OTR Ratio
The OTR ratio (Overhead-to-Range) determines whether a trade has positive expected value after all costs. It matters more here than in futures-based implementations because forex and crypto costs are higher relative to a typical move.




### 12.1 Cost Structures by Exchange

### 12.2 Per-Pair Baseline Spreads
Each pair has an individually calibrated baseline spread in the fee calculator. Spike detection and OTR estimates use the pair-specific baseline rather than a generic default. This matters most for crosses: a 4-pip spread on GBP/NZD requires a much wider box to clear than a 1.1-pip spread on USD/JPY.



### 12.3 OANDA Spread Multipliers by Session

### 12.4 Kraken Fee Tiers


## 13. Box Lifecycle
### 13.1 Box State Machine

### 13.2 Alternative Box Drawing
Broke up: new top = session high. New bottom = PDH (old top becomes new bottom — polarity flip).
Broke down: new bottom = session low. New top = PDL (polarity flip).
Cheat code: Session High to Session Low. Use when both walls are broken or for simplification.
Pick whichever alternative gives the best OTR efficiency. Run OTR check before committing to it.

### 13.3 New Box Confidence

### 13.4 Box Age Decay


## 14. Mr. Burns — Volatility Breakout Strategy
Mr. Burns uses a fundamentally different approach: he chases confirmed breakouts from compression patterns. He does not fade extremes. Where the box theory bots wait for a wall and reversal, Burns waits for price to compress into a tight range and then explode.


### 14.1 Capital Deployment Rules
Maximum 80% of account equity deployed at any time
20% held in reserve for high-conviction breakout signals (score > 0.80)
At 80% deployed: only breakout signals can open new positions. Momentum signals skip.


## 15. System Architecture

### 15.1 Per-Candle Data Flow


## 16. Risk Management
### 16.1 Risk Parameters

### 16.2 Lestat Authority Matrix

### 16.3 Alert Triggers
Any bot not running when expected
Daily loss limit hit
Emergency market exit taken (taker penalty logged)
Combined OANDA margin (Burns + Scrooge) exceeds 60% of equity
Kraken API auth or rate limit error
Box broken on 3+ instruments simultaneously
Any config file hash changes without expected modification
Any DISABLED bot shows a launchctl PID (unauthorized boot)

### 16.4 Trading Universes
The universe screener evaluates every candidate pair on each 30-minute cycle. Being on the list does not guarantee a trade — the OTR ratio, ATR gate, and zone quality gates still apply. Per-pair baseline spreads are individually calibrated in the fee calculators so spike detection and OTR estimates are accurate for every instrument.

Mr. Scrooge — 24 Forex Pairs (OANDA)

Mr. Sprite — 20 Crypto Pairs (Kraken)


End of document.

### Table 1

| TRADING BOT ECOSYSTEM Executive Summary Mr. Burns  ·  Mr. Scrooge  ·  Mr. Sprite  ·  Mr. Wonderful |


### Table 2

| Classification: Internal. February 2026. Rocky Mount, NC. |


### Table 3

| Bot | Exchange | Strategy | Live Status | Account Floor |
| Mr. Burns | OANDA | Volatility breakout | LIVE — active | $750 |
| Mr. Scrooge | OANDA | Box theory reversal | LIVE — scanning | $500 (revised from $750) |
| Mr. Sprite | Kraken | Box theory reversal | LIVE — scanning | $500 |
| Mr. Wonderful | Kraken | Independent | OFFLINE | N/A |


### Table 4

| Note: Scrooge and Sprite are both live and running but have not yet taken trades. This is expected behaviour — no valid setups have formed since launch. See Section 3 for why. |


### Table 5

| BROCK  —  Final Authority | BROCK  —  Final Authority | BROCK  —  Final Authority | BROCK  —  Final Authority |
| ▼ | ▼ | ▼ | ▼ |
| LESTAT  —  Primary OpenClaw Agent (GPT / Slack) | LESTAT  —  Primary OpenClaw Agent (GPT / Slack) | LESTAT  —  Primary OpenClaw Agent (GPT / Slack) | LESTAT  —  Primary OpenClaw Agent (GPT / Slack) |
| ▼  ▼  ▼  ▼ | ▼  ▼  ▼  ▼ | ▼  ▼  ▼  ▼ | ▼  ▼  ▼  ▼ |
| CLAUDIA Slack Listener | SMITHERS Burns Monitor | AUSTIN Indeed Recruiter | Watchdog TBD Sprite Monitor |
| ▼  ▼  ▼  ▼ | ▼  ▼  ▼  ▼ | ▼  ▼  ▼  ▼ | ▼  ▼  ▼  ▼ |
| MR. BURNS OANDA Breakout | MR. SCROOGE OANDA Box Theory | MR. SPRITE Kraken Box Theory | MR. WONDERFUL Kraken [Offline] |


### Table 6

| IMPORTANT: Mr. Burns and Mr. Scrooge share the same OANDA account. Lestat monitors combined margin across both bots every hour. Alert threshold: 60% combined equity. |


### Table 7

| "Do not diddle in the middle." Only trade the box walls. Never enter in the center of the range. |


### Table 8

| Gate | Check | Values | Result |
| Daily Box | PDH / PDL / ATR(14) | PDH: 0.71260 | PDL: 0.70574 | ATR: 58.9 pips | ✅ Correct |
| Gate 1 Zone | Price within 0.3% of PDH | Entry 0.71229, PDH 0.71260 — distance 0.044% | ✅ Pass |
| Gate 2 Middle | Sell threshold = PDL + range x 80% | Threshold: 0.71122. Price above → sell zone. | ✅ Pass |
| Gate 3 ATR | Session range vs ATR minimum | 18.1 pips / 58.9 pips = 30.7% > 20% min | ✅ Pass (weak strength) |
| Gate 4 Sucker | 3-5 consecutive green candles to PDH | 5 green candles 03:10–03:30 UTC. Peak 0.71281 = 0.029% from PDH | ✅ Pass |
| Gate 5 Fork | Power of Towers confirmation | Engulf candles at 01:55/02:00 UTC. Trigger: 0.71259. Stop: 0.71342 | ✅ Pass |
| Gate 6 OTR | (spread x 2) / half-box | (0.00013 x 2) / 0.00343 = 7.6% → acceptable | ✅ Pass |
| Position Size | Box age 7.07h → 50% confidence | units = round(($730 x 1%) / 0.00083 x 0.50) = 4,381 | ✅ Correct |


### Table 9

| Signal calculation is correct. All six gates were independently verified. Losses from this session were caused by restart stacking (bug), not by bad signal logic. |


### Table 10

| UTC | Event |
| 21:48 | Bot starts (restart #1). trade_manager empty. |
| 21:48–21:58 | Signal fires but open wait blocks entry. |
| 22:03 | Open wait expires. Trade 1 fills: 4,860u @ 0.71032, SL 0.71182. |
| 22:08 | Trade 2 fills: 4,860u @ 0.71032. ⚠️ No duplicate-entry guard yet. |
| 22:13 | Trade 3 fills: 4,860u @ 0.71032. |
| 22:14 | Bot restarts (restart #2). trade_manager wiped. 3 live OANDA positions unknown to bot. |
| 22:24–22:37 | Trades 4–7 fill: 2,430u each. Bot registers none after restart. |
| 22:56 | 7 positions stopped out at SL 0.71182. Estimated loss: ~$36. |
| 22:59 | Staleness check fires: price 0.71232 at/above stop 0.71182. Entry blocked. |
| 23:04 | NEW signal with new stop 0.71342. Trade 8 fills: 4,381u @ 0.71229 (cd3095a5). ✅ |
| 23:34 | Time exit fires on cd3095a5 (30-min limit). 1 second later: Trade 9 enters on same signal. |
| 23:39 | AUD_JPY signal fires. Trade 10: 5,296u @ 111.194, SL 111.305, TP 110.727. |


### Table 11

| Issue | Fix Applied | Status |
| Restart position detection — bot re-entered all live positions after restart (caused ~$36 loss) | boot() now calls oanda.get_open_trades() then trade_manager.reconcile_from_oanda(). Finds any scrooge-* tagged trades and re-populates trade_manager with correct data. position_count starts at reconciled count, not 0. Verified live: 2 positions correctly detected on restart. | ✅ Fixed |
| Time exit immediately re-entered same signal | 60-minute cooldown added per symbol. When a time exit fires, ctx[time_exit_cooldowns][symbol] = now + 60min. Gate blocks re-entry until cooldown expires. decisions.log shows: Time-exit cooldown active until HH:MM UTC. | ✅ Fixed |
| move_stop() broken — wrong arg count + wrong OANDA ID | place_entry_order() now extracts orderFillTransaction.tradeOpened.tradeID and returns it as oanda_trade_id. OpenPosition has new oanda_trade_id field. move_stop call fixed to (pos.trade_id, pos.oanda_trade_id, price, reason). reconcile_from_oanda() also captures OANDA numeric ID for existing positions. Stop trailing and break-even now fully functional. | ✅ Fixed |


### Table 12

| All three open issues resolved. Verified live against OANDA: reconciliation detected both open positions (AUD_USD trade 739, AUD_JPY trade 731) correctly on restart. Bot no longer stacks entries after restarts, no longer re-enters after time exits, and stop management is now fully wired. |


### Table 13

| First Sprite trade: ATOM/USD BUY 86.22 units @ $1.948 — Kraken order OPNFR3-GMTNS-WMPHJC. Signal: power_of_towers. Position capped at $251 (90% of $274 available USD). |


### Table 14

| Bot | Status | Account | Position | Notes |
| Mr. Scrooge | LIVE — trading | OANDA $728.02 | AUD/USD SHORT — trade 749, entered 05:30 UTC | Stacking fix confirmed: 1 position only. AUD/JPY signal correctly rejected as stale. |
| Mr. Sprite | LIVE — scanning | Kraken $767.32 | No open positions — 18 pairs in watch mode | ATOM position liquidated and account reset to $767 USD cash. Per-symbol entry guard added. |
| Mr. Burns | LIVE — active | OANDA (shared) | — | Operating independently on shared OANDA account. |
| Mr. Wonderful | OFFLINE | — | — | — |


### Table 15

| Both bots running clean as of 05:30 UTC Feb 26. Restart stacking fix verified in production: Scrooge entered exactly 1 AUD/USD position and did not re-enter. All 29 bugs from three audit passes are resolved. |


### Table 16

| Timeframe | Role | What You Are Looking For | Duration |
| Daily | CONTEXT | Prior Day High, Prior Day Low, ATR for the session, box dimensions | Reference all day |
| 1-Hour | PRIMARY | Magic lines (pivot zones, breakout flips), Tier rankings, post-entry management | PRIMARY working chart. Return here after every entry. |
| 5-Minute | TIMING | Pitchfork confirmation candle, exact entry trigger, stop placement | Entry only. Switch back to hourly immediately after. |


### Table 17

| The 5-minute chart is for timing only. After entry, switch immediately to the 1-hour and do not return to the 5-minute to manage the trade. Managing on the 5-minute creates noise-driven exits from trades that are actually working on the hourly. |


### Table 18

| Zone Type | Definition | Why It Matters |
| Prior hourly highs/lows | Significant pivot points on the 1-hour chart | Price has already reacted here. That reaction leaves unfilled orders. |
| Breakout flip levels | Old resistance broken → price returns to test from above (or vice versa) | Highest quality zone. Double confluence: breakout + retest validation. |
| Multi-test levels | Same price area tested 3+ times on the hourly | More tests = more orders sitting there = stronger expected reaction. |
| Round number alignment | Zone near a psychological level (25,000 / 6,800 / 1.2000) | Retail orders cluster at round numbers. Adds liquidity depth. |


### Table 19

| Old resistance broken → price rallies → price pulls back to test the breakout level from above → holds as support. This is a polarity flip. Tier 1 or 2 zone. Enter with maximum confidence. |


### Table 20

| Tier | Definition | Confidence | Maximum OTR |
| Tier 1 | Hourly zone aligns with daily PDH or PDL (daily proximity alone qualifies) | Highest | 15% |
| Tier 2 | Breakout flip OR 3+ hourly tests | High | 15% |
| Tier 3 | Hourly pivot tested twice | Moderate | 10% |
| Tier 4 | Single untested hourly pivot | Low | 5% (excellent OTR only) |


### Table 21

| Three conditions. All three required simultaneously. Any one missing = no trade. |


### Table 22

| Condition | Requirement | Reasoning |
| Speed | 3–5 candles, no meaningful pullbacks | Retail does not chase slow drift. The explosive move is what creates the fear-of-missing-out buying/selling that generates the liquidity trap. |
| ATR Consumption | 60%+ of the daily ATR consumed by the move | The session must have used most of its expected range. At 60%+, the move is statistically extended and reversal probability is elevated. |
| Termination Point | Move ends AT a pre-identified magic line | The zone must be drawn before the move. If you draw the zone after seeing the reversal, it is hindsight. Institutional orders were already sitting there. |


### Table 23

| Threshold | Value | Question It Answers |
| Minimum | < 20% consumed | Is there a setup forming at all? No — session has barely moved. Ignore entirely. |
| Watch zone | 20–59% | Getting interesting. Monitor but do not enter. Keep alerts. |
| High confidence | 60–79% | Is the move statistically extended enough to fade? Yes — normal entry rules apply. |
| Maximum strength | 80%+ | Highest probability reversal. Can override marginal OTR requirements. |


### Table 24

| How the limit order approach implements the spec intent: a limit order placed at the pitchfork extreme + buffer cannot fill unless price subsequently moves through that level — mechanically identical to waiting for the next candle to break the pitchfork high or low. |


### Table 25

| Step | Behaviour |
| Signal identified | Pitchfork candle closes |
| Entry order | Limit order placed at pitchfork extreme + small buffer. Sits waiting. Cannot fill unless price moves past the level on a subsequent candle. |
| Order type | Always limit. Never market on entry. |
| Stop placement | Beyond the opposite extreme of the pitchfork candle |
| Timeout | Cancel unfilled limit after 5 minutes. Do not chase. |


### Table 26

| GATE 1 — ZONE CHECK Is price within 0.3% of a pre-identified magic line? |
| ▼ |
| GATE 2 — MIDDLE FILTER Is price in the middle 40% of the box? If yes → reject immediately. |
| ▼ |
| GATE 3 — ATR FILTER Has 60%+ of daily ATR been consumed? (Session range ÷ daily ATR) |
| ▼ |
| GATE 4 — SUCKER MOVE Fast 3-5 candle approach AND terminates at a pre-identified magic line? |
| ▼ |
| GATE 5 — PITCHFORK Reversal candle present? Limit order waits at extreme for subsequent break. |
| ▼ |
| GATE 6 — OTR RATIO Is overhead < 15% of half-box potential? |
| ▼ |
| ALL GATES PASSED → SIZE POSITION → PLACE LIMIT ORDER |


### Table 27

| After entry: switch immediately to the 1-hour chart. Never return to the 5-minute to manage the trade. |


### Table 28

| ENTRY — Limit order fills at trigger price. Switch to 1-hour chart immediately. |
| ▼ |
| TP1 — First magic line between entry and box centre. Close 40% at limit. "Paying myself" — locking in real profit, reducing exposure. |
| ▼ |
| STOP TO BREAK-EVEN — Move stop to entry price immediately after TP1. Trade is now risk-free. Worst case from here: scratch. |
| ▼ |
| TP2 — Next magic line toward centre. Close another 40%. 80% of position now closed at profit. |
| ▼ |
| TRAIL REMAINING 20% Move stop below each completed hourly candle low (longs) or above each hourly candle high (shorts). |
| ▼ |
| TRAILING STOP HIT → Final exit. Trade complete. |


### Table 29

| Condition | Behaviour |
| TP1 not hit after 30 minutes | Exit at market. Setup did not deliver follow-through. Move on. |
| TP1 already hit, running trailing stop | Time exit disabled. Position trails until stop is hit. Clock is irrelevant. |


### Table 30

| Both bots were restarted after fixes and confirmed clean boot. The strategy is now running as designed. |


### Table 31

| # | Issue Identified | Resolution | Status |
| 1 | Entry timing — pitchfork close vs next candle break | Non-issue on inspection. Limit order placed at pitchfork extreme + buffer cannot fill unless price subsequently moves past that level. Mechanically identical to spec intent. | ✅ Closed |
| 2 | Sucker move termination not enforced | Fixed: signal_engine.py now rejects any sucker move that does not terminate at a pre-identified magic line. | ✅ Fixed |
| 3 | ATR measurement — session span vs directional leg | Non-issue on inspection. Session high − low ÷ daily ATR correctly measures how much of the expected daily range has been consumed. Slightly more conservative than a single directional leg. Defensible as-is. | ✅ Closed |
| 4 | Time exit fires at 30 min even after TP1, cutting trailing runners | Fixed: trade_manager.py time exit now only fires if TP1 has not yet been hit. Trailing winners after TP1 run until stopped out. | ✅ Fixed |
| 5 | Tier 1 zone required 2 tests — spec says daily alignment alone qualifies | Fixed: zone_detector.py Tier 1 condition is now daily_aligned only, no test count required. | ✅ Fixed |
| 6 | No open wait exception for perfect setups at 50% size | Fixed: main.py (Scrooge) allows entry at 50% size when Tier 1 + 80%+ ATR + John Wick or Power of Towers aligns during open wait. Sprite is 24/7 — open wait does not apply. | ✅ Fixed |
| 7 | Gap handling — >0.5% gap triggered reactive alt-box instead of proactive rebuild | Fixed: zone_detector.py detects gap at boot and redraws immediately. Gap up: ceiling = session high, floor = prior PDH. Gap down: ceiling = prior PDL, floor = session low. | ✅ Fixed |
| 8 | new_box_trades counter never incremented — alt boxes permanently at 50% size | Fixed: main.py (both bots) calls record_new_box_trade_result() on every close. Bot advances 50% → 100% size after 3 wins on the alternative box. | ✅ Fixed |
| 9 | assess_reentry() built but never called from main.py | Fixed: main.py (both bots) queues a re-entry when stopped at break-even and calls assess_reentry() on the next evaluation cycle. | ✅ Fixed |


### Table 32

| # | Bot | Bug | Root Cause | Fix | Severity |
| 1 | Scrooge | ATR gate always failed | OANDA candle fetcher filtered out the current forming bar. ATR consumed vs a fully-formed daily candle = 100–120% every cycle. | Removed complete=False filter. 12/24 pairs viable on next scan. | Critical |
| 2 | Scrooge | Limit orders rejected by OANDA | WOULD_TRIGGER_IMMEDIATELY: limit placed at current market price triggered instant fill rejection. | Switched to OANDA market orders with TP+SL on fill. Only cost is spread, already in OTR. | Critical |
| 3 | Scrooge | Same position entered every 5 min | register_entry never called after fill. No record of open positions. Duplicate-entry guard missing. | Added register_entry call. Added per-symbol position check before entry. | Critical |
| 4 | Scrooge | Open wait reset on every restart | session_start = datetime.now() at boot. Every restart treated as market just opened. | Added _compute_session_start() reading SESSION_WINDOWS to derive actual session open time. | High |
| 5 | Sprite | Zone gate always failed | zone_proximity_pct was 0.3% (forex default). Crypto needs 1.5%. ATOM at 0.67% from PDL failed every cycle. | zone_proximity_pct: 0.015. sucker_zone_tolerance: 0.015. | Critical |
| 6 | Sprite | Sucker move lookback too short | lookback = sucker_max_candles + 3 = 8 bars. A sucker move from 45 min ago (9 bars) was invisible. | Lookback extended to 20 bars (100 min of 5M history). | High |
| 7 | Sprite | Sucker move terminus wrong bar | move_end = bars.iloc[-2] always. Used the second-to-last bar regardless of where the move peaked. | move_end = max(high) across the actual directional candles in the identified move. | Critical |
| 8 | Sprite | cl_ord_id rejected by Kraken | Kraken returned EGeneral:Invalid arguments:cl_ord_id. The field is optional. | Removed cl_ord_id from order payload. Kraken txid used for tracking. | High |
| 9 | Sprite | Position size overflow | Tight stops on low-priced coins produced 1,000–3,000 unit orders on a $785 account (EOrder:Insufficient funds). | Cap: quantity limited to 90% of live USD balance or $500, whichever is less. get_usd_balance() called before every entry. | Critical |
| 10 | Sprite | Post-only orders never filled at zone | oflags:post caused Kraken to reject any order that would execute as taker. Signal at zone level = taker fill = rejected. | Removed post flag. Added 0.15% slippage buffer to limit price. OTR updated to use taker_rate. | Critical |
| 11 | Sprite | Price precision rejection | ATOM slippage-adjusted price rounded to 6 decimals. Kraken max is 4 for ATOM. | Decimal count = max(1, min(5, 4 - floor(log10(price)))). Dynamic per-pair precision. | Medium |
| 12 | Both | Too few pivots, stale zones | Hourly bar fetch was count=50. Only 2 days of levels. pivot_lookback_bars=5 too restrictive for fast-moving crypto. | count=100 (4 days). pivot_lookback_bars=3 for Sprite. hourly_bars_back: 96. | Medium |


### Table 33

| # | Bot | Bug | Root Cause | Fix | Severity |
| 13 | Scrooge | Market orders not filling — missing FOK/positionFill | OANDA market orders require timeInForce: FOK and positionFill: DEFAULT. Missing fields caused silent rejection. Discovered by comparing to Mr. Burns’ working order client. | Added timeInForce: FOK and positionFill: DEFAULT to all market order payloads. | Critical |
| 14 | Scrooge | Units sent as float string | str(-2430.0) sent instead of str(-2430). OANDA rejected with STOP_LOSS_ON_FILL_LOSS or silent rejection. | units = int(round(units)). Applied to both place_entry_order and place_market_order. | Critical |
| 15 | Scrooge | clientExtensions at wrong level | clientExtensions is an order-level field. Trade metadata requires tradeClientExtensions. Bot’s trade ID was invisible to OANDA’s trade lookup. | Changed to tradeClientExtensions in place_entry_order. | High |
| 16 | Scrooge | No boot-time position sync from OANDA | trade_manager starts empty on every boot. Bot does not query OANDA for existing open positions. After any restart, all live positions are unknown and the bot re-enters them. | Fixed: boot() calls oanda.get_open_trades() then reconcile_from_oanda(). Scans for scrooge-* tagged trades and re-populates trade_manager. position_count initialized to reconciled count. Verified live — 2 positions detected correctly on restart. | ✅ Fixed |
| 17 | Scrooge | Time exit immediately re-enters same signal | After a 30-min time exit, the same signal fires 1 second later and a new position is opened. Defeats the purpose of exiting for inactivity. | Fixed: 60-min cooldown per symbol. ctx[time_exit_cooldowns][symbol] = now + 60min on time exit. Gate blocks re-entry until expiry. decisions.log shows cooldown status. | ✅ Fixed |
| 18 | Scrooge | move_stop() crashes silently | Wrong arg count: (symbol, trade_id, price) vs signature (trade_id, oanda_trade_id, new_stop, reason). Also sends UUID to OANDA which expects numeric trade ID. TypeError is swallowed. | Fixed: place_entry_order() extracts orderFillTransaction.tradeOpened.tradeID and returns oanda_trade_id. OpenPosition has new oanda_trade_id field. move_stop call fixed to 4 correct args. reconcile_from_oanda() also captures numeric ID for existing positions. | ✅ Fixed |
| 19 | Scrooge | Stale signal fires after price passes stop | AUD/USD moved past the stop level (0.71232 > 0.71182) but ENTER_SHORT kept firing. OANDA rejected with STOP_LOSS_ON_FILL_LOSS. | Staleness check added: if current_price >= stop for SHORT (or <= stop for LONG), skip and log. | High |
| 20 | Scrooge | emergency_exit args in wrong order | Called as (symbol, side, qty, pos.trade_id, current_price, reason). Signature expects (symbol, side, qty, stop_loss, trade_id, reason). UUID was passed as stop_loss causing round(str) TypeError. | Fixed to pass pos.current_stop as stop_loss. | Medium |
| 21 | Sprite | No per-symbol entry guard | Sprite only checked global position_count >= 3. No per-symbol check. When ATOM fired at three consecutive 5-minute candles, all three entered because count (1, 2) was still under the cap. Burns’ reference code not checked for Sprite. | Fixed: per-symbol gate added before global cap. Checks trade_manager.get_all_open() and router.pending for matching symbol before allowing entry. | ✅ Fixed |


### Table 34

| All 21 items across three audits are now resolved. Scrooge: restart reconciliation, 60-min time-exit cooldown, move_stop fully wired. Sprite: per-symbol entry guard added. Both verified in production. |


### Table 35

| OTR = Total Round-Trip Overhead ÷ Half-Box Potential |


### Table 36

| EXCELLENT  < 5% | ACCEPTABLE  5-10% | MARGINAL  10-15% | SKIP  > 15% |


### Table 37

| OTR Range | Category | Minimum Requirements | Extra Requirements |
| < 5% | Excellent | Any zone + 60%+ ATR + any pitchfork | None |
| 5-10% | Acceptable | Tier 1-3 zone + 60%+ ATR + any pitchfork | None |
| 10-15% | Marginal | Tier 1-2 zone + 80%+ ATR + named signal only | John Wick or Power of Towers required. Standard pitchfork not sufficient. |
| > 15% | Skip | Do not trade regardless of signal quality | — |


### Table 38

| Exchange | Cost Type | Round-Trip Cost | Key Risk |
| OANDA (Scrooge) | Spread only, no commission | Spread × 2 (entry + exit) | Spread spikes 2-10x during news, London close, thin sessions. Per-pair baselines calibrated for all 24 pairs. |
| Kraken (Sprite) | Taker fee 0.26%/side (slippage-buffered limits) | 0.52% + spread round-trip | Slippage buffer (+0.15%) ensures immediate fill. OTR gate now uses taker_rate. Per-pair spread estimates calibrated for all 20 pairs. |


### Table 39

| Category | Pairs | Typical Spread | OTR Implication |
| Dollar majors | EUR/USD, USD/JPY, GBP/USD, AUD/USD, USD/CHF, USD/CAD, NZD/USD | 1.1–1.6 pips | Most competitive. Pass OTR gate on 30-pip boxes. |
| JPY crosses | EUR/JPY, GBP/JPY, AUD/JPY, CAD/JPY, CHF/JPY, NZD/JPY | 1.3–2.0 pips | GBP/JPY needs 60-pip box. Others 40 pips. |
| EUR crosses | EUR/GBP, EUR/CAD, EUR/AUD, EUR/NZD, EUR/CHF | 1.3–3.0 pips | EUR/NZD selective at 3 pips. EUR/GBP tight at 1.3. |
| GBP crosses | GBP/CAD, GBP/AUD, GBP/NZD, GBP/CHF | 2.2–4.0 pips | GBP/NZD needs 70+ pip box. Only passes on volatile sessions. |
| Commodity cross | AUD/CAD, AUD/NZD | 1.8–2.2 pips | Moderate. Pass on 30–35 pip boxes. |


### Table 40

| Crypto Tier | Pairs | Spread Estimate | OTR Implication |
| Large cap | BTC, ETH | 0.01% | Negligible overhead. OTR dominated by maker fee. |
| Large mid | SOL, XRP, DOGE, LTC | 0.02% | Very tight. Passes on 1.5–2.5% boxes. |
| Mid cap | ADA, BCH, LINK, AVAX, DOT | 0.02–0.03% | Normal. 2.5–3% box required. |
| DeFi/alts | UNI, AAVE, XLM, NEAR, ATOM, INJ, FIL | 0.04–0.05% | Wider minimum boxes (3–4%). Self-select on volatile days. |
| TRX/unlisted | TRX + any future pairs | 0.03–0.05% | Default 0.05% fallback — deliberately pessimistic. |


### Table 41

| Session | Typical Spread Multiplier |
| London / NY overlap (best) | 1.0x — tightest spreads of the day |
| NY open | 1.1x |
| London close | 1.8x — liquidity drops sharply |
| Asian session | 1.5x — thinner market |
| Major news event | 3-10x — OTR gate will fail automatically |


### Table 42

| 30-Day Volume | Maker Rate | Taker Rate | RT Cost on $10k Order |
| $0 (current) | 0.16% | 0.26% | $32 maker / $52 taker |
| $50,000 | 0.14% | 0.24% | $28 / $48 |
| $100,000 | 0.12% | 0.22% | $24 / $44 |
| $500,000 | 0.08% | 0.18% | $16 / $36 |
| $10,000,000+ | 0.00% | 0.10% | $0 / $20 (zero maker fee) |


### Table 43

| State | Condition | System Action |
| Ranging | Price between PDH and PDL | Normal operations. All gates active. |
| Breach Pending | One candle closes beyond a wall | Wait for second candle confirmation. |
| Box Broken | 2+ candles beyond wall OR 1%+ extension | Draw alternative box. |
| Shelved | No viable alternative box possible | Skip instrument until next daily reset. |


### Table 44

| Status | Position Size | Advancement |
| Unproven (0-2 wins on alt box) | 50% of normal | Counter increments on every close against the alternative box |
| Building (3+ wins) | 100% of normal | Advances automatically. Counter is tracked per-symbol in box state machine. |


### Table 45

| Box Age | Confidence | Size Multiplier | Gates Required |
| 0-2 hours | 100% | 100% | 2 minimum |
| 2-4 hours | 85% | 85% | 2 minimum |
| 4-6 hours | 70% | 70% | 3 required |
| 6+ hours | 50% | 50% | 3 required |


### Table 46

| Phase | Signal | Threshold |
| Compression (setup) | Bollinger Band squeeze AND ATR ratio below baseline | Both conditions simultaneously |
| Breakout (trigger) | Price closes outside BB + ATR expands | Score > 0.80 for primary signal |
| Momentum (secondary) | EMA9/EMA21 cross + RSI + ADX alignment | Score > 0.40. Skipped when capital is 80% deployed. |


### Table 47

| Module | Lines | Responsibility |
| main.py | ~300 | Runtime loop, boot, daily reset, emergency shutdown, position sizing |
| zone_detector.py | 574 | Zone map: daily box + hourly magic lines + Tier 1-4 rankings + polarity flip detection |
| signal_engine.py | 765 | All 6 gates in sequence. Returns fire/no-fire with full gate trace for every evaluation. |
| box_state_machine.py | 586 | Box lifecycle: ranging → breach → broken → alternative box + age decay |
| trade_manager.py | 634 | Partial TPs, break-even stops, hourly trailing, re-entry assessment (wired into main.py on break-even stops) |
| oanda_client.py | 396 | OANDA v20 REST: candles (3 timeframes), live spread, limit orders, stop modification, partial close |
| execution_router.py | 288/440 | Order routing, limit fill polling, timeout cancellation, emergency exits + taker penalty logging |
| fee_calculator.py | 287/376 | OTR ratio, spread/fee math, spread spike detection, viability gate, PnL attribution per partial |
| universe_screener.py | 237/252 | Candidate universe screening: 24 forex pairs (Scrooge) and 20 crypto pairs (Sprite). Evaluates box size, OTR viability, ATR, and zone quality. Runs at boot + every 30 min. Returns ranked shortlist for the main loop. |


### Table 48

| Every 5-minute candle close |
| ▼ |
| Fetch: 5M bars + 1H bars + Daily bars + live spread/ticker |
| ▼ |
| BoxStateMachine.update() — check breach, draw alternative if broken |
| ▼ |
| TradeManager.manage_positions() — partials, trailing stops, time exits |
| ▼ |
| ExecutionRouter.check_pending() — poll fills, cancel timeouts |
| ▼ |
| ZoneDetector.build_zone_map() — refresh magic lines from latest hourly data |
| ▼ |
| SignalEngine.evaluate() — run all 6 gates |
| ▼ |
| If signal.fire: FeeCalculator → size position → place limit order |


### Table 49

| Parameter | Mr. Burns | Mr. Scrooge | Mr. Sprite |
| Exchange | OANDA | OANDA | Kraken |
| Risk per trade | 0.5% | 1.0% | 1.0% |
| Max concurrent | 2 | 3 | 3 |
| Daily loss halt | 6% | 2% | 2% |
| Account floor | $750 | $500 (revised) | $500 |
| Entry orders | Market | Limit (always) | Limit (always) |
| Mode | Live | Live | Live |
| Universe | EUR/USD, USD/JPY, GBP/USD | 24 pairs — see Section 16.4 | 20 pairs — see Section 16.4 |


### Table 50

| Action | Lestat Alone | Requires Brock |
| Read logs, check status, generate reports | ✅ | — |
| Alert Brock via Claudia | ✅ | — |
| Emergency halt (Level 3 uncontrolled risk only) | ⚠️ Level 3 only | ✅ All other halts |
| Modify config or strategy files | ❌ Never | ✅ Always |
| Restart any bot | ❌ Never | ✅ Always |
| Place or cancel trades | ❌ Never | ❌ Never |


### Table 51

| Pair | Category | Session Activity | Min Box | Baseline Spread |
| EUR/USD | Major | London + NY | 30 pips | 1.2 pips |
| GBP/USD | Major | London + NY | 40 pips | 1.4 pips |
| USD/JPY | Major | Asian + London + NY | 30 pips | 1.1 pips |
| AUD/USD | Major | Asian + early London | 30 pips | 1.3 pips |
| USD/CHF | Major | London + NY | 30 pips | 1.4 pips |
| USD/CAD | Major | NY (oil-correlated) | 35 pips | 1.5 pips |
| NZD/USD | Major | Asian + early London | 30 pips | 1.6 pips |
| EUR/JPY | JPY Cross | Asian + London | 40 pips | 1.3 pips |
| GBP/JPY | JPY Cross | All sessions — high vol | 60 pips | 2.0 pips |
| AUD/JPY | JPY Cross | Asian — risk proxy | 40 pips | 1.4 pips |
| CAD/JPY | JPY Cross | Asian + NY | 40 pips | 1.4 pips |
| CHF/JPY | JPY Cross | Asian + London | 40 pips | 1.5 pips |
| NZD/JPY | JPY Cross | Asian + early London | 35 pips | 1.6 pips |
| EUR/GBP | EUR Cross | London-driven, tight | 20 pips | 1.3 pips |
| EUR/CAD | EUR Cross | London + NY | 40 pips | 2.2 pips |
| EUR/AUD | EUR Cross | Asian + London | 45 pips | 2.2 pips |
| EUR/NZD | EUR Cross | Asian + London | 50 pips | 3.0 pips — selective |
| EUR/CHF | EUR Cross | London | 20 pips | 1.5 pips |
| GBP/CAD | GBP Cross | London + NY | 60 pips | 3.0 pips — selective |
| GBP/AUD | GBP Cross | Asian + London | 65 pips | 3.0 pips — selective |
| GBP/NZD | GBP Cross | Asian + London | 70 pips | 4.0 pips — selective |
| GBP/CHF | GBP Cross | London | 40 pips | 2.2 pips |
| AUD/CAD | Commodity | Asian + NY | 30 pips | 1.8 pips |
| AUD/NZD | Commodity | Asian | 35 pips | 2.2 pips |


### Table 52

| GBP crosses and EUR/NZD carry the widest baseline spreads (2–4 pips). They self-select only on days with sufficiently wide boxes. No manual session management required — the OTR gate handles it automatically. |


### Table 53

| Pair | Tier | Min Box | Spread Est. | Kraken Symbol | Status |
| BTC/USD | Large cap | 1.5% | 0.01% | XXBTZUSD | ✅ Active |
| ETH/USD | Large cap | 2.0% | 0.01% | XETHZUSD | ✅ Active |
| SOL/USD | Large cap | 2.5% | 0.02% | SOLUSD | ✅ Active |
| XRP/USD | Mid cap | 2.5% | 0.02% | XXRPZUSD | ✅ Active |
| ADA/USD | Mid cap | 3.0% | 0.03% | ADAUSD | ✅ Active |
| DOGE/USD | Mid cap | 4.0% | 0.02% | DOGEUSD | ✅ Active |
| LTC/USD | Mid cap | 2.5% | 0.02% | XLTCZUSD | ✅ Active |
| BCH/USD | Mid cap | 2.5% | 0.03% | BCHUSD | ✅ Active |
| XLM/USD | Mid cap | 3.5% | 0.04% | XXLMZUSD | ✅ Active |
| LINK/USD | DeFi | 3.0% | 0.03% | LINKUSD | ✅ Active |
| UNI/USD | DeFi | 3.5% | 0.04% | UNIUSD | ✅ Active |
| AAVE/USD | DeFi | 3.0% | 0.04% | AAVEUSD | ✅ Active |
| DOT/USD | L1 | 3.0% | 0.03% | DOTUSD | Selective — box tight today |
| AVAX/USD | L1 | 3.0% | 0.03% | AVAXUSD | ✅ Active |
| NEAR/USD | L1 | 3.5% | 0.04% | NEARUSD | ✅ Active |
| ALGO/USD | L1 | 4.0% | 0.05% | ALGOUSD | ✅ Active |
| ATOM/USD | L1 | 3.5% | 0.04% | ATOMUSD | ✅ Active |
| INJ/USD | Alt | 3.5% | 0.05% | INJUSD | ✅ Active |
| FIL/USD | Alt | 3.5% | 0.05% | FILUSD | ✅ Active |
| TRX/USD | Alt | 2.5% | 0.03% | TRXUSD | Selective — range narrow today |


### Table 54

| Smaller alts use a conservative 0.05% default spread. Any pair not explicitly listed falls back to 0.05% — deliberately pessimistic so OTR estimates never understate cost. 18 of 20 pairs actively scanning as of last boot. |


### Table 55

| Total codebase: Scrooge 4,488 lines · Sprite 4,348 lines · Three audit passes (29 items, all resolved) · Universe: 24 forex + 18 active crypto · Restart stacking fix verified in production Feb 26 · Both bots live and healthy. |
