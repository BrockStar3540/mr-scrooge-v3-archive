#!/usr/bin/env python3
"""Generate the two markdown summaries from the already-written CSVs."""
from pathlib import Path
import pandas as pd

OUT = Path('/Users/brock-mini-mac/scrooge-research/seed-family-factory')

lineage = pd.read_csv(OUT/'seed_family_lineage.csv')
winners = pd.read_csv(OUT/'seed_family_children_winners.csv')
losers  = pd.read_csv(OUT/'seed_family_children_loser_contrast_bank.csv')

def md_table(df, cols):
    out = []
    out.append('| ' + ' | '.join(cols) + ' |')
    out.append('|' + '|'.join(['---']*len(cols)) + '|')
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r.get(c, '')
            if isinstance(v, float):
                cells.append(f'{v:.4g}')
            else:
                cells.append(str(v))
        out.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(out)

md = ['# seed_family_children_winners','']
md.append(f'**Built:** {pd.Timestamp.utcnow().isoformat()}')
md.append(f'**Source mutations (gen-1 from 141 seeds):** {len(lineage):,} children evaluated')
md.append(f'**Winner-side rows (winner_seed + near_pure_seed):** {len(winners):,}')
md.append('')
md.append('## Bucket distribution across ALL evaluated children')
md.append('')
for b, n in lineage['bucket'].value_counts().items():
    md.append(f'- **{b}**: {n:,}')
md.append('')
md.append('## Winner-side composition')
md.append('')
wb = winners.merge(lineage[['seed_id','bucket']], on='seed_id', how='left')
for b, sub in wb.groupby('bucket'):
    md.append(f'- **{b}**: {len(sub):,}')
md.append('')
md.append('## Mutation_type yield (% becoming winner-side)')
md.append('')
mtot = lineage['mutation_type'].value_counts()
mwin = wb['mutation_type'].value_counts()
md.append('| mutation_type | total | winner-side | yield |')
md.append('|---|---:|---:|---:|')
for mt, n in mtot.items():
    w = int(mwin.get(mt, 0))
    md.append(f'| {mt} | {n:,} | {w:,} | {w/n:.1%} |')
md.append('')
md.append('## Top 25 by seed_survival_score')
md.append('')
cols = ['rank','seed_id','strategy_id','pair','direction','technical_regime_53','mutation_type','n','wins','losses','wr','mean_R','hold_wins','hold_losses','purity_gain','seed_survival_score']
md.append(md_table(winners.head(25), cols))
md.append('')
md.append('## Strategy x regime winner-side counts (top 15)')
md.append('')
g = wb.groupby(['strategy_id','technical_regime_53']).size().sort_values(ascending=False).head(15)
md.append('| strategy | regime | winner-side cells |')
md.append('|---|---|---:|')
for (s,r), n in g.items():
    md.append(f'| {s} | {r} | {n} |')
(OUT/'seed_family_children_winners.md').write_text('\n'.join(md))

md = ['# seed_family_children_loser_contrast_bank','']
md.append(f'**Built:** {pd.Timestamp.utcnow().isoformat()}')
md.append(f'**Row count:** {len(losers):,}')
md.append(f'**Size on disk:** ~{(OUT/"seed_family_children_loser_contrast_bank.csv").stat().st_size/1e9:.2f} GB  (Mini-only; gitignored from EC2 commit)')
md.append('')
md.append('## Bucket counts')
md.append('')
for b, n in losers['bucket'].value_counts().items():
    md.append(f'- **{b}**: {n:,}')
md.append('')
md.append('## Loser session distribution (rejected_by_shave + residual + false_friend_sibling)')
md.append('')
keep = losers[losers['bucket'].isin(['rejected_by_shave','residual','false_friend_sibling'])]
for s, n in keep['session_bucket'].value_counts().items():
    md.append(f'- {s}: {n:,}')
md.append('')
md.append('## Top loser-heavy parent cells (rejected_by_shave + residual)')
md.append('')
kb = losers[losers['bucket'].isin(['rejected_by_shave','residual'])]
kp = kb.groupby(['strategy_id','pair','direction','technical_regime_53']).size().sort_values(ascending=False).head(15)
md.append('| strategy | pair | dir | regime | loser rows |')
md.append('|---|---|---|---|---:|')
for (s,p,d,r), n in kp.items():
    md.append(f'| {s} | {p} | {d} | {r} | {n:,} |')
md.append('')
md.append('## Loser hot zones by factor median (residual rows only)')
md.append('')
resid = losers[losers['bucket'] == 'residual']
md.append('| factor | median | p25 | p75 |')
md.append('|---|---:|---:|---:|')
for f in ['ATR_ratio','RSI14','BB_compress','price_pos','volume_ratio','ADX14','hour_utc']:
    s = pd.to_numeric(resid[f], errors='coerce').dropna()
    if len(s):
        md.append(f'| {f} | {s.median():.4g} | {s.quantile(.25):.4g} | {s.quantile(.75):.4g} |')
(OUT/'seed_family_children_loser_contrast_bank.md').write_text('\n'.join(md))

print('wrote 2 md files')
