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
| [trend](#trend) | continuation | sidelined | 80% | 27/27 | Legacy V3 family — V4 deletion candidate (see entry) |
| [trend_aligned_breakout](#trend_aligned_breakout) | breakout | conditional | 72% | 20/27 | HTF-confluence breakout, narrow coverage |
| [canonical_lien_dbb](#canonical_lien_dbb) | continuation | ✓ | 78% | 25/27 | Current — DBB derivative |
| [canonical_darvas](#canonical_darvas) | box | conditional | **n/a** | **0/27 in matrix** | **Coverage gap** — see entry |
| [trend_pullback](#trend_pullback) | continuation | ✓ (promoted 2026-05-27) | 81% | 27/27 | Current |
| [chaikin_macd_atr](#chaikin_macd_atr) | continuation | ✓ (promoted 2026-05-27) | 81% | 27/27 | Current |
| [compression_expansion](#compression_expansion) | breakout | ✓ (promoted 2026-05-27) | 80% | 27/27 | Current |
| [compression_reversion](#compression_reversion) | reversion | ✓ (promoted 2026-05-27, **regime-mismatched**) | tiny n | n/a | Entry pending Phase 3 |
| [ifvg](#ifvg) | other (inverse FVG) | ✓ (promoted 2026-05-27) | 81% | 27/27 | Current |
| [session_breakout](#session_breakout) | breakout | ✓ (promoted 2026-05-27) | 80% | **8/27** | Current — narrow pair coverage |
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

## canonical_lien_dbb

**Family:** continuation (DBB-derived; simpler variant of `dbb_trend`
focused on the structural-stop side of the entry rather than the
breakout/pullback mode distinction).

**Signal philosophy.** A leaner DBB strategy. Where `dbb_trend`
branches on breakout vs pullback modes, `canonical_lien_dbb` uses a
single entry condition: price tags an outer Bollinger band and
the prior swing-low/high provides the structural stop (the "lien"
the trade is filed against). Routes shorter pullback geometries than
the breakout-flavored `dbb_trend`.

**Probe code reference.** `src/scrooge/strategies/canonical_lien_dbb.py`

**Stop / TP geometry + management profile.**
- Stop: prior swing low (long) / high (short) + small buffer
- TP: variable; matrix-cell driven
- Management: `default` (`early_hold_r=0.5, min_sl_step_pips=3.0`)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 4,177 | 79.7% | 6.16 | 3.41 |
| short | 4,197 | 76.4% | 5.60 | 3.42 |

- **25/27 pair coverage** (two pairs missing — likely thin lab data)
- 123 long + 125 short cells in the matrix
- Direction-symmetric — slight long-side advantage on exp_pips

**Known limitations / failure modes.**
- 2 pairs without matrix data — admission for those pairs will be
  abstained until next module rebuild (Task #41) fills coverage
- Same regime sensitivity as `dbb_trend` — counter-trend bets on
  strong directional days bleed unless HTF gate catches misalignment

**Related strategies.**
- `dbb_trend` — same DBB family, different entry-mode logic
- `trend_pullback` — non-DBB pullback equivalent

---

## canonical_darvas

**Family:** box (Darvas-style rolling-N-day box construction)

**⚠️ Coverage gap.** No matrix data, no factor_lift_table data as of
2026-05-30. Strategy is registered in `bootstrap.py` but absent from
the lab corpus mining. Same gap pattern as `reversal` — queued for
Task #41 (Phase 3 module rebuild).

**Signal philosophy.** Nicolas Darvas's box theory adapted for forex.
Rolling N-day highs / lows form a "box" the price action stays inside
until a breakout. Long when price closes above the box top; short on
box-bottom breakdown. Differs from `box_master_theory` in that the
box construction is rolling-N (not previous-day-only) and the trade
direction is breakout (not reversal).

**Probe code reference.** `src/scrooge/strategies/canonical_darvas.py`

**Stop / TP geometry + management profile.**
- Stop: opposite edge of the box
- TP: box-height projection beyond the breakout
- Management: `default`

**Lab-measured behavior.** **n/a — strategy not in lab corpus.**

**Live behavior.** Routed conditionally when matrix has no cells.
Effectively dormant in current live deployment.

**Known limitations / failure modes.**
- Coverage gap is the primary limitation; cannot make confident
  admission decisions without lab-mined factor lift
- Like `box_master_theory`, sensitive to noisy box geometry on
  range-bound days

**Related strategies.**
- `box_master_theory` — different box construction (PDH/PDL)
- `compression_expansion` — different breakout shape (vol-coil)

---

## chaikin_macd_atr

**Family:** continuation (momentum-confluence trend-follow)

**Signal philosophy.** Triple-confluence trend continuation. The
strategy fires when Chaikin Money Flow (volume-weighted accumulation/
distribution) AND MACD histogram AND ATR-normalized momentum all
align in the same direction. Conceptually the "everything points the
same way" version of trend-follow — sacrifices entry frequency for
confluence-driven WR.

**Probe code reference.** `src/scrooge/strategies/chaikin_macd_atr.py`

**Stop / TP geometry + management profile.**
- Stop: ATR-based (1.5 × ATR_5m typical)
- TP: matrix-cell driven, 2R typical
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,578 | 81.3% | 6.53 | 3.99 |
| short | 5,310 | 79.9% | 6.43 | 4.08 |

- 27/27 pair coverage
- 168 long + 166 short cells in the matrix
- Direction-symmetric, high WR — confluence requirement filters cleanly

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Limited
live trade volume in the first days post-promotion; per-strategy
audit pending Phase 3 module rebuild.

**Known limitations / failure modes.**
- Confluence requirement = low fire rate; misses trends that only
  one of the three signals catches
- Chaikin Money Flow on OANDA is approximate (no true order-book
  depth) — relies on tick-volume proxy

**Related strategies.**
- `trend_pullback` — looser confluence (no volume requirement)
- `dbb_trend` — DBB-based trend version

---

## compression_expansion

**Family:** breakout (volatility-compression → expansion shape)

**Signal philosophy.** Bollinger Band width compressing below
historical norm signals stored energy; subsequent expansion is the
release. Fires LONG on upward expansion from compression, SHORT on
downward expansion. The "squeeze + release" classic, refined with
ATR-relative thresholds for compression detection.

**Probe code reference.** `src/scrooge/strategies/compression_expansion.py`

**Stop / TP geometry + management profile.**
- Stop: BB midline (target-side stop — gives room for the expansion)
- TP: opposite Bollinger band on the expansion side
- Management: `trend_runner` (the expansion can run; let it)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 4,916 | 81.4% | 6.33 | 3.76 |
| short | 5,124 | 79.2% | 6.12 | 3.78 |

- 27/27 pair coverage
- 152 long + 156 short cells in the matrix
- Direction-symmetric

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Sub-variant
naming (CE_*) appears in attribution logs.

**Known limitations / failure modes.**
- Compression detection is threshold-sensitive; choppy markets with
  brief compressions produce false signals
- BE config A/B sweep deferred to v1.14c per ADR 3016 — current BE
  geometry may not be optimal for this strategy

**Related strategies.**
- `CP1_coil_breakout` (Phase 3 sidelined) — same family, different
  thresholds
- `CP2_squeeze_momentum_long` (Phase 3 sidelined) — adds momentum
  filter
- `compression_reversion` — same compression detector, opposite
  direction (mean-revert thesis)

---

## trend_pullback

**Family:** continuation (intraday trend + pullback to mean)

**Signal philosophy.** Identify an established intraday trend (slope
of EMA + ADX threshold) and wait for a shallow pullback to a
designated mean (EMA20 or fib retracement). Fire continuation
in the trend's direction on resumption signal. The "buy the dip
in an uptrend" textbook trade, formalized.

**Probe code reference.** `src/scrooge/strategies/trend_pullback.py`

**Stop / TP geometry + management profile.**
- Stop: prior swing extreme (last pullback low/high)
- TP: prior trend leg height projection
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,125 | 81.3% | 6.27 | 3.74 |
| short | 5,289 | 80.8% | 6.42 | 3.96 |

- 27/27 pair coverage
- 156 long + 165 short cells in the matrix
- Direction-symmetric — slight short-side edge in pips

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Sub-variant
`ITP_pullback_long` appears in broker truth — small sample (n=2, both
losses in the 27d window).

**Known limitations / failure modes.**
- Pullback definition is loose; can fire on noise that retraces to
  EMA20 without being a real countertrend wave
- The TF2_pullback_EMA20 Phase 3 finding (wrong-direction in this
  corpus regime) is a cousin pattern — worth cross-referencing once
  Phase 3 numbers land for `trend_pullback` specifically

**Related strategies.**
- `TF2_pullback_EMA20_long/short` (Phase 3) — same shape, different probe
- `dbb_trend` PULLBACK mode — DBB-version
- `chaikin_macd_atr` — confluence-version

---

## ifvg

**Family:** other (Inverse Fair Value Gap — ICT concept)

**Signal philosophy.** A Fair Value Gap (FVG) is a 3-candle pattern
where candle[1].high < candle[3].low (bullish gap) or candle[1].low >
candle[3].high (bearish gap). The "inverse" version trades into the
unfilled gap — long into bullish gaps expecting return-to-mean,
short into bearish gaps. ICT lineage; this is the strategy that the
broader ICT-derived strategy spec (HTF_PO3_SMT) was hoping to add as
a more sophisticated framework eventually.

**Probe code reference.** `src/scrooge/strategies/ifvg.py`

**Stop / TP geometry + management profile.**
- Stop: opposite side of the gap
- TP: mean of the gap (filling) + extension to next swing
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,866 | 81.4% | 6.54 | 4.08 |
| short | 5,808 | 80.2% | 6.66 | 4.45 |

- 27/27 pair coverage
- 169 long + 167 short cells in the matrix
- Direction-symmetric

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Sub-variants
`IFVG_v1_long`, `IFVG_v1_short` appear in broker truth. Small live
sample so far; IFVG_v1_short showed 0/2 W in the post-promotion
window, IFVG_v1_long 1/1 W.

**Known limitations / failure modes.**
- FVG detection requires reliable candle data — broker-side gap
  artifacts (e.g., weekend gaps) can produce false signals
- "Mean reversion into gap" thesis is regime-dependent; in strong
  directional regimes the gap continues to be ignored rather than
  filled

**Related strategies.**
- The HTF_PO3_SMT_Strategy_Spec (Phase 4 backlog candidate) would
  build on IFVG by adding the broader Power-of-Three context

---

## session_breakout

**Family:** breakout (session-anchored opening range)

**Signal philosophy.** Each trading session (Tokyo, London, NY) opens
with an opening range. After ~30 minutes, the high and low of that
opening range become breakout levels. Fire LONG on close above the
range, SHORT on close below. Session-anchored timing is the key
ingredient.

**Probe code reference.** `src/scrooge/strategies/session_breakout.py`

**Stop / TP geometry + management profile.**
- Stop: opposite side of opening range
- TP: 1× or 2× opening-range height projection
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 782 | 82.2% | 6.54 | 4.02 |
| short | 774 | 77.4% | 5.43 | 3.36 |

- **8/27 pair coverage** (much lower than other promoted strategies)
- 25 long + 25 short cells in the matrix
- Long-direction advantage (~5pp WR + better exp_pips and lift)

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Limited
fire rate by design — only 8 pair-coverage means it's silent for ~70%
of the pair universe.

**Known limitations / failure modes.**
- Low pair coverage (8/27) — most pairs don't have meaningful
  session-anchored breakout edge in the lab data
- Session boundary definitions assume canonical Tokyo/London/NY hours;
  daylight savings shifts and broker session quirks can confuse the
  opening-range computation
- Asymmetric direction edge (long > short) suggests the lab regime
  favored upward breakouts; may invert in other regimes

**Related strategies.**
- `BR5_opening_range_breakout` (Phase 3 sidelined) — same shape,
  different threshold defaults; Phase 3 lab showed it as a strong
  variant (~$4.5M PnL, 6/27 pair concentration warning)
- `compression_expansion` — different breakout trigger (BB squeeze)

---

## trend

**Family:** continuation (legacy V3 trend strategy — sidelined)

**Signal philosophy.** The V3-era "trend" strategy: identify a
prevailing trend via EMA/ADX, enter on confirmation. Predates the
DBB-specific variants. Effectively superseded by `dbb_trend`,
`canonical_lien_dbb`, and `trend_pullback` — those are sharper-edged
versions of the same idea.

**Sidelined status.** Registered in `bootstrap.py` but explicitly
sidelined in routing — the routing table doesn't admit `trend` cells.
The strategy code is preserved for backward compatibility and as a
fallback if all newer trend variants are disabled simultaneously.

**Probe code reference.** `src/scrooge/strategies/trend.py`

**Stop / TP geometry + management profile.**
- Stop: ATR-based (default)
- TP: 2R typical
- Management: `trend_runner`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,250 | 80.2% | 6.24 | 3.87 |
| short | 5,332 | 79.3% | 6.42 | 3.93 |

- 27/27 pair coverage in matrix (was mined when strategy was active)
- 162 long + 164 short cells

**Live behavior.** Zero live trades since sidelined. Lab data only.

**Known limitations / failure modes.**
- Superseded — its admission space is fully covered by sharper-edged
  successors
- At V4 cutover (Task #57 code archaeology), `trend` is a deletion
  candidate. Decision deferred until Phase 3 confirms the newer
  trend variants are robust enough to fully replace it

**Related strategies.**
- All other continuation-family strategies are direct successors

---

## trend_aligned_breakout

**Family:** breakout (HTF-trend-aligned breakout)

**Signal philosophy.** Breakout trade with explicit HTF (1H/4H)
trend-alignment requirement. Fires LONG only when both M5 breakout
condition AND HTF1 trend is up AND HTF4 trend is up (or aligned-with).
The HTF-aligned subset of breakouts — sacrifices fire rate for
WR + directional confidence.

**Probe code reference.** `src/scrooge/strategies/trend_aligned_breakout.py`

**Stop / TP geometry + management profile.**
- Stop: structural breakout-base
- TP: variable
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 931 | 72.4% | 5.92 | 3.25 |
| short | 1,871 | 72.5% | 5.96 | 3.49 |

- **20/27 pair coverage** (7 pairs missing — likely thin breakout-aligned data)
- 30 long + **60 short** cells (2× short-side cells — bearish-regime
  artifact in the corpus)
- Direction-symmetric WR despite the cell-count asymmetry
- Lower WR than the matrix average (~80%) — confluence requirements
  produce a tighter cohort but at lower per-cell quality

**Live behavior.** Routed conditionally where cells exist. Limited
fire rate by design.

**Known limitations / failure modes.**
- Asymmetric cell count (60 short vs 30 long) reflects the bearish
  corpus regime — short-direction had more confluence-aligned setups
  during the lab window. Will likely rebalance in different regimes
- 7-pair coverage gap means it's silent on some major pairs
- The "confluence sacrifice" trade-off (fewer fires for higher
  directional confidence) means it underperforms volume-greedy
  variants like `BR2_vcb` in raw PnL

**Related strategies.**
- `compression_expansion`, `session_breakout` — different breakout triggers
- `chaikin_macd_atr` — different confluence framework
- The HTF gate ([ADR 3015](decisions/3015-htf-trend-filter-observe-to-hard.md))
  applies a similar filter at the system level — `trend_aligned_breakout`
  is the strategy-internal version of that filter


---

# Pending entries (Phase 3 module rebuild needed)

The following strategy entries are queued for fill-in once the Phase 3
sweep (Task #40) completes and the module rebuild (Task #41) lands.
Each follows the same 9-field template. Phase 3 produces per-variant
lab metrics; the rebuild produces routing-table cells per (pair ×
regime × strategy × direction); together they fill the encyclopedia's
"Lab-measured behavior" + "Live behavior" sections.

Pending V3-promoted families (only `compression_reversion` left from this group):
- ~~`canonical_lien_dbb`~~ — **entry written** (matrix data, 25/27 pairs)
- ~~`canonical_darvas`~~ — **entry written** (coverage gap noted)
- ~~`trend_pullback`~~ — **entry written** (matrix data, 27/27 pairs)
- ~~`chaikin_macd_atr`~~ — **entry written** (matrix data, 27/27 pairs)
- ~~`compression_expansion`~~ — **entry written** (matrix data, 27/27 pairs)
- `compression_reversion` — regime-mismatched, very low n; entry pending Phase 3 confirmation
- ~~`ifvg`~~ — **entry written** (matrix data, 27/27 pairs)
- ~~`session_breakout`~~ — **entry written** (matrix data, 8/27 pairs — narrow coverage)

**Pending probes_v2 family** (10 NATO-phonetic probes from `src/scrooge/strategies/probes_v2.py`,
all default-DISABLED — fan in one at a time per Phase 3 evidence). **None of these are in the
matrix yet** — they enter for the first time via Task #41 module rebuild after Phase 3.

| Probe | Live family | Description | Phase 3 sweep |
|---|---|---|---|
| `alpha_pullback_v2` | dbb_trend | continuation pullback | ✓ |
| `alpha_breakout_retest_v2` | direct | breakout retest | ✓ |
| `alpha_extended_fade_v2` | reversal | extension fade | ✓ |
| `bravo_failed_momentum` | reversal | failed-momentum fade | ✓ |
| `bravo_expansion_continuation` | dbb_trend | range expansion | ✓ |
| `charlie_pullback_continuation_v2` | dbb_trend | continuation (**$297M Phase 3 compounder** — needs forensic) | ✓ |
| `charlie_compression_breakout` | direct | compression breakout | ✓ |
| `delta_tag_and_go_v2` | direct | tag-and-go continuation | ✓ |
| `echo_box_fade_v2` | reversal | rail fade | pending Phase 3 33/34 |
| `echo_failed_breakout_v2` | reversal | failed-break fade | pending Phase 3 34/34 |

Pending textbook_scalper family — 22 variants from `src/scrooge/strategies/textbook_scalper.py`,
**none in matrix yet** (matrix re-mine via Task #41 brings them in):

- **BR family (breakouts):** BR2_vcb_long, BR2_vcb_short,
  BR3_inside_bar_long, BR3_inside_bar_short, BR5_opening_range_breakout_long,
  BR5_opening_range_breakout_short
- **CP family (coils):** CP1_coil_breakout_long, CP1_coil_breakout_short,
  CP2_squeeze_momentum_long, CP3_vol_coil_fade_long, CP3_vol_coil_fade_short
- **MR family (mean-reversion):** MR2_bb_reversion_short,
  MR4_zscore_extreme_long, MR4_zscore_extreme_short,
  MR5_williams_extreme_long, MR5_williams_extreme_short
- **RG family (range scalps):** RG1_range_bound_scalp_long,
  RG1_range_bound_scalp_short, **RG2_range_support_bounce_long** (0 trades in
  Phase 3 sweep — probe may be broken, verify before encyclopedia entry)
- **TF family (trend-follow pullbacks):** TF2_pullback_EMA20_long,
  TF2_pullback_EMA20_short, **TF4_sar_long** (Parabolic SAR trend-follow,
  promoted in Phase 3 sweep)

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
