# routing_table_v9 — build summary

Built: 2026-05-18T04:07:03.286409+00:00

## Doctrine (Brock 2026-05-18)

Two surfaces emitted from one candidate universe:

- **`routing_table_v9_trade.parquet`** — only `Elite`/`Pro`/`Seed-Pro`. Live-tradable.
- **`routing_table_v9_observe.parquet`** — adds `Seed`. Telemetry only. Do NOT flip the bot to point at this file with HARD enforcement.

## Inputs

- Combined candidate children: **8,455**
- Legacy session-vocab textbook rows dropped: **610**
- Unique cells after best-per-cell aggregation: **759** (parent-regime grain)

## Tier distribution (cells, not session-expanded rows)

| Tier | v9 cells | v8 cells (parent-grain) | Δ | trade? |
|---|---:|---:|---:|---|
| Elite | 6 | 1 | +5 | ✓ |
| Pro | 3 | 21 | -18 | ✓ |
| Seed-Pro | 17 | 0 | +17 | ✓ |
| Standard | 0 | 46 | -46 | — |
| Seed | 413 | 0 | +413 | observe |
| Probationary | 320 | 50 | +270 | — |

## Family × tier (v9)

| Family | Elite | Pro | Seed-Pro | Standard | Seed | Probationary |
|---|---:|---:|---:|---:|---:|---:|
| dbb_trend | 6 | 1 | 11 | 0 | 204 | 122 |
| direct | 0 | 1 | 3 | 0 | 96 | 99 |
| reversal | 0 | 1 | 3 | 0 | 113 | 99 |

## Output sizes

| File | Cells | Rows (session-expanded) |
|---|---:|---:|
| routing_table_v9_trade.parquet | 26 | 182 |
| routing_table_v9_observe.parquet | 439 | 3073 |

## Live-deployment policy

**To flip the bot to v9 trade surface:**
```
strategies.routing_table_path = "data/routing_table_v9_trade.parquet"
```
Keep `gates.entry_filter.mode = "hard"`. `min_tier` can stay at `Standard`
or move to `Seed-Pro` — both work; v9_trade has no Probationary/Standard
rows so the practical difference is small.

**For Seed observation:** ship a separate observer that reads the observe parquet
and writes telemetry on Seed-cell candidates without affecting execution. The
trade parquet is the load-bearing path.

## Promotion lifecycle

Each row carries `promotion_status` and `oos_status`. The intended flow:

1. `candidate` + `untested` — fresh from this build.
2. Run static-rule OOS replay on a held-out window. Sets `oos_status = passed|failed`.
3. After live observation accumulates clean evidence on Seed cells, those
   get `promotion_status = observe → live` and may move up a tier.
4. Cells that perform badly live get `demoted` and dropped from the trade parquet.

These columns are written as `untested` / `candidate` here; a future
`promote_routing_cells.py` script will edit them based on OOS + live data.