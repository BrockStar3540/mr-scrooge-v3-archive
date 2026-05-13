# Box-Geometry Forensic v0 — 87 contaminated trades

Generated: 2026-05-13T02:05:46.351032+00:00

## Method

For each of the 87 broker_actual_loser rows tagged `correct_box_replay_required`
(i.e. entered in a known box-bug window B-068 to B-074):

1. Reconstructed entry price from M5 dukascopy bars at entry_ts (5-min bar containing entry)
2. Computed correct PDH/PDL from prior trading day's daily bar (real bid high/low)
3. Classified entry location vs correct box:
   - `below_pdl`, `at_pdl_edge`, `inside_box`, `at_pdh_edge`, `above_pdh`
4. Determined repair category by combining (location × direction × mfe_r)

## Headline split (Brock's requested output)

| Repair recommendation | Count | % |
|---|---|---|
| **skip_required** | 33 | 37.9% |
| **same_direction_repair** | 27 | 31.0% |
| **direction_flip_repair** | 20 | 23.0% |
| **no_clean_answer** | 7 | 8.0% |

**Translation:**

- **38% of contaminated trades should never have been taken.** The box bug made the bot see a wall where there was none; it entered from the middle of the correct range with no rail to fade. These are pure false signals.
- **31% had the right direction at the wrong location.** Direction was correct, but bot entered from inside_box instead of waiting for the correct PDH/PDL rail. Strategy logic was sound, box logic rotted the entry.
- **23% were directionally wrong.** Bot shorted at PDL or longed at PDH — the OPPOSITE direction was the legitimate trade against the correct box.
- **8% are unresolved.** Mostly trades with valid location but mfe<0.15R; market never developed in any direction.

## Location distribution

| location    |   count |
|:------------|--------:|
| inside_box  |      36 |
| above_pdh   |      24 |
| below_pdl   |      12 |
| at_pdh_edge |       8 |
| at_pdl_edge |       6 |
| unknown     |       1 |

**41% of contaminated entries were inside_box.** The bot saw a fake wall in the middle of the day's range and faded it. Of those 36 inside_box trades, most (those with low mfe) became skip_required. A few (with high mfe) became same_direction_repair — the trend was strong enough that the entry worked anyway.

**28% entered above_pdh** — these are short trades that look like trend rejections at resistance. When direction was short, they're same_direction_repair. When long, they're direction_flip (longing into resistance).

**14% entered below_pdl** — symmetric, for longs at support.

## Breakdown by box-bug context

| box_bug_context                                                                            |   direction_flip_repair |   no_clean_answer |   same_direction_repair |   skip_required |
|:-------------------------------------------------------------------------------------------|------------------------:|------------------:|------------------------:|----------------:|
| B-069:30m rolling box experiment; B-074:regime vs alt-box mismatch (any alt-box trade)     |                       0 |                 0 |                       3 |               1 |
| B-072:UTC midnight box-reset amnesia; B-074:regime vs alt-box mismatch (any alt-box trade) |                       9 |                 1 |                      10 |              11 |
| B-073:stale-box absurd TPs; B-074:regime vs alt-box mismatch (any alt-box trade)           |                       0 |                 0 |                       3 |               1 |
| B-074:regime vs alt-box mismatch (any alt-box trade)                                       |                      11 |                 6 |                      11 |              20 |

**B-074 (regime vs alt-box mismatch) is in EVERY contaminated row** — it's documented as 'open as of 2026-04-13, applies to all alt-box trades through that date.' So every alt-box trade pre-4/13 is contaminated by B-074. Other bugs overlap on top.

**B-072 (UTC midnight amnesia) shows the most balanced split** (direction_flip 9 / same_direction 10 / skip 11 / no_clean 1). The midnight-amnesia trades fired against a freshly-reset box, so the bot's directional intuition was random against the corrected reference.

## Breakdown by pair family

| pair_family      |   direction_flip_repair |   no_clean_answer |   same_direction_repair |   skip_required |   total |   skip_pct |   flip_pct |
|:-----------------|------------------------:|------------------:|------------------------:|----------------:|--------:|-----------:|-----------:|
| antipodean_cross |                       6 |                 2 |                       6 |              17 |      31 |       54.8 |       19.4 |
| eur_cross        |                       2 |                 3 |                       3 |               2 |      10 |       20   |       20   |
| gbp_cross        |                       4 |                 0 |                       9 |               4 |      17 |       23.5 |       23.5 |
| usd_base         |                       8 |                 2 |                       9 |              10 |      29 |       34.5 |       27.6 |

- **antipodean_cross has the highest skip_required ratio (55%)** — most of the bot's contaminated antipodean shorts/longs were pure false signals
- **gbp_cross has the highest same_direction_repair ratio (53%)** — the bot's direction was right, just the location was wrong
- **usd_base is the most evenly mixed** — every repair type appears

## What this resolves for the trade-film ledger

Per row, the ledger now carries:
- `correct_pdh`, `correct_pdl` — actual prior-day high/low from market data
- `reconstructed_entry_price` — M5 bar open at entry_ts
- `entry_location_vs_correct_box` — categorical location
- `repair_recommendation` — one of {same_direction_repair, direction_flip_repair, skip_required, no_clean_answer}
- `repair_evidence` — free-text basis for the classification

## What v0 cannot resolve

- The heuristic uses PDH/PDL only. V1 should add intraday box adjustments (PDH formation time, mid-session walls).
- The `no_clean_answer` bucket (7 trades) needs deeper context — likely they entered in a valid location but the market simply didn't move. Those aren't system failures, they're noise.
- The 27 same_direction_repair trades have a hypothetical 'better entry exists' claim that v0 doesn't verify with actual replay — only that the location was suboptimal. A v1 would simulate the corrected entry to confirm winnability.

## What's queued (per direction)

- Step 6: direction_repair_or_skip lookup for the 88 non-contaminated should-have-skipped rows
- Cluster naming: still on hold. Patterns are visible (Asia winners, USD-base dominance, etc.) but no regime names assigned.
- ready_for_backtest: FALSE everywhere.

## Honest constraints

- Heuristic-based classification, not full V1-code replay against historic data
- M5 entry_price proxy: uses the bar's open at the 5-min boundary containing entry_ts. Real fill price could be ±a few pips
- Daily PDH/PDL uses dukascopy bid-side daily. The bot may have used a different definition (ask-side, hourly aggregation, etc.)
- The same_direction_repair recommendations DO NOT claim the corrected trade would have been a winner. Only that direction was right.