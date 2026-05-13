# Box Freshness Validation Pass — box_age_hours

Generated: 2026-05-13T03:06:57.196101+00:00

## Question

Per 2026-05-13 direction: is box_age_hours an INDEPENDENT signal, or just a
pocket-tag for Asia/USD-antipodean?

## Inputs

- 155 broker rows (non-contaminated) with `factor_box_age_hours` non-null
- 64 winners + 91 losers
- Manual rows excluded (no box_age data)
- Contaminated rows excluded (pending Step 5 correct-box replay)

## Headline: signal is real and independent

**Global cumulative thresholds:**

| Threshold | n | winner_rate | mean_r |
|---|---|---|---|
| ≤24h | 63 | **58.7%** | −0.064 |
| ≤48h | 70 | 57.1% | −0.055 |
| ≤72h | 79 | 53.2% | −0.125 |
| **>168h** | **76** | **28.9%** | **−0.447** |

**30-point WR gap between fresh (≤24h, 58.7% WR) and stale (>168h, 28.9% WR).**

Data quirk worth flagging: box_age is bimodal. The 72-168h range has 0 trades.
Most trades are EITHER fresh (<48h) or stale (>168h, i.e., >1 week old). Middle range empty.

## Per-pocket independence test

For each (pair_family, direction): does fresh (≤72h) WR exceed stale (>72h) WR?

| Pocket | n_fresh | n_stale | fresh_WR | stale_WR | wr_diff | Verdict |
|---|---|---|---|---|---|---|
| eur_cross / long | 4 | 7 | 100.0% | 28.6% | **+71.4** | ✓ yes (small n) |
| antipodean / long | 6 | 14 | 50.0% | 14.3% | **+35.7** | ✓ yes |
| antipodean / short | 23 | 8 | 52.2% | 25.0% | **+27.2** | ✓ yes |
| usd_base / long | 17 | 4 | 47.1% | 25.0% | **+22.1** | ✓ yes |
| gbp_cross / short | 4 | 7 | 50.0% | 28.6% | **+21.4** | ✓ yes (small n) |
| usd_base / short | 19 | 19 | 52.6% | 36.8% | **+15.8** | ✓ yes |
| eur_cross / short | 5 | 10 | 40.0% | 40.0% | 0 | flat |
| gbp_cross / long | 1 | 7 | 100% | 28.6% | — | n too small |

**6 of 7 testable pockets show fresh-box advantage. Only eur_cross/short was flat.**

## Session control

Per session, does fresh still beat stale? (ignoring pair_family)

| Session | n_fresh | n_stale | fresh_WR | stale_WR | wr_diff |
|---|---|---|---|---|---|
| asia | 45 | 40 | 44.4% | 35.0% | +9.4 |
| london | 20 | 28 | 70.0% | 25.0% | **+45.0** |
| ny_pm | 4 | 3 | 100% | 33.3% | +66.7 |
| overlap | 10 | 5 | 40.0% | 0% | +40.0 |

**All 4 sessions show fresh-box advantage. Signal is NOT a session proxy.**

## Is fresh box a pocket-proxy?

Strong pockets (usd_base + antipodean): fresh WR 50.8% vs stale 26.7% (gap 24.1)
Weak pockets (eur + gbp crosses): fresh WR 64.3% vs stale 32.3% (gap 32.0)

**Signal is actually STRONGER in the weak pockets.** Definitively NOT concentrated
in usd_base/antipodean — it generalizes.

Fresh-box trades are roughly evenly distributed across sessions (52.9% asia, 41.7%
london, 57.1% ny_pm, 66.7% overlap). Not concentrated in any single session.

## Validation verdict

| Independence test | Result |
|---|---|
| Holds across (pair_family × direction) pockets | **6/7 yes, 1 flat** |
| Holds across session_buckets | **4/4 yes** |
| NOT concentrated in strong pockets | **confirmed** (actually stronger in weak) |
| NOT a session proxy | **confirmed** (even distribution) |
| Sample size adequate | **yes** (n_fresh=79, n_stale=76 global) |
| Effect size | **+30 WR pts global, +15 to +71 per pocket** |

**box_age_hours is independently useful. Validation passes.**

Per locked protocol: `candidate_filter` status moves from `under_review` to
`validation_passed`. ADR consideration is now your call.

## Caveats / known concerns before ADR

- **Bimodal data**: ~50% of trades have box_age <48h, ~50% have >168h, ~0 in between.
  This is suspicious. Possible explanations:
  - The bot has TWO box-formation paths (e.g., fresh daily reset vs alt-box that persists)
  - The >168h trades are alt-box entries that never got their primary box recomputed
  - Weekend gaps + intraday vs overnight scanning
  - Before ADR, the bimodality should be diagnosed structurally (which V3 code path
    generates each)

- **`>168h` is a very wide tail bucket** — could include trades on boxes weeks or
  months old (max observed: 428h = 18 days). Need to see if the signal is
  monotone (older = worse) or if it's a step function at some threshold

- **n=4 in some pockets** (eur_cross/long, gbp_cross/short fresh) — directional signal
  is consistent but per-pocket statistical confidence is weak

- **Same-cell loser comparison** wasn't done in detail at this pass. Could be added
  (e.g., usd_base/short fresh winners vs usd_base/short fresh losers — what makes
  fresh trades that fail different from fresh trades that win?)

## What's locked vs what's NOT yet locked

**Locked finding:** box_age_hours separates winners from losers consistently across
pockets, directions, and sessions. The signal is real and independent.

**Not yet locked:**
- The exact threshold (24h? 48h? 72h?) — depends on the bimodality story
- Whether the signal is monotone or step-function
- Whether the bot should HARD-BLOCK stale-box trades or SOFT-WEIGHT them
- Whether to combine with other signals (e.g., box_age + spread + wall_proximity
  could be a multi-factor entry gate)

## What ADR would need (when authorized)

1. Structural diagnosis of the bimodal box_age distribution
2. Choice of threshold (probably 48-72h based on data)
3. Block vs weight decision
4. Live A/B specification: how to measure if the filter works
5. Rollback criteria

## What's queued (per scope)

- Bimodal-distribution diagnostic on box_age values (cheap)
- Same-cell winners-vs-losers within fresh-box subset (cheap)
- Sister-factor validation: do `wall_proximity`, `current_volume`, `spread_pips`
  hold up to the same independence test? (similar method, ~30 min)
- THEN ADR (only if structurally diagnosed)