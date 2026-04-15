# Mr. Scrooge V2 Dashboard Operations

type: method
status: active
tags: [scrooge, trading, dashboard, workflow, v2]

trust:
  score: 90
  confidence: high
  evidence:
    - source: production deployment 2026-04-09
      type: firsthand

## Summary
V2 has its own independent Flask dashboard on port 8084 via Tailscale. Completely separate from V1's dashboard on port 8081. No shared code, no shared service.

## Access
- **URL:** `https://[REDACTED-HOST]:8084`
- **Auth:** HTTP Basic Auth (same credentials as V1)
- **Network:** Tailscale only — not publicly routable

## Service
```bash
systemctl --user start|stop|restart|status mr-scrooge-v2-dashboard.service
```

- **WorkingDirectory:** `~/.openclaw/workspace/agents/mr-scrooge-v2/`
- **ExecStart:** `~/mr_burns_env/bin/python3 dashboard.py`
- **Port:** 8084 (V1 is 8081)
- **Restart:** always, 5s delay

## Code Location
Both files live in V2's workspace (NOT shared with V1):
- `~/.openclaw/workspace/agents/mr-scrooge-v2/dashboard.py` — Flask app (adapted from V1)
- `~/.openclaw/workspace/agents/mr-scrooge-v2/dashboard.html` — Template

## Data Pipeline
The dashboard reads from `data/status.json` which is written by `status.py` every 5-minute cycle. Key data:

| Data | Source | Format |
|------|--------|--------|
| Signals | coordinator.py signal evaluation | Rich gate objects (zone.tier, atr.consumed_pct, etc.) |
| Score detail | signals/engine.py _score() | Per-component breakdown dict |
| Box states | coordinator.py from box_machine.states | All initialized instruments (not just viable) |
| Screen results | coordinator.py _serialize_screen() | 12 fields including half_box, ATR, spread, OTR |
| Sessions | coordinator.py _update_sessions() | Set at boot + updated on hour change |
| Regime | /api/regime-summary from regime-protests.jsonl | Blocked/restricted/clean counts |
| Market summary | status.py from validity_detail | Valid/rejected counts + top rejection reasons |

## Score Breakdown Display
Signal cards show Layer 4 scoring components:
- `zone`, `atr`, `otr`, `rr`, `pattern` — base scoring
- `z_edge`, `bb_edge`, `structure`, `gap` — contextual
- `ranging`, `ct_pot`, `ct_jw`, `ct_t1`, `ct_t2`, `z_align`, `regime` — OANDA truth adjustments

## Important Notes
- Signals evaluate even at max_positions (for dashboard visibility)
- Box states show all initialized instruments, not just currently viable
- Screen results can show slightly different OTR than V1 due to spread sampling timing (both bots sample independently)

## Related
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V2 Scoring System]]
- [[Mr. Scrooge Debugging Workflow]]
