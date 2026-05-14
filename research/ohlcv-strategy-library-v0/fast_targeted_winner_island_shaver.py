from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd

BASE = Path('/Users/brock-mini-mac/scrooge-research')
TRADE_LOG = BASE / 'all_strategies_all_pairs_trades.parquet'
TEST3 = BASE / 'test3_inside_regime_splits.csv'
OUTDIR = BASE / 'winner-islands'
OUTDIR.mkdir(parents=True, exist_ok=True)

PARENT_KEYS = ['strategy_id', 'pair', 'direction', 'technical_regime_53']
BASE_FACTORS = ['ATR_ratio', 'ADX14', 'BB_compress', 'RSI14', 'price_pos', 'volume_ratio', 'hour_utc']
CAT_FACTORS = ['session_bucket']
MIN_WINS = 10
MAX_LOSSES = 2
MIN_WR = 0.75
MAX_DEPTH = 4
MAX_PARENT_FRAC = 0.40


def parse_rule_mask(df, rule):
    mask = pd.Series(True, index=df.index)
    if not isinstance(rule, str) or not rule:
        return mask
    for part in rule.split(' AND '):
        part = part.strip()
        if '<=' in part:
            f, v = part.split('<=', 1)
            mask &= df[f.strip()].astype(float).le(float(v))
        elif '>' in part:
            f, v = part.split('>', 1)
            mask &= df[f.strip()].astype(float).gt(float(v))
    return mask.fillna(False)


def make_rules(df, factors):
    rules = []
    for factor in factors:
        if factor == 'session_bucket':
            for val in sorted(df[factor].dropna().astype(str).unique()):
                rules.append((factor, '==', val, val, f'{factor}=={val}'))
            continue
        if factor not in df or df[factor].notna().sum() < 20:
            continue
        vals = df[factor].dropna().astype(float)
        if vals.nunique() < 5:
            continue
        qs = sorted(set(float(x) for x in np.nanquantile(vals, [0.05,0.10,0.15,0.20,0.25,0.33,0.50,0.67,0.75,0.80,0.85,0.90,0.95])))
        # Tails: most useful for shaving losers.
        for q in qs[1:-1]:
            rules.append((factor, '<=', None, q, f'{factor}<={q:.6g}'))
            rules.append((factor, '>=', q, None, f'{factor}>={q:.6g}'))
        # A few middle bands, because some islands are not tails.
        for lo, hi in zip(qs[:-2], qs[2:]):
            rules.append((factor, 'between', lo, hi, f'{factor}>={lo:.6g} AND {factor}<={hi:.6g}'))
    return rules


def apply_rule(df, rule):
    f, op, lo, hi, label = rule
    if op == '==':
        return df[f].astype(str).eq(str(lo))
    vals = df[f].astype(float)
    if op == '<=':
        return vals.le(float(hi)).fillna(False)
    if op == '>=':
        return vals.ge(float(lo)).fillna(False)
    return (vals.ge(float(lo)) & vals.le(float(hi))).fillna(False)


def metrics(parent, mask):
    sub = parent[mask]
    n = len(sub)
    if n == 0 or n > len(parent) * MAX_PARENT_FRAC:
        return None
    wins = int(sub.is_win.sum())
    losses = n - wins
    if wins < 3:
        return None
    disc = sub[sub.era.eq('discovery')]
    hold = sub[sub.era.eq('holdout')]
    return dict(
        n=n, wins=wins, losses=losses, wr=wins/n,
        mean_R=float(sub.realized_R.mean()), sum_R=float(sub.realized_R.sum()),
        disc_n=len(disc), disc_wins=int(disc.is_win.sum()) if len(disc) else 0,
        disc_losses=int((~disc.is_win).sum()) if len(disc) else 0,
        disc_wr=float(disc.is_win.mean()) if len(disc) else 0.0,
        hold_n=len(hold), hold_wins=int(hold.is_win.sum()) if len(hold) else 0,
        hold_losses=int((~hold.is_win).sum()) if len(hold) else 0,
        hold_wr=float(hold.is_win.mean()) if len(hold) else 0.0,
    )


def frame_to_markdown(df):
    try:
        return df.to_markdown(index=False)
    except ImportError:
        cols = list(df.columns)
        lines = ['| ' + ' | '.join(cols) + ' |', '| ' + ' | '.join(['---'] * len(cols)) + ' |']
        for _, row in df.iterrows():
            vals = []
            for c in cols:
                v = row[c]
                if pd.isna(v):
                    s = ''
                elif isinstance(v, float):
                    s = f'{v:.6g}'
                else:
                    s = str(v)
                vals.append(s.replace('|', '\\|').replace('\n', ' '))
            lines.append('| ' + ' | '.join(vals) + ' |')
        return '\n'.join(lines)


def main():
    t3 = pd.read_csv(TEST3).rename(columns={'regime':'technical_regime_53'})
    parents = t3[PARENT_KEYS + ['top1_factor','top2_factor','top3_factor','split_rule','cell_winners','cell_losers','cell_wr']].drop_duplicates()
    cols = sorted(set(PARENT_KEYS + ['pair_family','technical_regime_desc','entry_ts','era','is_win','realized_R','session_bucket'] + BASE_FACTORS))
    df = pd.read_parquet(TRADE_LOG, columns=cols)
    df['is_win'] = df.is_win.astype(bool)
    work = df.merge(parents[PARENT_KEYS], on=PARENT_KEYS, how='inner')
    print(f'parents={len(parents)} rows={len(work):,}', flush=True)
    rows=[]
    by_parent = dict(tuple(work.groupby(PARENT_KEYS, sort=False, dropna=False)))
    for i, prow in parents.iterrows():
        key = tuple(prow[k] for k in PARENT_KEYS)
        parent = by_parent.get(key)
        if parent is None or len(parent) == 0:
            continue
        if (i+1) % 50 == 0:
            print(f'processed {i+1}/{len(parents)} hits={len(rows)}', flush=True)
        parent_n=len(parent); parent_w=int(parent.is_win.sum()); parent_l=parent_n-parent_w; parent_wr=parent_w/parent_n
        factors=[]
        for f in [prow.top1_factor, prow.top2_factor, prow.top3_factor, 'session_bucket']:
            if isinstance(f,str) and f and f not in factors and (f in BASE_FACTORS or f=='session_bucket'):
                factors.append(f)
        # Seeds include the original test3 split and empty parent.
        seed_masks=[('', pd.Series(True,index=parent.index))]
        try:
            seed_masks.append((str(prow.split_rule), parse_rule_mask(parent, str(prow.split_rule))))
        except Exception:
            pass
        candidates=[]
        for seed_label, seed_mask in seed_masks:
            states=[(seed_label, seed_mask, set())]
            for depth in range(1, MAX_DEPTH+1):
                next_states=[]
                for label, mask, used in states:
                    sub=parent[mask]
                    if len(sub)<MIN_WINS:
                        continue
                    for rule in make_rules(sub, [f for f in factors if f not in used]):
                        rmask = mask & apply_rule(parent, rule)
                        m = metrics(parent, rmask)
                        if not m:
                            continue
                        rlabel = (label + ' AND ' if label else '') + rule[4]
                        next_states.append((rlabel, rmask, used | {rule[0]}, m))
                        if m['wins'] >= MIN_WINS and (m['losses'] <= MAX_LOSSES or m['wr'] >= MIN_WR):
                            candidates.append((rlabel, m))
                next_states.sort(key=lambda x:(x[3]['wr'], x[3]['wins'], x[3]['mean_R']), reverse=True)
                states=[(a,b,c) for a,b,c,d in next_states[:30]]
                if not states:
                    break
        seen=set()
        for label,m in candidates:
            if label in seen:
                continue
            seen.add(label)
            row={k:v for k,v in zip(PARENT_KEYS,key)}
            row.update(dict(pair_family=str(parent.pair_family.iloc[0]), technical_regime_desc=str(parent.technical_regime_desc.iloc[0]),
                            parent_n=parent_n,parent_wins=parent_w,parent_losses=parent_l,parent_wr=parent_wr,
                            top1_factor=prow.top1_factor,top2_factor=prow.top2_factor,top3_factor=prow.top3_factor,
                            rule=label, depth=label.count(' AND ')+1, wr_lift=m['wr']-parent_wr, **m))
            rows.append(row)
    out=pd.DataFrame(rows)
    if not out.empty:
        out=out.drop_duplicates(subset=PARENT_KEYS+['rule'])
        out=out.sort_values(['losses','wr','wins','hold_wr','mean_R'], ascending=[True,False,False,False,False])
    out.to_csv(OUTDIR/'fast_targeted_winner_islands.csv', index=False)
    lines=['# Fast Targeted Winner Islands\n']
    lines.append('Uses `test3_inside_regime_splits.csv` as the map of mixed mass regimes, then shaves only each parent cell\'s top separator factors plus session. This is micro-strategy discovery, not deployment validation.\n')
    lines.append(f'- Parent mixed cells: {len(parents):,}\n')
    lines.append(f'- Row-level trades searched: {len(work):,}\n')
    lines.append(f'- Candidate winner islands: {len(out):,}\n')
    if not out.empty:
        pure=out[(out.wins>=MIN_WINS)&(out.losses==0)]
        near=out[(out.wins>=MIN_WINS)&(out.wr>=MIN_WR)]
        hold_clean=out[(out.hold_wins>=3)&(out.hold_losses==0)]
        lines.append(f'- Pure islands (>=10 wins, 0 losses): {len(pure):,}\n')
        lines.append(f'- Near-pure islands (>=10 wins, WR>=75%): {len(near):,}\n')
        lines.append(f'- Holdout-clean islands (>=3 holdout wins, 0 losses): {len(hold_clean):,}\n')
        show=['strategy_id','pair','direction','technical_regime_53','parent_n','parent_wins','parent_losses','parent_wr','rule','n','wins','losses','wr','disc_wins','disc_losses','hold_wins','hold_losses','hold_wr','mean_R']
        lines.append('\n## Top Islands\n')
        lines.append(frame_to_markdown(out[show].head(80)))
    (OUTDIR/'summary_fast_targeted_winner_islands.md').write_text('\n'.join(lines))
    print(OUTDIR/'summary_fast_targeted_winner_islands.md')
    print(f'islands={len(out)}')

if __name__=='__main__':
    main()
