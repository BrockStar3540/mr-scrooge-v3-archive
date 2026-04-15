# Mr. Scrooge Dashboard Operations

type: method
status: active
tags: [scrooge, trading, dashboard, workflow]

trust:
  score: 90
  confidence: high
  evidence:
    - source: production system review 2026-04-09
      type: firsthand

## Summary
Single Flask dashboard serving both V1 and V2 on port 8081 via Tailscale. The code lives in V1's workspace but the service is shared. Restarting it affects visibility for both bots.

## WARNING: Shared Service
`mr-scrooge-dashboard.service` is a SINGLE service that serves data for BOTH V1 and V2. Restarting or breaking it blinds monitoring for both bots simultaneously.

## Access
- **URL:** `https://[REDACTED-HOST]:8081`
- **Auth:** HTTP Basic Auth (401 on failure)
- **Network:** Tailscale only — not publicly routable

## Service
```bash
systemctl --user start|stop|restart|status mr-scrooge-dashboard.service
```

Unit file: `~/.config/systemd/user/mr-scrooge-dashboard.service`
- `WorkingDirectory`: V1's workspace (`~/.openclaw/workspace/agents/mr-scrooge/`)
- `ExecStart`: `~/mr_scrooge_env/bin/python3 dashboard.py`
- `Restart=always`, `RestartSec=5`

## Code Location
Both files live in V1's workspace:
- `~/.openclaw/workspace/agents/mr-scrooge/dashboard.py` — Flask app
- `~/.openclaw/workspace/agents/mr-scrooge/dashboard.html` — Template

V2 has `dashboard/templates/` but the main `dashboard.py` is in V1.

## What It Shows
- Account equity and daily PnL
- Open positions with unrealized PnL
- Decision log (entry signals, regime blocks, NO_TRADE reasons)
- Regime scores and signal breakdown
- Instrument screening status

## Editing
Since dashboard code lives in V1's workspace, follow [[Mr. Scrooge Edit and Deploy Workflow]] using V1's path. Remember: changes affect both V1 and V2 visibility.

### Score Breakdown Display (added 2026-04-09)
The dashboard now shows Layer 4 scoring components for each evaluated signal:
- `ranging`: red badge (-20) when 50H EMA slope is near zero
- `ct_pot`: CT + power_of_towers penalty (-15)
- `ct_jw`: CT + john_wick penalty (-5)
- `ct_t1` / `ct_t2`: CT tier adjustment (-10 / +5)
- `regime`: NORMAL +10 or CAUTION -10
- `z_align`: z-score alignment bonus (+5)

### Trend Classification Badges (planned)
Per-instrument badges showing trend state: "WT" (green), "CT" (red), "RNG" (orange). Implementation pending in Phase C dashboard updates.

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[Mr. Scrooge Debugging Workflow]]
