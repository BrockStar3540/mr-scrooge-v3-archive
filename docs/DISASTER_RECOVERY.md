# DISASTER RECOVERY — from zero to running
*Scenario: laptop gone, EC2 gone. What you need: your logins. Updated 2026-06-11.*

## The three keys (memorize where they live, nothing else matters)
1. **GitHub login** → both repos (code, models, cells, configs — everything except secrets)
2. **Dropbox login** → `SCROOGE V3/Full Backup 1.0/` (includes `env.SECRETS` — the OANDA credentials)
3. **OANDA login** → fallback if Dropbox is also gone: regenerate an API token in the dashboard

## Path A — fastest to LIVE TRADING (~15 min): Dropbox alone
1. Any Linux box (or cloud VM). Download `SCROOGE V3/Full Backup 1.0/scrooge_v3_full_backup_1.0_*.tar.gz`.
2. Follow `RESTORE.md` inside it: untar → `mv env.SECRETS .env` → venv + `pip install -r requirements_frozen.txt` → systemd unit → start.
3. That snapshot IS the cell-book era bot: playbook, 157 cells, models, calendar, rails. Trading.

## Path B — GitHub only (no Dropbox): V3 repo + OANDA login (~25 min)
1. `git clone github.com/BrockStar3540/mr-scrooge-v3` — verified to track the playbook,
   p_win model, exit model, calendar, config, bucketizer (checked 2026-06-11).
2. Create `.env` from `.env.example` with a fresh OANDA token (OANDA dashboard → API).
3. venv (python3.12; lightgbm/xgboost/pandas/numpy), systemd unit from `deploy/`, start.
Caveat: repo is the hourly mirror — at most 1h behind the dead EC2.

## Path C — V4 repo (the future, NOT live trading yet)
`git clone github.com/BrockStar3540/mr-scrooge-v4` → `pip install -e .` →
`python3 runtime.py --status`. The golden self-checks verify models+features
survived transit; `--shadow` runs the full pipeline with the 157 cells
(cells/allowlist.json IS in the repo). V4 places no orders until the shadow
comparator earns cutover (V4_CHARTER.md rule 5). For money today: Path A or B.

## NOT needed to trade (lives on the Mini, rebuildable)
The 8yr corpus, M5 caches, lab research. Trading needs only what the repos/backup carry.

## What is nowhere in git (by design)
Secrets. `.env` is gitignored in both repos. Dropbox backup carries the practice
credentials inside the tarball; live-account credentials should only ever be
re-issued from the OANDA dashboard.
