"""Forward-labeler — turns the candidate ledger into labeled counterfactuals.
Daily cron (01:15 UTC). For each ledger record >=24h old and not yet labeled:
fetch M5 candles from entry ts forward 24h, compute first-touch outcome at the
record's own stop distance (TP = same distance, the 1R race), plus MFE/MAE in
pips — the path labels. Appends to data/candidate-ledger-labels.jsonl.
Read-only vs the bot; OANDA practice API; safe to re-run (idempotent by key)."""
import json, os, time, urllib.request
from datetime import datetime, timedelta, timezone

BASE_DIR = "/home/ubuntu/mr-scrooge-v3"
LEDGER = f"{BASE_DIR}/data/candidate-ledger.jsonl"
LABELS = f"{BASE_DIR}/data/candidate-ledger-labels.jsonl"

env = {}
for line in open(f"{BASE_DIR}/.env"):
    line = line.strip()
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1); env[k] = v
API = env["OANDA_API_URL"].rstrip("/")
HDR = {"Authorization": f"Bearer {env['OANDA_API_TOKEN']}"}

def get(url):
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=30).read())

done = set()
if os.path.exists(LABELS):
    for line in open(LABELS):
        try: done.add(json.loads(line)["key"])
        except Exception: pass

cutoff = datetime.now(timezone.utc) - timedelta(hours=24)
candles_cache = {}
out = open(LABELS, "a")
n_new = 0
for line in open(LEDGER):
    try: r = json.loads(line)
    except Exception: continue
    key = f"{r['ts']}|{r['symbol']}|{r['strategy']}|{r['direction']}"
    if key in done: continue
    ts = datetime.fromisoformat(r["ts"])
    if ts > cutoff: continue
    entry, stop = r.get("entry"), r.get("stop")
    if not entry or not stop: continue
    pip = 0.01 if "JPY" in r["symbol"] else 0.0001
    risk = abs(entry - stop)
    sign = 1 if r["direction"] == "long" else -1
    ck = (r["symbol"], r["ts"][:13])
    if ck not in candles_cache:
        frm = ts.strftime("%Y-%m-%dT%H:%M:%SZ")
        try:
            candles_cache[ck] = get(f"{API}/v3/instruments/{r['symbol']}/candles?granularity=M5&from={frm}&count=288&price=M")["candles"]
        except Exception:
            candles_cache[ck] = None
        time.sleep(0.15)
    candles = candles_cache[ck]
    if not candles: continue
    mfe = mae = 0.0; first = "none"
    for c in candles:
        hi, lo = float(c["mid"]["h"]), float(c["mid"]["l"])
        fav = (hi - entry) * sign / pip if sign > 0 else (entry - lo) / pip
        adv = (entry - lo) / pip if sign > 0 else (hi - entry) / pip
        mfe, mae = max(mfe, fav), max(mae, adv)
        if first == "none":
            hit_tp = fav >= risk / pip
            hit_sl = adv >= risk / pip
            if hit_tp and hit_sl: first = "both_same_bar"
            elif hit_tp: first = "tp"
            elif hit_sl: first = "sl"
    out.write(json.dumps({"key": key, "symbol": r["symbol"], "strategy": r["strategy"],
        "direction": r["direction"], "align": r.get("align"), "p_win": r.get("p_win"),
        "passed": r.get("passed"), "rejection": (r.get("rejection") or "")[:60],
        "risk_pips": round(risk/pip, 1), "first_touch_1R": first,
        "mfe_pips": round(mfe, 1), "mae_pips": round(mae, 1)}) + "\n")
    n_new += 1
out.close()
print(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} labeled {n_new} new candidates")
