from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

BASE = Path('/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0')
INFILE = BASE / 'fast_targeted_winner_islands.csv'
OUT_CSV = BASE / 'winner_island_sibling_seed_bank.csv'
OUT_MD = BASE / 'winner_island_sibling_seed_bank.md'
PARENT_KEYS = ['strategy_id', 'pair', 'direction', 'technical_regime_53']
FACTOR_RE = re.compile(r'(ATR_ratio|ADX14|BB_compress|RSI14|price_pos|volume_ratio|hour_utc|session_bucket)')
MAX_PER_PARENT = 4


def frame_to_markdown(df: pd.DataFrame) -> str:
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


def factor_signature(rule: str) -> str:
    seen = []
    for match in FACTOR_RE.findall(rule):
        if match not in seen:
            seen.append(match)
    return ' + '.join(seen)


def statement(row: pd.Series) -> str:
    return (
        f"mixed parent {row.strategy_id} / {row.pair} / {row.direction} / {row.technical_regime_53} "
        f"({int(row.parent_wins)}W/{int(row.parent_losses)}L) -> factor shave {row.rule} -> "
        f"seed {int(row.wins)}W/{int(row.losses)}L (holdout {int(row.hold_wins)}W/{int(row.hold_losses)}L, mean_R {row.mean_R:.2f})"
    )


def main() -> None:
    df = pd.read_csv(INFILE)
    df = df.sort_values(['losses', 'wr', 'wins', 'hold_losses', 'hold_wins', 'mean_R'], ascending=[True, False, False, True, False, False]).copy()
    df['factor_signature'] = df['rule'].map(factor_signature)
    df['is_pure_seed'] = (df['wins'] >= 10) & (df['losses'] == 0)
    df['is_holdout_clean_seed'] = (df['hold_wins'] >= 3) & (df['hold_losses'] == 0)

    kept_rows = []
    for _, grp in df.groupby(PARENT_KEYS, sort=False, dropna=False):
        seen_signatures: set[str] = set()
        seen_shapes: set[tuple[int, int, int, int]] = set()
        parent_keep = 0
        for _, row in grp.iterrows():
            sig = row['factor_signature']
            shape = (int(row['wins']), int(row['losses']), int(row['hold_wins']), int(row['hold_losses']))
            if parent_keep == 0:
                kept_rows.append(row.to_dict())
                seen_signatures.add(sig)
                seen_shapes.add(shape)
                parent_keep += 1
                continue
            if parent_keep >= MAX_PER_PARENT:
                break
            if sig in seen_signatures and shape in seen_shapes:
                continue
            if sig in seen_signatures and row['losses'] > 1:
                continue
            kept_rows.append(row.to_dict())
            seen_signatures.add(sig)
            seen_shapes.add(shape)
            parent_keep += 1

    bank = pd.DataFrame(kept_rows)
    bank = bank.sort_values(['losses', 'wr', 'wins', 'hold_losses', 'hold_wins', 'mean_R'], ascending=[True, False, False, True, False, False]).reset_index(drop=True)
    bank['seed_bank_rank'] = bank.index + 1
    bank['seed_statement'] = bank.apply(statement, axis=1)
    bank.to_csv(OUT_CSV, index=False)

    parent_counts = bank.groupby(PARENT_KEYS[:3]).size().reset_index(name='seed_count').sort_values('seed_count', ascending=False)
    lines = []
    lines.append('# Winner Island Sibling Seed Bank')
    lines.append('')
    lines.append('This bank keeps multiple distinct winner-island descendants per mixed parent instead of collapsing immediately to one best seed. The goal is to preserve sibling micro-bots when the factor recipe materially differs.')
    lines.append('')
    lines.append(f'- Raw island variants available: {len(df):,}')
    lines.append(f'- Diversified sibling-bank seeds kept: {len(bank):,}')
    lines.append(f'- Parents represented: {bank[PARENT_KEYS].drop_duplicates().shape[0]:,}')
    lines.append(f'- Pure sibling seeds: {int(bank.is_pure_seed.sum()):,}')
    lines.append(f'- Holdout-clean sibling seeds: {int(bank.is_holdout_clean_seed.sum()):,}')
    lines.append('')
    lines.append('## Top Seed Families By Count')
    lines.append(frame_to_markdown(parent_counts.head(20)))
    lines.append('')
    lines.append('## Top Sibling Seeds')
    for _, row in bank.head(30).iterrows():
        lines.append(f'- {row.seed_statement}')
    lines.append('')
    table_cols = ['seed_bank_rank', 'strategy_id', 'pair', 'direction', 'technical_regime_53', 'factor_signature', 'rule', 'wins', 'losses', 'wr', 'hold_wins', 'hold_losses', 'mean_R']
    lines.append('## Ranked Sibling Table')
    lines.append(frame_to_markdown(bank[table_cols].head(40)))
    OUT_MD.write_text('\n'.join(lines))
    print(OUT_CSV)
    print(OUT_MD)
    print(f'bank={len(bank)} parents={bank[PARENT_KEYS].drop_duplicates().shape[0]}')


if __name__ == '__main__':
    main()
