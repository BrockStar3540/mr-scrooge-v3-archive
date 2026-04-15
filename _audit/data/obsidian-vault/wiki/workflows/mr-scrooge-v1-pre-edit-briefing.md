# Mr. Scrooge V1 Pre-Edit Briefing

type: method
status: active
tags: [scrooge, trading, onboarding, safety]

trust:
  score: 95
  confidence: high
  evidence:
    - source: production incidents from skipped steps, 2026-02 through 2026-04
      type: firsthand

## Summary
Read this before touching any V1 code. Mr. Scrooge V1 trades real money on OANDA. A bad edit can lose money in minutes. This document tells you what you need to know, where everything is, and what will break the bot.

## What the Bot Does

Mr. Scrooge is a box-theory mean-reversion forex bot. It identifies the previous day's high/low (PDH/PDL), waits for price to reach those walls, enters reversal trades when candle patterns confirm, then manages the position with a ratcheting stop-loss, tiered profit harvesting, and limit order exits. It runs a 5-minute decision cycle and trades up to 21 currency pairs on a live OANDA account.

## Where Everything Lives

| What | Location |
|------|----------|
| **Source code (truth)** | EC2: `~/.openclaw/workspace/agents/mr-scrooge/` |
| **GitHub backup** | `BrockStar3540/mr-scrooge` (private, own fine-grained PAT) |
| **Alien Device backup** | `/Volumes/Alien Device/mr-scrooge/` (push from EC2) |
| **Bot service** | `systemctl --user {start\|stop\|restart\|status} mr-scrooge.service` |
| **Harvester service** | `systemctl --user ... mr-scrooge-harvester.service` |
| **Dashboard service** | `systemctl --user ... mr-scrooge-dashboard.service` (SHARED with V2!) |
| **Logs** | `logs/mrscrooge.log`, `logs/decisions.log`, `logs/trades.log` |
| **OANDA credentials** | `.env` in bot dir (never in vault, never in git) |
| **Config** | `main.py` CONFIG dict (not config.json — that's legacy) |

## Key Files

| File | What It Does | Size |
|------|-------------|------|
| `main.py` | Main loop, entry ranking, regime injection, position sizing | 84KB |
| `gates.py` | All signal gates + scoring function (`_calculate_score`) | 132KB |
| `portfolio/trade_manager.py` | Position lifecycle, P/L calculation, ratchet stages | 34KB |
| `core/oanda_client.py` | OANDA REST API wrapper | 32KB |
| `core/execution_router.py` | Order routing (market + limit) | 10KB |
| `core/fee_calculator.py` | Spread cost breakdown | 12KB |
| `harvester/main.py` | Profit extraction daemon (separate service) | 23KB |
| `regime/supervisor.py` | Regime assessment (blocks/restricts entries) | ~15KB |
| `dashboard.py` + `dashboard.html` | Web dashboard on port 8081 | 86KB combined |

## Three Things That Will Break the Bot

### 1. Dataclass Field Ordering in trade_manager.py
`OpenPosition` is a `@dataclass`. Fields with defaults (like `pip_value_per_unit: float = 1.0`) MUST come after fields without defaults. Adding a default field in the wrong position crashes Python on import. All default fields live after line 76.

### 2. Stale __pycache__
Python caches compiled `.pyc` files. After editing any `.py` file, you MUST clear the cache:
```bash
find ~/.openclaw/workspace/agents/mr-scrooge -name '*.pyc' -delete
```
Without this, the bot runs OLD code from cache.

### 3. Dashboard Is Shared
`mr-scrooge-dashboard.service` serves BOTH V1 and V2. Restarting it affects both bots' dashboards. Editing `dashboard.py` or `dashboard.html` affects both.

## Required Reading (in this order)

1. This document (you're reading it)
2. [[Mr. Scrooge V1]] — bot registration, services, modules
3. [[Mr. Scrooge V1 Scoring System]] — how entries are scored and ranked
4. [[Mr. Scrooge Known Defects]] — what's broken and what's been fixed
5. [[Mr. Scrooge Edit and Deploy Workflow]] — step-by-step deploy procedure

## How to Make a Change

1. SSH to EC2: `ssh -i ~/.ssh/openclaw-key.pem ubuntu@[REDACTED-IP]`
2. Edit the file in `~/.openclaw/workspace/agents/mr-scrooge/`
3. Clear pycache: `find . -name '*.pyc' -delete`
4. Stop bot: `systemctl --user stop mr-scrooge.service`
5. Start bot: `systemctl --user start mr-scrooge.service`
6. Check logs: `tail -20 logs/mrscrooge.log` — look for tracebacks
7. Watch one full cycle (5 min): confirm "RANKING" lines appear in `logs/decisions.log`
8. Commit: `git add <files> && git commit -m "description"`
9. Push: `git push origin main` (GitHub) — Alien Device push may be automatic

See [[Mr. Scrooge Edit and Deploy Workflow]] for the full procedure.

## How to Document a Change

- **Code change:** Append dated section to EC2 `NOTES.md` in bot dir
- **Bug found/fixed:** Update [[Mr. Scrooge Known Defects]] in vault
- **Scoring change:** Update [[Mr. Scrooge V1 Scoring System]] — requires OANDA data audit
- **Architecture change:** Update [[Mr. Scrooge Architecture]] in vault
- See [[Mr. Scrooge Changelog Process]] for the full documentation rules

## Emergency: How to Stop the Bot

```bash
# Stop immediately — open positions keep their OANDA native SL/TP
systemctl --user stop mr-scrooge.service

# Check if positions are protected
# Log into OANDA web/app — every open trade should have SL and TP orders

# Roll back to last known good code
cd ~/.openclaw/workspace/agents/mr-scrooge
git log --oneline -5          # find the good commit
git checkout <commit> -- .    # restore files
find . -name '*.pyc' -delete
systemctl --user start mr-scrooge.service
```

The bot uses OANDA native SL/TP orders. If the bot crashes, open positions are still protected by OANDA's server-side stop-loss and take-profit. The only risk is no new entries — existing positions are safe.

## Key Takeaways

- EC2 is the source of truth — edit there, push one-way to GitHub and Alien Device
- Clear pycache after every edit
- The scoring system was calibrated from OANDA data — don't change point values without a new audit
- The dashboard is shared with V2 — restart carefully
- When in doubt, stop the bot. Native SL/TP protects open positions.

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V1 Scoring System]]
- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge Changelog Process]]
