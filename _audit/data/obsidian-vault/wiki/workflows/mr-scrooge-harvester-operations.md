# Mr. Scrooge Harvester Operations

type: method
status: active
tags: [scrooge, trading, harvester, workflow]

trust:
  score: 90
  confidence: high
  evidence:
    - source: production system review 2026-04-09
      type: firsthand

## Summary
The harvester is a separate daemon that polls OANDA every 30 seconds, closing partial positions at equity-percentage-based tier thresholds. Each version (V1, V2) has its own harvester service.

## Services

| Service | Bot | WorkingDirectory |
|---------|-----|-----------------|
| `mr-scrooge-harvester.service` | V1 | `~/.openclaw/workspace/agents/mr-scrooge/harvester/` |
| `mr-scrooge-v2-harvester.service` | V2 | `~/.openclaw/workspace/agents/mr-scrooge-v2/harvester/` |

Both: `Restart=always`, `RestartSec=15`, depends on parent bot service.

## Commands
```bash
# V1
systemctl --user start|stop|restart|status mr-scrooge-harvester.service

# V2
systemctl --user start|stop|restart|status mr-scrooge-v2-harvester.service
```

## How It Works
1. Polls OANDA account every 30 seconds
2. For each open position, checks unrealized PnL against account equity
3. If PnL exceeds tier threshold, closes a percentage and ratchets SL

## Tier Configuration
Stored in `harvester/harvester_config.json`:

```json
{
  "tier_equity_pcts": [0.015, 0.030, 0.045],
  "sl_lock_equity_pcts": [0.0, 0.015, 0.030],
  "close_pcts": [0.25, 0.25, 0.25],
  "pair_pip_overrides": {}
}
```

| Tier | Equity Gain % | Close % | SL Lock % | V1 Example (~$1,670) | V2 Example (~$88K) |
|------|--------------|---------|-----------|----------------------|---------------------|
| T1 | 1.5% | 25% | 0.0% | +$25 → close 25% | +$1,320 → close 25% |
| T2 | 3.0% | 25% | 1.5% | +$50 → close 25%, SL to T1 | +$2,640 → close 25% |
| T3 | 4.5% | 25% | 3.0% | +$75 → close 25%, SL to T2 | +$3,960 → close 25% |
| Runner | — | 25% stays | — | Rides to native TP2 | Rides to native TP2 |

## State File
`harvester/harvester_state.json` tracks which positions have been harvested at which tier. Prevents double-closing on restart.

## Stagnant Position Timeout
After 6 hours, if a position is profitable by at least 2 pips, the harvester sets a limit exit to free capital.

## Editing the Harvester
Follow [[Mr. Scrooge Edit and Deploy Workflow]]. The harvester is in its own subdirectory but shares the parent bot's `.env` credentials.

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge Architecture]]
- [[Mr. Scrooge Edit and Deploy Workflow]]
