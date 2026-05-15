#!/usr/bin/env python3
"""Temporal OOS validation of strong-edge islands (v2 — patched).

Strong-edge in-sample criterion: post_WR >= 0.30 AND n_kept >= 100  -> 261 islands.
Split: train < 2025-01-01 UTC, test >= 2025-01-01 UTC (~16 months holdout).

Two independent OOS tests per island:
  A) Rule replay     — parse in-sample rule, apply to TEST.
  B) Refit-on-train  — fit fresh depth-5 tree on TRAIN, pick best leaf, apply to TEST.

Patches over v1:
  - Derived feature  (green_count_4 if long else 4 - green_count_4).
  - Rule parser handles  membership clauses.
  - Tree min_samples_leaf bumped to 30 so MIN_TRAIN_KEEP is naturally satisfied.
  - Rules referencing  are flagged but B-refit still runs.
"""
from __future__ import annotations

import re, time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
CORPUS = ROOT / 'routing-table-v2' / 'ml_training_corpus.parquet'
ISLANDS = ROOT / 'routing-table-v2' / 'islands_best_overall.csv'
OUT_CSV = ROOT / 'routing-table-v2' / 'oos_validation_strong_islands.csv'
OUT_MD  = ROOT / 'routing-table-v2' / 'oos_validation_summary.md'

SPLIT_TS = pd.Timestamp('2025-01-01', tz='UTC')

STRONG_POST_WR = 0.30
STRONG_N_KEPT  = 100

MIN_TRAIN_N    = 200
MIN_TEST_N     = 50
MIN_LEAF       = 30   # tree leaf size AND replay test-kept threshold
MIN_TEST_KEEP  = 20

FEATURES = [
    'ATR14','ATR_ratio','BB_width','BB_compress','ADX14','EMA_slope','RSI14','close_pos',
    'z_score','bb_position','ema20_dist_pct','ema50_dist_pct','sma20_dist_signed_bps',
    'spread_pips','range_half','volume_ratio','adr_consumed','otr_ratio',
    'green_count_3','green_count_4','green_count_5',
    'directional_confirmation',   # derived
    'hour_utc','day_of_week',
]

SESSION_OF = {h: ('asia' if 0<=h<4 else 'asia_late' if 4<=h<6 else 'london_open' if 6<=h<9
                  else 'ny_open' if 9<=h<13 else 'ny_mid' if 13<=h<17 else 'ny_close' if 17<=h<21
                  else 'off_hours') for h in range(24)}

DOW_INT = {'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4,'Sat':5,'Sun':6}

_RULE_NUMERIC = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*(<=|>=|<|>|==|!=)\s*(-?[0-9.eE+-]+)$')
_RULE_DAYSET  = re.compile(r'^day\s+in\s+\{([A-Za-z,\s]+)\}$')

def parse_rule(rule_str: str):
    out = []
    for clause in rule_str.split(' AND '):
        c = clause.strip()
        m = _RULE_NUMERIC.match(c)
        if m:
            out.append((m.group(1), m.group(2), float(m.group(3))))
            continue
        m = _RULE_DAYSET.match(c)
        if m:
            names = [x.strip() for x in m.group(1).split(',')]
            ints  = set(DOW_INT[n] for n in names)
            out.append(('day_of_week','in', ints))
            continue
        raise ValueError(f'Bad clause: {c!r}')
    return out

def apply_rule(df: pd.DataFrame, clauses) -> pd.Series:
    mask = pd.Series(True, index=df.index)
    for col, op, val in clauses:
        if col not in df.columns:
            return pd.Series(False, index=df.index)
        s = df[col]
        if   op == '<=':  mask &= (s <= val)
        elif op == '>=':  mask &= (s >= val)
        elif op == '<':   mask &= (s <  val)
        elif op == '>':   mask &= (s >  val)
        elif op == '==':  mask &= (s == val)
        elif op == '!=':  mask &= (s != val)
        elif op == 'in':  mask &= s.isin(val)
        else: raise ValueError(op)
    return mask

def best_leaf_rule(tree: DecisionTreeClassifier, features: list[str], min_keep: int):
    t = tree.tree_
    class_idx = {c: i for i, c in enumerate(tree.classes_)}
    win_idx = class_idx.get(True, class_idx.get(1, None))
    if win_idx is None: return None
    best = None

    def walk(node: int, path: list):
        nonlocal best
        if t.children_left[node] == _tree.TREE_LEAF:
            # sklearn 1.6+ stores normalized probabilities in value; use n_node_samples for raw counts
            n_kept = int(t.n_node_samples[node])
            probs  = t.value[node][0]
            w_kept = int(round(float(probs[win_idx]) * n_kept))
            if n_kept >= min_keep and n_kept > 0:
                post_wr = w_kept / n_kept
                if best is None or post_wr > best[0] or (post_wr == best[0] and n_kept > best[1]):
                    best = (post_wr, n_kept, list(path), w_kept, n_kept - w_kept)
            return
        feat = features[t.feature[node]]
        thr  = float(t.threshold[node])
        walk(t.children_left[node],  path + [(feat, '<=', thr)])
        walk(t.children_right[node], path + [(feat,  '>', thr)])

    walk(0, [])
    if best is None: return None
    post_wr, n_kept, clauses, w_kept, l_kept = best
    return clauses, n_kept, w_kept, l_kept

def main():
    t0 = time.time()
    print('[load] islands_best_overall...')
    ib = pd.read_csv(ISLANDS)
    strong = ib[(ib['post_WR'] >= STRONG_POST_WR) & (ib['n_kept'] >= STRONG_N_KEPT)].reset_index(drop=True)
    print(f'  strong islands: {len(strong)}')

    print('[load] corpus parquet...')
    base = ['source','strategy_id','pair','direction','entry_ts','is_win','technical_regime_53','hour_utc','day_of_week']
    factor_cols = [f for f in FEATURES if f not in ('hour_utc','day_of_week','directional_confirmation')]
    corpus = pq.read_table(CORPUS, columns=base + factor_cols).to_pandas()
    print(f'  corpus rows: {len(corpus):,}  ({time.time()-t0:.1f}s)')

    corpus['session'] = corpus['hour_utc'].map(SESSION_OF)
    corpus['regime']  = corpus['technical_regime_53']
    # derived
    is_long = (corpus['direction'] == 'long').values
    g4 = corpus['green_count_4'].values
    corpus['directional_confirmation'] = np.where(is_long, g4, 4 - g4)

    key_cols = ['source','strategy_id','regime','pair','session','direction']
    grouped = corpus.groupby(key_cols, sort=False)
    print(f'  groups: {len(grouped):,}  ({time.time()-t0:.1f}s)')

    rows = []
    for i, isl in strong.iterrows():
        key = tuple(isl[c] for c in key_cols)
        try:
            df = grouped.get_group(key)
        except KeyError:
            rows.append({**isl.to_dict(), 'oos_status': 'no_corpus_match'}); continue

        df = df.dropna(subset=FEATURES)
        if len(df) == 0:
            rows.append({**isl.to_dict(), 'oos_status': 'all_nan_features'}); continue

        train = df[df['entry_ts'] <  SPLIT_TS]
        test  = df[df['entry_ts'] >= SPLIT_TS]

        rec = {**isl.to_dict()}
        rec['train_n']  = len(train); rec['train_wins'] = int(train['is_win'].sum())
        rec['test_n']   = len(test);  rec['test_wins']  = int(test['is_win'].sum())
        rec['train_pre_WR'] = rec['train_wins']/rec['train_n'] if rec['train_n'] else None
        rec['test_pre_WR']  = rec['test_wins'] /rec['test_n']  if rec['test_n']  else None

        if rec['train_n'] < MIN_TRAIN_N or rec['test_n'] < MIN_TEST_N:
            rec['oos_status'] = 'undersized_split'; rows.append(rec); continue

        # --- A) Rule replay ---
        try:
            clauses_a = parse_rule(isl['rule'])
            mask_a    = apply_rule(test, clauses_a)
            kept      = test[mask_a]
            rec['A_n_kept']  = len(kept)
            rec['A_w_kept']  = int(kept['is_win'].sum())
            rec['A_post_WR'] = (rec['A_w_kept']/rec['A_n_kept']) if rec['A_n_kept'] else None
            rec['A_holds30'] = bool(rec['A_n_kept'] >= MIN_TEST_KEEP and (rec['A_post_WR'] or 0) >= 0.30)
        except Exception as e:
            rec['A_error'] = str(e)

        # --- B) Refit ---
        try:
            ytr = train['is_win'].astype(bool).values
            if ytr.sum() == 0 or ytr.sum() == len(ytr):
                rec['oos_status'] = 'train_degenerate'; rows.append(rec); continue
            Xtr = train[FEATURES].values
            tree = DecisionTreeClassifier(max_depth=5, criterion='gini',
                                          min_samples_leaf=MIN_LEAF,
                                          random_state=42)
            tree.fit(Xtr, ytr)
            leaf = best_leaf_rule(tree, FEATURES, min_keep=MIN_LEAF)
            if leaf is None:
                rec['B_status'] = 'no_qualifying_leaf'; rows.append(rec); continue
            clauses_b, b_train_keep, b_train_w, b_train_l = leaf
            rec['B_rule'] = ' AND '.join(f'{c} {op} {v:.6g}' for c,op,v in clauses_b)
            rec['B_train_n_kept'] = b_train_keep
            rec['B_train_post_WR'] = b_train_w / b_train_keep
            mask_b = apply_rule(test, clauses_b)
            kept_b = test[mask_b]
            rec['B_n_kept']  = len(kept_b)
            rec['B_w_kept']  = int(kept_b['is_win'].sum())
            rec['B_post_WR'] = (rec['B_w_kept']/rec['B_n_kept']) if rec['B_n_kept'] else None
            rec['B_holds30'] = bool(rec['B_n_kept'] >= MIN_TEST_KEEP and (rec['B_post_WR'] or 0) >= 0.30)
            rec['oos_status'] = 'ok'
        except Exception as e:
            rec['B_error'] = str(e)
            rec['oos_status'] = rec.get('oos_status','error')

        rows.append(rec)

    out = pd.DataFrame(rows)
    out.to_csv(OUT_CSV, index=False)
    print(f'[write] {OUT_CSV}  ({len(out)} rows, {time.time()-t0:.1f}s)')

    total = len(out)
    status = out['oos_status'].fillna('no_status').value_counts().to_dict()
    a_col = out['A_holds30'] if 'A_holds30' in out.columns else pd.Series(dtype=bool)
    b_col = out['B_holds30'] if 'B_holds30' in out.columns else pd.Series(dtype=bool)
    a_holds = int((a_col == True).sum())
    b_holds = int((b_col == True).sum())
    a_attempted = int(out['A_post_WR'].notna().sum()) if 'A_post_WR' in out.columns else 0
    b_attempted = int(out['B_post_WR'].notna().sum()) if 'B_post_WR' in out.columns else 0

    def safe_mean(s): return float(np.nanmean(s)) if len(s) else float('nan')
    train_mean_post_wr = safe_mean(out['post_WR'])
    a_mean_test = safe_mean(out['A_post_WR'].dropna()) if 'A_post_WR' in out.columns else float('nan')
    b_mean_test = safe_mean(out['B_post_WR'].dropna()) if 'B_post_WR' in out.columns else float('nan')

    md = []
    md.append('# OOS validation — strong-edge islands')
    md.append('')
    md.append(f'**Generated:** {pd.Timestamp.utcnow().isoformat()}')
    md.append(f'**Selection:** in-sample post_WR >= {STRONG_POST_WR}, n_kept >= {STRONG_N_KEPT}  ({total} islands)')
    md.append(f'**Split:** train < {SPLIT_TS.isoformat()}, test >= {SPLIT_TS.isoformat()}')
    md.append(f'**Gates:** train_n >= {MIN_TRAIN_N}, test_n >= {MIN_TEST_N}, leaf >= {MIN_LEAF}, test_n_kept >= {MIN_TEST_KEEP}')
    md.append('')
    md.append('## Pipeline status')
    md.append('')
    for k,v in sorted(status.items(), key=lambda x: -x[1]):
        md.append(f'- {k}: {v}')
    md.append('')
    md.append('## Holdout survival (test post_WR >= 30%)')
    md.append('')
    md.append(f'- **A) Rule replay** (in-sample rule applied to test): **{a_holds}/{total}** survive  (parsed/applied on {a_attempted})')
    md.append(f'- **B) Refit on train** (new depth-5 tree, best leaf applied to test): **{b_holds}/{total}** survive  (fitted on {b_attempted})')
    md.append('')
    md.append('## Mean post-WR comparison')
    md.append('')
    md.append(f'- In-sample (training metadata):           {train_mean_post_wr:.3f}')
    md.append(f'- Test, in-sample rule replay (A):         {a_mean_test:.3f}')
    md.append(f'- Test, refit-on-train best leaf (B):      {b_mean_test:.3f}')
    md.append('')

    md.append('## Per-strategy holdout survival')
    md.append('')
    grp = out.groupby('strategy_id').agg(
        n=('strategy_id','size'),
        A_holds=('A_holds30', lambda s: int((s==True).sum())) if 'A_holds30' in out.columns else ('strategy_id','size'),
        B_holds=('B_holds30', lambda s: int((s==True).sum())) if 'B_holds30' in out.columns else ('strategy_id','size'),
    ).sort_values('n', ascending=False).head(20)
    md.append('| strategy | n | A holds | B holds |')
    md.append('|---|---:|---:|---:|')
    for sid, row in grp.iterrows():
        md.append(f'| {sid} | {int(row["n"])} | {int(row["A_holds"])} | {int(row["B_holds"])} |')
    md.append('')

    OUT_MD.write_text('\n'.join(md))
    print(f'[write] {OUT_MD}')
    print()
    print('='*60)
    print(f'A (rule replay):    {a_holds}/{total} survive  (mean test post_WR {a_mean_test:.3f})')
    print(f'B (refit on train): {b_holds}/{total} survive  (mean test post_WR {b_mean_test:.3f})')
    print(f'In-sample mean post_WR was {train_mean_post_wr:.3f}')
    print(f'Elapsed: {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
