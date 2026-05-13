"""Step 7 v2: candidate outcome replay using V3 OWN scans as forward-walk price feed.

Reason for v2: dukascopy M5 ends 2026-04-22. Most of the 39 candidates are post-Apr-22.
But scans.jsonl runs through May 12. Each scan record carries
features.bollinger.current_close at scan_ts — that's price evolution.

Forward walk:
  - Anchor: candidate scan at T0 with current_close = entry_price
  - Steps: same-pair scans at T0+1min through T0+8h
  - At each step, read current_close (high/low not available — using close as both)
  - Track MFE, MAE relative to entry_price
  - Stop-touch: when |close - entry| exceeds stop_dist in adverse direction

This is approximate (close-only, not bar high/low) but uses real V3-observed prices.
"""
import pandas as pd
import json
from pathlib import Path
from datetime import timedelta
from collections import defaultdict

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
SCANS_FILE = "/data/scrooge-v3-data/ml-observer/scans.jsonl"
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/candidate-replay-step7")
OUT.mkdir(parents=True, exist_ok=True)


def infer_direction(z_score, bb_position):
    if z_score is None or bb_position is None: return "ambiguous"
    if z_score >= 0.8 and bb_position >= 0.7: return "short"
    if z_score <= -0.8 and bb_position <= 0.3: return "long"
    if 0.4 < bb_position < 0.6 and abs(z_score) < 0.4: return "ambiguous"
    if z_score > 0 and bb_position > 0.55: return "short"
    if z_score < 0 and bb_position < 0.45: return "long"
    return "ambiguous"


# === Load targets ===
df = pd.read_parquet(LEDGER)
target = df[df["step6b_recommendation"].isin([
    "direction_repair_candidate", "same_direction_timing_repair_candidate"
])].copy()
target["entry_ts"] = pd.to_datetime(target["entry_ts"], utc=True, errors="coerce")
print(f"candidates: {len(target)}")

target_pairs = set(target["pair"].unique())
t_min = target["entry_ts"].min() - timedelta(hours=1)
t_max = target["entry_ts"].max() + timedelta(hours=9)
WINDOW = timedelta(minutes=30)

# === Stream scans, keep ALL scans (for both candidate detection AND forward-walk) ===
print(f"\nstreaming scans.jsonl...")
all_scans_per_pair = defaultdict(list)
cycle_scans = defaultdict(list)
n_lines = 0
with open(SCANS_FILE) as f:
    for line in f:
        n_lines += 1
        try: d = json.loads(line)
        except: continue
        sym = d.get("symbol")
        if sym not in target_pairs: continue
        ts_str = d.get("ts")
        if not ts_str: continue
        try: ts = pd.Timestamp(ts_str)
        except: continue
        if ts < t_min or ts > t_max: continue

        scorer = d.get("scorer") or {}
        features = d.get("features") or {}
        bb = features.get("bollinger") or {}
        zd = features.get("zone_detector") or {}
        ml_feat = d.get("ml_features") or {}

        rec = {
            "ts": ts,
            "cycle": d.get("cycle"),
            "verdict": d.get("verdict"),
            "score": scorer.get("final"),
            "tier": scorer.get("tier"),
            "fam": scorer.get("fam"),
            "current_close": bb.get("current_close"),
            "z_score": bb.get("z_score"),
            "bb_position": bb.get("bb_position") or ml_feat.get("bb_position"),
            "atr": ml_feat.get("atr"),
            "pdh": zd.get("PDH"),
            "pdl": zd.get("PDL"),
            "trade_id": d.get("trade_id"),
            "strategy_allowed": d.get("strategy_allowed"),
            "blocks": scorer.get("blocks") or [],
            "blocks_count": scorer.get("blocks_count") or 0,
        }
        all_scans_per_pair[sym].append(rec)
        cycle_scans[(sym, d.get("cycle"))].append(rec)
print(f"  total scans read: {n_lines:,}")
for p in all_scans_per_pair:
    all_scans_per_pair[p] = sorted(all_scans_per_pair[p], key=lambda x: x["ts"])
print(f"  pairs with scans: {len(all_scans_per_pair)}")


# === Select best candidate scan per ledger row ===
print("\nselecting best TAKE scan per candidate ...")
candidates = []
for idx, row in target.iterrows():
    pair = row["pair"]
    bot_dir = row["direction"]
    entry_ts = row["entry_ts"]
    is_flip = row["step6b_recommendation"] == "direction_repair_candidate"
    target_dir = ("short" if bot_dir == "long" else "long") if is_flip else bot_dir

    nearby_takes = [s for s in all_scans_per_pair.get(pair, [])
                    if entry_ts - WINDOW <= s["ts"] <= entry_ts + WINDOW
                    and s["verdict"] in ("TAKE_A", "TAKE_B")
                    and infer_direction(s["z_score"], s["bb_position"]) == target_dir]
    if nearby_takes:
        best = max(nearby_takes, key=lambda s: s["score"] or 0)
        candidates.append({"idx": idx, "row": row, "scan": best, "target_dir": target_dir})
print(f"  candidates with scan: {len(candidates)}")


def forward_walk_via_scans(pair, anchor_ts, entry_price, direction, stop_dist, max_hold_hours=8):
    """Walk forward using subsequent scan current_close values as the price feed."""
    scans = all_scans_per_pair.get(pair, [])
    if not scans or stop_dist <= 0: return None
    end_ts = anchor_ts + timedelta(hours=max_hold_hours)
    mfe = 0.0
    mae = 0.0
    last_price = entry_price
    last_ts = anchor_ts
    for s in scans:
        if s["ts"] <= anchor_ts: continue
        if s["ts"] > end_ts:
            return {"exit_reason": "time_stop", "mfe_dist": mfe, "mae_dist": mae,
                    "exit_ts": last_ts, "exit_price": last_price, "n_samples": 0}
        cc = s["current_close"]
        if cc is None: continue
        if direction == "long":
            adverse = entry_price - cc  # negative if price moved up
            favorable = cc - entry_price
        else:
            adverse = cc - entry_price
            favorable = entry_price - cc
        if favorable > 0: mfe = max(mfe, favorable)
        if adverse > 0: mae = max(mae, adverse)
        last_price = cc
        last_ts = s["ts"]
        # Stop check
        if adverse >= stop_dist:
            return {"exit_reason": "stop", "mfe_dist": mfe, "mae_dist": stop_dist,
                    "exit_ts": s["ts"], "exit_price": cc, "n_samples": 0}
    return {"exit_reason": "data_end", "mfe_dist": mfe, "mae_dist": mae,
            "exit_ts": last_ts, "exit_price": last_price, "n_samples": 0}


# === Replay ===
print("\nreplaying candidates ...")
replay = []
for c in candidates:
    scan = c["scan"]
    row = c["row"]
    inferred = c["target_dir"]
    pair = row["pair"]
    entry_price = scan["current_close"]
    atr = scan["atr"]
    if entry_price is None or atr is None or atr <= 0:
        replay.append({"idx": c["idx"], "ledger_id": row["ledger_id"], "verdict": "missing_atr_or_price"})
        continue
    stop_dist = atr
    walk = forward_walk_via_scans(pair, scan["ts"], entry_price, inferred, stop_dist, 8)
    if walk is None:
        replay.append({"idx": c["idx"], "ledger_id": row["ledger_id"], "verdict": "no_walk_data"})
        continue

    mfe_r = walk["mfe_dist"] / stop_dist
    mae_r = walk["mae_dist"] / stop_dist

    # Outcomes at different R targets
    out_1r = 1.0 if mfe_r >= 1.0 else (-1.0 if walk["exit_reason"] == "stop" else (mfe_r if mfe_r > 0 else 0.0))
    out_15r = 1.5 if mfe_r >= 1.5 else (-1.0 if walk["exit_reason"] == "stop" else (min(mfe_r, 1.0) if mfe_r > 0 else 0.0))
    out_2r = 2.0 if mfe_r >= 2.0 else (-1.0 if walk["exit_reason"] == "stop" else (min(mfe_r, 1.5) if mfe_r > 0 else 0.0))

    # Outcome with ratchet at 0.5R BE
    if mfe_r >= 2.0:
        out_ratchet = 2.0
    elif mfe_r >= 0.5 and walk["exit_reason"] == "stop":
        out_ratchet = 0.0  # BE
    else:
        out_ratchet = out_2r

    # Classification
    if mfe_r >= 1.5 and walk["exit_reason"] != "stop":
        outcome_class = "full_winner"
    elif mfe_r >= 1.0 and walk["exit_reason"] != "stop":
        outcome_class = "1R_winner"
    elif mfe_r >= 0.5 and walk["exit_reason"] == "stop":
        outcome_class = "gave_back_green"
    elif walk["exit_reason"] == "stop":
        outcome_class = "clean_stop"
    elif mfe_r >= 0.5:
        outcome_class = "partial_winner_ratchet_save"
    else:
        outcome_class = "no_development"

    # Promotion
    rec = row["step6b_recommendation"]
    if outcome_class in ("full_winner", "1R_winner"):
        verdict_final = ("direction_repair_confirmed" if rec == "direction_repair_candidate"
                         else "same_direction_timing_repair_confirmed")
    elif outcome_class == "partial_winner_ratchet_save":
        verdict_final = ("direction_repair_partial" if rec == "direction_repair_candidate"
                         else "same_direction_timing_repair_partial")
    elif outcome_class == "gave_back_green":
        verdict_final = "false_candidate_management_dependent"
    elif outcome_class == "clean_stop":
        verdict_final = "false_candidate"
    else:
        verdict_final = "no_development"

    replay.append({
        "idx": c["idx"],
        "ledger_id": row["ledger_id"],
        "pair": pair,
        "bot_direction": row["direction"],
        "inferred_candidate_direction": inferred,
        "step6b_recommendation": rec,
        "scan_ts": scan["ts"],
        "scan_cycle": scan["cycle"],
        "scan_score": scan["score"],
        "scan_tier": scan["tier"],
        "scan_fam": scan["fam"],
        "entry_price": float(entry_price),
        "atr": float(atr),
        "stop_dist": float(stop_dist),
        "walk_mfe_r": float(mfe_r),
        "walk_mae_r": float(mae_r),
        "walk_exit_reason": walk["exit_reason"],
        "out_at_1R": float(out_1r),
        "out_at_1_5R": float(out_15r),
        "out_at_2R": float(out_2r),
        "out_with_ratchet": float(out_ratchet),
        "outcome_class": outcome_class,
        "verdict_final": verdict_final,
        "pair_family": row["pair_family"],
        "session_bucket": row["session_bucket"],
        "session_quarter": row["session_quarter"],
    })

replay_df = pd.DataFrame(replay)
print(f"\nreplay results: {len(replay_df)}")
print(f"\noutcome_class:")
if "outcome_class" in replay_df.columns:
    print(replay_df["outcome_class"].value_counts(dropna=False).to_string())
print(f"\nverdict_final:")
if "verdict_final" in replay_df.columns:
    print(replay_df["verdict_final"].value_counts(dropna=False).to_string())

# Gate audit
print("\ngate audit:")
gate_rows = []
for r in replay:
    if "scan_cycle" not in r or not r.get("scan_cycle"): continue
    key = (r["pair"], r["scan_cycle"])
    siblings = cycle_scans.get(key, [])
    fired = [s for s in siblings if s.get("trade_id")]
    takes = [s for s in siblings if s.get("verdict") in ("TAKE_A","TAKE_B")]
    gate_rows.append({
        "ledger_id": r["ledger_id"],
        "verdict_final": r.get("verdict_final"),
        "scan_cycle": r["scan_cycle"],
        "n_siblings": len(siblings),
        "n_take_in_cycle": len(takes),
        "n_fired_in_cycle": len(fired),
    })
gate_df = pd.DataFrame(gate_rows)
if len(gate_df) and "n_fired_in_cycle" in gate_df.columns:
    print(f"  rows with cycle data: {len(gate_df)}")
    print(f"  cycles where NO trade fired: {(gate_df['n_fired_in_cycle'] == 0).sum()}")
    print(f"  cycles where a sibling DID fire: {(gate_df['n_fired_in_cycle'] > 0).sum()}")
    print(f"  by final verdict:")
    print(gate_df.groupby("verdict_final")["n_fired_in_cycle"].agg(["mean","max","count"]).to_string())

replay_df.to_csv(OUT / "replay_results.csv", index=False)
replay_df.to_parquet(OUT / "replay_results.parquet", index=False)
if len(gate_df):
    gate_df.to_csv(OUT / "gate_audit.csv", index=False)
print(f"\nsaved")

# Update ledger
df["step7_final_verdict"] = None
df["step7_outcome_class"] = None
df["step7_replay_mfe_r"] = None
df["step7_replay_mae_r"] = None
df["step7_out_at_2R"] = None
df["step7_out_with_ratchet"] = None
for r in replay:
    idx = r["idx"]
    df.at[idx, "step7_final_verdict"] = r.get("verdict_final")
    df.at[idx, "step7_outcome_class"] = r.get("outcome_class")
    df.at[idx, "step7_replay_mfe_r"] = r.get("walk_mfe_r")
    df.at[idx, "step7_replay_mae_r"] = r.get("walk_mae_r")
    df.at[idx, "step7_out_at_2R"] = r.get("out_at_2R")
    df.at[idx, "step7_out_with_ratchet"] = r.get("out_with_ratchet")

for c in df.columns:
    if df[c].dtype == "object" and c not in ("correct_pdh","correct_pdl","reconstructed_entry_price",
                                              "best_opp_r","best_same_r","actual_realized_r",
                                              "actual_realized_pl","actual_mfe_r","actual_mae_r",
                                              "step7_replay_mfe_r","step7_replay_mae_r",
                                              "step7_out_at_2R","step7_out_with_ratchet"):
        df[c] = df[c].astype(str).replace({"nan": None, "None": None, "<NA>": None})
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"saved ledger ({len(df)} rows, {len(df.columns)} cols)")
