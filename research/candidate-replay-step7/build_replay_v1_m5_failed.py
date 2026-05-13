"""Step 7: Candidate outcome replay + gate-blocking audit.

For each of the 39 step6b candidates (22 direction_repair_candidate + 17 same_direction_timing_repair_candidate):
  1. Extract the best opposite-direction or same-direction TAKE scan from scans.jsonl
  2. Forward-walk M5 bars from scan ts; compute outcomes at 1R / 1.5R / 2R + ratchet save
  3. Audit which gate blocked the fire (or which scan won the cycle)
  4. Promote to *_confirmed or demote to false_candidate

Method (entry replay):
  - entry_price = features.bollinger.current_close at scan_ts (the price the scan saw)
  - inferred direction (z_score sign × bb_position) → long or short
  - stop = entry ± ATR (1× ATR proxy for V3 natural_stop_pips)
  - TP1 = 1R, TP2 = 1.5R, TP3 = 2R (R = stop distance)
  - walk M5 forward up to 8 hours; first-touch wins
  - record MFE, MAE, realized R at each TP target + ratchet outcome (BE if mfe ≥ 0.5R)

Gate audit:
  - cycle from the candidate scan
  - find other scans in the same cycle (or the fired scan if any)
  - which gate failed: examine gates dict + cycle-level priority
"""
import pandas as pd
import json
from pathlib import Path
from datetime import timedelta
from collections import defaultdict

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
SCANS_FILE = "/data/scrooge-v3-data/ml-observer/scans.jsonl"
DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
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


# === Load target ledger rows ===
df = pd.read_parquet(LEDGER)
target = df[df["step6b_recommendation"].isin([
    "direction_repair_candidate", "same_direction_timing_repair_candidate"
])].copy()
target["entry_ts"] = pd.to_datetime(target["entry_ts"], utc=True, errors="coerce")
print(f"step6b candidates: {len(target)}")

# === Stream scans to extract candidate TAKE records ===
print("\nstreaming scans.jsonl to extract candidate scans...")
target_pairs = set(target["pair"].unique())
t_min = target["entry_ts"].min() - timedelta(hours=1)
t_max = target["entry_ts"].max() + timedelta(hours=1)
WINDOW = timedelta(minutes=30)

# Bucket scans per pair
scans_per_pair = defaultdict(list)
cycle_scans = defaultdict(list)  # (pair, cycle) → all scans in that cycle (for gate audit)
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

        scan_rec = {
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
            "natural_stop_pips": ml_feat.get("natural_stop_pips"),
            "pdh": zd.get("PDH"),
            "pdl": zd.get("PDL"),
            "trade_id": d.get("trade_id"),
            "strategy_allowed": d.get("strategy_allowed"),
            "gates": d.get("gates") or {},
        }
        scans_per_pair[sym].append(scan_rec)
        cycle_scans[(sym, d.get("cycle"))].append(scan_rec)
print(f"  read {n_lines:,} scan lines")
print(f"  scans kept (matched target pairs+window): {sum(len(v) for v in scans_per_pair.values()):,}")

# === For each candidate, pick the BEST TAKE in the right direction ===
print("\nselecting best candidate scan per ledger row...")
candidate_scans = []
for idx, row in target.iterrows():
    pair = row["pair"]
    bot_dir = row["direction"]
    entry_ts = row["entry_ts"]
    is_dir_flip = row["step6b_recommendation"] == "direction_repair_candidate"
    target_dir = ("short" if bot_dir == "long" else "long") if is_dir_flip else bot_dir

    nearby = [s for s in scans_per_pair.get(pair, [])
              if entry_ts - WINDOW <= s["ts"] <= entry_ts + WINDOW
              and s["verdict"] in ("TAKE_A", "TAKE_B")
              and infer_direction(s["z_score"], s["bb_position"]) == target_dir]
    if not nearby:
        candidate_scans.append(None)
        continue
    # Best = highest score, then earliest ts
    best = max(nearby, key=lambda s: (s["score"] or 0, -((s["ts"] - entry_ts).total_seconds())))
    candidate_scans.append(best)

target["best_candidate_scan"] = candidate_scans
n_found = sum(1 for c in candidate_scans if c)
print(f"  candidates with a best scan: {n_found}/{len(target)}")


# === Forward-walk M5 for each candidate ===
print("\nloading M5 bars per pair (for forward-walk)...")
m5_cache = {}
for pair in target_pairs:
    pair_dir = DUKA / pair
    if not pair_dir.exists():
        m5_cache[pair] = []
        continue
    bars = []
    for f in sorted(pair_dir.glob(f"{pair}_M5_*.jsonl")):
        # Only files overlapping our window
        stem = f.stem
        parts = stem.rsplit("_", 2)
        if len(parts) >= 3:
            try:
                file_start = pd.Timestamp(parts[-2], tz="UTC")
                file_end = pd.Timestamp(parts[-1], tz="UTC")
                if file_end < t_min or file_start > t_max:
                    continue
            except: pass
        for line in open(f):
            try:
                d = json.loads(line)
                ts = pd.Timestamp(d["time"])
                if t_min <= ts <= t_max + timedelta(hours=8):
                    bars.append({
                        "ts": ts,
                        "high": (float(d["high_bid"]) + float(d["high_ask"])) / 2,
                        "low": (float(d["low_bid"]) + float(d["low_ask"])) / 2,
                        "close": (float(d["close_bid"]) + float(d["close_ask"])) / 2,
                    })
            except: continue
    m5_cache[pair] = sorted(bars, key=lambda x: x["ts"])
    print(f"  {pair}: {len(m5_cache[pair])} M5 bars")


def forward_walk(pair, entry_ts, entry_price, direction, stop_dist, max_hold_hours=8):
    """Walk M5 forward; return (mfe_dist, mae_dist, exit_reason, exit_price, exit_ts)."""
    bars = m5_cache.get(pair, [])
    if not bars or stop_dist <= 0:
        return None
    walk_end = entry_ts + timedelta(hours=max_hold_hours)
    sl = entry_price + stop_dist if direction == "short" else entry_price - stop_dist
    mfe_dist = 0.0
    mae_dist = 0.0
    for b in bars:
        if b["ts"] < entry_ts: continue
        if b["ts"] > walk_end:
            return {"exit_reason": "time_stop", "mfe_dist": mfe_dist, "mae_dist": mae_dist,
                    "exit_ts": b["ts"], "exit_price": b["close"]}
        if direction == "long":
            adverse = entry_price - b["low"]
            favorable = b["high"] - entry_price
        else:
            adverse = b["high"] - entry_price
            favorable = entry_price - b["low"]
        mfe_dist = max(mfe_dist, favorable)
        mae_dist = max(mae_dist, adverse)
        # Did stop hit?
        if adverse >= stop_dist:
            return {"exit_reason": "stop", "mfe_dist": mfe_dist, "mae_dist": stop_dist,
                    "exit_ts": b["ts"], "exit_price": sl}
    # End of data
    return {"exit_reason": "data_end", "mfe_dist": mfe_dist, "mae_dist": mae_dist,
            "exit_ts": bars[-1]["ts"] if bars else entry_ts, "exit_price": None}


# === Per-candidate replay ===
print("\nreplaying candidate trades forward...")
replay_results = []
for i, (idx, row) in enumerate(target.iterrows()):
    scan = row["best_candidate_scan"]
    if scan is None:
        replay_results.append({
            "idx": idx, "ledger_id": row["ledger_id"], "pair": row["pair"],
            "verdict": "no_scan_found", "outcome": "unknown",
        })
        continue

    inferred_dir = infer_direction(scan["z_score"], scan["bb_position"])
    if inferred_dir == "ambiguous":
        replay_results.append({
            "idx": idx, "ledger_id": row["ledger_id"], "pair": row["pair"],
            "verdict": "direction_ambiguous", "outcome": "unknown",
        })
        continue

    pair = row["pair"]
    entry_price = scan["current_close"]
    atr = scan["atr"]
    if entry_price is None or atr is None or atr <= 0:
        replay_results.append({
            "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
            "verdict": "missing_inputs", "outcome": "unknown",
        })
        continue

    # Stop distance = 1×ATR proxy for natural_stop
    stop_dist = atr
    walk = forward_walk(pair, scan["ts"], entry_price, inferred_dir, stop_dist, max_hold_hours=8)
    if walk is None:
        replay_results.append({
            "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
            "verdict": "no_m5_data", "outcome": "unknown",
        })
        continue

    mfe_r = walk["mfe_dist"] / stop_dist
    mae_r = walk["mae_dist"] / stop_dist
    actual_outcome_r = -1.0 if walk["exit_reason"] == "stop" else (walk["mfe_dist"] / stop_dist if walk["mfe_dist"] > 0 else 0.0)

    # Outcomes at different R targets
    out_1r = 1.0 if mfe_r >= 1.0 else (mae_r * -1 if mae_r >= 1.0 else 0)
    out_15r = 1.5 if mfe_r >= 1.5 else (mae_r * -1 if mae_r >= 1.0 else 0)
    out_2r = 2.0 if mfe_r >= 2.0 else (mae_r * -1 if mae_r >= 1.0 else 0)

    # Ratchet save (BE at 0.5R MFE)
    if mfe_r >= 0.5 and walk["exit_reason"] == "stop":
        out_ratchet = 0.0  # BE save
    elif mfe_r >= 2.0:
        out_ratchet = 2.0
    else:
        out_ratchet = actual_outcome_r

    # Classify
    if mfe_r >= 1.5 and mae_r < 1.0:
        outcome_class = "full_winner"
    elif mfe_r >= 0.5 and mae_r < 1.0:
        outcome_class = "partial_winner_or_ratchet_save"
    elif mfe_r >= 0.5 and walk["exit_reason"] == "stop":
        outcome_class = "gave_back_green"
    elif walk["exit_reason"] == "stop":
        outcome_class = "clean_stop"
    else:
        outcome_class = "ambiguous"

    replay_results.append({
        "idx": idx,
        "ledger_id": row["ledger_id"],
        "pair": pair,
        "step6b_recommendation": row["step6b_recommendation"],
        "bot_direction": row["direction"],
        "inferred_candidate_direction": inferred_dir,
        "scan_ts": scan["ts"],
        "scan_cycle": scan["cycle"],
        "scan_score": scan["score"],
        "scan_tier": scan["tier"],
        "scan_fam": scan["fam"],
        "entry_price": entry_price,
        "atr": atr,
        "stop_dist": stop_dist,
        "walk_mfe_r": float(mfe_r),
        "walk_mae_r": float(mae_r),
        "walk_exit_reason": walk["exit_reason"],
        "walk_exit_ts": walk["exit_ts"],
        "out_at_1R": float(out_1r),
        "out_at_1_5R": float(out_15r),
        "out_at_2R": float(out_2r),
        "out_with_ratchet": float(out_ratchet),
        "actual_outcome_r_proxy": float(actual_outcome_r),
        "outcome_class": outcome_class,
        "verdict": "replayed",
    })


replay_df = pd.DataFrame(replay_results)
print(f"  replay results: {len(replay_df)}")
print(f"\noutcome_class distribution:")
if "outcome_class" in replay_df.columns:
    print(replay_df["outcome_class"].value_counts(dropna=False).to_string())
print(f"\nverdict distribution:")
print(replay_df["verdict"].value_counts().to_string())

# === Promotion / demotion ===
print("\npromoting verified vs false candidates...")
def final_verdict(row):
    if row["verdict"] != "replayed":
        return row["verdict"]
    if row["outcome_class"] == "full_winner":
        if row["step6b_recommendation"] == "direction_repair_candidate":
            return "direction_repair_confirmed"
        else:
            return "same_direction_timing_repair_confirmed"
    if row["outcome_class"] in ("partial_winner_or_ratchet_save",):
        if row["step6b_recommendation"] == "direction_repair_candidate":
            return "direction_repair_partial"
        else:
            return "same_direction_timing_repair_partial"
    if row["outcome_class"] == "gave_back_green":
        return "false_candidate_management_dependent"
    if row["outcome_class"] == "clean_stop":
        return "false_candidate"
    return "ambiguous"

replay_df["final_verdict"] = replay_df.apply(final_verdict, axis=1)
print(f"\nfinal verdict distribution:")
print(replay_df["final_verdict"].value_counts().to_string())

# === Gate audit (lightweight) ===
print("\ngate audit: which scan fired in the candidate's cycle?")
gate_audit_rows = []
for r in replay_results:
    if "scan_cycle" not in r or not r.get("scan_cycle"):
        continue
    cycle_key = (r["pair"], r["scan_cycle"])
    siblings = cycle_scans.get(cycle_key, [])
    fired_in_cycle = [s for s in siblings if s.get("trade_id")]
    take_in_cycle = [s for s in siblings if s.get("verdict") in ("TAKE_A","TAKE_B")]
    gate_audit_rows.append({
        "ledger_id": r["ledger_id"],
        "scan_cycle": r["scan_cycle"],
        "n_siblings": len(siblings),
        "n_take_in_cycle": len(take_in_cycle),
        "n_fired_in_cycle": len(fired_in_cycle),
        "fired_trade_ids": [s["trade_id"] for s in fired_in_cycle],
    })
gate_audit_df = pd.DataFrame(gate_audit_rows)
print(f"  gate audit rows: {len(gate_audit_df)}")
print(f"  cycles with no fired trade: {(gate_audit_df['n_fired_in_cycle'] == 0).sum()}")
print(f"  cycles with fired trade(s): {(gate_audit_df['n_fired_in_cycle'] > 0).sum()}")

# Save outputs
replay_df.to_csv(OUT / "replay_results.csv", index=False)
replay_df.to_parquet(OUT / "replay_results.parquet", index=False)
gate_audit_df.to_csv(OUT / "gate_audit.csv", index=False)
print(f"\nsaved")
