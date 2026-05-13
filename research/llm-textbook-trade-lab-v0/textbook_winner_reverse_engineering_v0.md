# LLM Textbook Trade Lab v0 — Winner-First Reverse Engineering

Generated: 2026-05-13

## Why This Exists

The blind discretionary batch proved a useful negative: six LLM-designed TAKEs from random textbook-looking contexts all stopped out. That means the task is not "look at random charts and opine." The useful workflow is winner-first:

1. Find real historical chart events that became clean winners.
2. Hide old bot/probe labels.
3. Let the LLM describe the textbook trade that existed at the entry moment.
4. Convert repeated textbook descriptions into deterministic microstrategy candidates.
5. Backtest those candidates directly from raw chart data.

This file is the first winner-first seed sheet.

## Blind Batch Result

File inputs:
- `contexts/CTX-001.md` through `contexts/CTX-012.md`
- `trade_plans_v0.jsonl`
- `textbook_trade_scores.csv`

Result:
- 12 blind contexts
- 6 SKIP
- 6 TAKE
- 6/6 TAKE trades stopped

Interpretation: discretionary-looking context is not enough. We need to reverse-engineer known winners and then formalize the repeated mechanics.

## Winner Seed Events

Source:
- `research/raw-m5-winner-factory-v1/raw_m5_candidate_events.parquet`
- exported subset: `winner_seed_events.csv`

Filters:
- non-rollover
- clean 2R winner
- `mae_r <= 0.55`
- `exit_bars` between 4 and 48
- `stop_pips >= 5`
- diversified by trigger/session/direction

## Seed Table

| pair | timestamp | direction | trigger | session | stop | BB | RSI | EMA | BBW | Echo | MFE | MAE | bars |
|---|---|---:|---|---|---:|---|---|---|---|---|---:|---:|---:|
| AUD_USD | 2020-06-11 22:35 | long | T1 lower reclaim | asia_q1 | 6.5 | lower_band | low | ema_mid | explosive | expanded | 2R | 0.0R | 4 |
| EUR_USD | 2022-07-18 06:15 | long | T1 lower reclaim | london_q1 | 5.2 | lower_band | low | ema_near | wide | expanded | 2R | 0.0R | 4 |
| EUR_USD | 2021-12-13 16:00 | long | T1 lower reclaim | ny_pm_q1 | 6.1 | lower_band | low | ema_near | wide | mid | 2R | 0.0R | 4 |
| EUR_USD | 2025-10-14 12:50 | long | T1 lower reclaim | overlap_q1 | 5.2 | lower_band | low | ema_near | mid | mid | 2R | 0.0R | 4 |
| EUR_USD | 2026-03-09 22:15 | short | T2 upper reject | asia_q1 | 5.2 | middle | high | ema_near | mid | explosive | 2R | 0.0R | 4 |
| EUR_USD | 2022-08-30 06:20 | short | T2 upper reject | london_q1 | 5.4 | upper_band | high | ema_near | mid | explosive | 2R | 0.0R | 4 |
| EUR_USD | 2022-02-22 16:55 | short | T2 upper reject | ny_pm_q1 | 6.4 | middle | mid | ema_near | wide | mid | 2R | 0.0R | 4 |
| GBP_USD | 2020-12-30 12:00 | short | T2 upper reject | overlap_q1 | 6.8 | upper_band | high | ema_near | wide | mid | 2R | 0.0R | 4 |
| GBP_USD | 2020-07-08 06:15 | long | T3 band reentry | london_q1 | 5.2 | lower_rail | low | ema_near | wide | explosive | 2R | 0.0R | 4 |
| GBP_USD | 2025-03-21 16:10 | long | T3 band reentry | ny_pm_q1 | 7.9 | lower_rail | oversold | ema_mid | explosive | mid | 2R | 0.0R | 4 |
| GBP_USD | 2020-11-03 12:55 | long | T3 band reentry | overlap_q1 | 6.5 | lower_rail | low | ema_near | mid | mid | 2R | 0.0R | 4 |

`USD_MXN` seed was omitted from the technique sheet despite passing the filter because its 75-pip stop lives in a different cost/volatility world and should not be mixed into USD-major microstrategies.

## Reverse-Engineered Technique 1: Lower-Band Reclaim Snapback Long

Seed examples:
- AUD_USD asia_q1
- EUR_USD london_q1
- EUR_USD ny_pm_q1
- EUR_USD overlap_q1

Textbook trade:
- Market tags or presses the lower Bollinger band.
- RSI is low but not necessarily capitulation-only.
- Price is near EMA20 or reclaiming toward it.
- Band width is not tight; the move has enough expansion to pay a small stop.
- Entry is long on reclaim/acceptance after lower-band pressure.
- Stop is tight, around 5-7 pips in USD majors.
- Target is fast 2R, often within about 20 minutes in these seeds.

Deterministic draft rule:
```text
IF pair in USD majors or liquid USD-base
AND session_quarter in {asia_q1, london_q1, overlap_q1, ny_pm_q1}
AND direction = long
AND prior candle or current structure shows lower-band pressure
AND bb_pos in {lower_rail, lower_band}
AND rsi in {oversold, low}
AND ema20_dist in {ema_near, ema_mid}
AND bbw in {bbw_mid, bbw_wide, bbw_explosive}
AND spread <= liquid-session threshold
THEN enter long on close back inside lower band or first higher M5 close
STOP below reclaim low / 1 ATR M5 cap
TARGET 2R fast; abandon if no progress by 4-6 bars
```

What makes it textbook:
- It is not a blind falling-knife fade. It is a reclaim trade: lower-band pressure first, then acceptance back inside.
- The stop is close because the setup is invalid if the reclaim fails immediately.

Kill tests:
- Does it survive when requiring close-back-inside rather than merely lower-band touch?
- Does it die outside q1 session phases?
- Does it require EUR/GBP/AUD majors only?
- Does it still work after spread/slippage?

## Reverse-Engineered Technique 2: Upper-Band Rejection Snapback Short

Seed examples:
- EUR_USD asia_q1
- EUR_USD london_q1
- EUR_USD ny_pm_q1
- GBP_USD overlap_q1

Textbook trade:
- Market presses upper band.
- RSI is high or stretched relative to local context.
- EMA20 distance is near, meaning this is not a runaway extension far from mean; it is an upper-band rejection from a tradable shelf.
- Entry is short after failure to hold the upper-band/upper-shelf pressure.
- Stop is tight, generally 5-7 pips in these seeds.
- Target is fast 2R.

Deterministic draft rule:
```text
IF liquid USD major
AND session_quarter in {asia_q1, london_q1, overlap_q1, ny_pm_q1}
AND direction = short
AND upper-band pressure occurred within last 1-3 candles
AND bb_pos in {upper_band, upper_rail, middle-after-reject}
AND rsi in {high, mid-after-high}
AND ema20_dist = ema_near
AND spread <= liquid-session threshold
THEN enter short on rejection close or failed continuation candle
STOP above rejection high / 1 ATR M5 cap
TARGET 2R fast; abandon if no progress by 4-6 bars
```

What makes it textbook:
- It is not simply "RSI high, short." The seed pattern is upper-band pressure plus failure/rejection with EMA still close enough to keep stop tight.

Kill tests:
- Does `ema_near` matter, or are far-from-EMA shorts different?
- Is q1 session timing essential?
- Does this fail in strong H1 trend days?

## Reverse-Engineered Technique 3: Lower-Rail Band-Reentry Long

Seed examples:
- GBP_USD london_q1
- GBP_USD ny_pm_q1
- GBP_USD overlap_q1

Textbook trade:
- Price exits or rides below lower rail, then re-enters.
- RSI is low/oversold.
- EMA distance can be near or mid, but the key is re-entry after failed downside continuation.
- This is a stronger version of Technique 1: not just lower-band pressure, but explicit band reentry.

Deterministic draft rule:
```text
IF GBP_USD or liquid USD major
AND session_quarter in {london_q1, overlap_q1, ny_pm_q1}
AND direction = long
AND previous candle closed outside/below lower band
AND current candle closes back inside lower band
AND rsi in {oversold, low}
AND stop <= 8 pips for majors
THEN enter long at next open
STOP below reentry low
TARGET 2R fast; abandon if no progress by 4-6 bars
```

What makes it textbook:
- Failed breakdown. Sellers had their chance and lost immediate control.
- Stop is naturally defined below the failed breakdown low.

Kill tests:
- Does reentry beat plain lower-band touch?
- Does it only work in liquid majors?
- Does it survive with conservative bid/ask execution?

## Important Caveat

These seeds are known winners. That is intentional for reverse engineering, but it means the technique drafts are hypotheses, not validated rules. The next step is to generate every matching raw-M5 event historically, then forward-score all of them with costs.

## Next Build For Claude

Build deterministic replays for the three drafted techniques above:

1. `lower_band_reclaim_snapback_long`
2. `upper_band_rejection_snapback_short`
3. `lower_rail_band_reentry_long`

For each:
- Generate entries from raw M5 across all available pairs.
- Use bid/ask execution.
- Exclude rollover.
- Require spread threshold by pair/session.
- Test 1R, 1.5R, 2R, BE-after-1R, and time-stop after 6 bars.
- Split discovery/holdout.
- Report pair concentration.
- Kill if holdout is not net positive after costs.
