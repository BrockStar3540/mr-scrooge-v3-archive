#!/usr/bin/env python3
"""
mine_class_islands.py

Phase A of the two-sided refinery.

For every parent cell (strategy_id x pair x direction x technical_regime_53) in
the raw trade ledger, fit a depth-5 decision tree targeting either is_win=True
(winner mining) or is_win=False (loser mining), then walk every leaf and pick
the best one -- highest P(target_class | leaf) subject to a minimum support gate.

Runs ALL FOUR combinations in one pass to share the corpus load:
    target = {win, loss}  x  window = {6yr, 6mo}

The 'islands' are tree-path conjunctions over 7 numeric factors + 7
one-hot-encoded session_bucket values. No prior factor filtering is used; the
classifier sees raw trades and chooses split points itself.

Outputs (in /Users/brock-mini-mac/scrooge-research/seed-family-factory/):
    raw_winner_islands_6yr.csv
    raw_winner_islands_6mo.csv
    raw_loser_islands_6yr.csv
    raw_loser_islands_6mo.csv
    raw_islands_summary.md
"""
from __future__ import annotations
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path('/Users/brock-mini-mac/scrooge-research')
PARQUET = ROOT / 'all_strategies_all_pairs_trades.parquet'
OUT_DIR = ROOT / 'seed-family-factory'
OUT_DIR.mkdir(parents=True, exist_ok=True)

KEY_COLS = ['strategy_id','pair','direction','technical_regime_53']
FACTORS_NUMERIC = ['ATR_ratio','BB_compress','RSI14','price_pos','volume_ratio','ADX14','hour_utc']
SESSION_BUCKETS = ['asia','asia_late','london_open','ny_open','ny_mid','ny_close','off_hours']
SB_FEATS = [f'sb_{s}' for s in SESSION_BUCKETS]
FEATURES = FACTORS_NUMERIC + SB_FEATS

# per-window gates
GATES = {
    '6yr': dict(min_cell_n=200, min_leaf=20),
    '6mo': dict(min_cell_n=50,  min_leaf=10),
}
MIN_TARGET_RATE  = 0.60  # absolute floor on leaf target density
MIN_PURITY_GAIN  = 0.15  # leaf target_rate must beat parent target_rate by at least this much
WINDOW_DAYS = {'6yr': None, '6mo': 180}

# tree leaf walker -----------------------------------------------------------
def best_leaf_for_class(tree: DecisionTreeClassifier, target_value: bool, min_keep: int):
    """Return (path_clauses, n_kept, target_count, other_count, target_rate) or None."""
    t = tree.tree_
    class_idx = {c: i for i, c in enumerate(tree.classes_)}
    tgt_idx = class_idx.get(target_value, class_idx.get(int(target_value), None))
    if tgt_idx is None: return None
    best = None
    def walk(node, path):
        nonlocal best
        if t.children_left[node] == _tree.TREE_LEAF:
            n_kept = int(t.n_node_samples[node])
            if n_kept < min_keep:
                return
            probs = t.value[node][0]
            tgt_kept = int(round(float(probs[tgt_idx]) * n_kept))
            other_kept = n_kept - tgt_kept
            rate = tgt_kept / n_kept
            if rate < MIN_TARGET_RATE:
                return
            if best is None or rate > best[4] or (rate == best[4] and n_kept > best[1]):
                best = (list(path), n_kept, tgt_kept, other_kept, rate)
            return
        feat = FEATURES[t.feature[node]]
        thr = float(t.threshold[node])
        walk(t.children_left[node],  path + [(feat, '<=', thr)])
        walk(t.children_right[node], path + [(feat,  '>', thr)])
    walk(0, [])
    return best

def render_rule(clauses) -> str:
    """Convert tree-path clauses into a human-readable rule string."""
    parts = []
    for feat, op, thr in clauses:
        if feat.startswith('sb_'):
            sb = feat[3:]
            if op == '>' and thr >= 0.5:
                parts.append(f'session_bucket=={sb}')
            elif op == '<=' and thr >= 0.5:
                parts.append(f'session_bucket!={sb}')
            else:
                parts.append(f'{feat}{op}{thr:.4g}')
        else:
            parts.append(f'{feat}{op}{thr:.6g}')
    return ' AND '.join(parts)

def factor_signature(clauses) -> str:
    feats = set()
    for feat, _, _ in clauses:
        if feat.startswith('sb_'):
            feats.add('session_bucket')
        else:
            feats.add(feat)
    return ' + '.join(sorted(feats))

# main -----------------------------------------------------------------------
def main():
    t0 = time.time()
    print(f'[load] parquet: {PARQUET}')
    cols = KEY_COLS + ['entry_ts','is_win','session_bucket'] + FACTORS_NUMERIC
    corpus = pq.read_table(PARQUET, columns=cols).to_pandas()
    print(f'  corpus rows: {len(corpus):,}  ({time.time()-t0:.1f}s)')
    print(f'  entry_ts range: {corpus["entry_ts"].min()} -> {corpus["entry_ts"].max()}')

    # one-hot session
    for s in SESSION_BUCKETS:
        corpus[f'sb_{s}'] = (corpus['session_bucket'] == s).astype(np.int8)

    summary_blocks = []
    for window_name in ['6yr', '6mo']:
        days = WINDOW_DAYS[window_name]
        if days is None:
            window_df = corpus
        else:
            cutoff = corpus['entry_ts'].max() - pd.Timedelta(days=days)
            window_df = corpus[corpus['entry_ts'] >= cutoff]
        print(f'\n[window {window_name}] {len(window_df):,} rows; cutoff '
              f'{None if days is None else cutoff.isoformat()}')
        gates = GATES[window_name]
        grouped = window_df.groupby(KEY_COLS, sort=False)
        print(f'  parent cells: {grouped.ngroups:,}  ({time.time()-t0:.1f}s)')

        for target_name in ['win', 'loss']:
            target_value = (target_name == 'win')
            rows = []
            cells_tried = 0
            cells_emitted = 0
            for key, df in grouped:
                n = len(df)
                if n < gates['min_cell_n']:
                    continue
                cells_tried += 1
                ydf = df['is_win'].astype(bool).values
                # need both classes present for a meaningful split
                if ydf.sum() == 0 or ydf.sum() == n:
                    continue
                X = df[FEATURES].fillna(0).values
                y = ydf if target_name == 'win' else ~ydf
                if y.sum() < gates['min_leaf']:
                    continue
                tree = DecisionTreeClassifier(max_depth=5, criterion='gini',
                                              min_samples_leaf=gates['min_leaf'],
                                              random_state=42)
                tree.fit(X, y)
                parent_target_rate = (y.sum() / n)  # P(target=True) in this parent cell
                leaf = best_leaf_for_class(tree, target_value=True, min_keep=gates['min_leaf'])
                if leaf is None:
                    continue
                clauses, n_kept, tgt_kept, other_kept, rate = leaf
                if rate - parent_target_rate < MIN_PURITY_GAIN:
                    continue  # leaf is not meaningfully purer than parent
                rule = render_rule(clauses)
                if not rule:
                    continue
                parent_wr = int(ydf.sum()) / n
                # Stats inside leaf, in original win/loss terms (not target terms)
                if target_name == 'win':
                    leaf_wins   = tgt_kept
                    leaf_losses = other_kept
                else:
                    leaf_wins   = other_kept
                    leaf_losses = tgt_kept
                lift = (rate / parent_wr) if (target_name=='win' and parent_wr>0) else                        (rate / (1.0-parent_wr)) if (target_name=='loss' and parent_wr<1) else float('nan')
                rows.append({
                    'strategy_id':         key[0],
                    'pair':                key[1],
                    'direction':           key[2],
                    'technical_regime_53': key[3],
                    'parent_n':            n,
                    'parent_wins':         int(ydf.sum()),
                    'parent_losses':       n - int(ydf.sum()),
                    'parent_wr':           round(parent_wr, 4),
                    'rule':                rule,
                    'factor_signature':    factor_signature(clauses),
                    'depth':               len(clauses),
                    'n':                   n_kept,
                    'wins':                leaf_wins,
                    'losses':              leaf_losses,
                    'target_rate':         round(rate, 4),
                    'lift':                round(lift, 3),
                })
                cells_emitted += 1
            df_out = pd.DataFrame(rows)
            out_path = OUT_DIR / f'raw_{target_name}ner_islands_{window_name}.csv' if target_name=='win' else OUT_DIR / f'raw_loser_islands_{window_name}.csv'
            df_out.to_csv(out_path, index=False)
            print(f'  [{target_name}/{window_name}] {len(df_out)} islands from {cells_tried} cells '
                  f'(emit rate {len(df_out)/max(1,cells_tried):.1%})  -> {out_path.name}')
            summary_blocks.append((target_name, window_name, df_out))

    # summary md -------------------------------------------------------------
    md = ['# Raw class-islands summary','']
    md.append(f'**Generated:** {pd.Timestamp.utcnow().isoformat()}')
    md.append('')
    md.append('## Counts per (target, window)')
    md.append('')
    md.append('| target | window | islands | parent cells qualifying | min leaf | min cell n |')
    md.append('|---|---|---:|---|---:|---:|')
    for tname, wname, df in summary_blocks:
        md.append(f'| {tname} | {wname} | {len(df):,} | n>={GATES[wname]["min_cell_n"]} | {GATES[wname]["min_leaf"]} | {GATES[wname]["min_cell_n"]} |')
    md.append('')

    # winner-vs-loser overlap on 6yr and on 6mo
    def overlap(wdf, ldf):
        wk = set(map(tuple, wdf[KEY_COLS].values.tolist()))
        lk = set(map(tuple, ldf[KEY_COLS].values.tolist()))
        return len(wk & lk), len(wk - lk), len(lk - wk)
    wb = {n: d for t, n, d in summary_blocks if t=='win'}
    lb = {n: d for t, n, d in summary_blocks if t=='loss'}
    for wname in ('6yr','6mo'):
        if wname in wb and wname in lb:
            both, only_w, only_l = overlap(wb[wname], lb[wname])
            md.append(f'### {wname} winner-vs-loser cell overlap')
            md.append('')
            md.append(f'- cells with BOTH a winner island and a loser island: **{both}**')
            md.append(f'- cells with only a winner island: {only_w}')
            md.append(f'- cells with only a loser island: {only_l}')
            md.append('')

    # 6yr-vs-6mo persistence
    def persistence(d6yr, d6mo):
        k6yr = set(map(tuple, d6yr[KEY_COLS].values.tolist()))
        k6mo = set(map(tuple, d6mo[KEY_COLS].values.tolist()))
        return len(k6yr & k6mo), len(k6yr - k6mo), len(k6mo - k6yr)
    for tname in ('win','loss'):
        if '6yr' in {n: d for t,n,d in summary_blocks if t==tname} and            '6mo' in {n: d for t,n,d in summary_blocks if t==tname}:
            d6yr = next(d for t,n,d in summary_blocks if t==tname and n=='6yr')
            d6mo = next(d for t,n,d in summary_blocks if t==tname and n=='6mo')
            both, only_6yr, only_6mo = persistence(d6yr, d6mo)
            md.append(f'### {tname} islands: 6yr vs 6mo cell persistence')
            md.append('')
            md.append(f'- cells with an island in BOTH windows: **{both}** (durable)')
            md.append(f'- only 6yr (no longer present in last 6mo): {only_6yr}')
            md.append(f'- only 6mo (new in last 6mo): {only_6mo}')
            md.append('')

    md.append('## Top 15 winner islands per window (by target_rate then n)')
    md.append('')
    for wname in ('6yr','6mo'):
        if wname in wb:
            md.append(f'### {wname}')
            md.append('')
            top = wb[wname].sort_values(['target_rate','n'], ascending=[False, False]).head(15)
            md.append('| strategy | pair | dir | regime | parent | leaf n | W | L | wr | lift |')
            md.append('|---|---|---|---|---:|---:|---:|---:|---:|---:|')
            for _, r in top.iterrows():
                md.append(f'| {r["strategy_id"]} | {r["pair"]} | {r["direction"]} | {r["technical_regime_53"]} | {r["parent_n"]} | {r["n"]} | {r["wins"]} | {r["losses"]} | {r["target_rate"]:.3f} | {r["lift"]:.2f} |')
            md.append('')

    md.append('## Top 15 loser islands per window (by target_rate then n)')
    md.append('')
    for wname in ('6yr','6mo'):
        if wname in lb:
            md.append(f'### {wname}')
            md.append('')
            top = lb[wname].sort_values(['target_rate','n'], ascending=[False, False]).head(15)
            md.append('| strategy | pair | dir | regime | parent | leaf n | W | L | loss_rate | lift |')
            md.append('|---|---|---|---|---:|---:|---:|---:|---:|---:|')
            for _, r in top.iterrows():
                md.append(f'| {r["strategy_id"]} | {r["pair"]} | {r["direction"]} | {r["technical_regime_53"]} | {r["parent_n"]} | {r["n"]} | {r["wins"]} | {r["losses"]} | {r["target_rate"]:.3f} | {r["lift"]:.2f} |')
            md.append('')

    (OUT_DIR/'raw_islands_summary.md').write_text('\n'.join(md))
    print()
    print(f'[write] {OUT_DIR/"raw_islands_summary.md"}')
    print(f'Total elapsed: {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
