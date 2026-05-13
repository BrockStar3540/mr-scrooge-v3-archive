"""v2 order-of-events bar-by-bar management replay.

Tests whether the V_BE05 dominance found via mfe/mae approximation survives
explicit state-machine replay on top double-survivor cells.

For each top cell, re-load the pair's M5 bars, find the same entry candidates
by (pair, entry_ts), and forward-walk each candidate with five managements
running in parallel — each as its own state machine that responds to bars in
order.

Variants:
  V_2R     stop at -1R, TP at +2R
  V_1R     stop at -1R, TP at +1R
  V_BE05   stop at -1R until mfe>=0.5R then stop moves to entry (0), TP at +2R
  V_BE10   stop at -1R until mfe>=1.0R then stop moves to entry (0), TP at +2R
  V_PART1  TP1 at +1R (half off), runner with BE at 1R then TP at +2R

All include spread_cost on exit.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path

DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v2")
MAX_HOLD = 300

SPREAD_PIPS = {
    "EUR_USD": 0.6, "GBP_USD": 0.9, "AUD_USD": 0.8, "NZD_USD": 1.2,
    "USD_JPY": 0.7, "USD_CHF": 1.0, "USD_CAD": 1.2, "USD_MXN": 12.0,
    "EUR_GBP": 1.0, "EUR_AUD": 1.6, "EUR_NZD": 2.8, "EUR_CAD": 1.8,
    "EUR_CHF": 1.4, "EUR_JPY": 1.2,
    "GBP_AUD": 2.5, "GBP_NZD": 3.5, "GBP_CAD": 2.4, "GBP_CHF": 2.2, "GBP_JPY": 1.6,
    "AUD_CAD": 1.5, "AUD_CHF": 1.8, "AUD_JPY": 1.2, "AUD_NZD": 2.0,
    "CAD_JPY": 1.5, "CHF_JPY": 1.6, "NZD_JPY": 1.8,
}


def pip_size(pair): return 0.01 if pair.endswith("JPY") else 0.0001


def load_pair_m5(pair):
    bars = []
    for f in sorted(Path(DUKA / pair).glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({
                    "time": d["time"],
                    "high": (d["high_bid"] + d["high_ask"]) / 2,
                    "low":  (d["low_bid"]  + d["low_ask"])  / 2,
                    "close":(d["close_bid"]+ d["close_ask"])/ 2,
                })
            except: pass
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)


def oop_walk_long(highs, lows, ei, ep, sd, spread_cost, max_hold=MAX_HOLD):
    """Returns dict of {variant: realized_r}."""
    end = min(ei + max_hold, len(highs) - 1)
    sl = ep - sd
    tp_1r = ep + sd
    tp_2r = ep + 2*sd
    # State machines per variant
    # Each: (active, realized_r). active=True means still in trade.
    state = {
        "V_2R":   {"open": True, "sl": sl,     "be_armed": False, "tp": tp_2r, "r": None},
        "V_1R":   {"open": True, "sl": sl,     "be_armed": False, "tp": tp_1r, "r": None},
        "V_BE05": {"open": True, "sl": sl,     "be_armed": False, "tp": tp_2r, "be_thresh": ep + 0.5*sd, "r": None},
        "V_BE10": {"open": True, "sl": sl,     "be_armed": False, "tp": tp_2r, "be_thresh": ep + 1.0*sd, "r": None},
        "V_PART1":{"open": True, "sl": sl,     "part_taken": False, "tp_runner": tp_2r, "tp_part": tp_1r, "r_acc": 0.0, "r": None},
    }
    for i in range(ei + 1, end + 1):
        h = highs[i]; l = lows[i]
        # V_2R
        s = state["V_2R"]
        if s["open"]:
            # check stop first (conservative — within-bar ordering unknown)
            if l <= s["sl"]:
                s["open"] = False; s["r"] = -1.0 - spread_cost/sd
            elif h >= s["tp"]:
                s["open"] = False; s["r"] = 2.0 - spread_cost/sd
        # V_1R
        s = state["V_1R"]
        if s["open"]:
            if l <= s["sl"]:
                s["open"] = False; s["r"] = -1.0 - spread_cost/sd
            elif h >= s["tp"]:
                s["open"] = False; s["r"] = 1.0 - spread_cost/sd
        # V_BE05
        s = state["V_BE05"]
        if s["open"]:
            # arm BE if mfe>=0.5R (high in this bar)
            if not s["be_armed"] and h >= s["be_thresh"]:
                s["be_armed"] = True
                # check if same bar also hit stop AFTER arming: if low<entry, BE-stop at 0
                # conservative: assume arm happens at the threshold, then for rest of bar low can hit BE
                if l <= ep:
                    s["open"] = False; s["r"] = 0.0 - spread_cost/sd
                    s["sl"] = ep  # for record
            elif s["be_armed"] and l <= ep:
                s["open"] = False; s["r"] = 0.0 - spread_cost/sd
            elif l <= s["sl"]:
                s["open"] = False; s["r"] = -1.0 - spread_cost/sd
            if s["open"] and h >= s["tp"]:
                s["open"] = False; s["r"] = 2.0 - spread_cost/sd
        # V_BE10
        s = state["V_BE10"]
        if s["open"]:
            if not s["be_armed"] and h >= s["be_thresh"]:
                s["be_armed"] = True
                if l <= ep:
                    s["open"] = False; s["r"] = 0.0 - spread_cost/sd
            elif s["be_armed"] and l <= ep:
                s["open"] = False; s["r"] = 0.0 - spread_cost/sd
            elif l <= s["sl"]:
                s["open"] = False; s["r"] = -1.0 - spread_cost/sd
            if s["open"] and h >= s["tp"]:
                s["open"] = False; s["r"] = 2.0 - spread_cost/sd
        # V_PART1
        s = state["V_PART1"]
        if s["open"]:
            if not s["part_taken"]:
                if l <= s["sl"]:
                    s["open"] = False; s["r"] = -1.0 - spread_cost/sd
                elif h >= s["tp_part"]:
                    # take half at +1R (pay half-spread on this exit), arm BE on runner
                    s["part_taken"] = True
                    s["r_acc"] = 0.5 * (1.0 - spread_cost/sd)
                    s["sl"] = ep  # runner BE at entry
            else:
                if l <= s["sl"]:
                    s["open"] = False; s["r"] = s["r_acc"] + 0.5 * (0.0 - spread_cost/sd)
                elif h >= s["tp_runner"]:
                    s["open"] = False; s["r"] = s["r_acc"] + 0.5 * (2.0 - spread_cost/sd)
    # time-stop for any still open
    for v, s in state.items():
        if s["open"]:
            if v == "V_PART1" and s["part_taken"]:
                s["r"] = s["r_acc"] + 0.5 * (0.0 - spread_cost/sd)
            else:
                s["r"] = 0.0 - spread_cost/sd
    return {v: s["r"] for v, s in state.items()}


def oop_walk_short(highs, lows, ei, ep, sd, spread_cost, max_hold=MAX_HOLD):
    end = min(ei + max_hold, len(highs) - 1)
    sl = ep + sd
    tp_1r = ep - sd
    tp_2r = ep - 2*sd
    state = {
        "V_2R":   {"open": True, "sl": sl,     "tp": tp_2r, "r": None},
        "V_1R":   {"open": True, "sl": sl,     "tp": tp_1r, "r": None},
        "V_BE05": {"open": True, "sl": sl,     "be_armed": False, "tp": tp_2r, "be_thresh": ep - 0.5*sd, "r": None},
        "V_BE10": {"open": True, "sl": sl,     "be_armed": False, "tp": tp_2r, "be_thresh": ep - 1.0*sd, "r": None},
        "V_PART1":{"open": True, "sl": sl,     "part_taken": False, "tp_runner": tp_2r, "tp_part": tp_1r, "r_acc": 0.0, "r": None},
    }
    for i in range(ei + 1, end + 1):
        h = highs[i]; l = lows[i]
        # V_2R / V_1R
        for k in ("V_2R","V_1R"):
            s = state[k]
            if s["open"]:
                if h >= s["sl"]:
                    s["open"] = False; s["r"] = -1.0 - spread_cost/sd
                elif l <= s["tp"]:
                    s["open"] = False; s["r"] = (2.0 if k=="V_2R" else 1.0) - spread_cost/sd
        # V_BE05 / V_BE10
        for k in ("V_BE05","V_BE10"):
            s = state[k]
            if s["open"]:
                if not s["be_armed"] and l <= s["be_thresh"]:
                    s["be_armed"] = True
                    if h >= ep:
                        s["open"] = False; s["r"] = 0.0 - spread_cost/sd
                elif s["be_armed"] and h >= ep:
                    s["open"] = False; s["r"] = 0.0 - spread_cost/sd
                elif h >= s["sl"]:
                    s["open"] = False; s["r"] = -1.0 - spread_cost/sd
                if s["open"] and l <= s["tp"]:
                    s["open"] = False; s["r"] = 2.0 - spread_cost/sd
        # V_PART1
        s = state["V_PART1"]
        if s["open"]:
            if not s["part_taken"]:
                if h >= s["sl"]:
                    s["open"] = False; s["r"] = -1.0 - spread_cost/sd
                elif l <= s["tp_part"]:
                    s["part_taken"] = True
                    s["r_acc"] = 0.5 * (1.0 - spread_cost/sd)
                    s["sl"] = ep
            else:
                if h >= s["sl"]:
                    s["open"] = False; s["r"] = s["r_acc"] + 0.5 * (0.0 - spread_cost/sd)
                elif l <= s["tp_runner"]:
                    s["open"] = False; s["r"] = s["r_acc"] + 0.5 * (2.0 - spread_cost/sd)
    for v, s in state.items():
        if s["open"]:
            if v == "V_PART1" and s["part_taken"]:
                s["r"] = s["r_acc"] + 0.5 * (0.0 - spread_cost/sd)
            else:
                s["r"] = 0.0 - spread_cost/sd
    return {v: s["r"] for v, s in state.items()}


# Load v2 parquet, isolate top-20 cells, re-walk
print("loading v2 candidates ...")
full = pd.read_parquet(OUT / "raw_m5_v2_candidate_events.parquet")
full["_cell"] = full["trigger_type"]+"|"+full["pair_family"]+"|"+full["direction"]+"|"+full["session_quarter"]+"|"+full["m15_trend"].astype(str)+"|"+full["h1_regime"].astype(str)

ds = pd.read_csv(OUT / "report_double_survivors.csv")
ds["_cell"] = ds["trigger_type"]+"|"+ds["pair_family"]+"|"+ds["direction"]+"|"+ds["session_quarter"]+"|"+ds["m15_trend"].astype(str)+"|"+ds["h1_regime"].astype(str)
top = ds.sort_values("mean_R_2r_disc", ascending=False).head(20)
top_cells_set = set(top["_cell"])

cand = full[full["_cell"].isin(top_cells_set)].copy()
print(f"top-20-cell candidates to replay: {len(cand)}")
print(f"pairs involved: {sorted(cand['pair'].unique())}")

# Group by pair for efficient bar loading
results = []
for pair in sorted(cand["pair"].unique()):
    sub = cand[cand["pair"] == pair].sort_values("entry_ts")
    print(f"\n[{pair}] candidates: {len(sub)} — loading bars ...")
    bars = load_pair_m5(pair)
    bars_ts = bars["ts"].values
    highs = bars["high"].values
    lows = bars["low"].values
    # build ts -> index lookup
    ts_to_idx = {t: i for i, t in enumerate(bars_ts)}
    spread_px = SPREAD_PIPS[pair] * pip_size(pair)
    for _, r in sub.iterrows():
        ts = np.datetime64(r["entry_ts"])
        ei = ts_to_idx.get(ts)
        if ei is None: continue
        ep = r["entry_price"]
        sd = r["atr14"]
        spread_cost = spread_px / 2
        if r["direction"] == "long":
            out = oop_walk_long(highs, lows, ei, ep, sd, spread_cost)
        else:
            out = oop_walk_short(highs, lows, ei, ep, sd, spread_cost)
        results.append({
            "_cell": r["_cell"],
            "pair": pair,
            "entry_ts": r["entry_ts"],
            "era": r["era"],
            "trigger_type": r["trigger_type"],
            "pair_family": r["pair_family"],
            "direction": r["direction"],
            "session_quarter": r["session_quarter"],
            "m15_trend": r["m15_trend"],
            "h1_regime": r["h1_regime"],
            **out,
        })

rdf = pd.DataFrame(results)
rdf.to_csv(OUT / "report_oop_replay_top20.csv", index=False)
print(f"\ntotal replayed: {len(rdf)}")

# Aggregate by cell, by era
print("\n=== ORDER-OF-EVENTS VARIANT MEANS (per cell, per era) ===")
agg = rdf.groupby(["_cell","era"]).agg(
    n=("V_2R","size"),
    V_2R=("V_2R","mean"),
    V_1R=("V_1R","mean"),
    V_BE05=("V_BE05","mean"),
    V_BE10=("V_BE10","mean"),
    V_PART1=("V_PART1","mean"),
).reset_index()
# Pivot eras side-by-side
piv = agg.pivot(index="_cell", columns="era", values=["n","V_2R","V_1R","V_BE05","V_BE10","V_PART1"])
piv.columns = [f"{a}_{b}" for a,b in piv.columns]
piv = piv.reset_index()
# Merge cell descriptors
desc = rdf.drop_duplicates("_cell")[["_cell","trigger_type","pair_family","direction","session_quarter","m15_trend","h1_regime"]]
piv = desc.merge(piv, on="_cell")
piv = piv.sort_values("V_2R_discovery", ascending=False)
print(piv.to_string(index=False, float_format="%.3f"))
piv.to_csv(OUT / "report_oop_replay_top20_pivot.csv", index=False)

# Summary: which variant wins per cell, by era
print("\n=== BEST VARIANT PER CELL ===")
variants = ["V_2R","V_1R","V_BE05","V_BE10","V_PART1"]
piv["best_disc"] = piv[[f"{v}_discovery" for v in variants]].idxmax(axis=1).str.replace("_discovery","")
piv["best_hold"] = piv[[f"{v}_holdout"   for v in variants]].idxmax(axis=1).str.replace("_holdout","")
print(piv[["trigger_type","pair_family","direction","session_quarter","m15_trend","h1_regime",
           "best_disc","best_hold",
           "V_2R_discovery","V_BE05_discovery","V_BE05_holdout"]].to_string(index=False))
print("\nbest_disc value counts:")
print(piv["best_disc"].value_counts())
print("\nbest_hold value counts:")
print(piv["best_hold"].value_counts())

# Compare V_BE05 vs V_2R lift, signed
piv["BE05_lift_disc"] = piv["V_BE05_discovery"] - piv["V_2R_discovery"]
piv["BE05_lift_hold"] = piv["V_BE05_holdout"]   - piv["V_2R_holdout"]
print(f"\nV_BE05 vs V_2R lift (discovery): mean = {piv['BE05_lift_disc'].mean():+.3f}, "
      f"median = {piv['BE05_lift_disc'].median():+.3f}, positive = {(piv['BE05_lift_disc']>0).sum()}/{len(piv)}")
print(f"V_BE05 vs V_2R lift (holdout):   mean = {piv['BE05_lift_hold'].mean():+.3f}, "
      f"median = {piv['BE05_lift_hold'].median():+.3f}, positive = {(piv['BE05_lift_hold']>0).sum()}/{len(piv)}")

print(f"\nsaved {OUT}/report_oop_replay_top20*.csv")
