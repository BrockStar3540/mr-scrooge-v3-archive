"""Management-Bug Atlas v1 — using per_trade_factors_filled (90K trades with real MFE/MAE).

The broker ledger doesn't have MFE/MAE populated. The sim audit corpus does.
This is the intraday-safe outcome data Brock asked for.

Source: per_trade_factors_filled.csv.gz
  90,024 filled simulated trades
  All have max_favorable_r, max_adverse_r, realized_r
  Strategy labels are V3 branches: direct, dbb_trend
  Date window: 2026-03-15 → 2026-04-13 (V1/V2 live era)
  This data was the audit's per-trade factor walk — it's the same
  one Step 8 used but here we ignore factor signatures entirely
  and focus on exit-path metrics only.

Grain: strategy × pair_family × direction × session_bucket
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

SRC = "/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/factor_audit/per_trade_factors_filled.csv.gz"
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/management-bug-atlas-v1")
OUT.mkdir(parents=True, exist_ok=True)

PAIR_FAMILY = {
    "EUR_USD":"usd_base","GBP_USD":"usd_base","AUD_USD":"usd_base","NZD_USD":"usd_base",
    "USD_JPY":"usd_base","USD_CHF":"usd_base","USD_CAD":"usd_base","USD_MXN":"usd_base",
    "EUR_GBP":"eur_cross","EUR_AUD":"eur_cross","EUR_NZD":"eur_cross","EUR_CAD":"eur_cross",
    "EUR_CHF":"eur_cross","EUR_JPY":"eur_cross",
    "GBP_AUD":"gbp_cross","GBP_NZD":"gbp_cross","GBP_CAD":"gbp_cross","GBP_CHF":"gbp_cross","GBP_JPY":"gbp_cross",
    "AUD_NZD":"antipodean_cross","AUD_CAD":"antipodean_cross","AUD_CHF":"antipodean_cross",
    "AUD_JPY":"antipodean_cross","NZD_JPY":"antipodean_cross","CAD_JPY":"antipodean_cross","CHF_JPY":"antipodean_cross",
}

def session_of(h):
    if pd.isna(h): return "unknown"
    h = int(h) % 24
    if 22 <= h or h < 6: return "asia"
    elif 6 <= h < 12: return "london"
    elif 12 <= h < 16: return "overlap"
    else: return "ny_pm"

print(f"loading {SRC} ...")
df = pd.read_csv(SRC)
df["pair_family"] = df["symbol"].map(PAIR_FAMILY).fillna("other")
df["session_bucket"] = df["hour_utc"].apply(session_of)
df["mfe_r"] = pd.to_numeric(df["max_favorable_r"], errors="coerce")
df["mae_r"] = pd.to_numeric(df["max_adverse_r"], errors="coerce")
df["realized_r"] = pd.to_numeric(df["realized_r"], errors="coerce")
print(f"  loaded {len(df):,} sim trades")
print(f"  strategies: {df['strategy'].value_counts().to_dict()}")
print(f"  pair_families: {df['pair_family'].value_counts().to_dict()}")
print(f"  sessions: {df['session_bucket'].value_counts().to_dict()}")
print(f"  MFE distribution: min={df['mfe_r'].min():.2f} median={df['mfe_r'].median():.2f} max={df['mfe_r'].max():.2f}")
print()

THRESHOLDS = [0.3, 0.5, 0.7, 1.0, 1.5, 2.0]
R_TARGET = 2.0  # r_multiple from corpus

def cell_metrics(g):
    n = len(g)
    if n < 30:
        return {"n_trades": n, "insufficient": True}
    r = g["realized_r"]
    mfe = g["mfe_r"]
    out = {"n_trades": n}
    out["winner_pct"] = (r > 0).mean()
    out["full_tp_pct"] = (mfe >= 1.9).mean()  # 2.0R target with small tolerance
    out["clean_stop_pct"] = ((r <= -0.95) & (mfe < 0.15)).mean()
    out["gave_back_pct"] = ((mfe > 0.3) & (r < -0.1)).mean()
    out["mfe_median"] = float(mfe.median())
    out["mfe_p25"] = float(mfe.quantile(0.25))
    out["mfe_p75"] = float(mfe.quantile(0.75))
    out["mfe_p90"] = float(mfe.quantile(0.90))
    out["realized_median"] = float(r.median())
    out["realized_mean"] = float(r.mean())
    out["holding_min_median"] = float(pd.to_numeric(g["holding_minutes"], errors="coerce").median())
    out["time_to_05R_min"] = float(pd.to_numeric(g["time_to_0_5r"], errors="coerce").median()) if "time_to_0_5r" in g else None
    out["time_to_1R_min"] = float(pd.to_numeric(g["time_to_1r"], errors="coerce").median()) if "time_to_1r" in g else None
    for t in THRESHOLDS:
        reached = (mfe >= t)
        held = reached & (r >= t * 0.95)
        gave_back = reached & (r <= 0)
        out[f"reached_{t:.1f}R_pct"] = float(reached.mean())
        out[f"held_{t:.1f}R_pct"] = float(held.mean())
        out[f"conv_{t:.1f}R"] = float(held.sum() / max(reached.sum(), 1))
        out[f"giveback_at_{t:.1f}R_pct"] = float(gave_back.mean())
    return out


def derive_recommendation(m):
    if m.get("insufficient"):
        return "insufficient_data", f"n={m['n_trades']}"
    r03 = m.get("reached_0.3R_pct", 0)
    r05 = m.get("reached_0.5R_pct", 0)
    r07 = m.get("reached_0.7R_pct", 0)
    r10 = m.get("reached_1.0R_pct", 0)
    r15 = m.get("reached_1.5R_pct", 0)
    r20 = m.get("reached_2.0R_pct", 0)
    c10 = m.get("conv_1.0R", 0)
    c20 = m.get("conv_2.0R", 0)
    gb05 = m.get("giveback_at_0.5R_pct", 0)
    gb10 = m.get("giveback_at_1.0R_pct", 0)
    clean = m.get("clean_stop_pct", 0)
    gave_back = m.get("gave_back_pct", 0)
    wr = m.get("winner_pct", 0)

    # Priority cascade
    if r03 < 0.30:
        return "skip_cell", f"only {r03*100:.1f}% reach 0.3R; entry doesn't develop"
    if r20 > 0.20 and c20 > 0.60:
        return "hold_for_2R", f"{r20*100:.1f}% reach 2R, conversion {c20*100:.1f}%"
    if r10 > 0.30 and c10 > 0.55:
        return "hold_for_1R", f"{r10*100:.1f}% reach 1R, conversion {c10*100:.1f}%"
    if gb05 > 0.30 and r07 < 0.20:
        return "earlier_BE_at_0.5R", f"reach 0.5R {r05*100:.1f}% but {gb05*100:.1f}% give back; only {r07*100:.1f}% reach 0.7R"
    if r05 > 0.50 and r10 < 0.20:
        return "quick_partial_at_0.5R", f"reach 0.5R {r05*100:.1f}%, conversion at 1R only {c10*100:.1f}%"
    if r03 > 0.60 and r10 < 0.15:
        return "scalp_quick_at_0.3R", f"reach 0.3R {r03*100:.1f}%, only {r10*100:.1f}% reach 1R"
    if gave_back > 0.40:
        return "earlier_BE_at_0.5R", f"gave_back_green {gave_back*100:.1f}%, mfe_median {m['mfe_median']:.2f}R"
    return "needs_investigation", f"r03={r03*100:.1f}% r05={r05*100:.1f}% r10={r10*100:.1f}% wr={wr*100:.1f}% gb={gave_back*100:.1f}%"


# === Coarse: strategy × pair_family × direction ===
print("=== COARSE GRAIN (strategy × pair_family × direction) ===")
rows = []
for keys, g in df.groupby(["strategy", "pair_family", "direction"]):
    m = cell_metrics(g)
    rec, basis = derive_recommendation(m)
    rec_row = {"strategy": keys[0], "pair_family": keys[1], "direction": keys[2],
               "recommendation": rec, "basis": basis}
    rec_row.update(m)
    rows.append(rec_row)
coarse_df = pd.DataFrame(rows)
print(f"cells: {len(coarse_df)}")
print(coarse_df["recommendation"].value_counts().to_string())
print()

# === Mid: + session_bucket ===
print("=== MID GRAIN (+ session_bucket) ===")
mid_rows = []
for keys, g in df.groupby(["strategy", "pair_family", "direction", "session_bucket"]):
    m = cell_metrics(g)
    rec, basis = derive_recommendation(m)
    rec_row = {"strategy": keys[0], "pair_family": keys[1], "direction": keys[2],
               "session_bucket": keys[3], "recommendation": rec, "basis": basis}
    rec_row.update(m)
    mid_rows.append(rec_row)
mid_df = pd.DataFrame(mid_rows)
print(f"cells: {len(mid_df)}")
print(mid_df["recommendation"].value_counts().to_string())
print()

coarse_df.to_csv(OUT / "atlas_coarse.csv", index=False)
mid_df.to_csv(OUT / "atlas_mid.csv", index=False)


# Print answers to Brock's questions
print("\n=== BROCK'S QUESTION 1: which cells should move to BE earlier? ===")
be = mid_df[mid_df["recommendation"].str.contains("earlier_BE", na=False)].sort_values("n_trades", ascending=False).head(15)
print(be[["strategy","pair_family","direction","session_bucket","n_trades","reached_0.5R_pct","giveback_at_0.5R_pct","mfe_median","basis"]].to_string(index=False))

print("\n=== BROCK'S QUESTION 2: which cells should take quick partials / scalp? ===")
qp = mid_df[mid_df["recommendation"].str.contains("quick_partial|scalp", na=False, regex=True)].sort_values("n_trades", ascending=False).head(15)
print(qp[["strategy","pair_family","direction","session_bucket","n_trades","reached_0.3R_pct","reached_1.0R_pct","basis"]].to_string(index=False))

print("\n=== BROCK'S QUESTION 3: which cells should be SCALP-ONLY? ===")
scalp = mid_df[mid_df["recommendation"] == "scalp_quick_at_0.3R"][
    ["strategy","pair_family","direction","session_bucket","n_trades","reached_0.3R_pct","reached_1.0R_pct","basis"]
].sort_values("n_trades", ascending=False)
print(scalp.to_string(index=False))

print("\n=== BROCK'S QUESTION 4: which cells should be SKIPPED? ===")
skip = mid_df[mid_df["recommendation"] == "skip_cell"][
    ["strategy","pair_family","direction","session_bucket","n_trades","reached_0.3R_pct","clean_stop_pct","basis"]
].sort_values("n_trades", ascending=False)
print(skip.head(15).to_string(index=False))

print("\n=== BROCK'S QUESTION 5: which cells can hold for 1R / 2R? ===")
hold = mid_df[mid_df["recommendation"].str.contains("hold_for", na=False, regex=True)][
    ["strategy","pair_family","direction","session_bucket","n_trades","reached_1.0R_pct","reached_2.0R_pct","conv_1.0R","conv_2.0R","basis"]
].sort_values("n_trades", ascending=False)
print(hold.to_string(index=False))

print("\n=== BROCK'S QUESTION 6: does asia/direct/USD-antipodean need different exit than london/USD-base? ===")
key_pockets = mid_df[
    ((mid_df["session_bucket"] == "asia") & (mid_df["strategy"] == "direct") & (mid_df["pair_family"].isin(["usd_base","antipodean_cross"])))
    |
    ((mid_df["session_bucket"] == "london") & (mid_df["pair_family"] == "usd_base"))
][["strategy","pair_family","direction","session_bucket","n_trades","recommendation",
   "mfe_median","reached_0.5R_pct","reached_1.0R_pct","reached_2.0R_pct","gave_back_pct","basis"]]
print(key_pockets.to_string(index=False))

print(f"\nsaved {OUT}")
