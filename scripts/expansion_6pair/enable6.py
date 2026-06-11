"""Re-enable 4 of the 6 researched pairs (USD_JPY, USD_CHF, AUD_JPY, EUR_JPY)
with PAIR-SCOPED cells. NZD_USD (11 sides) + EUR_GBP (6) stay benched - too thin.

1. gate: allowlist cells gain optional 5th element = pair. 5-tuples fire only on
   their pair; legacy 4-tuples fire only on cell_allowlist_default_pairs (the
   pooled-validated 4) so old cells can't leak onto new pairs.
2. config: splice spread-haircut survivors (ev_adj>=1.25 at measured spreads) as
   5-tuples; record provenance + default-pairs scope.
3. screener: CANDIDATE_PAIRS 4 -> 8."""
import json
import pandas as pd

ROOT = '/home/ubuntu/mr-scrooge-v3'
ENABLE = ['USD_JPY', 'USD_CHF', 'AUD_JPY', 'EUR_JPY']
HAIR = {'USD_JPY': 0.65, 'USD_CHF': -0.10, 'NZD_USD': 0.70,
        'EUR_JPY': 1.75, 'AUD_JPY': 1.05, 'EUR_GBP': -0.05}

# --- 1. gate ---
p = f'{ROOT}/src/scrooge_v3/gates/pip_eater_gate.py'
s = open(p).read()
old = """        self.cell_allowlist = dict(self.config.get("cell_allowlist") or {})"""
new = """        self.cell_allowlist = dict(self.config.get("cell_allowlist") or {})
        # Cells may carry a 5th element = pair (pair-scoped, 2026-06-11 6-pair
        # expansion). Legacy 4-tuples were validated POOLED on these pairs only
        # and must not leak onto newly enabled pairs.
        self.allowlist_default_pairs = set(
            self.config.get("cell_allowlist_default_pairs")
            or ["AUD_USD", "EUR_USD", "GBP_USD", "USD_CAD"]
        )"""
assert s.count(old) == 1, 'gate init anchor'
s = s.replace(old, new)
old = """                _hits = sum(
                    1 for _c in (_allow or [])
                    if int(_c[0]) == align_score and buckets.get(_c[1]) == _c[2]
                    and (len(_c) < 4 or _c[3] == direction)
                )"""
new = """                _hits = sum(
                    1 for _c in (_allow or [])
                    if int(_c[0]) == align_score and buckets.get(_c[1]) == _c[2]
                    and (len(_c) < 4 or _c[3] == direction)
                    and (_c[4] == pair if len(_c) > 4
                         else pair in self.allowlist_default_pairs)
                )"""
assert s.count(old) == 1, 'gate hits anchor'
open(p, 'w').write(s.replace(old, new))
print('1. gate pair-scoped')

# --- 2. config splice ---
d = pd.read_csv(f'{ROOT}/data/lab_training/cell_book_6pair_candidate_sides_2026-06-11.csv')
d['ev_adj'] = d.ev_te - d.pair.map(HAIR)
surv = d[(d.ev_adj >= 1.25) & d.pair.isin(ENABLE)]
cfgp = f'{ROOT}/config/default.json'
cfg = json.load(open(cfgp))
pe = cfg['gates']['pip_eater']
pe['cell_allowlist_default_pairs'] = ['AUD_USD', 'EUR_USD', 'GBP_USD', 'USD_CAD']
added = {}
for _, r in surv.iterrows():
    cell = [int(r['align']), r['factor'], r['bucket'], r['direction'], r['pair']]
    pe['cell_allowlist'].setdefault(r['strategy'], []).append(cell)
    added[r['pair']] = added.get(r['pair'], 0) + 1
prov = pe['cell_allowlist'].setdefault('_provenance', {})
if isinstance(prov, dict):
    prov['6pair_expansion_2026-06-11'] = (
        'pair-scoped 5-tuples from cell_book_6pair_candidate_sides_2026-06-11.csv, '
        f'spread-haircut survivors (measured 20:30Z: {HAIR}), enabled {ENABLE}; '
        'NZD_USD+EUR_GBP benched (thin books)')
json.dump(cfg, open(cfgp, 'w'), indent=2)
print('2. spliced sides per pair:', added)

# --- 3. screener roster ---
p = f'{ROOT}/src/scrooge_v3/market/screener.py'
s = open(p).read()
old = '''CANDIDATE_PAIRS = [
    # 2026-06-03 align_min=4 dial-in: kept the 4 strongest align=4 pairs
    # (net/trade EUR_USD +1.42, GBP_USD +1.26, AUD_USD +0.97, USD_CAD +0.77).
    # Chopped EUR_JPY (laggard +0.52p, sub-50% WR even fully aligned).
    "AUD_USD", "EUR_USD", "GBP_USD", "USD_CAD",
]'''
new = '''CANDIDATE_PAIRS = [
    # Core 4 (2026-06-03 dial-in), validated pooled — legacy 4-tuple cells.
    "AUD_USD", "EUR_USD", "GBP_USD", "USD_CAD",
    # 2026-06-11 re-add: 8yr per-pair direction-keyed cells, OOS bar + measured-
    # spread haircut (pair-scoped 5-tuples; data/lab_training/
    # cell_book_6pair_candidate_sides_2026-06-11.csv). NZD_USD/EUR_GBP benched.
    "USD_JPY", "USD_CHF", "AUD_JPY", "EUR_JPY",
]'''
assert s.count(old) == 1, 'screener anchor'
open(p, 'w').write(s.replace(old, new))
print('3. roster -> 8 pairs')

import py_compile
py_compile.compile(f'{ROOT}/src/scrooge_v3/gates/pip_eater_gate.py', doraise=True)
py_compile.compile(f'{ROOT}/src/scrooge_v3/market/screener.py', doraise=True)
json.load(open(cfgp))
print('compile + json OK')
