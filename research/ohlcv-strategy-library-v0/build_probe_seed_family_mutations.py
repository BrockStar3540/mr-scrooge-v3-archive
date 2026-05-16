#!/usr/bin/env python3
"""
build_seed_family_mutations.py

Step 1 of the seed-family factory.

For each row in winner_island_sibling_seed_bank.csv, parse the rule into typed
clauses (numeric bands + session_bucket membership), then emit child rules by
applying one mutation operator at a time. Generation 1 only on this pass.

Mutation operators (one factor at a time):
  1. widen_low     -- shift the lower bound of one numeric band down by one quantile step
  2. widen_high    -- shift the upper bound of one numeric band up by one quantile step
  3. narrow_low    -- shift the lower bound of one numeric band up by one quantile step
  4. narrow_high   -- shift the upper bound of one numeric band down by one quantile step
  5. shift_up      -- shift both bounds of one numeric band up by one quantile step
  6. shift_down    -- shift both bounds of one numeric band down by one quantile step
  7. add_filter    -- add one filter on an unused factor at median +/- 0.5 sigma
  8. remove_filter -- drop one existing filter
  9. swap_session  -- replace session_bucket clause with each other bucket (one child per swap)
 10. add_session   -- if no session clause, add session_bucket==X for each bucket

Quantile steps are computed per-(parent cell, factor) from the parent rows so
that 'one step' is meaningful in that pocket's local distribution.

Output: seed_family_mutations.csv with one row per CHILD candidate. Scoring is
the next stage (score_seed_family_mutations.py).

Schema is intentionally rule-only here -- evaluation happens in stage 2.
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
SEED_BANK = ROOT / 'seed-family-factory' / 'hybrid_probe_winner_islands_6yr_top1.csv'
PARQUET   = ROOT / 'seed-family-factory' / 'probe_corpus.parquet'
OUT_DIR   = ROOT / 'seed-family-factory'
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV   = OUT_DIR / 'probe_seed_family_mutations.csv'

ADD_FILTER_POOL = ['ATR_ratio','RSI14','BB_compress','price_pos','volume_ratio','ADX14','hour_utc']
SESSION_BUCKETS = ['asia','asia_late','london_open','ny_open','ny_mid','ny_close','off_hours','london']

# rule parser  ---------------------------------------------------------------
_NUM = re.compile(r'^(ATR_ratio|RSI14|BB_compress|price_pos|volume_ratio|ADX14|hour_utc)\s*(<=|>=|<|>|==)\s*(-?[0-9.eE+-]+)$')
_SES = re.compile(r'^session_bucket\s*==\s*([A-Za-z_]+)$')

def parse_rule(rule: str):
    clauses = []
    for raw in rule.split(' AND '):
        c = raw.strip()
        m = _NUM.match(c)
        if m:
            clauses.append({'kind':'num','feat':m.group(1),'op':m.group(2),'val':float(m.group(3))})
            continue
        m = _SES.match(c)
        if m:
            clauses.append({'kind':'ses','feat':'session_bucket','op':'==','val':m.group(1)})
            continue
        clauses.append({'kind':'unk','raw':c})
    return clauses

def render_rule(clauses) -> str:
    parts = []
    for c in clauses:
        if c['kind']=='num':
            parts.append(f"{c['feat']}{c['op']}{c['val']:.6g}")
        elif c['kind']=='ses':
            parts.append(f"session_bucket=={c['val']}")
        else:
            parts.append(c['raw'])
    return ' AND '.join(parts)

# quantile step helper -------------------------------------------------------
QSTEP = 0.05  # one quantile step = 5pp

def quantile_step(values: np.ndarray, target: float, direction: int) -> float:
    """Return the closest quantile value that is one QSTEP away from where 
    falls in the distribution. direction=+1 -> step up; -1 -> step down."""
    if len(values) < 20:
        return target
    sorted_vals = np.sort(values[np.isfinite(values)])
    if len(sorted_vals) < 20:
        return target
    # rank of target
    rank = float(np.searchsorted(sorted_vals, target)) / len(sorted_vals)
    rank_new = max(0.0, min(1.0, rank + direction * QSTEP))
    return float(np.quantile(sorted_vals, rank_new))

# loaders --------------------------------------------------------------------
def load_parent_rows(corpus_df: pd.DataFrame, seed: pd.Series) -> pd.DataFrame:
    mask = (
        (corpus_df['strategy_id']         == seed['strategy_id']) &
        (corpus_df['pair']                == seed['pair']) &
        (corpus_df['direction']           == seed['direction']) &
        (corpus_df['technical_regime_53'] == seed['technical_regime_53'])
    )
    return corpus_df[mask]

# mutators -------------------------------------------------------------------
def mutate_numeric(clauses, parent_df: pd.DataFrame) -> Iterable[tuple[str, list]]:
    for idx, c in enumerate(clauses):
        if c['kind'] != 'num':
            continue
        feat = c['feat']
        col_values = parent_df[feat].to_numpy() if feat in parent_df.columns else np.array([])
        if len(col_values) < 20:
            continue
        op  = c['op']; val = c['val']

        # widen
        if op in ('>=','>'):  # lower bound -> widen by stepping value down
            new_val = quantile_step(col_values, val, direction=-1)
            if new_val != val:
                yield 'widen_low', _replace_at(clauses, idx, val=new_val)
        if op in ('<=','<'):  # upper bound -> widen by stepping up
            new_val = quantile_step(col_values, val, direction=+1)
            if new_val != val:
                yield 'widen_high', _replace_at(clauses, idx, val=new_val)
        # narrow
        if op in ('>=','>'):
            new_val = quantile_step(col_values, val, direction=+1)
            if new_val != val:
                yield 'narrow_low', _replace_at(clauses, idx, val=new_val)
        if op in ('<=','<'):
            new_val = quantile_step(col_values, val, direction=-1)
            if new_val != val:
                yield 'narrow_high', _replace_at(clauses, idx, val=new_val)
        # shift up / down  -- only meaningful if this clause is paired with a complementary bound
        complementary = [(i,cc) for i,cc in enumerate(clauses)
                         if i != idx and cc.get('feat')==feat]
        if complementary:
            v_up_a = quantile_step(col_values, val, direction=+1)
            v_dn_a = quantile_step(col_values, val, direction=-1)
            if v_up_a != val:
                shifted = list(clauses)
                shifted[idx] = dict(c, val=v_up_a)
                for ci, cc in complementary:
                    shifted[ci] = dict(cc, val=quantile_step(col_values, cc['val'], direction=+1))
                yield 'shift_up', shifted
            if v_dn_a != val:
                shifted = list(clauses)
                shifted[idx] = dict(c, val=v_dn_a)
                for ci, cc in complementary:
                    shifted[ci] = dict(cc, val=quantile_step(col_values, cc['val'], direction=-1))
                yield 'shift_down', shifted

def mutate_add_filter(clauses, parent_df: pd.DataFrame):
    used = {c.get('feat') for c in clauses}
    for feat in ADD_FILTER_POOL:
        if feat in used or feat not in parent_df.columns:
            continue
        vals = parent_df[feat].to_numpy()
        finite = vals[np.isfinite(vals)]
        if len(finite) < 20:
            continue
        med = float(np.median(finite))
        # add two filters: feat >= median (favors high-half pocket), feat <= median (low-half)
        yield 'add_filter', clauses + [{'kind':'num','feat':feat,'op':'>=','val':med}]
        yield 'add_filter', clauses + [{'kind':'num','feat':feat,'op':'<=','val':med}]

def mutate_remove_filter(clauses):
    if len(clauses) <= 1:
        return
    for idx in range(len(clauses)):
        if clauses[idx]['kind'] == 'unk':
            continue
        kept = [c for i,c in enumerate(clauses) if i != idx]
        if kept:
            yield 'remove_filter', kept

def mutate_session(clauses, parent_df: pd.DataFrame):
    existing_sess = [i for i,c in enumerate(clauses) if c['kind']=='ses']
    if existing_sess:
        idx = existing_sess[0]
        cur = clauses[idx]['val']
        for b in SESSION_BUCKETS:
            if b == cur: continue
            yield 'swap_session', [dict(c) if i!=idx else dict(c,val=b) for i,c in enumerate(clauses)]
    else:
        for b in SESSION_BUCKETS:
            yield 'add_session', clauses + [{'kind':'ses','feat':'session_bucket','op':'==','val':b}]

def _replace_at(clauses, idx: int, **upd):
    out = [dict(c) for c in clauses]
    out[idx] = dict(out[idx], **upd)
    return out

# main -----------------------------------------------------------------------
def main():
    t0 = time.time()
    print(f'[load] seed bank: {SEED_BANK}')
    seeds = pd.read_csv(SEED_BANK)
    print(f'  seeds: {len(seeds)}')

    print(f'[load] corpus: {PARQUET}')
    needed = ['pair','strategy_id','direction','technical_regime_53','session_bucket',
              'hour_utc','ATR_ratio','RSI14','BB_compress','price_pos','volume_ratio','ADX14',
              'is_win','realized_R','entry_ts','technical_regime_desc']
    corpus = pq.read_table(PARQUET, columns=needed).to_pandas()
    print(f'  corpus rows: {len(corpus):,}  ({time.time()-t0:.1f}s)')

    out_rows = []
    next_id = 1
    for si, seed in seeds.iterrows():
        parent = load_parent_rows(corpus, seed)
        if len(parent) == 0:
            continue
        clauses = parse_rule(str(seed['rule']))
        seed_id = f's{si+1:04d}'   # parent seed id
        # all mutations -- one operator per child
        children = []
        children.extend(mutate_numeric(clauses, parent))
        children.extend(mutate_add_filter(clauses, parent))
        children.extend(mutate_remove_filter(clauses))
        children.extend(mutate_session(clauses, parent))

        for ci, (mut_type, child_clauses) in enumerate(children):
            child_rule = render_rule(child_clauses)
            if child_rule == render_rule(clauses):
                continue   # identity mutation -- skip
            child_id = f'{seed_id}_g1_c{ci+1:04d}'
            factor_sig = ' + '.join(sorted({c['feat'] for c in child_clauses if c.get('feat')}))
            out_rows.append({
                'seed_id':              child_id,
                'parent_seed_id':       seed_id,
                'root_strategy_id':     seed['strategy_id'],
                'strategy_id':          seed['strategy_id'],
                'pair':                 seed['pair'],
                'direction':            seed['direction'],
                'technical_regime_53':  seed['technical_regime_53'],
                'generation':           1,
                'mutation_type':        mut_type,
                'base_rule':            seed['rule'],
                'child_rule':           child_rule,
                'factor_signature':     factor_sig,
            })
            next_id += 1

        if (si+1) % 25 == 0:
            print(f'  [{si+1}/{len(seeds)}]  children so far: {len(out_rows)}  ({time.time()-t0:.1f}s)')

    df = pd.DataFrame(out_rows)
    df.to_csv(OUT_CSV, index=False)
    print(f'[write] {OUT_CSV}  ({len(df)} children, {time.time()-t0:.1f}s)')
    print()
    print('mutation_type counts:')
    print(df['mutation_type'].value_counts().to_string())

if __name__ == '__main__':
    main()
