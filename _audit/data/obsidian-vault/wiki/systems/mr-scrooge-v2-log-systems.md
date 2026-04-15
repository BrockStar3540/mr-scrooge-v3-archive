---
type: system
status: active
tags: [scrooge, trading, logging, v2]
trust:
  score: 90
  confidence: high
  reason: Verified against running V2 bot configuration and log output
---

## Summary

Mr. Scrooge V2 produces four log files in `~/.openclaw/workspace/agents/mr-scrooge-v2/logs/`. The main log uses system-level logrotate; decision and trade logs use Python's RotatingFileHandler. Child loggers have `propagate=False` to prevent duplicate lines. Bot log P/L data is unreliable for non-USD-quote pairs (fixed 2026-04-09 but historical logs are tainted).

## Log Files

| File | Purpose | Rotation | Retention |
|---|---|---|---|
| `mrscroogev2.log` | Main bot output (cycles, errors, startup) | Daily via system logrotate (`/etc/logrotate.d/`) | 20 days |
| `decisions.log` | Signal evaluations, regime blocks, scoring details | RotatingFileHandler, 10MB max | 5 backups |
| `trades.log` | ENTRY, CLOSE, GREEN_EXIT, SL_LIMIT_FILL events | RotatingFileHandler, 10MB max | 5 backups |
| `launchd.log` | Startup and shutdown events | None | Manual cleanup |

## Logger Architecture

The bot uses Python's logging module with a parent-child hierarchy:

- **Parent:** `mr-scrooge-v2` --- writes to `mrscroogev2.log`
- **Child:** `mr-scrooge-v2.decisions` --- writes to `decisions.log`, `propagate=False`
- **Child:** `mr-scrooge-v2.trades` --- writes to `trades.log`, `propagate=False`

Setting `propagate=False` on child loggers prevents their messages from bubbling up to the parent handler. Without this, every decision and trade log line would appear twice: once in its dedicated file and once in the main log.

## Grep Recipes

### Errors in Main Log
```bash
grep -i 'error\|traceback\|exception' logs/mrscroogev2.log | tail -10
```

### Today's Trades
```bash
cat logs/trades.log
```

### Current Cycle
```bash
grep 'Cycle' logs/mrscroogev2.log | tail -1
```

### Regime Blocks
```bash
grep 'REGIME_BLOCKED' logs/decisions.log | tail -10
```

### New Scoring Factors (Layer 4)
```bash
grep 'ranging\|ct_pot\|ct_t1\|regime.*+10\|regime.*-10' logs/decisions.log
```

### Signal Ranking
```bash
grep 'RANKING' logs/decisions.log | tail -5
```

## OANDA Cross-Reference Warning

Bot logs are **secondary data**. The OANDA API is truth.

P/L figures in bot logs may be wrong for non-USD-quote pairs. A quote-currency conversion bug was fixed on 2026-04-09, but all historical log entries before that date are tainted. For any analysis requiring accurate P/L:

1. Pull closed trades from the OANDA v20 API (`/v3/accounts/{id}/trades?state=CLOSED`)
2. Use the `realizedPL` field (already in account currency)
3. Do not rely on bot-computed P/L from log files

This applies to both V1 and V2 logs.

## Key Takeaways

- Four log files serve distinct purposes: main (operations), decisions (scoring/regime), trades (entries/exits), launchd (lifecycle)
- `propagate=False` on child loggers is critical --- removing it causes every line to appear twice
- Historical bot log P/L is wrong for 17/21 non-USD-quote pairs (pre-2026-04-09). Always verify against OANDA API.
- Main log rotates daily via system logrotate (20 days). Decision and trade logs rotate at 10MB with 5 backups.
- The `decisions.log` is the best place to audit scoring behavior --- it contains per-signal score breakdowns and regime state

## Related

- [[Mr. Scrooge V2]]
- [[Mr. Scrooge Debugging Workflow]]
