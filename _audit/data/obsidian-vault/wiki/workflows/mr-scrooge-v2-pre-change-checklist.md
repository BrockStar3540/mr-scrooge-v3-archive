---
type: workflow
status: active
tags: [scrooge, trading, workflow, safety, v2]
trust:
  score: 95
  confidence: high
  reason: Distilled from multiple production incidents and the 2026-04-09 audit process
---

## Summary

The read-before-you-touch doc for Mr. Scrooge V2. If you are about to change anything in the V2 codebase, read this first. It covers what the bot does, where everything lives, what will break it, and how to make changes safely.

## 1. What the Bot Does

Mr. Scrooge V2 is a box theory forex reversal bot. It identifies support/resistance boxes on multiple timeframes, scores potential reversal signals through a four-layer system, and enters trades with native OANDA stop-loss and take-profit orders. It runs on an OANDA practice account.

## 2. Where Everything Is

| Location | Purpose | Access |
|---|---|---|
| EC2 `~/.openclaw/workspace/agents/mr-scrooge-v2/` | **Source of truth** --- live code | SSH with openclaw-key.pem |
| GitHub `BrockStar3540/mr-scrooge-v2` | History and collaboration | `git push origin main` |
| Alien Device `/Volumes/Alien Device/mr-scrooge-v2/` | Offline backup | Mount on Mac Mini |

## 3. Code Flow

```
EC2 (truth) --> GitHub (history) --> Alien Device (backup)
```

One-way only. Never edit on GitHub or Alien Device and push back to EC2.

## 4. Key Files

| File | Role | Lines (approx) |
|---|---|---|
| `coordinator.py` | Orchestrator --- cycle loop, regime enforcement, ranking, entry decisions | ~1372 |
| `signals/engine.py` | Scoring, gate evaluation, signal generation | Large |
| `gates/` | 6 gate directories (trend, volatility, session, structure, momentum, spread) | Varies |
| `positions/manager.py` | Post-entry position management (green exits, SL adjustments) | Medium |
| `config.py` | All configurable parameters (SL/TP pips, margin, thresholds) | Medium |

## 5. Three Things That Will Break the Bot

### (a) Editing Without Clearing `__pycache__`

Python caches compiled bytecode in `__pycache__/` directories. If you edit a `.py` file but do not clear the cache, the bot may run stale code. Symptoms: your change appears to have no effect, or the bot behaves inconsistently.

**Fix:** After any edit, run:
```bash
find ~/.openclaw/workspace/agents/mr-scrooge-v2/ -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
```

### (b) Adding Dataclass Fields in Wrong Order

Python dataclasses require fields without defaults to come before fields with defaults. Adding a non-default field after a default field causes a `TypeError` at import time and the bot will not start.

### (c) Restarting `mr-scrooge-dashboard.service`

The dashboard service is shared between V1 and V2. Restarting it affects both bots' monitoring. Do not restart it unless you intend to affect both.

## 6. Scoring Calibration Warning

The scoring system was calibrated from OANDA trade data on 2026-04-09. The point values in Layer 4 (OANDA truth) are empirically derived from 511 V1 + 58 V2 closed trades. Do not change point values without re-running the audit against current OANDA data.

## 7. How to Make a Change

1. **Stop the service:** `systemctl --user stop mr-scrooge-v2.service`
2. **Edit on EC2:** Make your changes to the source files
3. **Clear pycache:** `find ~/.openclaw/workspace/agents/mr-scrooge-v2/ -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null`
4. **Start the service:** `systemctl --user start mr-scrooge-v2.service`
5. **Tail logs for 10+ minutes:** `tail -f ~/.openclaw/workspace/agents/mr-scrooge-v2/logs/mrscroogev2.log`
6. **Verify:** Check for errors, confirm scoring active, confirm regime state loading
7. **Commit:** `cd ~/.openclaw/workspace/agents/mr-scrooge-v2/ && git add -A && git commit -m "description"`
8. **Push:** `git push origin main` and sync to Alien Device

## 8. How to Document

| What | Where |
|---|---|
| Session log / timeline | EC2 bot `NOTES.md` (append dated section) |
| Structured knowledge | Obsidian vault (wiki/systems/, wiki/workflows/) |
| Bug tracking | Vault `mr-scrooge-known-defects.md` |
| Code history | Git commits (atomic, descriptive messages) |

Never duplicate the same information across all three. Each has its role.

## 9. Emergency Procedures

**Immediate stop:**
```bash
systemctl --user stop mr-scrooge-v2.service
```

Open positions are protected by native OANDA SL/TP orders. Stopping the bot does not remove those orders. Positions will close at their SL or TP levels.

**Rollback to pre-audit state:**
```bash
cd ~/.openclaw/workspace/agents/mr-scrooge-v2/
git checkout pre-audit-backup -- .
```

## 10. Required Reading

Before making changes, read these vault documents:

- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V2 Scoring System]]
- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge V2 Regime System]]

## Key Takeaways

- EC2 is the source of truth. GitHub is history. Alien Device is backup. Never reverse the flow.
- Always clear `__pycache__` after editing any `.py` file, or your changes may not take effect
- Scoring point values are empirically calibrated --- do not change them without an OANDA data audit
- Native OANDA SL/TP protects open positions even if the bot is stopped
- Tail logs for at least 10 minutes after any restart to catch delayed errors

## Related

- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V2 Scoring System]]
