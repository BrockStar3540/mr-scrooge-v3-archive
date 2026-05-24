# Missing Strategy Gap: Box Theory + Double Bollinger Band — CLOSED 2026-05-22

> ⚠️ **Naming disambiguation**: V3 has live modules named `dbb_trend` and `box_v3_shadow`. They are **NOT** the canonical textbook strategies. The canonical Lien Double BB (1σ + 2σ trend-zone) and canonical Darvas Box Theory (N-bar + K-bar consolidation breakout) are offline-replayed in this directory only. See `wiki/systems/scrooge-strategy-naming-disambiguation.md` in the vault for the four-namespace map.


## Status: CLOSED

Per Brock's 2026-05-22 directive: "Do not freeze at 'gap acknowledged.' Close the gap and test it."

The gap is now closed. Box Theory and true Double Bollinger Band have been sourced from canonical literature, implemented in the corpus, replayed across 26 pairs × 6 years, and ranked against the v1.9 live bank.

## What was missing

- **Box Theory**: zero strategy_ids in the original trade_log corpus matched. Spec was 66 strategies; corpus had 56 (gap of 10).
- **True Double Bollinger Band**: only `MR2_bb_reversion` (single 2σ-band mean-reversion fade) was in the corpus. True DBB (Kathy Lien) uses TWO bands (1σ + 2σ) and is **trend-following**, not mean-reversion. `MR2_bb_reversion` is the opposite strategy.

## What was added (10 new strategies)

| strategy_id | source | type |
|---|---|---|
| `BX1_darvas_box_breakout_long/short` | Darvas (1960) | breakout above/below 20-bar / 5-bar consolidation box |
| `BX2_darvas_box_retest_long/short` | Darvas | breakout + retest within 5 bars |
| `DBB1_buy_zone_long` / `DBB1_sell_zone_short` | Lien (2002) | close ∈ [bb_1σ, bb_2σ] zone entry |
| `DBB2_buy_zone_confirmed_long` / `DBB2_sell_zone_confirmed_short` | Lien | zone + EMA20_slope5 trend confirmation |
| `DBB3_buy_zone_sustained_long` / `DBB3_sell_zone_sustained_short` | Lien | zone held 2 consecutive bars |

Implementation: `~/scrooge-rebuild/supplement_box_dbb/backtest_box_dbb.py` (Mac Mini)
Canonical rules + adaptation: `~/scrooge-rebuild/supplement_box_dbb/canonical_rules.md`

## Replay scope

- 26 pairs (all live-bot pairs)
- 355 weeks (2019-07-01 → 2026-04-21)
- 5,696,714 total events generated
- 10/12/ratchet relabel applied (matches v1.9 methodology line-for-line)

## Result vs v1.9

**6 cells** technically pass v1.9 selection rules (n≥50, amb≤0.85, E[pips]/trade≥0.15) AND match/beat v1.9's lowest E[pips]/wk floor (0.43):

1. DBB1 USD_JPY C02 long asia → +1.589 pips/wk (would rank #4 in v1.9)
2. DBB2 USD_JPY C02 long asia → +1.507
3. DBB3 USD_JPY C01 long london → +0.690
4. BX2 USD_JPY C02 long london → +0.544 (but n_clean=99, borderline)
5. DBB3 AUD_JPY C01 long asia → +0.454
6. DBB3 USD_JPY C01 long asia → +0.451

## With diversity caps applied (3 cells/pair, 2 cells/strategy)

- USD_JPY is already at v1.9's 3-cell cap → cannot add more without displacing existing
- DBB1/DBB2/DBB3 USD_JPY C02 asia long are the same edge restated
- All 6 candidates are LONG; zero DBB or Box Theory shorts cleared the floor

**Net actionable**: 1 cell. `DBB3_buy_zone_sustained_long AUD_JPY C01 long asia` is the clean candidate for v1.10 — adds DBB family coverage + AUD_JPY pair coverage (v1.9 has only 1 AUD_JPY cell).

## Box Theory specifically

- Best Box cell (BX2 USD_JPY C02 long london at +0.544) has n=99 — too thin
- Median Box Theory WR is 10-15% under 10/12/ratchet, vs v1.9 cells at 36-44%
- Structurally similar to RG1/RG2/BR1 range strategies already covered
- **Net**: Box Theory replay confirms the gap was real but the gap was small. ~0 cells worth deploying

## DBB sell-side note

Zero DBB short cells cleared the floor. Either:
- DBB sell-zone fundamentally underperforms in this corpus (real signal), or
- Long-bias artifact from 6-year JPY pair appreciation (selection effect)

Worth a focused debug pass, not blocking.

## Out of scope / non-blocking

- OHLC ambiguity resolution (still 69% of corpus ambiguous under MFE/MAE)
- Boundary-thin / sibling expansion around the 6 DBB candidates
- Other potentially-missing textbook strategies (any not yet enumerated)

## Files

All on Mac Mini (CPYQTH294R) at `~/scrooge-rebuild/supplement_box_dbb/`:
- `canonical_rules.md` — sourcing + FX M5 adaptation
- `backtest_box_dbb.py` — strategy implementation + replay
- `supplement_rebuild.py` — 10/12/ratchet relabel + v1.9 comparison
- `deliverables_summary.md` — full deliverables index
- `outputs/trade_log_supplement_<pair>.parquet` × 26 — per-pair trade logs (gitignored, ~470MB total)
- `outputs/supplement_rebuild_10sl_12tp_ratchet.csv` — all 7,378 cells
- `outputs/supplement_ranked_parent_seeds.csv` — 16 parent seeds
- `outputs/supplement_ranked_island_candidates.csv` — 68 island candidates
- `outputs/supplement_rebuild_summary.md` — family + top-20 summary
- `outputs/v1_9_comparison.md` — explicit go/no-go verdict
