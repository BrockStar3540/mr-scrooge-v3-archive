from pathlib import Path
import pandas as pd

OUT = Path('/home/ubuntu/mr-scrooge-v3/research/technical-regime-53-atlas-v1')
daily_path = Path('/home/ubuntu/mr-scrooge-v3/research/daily-textbook-trade-encyclopedia-v0/daily_textbook_trade_ledger.parquet')
bar_path = OUT / 'daily_trade_ledger_with_regime53_bartrue.parquet'
cols = ['pair','entry_ts','ATR14','ATR_ratio','BB_width','BB_compress','ADX14','EMA_slope','RSI14','close_pos','technical_regime_53','technical_regime_desc']

daily = pd.read_parquet(daily_path)
daily['entry_ts'] = pd.to_datetime(daily['entry_ts'], utc=True)
bar = pd.read_parquet(bar_path, columns=cols)
bar['entry_ts'] = pd.to_datetime(bar['entry_ts'], utc=True)
labels = bar[cols].drop_duplicates(['pair','entry_ts'])
joined = daily.merge(labels, on=['pair','entry_ts'], how='left')
missing = int(joined['technical_regime_53'].isna().sum())
joined.to_parquet(OUT / 'daily_textbook_trade_ledger_with_regime53_bartrue.parquet', index=False)
joined.to_csv(OUT / 'daily_textbook_trade_ledger_with_regime53_bartrue.csv', index=False)

group = ['technical_regime_53','technical_regime_desc','strategy_name','pair_family','direction']
rep = joined[joined['record_type'].eq('repaired_winner')]
rep_sum = rep.groupby(group).agg(
    repaired_winners=('entry_ts','size'),
    median_R=('realized_at_2R_net','median'),
    median_mfe=('mfe_r_net','median'),
    median_mae=('mae_r','median'),
    discovery_winners=('era', lambda x: int((x == 'discovery').sum())),
    holdout_winners=('era', lambda x: int((x == 'holdout').sum())),
).reset_index().sort_values(['repaired_winners','median_R'], ascending=[False, False])
rep_sum.to_csv(OUT / 'daily_strategy_x_regime53_repaired_winners_bartrue.csv', index=False)

fp = joined[joined['record_type'].eq('first_pass')]
fp_sum = fp.groupby(group).agg(
    first_pass_n=('entry_ts','size'),
    first_pass_win_rate=('clean_2r','mean'),
    mean_R=('realized_at_2R_net','mean'),
    median_mfe=('mfe_r_net','median'),
).reset_index().sort_values('first_pass_n', ascending=False)
fp_sum.to_csv(OUT / 'daily_strategy_x_regime53_first_pass_bartrue.csv', index=False)

with open(OUT / 'summary_daily_encyclopedia.md', 'w') as f:
    f.write('# Daily Textbook Encyclopedia x Technical Regime 53 v1\n\n')
    f.write('Exact bar-true 53-regime labels joined back to the 63k-row daily textbook trade ledger. This is the paper-trade / repaired-winner strategy discovery view.\n\n')
    f.write('## Coverage\n\n')
    f.write(f'- Daily ledger rows labeled: {len(joined):,}\n')
    f.write(f'- Repaired winner rows: {len(rep):,}\n')
    f.write(f'- Regimes represented: {joined["technical_regime_53"].nunique()}\n')
    f.write(f'- Missing labels: {missing:,}\n\n')
    f.write('## Top Repaired Winner Synchrony\n\n')
    f.write(rep_sum.head(30).to_markdown(index=False))
    f.write('\n\n## First-Pass Strategy x Regime\n\n')
    f.write(fp_sum.head(20).to_markdown(index=False))
    f.write('\n\n## Interpretation\n\n')
    f.write('This is the clean bridge Brock asked for: textbook/repaired winning trades now carry an exact OHLCV technical regime label, strategy name, pair family, direction, session fields, and the original factor snapshot. Use this table to select candidate microstrategy bots; use the larger raw-event atlas for statistical backtesting and threshold tuning.\n')

print(f'joined={len(joined):,} repaired={len(rep):,} regimes={joined["technical_regime_53"].nunique()} missing={missing:,}')
print(rep_sum.head(10).to_string(index=False))
