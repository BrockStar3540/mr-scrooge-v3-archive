"""Step 6b: scans.jsonl deep-dive for the 68 V3-era direction_repair_or_skip rows.

Approach:
  1. Stream scans.jsonl once, build a per-pair time-indexed list of (ts, verdict,
     scorer_final, z_score, bb_position, trade_id, etc.)
  2. Load outcomes.jsonl (small, 246 rows) to map trade_id → realized PL/outcome
  3. For each of 68 V3-era target rows:
     - Filter scans to same pair, ±30 min
     - Determine inferred direction per nearby scan (z_score sign, bb_position)
     - Classify nearby candidates as opposite vs same direction
     - Count TAKE verdicts vs REJECT verdicts
     - If TAKE with trade_id: lookup outcome
  4. Classify per target:
     - direction_repair: opposite-direction TAKE existed (preferably fired+won)
     - same_direction_timing_repair: same-direction TAKE existed (preferably fired+won)
     - skip_required: no TAKE verdicts in either direction nearby
     - no_clean_answer: TAKEs both directions / data ambiguous
"""
import pandas as pd
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import defaultdict

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
SCANS = "/data/scrooge-v3-data/ml-observer/scans.jsonl"
OUTCOMES = "/data/scrooge-v3-data/ml-observer/outcomes.jsonl"
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/direction-repair-lookup")


def infer_direction(z_score, bb_position):
    """Infer the bot's likely direction-of-interest from BB context.
    Positive z_score / bb_position > 0.7 → short setup (fade upper rail).
    Negative z_score / bb_position < 0.3 → long setup (fade lower rail).
    Otherwise → ambiguous.
    """
    if z_score is None or bb_position is None:
        return "ambiguous"
    if z_score >= 0.8 and bb_position >= 0.7:
        return "short"
    if z_score <= -0.8 and bb_position <= 0.3:
        return "long"
    if 0.4 < bb_position < 0.6 and abs(z_score) < 0.4:
        return "ambiguous"
    if z_score > 0 and bb_position > 0.55:
        return "short"
    if z_score < 0 and bb_position < 0.45:
        return "long"
    return "ambiguous"


# === Load targets ===
df = pd.read_parquet(LEDGER)
target = df[df["repair_taxonomy"] == "direction_repair_or_skip"].copy()
target["entry_ts"] = pd.to_datetime(target["entry_ts"], utc=True, errors="coerce")
cutoff = pd.Timestamp("2026-04-20", tz="UTC")
target_v3 = target[target["entry_ts"] >= cutoff].copy()
print(f"V3-era targets: {len(target_v3)}")

# Establish global window for scan filtering
t_min = target_v3["entry_ts"].min() - timedelta(hours=1)
t_max = target_v3["entry_ts"].max() + timedelta(hours=1)
target_pairs = set(target_v3["pair"].unique())
print(f"  pairs: {len(target_pairs)}")
print(f"  window: {t_min} → {t_max}")

# === Stream scans.jsonl ===
print(f"\nstreaming {SCANS} ...")
scans_per_pair = defaultdict(list)
n_lines = 0
n_kept = 0
with open(SCANS) as f:
    for line in f:
        n_lines += 1
        if n_lines % 100000 == 0:
            print(f"  read {n_lines:,} lines, kept {n_kept:,}")
        try:
            d = json.loads(line)
        except:
            continue
        sym = d.get("symbol")
        if sym not in target_pairs:
            continue
        ts_str = d.get("ts")
        if not ts_str:
            continue
        try:
            ts = pd.Timestamp(ts_str)
        except:
            continue
        if ts < t_min or ts > t_max:
            continue
        # Extract relevant fields
        verdict = d.get("verdict")
        scorer = d.get("scorer") or {}
        features = d.get("features") or {}
        bb = features.get("bollinger") or {}
        ml_feat = d.get("ml_features") or {}
        scans_per_pair[sym].append({
            "ts": ts,
            "verdict": verdict,
            "score": scorer.get("final"),
            "tier": scorer.get("tier"),
            "fam": scorer.get("fam"),
            "z_score": bb.get("z_score"),
            "bb_position": bb.get("bb_position") or ml_feat.get("bb_position"),
            "trade_id": d.get("trade_id"),
            "strategy_allowed": d.get("strategy_allowed"),
        })
        n_kept += 1
print(f"  total lines: {n_lines:,}, kept: {n_kept:,}")

# Sort by ts per pair
for p in scans_per_pair:
    scans_per_pair[p] = sorted(scans_per_pair[p], key=lambda x: x["ts"])

# === Load outcomes.jsonl ===
print(f"\nloading outcomes ...")
outcomes_by_trade = {}
with open(OUTCOMES) as f:
    for line in f:
        d = json.loads(line)
        tid = d.get("trade_id")
        if tid:
            outcomes_by_trade[tid] = d
print(f"  outcomes loaded: {len(outcomes_by_trade)}")

# === Per-target classification ===
WINDOW = timedelta(minutes=30)
results = []
for idx, row in target_v3.iterrows():
    pair = row["pair"]
    bot_dir = row["direction"]
    entry_ts = row["entry_ts"]
    opp_dir = "short" if bot_dir == "long" else "long"

    nearby_all = [s for s in scans_per_pair.get(pair, [])
                  if entry_ts - WINDOW <= s["ts"] <= entry_ts + WINDOW]

    if not nearby_all:
        results.append({
            "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
            "bot_direction": bot_dir, "entry_ts": entry_ts,
            "n_scans_nearby": 0,
            "n_takes_total": 0,
            "n_opp_takes": 0, "n_same_takes": 0,
            "max_opp_score": None, "max_same_score": None,
            "opp_fired_count": 0, "same_fired_count": 0,
            "step6b_recommendation": "no_clean_answer",
            "step6b_evidence": "no scans found in ±30min window",
        })
        continue

    takes = [s for s in nearby_all if s["verdict"] in ("TAKE_A", "TAKE_B")]
    opp_takes = [s for s in takes if infer_direction(s["z_score"], s["bb_position"]) == opp_dir]
    same_takes = [s for s in takes if infer_direction(s["z_score"], s["bb_position"]) == bot_dir]

    max_opp_score = max((s["score"] for s in opp_takes if s["score"] is not None), default=None)
    max_same_score = max((s["score"] for s in same_takes if s["score"] is not None), default=None)

    opp_fired = [s for s in opp_takes if s["trade_id"]]
    same_fired = [s for s in same_takes if s["trade_id"]]

    # Classify
    if opp_fired:
        # Did any fired opposite trade win?
        winners = []
        for s in opp_fired:
            o = outcomes_by_trade.get(s["trade_id"])
            if o:
                # Outcome has price/units fields; if exit was at TP it's a win
                winners.append(o)
        if winners:
            rec = "direction_repair"
            evidence = f"opposite-dir TAKE fired and resolved nearby (n={len(opp_fired)})"
        else:
            rec = "direction_repair_candidate"
            evidence = f"opposite-dir TAKE fired nearby (n={len(opp_fired)}) but outcome unknown"
    elif opp_takes:
        rec = "direction_repair_candidate"
        evidence = f"opposite-dir TAKE existed (verdict {[s['verdict'] for s in opp_takes[:3]]}) but did not fire — max_score {max_opp_score}"
    elif same_fired:
        rec = "same_direction_timing_repair_candidate"
        evidence = f"same-dir TAKE fired nearby at different time (n={len(same_fired)})"
    elif same_takes:
        rec = "same_direction_timing_repair_candidate"
        evidence = f"same-dir TAKE existed but did not fire — max_score {max_same_score}"
    elif takes:
        rec = "no_clean_answer"
        evidence = f"{len(takes)} TAKE scans nearby but direction ambiguous"
    else:
        rec = "skip_required"
        evidence = f"{len(nearby_all)} scans nearby, zero TAKE verdicts"

    results.append({
        "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
        "bot_direction": bot_dir, "entry_ts": entry_ts,
        "n_scans_nearby": len(nearby_all),
        "n_takes_total": len(takes),
        "n_opp_takes": len(opp_takes), "n_same_takes": len(same_takes),
        "max_opp_score": max_opp_score, "max_same_score": max_same_score,
        "opp_fired_count": len(opp_fired), "same_fired_count": len(same_fired),
        "step6b_recommendation": rec,
        "step6b_evidence": evidence,
    })

results_df = pd.DataFrame(results)
print(f"\nresults: {len(results_df)}")
print(f"\nSTEP 6B RECOMMENDATION:")
rec = results_df["step6b_recommendation"].value_counts()
n = len(results_df)
for k, v in rec.items():
    print(f"  {k}: {v}/{n} = {v/n*100:.1f}%")

# Save
results_df.to_csv(OUT / "scans_deep_dive_v3_era.csv", index=False)
results_df.to_parquet(OUT / "scans_deep_dive_v3_era.parquet", index=False)
print(f"\nsaved")

# Update ledger
df["step6b_recommendation"] = None
df["step6b_evidence"] = None
df["step6b_n_scans_nearby"] = None
df["step6b_n_opp_takes"] = None
df["step6b_n_same_takes"] = None
for r in results:
    idx = r["idx"]
    df.at[idx, "step6b_recommendation"] = r["step6b_recommendation"]
    df.at[idx, "step6b_evidence"] = r["step6b_evidence"]
    df.at[idx, "step6b_n_scans_nearby"] = r["n_scans_nearby"]
    df.at[idx, "step6b_n_opp_takes"] = r["n_opp_takes"]
    df.at[idx, "step6b_n_same_takes"] = r["n_same_takes"]

for c in df.columns:
    if df[c].dtype == "object" and c not in ("correct_pdh","correct_pdl","reconstructed_entry_price",
                                              "best_opp_r","best_same_r","actual_realized_r",
                                              "actual_realized_pl","actual_mfe_r","actual_mae_r"):
        df[c] = df[c].astype(str).replace({"nan": None, "None": None, "<NA>": None})
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"saved ledger ({len(df)} rows, {len(df.columns)} cols)")
