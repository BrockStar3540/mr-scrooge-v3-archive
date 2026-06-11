"""Wire (cell_hits, p_win) slot priority + raise p_win floor to 0.55.
1. pip_eater_gate: count matching cell-sides, stamp candidate.metadata['cell_hits']
2. scan_coordinator: rank survivors by (cell_hits, p_win)
3. pipeline._ledger: record cell_hits
4. .env: single LIGHTGBM_GATE_THRESHOLD=0.55 (remove stale dup lines)"""
import re

ROOT = '/home/ubuntu/mr-scrooge-v3'

# 1 — gate: hit count + metadata stamp
p = f'{ROOT}/src/scrooge_v3/gates/pip_eater_gate.py'
s = open(p).read()
old = """            _allow = self.cell_allowlist.get(strategy)
            if self.cell_allowlist:
                _hit = bool(_allow) and any(
                    int(_c[0]) == align_score and buckets.get(_c[1]) == _c[2]
                    and (len(_c) < 4 or _c[3] == direction)
                    for _c in _allow
                )
                if not _hit:"""
new = """            _allow = self.cell_allowlist.get(strategy)
            if self.cell_allowlist:
                # count of matching cell-sides: >=2 = multi-factor confirmation
                # (OOS +4.01p vs +2.21p single-hit) -> slot-priority signal.
                _hits = sum(
                    1 for _c in (_allow or [])
                    if int(_c[0]) == align_score and buckets.get(_c[1]) == _c[2]
                    and (len(_c) < 4 or _c[3] == direction)
                )
                try:
                    candidate.metadata["cell_hits"] = _hits
                except Exception:
                    pass
                if not _hits:"""
assert s.count(old) == 1, 'gate anchor'
open(p, 'w').write(s.replace(old, new))
print('1. gate patched')

# 2 — coordinator: rank by (cell_hits, p_win)
p = f'{ROOT}/src/scrooge_v3/core/scan_coordinator.py'
s = open(p).read()
old = """            # Re-rank survivors by p_win descending
            _scored.sort(key=lambda c: c.score, reverse=True)"""
new = """            # Re-rank survivors by (cell_hits, p_win) descending — a candidate
            # with more validated cell-sides vouching for it outranks a
            # single-hit one; p_win breaks ties (Brock 2026-06-11).
            _scored.sort(
                key=lambda c: (
                    int((getattr(c, "metadata", None) or {}).get("cell_hits", 0) or 0),
                    c.score,
                ),
                reverse=True,
            )"""
assert s.count(old) == 1, 'coordinator anchor'
open(p, 'w').write(s.replace(old, new))
print('2. coordinator patched')

# 3 — ledger: record cell_hits
p = f'{ROOT}/src/scrooge_v3/gates/pipeline.py'
s = open(p).read()
old = '                "align": meta.get("align_score"),'
new = '''                "align": meta.get("align_score"),
                "cell_hits": meta.get("cell_hits"),'''
assert s.count(old) == 1, 'ledger anchor'
open(p, 'w').write(s.replace(old, new))
print('3. ledger patched')

# 4 — .env: collapse to one threshold line at 0.55
p = f'{ROOT}/.env'
lines = open(p).read().splitlines()
out, done = [], False
for ln in lines:
    if re.match(r'#?\s*LIGHTGBM_GATE_THRESHOLD=', ln):
        if not done:
            out.append('LIGHTGBM_GATE_THRESHOLD=0.55  # raised 0.45->0.55 2026-06-11: corpus band [0.45,0.50) is +0.07p dead weight')
            done = True
        continue
    out.append(ln)
open(p, 'w').write('\n'.join(out) + '\n')
print('4. .env -> 0.55 (dup lines removed)')

import py_compile
for f in ('src/scrooge_v3/gates/pip_eater_gate.py', 'src/scrooge_v3/core/scan_coordinator.py', 'src/scrooge_v3/gates/pipeline.py'):
    py_compile.compile(f'{ROOT}/{f}', doraise=True)
print('all compile OK')
