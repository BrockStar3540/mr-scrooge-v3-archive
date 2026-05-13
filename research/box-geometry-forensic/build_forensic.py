"""Step 5 v2: box-geometry forensic using M5 entry-price lookup.

Source of entry_price: load M5 bars for pair, find bar at entry_ts.
Source of correct PDH/PDL: daily bars from prior trading day.

Same output as v1: same_direction_repair / direction_flip_repair / skip_required / no_clean_answer.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/box-geometry-forensic")
OUT.mkdir(parents=True, exist_ok=True)


def load_daily_bars(pair):
    pair_dir = DUKA / pair
    if not pair_dir.exists(): return None
    files = list(pair_dir.glob(f"{pair}_D_*.jsonl"))
    if not files: return None
    bars = []
    for f in files:
        for line in open(f):
            bars.append(json.loads(line))
    df = pd.DataFrame(bars)
    df["time"] = pd.to_datetime(df["time"], utc=True)
    df["date"] = df["time"].dt.date
    return df.set_index("date")


def load_m5_window(pair, start_ts, end_ts):
    """Stream M5 bars filtered to [start_ts, end_ts]. Returns dict by time."""
    pair_dir = DUKA / pair
    if not pair_dir.exists(): return {}
    files = sorted(pair_dir.glob(f"{pair}_M5_*.jsonl"))
    out = {}
    for f in files:
        # Filter by filename year range to skip irrelevant files
        stem = f.stem  # e.g. "EUR_USD_M5_2026-01-01_2026-04-22"
        parts = stem.rsplit("_", 2)
        if len(parts) >= 3:
            try:
                file_start = pd.Timestamp(parts[-2], tz="UTC")
                file_end = pd.Timestamp(parts[-1], tz="UTC")
                if file_end < start_ts or file_start > end_ts:
                    continue
            except Exception:
                pass
        for line in open(f):
            t = line[10:35]  # crude prefix filter on time string
            # safer: parse json
            try:
                d = json.loads(line)
            except:
                continue
            ts = pd.Timestamp(d["time"])
            if start_ts <= ts <= end_ts:
                out[ts] = d
    return out


def prior_pdh_pdl(daily_df, entry_date):
    if daily_df is None: return None, None, None
    for delta in range(1, 10):
        d = entry_date - timedelta(days=delta)
        if d in daily_df.index:
            row = daily_df.loc[d]
            if isinstance(row, pd.DataFrame): row = row.iloc[0]
            return float(row["high_bid"]), float(row["low_bid"]), d
    return None, None, None


def find_entry_price(m5_data, entry_ts):
    """Find the M5 bar containing entry_ts. Use bar open as entry price proxy."""
    # Round entry_ts down to nearest 5-min boundary
    minute = (entry_ts.minute // 5) * 5
    bar_ts = entry_ts.replace(minute=minute, second=0, microsecond=0, nanosecond=0)
    if bar_ts in m5_data:
        bar = m5_data[bar_ts]
        # Use ask side mid since trade direction varies
        return (float(bar["open_bid"]) + float(bar["open_ask"])) / 2
    # Fallback: any close bar within 30 min
    for offset_min in range(-30, 31, 5):
        candidate = bar_ts + timedelta(minutes=offset_min)
        if candidate in m5_data:
            bar = m5_data[candidate]
            return (float(bar["open_bid"]) + float(bar["open_ask"])) / 2
    return None


def classify_location(entry_price, pdh, pdl):
    if entry_price is None or pdh is None or pdl is None:
        return "unknown"
    box_range = pdh - pdl
    if box_range <= 0:
        return "invalid_box"
    pos = (entry_price - pdl) / box_range
    edge = 0.10
    if pos < -0.05:    return "below_pdl"
    elif pos < edge:   return "at_pdl_edge"
    elif pos > 1.05:   return "above_pdh"
    elif pos > 1 - edge: return "at_pdh_edge"
    else:              return "inside_box"


def classify_repair(direction, location, mfe, bug_ctx):
    if location in ("unknown", "invalid_box"):
        return "no_clean_answer", f"missing data for correct-box reconstruction (location={location})"

    if direction == "short":
        if location in ("at_pdh_edge", "above_pdh"):
            if pd.notna(mfe) and mfe > 0.5:
                return "same_direction_repair", f"valid short setup at correct PDH-edge ({location}); mfe={mfe:.2f}R → better management could capture"
            elif pd.notna(mfe) and mfe < 0.15:
                return "no_clean_answer", f"valid short at correct PDH-edge; mfe={mfe:.2f}R never developed"
            else:
                return "same_direction_repair", f"valid short at correct PDH-edge; mfe={mfe:.2f}R"
        elif location in ("at_pdl_edge", "below_pdl"):
            return "direction_flip_repair", f"bot shorted at PDL-edge ({location}) — long fade was the legitimate trade"
        else:  # inside_box
            if pd.notna(mfe) and mfe > 0.5:
                return "same_direction_repair", f"short from inside_box but ran +{mfe:.2f}R; legitimate but should have waited for PDH"
            return "skip_required", f"short from inside_box, mfe={mfe:.2f}R; no rail nearby — no setup"

    elif direction == "long":
        if location in ("at_pdl_edge", "below_pdl"):
            if pd.notna(mfe) and mfe > 0.5:
                return "same_direction_repair", f"valid long at correct PDL-edge ({location}); mfe={mfe:.2f}R"
            elif pd.notna(mfe) and mfe < 0.15:
                return "no_clean_answer", f"valid long location but mfe={mfe:.2f}R never developed"
            else:
                return "same_direction_repair", f"valid long at correct PDL-edge; mfe={mfe:.2f}R"
        elif location in ("at_pdh_edge", "above_pdh"):
            return "direction_flip_repair", f"bot longed at PDH-edge ({location}) — short fade was the legitimate trade"
        else:
            if pd.notna(mfe) and mfe > 0.5:
                return "same_direction_repair", f"long from inside_box but ran +{mfe:.2f}R; should have waited for PDL"
            return "skip_required", f"long from inside_box, mfe={mfe:.2f}R; no rail nearby"

    return "no_clean_answer", f"direction={direction!r}"


# === Load ===
df = pd.read_parquet(LEDGER)
contaminated = df[df["repair_taxonomy"] == "correct_box_replay_required"].copy()
contaminated["entry_ts"] = pd.to_datetime(contaminated["entry_ts"], utc=True, errors="coerce")
contaminated = contaminated[contaminated["entry_ts"].notna()]
print(f"contaminated rows with valid entry_ts: {len(contaminated)}")

# Group by pair for batched M5 loading
results = []
for pair, group in contaminated.groupby("pair"):
    print(f"\n[{pair}] {len(group)} rows")
    daily = load_daily_bars(pair)
    if daily is None:
        print(f"  no daily bars; marking all unknown")
        for idx, row in group.iterrows():
            results.append({
                "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
                "direction": row["direction"], "entry_ts": row["entry_ts"],
                "entry_price": None, "pdh": None, "pdl": None,
                "location": "unknown",
                "repair_recommendation": "no_clean_answer",
                "repair_evidence": "no daily bars for pair",
            })
        continue
    # M5 window: from earliest to latest entry_ts in this group
    t_min = group["entry_ts"].min() - timedelta(hours=1)
    t_max = group["entry_ts"].max() + timedelta(hours=1)
    m5 = load_m5_window(pair, t_min, t_max)
    print(f"  loaded {len(m5)} M5 bars")

    for idx, row in group.iterrows():
        ts = row["entry_ts"]
        direction = row["direction"]
        mfe = pd.to_numeric(row.get("actual_mfe_r"), errors="coerce")
        bug_ctx = row.get("box_boundary_context")

        entry_price = find_entry_price(m5, ts)
        pdh, pdl, ref_date = prior_pdh_pdl(daily, ts.date())
        location = classify_location(entry_price, pdh, pdl)
        recommendation, evidence = classify_repair(direction, location, mfe, bug_ctx)

        results.append({
            "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
            "direction": direction, "entry_ts": ts,
            "entry_date": str(ts.date()),
            "ref_date_used": str(ref_date) if ref_date else None,
            "entry_price": entry_price,
            "pdh": pdh, "pdl": pdl,
            "box_range_pips": (pdh - pdl) * (100 if pair.endswith("JPY") else 10000) if (pdh and pdl) else None,
            "location": location,
            "mfe_r": float(mfe) if pd.notna(mfe) else None,
            "realized_r": float(pd.to_numeric(row.get("actual_realized_r"), errors="coerce")) if pd.notna(row.get("actual_realized_r")) else None,
            "box_bug_context": row.get("box_boundary_context"),
            "session_bucket": row.get("session_bucket"),
            "session_quarter": row.get("session_quarter"),
            "pair_family": row.get("pair_family"),
            "bot_actual_strategy": row.get("bot_actual_strategy"),
            "repair_recommendation": recommendation,
            "repair_evidence": evidence,
        })

results_df = pd.DataFrame(results)
print(f"\n\n=== RESULTS: {len(results_df)} contaminated trades analyzed ===")
print(f"\nLocation distribution:")
print(results_df["location"].value_counts().to_string())

print(f"\n=== REPAIR RECOMMENDATION ===")
rec = results_df["repair_recommendation"].value_counts()
n = len(results_df)
for k, v in rec.items():
    print(f"  {k}: {v}/{n} = {v/n*100:.1f}%")

# Per-bug breakdown
print(f"\n=== BY BUG CONTEXT ===")
bug_breakdown = results_df.groupby("box_bug_context")["repair_recommendation"].value_counts().unstack(fill_value=0)
print(bug_breakdown.to_string())

# Per-pair_family breakdown
print(f"\n=== BY PAIR FAMILY ===")
pf_breakdown = results_df.groupby("pair_family")["repair_recommendation"].value_counts().unstack(fill_value=0)
print(pf_breakdown.to_string())

# Save
results_df.to_csv(OUT / "forensic_results.csv", index=False)
results_df.to_parquet(OUT / "forensic_results.parquet", index=False)

# Update ledger
df["correct_pdh"] = None
df["correct_pdl"] = None
df["reconstructed_entry_price"] = None
df["entry_location_vs_correct_box"] = None
df["repair_recommendation"] = None
df["repair_evidence"] = None
for r in results:
    idx = r["idx"]
    df.at[idx, "correct_pdh"] = r["pdh"]
    df.at[idx, "correct_pdl"] = r["pdl"]
    df.at[idx, "reconstructed_entry_price"] = r["entry_price"]
    df.at[idx, "entry_location_vs_correct_box"] = r["location"]
    df.at[idx, "repair_recommendation"] = r["repair_recommendation"]
    df.at[idx, "repair_evidence"] = r["repair_evidence"]

# Don't string-coerce the new numeric columns
for c in df.columns:
    if df[c].dtype == "object" and c not in ("correct_pdh", "correct_pdl", "reconstructed_entry_price"):
        df[c] = df[c].astype(str).replace({"nan": None, "None": None, "<NA>": None})
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"\nsaved ledger: {len(df)} rows, {len(df.columns)} cols")
