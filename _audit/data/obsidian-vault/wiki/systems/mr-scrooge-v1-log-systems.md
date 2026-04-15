# Mr. Scrooge V1 Log Systems

type: system
status: active
tags: [scrooge, trading, logging, v1]

trust:
  score: 90
  confidence: high
  evidence:
    - source: code review and production log analysis 2026-04-09
      type: firsthand

## Summary
V1 has 4 log files, each serving a different purpose. Decisions and trades logs use RotatingFileHandler (10MB, 5 backups). The main log is rotated by system logrotate. Bot logs are secondary — OANDA API is the source of truth for trade outcomes.

## Log Files

All in `~/.openclaw/workspace/agents/mr-scrooge/logs/`:

| File | Logger Name | Content | Rotation |
|------|-------------|---------|----------|
| `mrscrooge.log` | `mr-scrooge` (root child) | Main bot output — universe scans, regime assessments, position management, errors | Daily logrotate, gzip, 20 days |
| `decisions.log` | `mr-scrooge.decisions` | Entry/exit decisions, scoring, ranking, regime blocks | RotatingFileHandler 10MB, 5 backups |
| `trades.log` | `mr-scrooge.trades` | Trade executions — entries, harvests, SL limit fills, closes with P/L | RotatingFileHandler 10MB, 5 backups |
| `launchd.log` | systemd capture | Startup/shutdown events, crashes | Daily logrotate |

Harvester has separate logs in `harvester/logs/`:
- `harvests.log` — tier fills, stagnant exits
- `launchd.log` — harvester startup

## Logger Configuration

Set up in `main.py` lines 70-88:
- Root logger: StreamHandler to stdout (captured by systemd → mrscrooge.log)
- `decision_log`: FileHandler → decisions.log, `propagate=False`
- `trade_log`: FileHandler → trades.log, `propagate=False`

The `propagate=False` setting (added 2026-04-09) prevents child loggers from bubbling up to the root handler, which was causing every decision/trade line to appear twice (once in decisions.log AND once in mrscrooge.log).

## What Goes Where

| Event | Log File | Example Line |
|-------|----------|-------------|
| Universe scan result | mrscrooge.log | `Screen EUR_USD: VIABLE` |
| Regime assessment | mrscrooge.log | `REGIME EUR_USD: CAUTION score=+1.0 \| box_contained(+1)` |
| Signal qualified | decisions.log | `EUR_USD: ENTER_SHORT \| zone=True ATR=True fork=True OTR=True` |
| Regime block | decisions.log | `EUR_USD: REGIME_BLOCKED score=-4.0 — entry suppressed` |
| Candidate ranking | decisions.log | `RANKING: 5 candidate(s) \| on_deck=GBP_USD score=44` |
| Position sizing | decisions.log | `EUR_USD: Margin-based sizing — equity $1604 \| units 54824` |
| Trade entry | trades.log | `ENTRY scrooge_eurusd507c27a7 \| EUR_USD SELL 54824 units @ 1.17020` |
| SL limit fill | trades.log | `SL_LIMIT_FILL scrooge_nzdusd3b6d3b4c \| fill=0.58498 sl=0.58526 pips_saved=2.8` |
| Trade close | trades.log | `EUR_USD CLOSE scrooge_eurusd507c27a7: OANDA native close \| RealizedPL: -82.78` |
| Position opened/closed | mrscrooge.log | `Position opened: scrooge_xxx \| EUR_USD SHORT @ 1.17020` |
| Errors | mrscrooge.log | `ERROR` or `Traceback` |

## Grep Recipes

```bash
cd ~/.openclaw/workspace/agents/mr-scrooge/logs

# Today's entries
grep 'ENTRY' trades.log | grep "$(date +%Y-%m-%d)"

# Today's closes with P/L
grep 'CLOSE' trades.log | grep "$(date +%Y-%m-%d)"

# Scoring breakdown (new Layer 3b modifiers)
grep 'ranging\|ct_pot\|ct_t1\|ct_t2\|z_align' decisions.log

# Regime blocks
grep 'REGIME_BLOCKED\|REGIME_FLOOR\|REGIME_HYSTERESIS' decisions.log | tail -20

# Regime scoring adjustments
grep 'regime.*+10\|regime.*-10' decisions.log

# Rankings (who's on deck)
grep 'RANKING' decisions.log | tail -10

# Errors (check after restart)
grep -i 'error\|traceback\|exception' mrscrooge.log | tail -10

# SL limit activity
grep 'SL_LIMIT\|sl_limit' mrscrooge.log | tail -10

# Specific instrument today
grep 'NZD_USD' decisions.log | grep "$(date +%Y-%m-%d)"
```

## OANDA API Cross-Reference

Bot logs can be wrong. The P/L calculation bug (fixed 2026-04-09) showed bot-logged P/L of -$124.90 for a trade that OANDA recorded as -$22.09. Always verify against OANDA:

```bash
# Pull today's fills from OANDA API
curl -s -H "Authorization: Bearer $OANDA_API_KEY" \
  "https://api-fxtrade.oanda.com/v3/accounts/$OANDA_ACCOUNT_ID/transactions?from=$(date -u +%Y-%m-%dT00:00:00Z)&type=ORDER_FILL"

# Check specific trade P/L
curl -s -H "Authorization: Bearer $OANDA_API_KEY" \
  "https://api-fxtrade.oanda.com/v3/accounts/$OANDA_ACCOUNT_ID/trades/{trade_id}"
```

OANDA credentials are in `.env` in the bot directory (LEVEL 4 — never in vault).

## Audit Methodology (Established 2026-04-09)

When analyzing bot performance:
1. Pull ALL closed trades from OANDA API (not bot logs)
2. Pull M15/H1 candles from OANDA to classify trend/ranging independently
3. Cross-reference OANDA fills with bot decision logs by client ID (scrooge_xxx)
4. Use OANDA's `realizedPL` as truth — bot's internal P/L may be wrong for non-USD-quote pairs

Audit data preserved at: `data/audit/scrooge_v1_audit.csv` and `data/audit/oanda_v1_fills.json`

## Key Takeaways

- decisions.log is the most useful log for understanding why the bot did or didn't enter
- trades.log shows actual executions with P/L
- mrscrooge.log is verbose — use grep, don't read end to end
- OANDA API is the source of truth for P/L, not bot logs
- After restart, always check mrscrooge.log for tracebacks

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V1 Pre-Edit Briefing]]
- [[Mr. Scrooge Debugging Workflow]]
