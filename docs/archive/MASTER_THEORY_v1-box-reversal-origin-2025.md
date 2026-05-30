> **ARCHIVED 2026-05-30** as part of V4 cutover prep. The Box Reversal
> master theory was V1's guiding doctrine (Feb 2026) and remained
> canonical through V3 (Apr 2026). At V4, Box reversal becomes ONE
> of ~25 strategies in `STRATEGY_ENCYCLOPEDIA.md`, no longer privileged.
> 
> This document is preserved verbatim as the historical record of the
> original guiding theory. Its evergreen content (zone structure, sweep
> logic, BB exhaustion gates, sucker-move taxonomy) is being integrated
> into the `box_master_theory` entry of the V4 Strategy Encyclopedia.
> 
> For current canonical truth see:
> - `docs/LIVE_SYSTEM_SPEC.md` — what the bot actually does
> - `docs/STRATEGY_ENCYCLOPEDIA.md` (V4) — all strategies including Box
> - `docs/decisions/1001-box-reversal-core-philosophy.md` (ADR)

---

# Master Theory — V3

## Box Theory + Liquidity Behavior + Modular Execution Framework

This document has two parts:

- **Part I: Source Theory** — extracted directly from Doug and Sylvia's video transcripts. This is ground truth. When the bot and this document disagree, the bot is wrong. Do not modify Part I to reflect implementation decisions.
- **Part II: Engineering Extensions** — discoveries, classification systems, execution doctrine, and system design developed during V1/V2 bot development. These are valid expansions built on top of the source theory, not replacements for it.

---

# PART I — SOURCE THEORY

> This section contains only rules, quotes, and examples that appear in the source material.
> Implementation-specific additions (ATR thresholds, OTR ratios, tier schemas, state machine rules) belong in Part II — not here.

---

# 1. Core Philosophy

The strategy is built on one observation: the way retail trading education teaches entries is designed to make you enter late, after the move has already happened.

> "Patterns are not the problem. Timing is the problem."

> "Your problem is entries."

> "Professional traders don't wait for confirmations. They enter all the way down here before that pattern has even developed."

> "The way they teach the entry is designed to make you enter late after the move has already happened, leaving you with a huge stop and tiny reward."

Traditional education:
```
pattern develops
-> breakout/breakdown confirms
-> retail enters late
-> stop is wide
-> reward is compressed
```

This system:
```
find level first
-> let emotional move hit the level
-> wait for reversal clue
-> enter early
-> keep stop tight
```

---

# 2. The Market Model

The market is a place where liquidity must be created before large players can enter.

> "Institutional traders can't just hit buy and sell button just like you and I do."

> "They need volume and liquidity. Otherwise, they cannot get filled."

> "Retail traders put their stop losses at obvious places below lows, below patterns, below support, and the price dips just far enough to hook these stops. That's the liquidity."

> "If there are not enough orders around this low, the price will keep going lower until eventually enough liquidity is created."

> "The market moves first to clear amateur traders out and then picks a direction."

The market cycle:
```
trend develops
-> retail traders join
-> stops accumulate
-> liquidity sweep occurs
-> institutional orders fill
-> reversal begins
```

---

# 3. The Sucker Move

This is the most important concept in the entire system.

> "The sucker move."

> "A move that sucks people in just to trigger their stop losses."

> "This is a move that is designed to do one thing: get people stopped out, screwed, and grab liquidity."

> "That move is designed to do one thing. Pull traders in emotionally and force them out mechanically."

> "You're the liquidity."

### What it looks like

For long setups (bearish sucker move into support):

> "Three to five red candlesticks in a row straight into our liquidity zone."

> "A few big red candles going straight into the previous low."

For short setups (bullish sucker move into resistance):

> "Three to five green candlesticks in a row straight into the previous high-end liquidity area."

### CRITICAL: It does not have to be clean

This is frequently misunderstood.

> "Sometimes it can look a little choppier... red green green red green candlestick and slightly drop below the support zone."

The real rule:
```
Look for emotional directional pressure into a known level.
Not necessarily a perfect same-color sequence.
```

---

# 4. Levels Come First

This rule is stated repeatedly across all transcripts.

> "If it's not happening at the right place, it has no meaning."

> "I don't care how scary the move looks like. If it's not happening at the right place, it has no meaning."

> "Levels tell you where something might happen. But the pitchfork confirmation shows you when to act."

> "A pattern is meaningless if it's not at the right place on the chart."

The summary:
```
Level tells you where to prepare.
Pitchfork tells you when to act.
```

---

# 5. Liquidity Zones / Magic Lines

The zone-marking process is intentionally simple.

> "Look to the left and draw a horizontal line around the previous high... and one more around the previous low. That's it. No indicators, no fancy tools, just two lines and structure."

> "I call these lines the magic lines."

> "We want to open up the 1 hour chart and we want to draw a horizontal line around the previous high, the previous low and the breakout areas."

> "Mark the previous day's high and the previous day's low."

> "Draw a box from the swing high to the swing low."

### Sources of levels explicitly mentioned in the transcripts

1. Previous day high
2. Previous day low
3. Previous swing high
4. Previous swing low
5. Breakout area
6. Breakdown area
7. Repeatedly tested high/low
8. Prior support that became resistance
9. Prior resistance that became support
10. The top and bottom of the box / range

### Why these levels matter

> "These highs and lows are liquidity zones because this is where most stops are sitting."

> "This is where amateur traders get trapped and most likely where institutional traders step in."

> "The upper line represents the biggest, most committed, and well-funded sellers."

> "The lower line represents the biggest and most committed and well-funded buyers."

> "These are not some random drawings on the chart. They're matching with the pivotal highs and lows from the daily where most likely Smart Money is going to place their buy and sell orders."

---

# 6. Never Trade the Middle

This rule is stated more than any other in the transcripts.

> "Don't diddle in the middle."

> "We do not want to open any positions in the middle of the range. This is noise and chop area."

> "The middle represents nothing. It's just noise and randomness."

> "Try your very best not to execute trades in the center of that chart."

> "You're trading in the noise away from the premium level."

Hard rule:
```
If price is in the middle of the range, do nothing.
```

---

# 7. Buy Lows, Sell Highs

> "We want to be buying at the lower line."

> "We want to be selling at the upper line."

> "Buy at the lower line and sell at the upper line."

> "We buy at the lower line and we sell at the upper line. If the price is in the middle, we do nothing."

Why lows are buy zones:

> "The lows represent the biggest and most committed buyers."

> "This is where smart money puts their buy orders."

> "This is also an area where most amateurs either chase breakdowns or put their stop losses."

Why highs are sell zones:

> "Around the highs, most smart money place their sell orders."

> "This is where they sell their long positions or open short sell positions."

> "This is where most amateurs are chasing breakouts or placing their stop losses."

---

# 8. Daily Chart First

This rule is explicit and repeatedly stated.

> "We always start with the daily chart first."

> "This top-down approach is going to help us eliminate low quality setups and focus on high quality setups only."

> "It is also going to show us where are the most important liquidity zones and where big players are positioned."

> "The daily chart is not negotiable."

> "If you don't like the daily, you don't like the intraday either."

### What to determine from the daily chart

1. Current cycle — who is in control (buyers or sellers)
2. Bias for the session
3. Where price sits inside the larger box
4. Major support/resistance / liquidity zones

### Cycle language from the transcripts

> "Who is in control? Buyers or sellers?"

> "In this example we see a little bit more selloff happening... failed breakout... bigger ranges... increased volume on the red bars... more sellers are stepping in."

> "This is a distribution cycle."

### IMPORTANT NUANCE

Even in a bearish/distribution environment, if price is at the lower part of the box, the long side may be preferred:

> "Because we're at the lower part of the box I would prefer to trade to the long side trying to catch a bigger bounce towards the resistance zone."

The rule:
```
Higher-timeframe cycle provides context.
Location inside the box decides the specific trade.
```

---

# 9. The Box / Range Framework

Both Doug's "Box Theory" and Sylvia's box language describe the same structure.

> "Mark the previous day's high and the previous day's low."

> "Take the chart, move my eyes to the left, and box those two prices in."

> "The very top part represents the largest collective of selling that took place that day."

> "Down at the bottom... is where the largest collective of buyers took control."

> "The majority of activity that we need to know... is going to take place at those levels."

### Box definition

```
BOX = [PDH, PDL]

PDH = Prior Day High (or dominant swing high)
PDL = Prior Day Low  (or dominant swing low)
```

A box is valid if it has clear extremes, price has reacted to both sides, and the range is tradeable.

### Trading logic within the box

> "I'm trying to catch one swing towards the resistance zone and be out of the market. I'm not trying to predict what is going to happen after that."

Many of these trades are box-to-box swings, not large directional predictions.

### Fakeout vs true break

A wick beyond the box boundary is NOT a break. It is a sweep — the ideal reversal condition.

A single close beyond the boundary is suspect but not confirmed. It is a high-probability fakeout zone.

A true break requires structure forming outside the box: multiple closes, sustained acceptance, pullbacks that respect the new level.

Master rules from the source theory:
```
A box is valid until proven broken.
A wick is not a break.
A close is not enough — structure confirms.
New boxes form from accepted price, not touched price.
```

### Alternative box

When a true break occurs, the old box is deprecated and a new box forms:

**Break up:**
```
New floor   = OLD PDH (resistance becomes support)
New ceiling = NEW SESSION HIGH
```

**Break down:**
```
New ceiling = OLD PDL (support becomes resistance)
New floor   = NEW SESSION LOW
```

After break up: look for pullbacks to old PDH (now support), continuation trades. Do not short immediately after clean breakout.

After break down: look for rallies into old PDL (now resistance), continuation trades.

### Transition behavior

Do NOT trade during the transition between boxes. Between break and confirmation is a no-trade zone.

Most traders get trapped during box transitions.

**Double trap scenario:** break up fails, then break down fails. This means the market is range-expanding. Stand down or widen the box.

### Box-to-box priority

When multiple boxes exist (daily, session, intraday):
```
Daily > Session > Intraday
```

If boxes disagree, trade the higher-timeframe box. Ignore lower-timeframe noise.

### Box validity and the obvious-level problem

Each touch of a level reduces its edge:
```
1-2 touches -> strong
3-4 touches -> weakening
5+ touches  -> exhaustion
```

> "The more obvious the level, the more stops cluster there — which means the sweep gets bigger or the level finally fails."

Levels that hold for very long without being tested also weaken from staleness. Fresh, recently-tested levels with clean reactions are the strongest.

---

# 10. The Two-Timeframe Model

> "I combined the one hour chart for structure zones and bias and the five minute chart for precise sniper entries."

> "The higher time frame... gives you the idea where smart money is positioned and the lower time frame gives you sniper entries."

> "Together they filter out the noise and give you more clarity."

Standard timeframe hierarchy:
```
Daily  = context / box / cycle / major zones
1H     = structure / magic lines / zone refinement
5M     = precise entry / confirmation / stop placement
```

### Flexibility

The system is not fixed to these timeframes:

> "The higher the time frame, the more accurate the setups."

It can work on 5M, 15M, 1H, or others. Daily is always the starting point.

---

# 11. The Pitchfork Entry Pattern

The name refers to a candle sequence entry model. It is NOT Andrew's Pitchfork indicator.

> "The candlestick confirmation that I'm talking about is called the pitchfork."

> "Today I will show you the easiest way to master your entries with something I now call the Pitchfork candles."

## Long Entry (pitchfork from support)

> "We want to see three to five red candlesticks in a row straight into our liquidity zone, aka the sucker move."

> "Next we want to see one green candlestick closing green."

> "The entry happens above the high of that green candlestick and the stop-loss can be placed slightly below."

> "As soon as the price goes above the high of the first green candlestick, this is my entry."

> "I'm not waiting for that second green candlestick to close."

Long entry rule:
```
1. Price reaches lower liquidity zone
2. Sucker move forms (3-5 red candles, or emotional push)
3. First green candle closes
4. Enter when price breaks ABOVE that candle's high
5. Stop goes slightly BELOW that candle
```

## Short Entry (pitchfork from resistance)

> "For short selling, we want to see three to five green candlesticks in a row straight into the previous high-end liquidity area."

> "Confirmation happens after we see one red candlestick first closing red."

> "The entry happens below that red candlestick's low with stop-loss slightly above."

Short entry rule:
```
1. Price reaches upper liquidity zone
2. Sucker move forms (3-5 green candles, or emotional push)
3. First red candle closes
4. Enter when price breaks BELOW that candle's low
5. Stop goes slightly ABOVE that candle
```

---

# 12. Candle Quality — The John Wick

Wicks are explicitly favored.

> "It does not matter how this first green candlestick would look like. In some cases it would be with the wick on the bottom, a John Wick candlestick, and in other cases it would be a simple green candlestick."

> "It should have a wick on the bottom in a perfect scenario."

> "John Wick is in town."

> "Wicks are my favorite trading signals because they signify an instant change."

Preferred long signal candle:
- Closes green
- Has lower wick (rejection of the down move)
- Appears after the bearish sucker move
- Shows institutional absorption at the level

Preferred short signal candle:
- Closes red
- Has upper wick (rejection of the up move)
- Appears after the bullish sucker move
- Shows failed breakout / institutional selling

---

# 13. Do Not Catch a Falling Knife

The system does NOT enter blindly into the move.

> "We don't want to try to catch a falling knife."

> "Just because a price hits a certain level, it doesn't mean that it has to reverse there."

> "Red candles are emotion. They're panic and they don't tell you if buyers are actually stepping in."

> "We want to make sure that the liquidity grab is over and done."

This is why confirmation is required:
```
The level tells you where to prepare.
The confirmation candle tells you when to act.
```

---

# 14. Entry Execution

> "I'm not waiting for that second green candlestick to close."

> "As soon as the price starts to go above the high of this candlestick, this is my sign to enter."

> "I like giving it a few points room because I don't want to get stopped out for no reason."

Enter immediately when the signal candle breaks. Do not wait for additional confirmation candles to close before acting.

---

# 15. Opening / Gap Behavior

The "Eliminator" transcript adds specific open-related rules.

> "There are only three things that you will know for sure... gaps above the previous day's high, gaps below the previous day's low, or opens dead center."

> "If we gap, you don't want to buy the gap first thing in the morning."

> "You do not want to short sell the gap bottom."

> "When you open up in the center... wait for this to either test the high or test the low and then gather that data."

Opening rules:

**Gap up above prior high:**
Usually retests the prior high / gap area before continuing. Do not blindly buy the opening extension.

**Gap down below prior low:**
Usually retests the prior low / gap area. Do not blindly short the opening flush.

**Dead-center open:**
Wait for price to test one edge first, then react.

### First 30 minutes

> "The first 30 minutes of trading... that's where all the games get played."

> "For day trading and you're using the 5 minute chart you have to wait a couple of minutes after the market opens."

> "The highest form of activity takes place in those first 30 minutes."

> "Every 30-minute interval you're getting some type of pivot."

---

# 16. Daily Bias and Directional Preference

From the ORE (Opening Range Reversal) transcript:

> "Buy intraday weakness on strong assets or sell intraday strength on weak assets."

> "Dips tend to get bought on strong assets. Rallies tend to get sold on weak assets."

Bullish daily bias -> prefer buying opening weakness.
Bearish daily bias -> prefer selling opening strength.

This is a **context filter**, not a replacement for zone + sucker move + confirmation.

---

# 17. Trade Management

### Hold while valid

> "As long as the trade is valid and your stop-loss is not hit, you do not have a reason to exit."

> "As long as we're holding the lows, there's no reason to exit the trade."

> "Not all trades work right away. Sometimes they're going to take some time."

Do not micromanage. Only abandon if stop is hit, structure breaks, or setup is clearly invalidated.

### Pay yourself

> "Sell half of my position, pay myself."

> "Take partial profits and pay myself along the way."

> "Because I already had one minus trade, I'm going to go ahead and just move the stop-loss to break even and close some of my position just to pay myself."

Standard pattern:
```
take 1/2 off
-> move stop to breakeven
-> let the rest work
```

### Break-even stop

> "Move the remainder of the stop-loss around break even. This way I'm out of the risk."

> "At this point the stop has been moved to a break even area."

### Hourly trailing stop

This appears repeatedly as the standard management technique.

> "After each candlestick closes, I am moving manually the stop loss below the low of each candlestick."

> "I'm going to manually drag my stop-loss underneath each candlestick's low."

> "Move the stop below each hourly candlestick's low."

For longs:
```
After each higher-timeframe bullish candle closes,
move stop below its low.
```

For shorts:
```
Move stop above structure highs / candle highs.
```

### Exit at opposing zone or on rejection

Common exit signals:
- Rejection wick at resistance (for longs)
- Double top
- Lower low after a bounce
- Price reaches the opposite liquidity zone
- Momentum clearly lost

---

# 18. Re-Entry Logic

Being stopped once does NOT invalidate the zone.

> "If stopped out, come back later and see if I have another chance to re-enter."

> "As soon as I got stopped out, I was looking if more sellers step in again so that I can re-enter."

> "We still don't have a trade... I am still waiting to see if we get a chance to enter."

Re-entry rule:
```
If the level still holds AND a new pitchfork signal forms -> re-entry is allowed.
```

The transcripts do not define a maximum number of re-entries. The zone is valid as long as price is still reacting to it.

---

# 19. Some Trades Go Sideways First

This is explicitly addressed.

> "The market is going sideways here and it's getting a little stubborn, but I'm holding on because we're building a base here so far."

Choppy consolidation at the zone after entry is normal. It does not automatically mean the trade has failed.

---

# 20. Volume as Supporting Evidence

Not the primary trigger, but mentioned as supportive context.

> "We have increased volume on the red bars indicating that there are more sellers than buyers."

> "Please take a look at the volume here. We see increased volume on this green candlestick."

Volume is a clue:
- Rising red volume = distribution / seller pressure building
- Strong green reversal volume = buyer stepping in at the zone

It supports the read. It is not a standalone gate.

---

# 21. Measured Moves / Range Expectations

Doug adds a measured-move overlay to keep expectations realistic.

> "The measured move."

> "You can take any move that you see in succession and measure it and use that as a guide."

> "The market goes up and it goes down then it goes up and then it goes down."

> "It's just math."

> "You need to set your expectations."

From the daily range / ATR transcripts:

> "We begin every single day by looking at the daily range."

> "You can just put the ATR indicator up there... give me something to start with."

> "If you're buying it and you're expecting 750 points today, that's outrageous."

Use daily range / ATR to judge:
- Is the move already extended?
- Is there still reward left?
- Are we near exhaustion for the day?

Note: The transcripts do not specify exact ATR percentage thresholds. The ATR is used as a reference for setting realistic expectations, not as a hard gate.

---

# 22. The Complete Trade Flow

Summarized from the transcripts:

```
Start with daily chart
-> determine who is in control (buyers or sellers)
-> mark the box (prior day high / prior day low)
-> mark magic lines on 1H (prior highs, lows, breakout areas)
-> never trade the middle
-> wait for price to reach upper or lower liquidity zone
-> watch for sucker move into zone (3-5 candles, can be messy)
-> wait for first reversal candle (green at support, red at resistance)
-> preferably with a wick rejection
-> enter when price breaks above (long) or below (short) that candle
-> stop slightly beyond the candle
-> take partial profit, move stop to breakeven
-> trail stop below hourly candle lows (longs) or above highs (shorts)
-> exit at opposing zone or on rejection evidence
-> if stopped, re-enter if zone still valid and new signal forms
```

---

# 23. What This Theory Is NOT

For clarity on what belongs in Part I vs. Part II:

The transcripts do NOT specify:
- Exact ATR percentage thresholds (60%, 80%, etc.) as hard gates
- OTR (overhead-to-range) ratio formulas
- Formal tier ranking schemas with numbered tiers
- State machine states with specific names
- Exact percentage splits for position scaling (40/40/20)
- Fixed minute-based timeout rules
- Hard limits on re-entry count
- Confidence decay formulas by box age
- Bollinger Band classification systems
- Regime labels (TREND, EXTREME, etc.)
- Spread-based execution rules
- Module/contract/registry architecture

These are engineering additions made during bot development. They belong in Part II.

---
---

# PART II — ENGINEERING EXTENSIONS

> Everything below was discovered or designed during V1/V2 bot development.
> These are valid expansions built on top of the source theory.
> They must never contradict Part I. When in conflict, Part I wins.

---

# 24. Three Core Behaviors (Engineering Model)

All price action reduces to:

```
1. RANGE      (equilibrium)    -> source: Sections 6, 7, 9
2. EXPANSION  (trend)          -> source: Section 8 (cycle/bias)
3. EXHAUSTION (reversal setup) -> source: Sections 3, 4, 11
```

This is a classification overlay on the source theory, not a replacement for it.

---

# 25. Box Lifecycle State Machine (Engineering Formalization)

This section formalizes the box lifecycle from Part I Section 9 into mechanical rules for automation.

### State Machine

```
1. RANGING           -> price between PDH and PDL
2. BREACH_INITIATED  -> price closes beyond PDH or PDL (single close)
3. LIQUIDITY_SWEEP   -> price wicks/extends beyond boundary, then rejects back inside
4. CONFIRMED_BREAK   -> structure forming outside box (multiple closes, sustained acceptance)
5. ALTERNATIVE_BOX   -> new box active after confirmed break
6. INVALID           -> box shelved (too old, too many touches, or structure collapsed)
```

### Trade Permissions per State

```
RANGING         -> reversal allowed at edges, no middle trades
LIQUIDITY_SWEEP -> HIGH probability reversal (ideal condition)
BREACH_INITIATED -> NO TRADE (single close = fakeout zone, wait for resolution)
CONFIRMED_BREAK -> trend/continuation trades allowed
ALTERNATIVE_BOX -> treat as new RANGING with new boundaries
INVALID         -> no trades, wait for new box formation
```

### Confirmed Break Criteria

A break is confirmed ONLY if:

```
EITHER:
  2+ consecutive closes outside box

OR:
  Extension > threshold beyond boundary (instrument-dependent)

AND:
  No immediate rejection back inside
  Pullbacks respect the new level (old boundary becomes support/resistance)
```

### Box Creation Algorithm

```python
if no_active_box:
    box = [PDH, PDL]
    state = RANGING

elif price_inside(box):
    state = RANGING

elif wick_outside and return_inside:
    state = LIQUIDITY_SWEEP
    # keep original box — ideal reversal condition

elif close_outside:
    breach_count += 1

    if breach_count == 1:
        state = BREACH_INITIATED
        # no trade — wait for confirmation or rejection

    elif breach_count >= 2 or extension > threshold:
        state = CONFIRMED_BREAK

        if break_up:
            new_box = [old_PDH, new_session_high]
        elif break_down:
            new_box = [new_session_low, old_PDL]

        state = ALTERNATIVE_BOX
```

### Validity Decay (Engineering Parameters)

**Time-based:**
```
0-2 hrs  -> strong
2-4 hrs  -> moderate
4-6 hrs  -> weak
6+ hrs   -> low confidence (consider INVALID)
```

**Interaction-based:**
```
1-2 touches -> strong
3-4 touches -> weakening
5+ touches  -> exhaustion (level is obvious, sweep gets bigger or level fails)
```

These thresholds are engineering parameters — the source theory establishes the principle (levels weaken with time and touches) but does not specify exact numbers.

### Gap Edge Cases (from Section 15)

```
Gap up (open > PDH):
  Box = [PDH, Session High]

Gap down (open < PDL):
  Box = [Session Low, PDL]

Dead-center open:
  Box = [PDH, PDL] — wait for price to test one edge
```

### Multi-Box Resolution

When daily, session, and intraday boxes exist simultaneously:
```
Daily > Session > Intraday
```

If boxes conflict, the higher-timeframe box wins. The engineering implementation should tag each box with its timeframe source and resolve conflicts by priority.

### Double Trap Detection

```
Break up -> fail -> break down -> fail
= RANGE EXPANDING
```

When detected: stand down entirely or widen the box to encompass the new range. Do not attempt reversal trades at the original edges — they have been consumed.

---

# 26. Behavior Classification (Double BB Layer)

### Purpose

Classify **market state**, not signals. The source theory describes states qualitatively ("exhaustion," "trend," "range"). This layer quantifies them.

### Bands

```
Inner Band: 20 period / 2 std -> structure boundary
Outer Band:  4 period / 4 std -> extreme boundary
```

### States

```
RANGE   -> inside inner band
TREND   -> between inner and outer band
EXTREME -> outside outer band
```

### Critical Rule

Do NOT reverse unless EXTREME. This is the engineering translation of the source theory's requirement that reversals need exhaustion + sucker move + level confluence.

### Meaning

```
EXTREME -> exhaustion possible, reversal engine eligible
TREND   -> continuation likely, trend engine eligible
RANGE   -> mean reversion possible, no engine eligible (middle = noise)
```

---

# 27. ATR + OTR Expansion Logic

### ATR (from source theory)

Market has a daily movement budget (ATR). The source theory uses this qualitatively for setting realistic expectations.

### OTR (engineering addition)

Overhead-to-Range ratio quantifies how much of the daily budget remains:

```
Low ATR used  -> move likely incomplete, more room to run
High ATR used -> move near exhaustion, reversal conditions forming
```

Used for: filtering setups, identifying exhaustion, validating reversals, setting realistic take-profit expectations.

Note: Exact thresholds are engineering parameters, not source theory.

---

# 28. Strategy Stack

### Reversal Engine (Primary) — source: Sections 3, 4, 5, 11, 12

Conditions:
- Box boundary (Section 5: liquidity zone)
- Sucker move (Section 3: emotional push, can be messy)
- Pitchfork confirmation (Section 11: first reversal candle)
- John Wick quality bonus (Section 12: wick rejection)
- EXTREME BB context (Section 26: engineering classification)

### Trend Engine (Secondary) — engineering addition

Conditions:
- TREND BB state (between inner and outer band)
- Pullback to structure (BB20 / SMA20)
- Continuation bias from daily chart (Section 8)

### Future Engines

- **Opening gap engine** — source: Section 15 (gap behavior, first 30 minutes)
- **Measured move engine** — source: Section 21 (realistic expectations, "it's just math")
- **Volatility compression breakout** — engineering addition
- **Regime-specific strategies** — engineering addition

---

# 29. Regime Theory

### Not just trend vs range

```
RANGE           -> Section 6 (middle = noise, do nothing)
TREND           -> Section 8 (cycle direction)
EXPANSION       -> extreme directional move
EXHAUSTION      -> Section 3 (sucker move + sweep)
TRAP CONDITIONS -> Section 3 (liquidity grab that doesn't reverse)
```

### Strategy Mapping

```
EXHAUSTION -> reversal engine
TREND      -> trend engine
RANGE      -> no trade (source: "don't diddle in the middle")
OPENING    -> gap engine (source: Section 15)
```

---

# 30. Gate Theory

### Purpose

Gates remove bad trades, not find good ones.

### Core Gates

| Gate | Source |
|------|--------|
| Spread | Engineering: broker reality |
| Risk/Reward | Source: tight stop, realistic target |
| OTR | Engineering: ATR budget remaining |
| Zone proximity | Source: Section 4 (levels come first) |
| Debounce | Engineering: prevent rapid re-fire |
| Regime filter | Engineering: BB classification |
| Exhaustion filter | Source + Engineering: BB EXTREME required for reversals |

### Gate Rule

Each gate must be: independent, removable, observable.

---

# 31. Execution Theory (Critical Discovery)

### Core Insight

Execution errors destroy edge faster than bad signals.

### Broker Reality (OANDA)

```
Long SL triggers on BID
Short SL triggers on ASK
```

### Failure Mode Discovered in V2

```
SL calculated on mid/bid
Spread expands
SL placed inside executable spread
Immediate fill (dead on arrival)
```

### Execution Rules

**1. Trigger-side validation**
```
Short SL -> validate vs ASK
Long SL  -> validate vs BID
```

**2. No-man's-zone rule**
Never place SL inside spread.

**3. Spread-aware trailing**
Do not tighten stops in hostile spread. This directly supports the source theory's trailing stop rules (Section 17) — the source says trail below hourly candle lows, but the engineering reality is that spread conditions can make that placement suicidal.

**4. Execution lifecycle tracking**
```
CREATED -> SENT -> ACK -> TRIGGERED -> FILLED
```

---

# 32. Trade Management (Engineering Extensions)

The source theory (Section 17) defines: partial take profit, break-even shift, hourly trailing stop, exit at opposing zone.

Engineering additions:

### Ratchet logic
Lock a percentage of unrealized gains at periodic intervals. Provides mechanical discipline beyond the source theory's qualitative trailing rules.

### Time stop
If a trade has not moved favorably within a defined window, close it. The source theory says "some trades go sideways first" (Section 19) — the time stop must be generous enough to respect this.

### Green exit
If all conditions that justified entry have reversed (regime changed, BB state flipped), exit even if stop has not been hit.

### Emergency close
Hard circuit breaker for account-level risk events (margin, equity drawdown, broker disconnect).

---

# 33. Re-Entry Logic (Engineering Implementation)

Source theory (Section 18): zone remains valid after being stopped, re-entry allowed if new pitchfork forms.

Engineering implementation:
- Track zone hit count
- Track re-entry attempts per zone per session
- Debounce timer between attempts
- Zone validity decays if price behavior changes (e.g., zone broken and held below)
- No hard limit on re-entries (source theory doesn't define one), but debounce and zone decay provide natural limiting

---

# 34. Timing Physics

### Definition

The system must operate as a synchronized engine.

### Critical Timings

- Decision latency (scan cycle time)
- Order submission latency (API round-trip)
- Broker execution latency (fill delay)
- Spread at event (spread can change between decision and execution)
- Stop modification timing (trailing stop updates)

### Principle

A correct decision executed incorrectly is still a loss. This is the engineering translation of the source theory's emphasis on precise entries (Section 14: "as soon as the price goes above the high").

---

# 35. System Philosophy (V3)

### Core Doctrine

```
Every capability is a module.
Every module has a contract.
Every contract has health.
Every health state is visible.
Every decision is replayable.
```

### System Identity

This is NOT a strategy, an indicator system, or a signal bot.

This IS: a modular market behavior engine that routes capital based on context, structure, and execution quality.

### Governing Rule

Any module can be added, removed, disabled, or put in observe-only mode without breaking the rest of the system.

---

# 36. Edge Summary

The system's edge comes from combining:

1. **Structure** — box theory (Sections 2, 5, 9, 25), liquidity zones (Section 5)
2. **Behavior** — sucker moves (Section 3), stop hunts (Section 2), BB classification (Section 26)
3. **Timing** — pitchfork entries (Section 11), execution precision (Section 31)
4. **Control** — gates (Section 30), regime routing (Section 29), spread awareness (Section 31)
5. **Management** — partial exits, ratchet logic, trailing structure (Sections 17, 32)

---

# 37. Final Statement

You are not trading patterns. You are trading **forced behavior at known locations**, executed with **precision timing**, protected by **strict risk control**, and governed by a **modular decision system**.

The source theory tells you **what** to trade and **why** it works.
The engineering extensions tell you **how** to execute it with a machine.
When they conflict, the source theory wins.
