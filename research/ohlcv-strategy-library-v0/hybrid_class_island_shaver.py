#!/usr/bin/env python3
"""
hybrid_class_island_shaver.py — production-grade island miner

Hybrid of:
  - fast_targeted_winner_island_shaver.py  (band grammar, beam search, era split,
                                            multiple islands per parent, false-friend
                                            sibling bank, per-parent factor priors
                                            from test3_inside_regime_splits.csv)
  - mine_class_islands.py                  (symmetric winner/loser class mining,
                                            6yr vs 6mo window comparison)

Runs FOUR passes in one invocation, sharing the corpus load:
    target = {win, loss}  x  window = {6yr, 6mo}

Per parent cell (from test3_inside_regime_splits.csv, 293 cells):
  - prior factors = top1/top2/top3 separator factors + session_bucket
  - beam search up to depth-4 over band rules built from 13 quantile breakpoints
  - bucket each candidate as winner_island/loser_island, false_friend_sibling, or rejected
  - cap MAX_PARENT_FRAC=0.40  (no island can be >40% of parent — forces tightness)
  - cap MAX_FALSE_FRIENDS_PER_PARENT=8

Bucketing (symmetric by target_class):
  target=win:
    winner_island        : wins >= 10 AND (losses <= 2 OR wr >= 0.75)
    false_friend_sibling : wins >= 10 AND (wr > parent_wr OR mean_R > parent_mean_R)
  target=loss:
    loser_island         : losses >= 10 AND (wins <= 2 OR loss_rate >= 0.75)
    false_friend_sibling : losses >= 10 AND (loss_rate > parent_loss_rate OR mean_R < parent_mean_R)

Outputs:
    hybrid_winner_islands_6yr.csv  +  hybrid_false_friends_winner_6yr.csv  + .md
    hybrid_winner_islands_6mo.csv  +  hybrid_false_friends_winner_6mo.csv  + .md
    hybrid_loser_islands_6yr.csv   +  hybrid_false_friends_loser_6yr.csv   + .md
    hybrid_loser_islands_6mo.csv   +  hybrid_false_friends_loser_6mo.csv   + .md
    hybrid_islands_summary.md
"""
from __future__ import annotations
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path('/Users/brock-mini-mac/scrooge-research')
TRADE_LOG = BASE / 'all_strategies_all_pairs_trades.parquet'
TEST3 = BASE / 'test3_inside_regime_splits.csv'
OUTDIR = BASE / 'seed-family-factory'
OUTDIR.mkdir(parents=True, exist_ok=True)

PARENT_KEYS = ['strategy_id', 'pair', 'direction', 'technical_regime_53']
BASE_FACTORS = ['ATR_ratio', 'ADX14', 'BB_compress', 'RSI14', 'price_pos', 'volume_ratio', 'hour_utc']
CAT_FACTORS = ['session_bucket']
ALL_FACTORS = BASE_FACTORS + CAT_FACTORS

# bucketing thresholds (symmetric by target)
MIN_TARGET = 10           # min wins (target=win) or min losses (target=loss)
MAX_OTHER  = 2            # max losses (target=win) or max wins (target=loss)
MIN_TARGET_RATE = 0.75    # min wr (target=win) or min loss_rate (target=loss)

MAX_DEPTH = 4
MAX_PARENT_FRAC = 0.40
MAX_FALSE_FRIENDS_PER_PARENT = 8
RULE_RE = re.compile(r'^([\w_]+)\s*(<=|>=|<|>|=|==)\s*(.+?)\s*$')

WINDOW_DAYS = {'6yr': None, '6mo': 180}


def frame_to_markdown(df):
    cols = list(df.columns)
    lines = ['| ' + ' | '.join(cols) + ' |', '| ' + ' | '.join(['---'] * len(cols)) + ' |']
    for _, row in df.iterrows():
        vals = []
        for c in cols:
            v = row[c]
            if pd.isna(v): s = ''
            elif isinstance(v, float): s = f'{v:.6g}'
            else: s = str(v)
            vals.append(s.replace('|', '\\|').replace('\n', ' '))
        lines.append('| ' + ' | '.join(vals) + ' |')
    return '\n'.join(lines)


def parse_rule_parts(rule: str):
    parts = []
    if not isinstance(rule, str) or not rule.strip(): return parts
    for raw_part in rule.split(' AND '):
        part = raw_part.strip()
        m = RULE_RE.match(part)
        if not m: continue
        field, op, raw_value = m.groups()
        field = field.strip()
        op = '==' if op == '=' else op
        raw_value = raw_value.strip()
        if field in CAT_FACTORS:
            value = raw_value
        else:
            try: value = float(raw_value)
            except ValueError: continue
        parts.append((field, op, value))
    return parts


def parse_rule_mask(df, rule):
    mask = pd.Series(True, index=df.index)
    for field, op, value in parse_rule_parts(rule):
        if field not in df.columns:
            return pd.Series(False, index=df.index)
        if field in CAT_FACTORS:
            col = df[field].astype(str)
            if op in ('==','='):
                mask &= col.eq(str(value))
            else:
                return pd.Series(False, index=df.index)
            continue
        col = df[field].astype(float)
        if op == '<=':   mask &= col.le(float(value))
        elif op == '>=': mask &= col.ge(float(value))
        elif op == '<':  mask &= col.lt(float(value))
        elif op == '>':  mask &= col.gt(float(value))
        elif op in ('==','='): mask &= col.eq(float(value))
    return mask.fillna(False)


def factor_signature(rule: str) -> str:
    seen = []
    for factor in ALL_FACTORS:
        if factor in rule and factor not in seen:
            seen.append(factor)
    return ' + '.join(seen)


def make_rules(df, factors):
    rules = []
    for factor in factors:
        if factor == 'session_bucket':
            for val in sorted(df[factor].dropna().astype(str).unique()):
                rules.append((factor, '==', val, val, f'{factor}=={val}'))
            continue
        if factor not in df or df[factor].notna().sum() < 20: continue
        vals = df[factor].dropna().astype(float)
        if vals.nunique() < 5: continue
        qs = sorted(set(float(x) for x in np.nanquantile(vals, [0.05,0.10,0.15,0.20,0.25,0.33,0.50,0.67,0.75,0.80,0.85,0.90,0.95])))
        for q in qs[1:-1]:
            rules.append((factor,'<=',None,q,f'{factor}<={q:.6g}'))
            rules.append((factor,'>=',q,None,f'{factor}>={q:.6g}'))
        for lo, hi in zip(qs[:-2], qs[2:]):
            rules.append((factor,'between',lo,hi,f'{factor}>={lo:.6g} AND {factor}<={hi:.6g}'))
    return rules


def apply_rule(df, rule):
    field, op, lo, hi, _label = rule
    if op == '==':
        return df[field].astype(str).eq(str(lo))
    vals = df[field].astype(float)
    if op == '<=':  return vals.le(float(hi)).fillna(False)
    if op == '>=':  return vals.ge(float(lo)).fillna(False)
    return (vals.ge(float(lo)) & vals.le(float(hi))).fillna(False)


def metrics(parent, mask):
    sub = parent[mask]
    n = len(sub)
    if n == 0 or n > len(parent) * MAX_PARENT_FRAC:
        return None
    wins = int(sub.is_win.sum())
    losses = n - wins
    if min(wins, losses) < 0:  # impossible
        return None
    if wins < 3 and losses < 3:
        return None
    disc = sub[sub.era.eq('discovery')] if 'era' in sub.columns else sub.iloc[0:0]
    hold = sub[sub.era.eq('holdout')] if 'era' in sub.columns else sub.iloc[0:0]
    return dict(
        n=n, wins=wins, losses=losses,
        wr=wins/n, loss_rate=losses/n,
        mean_R=float(sub.realized_R.mean()),
        sum_R=float(sub.realized_R.sum()),
        disc_n=len(disc), disc_wins=int(disc.is_win.sum()) if len(disc) else 0,
        disc_losses=int((~disc.is_win).sum()) if len(disc) else 0,
        disc_wr=float(disc.is_win.mean()) if len(disc) else 0.0,
        hold_n=len(hold), hold_wins=int(hold.is_win.sum()) if len(hold) else 0,
        hold_losses=int((~hold.is_win).sum()) if len(hold) else 0,
        hold_wr=float(hold.is_win.mean()) if len(hold) else 0.0,
    )


def classify_candidate(target: str, parent_wr: float, parent_mean_r: float, m: dict):
    if target == 'win':
        if m['wins'] >= MIN_TARGET and (m['losses'] <= MAX_OTHER or m['wr'] >= MIN_TARGET_RATE):
            return 'winner_island', ''
        if m['wins'] >= MIN_TARGET and (m['wr'] > parent_wr or m['mean_R'] > parent_mean_r):
            return 'false_friend_sibling', 'improved_vs_parent_but_failed_purity'
        return None, ''
    else:  # loss
        parent_loss_rate = 1.0 - parent_wr
        if m['losses'] >= MIN_TARGET and (m['wins'] <= MAX_OTHER or m['loss_rate'] >= MIN_TARGET_RATE):
            return 'loser_island', ''
        if m['losses'] >= MIN_TARGET and (m['loss_rate'] > parent_loss_rate or m['mean_R'] < parent_mean_r):
            return 'false_friend_sibling', 'improved_vs_parent_but_failed_purity'
        return None, ''


def run_pass(corpus_full: pd.DataFrame, parents: pd.DataFrame, target: str, window_label: str, t0: float):
    days = WINDOW_DAYS[window_label]
    if days is None:
        corpus = corpus_full
    else:
        cutoff = corpus_full['entry_ts'].max() - pd.Timedelta(days=days)
        corpus = corpus_full[corpus_full['entry_ts'] >= cutoff]
    print(f'[pass target={target} window={window_label}] corpus rows={len(corpus):,}  ({time.time()-t0:.1f}s)')

    work = corpus.merge(parents[PARENT_KEYS], on=PARENT_KEYS, how='inner')
    by_parent = dict(tuple(work.groupby(PARENT_KEYS, sort=False, dropna=False)))

    island_rows = []
    ff_rows = []

    for i, prow in parents.iterrows():
        key = tuple(prow[k] for k in PARENT_KEYS)
        parent = by_parent.get(key)
        if parent is None or len(parent) < (MIN_TARGET + MAX_OTHER + 5):
            continue

        parent_n = len(parent)
        parent_w = int(parent.is_win.sum())
        parent_l = parent_n - parent_w
        parent_wr = parent_w / parent_n
        parent_mean_r = float(parent.realized_R.mean())

        # Need enough of the target class to even hope for an island.
        target_count_parent = parent_w if target == 'win' else parent_l
        if target_count_parent < MIN_TARGET:
            continue

        # Per-parent factor priors (top1/top2/top3 separators) + session_bucket
        factors = []
        for f in [prow.top1_factor, prow.top2_factor, prow.top3_factor, 'session_bucket']:
            if isinstance(f, str) and f and f not in factors and f in ALL_FACTORS:
                factors.append(f)

        seed_masks = [('', pd.Series(True, index=parent.index))]
        try:
            seed_masks.append((str(prow.split_rule), parse_rule_mask(parent, str(prow.split_rule))))
        except Exception:
            pass

        island_candidates = []
        false_candidates = []

        for seed_label, seed_mask in seed_masks:
            states = [(seed_label, seed_mask, set())]
            for _depth in range(1, MAX_DEPTH + 1):
                next_states = []
                for label, mask, used in states:
                    sub = parent[mask]
                    if len(sub) < MIN_TARGET:
                        continue
                    for rule in make_rules(sub, [f for f in factors if f not in used]):
                        rmask = mask & apply_rule(parent, rule)
                        m = metrics(parent, rmask)
                        if not m: continue
                        rlabel = (label + ' AND ' if label else '') + rule[4]
                        next_states.append((rlabel, rmask, used | {rule[0]}, m))
                        ctype, reason = classify_candidate(target, parent_wr, parent_mean_r, m)
                        if ctype in ('winner_island','loser_island'):
                            island_candidates.append((rlabel, m, reason))
                        elif ctype == 'false_friend_sibling':
                            false_candidates.append((rlabel, m, reason))
                # Sort beam by target metric, then volume
                if target == 'win':
                    next_states.sort(key=lambda x: (x[3]['wr'], x[3]['wins'], x[3]['mean_R']), reverse=True)
                else:
                    next_states.sort(key=lambda x: (x[3]['loss_rate'], x[3]['losses'], -x[3]['mean_R']), reverse=True)
                states = [(a,b,c) for a,b,c,d in next_states[:30]]
                if not states: break

        # Dedupe + emit per parent
        seen = set()
        for label, m, reason in island_candidates:
            if label in seen: continue
            seen.add(label)
            row = {k: v for k,v in zip(PARENT_KEYS, key)}
            row.update(dict(
                target_class=target, window=window_label,
                pair_family=str(parent.pair_family.iloc[0]) if 'pair_family' in parent.columns else '',
                technical_regime_desc=str(parent.technical_regime_desc.iloc[0]) if 'technical_regime_desc' in parent.columns else '',
                parent_n=parent_n, parent_wins=parent_w, parent_losses=parent_l,
                parent_wr=parent_wr, parent_mean_R=parent_mean_r,
                top1_factor=prow.top1_factor, top2_factor=prow.top2_factor, top3_factor=prow.top3_factor,
                factor_signature=factor_signature(label),
                rule=label, depth=label.count(' AND ') + 1,
                wr_lift=(m['wr'] - parent_wr) if target=='win' else (m['loss_rate'] - (1-parent_wr)),
                **m
            ))
            island_rows.append(row)

        seen = set()
        parent_ff = []
        for label, m, reason in false_candidates:
            if label in seen: continue
            seen.add(label)
            row = {k: v for k,v in zip(PARENT_KEYS, key)}
            row.update(dict(
                target_class=target, window=window_label,
                pair_family=str(parent.pair_family.iloc[0]) if 'pair_family' in parent.columns else '',
                technical_regime_desc=str(parent.technical_regime_desc.iloc[0]) if 'technical_regime_desc' in parent.columns else '',
                parent_n=parent_n, parent_wins=parent_w, parent_losses=parent_l,
                parent_wr=parent_wr, parent_mean_R=parent_mean_r,
                top1_factor=prow.top1_factor, top2_factor=prow.top2_factor, top3_factor=prow.top3_factor,
                factor_signature=factor_signature(label),
                rule=label, depth=label.count(' AND ') + 1,
                wr_lift=(m['wr'] - parent_wr) if target=='win' else (m['loss_rate'] - (1-parent_wr)),
                false_friend_reason=reason,
                **m
            ))
            parent_ff.append(row)
        if target == 'win':
            parent_ff.sort(key=lambda r: (r['wr'], r['wins'], r['mean_R']), reverse=True)
        else:
            parent_ff.sort(key=lambda r: (r['loss_rate'], r['losses'], -r['mean_R']), reverse=True)
        ff_rows.extend(parent_ff[:MAX_FALSE_FRIENDS_PER_PARENT])

        if (i+1) % 50 == 0:
            print(f'  [{target}/{window_label}] {i+1}/{len(parents)}  islands={len(island_rows)}  ff={len(ff_rows)}  ({time.time()-t0:.1f}s)')

    return island_rows, ff_rows


def main():
    t0 = time.time()
    print(f'[load] {TEST3}')
    parents = pd.read_csv(TEST3).rename(columns={'regime':'technical_regime_53'})
    parents = parents[PARENT_KEYS + ['top1_factor','top2_factor','top3_factor','split_rule','cell_winners','cell_losers','cell_wr']].drop_duplicates().reset_index(drop=True)
    print(f'  parent cells: {len(parents)}')

    print(f'[load] {TRADE_LOG}')
    cols = sorted(set(PARENT_KEYS + ['pair_family','technical_regime_desc','entry_ts','era','is_win','realized_R'] + ALL_FACTORS))
    corpus = pd.read_parquet(TRADE_LOG, columns=cols)
    corpus['is_win'] = corpus['is_win'].astype(bool)
    print(f'  corpus rows: {len(corpus):,}  ({time.time()-t0:.1f}s)')

    summary_blocks = []
    for window_label in ['6yr','6mo']:
        for target in ['win','loss']:
            island_rows, ff_rows = run_pass(corpus, parents, target, window_label, t0)
            isl = pd.DataFrame(island_rows)
            ff  = pd.DataFrame(ff_rows)
            if not isl.empty:
                isl = isl.drop_duplicates(subset=PARENT_KEYS + ['rule'])
                # ranking: lowest other-class first, highest target rate, highest target count, holdout cleanliness, mean_R
                if target == 'win':
                    isl = isl.sort_values(['losses','wr','wins','hold_wr','mean_R'], ascending=[True,False,False,False,False])
                else:
                    isl = isl.sort_values(['wins','loss_rate','losses','hold_losses','mean_R'], ascending=[True,False,False,False,True])
            if not ff.empty:
                ff = ff.drop_duplicates(subset=PARENT_KEYS + ['rule'])
                if target == 'win':
                    ff = ff.sort_values(['wr','wins','mean_R','losses'], ascending=[False,False,False,True])
                else:
                    ff = ff.sort_values(['loss_rate','losses','mean_R','wins'], ascending=[False,False,True,True])
            target_label = 'winner' if target=='win' else 'loser'
            isl_path = OUTDIR / f'hybrid_{target_label}_islands_{window_label}.csv'
            ff_path  = OUTDIR / f'hybrid_false_friends_{target_label}_{window_label}.csv'
            isl.to_csv(isl_path, index=False)
            ff.to_csv(ff_path, index=False)
            print(f'  -> {isl_path.name}  ({len(isl)} islands, {len(ff)} false-friends)')
            summary_blocks.append((target_label, window_label, isl, ff))

    # Summary md ------------------------------------------------------------
    md = ['# Hybrid class-island shaver — summary','']
    md.append(f'**Generated:** {pd.Timestamp.utcnow().isoformat()}')
    md.append(f'**Engine:** band grammar + beam(top-30) up to depth-4 + per-parent factor priors + MAX_PARENT_FRAC=0.40')
    md.append('')
    md.append('## Counts per (target, window)')
    md.append('')
    md.append('| target | window | islands | false-friends |')
    md.append('|---|---|---:|---:|')
    for t,w,isl,ff in summary_blocks:
        md.append(f'| {t} | {w} | {len(isl):,} | {len(ff):,} |')
    md.append('')

    # Cell-level cross views
    def cells(df): return set(map(tuple, df[PARENT_KEYS].values.tolist())) if not df.empty else set()
    by_key = {(t,w): cells(isl) for t,w,isl,_ in summary_blocks}
    md.append('## Cell overlap winners vs losers')
    md.append('')
    for w in ('6yr','6mo'):
        wk = by_key.get(('winner',w), set())
        lk = by_key.get(('loser',w), set())
        md.append(f'- **{w}**: both = {len(wk & lk)} | winner-only = {len(wk - lk)} | loser-only = {len(lk - wk)}')
    md.append('')
    md.append('## Cell persistence 6yr vs 6mo')
    md.append('')
    for t in ('winner','loser'):
        k6y = by_key.get((t,'6yr'), set())
        k6m = by_key.get((t,'6mo'), set())
        md.append(f'- **{t}**: durable (both windows) = {len(k6y & k6m)} | only 6yr = {len(k6y - k6m)} | only 6mo = {len(k6m - k6y)}')
    md.append('')

    md.append('## Top 15 per pass (by target rate then count)')
    md.append('')
    for t,w,isl,_ in summary_blocks:
        md.append(f'### {t} / {w}')
        md.append('')
        if isl.empty:
            md.append('_(no islands)_'); md.append(''); continue
        cols = ['strategy_id','pair','direction','technical_regime_53','parent_n','parent_wr','n','wins','losses',
                ('wr' if t=='winner' else 'loss_rate'),'mean_R','hold_wins','hold_losses','depth','rule']
        top = isl.head(15)[cols].copy()
        md.append(frame_to_markdown(top))
        md.append('')

    (OUTDIR/'hybrid_islands_summary.md').write_text('\n'.join(md))
    print(f'[write] {OUTDIR/"hybrid_islands_summary.md"}')
    print(f'Total elapsed: {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
