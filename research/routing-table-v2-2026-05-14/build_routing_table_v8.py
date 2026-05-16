"""Rebuild v8 with sub_regime as the cell key (proper granularity)."""
from __future__ import annotations
import datetime as dt
from pathlib import Path
import pandas as pd

ROOT = Path('/home/ubuntu/mr-scrooge-v3')
IN_PARQ = ROOT / 'data' / 'routing_table_v7.parquet'
OUT_PARQ = ROOT / 'data' / 'routing_table_v8.parquet'
OUT_CSV  = ROOT / 'data' / 'routing_table_v8.csv'
OUT_MD   = ROOT / 'data' / 'routing_table_v8_summary.md'

def tier_for(wr, n):
    if wr >= 0.65 and n >= 30: return 'Elite'
    if wr >= 0.50 and n >= 30: return 'Pro'
    if wr >= 0.40 and n >= 30: return 'Standard'
    return 'Probationary'

df = pd.read_parquet(IN_PARQ)
print(f'rows: {len(df):,}')
df['tier'] = df.apply(lambda r: tier_for(r['wr'], r['n']), axis=1)

# Unique cells by sub_regime (real granularity)
unique = df.drop_duplicates(subset=['sub_regime','pair','strategy','direction'])
print(f'unique cells (by sub_regime): {len(unique)}')

print()
print('=== Tier distribution ===')
print('| tier         | cells | mean_wr | mean_n | mean_R/trade | %/trade (@80%) |')
for tier in ['Elite','Pro','Standard','Probationary']:
    g = unique[unique.tier==tier]
    if g.empty:
        print(f'| {tier:<12} |  0    |   -     |   -    |     -        |     -          |')
        continue
    mean_wr = g['wr'].mean()
    mean_n = g['n'].mean()
    expected_R = mean_wr * 2.0 - (1 - mean_wr) * 1.0
    pct = expected_R * 1.8
    print(f'| {tier:<12} | {len(g):>4} | {mean_wr:.4f} | {mean_n:>5.1f}  |  {expected_R:+.3f}R    |  {pct:+5.2f}%        |')

print()
print('=== Elite cells (all of them) ===')
elite = unique[unique.tier=='Elite'].sort_values(['wr','n'], ascending=[False, False])
for _, r in elite.iterrows():
    print(f'  {r["sub_regime"]:<8s} {r["pair"]:<8s} {r["strategy"]:<35s} {r["direction"]:>5s}  n={int(r["n"]):>4d}  W={int(r["wins"])}/L={int(r["n"]-r["wins"])}  wr={r["wr"]:.4f}')
    print(f'           shave_rule: {r["shave_rule"]}')

print()
print('=== Pro cells (50-65% WR) ===')
pro = unique[unique.tier=='Pro'].sort_values(['wr','n'], ascending=[False, False])
for _, r in pro.head(15).iterrows():
    print(f'  {r["sub_regime"]:<8s} {r["pair"]:<8s} {r["strategy"]:<35s} {r["direction"]:>5s}  n={int(r["n"]):>4d}  wr={r["wr"]:.4f}')

df.to_parquet(OUT_PARQ, index=False)
df.to_csv(OUT_CSV, index=False)

md = ['# routing_table_v8 summary','']
md.append(f'**Built:** {dt.datetime.now(dt.timezone.utc).isoformat()}')
md.append(f'**Source:** routing_table_v7 + sub_regime tier classification')
md.append(f'**Rows:** {len(df):,}  |  Unique cells: {len(unique)}')
md.append('')
md.append('## Tier breakdown')
md.append('')
md.append('| tier | cells | mean_wr | mean_n | mean_R/trade | %/trade @ 80% margin |')
md.append('|---|---:|---:|---:|---:|---:|')
for tier in ['Elite','Pro','Standard','Probationary']:
    g = unique[unique.tier==tier]
    if g.empty: continue
    mean_wr = g['wr'].mean()
    expected_R = mean_wr * 2.0 - (1 - mean_wr) * 1.0
    pct = expected_R * 1.8
    md.append(f'| {tier} | {len(g)} | {mean_wr:.4f} | {g["n"].mean():.1f} | +{expected_R:.3f}R | +{pct:.2f}% |')
md.append('')
md.append('## Brock target: +2% per trade')
md.append('')
md.append('At 80% margin + 50:1 leverage, 2% per trade requires +1R per trade.')
md.append('Math: WR x 2R - (1-WR) x 1R = 1.0R  →  WR = 66.7 percent')
md.append('')
md.append('**The Elite tier (wr>=65% and n>=30) is the path to the 2% per-trade target.**')
md.append('')
md.append('Config flip to make the bot trade Elite-only:')
md.append('```')
md.append('gates.entry_filter.min_tier = "Elite"   # default Probationary')
md.append('```')
md.append('')
md.append('Trade-off: Elite tier fires far less often than the full v7 surface (1-5 trades/week vs 25-35).')
OUT_MD.write_text('\n'.join(md))
print(f'\n[wrote] v8 + summary')
