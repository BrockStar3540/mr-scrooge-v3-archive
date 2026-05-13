# Textbook Trade 001 — EUR_USD London Lower-Band Reclaim Long

Status: historical paper trade, reverse-engineering seed
Pair: EUR_USD
Date: 2022-07-18
Decision time: 06:15 UTC
Entry time: 06:20 UTC
Session: London q1
Technique draft: `lower_band_reclaim_snapback_long`

## Purpose

This is the workflow Brock asked for: analyze the previous session and current session, design the textbook trade, enter it with a profit goal, exit it, then reverse-engineer the technique for bot trading.

This was not a real-money broker order. It is a historical paper trade built from raw bid/ask M5 data so the bot logic can be extracted and tested.

## Previous Session Context — Asia

Asia window: 2022-07-17 22:00 UTC to 2022-07-18 06:00 UTC

- Asia high: `1.01145`
- Asia low: `1.007885`
- Asia range: `35.65 pips`

Interpretation:

Asia built a contained range. London opened near the lower side of that range, but had not broken the Asia low. That creates a clean binary map:

- If London breaks and accepts below Asia low, no long.
- If London presses lower band but fails to break Asia low, a snapback long is textbook.

## Current Session Context — London Open

At 06:00-06:15 UTC, London q1 pressed the lower Bollinger band.

| time UTC | close | BB pos | RSI14 | EMA20 dist | spread |
|---|---:|---:|---:|---:|---:|
| 06:00 | 1.008380 | 0.049 | 34.3 | -10.5 pips | 0.6 |
| 06:05 | 1.008535 | 0.164 | 37.0 | -8.1 pips | 0.5 |
| 06:10 | 1.008535 | 0.182 | 37.0 | -7.3 pips | 0.3 |
| 06:15 | 1.008370 | 0.139 | 35.2 | -8.1 pips | 0.4 |

Key read:

- Price pressed the lower band.
- RSI was low, not just neutral chop.
- Spread was clean.
- Price did **not** break the Asia low.
- Two M5 lows formed at `1.008145`, above the Asia low `1.007885`.
- This is a failed downside push inside the prior-session range.

## Trade Plan

Direction: long

Entry rule:

```text
Enter long at the next M5 open after the 06:15 lower-band pressure candle fails to break the Asia low.
```

Entry:

```text
Long EUR_USD at 1.00840 ask, 2022-07-18 06:20 UTC
```

Invalidation:

```text
Stop below Asia low / failed-lower-band structure.
```

Stop:

```text
1.00788
```

Risk:

```text
5.2 pips
```

Profit goal:

```text
2R target = 1.00944 bid-side exit
```

Management:

```text
If +1R hits quickly, allow the trade to continue to 2R unless the next candle closes back below entry.
Time-stop if no progress after 6 M5 bars.
```

## Outcome

Entry candle sequence after the trade:

| time UTC | bid high | bid low | bid close | result |
|---|---:|---:|---:|---|
| 06:20 | 1.00899 | 1.00836 | 1.00891 | +1R reached |
| 06:25 | 1.00900 | 1.00859 | 1.00889 | held above entry |
| 06:30 | 1.00897 | 1.00864 | 1.00882 | still valid |
| 06:35 | 1.00941 | 1.00881 | 1.00916 | nearly 2R |
| 06:40 | 1.01051 | 1.00897 | 1.01035 | 2R target filled |

Exit:

```text
Exit at 1.00944, 2022-07-18 06:40 UTC
```

Result:

```text
+2.0R / +10.4 pips
```

Additional observation:

The trade continued far beyond 2R after the exit, but the research goal here is not hindsight maximizing. The goal is to define a repeatable textbook technique with a predetermined profit objective.

## Why This Was A Textbook Trade

This was not "RSI low, buy." The full synchrony was:

```text
previous session contained range
+ London open lower-band pressure
+ failed break of Asia low
+ low RSI
+ price below EMA20 but not structurally broken
+ tight spread
+ immediate reclaim behavior
+ compact stop
```

The important feature is the map: prior-session low gives invalidation. The lower-band pressure creates the entry. The reclaim creates timing. The tight stop creates enough R-multiple payoff.

## Bot Strategy Draft

Name:

```text
london_q1_asia_low_reclaim_long
```

Candidate deterministic rule:

```text
IF pair is liquid USD major
AND current session_quarter == london_q1
AND previous Asia range is defined
AND current price is in lower 25% of Asia range
AND current/previous M5 candle has bb_pos <= 0.20
AND RSI14 <= 40
AND spread <= 0.6 pips
AND current low remains above Asia low or reclaims immediately after a small sweep
AND EMA20 distance is negative but not more than ~2 ATR
THEN enter long on next M5 open after reclaim/failed-break candle
STOP = min(setup low, Asia low) - small buffer
TARGET = 2R
TIME STOP = 6 bars if no +1R progress
```

Kill tests:

- Does it survive on all liquid USD majors?
- Does it survive London q1 only, or all q1 session opens?
- Does requiring `low > Asia low` outperform allowing small sweeps?
- Does RSI <= 40 matter?
- Does BB pos <= 0.20 matter?
- Does the edge die if spread > 0.6 pips?
- Does 1.5R outperform 2R after costs?

## Reverse-Engineering Summary

This is a microstrategy candidate, not a production rule.

The repeatable idea is:

```text
At London open, fade a failed lower-band push only when the prior Asia low defines a nearby invalidation and the market refuses to break it.
```

This is the kind of technique the bot can learn: session structure first, chart pressure second, entry timing third, management last.
