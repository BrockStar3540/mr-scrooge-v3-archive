"""Nightly lab — closes the learning loop (cron 02:00Z, after the labeler).
1. Join forward-labels to ledger candidates -> live-vs-corpus drift per cell-side.
2. Live p_win calibration check vs 1R outcomes.
3. Retrain/promotion gate: report-only until live labels >= 2,000 (then the
   retrain conversation happens with evidence, never auto-applied).
Writes wiki/systems/nightly-lab-report.md + one activity-log line."""
import json, os
from collections import defaultdict
from datetime import datetime, timezone

BASE = "/home/ubuntu/mr-scrooge-v3"
now = datetime.now(timezone.utc).isoformat(timespec='minutes')

labels = {}
if os.path.exists(f"{BASE}/data/candidate-ledger-labels.jsonl"):
    for line in open(f"{BASE}/data/candidate-ledger-labels.jsonl"):
        try:
            r = json.loads(line); labels[r['key']] = r
        except Exception: pass

recs = []
for line in open(f"{BASE}/data/candidate-ledger.jsonl"):
    try: recs.append(json.loads(line))
    except Exception: pass

def align_of(b):
    if not b: return None
    return ((b.get('T1')=='T1a')+(b.get('T4')=='T4a')
            +(b.get('H20') in ('H20a','H20b'))+(b.get('H60') in ('H60a','H60b')))

joined = []
for r in recs:
    key = f"{r['ts']}|{r['symbol']}|{r['strategy']}|{r['direction']}"
    if key in labels:
        joined.append((r, labels[key]))

lines = [f"# Nightly lab report — {now}", "",
         f"ledger records: {len(recs)} | forward-labeled: {len(joined)}", ""]

if joined:
    # p_win calibration on labeled candidates (1R first-touch basis)
    buckets = defaultdict(lambda: [0,0])
    cells = defaultdict(lambda: [0,0,0.0])
    for r, l in joined:
        pw = r.get('p_win'); ft = l.get('first_touch_1R')
        if pw is not None and ft in ('tp','sl'):
            b = min(int(pw*10), 9)
            buckets[b][0] += 1
            buckets[b][1] += (ft == 'tp')
        a = align_of(r.get('buckets'))
        if a is not None and ft in ('tp','sl'):
            k = (r['strategy'], a, r['direction'])
            cells[k][0] += 1; cells[k][1] += (ft=='tp'); cells[k][2] += l.get('mfe_pips',0)
    lines.append("## live p_win calibration (1R basis)")
    for b in sorted(buckets):
        n, w = buckets[b]
        if n >= 20:
            lines.append(f"- p_win {b/10:.1f}-{(b+1)/10:.1f}: n={n} live WR={100*w/n:.0f}%")
    lines.append("")
    lines.append("## top live (strategy, align, direction) keys by labeled volume")
    top = sorted(cells.items(), key=lambda kv: -kv[1][0])[:15]
    for (s,a,d),(n,w,mfe) in top:
        lines.append(f"- {s} a{a} {d}: n={n} WR={100*w/n:.0f}% avg_mfe={mfe/n:.1f}p")
else:
    lines.append("_No labels joined yet (labels begin 24h after ledger records)._")

gate = "OPEN — sufficient labels, schedule retrain review" if len(joined) >= 2000 else f"CLOSED — {len(joined)}/2000 labeled candidates"
lines += ["", f"## retrain/promotion gate: {gate}",
          "", "_Models are corpus-trained (through 2026-05-24). Corpus refresh = Mini pipeline (scored_7yr rebuild). Live retrain only after gate opens; promotion only if new model beats serving on live labels. Never auto-applied._"]

report = "\n".join(lines)
open("/data/obsidian-vault/wiki/systems/nightly-lab-report.md", "w").write(report + "\n")
with open("/data/obsidian-vault/wiki/systems/agent-activity-log.md", "a") as f:
    f.write(f"{now}Z [nightly-lab] ledger={len(recs)} labeled={len(joined)} gate={'OPEN' if len(joined)>=2000 else 'closed'} -> wiki/systems/nightly-lab-report.md\n")
print(f"report written: {len(recs)} records, {len(joined)} labeled, gate {gate}")
