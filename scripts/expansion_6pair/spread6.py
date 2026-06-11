"""Live OANDA spread check for the 6 re-add candidate pairs (vs the assumed
spreads baked into scored_6pair net_ladder) + the 4 live pairs as reference.
Samples pricing every 10s x 12 (~2 min), reports median/p90 in pips."""
import json, time, urllib.request, statistics

env={}
for line in open('/home/ubuntu/mr-scrooge-v3/.env'):
    line=line.strip()
    if '=' in line and not line.startswith('#'): k,v=line.split('=',1); env[k]=v.split('  #')[0].strip()
API=env['OANDA_API_URL'].rstrip('/'); ACCT=env['OANDA_ACCOUNT_ID']
HDR={'Authorization':f"Bearer {env['OANDA_API_TOKEN']}"}
def get(u):
    for _try in range(4):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=HDR),timeout=30).read())
        except Exception as e:
            if _try==3: raise
            time.sleep(5)
def _unused(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=HDR),timeout=30).read())

ASSUMED={'USD_JPY':1.0,'USD_CHF':1.5,'EUR_JPY':1.5,'AUD_JPY':1.5,'EUR_GBP':1.5,'NZD_USD':1.8,
         'AUD_USD':None,'EUR_USD':None,'GBP_USD':None,'USD_CAD':None}
INSTS_ENC='%2C'.join(ASSUMED)
PIP=lambda p: 0.01 if p.endswith('_JPY') else 0.0001

samples={p:[] for p in ASSUMED}
for i in range(12):
    px=get(f"{API}/v3/accounts/{ACCT}/pricing?instruments={INSTS_ENC}")['prices']
    for q in px:
        p=q['instrument']
        bid=float(q['bids'][0]['price']); ask=float(q['asks'][0]['price'])
        samples[p].append((ask-bid)/PIP(p))
    if i<11: time.sleep(10)

print(f"{'pair':9} {'median':>7} {'p90':>6} {'max':>6} {'assumed':>8} {'delta':>7}")
for p in ['USD_JPY','USD_CHF','NZD_USD','EUR_JPY','AUD_JPY','EUR_GBP','AUD_USD','EUR_USD','GBP_USD','USD_CAD']:
    s=sorted(samples[p]); med=statistics.median(s)
    a=ASSUMED[p]
    d=f"{med-a:+7.2f}" if a else '   live'
    print(f"{p:9} {med:7.2f} {s[int(len(s)*0.9)]:6.2f} {s[-1]:6.2f} {a if a else '-':>8} {d}")
print(f"\nsampled {len(samples['USD_JPY'])}x over ~2min, ~20:30Z (NY afternoon; rollover 21-22Z widens)")
