"""Block 3 — miner v3 gen-1: recursive cell division with survival test (2026-06-10).
Base key (align,pair,strategy,direction) -> greedy best-factor splits (depth<=2).
Select on TRAIN (<=2024-06), survive on OOS TEST (>=2025-07). Read-only analysis."""
import pandas as pd, numpy as np
import pyarrow.parquet as pq

F14 = ['BB','BBP','A5','A1','RSI','E20','E50','ZS','SPR','ADR','H20','H60','T1','T4']
LIVE = {'AUD_USD','EUR_USD','GBP_USD','USD_CAD'}
NEED = F14 + ['pair','strategy','direction','entry_time','net_ladder','alignv']
df = pq.read_table('/home/ubuntu/scored_7yr.parquet', columns=NEED).to_pandas(categories=F14+['pair','strategy','direction'])
df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
df = df[df.pair.isin(LIVE)]
df['era'] = np.where(df.entry_time < pd.Timestamp('2024-07-01', tz='UTC'), 'tr',
             np.where(df.entry_time >= pd.Timestamp('2025-07-01', tz='UTC'), 'te', 'mid'))
df = df[df.era != 'mid']
print(f"rows={len(df)}", flush=True)

MIN_TR, MIN_TE = 200, 75
WIN_T, LOSE_T = 1.25, -0.5
out = []

def classify(tr_m, te_m):
    if tr_m >= WIN_T and te_m >= WIN_T: return 'WINNER'
    if tr_m <= LOSE_T and te_m <= LOSE_T: return 'LOSER'
    return 'MARGINAL'

def mine(node, path, used, depth, base_id):
    ntr, nte = node[node.era=='tr'], node[node.era=='te']
    if len(ntr) < MIN_TR or len(nte) < MIN_TE: return
    tr_m, te_m = ntr.net_ladder.mean(), nte.net_ladder.mean()
    verdict = classify(tr_m, te_m)
    out.append(dict(base=base_id, lineage=path or '(root)', depth=depth,
        n_tr=len(ntr), n_te=len(nte), ev_tr=round(tr_m,2), ev_te=round(te_m,2),
        wr_te=round(100*(nte.net_ladder>0).mean(),1),
        tot_te=round(nte.net_ladder.sum()), verdict=verdict))
    if depth >= 2 or verdict != 'MARGINAL': return
    best_f, best_sep = None, 0.0
    for f in F14:
        if f in used: continue
        g = ntr.groupby(f, observed=True).net_ladder.agg(['size','mean'])
        g = g[g['size'] >= MIN_TR]
        if len(g) < 2: continue
        sep = (g['size'] * (g['mean'] - tr_m).abs()).sum() / max(g['size'].sum(),1)
        if sep > best_sep: best_sep, best_f = sep, f
    if best_f is None: return
    for lvl in node[best_f].dropna().unique():
        child = node[node[best_f] == lvl]
        mine(child, f"{path}>{best_f}={lvl}" if path else f"{best_f}={lvl}",
             used | {best_f}, depth+1, base_id)

bases = df.groupby(['alignv','pair','strategy','direction'], observed=True)
n_base = 0
for (al, pair, strat, d), g in bases:
    if len(g) < MIN_TR + MIN_TE: continue
    n_base += 1
    mine(g, '', set(), 0, f"a{al}|{pair}|{strat}|{d}")
res = pd.DataFrame(out)
res.to_csv('/home/ubuntu/mr-scrooge-v3/data/lab_training/miner_v3_gen1.csv', index=False)
w = res[(res.verdict=='WINNER') & (res.depth>0)]
l = res[(res.verdict=='LOSER') & (res.depth>0)]
print(f"bases mined: {n_base}  nodes: {len(res)}", flush=True)
print(f"NEW winner children: {len(w)} (OOS total {w.tot_te.sum():+,.0f}p)", flush=True)
print(f"NEW loser children:  {len(l)} (OOS total {l.tot_te.sum():+,.0f}p avoidable)", flush=True)
print("\nTOP 15 winner children by OOS total:", flush=True)
print(w.sort_values('tot_te', ascending=False).head(15).to_string(index=False), flush=True)
print("\nTOP 15 loser children by OOS pips avoidable:", flush=True)
print(l.sort_values('tot_te').head(15).to_string(index=False), flush=True)
