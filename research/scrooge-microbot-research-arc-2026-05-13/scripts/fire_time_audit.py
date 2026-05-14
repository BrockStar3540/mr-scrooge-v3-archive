"""When do the 4 survivor bots fire? Audit hour/weekday distribution."""
import pandas as pd
import numpy as np
import re
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
IN = ROOT / "strategy-library-v1"

SURVIVORS = [
    {"strategy": "TF6_short", "pair": "USD_JPY",
     "rule": "spread_cost_R>0.004112 AND weekday>1.5 AND bb_width_rank<=0.9983 AND ema50_dist<=-0.004768"},
    {"strategy": "MR4_long",  "pair": "CHF_JPY", "rule": "vol_ratio<=0.2397 AND vol_ratio<=0.08077"},
    {"strategy": "MR4_long",  "pair": "EUR_JPY", "rule": "vol_ratio<=0.7493 AND vol_ratio<=0.0781"},
    {"strategy": "MR4_long",  "pair": "AUD_JPY", "rule": "vol_ratio<=0.3576 AND rsi14<=35.09"},
]

def parse_rule(rule_text):
    parts = re.split(r"\s+AND\s+", rule_text)
    out = []
    for p in parts:
        m = re.match(r"^([\w_]+)(<=|>=|<|>|=)(-?[\d.eE+]+)$", p.strip())
        if m: out.append((m.group(1), m.group(2), float(m.group(3))))
    return out

def apply_rule(df, rule):
    m = pd.Series(True, index=df.index)
    for f, op, thr in rule:
        if op == "<=": m &= (df[f] <= thr)
        elif op == ">=": m &= (df[f] >= thr)
        elif op == "<":  m &= (df[f] <  thr)
        elif op == ">":  m &= (df[f] >  thr)
    return m

for surv in SURVIVORS:
    strat = surv["strategy"]; pair = surv["pair"]
    trades = pd.read_parquet(IN / f"trades_{pair}.parquet")
    trades["entry_ts"] = pd.to_datetime(trades["entry_ts"], utc=True)
    trades = trades[(trades["hour_utc"] < 21) | (trades["hour_utc"] >= 22)].copy()
    sub = trades[trades.strategy == strat]
    sub = sub[apply_rule(sub, parse_rule(surv["rule"]))]
    print(f"\n=== {strat} / {pair} — {len(sub)} fires ===")
    print(f"  win_rate = {(sub['realized_R']>0).mean():.1%}  mean_R = {sub['realized_R'].mean():+.3f}")
    print("  hour_utc distribution:")
    h = sub["hour_utc"].value_counts().sort_index()
    total = len(sub)
    for hr, n in h.items():
        bar = "█" * int(40 * n / total)
        print(f"    {int(hr):2d}h  {n:5d}  {n/total:5.1%}  {bar}")
    print(f"  weekday distribution: {sub['weekday'].value_counts().sort_index().to_dict()}")
    # Win rate by hour
    print("  win_rate by hour (>=5 fires):")
    wr = sub.groupby("hour_utc").agg(n=("realized_R","size"), mr=("realized_R","mean"),
                                      wr=("realized_R", lambda x: (x>0).mean())).reset_index()
    for _, r in wr[wr.n >= 5].iterrows():
        print(f"    {int(r['hour_utc']):2d}h  n={int(r['n']):4d}  mR={r['mr']:+.2f}  wr={r['wr']:.1%}")
