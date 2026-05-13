"""Add session_quarter + finer time axes to trade-film ledger, recluster.

New axes:
  session_bucket: asia / london / overlap / ny_pm / rollover (NEW: rollover)
  session_quarter: <bucket>_q{1-4} (NEW)
  hour_utc: int 0-23
  minute_of_day: int 0-1439
  weekday: Mon..Sun
  day_of_week_session: e.g., 'Mon_asia', 'Fri_ny_pm'
  local_market_phase: open/mid/late within bucket (matches q1/q2-3/q4)

Recluster grain:
  strategy × pair_family × session_bucket × session_quarter × direction
  + sample-size warnings (n < 3, n < 5, n < 10)
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/winner-clusters-v0")


def session_bucket(hour):
    if pd.isna(hour): return None
    h = int(hour) % 24
    if 22 <= h: return "asia"          # 22-23 (Sydney late, pre-Tokyo)
    if h < 6:   return "asia"          # 00-05 (Tokyo open through late Asia)
    if h < 12:  return "london"        # 06-11
    if h < 16:  return "overlap"       # 12-15 (London-NY overlap)
    if h < 21:  return "ny_pm"         # 16-20
    return "rollover"                  # 21


def session_quarter(hour, minute):
    """Quarter within the session bucket. Each bucket subdivided into 4 equal parts."""
    if pd.isna(hour) or pd.isna(minute):
        return None
    h = int(hour) % 24
    m = int(minute) % 60
    minute_of_day = h * 60 + m

    bucket = session_bucket(hour)
    if bucket is None:
        return None

    # Bucket time ranges (in minutes from 00:00 UTC)
    if bucket == "asia":
        # 22:00 -> 06:00 = 22*60..30*60 = wraps around midnight
        # normalize so that within-bucket minute starts at 22:00
        if h >= 22:
            within = (h - 22) * 60 + m
        else:
            within = (h + 2) * 60 + m  # h+2 because 00 is at +2hr from start
        bucket_minutes = 8 * 60  # 8-hour bucket
    elif bucket == "london":
        within = (h - 6) * 60 + m
        bucket_minutes = 6 * 60  # 06-12 = 6 hours
    elif bucket == "overlap":
        within = (h - 12) * 60 + m
        bucket_minutes = 4 * 60  # 12-16 = 4 hours
    elif bucket == "ny_pm":
        within = (h - 16) * 60 + m
        bucket_minutes = 5 * 60  # 16-21 = 5 hours
    elif bucket == "rollover":
        within = (h - 21) * 60 + m
        bucket_minutes = 60  # single hour, just q1 if subdividing
    else:
        return None

    q = min(4, max(1, int(within / bucket_minutes * 4) + 1))
    return f"{bucket}_q{q}"


def local_market_phase(quarter):
    """open / mid / late based on quarter."""
    if quarter is None or not isinstance(quarter, str) or pd.isna(quarter):
        return None
    q = quarter.split("_")[-1]
    return {"q1": "open", "q2": "early-mid", "q3": "late-mid", "q4": "late"}.get(q, None)


# === Load ledger ===
df = pd.read_parquet(LEDGER)
print(f"ledger: {len(df)} rows, {len(df.columns)} cols")

# Need datetime entry_ts
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True, errors="coerce")
print(f"entry_ts non-null: {df['entry_ts'].notna().sum()}/{len(df)}")

# Derive new columns
df["hour_utc"] = df["entry_ts"].dt.hour
df["minute_of_day"] = df["entry_ts"].dt.hour * 60 + df["entry_ts"].dt.minute
df["weekday"] = df["entry_ts"].dt.day_name().str[:3]  # Mon, Tue, ...
df["session_bucket"] = df["hour_utc"].apply(session_bucket)
df["session_quarter"] = df.apply(lambda r: session_quarter(r["hour_utc"], r["entry_ts"].minute if pd.notna(r["entry_ts"]) else None), axis=1)
df["local_market_phase"] = df["session_quarter"].apply(local_market_phase)
df["day_of_week_session"] = df["weekday"].fillna("?") + "_" + df["session_bucket"].fillna("?")

print(f"\nsession_bucket distribution:")
print(df["session_bucket"].value_counts().to_string())
print(f"\nsession_quarter distribution (top 20):")
print(df["session_quarter"].value_counts().head(20).to_string())

# Recluster
df["_strategy"] = df["bot_actual_strategy"].fillna(df["strategy_label"]).fillna("unknown")
winners = df[df["repair_taxonomy"] == "actual_winner"].copy()
print(f"\nactual winners: {len(winners)}")

# Two grains: bucket-level (broad) and quarter-level (fine)
def build_clusters(grain_keys, label):
    clusters = []
    for keys, grp in winners.groupby(grain_keys):
        if any(pd.isna(k) for k in (keys if isinstance(keys, tuple) else (keys,))):
            continue
        cluster_id = "_".join(str(k)[:6] if isinstance(k, str) else str(k) for k in (keys if isinstance(keys, tuple) else (keys,)))
        realized = pd.to_numeric(grp["actual_realized_r"], errors="coerce")
        mfe = pd.to_numeric(grp["actual_mfe_r"], errors="coerce")
        src = grp["source_label"].value_counts()
        n = len(grp)
        if n < 5:
            warn = "n<5_unstable"
        elif n < 10:
            warn = "n<10_noisy"
        else:
            warn = None
        row = {"grain": label, "cluster_id": cluster_id, "n_winners": int(n),
               "n_broker": int(src.get("bot_actual_winner", 0)),
               "n_human": int(src.get("manual_human", 0)),
               "n_ai_curated": int(src.get("manual_ai_curated", 0)),
               "median_realized_r": float(realized.median()) if realized.notna().any() else None,
               "median_mfe_r": float(mfe.median()) if mfe.notna().any() else None,
               "pairs": ",".join(sorted(grp["pair"].unique().tolist())),
               "size_warning": warn}
        if isinstance(keys, tuple):
            for k_name, k_val in zip(grain_keys, keys):
                row[k_name] = k_val
        else:
            row[grain_keys[0]] = keys
        clusters.append(row)
    return pd.DataFrame(clusters)


# Coarse: strategy × pair_family × session_bucket × direction
coarse = build_clusters(
    ["_strategy", "pair_family", "session_bucket", "direction"], "coarse"
)
coarse.to_csv(OUT / "clusters_coarse_v2.csv", index=False)
print(f"\ncoarse clusters: {len(coarse)} cells")

# Fine: strategy × pair_family × session_bucket × session_quarter × direction
fine = build_clusters(
    ["_strategy", "pair_family", "session_bucket", "session_quarter", "direction"], "fine"
)
fine.to_csv(OUT / "clusters_fine_v2.csv", index=False)
print(f"fine clusters: {len(fine)} cells")

# Sample-size diagnostics
print(f"\nSize warning distribution at fine grain:")
print(fine["size_warning"].value_counts(dropna=False).to_string())

# Top fine-grain clusters
print(f"\nTop 20 fine-grain clusters by n_winners:")
print(fine.sort_values("n_winners", ascending=False).head(20)[
    ["cluster_id","_strategy","pair_family","session_bucket","session_quarter","direction",
     "n_winners","n_broker","n_human","n_ai_curated","median_realized_r","median_mfe_r","size_warning"]
].to_string(index=False))

# Update ledger with new columns (drop the scratch _strategy col)
df = df.drop(columns=["_strategy"])
for c in df.columns:
    if df[c].dtype == "object":
        df[c] = df[c].astype(str).replace({"nan": None, "None": None, "<NA>": None})
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"\nsaved ledger: {len(df)} rows, {len(df.columns)} cols")
