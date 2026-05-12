"""Build the trade-film ledger from manual + broker-truth sources.

Locked design rules (per 2026-05-12 direction):
- actual_* columns are immutable trade truth
- counterfactual_* columns are audit-generated repair hypotheses
- review_* columns are empty, reserved for human/forensic work
- source_label distinguishes provenance and trust
- losers NEVER quietly become winners

Inputs:
  /home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/manual_tradebook/manual_theory_tradebook.csv
    94 rows: 70 review_source=manual + 24 review_source=ai_curated
  /home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/audits/regime/regime_manual_tradebook_v2.csv
    94 rows: enriched with regime_label, bb_position, ema20_dist_pct, bb_band_width
  /home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/audits/live_broker_reverse_engineering.csv
    196 rows: broker truth + audit-generated counterfactual + classification

Output:
  /home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet
  /home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.csv  (human-readable)
  /home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/schema.md
"""
from pathlib import Path
import pandas as pd
import numpy as np
import uuid
from datetime import datetime, timezone

OUT = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger")
OUT.mkdir(parents=True, exist_ok=True)

INGEST_AT = datetime.now(timezone.utc).isoformat(timespec="seconds")

# =============================================================
# Source 1: manual_theory_tradebook (94 rows)
# =============================================================
mt = pd.read_csv("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/manual_tradebook/manual_theory_tradebook.csv")
print(f"manual_theory_tradebook: {len(mt)} rows")

# Source 2: regime-enriched. v1 has BB features but only 70 rows; v2 has 94 rows
# but no direction/BB. We left-merge v1 (richer) for the regime/factor enrichment,
# fall back to v2 for the additional 24 rows' regime_label/bot_filled coverage.
mt_regime_v1 = pd.read_csv("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/audits/regime/regime_manual_tradebook.csv")
mt_regime_v2 = pd.read_csv("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/audits/regime/regime_manual_tradebook_v2.csv")
print(f"regime_manual_tradebook v1: {len(mt_regime_v1)} rows, v2: {len(mt_regime_v2)} rows")

# Merge v1 for BB features (key: symbol+ts+strategy — direction in v1 is encoded
# as 0.0/1.0 float vs "long"/"short" string in main tradebook, so we skip it as key)
mt = mt.merge(
    mt_regime_v1[['symbol', 'ts', 'strategy', 'regime_label',
                  'bb_position', 'ema20_dist_pct', 'bb_band_width_a_bps',
                  'bot_filled', 'bot_realized_r', 'bot_strategy']],
    on=['symbol', 'ts', 'strategy'],
    how='left',
)

# Backfill regime_label / bot_filled / bot_realized_r / bot_strategy from v2 for rows v1 missed
# v2 key is symbol+ts+strategy (no direction)
v2_lookup = mt_regime_v2.set_index(['symbol', 'ts', 'strategy'])[
    ['regime_label', 'bot_filled', 'bot_realized_r', 'bot_strategy']
].to_dict('index')
for idx, r in mt.iterrows():
    if pd.isna(r.get('regime_label')):
        k = (r['symbol'], r['ts'], r['strategy'])
        v2_row = v2_lookup.get(k)
        if v2_row:
            for col in ('regime_label', 'bot_filled', 'bot_realized_r', 'bot_strategy'):
                if pd.isna(mt.at[idx, col]):
                    mt.at[idx, col] = v2_row[col]

# =============================================================
# Source 3: broker reverse-engineering (196 rows)
# =============================================================
br = pd.read_csv("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/audits/live_broker_reverse_engineering.csv")
print(f"live_broker_reverse_engineering: {len(br)} rows")


# =============================================================
# Build unified ledger rows
# =============================================================
def manual_row(r):
    """Map a manual_theory_tradebook row into the ledger schema."""
    # source_label: manual_human (review_source=manual) or manual_ai_curated
    if r["review_source"] == "manual":
        source_label = "manual_human"
        trust_score = "high"
    elif r["review_source"] == "ai_curated":
        source_label = "manual_ai_curated"
        trust_score = "medium"
    else:
        source_label = "manual_unknown"
        trust_score = "low"

    return {
        # identity
        "ledger_id": str(uuid.uuid4()),
        "source_label": source_label,
        "source_file": "manual_theory_tradebook.csv",
        "source_row_key": f"{r['symbol']}|{r['ts']}|{r['strategy']}|{r['direction']}",
        "trust_score": trust_score,
        "ingested_at": INGEST_AT,
        # trade truth (immutable)
        "pair": r["symbol"],
        "entry_ts": r["ts"],
        "direction": r["direction"],
        "strategy_label": r["strategy"],           # box/dbb/etc., from manual rubric
        "session": r["session"],
        "regime_label": r.get("regime_label"),
        # actual outcome (manual = theory_outcome_r since these never traded live)
        "actual_realized_r": r.get("theory_outcome_r"),
        "actual_realized_pl": None,
        "actual_exit_reason": r.get("exit_reason"),
        "actual_mfe_r": r.get("mfe_r"),
        "actual_mae_r": r.get("mae_r"),
        "actual_tp1_hit": r.get("tp1_hit"),
        "actual_tp2_hit": r.get("tp2_hit"),
        "actual_be_hit": r.get("be_hit"),
        "actual_ratchet_triggered": r.get("ratchet_triggered"),
        "actual_holding_minutes": r.get("holding_minutes"),
        "actual_winner": r.get("winner"),
        # entry/stop geometry
        "entry_price": r.get("entry_price"),
        "stop_price": r.get("stop_price"),
        "tp1_price": r.get("tp1_price"),
        "tp2_price": r.get("tp2_price"),
        "stop_pips_or_price": r.get("R_pips_or_price"),
        "atr14": r.get("atr14"),
        # factor snapshot link
        "factor_snapshot_id": None,
        "bb_position": r.get("bb_position"),
        "ema20_dist_pct": r.get("ema20_dist_pct"),
        "bb_band_width_a_bps": r.get("bb_band_width_a_bps"),
        # bot context (for manual: did the bot also see and act on this trade?)
        "bot_filled": r.get("bot_filled"),
        "bot_realized_r": r.get("bot_realized_r"),
        "bot_actual_strategy": r.get("bot_strategy"),
        "playbook_label": None,
        "playbook_confidence": None,
        "probe_conflict": None,
        # audit-generated counterfactual
        "audit_classification": None,
        "audit_classification_reason": None,
        "audit_best_counterfactual_model": None,
        "audit_best_counterfactual_r": None,
        "audit_delta_r_vs_actual": None,
        # forensic review (EMPTY by design — reserved for human work)
        "can_be_legitimately_saved": None,
        "save_method": None,
        "micro_strategy_candidate": None,
        "shared_features": None,
        "review_status": "untriaged",
        "notes": None,
    }


def broker_row(r):
    """Map a live_broker_reverse_engineering row into the ledger schema."""
    actual_r = float(r["actual_realized_r"]) if r.get("actual_realized_r") not in (None, "") else None
    if actual_r is None:
        source_label = "bot_actual_unknown"
    elif actual_r > 0:
        source_label = "bot_actual_winner"
    else:
        source_label = "bot_actual_loser"

    return {
        # identity
        "ledger_id": str(uuid.uuid4()),
        "source_label": source_label,
        "source_file": "live_broker_reverse_engineering.csv",
        "source_row_key": r["trade_id"],
        "trust_score": "high",   # broker truth = highest trust
        "ingested_at": INGEST_AT,
        # trade truth (immutable)
        "pair": r["symbol"],
        "entry_ts": r["entry_ts"],
        "direction": r["direction"],
        "strategy_label": r.get("bot_actual_strategy"),
        "session": None,           # not in broker source; derive in step 2
        "regime_label": r.get("regime_label"),
        # actual outcome (broker truth)
        "actual_realized_r": actual_r,
        "actual_realized_pl": float(r["actual_realized_pl"]) if r.get("actual_realized_pl") not in (None, "") else None,
        "actual_exit_reason": None,
        "actual_mfe_r": None,
        "actual_mae_r": None,
        "actual_tp1_hit": None,
        "actual_tp2_hit": None,
        "actual_be_hit": None,
        "actual_ratchet_triggered": None,
        "actual_holding_minutes": None,
        "actual_winner": actual_r > 0 if actual_r is not None else None,
        # entry/stop geometry (not in this source)
        "entry_price": None,
        "stop_price": None,
        "tp1_price": None,
        "tp2_price": None,
        "stop_pips_or_price": None,
        "atr14": None,
        # factor snapshot link (broker rows DO have this — join later)
        "factor_snapshot_id": r.get("factor_snapshot_id"),
        "bb_position": None,
        "ema20_dist_pct": None,
        "bb_band_width_a_bps": None,
        # bot context
        "bot_filled": True,
        "bot_realized_r": actual_r,
        "bot_actual_strategy": r.get("bot_actual_strategy"),
        "playbook_label": r.get("playbook_label"),
        "playbook_confidence": r.get("playbook_confidence"),   # string: high/medium/low
        "probe_conflict": r.get("probe_conflict"),
        # audit-generated counterfactual
        "audit_classification": r.get("classification"),
        "audit_classification_reason": r.get("classification_reason"),
        "audit_best_counterfactual_model": r.get("best_counterfactual_model"),
        "audit_best_counterfactual_r": float(r["best_counterfactual_r"]) if r.get("best_counterfactual_r") not in (None, "") else None,
        "audit_delta_r_vs_actual": float(r["delta_r_vs_actual"]) if r.get("delta_r_vs_actual") not in (None, "") else None,
        # forensic review (EMPTY)
        "can_be_legitimately_saved": None,
        "save_method": None,
        "micro_strategy_candidate": None,
        "shared_features": None,
        "review_status": "untriaged",
        "notes": r.get("notes"),
    }


rows = []
for _, r in mt.iterrows():
    rows.append(manual_row(r))
for _, r in br.iterrows():
    rows.append(broker_row(r))

ledger = pd.DataFrame(rows)
# Coerce mixed-type identity fields to string for parquet
ledger["source_row_key"] = ledger["source_row_key"].astype(str)
ledger["factor_snapshot_id"] = ledger["factor_snapshot_id"].astype(str).replace("nan", None)
print(f"\nledger: {len(ledger)} rows")
print(ledger["source_label"].value_counts().to_string())

# =============================================================
# Output
# =============================================================
ledger_pq = OUT / "ledger.parquet"
ledger_csv = OUT / "ledger.csv"
ledger.to_parquet(ledger_pq, index=False)
ledger.to_csv(ledger_csv, index=False)
print(f"\nwrote {ledger_pq} ({ledger_pq.stat().st_size} B)")
print(f"wrote {ledger_csv} ({ledger_csv.stat().st_size} B)")
print(f"columns: {len(ledger.columns)}")

# Brief integrity check
print("\n--- INTEGRITY CHECK ---")
print(f"manual_human rows:      {(ledger.source_label == 'manual_human').sum()}  (expected 70)")
print(f"manual_ai_curated rows: {(ledger.source_label == 'manual_ai_curated').sum()}  (expected 24)")
print(f"bot_actual_winner rows: {(ledger.source_label == 'bot_actual_winner').sum()}")
print(f"bot_actual_loser rows:  {(ledger.source_label == 'bot_actual_loser').sum()}")
print(f"Total bot:              {ledger.source_label.str.startswith('bot_').sum()}  (expected 196)")
print(f"Total all:              {len(ledger)}  (expected 290)")
