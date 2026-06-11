# DISASTER RECOVERY — from zero to running
*Scenario: laptop gone, EC2 gone. What you need: your logins. Updated 2026-06-12 (V4 cutover).*

**As of 2026-06-11 21:13Z the LIVE trader is V4** (`mr-scrooge-v4`, systemd `mr-scrooge-v4.service`,
`runtime.py --live`). V3 still runs beside it as the order-muted shadow. Restore V4 first;
V3 is optional (shadow/comparison only).

## The three keys (memorize where they live, nothing else matters)
1. **GitHub login** → both repos (code, models, cells, configs — everything except secrets)
2. **Dropbox login** → `SCROOGE V3/Full Backup 2.0 (V4 cutover)/` (includes `env.SECRETS` — OANDA credentials)
3. **OANDA login** → fallback if Dropbox is also gone: regenerate an API token in the dashboard

## Path A — fastest to LIVE TRADING (~15 min): Dropbox alone
1. Any Linux box (or cloud VM). Download `SCROOGE V3/Full Backup 2.0 (V4 cutover)/scrooge_v4_*.tar.gz`.
2. Follow `RESTORE.md` beside it: untar → place `env.SECRETS` as `~/mr-scrooge-v3/.env`
   (V4 reads creds from that path via its env fallback) → venv (python3.12: lightgbm,
   xgboost, pandas, numpy, pyarrow, scikit-learn) → systemd unit (below) → start.
3. That snapshot IS the cutover-era machine: 423 cell-sides (8 pairs), p_win 0.55 floor,
   exit brain, severity + cooldown gates, spread guard, learning-loop crons. Trading.

## Path B — GitHub only (no Dropbox): V4 repo + OANDA login (~25 min)
1. `git clone github.com/BrockStar3540/mr-scrooge-v4` — tracks models (win_probability,
   severity, runner/exit), cells/allowlist.json, golden tests, calendar, pair plugins.
2. Create `.env` (OANDA_API_URL / OANDA_API_TOKEN / OANDA_ACCOUNT_ID) — fresh token from
   the OANDA dashboard. Put it at `~/mr-scrooge-v3/.env` or repo root.
3. venv + deps as above; verify with `python runtime.py --status` and the test suite.

## The systemd unit (user-level)
```ini
[Unit]
Description=Mr. Scrooge V4 Trading Platform (LIVE)
After=network-online.target
[Service]
WorkingDirectory=/home/ubuntu/mr-scrooge-v4
ExecStart=/home/ubuntu/mr_burns_env/bin/python3 runtime.py --live
Restart=always
RestartSec=15
Environment=PYTHONUNBUFFERED=1
[Install]
WantedBy=default.target
```
Control panel: `:8090/` · health JSON `:8090/health`. Learning-loop crons (UTC):
`25 1 * * * lab/run_labeler.py` · `10 2 * * * lab/run_nightly.py` · `30 2 * * * lab/shadow_compare.py`.

## V3 shadow (optional, for the live A/B)
Clone `mr-scrooge-v3`, same .env, its systemd unit PLUS `Environment=SCROOGE_SHADOW_MODE=1`
(without that line V3 places real orders — never run both unmuted).

## Sanity checklist after restore
- `curl :8090/health` → overall green (a RED model REFUSES to arm — that's by design)
- journal shows one JSON cycle line per minute, `views: 8`
- OANDA dashboard shows orders only from V4
