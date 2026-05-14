from __future__ import annotations

from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
INFILE = BASE / 'fast_targeted_winner_islands.csv'
OUT_CSV = BASE / 'winner_island_seed_ranking.csv'
OUT_MD = BASE / 'winner_island_seed_ranking.md'
PARENT_KEYS = ['strategy_id', 'pair', 'direction', 'technical_regime_53']


def frame_to_markdown(df: pd.DataFrame) -> str:
    try:
        return df.to_markdown(index=False)
    except ImportError:
        cols = list(df.columns)
        lines = [
            '| ' + ' | '.join(cols) + ' |',
            '| ' + ' | '.join(['---'] * len(cols)) + ' |',
        ]
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


def build_seed_statement(row: pd.Series) -> str:
    parent = (
        f"mixed parent {row.strategy_id} / {row.pair} / {row.direction} / {row.technical_regime_53} "
        f"({int(row.parent_wins)}W/{int(row.parent_losses)}L, WR {row.parent_wr:.1%})"
    )
    shave = f"factor shave {row.rule}"
    island = (
        f"winner island {int(row.wins)}W/{int(row.losses)}L "
        f"(n={int(row.n)}, WR {row.wr:.1%}, holdout {int(row.hold_wins)}W/{int(row.hold_losses)}L, mean_R {row.mean_R:.2f})"
    )
    return f'{parent} -> {shave} -> {island}'


def classify_bucket(row: pd.Series) -> str:
    if row.is_pure_seed and row.is_holdout_clean_seed:
        return 'pure_holdout_clean'
    if row.is_pure_seed:
        return 'pure'
    if row.is_holdout_clean_seed:
        return 'near_pure_holdout_clean'
    return 'near_pure'


def main() -> None:
    df = pd.read_csv(INFILE)
    ordered = df.sort_values(
        ['losses', 'wr', 'wins', 'hold_losses', 'hold_wins', 'hold_wr', 'mean_R', 'wr_lift'],
        ascending=[True, False, False, True, False, False, False, False],
    ).copy()

    best = ordered.drop_duplicates(subset=PARENT_KEYS, keep='first').copy()
    best['parent_keep_frac'] = best['n'] / best['parent_n']
    best['is_pure_seed'] = (best['wins'] >= 10) & (best['losses'] == 0)
    best['is_near_pure_seed'] = (best['wins'] >= 10) & (best['wr'] >= 0.75)
    best['is_holdout_clean_seed'] = (best['hold_wins'] >= 3) & (best['hold_losses'] == 0)
    best['primary_bucket'] = best.apply(classify_bucket, axis=1)
    best['seed_statement'] = best.apply(build_seed_statement, axis=1)

    bucket_order = {
        'pure_holdout_clean': 0,
        'pure': 1,
        'near_pure_holdout_clean': 2,
        'near_pure': 3,
    }
    best['bucket_order'] = best['primary_bucket'].map(bucket_order)
    best = best.sort_values(
        ['bucket_order', 'losses', 'wr', 'wins', 'hold_wins', 'mean_R', 'wr_lift'],
        ascending=[True, True, False, False, False, False, False],
    ).reset_index(drop=True)
    best['seed_rank'] = best.index + 1
    best['bucket_rank'] = best.groupby('primary_bucket').cumcount() + 1

    export_cols = [
        'seed_rank', 'bucket_rank', 'primary_bucket',
        'strategy_id', 'pair', 'direction', 'technical_regime_53',
        'parent_n', 'parent_wins', 'parent_losses', 'parent_wr', 'parent_keep_frac',
        'rule', 'n', 'wins', 'losses', 'wr', 'wr_lift', 'mean_R',
        'disc_wins', 'disc_losses', 'hold_wins', 'hold_losses', 'hold_wr',
        'is_pure_seed', 'is_near_pure_seed', 'is_holdout_clean_seed',
        'seed_statement',
    ]
    best[export_cols].to_csv(OUT_CSV, index=False)

    pure = best[best['is_pure_seed']].copy()
    near = best[(best['is_near_pure_seed']) & (~best['is_pure_seed'])].copy()
    hold_clean = best[best['is_holdout_clean_seed']].copy()

    lines = []
    lines.append('# Winner Island Seed Ranking')
    lines.append('')
    lines.append('This file collapses the raw winner-island variant list down to the single best winner island per mixed parent cell. Treat each row as a candidate micro-strategy seed, not a deployable rule.')
    lines.append('')
    lines.append(f'- Distinct mixed-parent seeds: {len(best):,}')
    lines.append(f'- Pure seeds: {len(pure):,}')
    lines.append(f'- Near-pure seeds excluding pure: {len(near):,}')
    lines.append(f'- Holdout-clean seeds: {len(hold_clean):,}')
    lines.append('')
    lines.append('## Top Pure Seeds')
    for _, row in pure.head(12).iterrows():
        lines.append(f"- {row.seed_statement}")
    lines.append('')
    lines.append('## Top Holdout-Clean Seeds')
    for _, row in hold_clean.head(12).iterrows():
        lines.append(f"- {row.seed_statement}")
    lines.append('')
    lines.append('## Top Near-Pure Seeds')
    for _, row in near.head(20).iterrows():
        lines.append(f"- {row.seed_statement}")
    lines.append('')
    table_cols = [
        'seed_rank', 'primary_bucket', 'strategy_id', 'pair', 'direction', 'technical_regime_53',
        'rule', 'wins', 'losses', 'wr', 'hold_wins', 'hold_losses', 'mean_R', 'wr_lift',
    ]
    lines.append('## Ranked Seed Table')
    lines.append(frame_to_markdown(best[table_cols].head(40)))
    OUT_MD.write_text('\n'.join(lines))

    print(OUT_CSV)
    print(OUT_MD)
    print(f'seeds={len(best)} pure={len(pure)} near={len(near)} hold_clean={len(hold_clean)}')


if __name__ == '__main__':
    main()
