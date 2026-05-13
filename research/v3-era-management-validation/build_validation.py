"""V3 Broker-Era Directional Management Validation.

Question per 2026-05-13: does the short-BE@0.5R rule survive on ACTUAL V3 broker
trades with V3's actual natural_stop_pips, not the 1xATR-stop walker assumptions?

Method:
  1. For each broker trade with entry_ts >= 2026-04-20 (scans.jsonl coverage):
     - Find the entry scan in scans.jsonl (closest scan on same pair at or near entry_ts)
     - Pull entry_price from features.bollinger.current_close
     - Pull natural_stop_pips from ml_features.natural_stop_pips
     - Forward-walk through subsequent same-pair scans for up to 8h
     - Track MFE_r = mfe_pips / natural_stop_pips
  2. V0_baseline: use the broker's actual_realized_r (real V3 outcome)
  3. Apply BE variants:
     V_BE_0.5R: shorts with mfe_r >= 0.5 → floor realized at 0
     V_BE_0.6R: same with 0.6
     V_BE_0.7R: same with 0.7
     LONGS unchanged in all variants
  4. Tabulate by strategy, pair_family, session, direction

Honest framing: this is forensic, not predictive. Real production of BE@0.5R
would trip on retracement that this measurement doesn't see. Upper bound caveat applies.
"""
import pandas as pd
import json
import numpy as np
from pathlib import Path
from datetime import timedelta
from collections import defaultdict

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
SCANS_FILE = "/data/scrooge-v3-data/ml-observer/scans.jsonl"
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/v3-era-management-validation")
OUT.mkdir(parents=True, exist_ok=True)


df = pd.read_parquet(LEDGER)
broker = df[df["source_label"].isin(["bot_actual_winner", "bot_actual_loser"])].copy()
broker["entry_ts"] = pd.to_datetime(broker["entry_ts"], utc=True, errors="coerce")
v3_cutoff = pd.Timestamp("2026-04-20", tz="UTC")
v3_broker = broker[broker["entry_ts"] >= v3_cutoff].copy()
v3_broker["realized_r"] = pd.to_numeric(v3_broker["actual_realized_r"], errors="coerce")
print(f"V3-era broker trades (entry_ts >= 2026-04-20): {len(v3_broker)}")
print(f"  winners: {(v3_broker['realized_r'] > 0).sum()}")
print(f"  losers: {(v3_broker['realized_r'] <= 0).sum()}")
print(f"  by direction: {v3_broker['direction'].value_counts().to_dict()}")
print(f"  by strategy: {v3_broker['bot_actual_strategy'].value_counts().to_dict()}")

target_pairs = set(v3_broker["pair"].unique())
t_min = v3_broker["entry_ts"].min() - timedelta(hours=1)
t_max = v3_broker["entry_ts"].max() + timedelta(hours=10)

# Build scans index per pair
print(f"\nstreaming scans.jsonl ...")
scans_per_pair = defaultdict(list)
n = 0
with open(SCANS_FILE) as f:
    for line in f:
        n += 1
        try: d = json.loads(line)
        except: continue
        sym = d.get("symbol")
        if sym not in target_pairs: continue
        ts_str = d.get("ts")
        if not ts_str: continue
        try: ts = pd.Timestamp(ts_str)
        except: continue
        if ts < t_min or ts > t_max: continue
        bb = (d.get("features") or {}).get("bollinger") or {}
        ml = d.get("ml_features") or {}
        scans_per_pair[sym].append({
            "ts": ts,
            "current_close": bb.get("current_close"),
            "natural_stop_pips": ml.get("natural_stop_pips"),
            "atr": ml.get("atr"),
        })
print(f"  read {n:,} scan lines")
for p in scans_per_pair:
    scans_per_pair[p] = sorted(scans_per_pair[p], key=lambda x: x["ts"])


def pip_size(pair):
    return 0.01 if pair.endswith("JPY") else 0.0001


def forward_walk_v3(pair, entry_ts, direction, entry_price, stop_pips):
    """Walk forward up to 8h using scan current_close prices on same pair.
    Returns mfe_pips and outcome detail."""
    scans = scans_per_pair.get(pair, [])
    if not scans or entry_price is None or stop_pips is None or stop_pips <= 0:
        return None
    end_ts = entry_ts + timedelta(hours=8)
    pip = pip_size(pair)
    stop_dist_price = stop_pips * pip
    sl = entry_price + stop_dist_price if direction == "short" else entry_price - stop_dist_price
    mfe_pips = 0.0
    mae_pips = 0.0
    sample_count = 0
    for s in scans:
        if s["ts"] <= entry_ts: continue
        if s["ts"] > end_ts:
            return {"exit_reason":"time","mfe_pips":mfe_pips,"mae_pips":mae_pips,"n_samples":sample_count}
        cc = s["current_close"]
        if cc is None: continue
        sample_count += 1
        if direction == "long":
            adv_pips = (entry_price - cc) / pip
            fav_pips = (cc - entry_price) / pip
        else:
            adv_pips = (cc - entry_price) / pip
            fav_pips = (entry_price - cc) / pip
        if fav_pips > mfe_pips: mfe_pips = fav_pips
        if adv_pips > mae_pips: mae_pips = adv_pips
        if adv_pips >= stop_pips:
            return {"exit_reason":"stop","mfe_pips":mfe_pips,"mae_pips":stop_pips,"n_samples":sample_count}
    return {"exit_reason":"data_end","mfe_pips":mfe_pips,"mae_pips":mae_pips,"n_samples":sample_count}


def find_entry_scan(pair, entry_ts, direction):
    """Find the scan at or just before entry_ts on the same pair."""
    scans = scans_per_pair.get(pair, [])
    if not scans: return None
    # closest scan within ±5 min
    best = None
    best_dt = timedelta(minutes=5)
    for s in scans:
        dt = abs(s["ts"] - entry_ts)
        if dt < best_dt:
            best_dt = dt
            best = s
    return best


# Per-trade forward walk
print(f"\nforward-walking V3-era broker trades ...")
walks = []
for idx, row in v3_broker.iterrows():
    pair = row["pair"]
    entry_ts = row["entry_ts"]
    direction = row["direction"]
    actual_r = row["realized_r"]
    if pd.isna(actual_r): continue
    anchor = find_entry_scan(pair, entry_ts, direction)
    if anchor is None or anchor.get("current_close") is None:
        walks.append({"idx":idx,"verdict":"no_anchor_scan","mfe_r":None,"actual_r":float(actual_r)})
        continue
    entry_price = anchor["current_close"]
    stop_pips = anchor.get("natural_stop_pips")
    if stop_pips is None or stop_pips <= 0:
        # Fall back to ATR-derived stop if natural_stop_pips missing
        atr = anchor.get("atr")
        if atr is not None and atr > 0:
            # ATR is in price units; convert to pips
            stop_pips = atr / pip_size(pair)
        else:
            walks.append({"idx":idx,"verdict":"no_stop_basis","mfe_r":None,"actual_r":float(actual_r)})
            continue
    walk = forward_walk_v3(pair, entry_ts, direction, entry_price, stop_pips)
    if walk is None:
        walks.append({"idx":idx,"verdict":"no_walk","mfe_r":None,"actual_r":float(actual_r)})
        continue
    mfe_r = walk["mfe_pips"] / stop_pips if stop_pips > 0 else 0
    walks.append({
        "idx": idx,
        "ledger_id": row["ledger_id"],
        "pair": pair, "direction": direction,
        "strategy": row["bot_actual_strategy"],
        "pair_family": row["pair_family"],
        "session_bucket": row["session_bucket"],
        "actual_r": float(actual_r),
        "entry_price": entry_price,
        "stop_pips": stop_pips,
        "mfe_pips": walk["mfe_pips"],
        "mae_pips": walk["mae_pips"],
        "mfe_r": float(mfe_r),
        "walk_exit": walk["exit_reason"],
        "n_samples": walk["n_samples"],
        "verdict": "ok",
    })

walks_df = pd.DataFrame(walks)
print(f"  walks: {len(walks_df)}")
print(f"  ok: {(walks_df['verdict'] == 'ok').sum()}")
print(f"  by verdict: {walks_df['verdict'].value_counts().to_dict()}")


# Filter to OK walks
ok = walks_df[walks_df["verdict"] == "ok"].copy()
print(f"\n=== USABLE TRADES FOR ANALYSIS: {len(ok)} ===")
print(f"  direction: {ok['direction'].value_counts().to_dict()}")
print(f"  by strategy: {ok['strategy'].value_counts().to_dict()}")
print(f"  mfe_r distribution: min={ok['mfe_r'].min():.2f} median={ok['mfe_r'].median():.2f} max={ok['mfe_r'].max():.2f}")


# Apply variants
def variant_r(actual_r, mfe_r, direction, be_threshold):
    """Short BE rule: if direction=short AND mfe_r >= threshold AND actual<0, floor at 0."""
    out = actual_r.copy()
    trip = (direction == "short") & (mfe_r >= be_threshold) & (out < 0)
    out.loc[trip] = 0.0
    return out


variants = {
    "V0_baseline": ok["actual_r"].copy(),
}
for t in [0.5, 0.6, 0.7]:
    variants[f"V_short_BE_{t:.1f}R"] = variant_r(ok["actual_r"], ok["mfe_r"], ok["direction"], t)


# Global summary
print(f"\n=== GLOBAL SUMMARY (V3-era, actual V3 outcomes) ===")
g_rows = []
for name, r in variants.items():
    g_rows.append({
        "variant": name,
        "n": len(r),
        "total_R": float(r.sum()),
        "mean_R": float(r.mean()),
        "winner_rate": float((r > 0).mean()),
    })
g_df = pd.DataFrame(g_rows)
base = g_df.loc[g_df["variant"] == "V0_baseline", "total_R"].iloc[0]
g_df["delta_total_R"] = g_df["total_R"] - base
g_df["delta_per_trade"] = g_df["delta_total_R"] / g_df["n"]
print(g_df.to_string(index=False))
g_df.to_csv(OUT / "global_summary.csv", index=False)


# Per direction
print(f"\n=== PER DIRECTION ===")
for dr in ["short", "long"]:
    mask = ok["direction"] == dr
    sub_actual = ok.loc[mask, "actual_r"]
    print(f"\n  {dr.upper()} (n={mask.sum()}):")
    rows = []
    for name, r in variants.items():
        sub_r = r[mask]
        rows.append({
            "variant": name,
            "n": int(mask.sum()),
            "total_R": float(sub_r.sum()),
            "mean_R": float(sub_r.mean()),
            "winner_rate": float((sub_r > 0).mean()),
        })
    rep = pd.DataFrame(rows)
    rep["delta_total"] = rep["total_R"] - rep.loc[rep["variant"] == "V0_baseline", "total_R"].iloc[0]
    rep["delta_per_trade"] = rep["delta_total"] / rep["n"]
    print(rep.to_string(index=False))
    rep.to_csv(OUT / f"direction_{dr}_summary.csv", index=False)


# Per (strategy, direction)
print(f"\n=== PER STRATEGY × DIRECTION ===")
sd_rows = []
for (s, dr), grp in ok.groupby(["strategy","direction"]):
    base = grp["actual_r"].sum()
    be05 = variants["V_short_BE_0.5R"].loc[grp.index].sum()
    be07 = variants["V_short_BE_0.7R"].loc[grp.index].sum()
    sd_rows.append({
        "strategy": s, "direction": dr, "n": len(grp),
        "baseline_total_R": float(base),
        "baseline_mean_R": float(grp["actual_r"].mean()),
        "BE_0.5R_total": float(be05),
        "BE_0.7R_total": float(be07),
        "delta_BE_0.5": float(be05 - base),
        "delta_BE_0.7": float(be07 - base),
    })
sd_df = pd.DataFrame(sd_rows)
print(sd_df.to_string(index=False))
sd_df.to_csv(OUT / "per_strategy_direction.csv", index=False)


# Cell-level analysis (pair_family × direction × session)
print(f"\n=== PER (pair_family × direction × session) ===")
cell_rows = []
for (pf, dr, sb), grp in ok.groupby(["pair_family","direction","session_bucket"]):
    base = grp["actual_r"].sum()
    be05 = variants["V_short_BE_0.5R"].loc[grp.index].sum()
    be07 = variants["V_short_BE_0.7R"].loc[grp.index].sum()
    cell_rows.append({
        "pair_family": pf, "direction": dr, "session_bucket": sb,
        "n": len(grp),
        "baseline_total_R": float(base),
        "BE_0.5R_total": float(be05),
        "BE_0.7R_total": float(be07),
        "delta_BE_0.5": float(be05 - base),
        "delta_BE_0.7": float(be07 - base),
    })
cell_df = pd.DataFrame(cell_rows).sort_values("delta_BE_0.5", ascending=False)
print(cell_df.head(20).to_string(index=False))
cell_df.to_csv(OUT / "per_cell.csv", index=False)

# Count: how many SHORT winners get hurt by BE@0.5R?
# A "hurt" = the broker's actual was a winning short, but our BE@0.5R rule would have intervened.
# Under our model, winners (actual_r > 0) don't get touched (rule only floors actual < 0 at 0).
# So no winners are stripped. But in production reality, BE@0.5R could prematurely cap a winner on retracement.

# What WE can measure: # of short winners with mfe_r >= 0.5 (where BE would have triggered).
# Those are the winners at RISK of being stopped at BE in real production (upper bound caveat).
short_winners = ok[(ok["direction"] == "short") & (ok["actual_r"] > 0)]
at_risk = short_winners[short_winners["mfe_r"] >= 0.5]
print(f"\n=== SHORT WINNERS AT RISK OF PREMATURE BE STOP (upper-bound caveat) ===")
print(f"  total short winners: {len(short_winners)}")
print(f"  at risk (mfe >= 0.5R): {len(at_risk)} ({len(at_risk)/max(len(short_winners),1)*100:.1f}%)")
print(f"  total R from these winners: {at_risk['actual_r'].sum():.2f}")
print(f"  (this R could be lost if BE trips before the winning move)")

# Save walks
walks_df.to_csv(OUT / "walks.csv", index=False)
print(f"\nsaved {OUT}")
