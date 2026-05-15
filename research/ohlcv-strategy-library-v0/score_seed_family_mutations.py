#!/usr/bin/env python3
"""
score_seed_family_mutations.py

Step 2 of the seed-family factory.

Reads seed_family_mutations.csv (children) and the raw trade ledger, applies
each child rule to its parent cell, computes:

  losers_removed     = (parent_losses - child_losses) / max(1, parent_losses)
  winners_retained   = child_wins / max(1, parent_wins)
  purity_gain        = child_wr - parent_wr
  seed_survival_score = max(0, purity_gain) * sqrt(max(0, child_wins-10)) / (1 + child_losses)

Bucketing (deterministic eligibility, not from score):
  winner_seed          : wins>=10 AND (losses<=2 OR wr>=0.75)
  near_pure_seed       : wins>=8  AND wr>=0.65 AND wr > parent_wr + 0.15
  false_friend_sibling : wins>=5  AND wr > parent_wr + 0.10 AND failed gates above
  child_reject         : everything else

Writes seven artifacts:
  seed_family_lineage.csv
  seed_family_children_winners.csv / .md
  seed_family_children_false_friends.csv
  seed_family_children_rejects.csv
  seed_family_children_loser_contrast_bank.csv / .md
"""
from __future__ import annotations

import math
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
PARQUET   = ROOT / 'all_strategies_all_pairs_trades.parquet'
MUTATIONS = ROOT / 'seed-family-factory' / 'seed_family_mutations.csv'
SEED_BANK = ROOT / 'winner_island_sibling_seed_bank.csv'
OUT_DIR   = ROOT / 'seed-family-factory'
OUT_DIR.mkdir(parents=True, exist_ok=True)

# parser ---------------------------------------------------------------------
_NUM = re.compile(r'^(ATR_ratio|RSI14|BB_compress|price_pos|volume_ratio|ADX14|hour_utc)\s*(<=|>=|<|>|==)\s*(-?[0-9.eE+-]+)$')
_SES = re.compile(r'^session_bucket\s*==\s*([A-Za-z_]+)$')

def parse_rule(rule: str):
    out = []
    if not isinstance(rule, str): return out
    for raw in rule.split(' AND '):
        c = raw.strip()
        m = _NUM.match(c)
        if m:
            out.append(('num', m.group(1), m.group(2), float(m.group(3)))); continue
        m = _SES.match(c)
        if m:
            out.append(('ses','session_bucket','==', m.group(1))); continue
        out.append(('unk', None, None, c))
    return out

def apply_rule(df: pd.DataFrame, clauses) -> pd.Series:
    mask = pd.Series(True, index=df.index)
    for kind, feat, op, val in clauses:
        if kind == 'unk':
            return pd.Series(False, index=df.index)
        if feat not in df.columns:
            return pd.Series(False, index=df.index)
        s = df[feat]
        if op == '<=':  mask &= (s <= val)
        elif op == '>=': mask &= (s >= val)
        elif op == '<':  mask &= (s <  val)
        elif op == '>':  mask &= (s >  val)
        elif op == '==': mask &= (s == val)
        else: return pd.Series(False, index=df.index)
    return mask

# scoring --------------------------------------------------------------------
def score_child(n_p, w_p, l_p, n_c, w_c, l_c):
    losers_removed   = max(0, l_p - l_c) / max(1, l_p)
    winners_retained = w_c / max(1, w_p)
    wr_p = w_p / max(1, n_p)
    wr_c = w_c / max(1, n_c) if n_c else 0.0
    purity_gain = wr_c - wr_p
    survival = max(0.0, purity_gain) * math.sqrt(max(0, w_c - 10)) / (1 + l_c)
    return wr_p, wr_c, losers_removed, winners_retained, purity_gain, survival

def bucket_child(w_c, l_c, wr_c, parent_wr):
    if w_c >= 10 and (l_c <= 2 or wr_c >= 0.75):
        return 'winner_seed'
    if w_c >= 8 and wr_c >= 0.65 and wr_c > parent_wr + 0.15:
        return 'near_pure_seed'
    if w_c >= 5 and wr_c > parent_wr + 0.10:
        return 'false_friend_sibling'
    return 'child_reject'

# main -----------------------------------------------------------------------
def main():
    t0 = time.time()
    print(f'[load] mutations: {MUTATIONS}')
    mut = pd.read_csv(MUTATIONS)
    print(f'  children: {len(mut)}')

    print(f'[load] seed bank: {SEED_BANK}')
    seeds = pd.read_csv(SEED_BANK)
    seeds = seeds.reset_index(drop=True)
    seeds['parent_seed_id'] = [f's{i+1:04d}' for i in seeds.index]
    # parent cell stats by (strategy_id, pair, direction, regime)
    key_cols = ['strategy_id','pair','direction','technical_regime_53']
    seeds_by_key = seeds.set_index(key_cols)

    print(f'[load] corpus: {PARQUET}')
    cols = ['pair','strategy_id','direction','technical_regime_53','technical_regime_desc',
            'session_bucket','hour_utc','ATR_ratio','RSI14','BB_compress','price_pos',
            'volume_ratio','ADX14','is_win','realized_R','mfe_R','mae_R','entry_ts']
    corpus = pq.read_table(PARQUET, columns=cols).to_pandas()
    print(f'  corpus rows: {len(corpus):,}  ({time.time()-t0:.1f}s)')

    # Group corpus once
    corpus_grp = corpus.groupby(key_cols, sort=False)
    print(f'  parent cells: {corpus_grp.ngroups}  ({time.time()-t0:.1f}s)')

    lineage_rows = []
    winner_rows  = []
    ff_rows      = []
    reject_rows  = []
    loser_bank   = []

    # Iterate by parent_seed_id so we process all children of one seed together
    mut_by_parent = mut.groupby('parent_seed_id', sort=False)

    for parent_seed_id, mchildren in mut_by_parent:
        first = mchildren.iloc[0]
        key = (first['strategy_id'], first['pair'], first['direction'], first['technical_regime_53'])
        try:
            parent_df = corpus_grp.get_group(key)
        except KeyError:
            continue
        if len(parent_df) == 0:
            continue

        # parent stats
        n_p = len(parent_df)
        w_p = int(parent_df['is_win'].sum())
        l_p = n_p - w_p
        if n_p == 0: continue
        wr_p = w_p / n_p

        parent_losers = parent_df[~parent_df['is_win']]

        # also pull seed-row stats if present
        seed_row = seeds_by_key.loc[key] if key in seeds_by_key.index else None
        seed_rule = first['base_rule']
        seed_clauses = parse_rule(seed_rule)

        # write 'parent' bucket loser entries ONCE per parent_seed (linked via parent_seed_id)
        for _, lr in parent_losers.iterrows():
            loser_bank.append(_loser_row(
                seed_id=parent_seed_id, parent_seed_id=parent_seed_id, bucket='parent',
                matched_rule=seed_rule, row=lr,
            ))

        for _, ch in mchildren.iterrows():
            clauses = parse_rule(str(ch['child_rule']))
            mask = apply_rule(parent_df, clauses)
            sub = parent_df[mask]
            n_c = len(sub)
            if n_c == 0:
                # degenerate child -- log as reject with explicit reason
                lineage_rows.append(_lineage_row(ch, n=0, w=0, l=0, wr=0.0,
                                                 mean_R=0.0, hold_w=0, hold_l=0,
                                                 bucket='child_reject', degenerate=True,
                                                 losers_removed=1.0, winners_retained=0.0,
                                                 purity_gain=-wr_p, survival=0.0))
                continue
            w_c = int(sub['is_win'].sum())
            l_c = n_c - w_c
            wr_p, wr_c, lr_pct, wr_ret, pg, surv = score_child(n_p, w_p, l_p, n_c, w_c, l_c)
            mean_R = float(sub['realized_R'].mean())
            # holdout = last 20% by entry_ts within this parent's child subset
            sub_sorted = sub.sort_values('entry_ts')
            n_hold = max(1, int(len(sub_sorted) * 0.2))
            hold = sub_sorted.tail(n_hold)
            hold_w = int(hold['is_win'].sum()); hold_l = len(hold) - hold_w
            bucket = bucket_child(w_c, l_c, wr_c, wr_p)

            lineage_rows.append(_lineage_row(ch, n=n_c, w=w_c, l=l_c, wr=wr_c,
                                             mean_R=mean_R, hold_w=hold_w, hold_l=hold_l,
                                             bucket=bucket, losers_removed=lr_pct,
                                             winners_retained=wr_ret, purity_gain=pg,
                                             survival=surv))

            base_kw = dict(
                seed_id=ch['seed_id'], parent_seed_id=parent_seed_id,
                root_strategy_id=ch['root_strategy_id'], strategy_id=ch['strategy_id'],
                pair=ch['pair'], direction=ch['direction'],
                technical_regime_53=ch['technical_regime_53'],
                generation=int(ch['generation']), mutation_type=ch['mutation_type'],
                child_rule=ch['child_rule'], factor_signature=ch['factor_signature'],
                n=n_c, wins=w_c, losses=l_c, wr=round(wr_c,4),
                mean_R=round(mean_R,4), hold_wins=hold_w, hold_losses=hold_l,
                losers_removed=round(lr_pct,4), winners_retained=round(wr_ret,4),
                purity_gain=round(pg,4), seed_survival_score=round(surv,4),
                parent_n=n_p, parent_wins=w_p, parent_losses=l_p, parent_wr=round(wr_p,4),
            )

            if bucket == 'winner_seed':
                winner_rows.append(base_kw)
                # row-level loser bank: rejected_by_shave + residual
                _write_loser_buckets(loser_bank, ch, parent_seed_id, parent_losers, mask, bucket)
            elif bucket == 'false_friend_sibling':
                ff_rows.append(base_kw)
                _write_loser_buckets(loser_bank, ch, parent_seed_id, parent_losers, mask, bucket)
            elif bucket == 'near_pure_seed':
                winner_rows.append(base_kw)   # treat near-pure as in the winner-side artifact set
                _write_loser_buckets(loser_bank, ch, parent_seed_id, parent_losers, mask, bucket)
            else:
                reject_rows.append(base_kw)
                # do not explode loser rows for rejects -- count-only

        if (mut_by_parent.indices.__len__() and
            int(list(mut_by_parent.groups.keys()).index(parent_seed_id)) % 20 == 0):
            print(f'  ...processed {parent_seed_id}  elapsed {time.time()-t0:.1f}s')

    # build dataframes -------------------------------------------------------
    lineage = pd.DataFrame(lineage_rows)
    winners = pd.DataFrame(winner_rows)
    ff      = pd.DataFrame(ff_rows)
    rejects = pd.DataFrame(reject_rows)
    losers  = pd.DataFrame(loser_bank)

    # ranking inside winner artifact
    if len(winners):
        winners = winners.sort_values(
            ['seed_survival_score','losses','wr','wins','hold_wins','mean_R'],
            ascending=[False, True, False, False, False, False]
        ).reset_index(drop=True)
        winners.insert(0, 'rank', winners.index + 1)

    if len(ff):
        ff = ff.sort_values(['purity_gain','wr','wins'], ascending=[False,False,False]).reset_index(drop=True)
    if len(rejects):
        rejects = rejects.sort_values('parent_seed_id').reset_index(drop=True)

    # write artifacts --------------------------------------------------------
    p_lineage = OUT_DIR/'seed_family_lineage.csv'
    p_winners = OUT_DIR/'seed_family_children_winners.csv'
    p_winners_md = OUT_DIR/'seed_family_children_winners.md'
    p_ff      = OUT_DIR/'seed_family_children_false_friends.csv'
    p_rej     = OUT_DIR/'seed_family_children_rejects.csv'
    p_losers  = OUT_DIR/'seed_family_children_loser_contrast_bank.csv'
    p_losers_md = OUT_DIR/'seed_family_children_loser_contrast_bank.md'

    lineage.to_csv(p_lineage, index=False)
    winners.to_csv(p_winners, index=False)
    ff.to_csv(p_ff, index=False)
    rejects.to_csv(p_rej, index=False)
    losers.to_csv(p_losers, index=False)

    # winners summary md
    md = ['# seed_family_children_winners','']
    md.append(f'**Built:** {pd.Timestamp.utcnow().isoformat()}')
    md.append(f'**Source mutations:** {len(mut)} children of {seeds.shape[0]} parent seeds')
    md.append(f'**Winner-side rows (winner_seed + near_pure_seed):** {len(winners)}')
    md.append('')
    if len(winners):
        md.append('## Bucket breakdown')
        md.append('')
        # join bucket from lineage on seed_id
        wb = winners.merge(lineage[['seed_id','bucket']], on='seed_id', how='left')
        for b, sub in wb.groupby('bucket'):
            md.append(f'- **{b}**: {len(sub)}')
        md.append('')
        md.append('## Top 25 by seed_survival_score')
        md.append('')
        cols = ['rank','seed_id','strategy_id','pair','direction','technical_regime_53',
                'mutation_type','n','wins','losses','wr','mean_R','hold_wins','hold_losses',
                'purity_gain','seed_survival_score']
        head = winners[cols].head(25)
        md.append(head.to_markdown(index=False))
    p_winners_md.write_text('\n'.join(md))

    # loser bank summary md
    md = ['# seed_family_children_loser_contrast_bank','']
    md.append(f'**Built:** {pd.Timestamp.utcnow().isoformat()}')
    md.append(f'**Row count:** {len(losers)}')
    md.append('')
    if len(losers):
        md.append('## Bucket counts')
        md.append('')
        for b, sub in losers.groupby('bucket'):
            md.append(f'- **{b}**: {len(sub)}')
        md.append('')
        md.append('## Top loser-heavy parent cells (rejected_by_shave + residual)')
        md.append('')
        kb = losers[losers['bucket'].isin(['rejected_by_shave','residual'])]
        if len(kb):
            kp = kb.groupby(['strategy_id','pair','direction','technical_regime_53']).size().sort_values(ascending=False).head(15)
            md.append('| strategy | pair | dir | regime | rows |')
            md.append('|---|---|---|---|---:|')
            for (s,p,d,r), n in kp.items():
                md.append(f'| {s} | {p} | {d} | {r} | {n} |')
    p_losers_md.write_text('\n'.join(md))

    print()
    print('='*60)
    print(f'lineage:           {len(lineage):>6}  -> {p_lineage}')
    print(f'winners (+near):   {len(winners):>6}  -> {p_winners}')
    print(f'false_friends:     {len(ff):>6}  -> {p_ff}')
    print(f'rejects:           {len(rejects):>6}  -> {p_rej}')
    print(f'losers (rows):     {len(losers):>6}  -> {p_losers}')
    print()
    print('Bucket breakdown:')
    if len(lineage):
        print(lineage['bucket'].value_counts().to_string())
    print(f'Total elapsed: {time.time()-t0:.1f}s')

def _lineage_row(ch, n, w, l, wr, mean_R, hold_w, hold_l, bucket,
                 losers_removed, winners_retained, purity_gain, survival, degenerate=False):
    return {
        'seed_id':              ch['seed_id'],
        'parent_seed_id':       ch['parent_seed_id'],
        'root_strategy_id':     ch['root_strategy_id'],
        'strategy_id':          ch['strategy_id'],
        'pair':                 ch['pair'],
        'direction':            ch['direction'],
        'technical_regime_53':  ch['technical_regime_53'],
        'generation':           int(ch['generation']),
        'mutation_type':        ch['mutation_type'],
        'base_rule':            ch['base_rule'],
        'child_rule':           ch['child_rule'],
        'factor_signature':     ch['factor_signature'],
        'bucket':               bucket,
        'n':                    n,
        'wins':                 w,
        'losses':               l,
        'wr':                   round(wr,4),
        'mean_R':               round(mean_R,4),
        'hold_wins':            hold_w,
        'hold_losses':          hold_l,
        'losers_removed':       round(losers_removed,4),
        'winners_retained':     round(winners_retained,4),
        'purity_gain':          round(purity_gain,4),
        'seed_survival_score':  round(survival,4),
        'degenerate':           degenerate,
    }

def _loser_row(seed_id, parent_seed_id, bucket, matched_rule, row):
    return {
        'seed_id':              seed_id,
        'parent_seed_id':       parent_seed_id,
        'bucket':               bucket,
        'matched_rule':         matched_rule,
        'entry_ts':             row.get('entry_ts'),
        'strategy_id':          row.get('strategy_id'),
        'pair':                 row.get('pair'),
        'direction':            row.get('direction'),
        'technical_regime_53':  row.get('technical_regime_53'),
        'realized_R':           row.get('realized_R'),
        'mfe_R':                row.get('mfe_R'),
        'mae_R':                row.get('mae_R'),
        'ATR_ratio':            row.get('ATR_ratio'),
        'ADX14':                row.get('ADX14'),
        'BB_compress':          row.get('BB_compress'),
        'RSI14':                row.get('RSI14'),
        'price_pos':            row.get('price_pos'),
        'volume_ratio':         row.get('volume_ratio'),
        'session_bucket':       row.get('session_bucket'),
        'hour_utc':             row.get('hour_utc'),
    }

def _write_loser_buckets(loser_bank, ch, parent_seed_id, parent_losers, mask, bucket_name):
    """For a kept child, emit per-loser rows for rejected_by_shave + residual buckets."""
    matched_idx = mask.index[mask]
    rejected = parent_losers[~parent_losers.index.isin(matched_idx)]
    residual = parent_losers[parent_losers.index.isin(matched_idx)]
    for _, lr in rejected.iterrows():
        loser_bank.append(_loser_row(
            seed_id=ch['seed_id'], parent_seed_id=parent_seed_id, bucket='rejected_by_shave',
            matched_rule=ch['child_rule'], row=lr))
    bucket_for_residual = 'false_friend_sibling' if bucket_name == 'false_friend_sibling' else 'residual'
    for _, lr in residual.iterrows():
        loser_bank.append(_loser_row(
            seed_id=ch['seed_id'], parent_seed_id=parent_seed_id, bucket=bucket_for_residual,
            matched_rule=ch['child_rule'], row=lr))

if __name__ == '__main__':
    main()
