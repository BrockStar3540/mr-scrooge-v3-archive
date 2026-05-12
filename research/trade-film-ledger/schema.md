# Trade-Film Ledger — Schema and Provenance

type: research-infrastructure
status: locked-v1
tags: [scrooge, trade-film, ledger, research, micro-strategy]
date: 2026-05-12
trust: high

## Purpose

Unified ledger of every researchable trade — manual and broker-truth — under
a single schema, with strict separation of **actual trade truth** from
**audit-generated counterfactual repairs** and from **human review work**.

The ledger is the input layer for the trade-film micro-strategy workflow.
It is **not** a strategy. It is the lab notebook the strategy work happens in.

## Locked design rules

1. `actual_*` columns are **immutable trade truth**. They never change.
2. `audit_*` columns are **audit-generated counterfactual repair hypotheses**.
   They represent what the reverse-engineering audit thought the trade
   *could have* been with a local fix. They are NOT actual outcomes.
3. Forensic review columns (`can_be_legitimately_saved`, `save_method`,
   `micro_strategy_candidate`, `shared_features`, `review_status`, `notes`)
   are **empty by design** in ingestion. They get filled by human or
   downstream-script work, not by the ingester.
4. A losing trade can later be annotated as
   `can_be_legitimately_saved=TRUE, save_method="X"` — but its
   `actual_realized_r` stays negative forever. **Losers never quietly
   become winners.**
5. `source_label` is mandatory and identifies provenance + trust.
   Never mix sources without it.

## Ledger schema (50 columns)

### Identity (6)

| Column | Type | Purpose |
|---|---|---|
| `ledger_id` | uuid str | Stable row identity for cross-reference |
| `source_label` | enum | `manual_human` / `manual_ai_curated` / `bot_actual_winner` / `bot_actual_loser` / `bot_actual_unknown` |
| `source_file` | str | Originating CSV filename for provenance |
| `source_row_key` | str | Foreign key back to source row |
| `trust_score` | enum | `high` (broker truth / human manual) / `medium` (ai_curated) / `low` |
| `ingested_at` | ISO ts | When this row was ingested |

### Trade truth — immutable (15)

| Column | Type | Purpose |
|---|---|---|
| `pair` | str | OANDA instrument |
| `entry_ts` | ISO ts | Entry timestamp |
| `direction` | str | long / short |
| `strategy_label` | str | What the row's source said the strategy was (box / dbb_trend / direct etc.) |
| `session` | str | asia / london / ny / overlap (where source provides) |
| `regime_label` | str | V2 regime classification |
| `actual_realized_r` | float | **The truth.** Realized R-multiple |
| `actual_realized_pl` | float | Realized P&L in account currency (broker only) |
| `actual_exit_reason` | str | SL / TP / time / manual / etc. |
| `actual_mfe_r` | float | Max favorable excursion |
| `actual_mae_r` | float | Max adverse excursion |
| `actual_tp1_hit` | bool | TP1 touched |
| `actual_tp2_hit` | bool | TP2 touched |
| `actual_be_hit` | bool | Stop-at-BE triggered |
| `actual_ratchet_triggered` | bool | Ratchet activated |
| `actual_holding_minutes` | int | Trade duration |
| `actual_winner` | bool | `actual_realized_r > 0` (convenience) |

### Entry/stop geometry (5)

| Column | Type | Purpose |
|---|---|---|
| `entry_price` | float | |
| `stop_price` | float | |
| `tp1_price` | float | |
| `tp2_price` | float | |
| `stop_pips_or_price` | float | R-distance |
| `atr14` | float | ATR at entry |

### Factor snapshot link (4)

| Column | Type | Purpose |
|---|---|---|
| `factor_snapshot_id` | str | Joinable to `live_broker_factor_snapshots.jsonl` for broker rows; null for manual |
| `bb_position` | float | Bollinger Band position |
| `ema20_dist_pct` | float | Distance from EMA20 |
| `bb_band_width_a_bps` | float | BB width in bps |

### Bot context (5)

For manual rows: did the bot also see/act on this trade?
For broker rows: just echoes the bot's actual behavior.

| Column | Type | Purpose |
|---|---|---|
| `bot_filled` | bool | Did the bot fill an order on this signal |
| `bot_realized_r` | float | If filled, what did the bot realize |
| `bot_actual_strategy` | str | Strategy name the bot used |
| `playbook_label` | str | Audit's classified playbook |
| `playbook_confidence` | str | high / medium / low |
| `probe_conflict` | str | Probes that disagreed |

### Audit-generated counterfactual (5)

**Hypotheses. Not truth.** From `live_broker_reverse_engineering.csv`.

| Column | Type | Purpose |
|---|---|---|
| `audit_classification` | enum | `should_have_skipped` / `good_entry_clean_winner` / `good_entry_clean_loser` / `good_entry_bad_management` / `uncertain` |
| `audit_classification_reason` | str | Free-text rationale |
| `audit_best_counterfactual_model` | str | e.g. `simple_2R`, `simple_1.5R` |
| `audit_best_counterfactual_r` | float | What the model says the trade *could* have realized |
| `audit_delta_r_vs_actual` | float | counterfactual_r − actual_r (the repair gap) |

### Forensic review — empty on ingestion (6)

| Column | Type | Purpose |
|---|---|---|
| `can_be_legitimately_saved` | bool | TRUE only if a local, rules-based fix at entry-bar makes this a winner |
| `save_method` | str | Free text or rule id of the legitimate save (NOT hindsight magic) |
| `micro_strategy_candidate` | str | ID linking to a registered micro-strategy (once registry exists) |
| `shared_features` | str/JSON | Repeated pair/session/regime/factor signature pieces |
| `review_status` | enum | `untriaged` / `in_review` / `resolved` |
| `notes` | str | Free-text |

## Provenance — what got ingested

### Manual sources (94 rows)

| Source label | Count | Source file | Notes |
|---|---|---|---|
| `manual_human` | 70 | `manual_theory_tradebook.csv` (review_source=manual) | Brock's hand-picked theory trades |
| `manual_ai_curated` | 24 | same file (review_source=ai_curated) | AI-curated Bravo/Delta selections — lower trust, needs human review |

Enriched via left-merge from:
- `data/replay/v2/audits/regime/regime_manual_tradebook.csv` (70 rows, has BB features)
- `data/replay/v2/audits/regime/regime_manual_tradebook_v2.csv` (94 rows, regime_label backfill)

### Broker-truth sources (196 rows)

| Source label | Count | Derivation |
|---|---|---|
| `bot_actual_winner` | 64 | `actual_realized_r > 0` |
| `bot_actual_loser` | 132 | `actual_realized_r <= 0` |
| `bot_actual_unknown` | 0 | (none in this corpus) |

Source: `data/replay/v2/audits/live_broker_reverse_engineering.csv`.
Includes the full counterfactual audit columns.

### Total: 290 rows, 50 columns

## What did NOT get ingested (intentionally deferred)

- **per_trade_factors_filled.csv.gz** — joinable via factor_snapshot_id. Defer
  the heavy factor join until a specific analysis needs it; ledger stays slim.
- **observations-v1v2-archive.jsonl** — V1/V2 era observer logs (only Apr 13-15,
  thin coverage; not aligned with the broker-truth window)
- **scans.jsonl / actions.jsonl** — V3-era observer streams (post Apr 20). Use
  for V3-era trade reconstruction, not for this V1/V2-era ledger
- **Discovery corpus parquets** — those are simulated, not actual trades. Don't
  belong in trade-film ledger

## The audit's classification breakdown (broker only)

From the source data, validates Brock's framing:

```
should_have_skipped:           184   ("wrong playbook / bad timing / wrong direction" bucket)
good_entry_clean_winner:         4   (legitimately-good entries that won)
good_entry_clean_loser:          5   (legitimately-good entries that lost — "clean losers")
good_entry_bad_management:       2
uncertain:                       1
```

Of 196: only **4 + 5 + 2 = 11 trades were "good entries"** by audit verdict.
**184 trades the bot took were trades it should not have taken.**
That's the structural gap the trade-film workflow needs to attack.

## Files

- `ledger.parquet` — main storage, 69 KB
- `ledger.csv` — human-readable mirror, 123 KB
- `schema.md` — this file
- `build_ledger.py` — ingestion script (committed alongside for reproducibility)

## Next layer (NOT this scaffolding)

Per locked direction 2026-05-12:

> Do NOT create new probes. Do NOT change thresholds. Do NOT promote any
> micro strategy. Do NOT collapse losers into "fixed winners" automatically.
> Do NOT blend AI-curated and human/manual trades without a trust label.

This ledger is the substrate. The next work is **forensic review**:
- For each `bot_actual_winner` (64 rows): reverse-engineer the conditions that made it win
- For each `bot_actual_loser` (132 rows): determine if a local, deterministic fix at entry-bar
  would have flipped it (and fill `can_be_legitimately_saved` / `save_method`)
- For each `manual_human` (70 rows): cross-reference against current V3 — would V3 fire?
- Build per-regime, per-pair-family, per-session **conditional factor maps** from the
  rows where audit verdict is good_entry_clean_winner or where review converts a loser

The unit of analysis is `regime × pair-family × session × direction × setup × management`,
NOT a single global score. Per Brock 2026-05-12.

## Cross-references

- [[scrooge-stage5-truth-table-2026-05-12]] — why this work is needed (Stage 5 macro probes failed)
- [[scrooge-bug-catalog]] — bugs affecting the broker-truth window
- [[scrooge-box-bugs-and-validation-targets]] — known contamination zones for the broker trades
- `mr-scrooge-v3/docs/history/` — durable archive layer
