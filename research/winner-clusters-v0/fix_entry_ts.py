"""Re-parse broker entry_ts properly and rebuild ledger."""
import pandas as pd
import numpy as np
from pathlib import Path

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
df = pd.read_parquet(LEDGER)
print(f"loaded: {len(df)} rows")

# Read broker source and parse the nanosecond Zulu format
br = pd.read_csv("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/audits/live_broker_reverse_engineering.csv")
# Truncate nanoseconds to microseconds for safe parsing
br["entry_ts_clean"] = br["entry_ts"].str.replace(r"(\d{6})\d*Z$", r"\1Z", regex=True)
br["entry_ts_parsed"] = pd.to_datetime(br["entry_ts_clean"], utc=True, errors="coerce")
print(f"broker parsed: {br['entry_ts_parsed'].notna().sum()}/{len(br)}")

# Build lookup by trade_id (which is source_row_key for broker rows)
lookup = dict(zip(br["trade_id"].astype(str), br["entry_ts_parsed"]))

mask_broker = df["source_label"].str.startswith("bot_") & df["entry_ts"].isna()
print(f"broker rows with NaT entry_ts before: {mask_broker.sum()}")

def lookup_ts(key):
    return lookup.get(str(key))

df.loc[mask_broker, "entry_ts"] = df.loc[mask_broker, "source_row_key"].apply(lookup_ts)
print(f"after fix: {df['entry_ts'].notna().sum()}/{len(df)} entry_ts populated")

df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print("saved")
