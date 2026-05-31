# Strategy Encyclopedia

The reference document for all ~25 trading strategies in Mr. Scrooge
V4. Each strategy gets the same template and equal footing. No
strategy is the "main one"; the routing table decides which fires for
which (pair × regime × session) cell.

Companion to [`LIVE_SYSTEM_SPEC.md`](LIVE_SYSTEM_SPEC.md) (what the
system does today) and [`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md)
(how strategies got measured).

---

## How to use this doc

**If you're picking a strategy to trust** — read the lab numbers and
the limitations. Lab data measures behavior over the Nov 2025 →
May 2026 corpus; live transferability is not guaranteed.

**If you're adding a strategy** — copy the template below, follow the
fields, run it through the lab, and add the entry. The
[lab reproduction guide](LAB_REPRODUCTION_GUIDE.md) covers the steps.

**If you're debugging a live trade** — check the strategy's failure
modes first, then cross-reference the regime + session in
`order-attribution.jsonl` to find the matching cell in the routing
table.

---

## Per-strategy template

Every entry has the same 9 fields:

1. **Name + canonical strategy_id** — the string used in
   `order-attribution.jsonl`, ML observer logs, and routing table.
2. **Family** — one of: reversion / continuation / box / breakout /
   other. Affects which other strategies share its routing-cell space.
3. **Signal philosophy** — one paragraph on what market behavior the
   strategy tries to capture.
4. **Probe code reference** — path to the strategy module + the entry
   conditions in pseudocode.
5. **Stop / TP geometry + management profile** — exit shape.
6. **Lab-measured behavior** — corpus WR, expected pips, pair
   coverage (X/27), regime applicability (X/20), direction asymmetry
   (native vs reversed).
7. **Live behavior** (if applicable) — recent broker-truth slice.
8. **Known limitations / failure modes** — when this strategy is
   known to misfire.
9. **Related strategies** — see-also references.

---

## Taxonomy summary

All ~25 strategies at a glance. Lab numbers are corpus aggregates;
see per-entry detail for breakdowns.

| Strategy | Family | Routed live | Lab WR | Lab pair coverage | Status |
|---|---|---|---|---|---|
| [box_master_theory](#box_master_theory) | box | ✓ | 81% | 27/27 | Current — V1 lineage, now equal footing |
| [dbb_trend](#dbb_trend) | continuation | ✓ | 77% | 27/27 | Current — V3 family workhorse |
| [direct](#direct) | other | ✓ (fallback) | 82% | 27/27 | Current — fallback admission path |
| [reversal](#reversal) | reversion | registered (rarely routes) | n/a | **0/27 in matrix** | **Coverage gap** — see entry |
| [trend](#trend) | continuation | sidelined | n/a | n/a | Legacy V3 family, kept registered |
| [canonical_lien_dbb](#canonical_lien_dbb) | continuation | ✓ | 78% | 27/27 | Current — DBB derivative |
| [canonical_darvas](#canonical_darvas) | box | conditional | TBD | TBD | Entry pending Phase 3 |
| [trend_pullback](#trend_pullback) | continuation | ✓ (promoted 2026-05-27) | TBD | TBD | Entry pending Phase 3 |
| [chaikin_macd_atr](#chaikin_macd_atr) | continuation | ✓ (promoted 2026-05-27) | TBD | TBD | Entry pending Phase 3 |
| [compression_expansion](#compression_expansion) | breakout | ✓ (promoted 2026-05-27) | TBD | TBD | Entry pending Phase 3 |
| [compression_reversion](#compression_reversion) | reversion | ✓ (promoted 2026-05-27, **regime-mismatched**) | tiny n | n/a | Entry pending Phase 3 |
| [ifvg](#ifvg) | other (inverse FVG) | ✓ (promoted 2026-05-27) | TBD | TBD | Entry pending Phase 3 |
| [session_breakout](#session_breakout) | breakout | ✓ (promoted 2026-05-27) | TBD | TBD | Entry pending Phase 3 |
| BR2_vcb (long + short) | breakout | sidelined | ~62% lab | 27/27 | Phase 3 lab winner, **promotion pending** |
| BR3_inside_bar | breakout | sidelined | 63% lab / loser | 27/27 | Phase 3 lab loser — drop candidate |
| BR5_opening_range_breakout (long + short) | breakout | sidelined | ~61% lab | 27/27 | Phase 3 lab winner, promotion pending |
| CP1_coil_breakout (long + short) | breakout | sidelined | ~62% lab | 27/27 | Phase 3 lab winner, promotion pending |
| CP2_squeeze_momentum_long | breakout | sidelined | ~62% lab | 27/27 | Phase 3 lab winner, promotion pending |
| CP3_vol_coil_fade (long + short) | reversion | sidelined | wrong-direction | 26-27/27 | Run reversed, promotion pending |
| MR2_bb_reversion_short | reversion | sidelined | wrong-direction | 27/27 | Run reversed, promotion pending |
| MR4_zscore_extreme (long + short) | reversion | sidelined | wrong-direction | 23-27/27 | Run reversed, promotion pending |
| MR5_williams_extreme (long + short) | reversion | sidelined | wrong-direction | 27/27 + narrow timing | Cautious promotion candidate |
| RG1_range_bound_scalp (long + short) | reversion | sidelined | wrong-direction | 27/27 | Run reversed, promotion pending |
| TF2_pullback_EMA20 (long + short) | other (pullback) | sidelined | wrong-direction | 27/27 | Run reversed, promotion pending |

**Coverage note:** "Lab WR" for current-routed strategies = corpus-mining
weighted aggregate from matrix. "Lab WR" for Phase 3 sidelined variants =
sweep-aggregate at default exit config. Lab numbers tied up in Phase 3
sweep completion (ETA Sun late / Mon AM 2026-05-31 / 06-01); entries
fill in as data lands.

---

## Glossary

- **Family** — the strategy's behavioral category. Determines routing-cell
  sharing (e.g., two continuation strategies compete for the same cells).
- **Routed live** — whether the strategy is admitted by the live MatrixRouter
  via the current `routing_table.parquet`. Some strategies are registered
  but not currently routed (`trend`, `reversal` currently).
- **Lab WR** — win rate over the 6mo corpus, weighted by trade count.
- **Pair coverage** — for how many of the 27 pairs the strategy generates
  enough trades to mine meaningful rules (>5 trades typically).
- **Regime applicability** — out of 20 KMeans regimes per pair, how many
  the strategy generates trades in.
- **Native / reversed** — Phase 3 lab tests each probe in both directions
  (the probe's coded direction, and its inverse). Direction asymmetry
  shows whether the probe is correctly directioned for the corpus regime.

---

# Strategy entries

---

## box_master_theory

**Family:** box (single-member family — only `box_master_theory` and
`canonical_darvas` qualify as box-shape strategies; everything else
is continuation/reversion/breakout flavored)

**Signal philosophy.** The original Mr. Scrooge V1 doctrine
([`MASTER_THEORY_v1-box-reversal-origin-2025.md`](archive/MASTER_THEORY_v1-box-reversal-origin-2025.md)
in the archive — the foundational document that defined the bot
through April 2026). The premise: each trading day forms a high-low
"box" (PDH / PDL). Liquidity sweeps at the box edges, followed by a
3-5-candle "sucker move" and a pitchfork-shaped entry pattern, signal
a reversal opportunity back toward the opposite box edge.

In V4, this is one of ~25 strategies and gets evaluated by the same
admission pipeline as everything else. The historical "this is THE
strategy" framing is preserved in `MASTER_THEORY_v1-box-reversal-origin-2025.md`;
operationally, `box_master_theory` is just an entry in the registry.

**Probe code reference.** `src/scrooge/strategies/box_master_theory.py`

Pseudocode:
```
candidate = box_master_theory.evaluate(symbol, features):
  if no PDH/PDL detected for symbol today:
    return None
  if not at_box_edge(features, proximity=0.25%):
    return None
  if not sucker_move_present(features, lookback=5, min_count=3):
    return None
  if not pitchfork_pattern(features.candles[-3:]):
    return None
  if not bb_exhaustion(features):
    return None
  direction = away_from_box_edge(features)
  return Candidate(symbol, direction, entry, stop, target)
```

**Stop / TP geometry + management profile.**
- Stop: signal candle extreme + buffer (typically 7p)
- TP1: 50% to mid-box (harvest)
- TP2: opposite box edge
- Management: `trend_runner` (`early_hold_r=0.6, min_sl_step_pips=4.0`)
  for trend-aligned firings; default for reversion-firings.

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 7,114 | 81.2% | 6.37 | 3.84 |
| short | 6,444 | 80.7% | 6.62 | 4.17 |

- 27/27 pair coverage
- 184 long cells + 180 short cells in the matrix
- Direction-symmetric — works both ways (consistent with reversal
  thesis — boxes form in any direction)

**Live behavior.** Routed live since V3 launch (2026-04-15). Per the
2026-05-30 27-day broker-truth audit: low live volume relative to
other live strategies (most fires happened pre-routing-table promotion).

**Known limitations / failure modes.**
- Box detection requires clean PDH/PDL geometry; range-bound days
  with multiple equal highs/lows confuse the detector
- Counter-trend bet by construction; bleeds in strong directional days
  unless the HTF gate ([ADR 3015](decisions/3015-htf-trend-filter-observe-to-hard.md))
  catches the directional alignment failure
- "Sucker move" detection has historically had high false-positive
  rate on choppy markets — the 3-5 candle window is permissive

**Related strategies.**
- `canonical_darvas` — different box construction (rolling N-day high)
- `reversal` — same reversion philosophy at non-box levels
- `compression_reversion` — same reversion intent at compressed-volatility moments

---

## dbb_trend

**Family:** continuation (the V3 family workhorse for trend-aligned
trades; routes into TREND_UP/DOWN, BREAKOUT_UP/DOWN, STRETCH_DOWN
historical BB states though those state mappings are subsumed by the
matrix router now).

**Signal philosophy.** Double Bollinger Band trend continuation. The
DBB strategy identifies two pattern types: **breakouts** (price closes
beyond the outer band signaling trend acceleration) and **pullbacks**
(price retraces to the inner band in an established trend, then
resumes). The strategy emits long candidates in uptrending DBB states
and short candidates in downtrending DBB states.

**Probe code reference.** `src/scrooge/strategies/dbb_trend.py`

Pseudocode:
```
candidate = dbb_trend.evaluate(symbol, features):
  bb_state = classifier.bb_state(features)  # TREND_UP/DOWN/BREAKOUT_UP/DOWN/STRETCH_DOWN

  if bb_state in {BREAKOUT_UP, BREAKOUT_DOWN}:
    mode = "BREAKOUT"
    direction = "long" if bb_state == BREAKOUT_UP else "short"
  elif bb_state in {TREND_UP, TREND_DOWN}:
    mode = "PULLBACK"
    direction = "long" if bb_state == TREND_UP else "short"
  elif bb_state == STRETCH_DOWN:
    mode = "BREAKOUT" ; direction = "short"
  else:
    return None

  return Candidate(symbol, direction, entry, stop, target)
```

**Stop / TP geometry + management profile.**
- Stop: structural (last swing low for longs / high for shorts)
- TP: variable based on mode (BREAKOUT goes for runners; PULLBACK
  takes 2R then trails)
- Management: `trend_runner` (`early_hold_r=0.6, min_sl_step_pips=4.0`)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 3,296 | 78.2% | 5.90 | 3.11 |
| short | 3,629 | 76.4% | 5.71 | 3.39 |

- 27/27 pair coverage
- 102 long cells + 113 short cells in the matrix
- Direction-symmetric within ~2pp

**Live behavior (27d broker-truth slice ending 2026-05-29):**
- 31 trades, 19% WR, sum −$6,659 (mean −$215/trade)
- Sub-variants firing: `DBB1_buy_zone_long` (0/6 W), `DBB2_buy_zone_confirmed_long`
  (0/7), `DBB3_buy_zone_sustained_long` (1/12), `DBB1_sell_zone_short` (1/5)
- The long-bias sub-variants (`*_buy_zone_long`) lost catastrophically in
  the bearish-friendly regime that dominated this 27d window
- The short-bias sub-variant `DBB3_sell_zone_sustained_short` was
  positive (6/13 W, +$269)

**Known limitations / failure modes.**
- Strongly regime-dependent: catastrophic when the prevailing trend
  reverses against the BB state's bias (the $5,350 streak diagnosed
  2026-05-04 was a `dbb_trend` family failure mode of this type)
- HTF gate (ADR 3015) is the structural fix — blocks counter-HTF
  direction admissions
- Sub-variant `_buy_zone_long` distribution showed 1/25 wins (4% WR)
  in the post-promotion window — under per-strategy audit

**Related strategies.**
- `canonical_lien_dbb` — DBB-derived simpler variant
- `trend_pullback` — non-DBB version of the pullback pattern
- `compression_expansion` — different breakout shape

---

## direct

**Family:** other (the fallback admission path — when no other
strategy emits a candidate but the matrix has WIN rules for the
current state, `direct` emits a generic candidate that the rules
themselves admit).

**Signal philosophy.** A backstop. Where strategies like
`box_master_theory` or `dbb_trend` only fire on specific patterns,
`direct` fires on any state where the matrix-mined rules say "this
combination of signature buckets has high WR." The strategy is
intentionally permissive at emission; the routing table + LightGBM gate
do the actual selection.

**Probe code reference.** `src/scrooge/strategies/direct.py`

Pseudocode:
```
candidate = direct.evaluate(symbol, features):
  for direction in ['long', 'short']:
    if matrix_router.has_admitted_cell(symbol, features, direction):
      return Candidate(symbol, direction, entry_at_market, stop, target)
  return None
```

**Stop / TP geometry + management profile.**
- Stop: ATR-based (default 1.5 × ATR_5m)
- TP: matrix-mined cell's mean R_optimized × ATR_5m
- Management: `default` (`early_hold_r=0.5, min_sl_step_pips=3.0`)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,990 | 83.2% | 7.05 | 4.47 |
| short | 5,943 | 81.6% | 6.80 | 4.45 |

- 27/27 pair coverage
- 173 long cells + 176 short cells in the matrix
- **Highest weighted WR in the matrix** (83% long / 82% short) —
  unsurprising since `direct` admissions are filtered to the
  highest-WR cells by construction

**Live behavior (27d broker-truth slice ending 2026-05-29):**
- 73 trades, 30% WR, sum −$13,052 (mean −$179/trade)
- Highest-volume strategy in the live broker truth window
- Net negative despite the highest lab WR — consistent with the bearish
  regime favoring shorts (the lab WR aggregates across regimes that
  weren't all present in the 27d live window)

**Known limitations / failure modes.**
- "Highest-volume + lowest realized WR" is the classic signature of a
  permissive emitter caught in a regime mismatch — the cells the matrix
  admitted aren't the cells the live regime is producing
- Reliance on matrix WIN rules means `direct` only fires when LightGBM
  ALSO admits; the failure mode is when LightGBM scores high (0.75+)
  but the realized regime isn't the historical regime that produced
  the WIN rule

**Related strategies.**
- All routed strategies share cells with `direct` — when a more
  specific strategy emits, it takes priority in scoring

---

## reversal

**Family:** reversion

**Signal philosophy.** The V3 family for sweep-reversal trades at
non-box levels — Bollinger Band extremes, RSI extremes, generic
liquidity-sweep-and-reject patterns. EXTREME and REJECTION mode
sub-variants. Conceptually the broader version of `box_master_theory`'s
reversal logic, applied to any level that produces a sweep + rejection.

**⚠️ Coverage gap.** As of 2026-05-30, `reversal` family **has no
entries in the lab matrix or per-pair modules.** The strategy is
registered in `bootstrap.py` and would be routed if the routing table
had cells for it, but the matrix was mined on a corpus that didn't
include `reversal`-family trades.

This is a known gap, queued for fix in [Task #41](https://github.com/BrockStar3540/mr-scrooge-v3/issues/41)
(Phase 3 module rebuild). Until then, `reversal` candidates that emit
are essentially abstained on by the live router (no admitted cells).

**Probe code reference.** `src/scrooge/strategies/reversal.py`

Pseudocode (abbreviated):
```
candidate = reversal.evaluate(symbol, features):
  mode = detect_mode(features)  # EXTREME or REJECTION
  if mode is None: return None
  direction = opposite_of_extreme(features)
  return Candidate(symbol, direction, entry, stop, target)
```

**Stop / TP geometry + management profile.**
- Stop: signal-candle extreme + buffer
- TP: variable based on mode
- Management: `reversal_core` (`early_hold_r=0.5, min_sl_step_pips=3.0`)

**Lab-measured behavior.** **n/a — strategy not in lab corpus.**

**Live behavior (27d broker-truth slice).** **0 trades.** The strategy
was registered but never routed during the 27d window (no admitted
cells in the routing table for `reversal`).

**Known limitations / failure modes.**
- The current "structural coverage gap" is itself the most important
  limitation. Until the strategy is in the matrix, we have no
  data-mined edge measurement for it
- Historically (V1/V2 era) reversal trades had ~75% WR on the
  documented NORMAL-regime cohort, but this is from the legacy
  hand-tuned doctrine, not the V4-era lab corpus
- Once added to the lab corpus + matrix in [Task #41], the encyclopedia
  entry will be updated with measured behavior

**Related strategies.**
- `box_master_theory` — reversal at PDH/PDL levels specifically
- `compression_reversion` — reversal at compressed-volatility moments
- `ifvg` — reversal into Fair Value Gap fills

---

# Pending entries (Phase 3 module rebuild needed)

The following strategy entries are queued for fill-in once the Phase 3
sweep (Task #40) completes and the module rebuild (Task #41) lands.
Each follows the same 9-field template. Phase 3 produces per-variant
lab metrics; the rebuild produces routing-table cells per (pair ×
regime × strategy × direction); together they fill the encyclopedia's
"Lab-measured behavior" + "Live behavior" sections.

Pending V3-promoted families:
- `canonical_lien_dbb` — partial matrix data; needs Phase 3 confirmation
- `canonical_darvas`
- `trend_pullback`
- `chaikin_macd_atr`
- `compression_expansion`
- `compression_reversion` (regime-mismatched, very low n)
- `ifvg`
- `session_breakout`

Pending Phase 3 sidelined-probe candidates (22 textbook_scalper +
related variants):
- **BR family (breakouts):** BR2_vcb_long, BR2_vcb_short,
  BR3_inside_bar_long, BR3_inside_bar_short, BR5_opening_range_breakout_long,
  BR5_opening_range_breakout_short
- **CP family (coils):** CP1_coil_breakout_long, CP1_coil_breakout_short,
  CP2_squeeze_momentum_long, CP3_vol_coil_fade_long, CP3_vol_coil_fade_short
- **MR family (mean-reversion):** MR2_bb_reversion_short,
  MR4_zscore_extreme_long, MR4_zscore_extreme_short,
  MR5_williams_extreme_long, MR5_williams_extreme_short
- **RG family (range scalps):** RG1_range_bound_scalp_long,
  RG1_range_bound_scalp_short
- **TF family (trend-follow pullbacks):** TF2_pullback_EMA20_long,
  TF2_pullback_EMA20_short

**Notable Phase 3 findings already known** (each gets its own entry
when filled):

- **Wrong-direction family pattern.** All 5 reversion-flavored families
  (MR2, MR4, MR5, RG1, CP3) showed strongly negative native-direction
  PnL and strongly positive reversed-direction PnL across 23-27/27
  pairs. The pattern was 100% week-by-week consistent for MR5 (26/26
  weeks). Reframed as "trade in the direction of the regime trend"
  rather than "flip the probe" — the HTF gate ([ADR 3015](decisions/3015-htf-trend-filter-observe-to-hard.md))
  is the durable expression.
- **TF2_pullback_EMA20** appeared as a large outlier ($1,578/trade ×
  80k trades × 27/27 positive pairs) — forensic confirmed real edge
  (compound growth on $50k seed equity, not artifact), but the
  "native direction" is structurally wrong-direction in the bearish
  corpus regime. Calibrated against external sources (TraderDale
  article, TradePro YouTube video) — both reported 60-63% WR for
  trend-filtered EMA20 pullback; our 61% raw is consistent.
- **BR3_inside_bar** was the only Phase 3 variant with net-negative
  aggregate PnL across the corpus. Drop candidate.

---

## Cross-references

- [`LIVE_SYSTEM_SPEC.md`](LIVE_SYSTEM_SPEC.md) — what the routing table
  currently admits and how the admission stack works
- [`ARCHITECTURE_DIAGRAM.md`](ARCHITECTURE_DIAGRAM.md) — visual map of
  the scan-to-execution flow including strategy emission
- [`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md) — how lab numbers
  in this doc were computed
- [`decisions/`](decisions/) — ADRs covering individual promotion +
  retirement decisions per strategy
- [`history/`](history/) — chronological story of which strategies
  came / went / changed family over V1 → V4
- [`archive/MASTER_THEORY_v1-box-reversal-origin-2025.md`](archive/MASTER_THEORY_v1-box-reversal-origin-2025.md)
  — the foundational V1 doctrine that originally defined
  `box_master_theory` (preserved as historical context)
