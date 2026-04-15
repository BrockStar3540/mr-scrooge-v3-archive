# Mr. Scrooge Debugging Workflow

type: method
status: active
tags: [scrooge, trading, workflow, debugging]

trust:
  score: 90
  confidence: high
  evidence:
    - source: used in production debugging 2026-04-07/09
      type: reproducible

## Summary
How to investigate Mr. Scrooge issues: service status, log locations, data files, dashboard, and common problems with their fixes.

## Service Status Commands

```bash
# All 5 Scrooge-related services
systemctl --user status mr-scrooge.service
systemctl --user status mr-scrooge-v2.service
systemctl --user status mr-scrooge-harvester.service
systemctl --user status mr-scrooge-v2-harvester.service
systemctl --user status mr-scrooge-dashboard.service
```

## Log Files

### V1 Logs
All in `~/.openclaw/workspace/agents/mr-scrooge/logs/`:

| File | Content | Check For |
|------|---------|-----------|
| `mrscrooge.log` | Main bot output | Tracebacks, cycle lines, equity |
| `decisions.log` | Entry/exit decisions | ENTER_SHORT, NO_TRADE, REGIME_BLOCKED |
| `trades.log` | Trade executions | ENTRY, CLOSE, PnL |
| `launchd.log` | Startup/shutdown | Boot errors, version info |

### V2 Logs
Same structure in `~/.openclaw/workspace/agents/mr-scrooge-v2/logs/` with `mrscroogev2.log`.

### Useful Log Searches
```bash
# Recent errors
grep -i 'error\|traceback' .../mrscrooge.log | tail -10

# Today's trades
cat .../trades.log

# Current cycle info
grep 'Cycle' .../mrscrooge.log | tail -1

# Regime blocks
grep 'REGIME_BLOCKED' .../mrscrooge.log | tail -10

# Position opens/closes
grep -E 'ENTRY|EXIT|Position closed' .../mrscrooge.log | tail -20

# New scoring factors
grep 'ranging\|ct_pot\|ct_t1\|regime.*+10\|regime.*-10' .../decisions.log
```

## Dashboard
- **URL:** `https://[REDACTED-HOST]:8081`
- Requires Tailscale connection + HTTP Basic Auth
- Shows: equity, positions, decisions, regime scores, instrument status

## Data Files to Inspect

| File | Location | Content |
|------|----------|---------|
| `data/status.json` | Both V1/V2 | Live cycle snapshot (equity, positions, health) |
| `data/entry-context.jsonl` | V1 | Entry decision context for quality analysis |
| `data/regime-protests.jsonl` | V1 | Regime supervisor objections |
| `data/entry-context.jsonl` | V2 | Entry decision context (outcomes populated) |
| `data/regime-protests.jsonl` | V2 | Regime supervisor observations + blocks |
| `data/audit/` | Both | OANDA trade exports from 2026-04-09 audit |
| `harvester/harvester_state.json` | Both | Harvest watermarks (prevents double-close) |
| `harvester/harvester_config.json` | Both | Tier thresholds, pip overrides |

## Common Issues

### Bot not trading (0 positions, no ENTER signals)
1. Check if market is open (forex closes Fri 5pm ET to Sun 5pm ET)
2. Check instrument count in cycle line — should be 8-21
3. Check decisions.log for NO_TRADE reasons (RR too low? OTR too high?)
4. Check if all pairs are REGIME_BLOCKED

### Repeated errors in log
1. `AttributeError` — check if recent code change broke an interface
2. `404 Client Error` — OANDA order expired, check SL limit system (see [[SL Limit Order System]])
3. `Unhandled error` — exception in process_instrument, non-fatal but pair is skipped

### Harvester not closing positions
1. Check harvester service: `systemctl --user status mr-scrooge-harvester.service`
2. Check harvester_state.json — is the position watermarked?
3. Check harvester_config.json — are tier thresholds reasonable?
4. Check if position equity gain meets T1 threshold (1.5% of account)

### Position stuck open for hours
1. Check if TP2 is far from current price (may need patience)
2. Check if harvester is running (stagnant position timeout = 6 hours)
3. Manual close: use OANDA web/app if needed — bot will detect "OANDA NATIVE CLOSE"

### Dashboard not loading
1. Check service: `systemctl --user status mr-scrooge-dashboard.service`
2. Check Tailscale connection to EC2
3. Dashboard code is in V1 workspace: `dashboard.py` + `dashboard.html`

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V2 Log Systems]]
- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[SL Limit Order System]]
