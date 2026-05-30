# 3007. Telegram drawdown alerting via 5-minute systemd timer

**Status:** Accepted
**Date:** 2026-05-04
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

After the 48h losing streak (ADR 3017 context), it became clear we needed out-of-band drawdown alerts that don't depend on the bot itself being healthy. If the bot is sick (silent crash, stuck circuit, broker auth failure), the bot can't be the one telling us.

## Decision

A separate `scrooge-drawdown-alert.timer` (systemd user-level timer) fires every 5 minutes and runs an alerter script that:
1. Reads `data/positions.json` + `data/daily_circuit.json` + broker equity directly
2. Computes daily P&L and cumulative drawdown
3. Sends Telegram alerts on:
   - Daily P&L ≤ −2.7%
   - Cumulative drawdown ≤ −6.5%
   - Service paused or circuit-tripped
   - Service down (process not running)
4. Dedup state persisted at `data/alert_state.json` to avoid spam

Independent of the main bot process. Alerts continue even if `mr-scrooge-v3.service` is down.

## Alternatives considered

- **In-process alerter** — rejected. Defeats the purpose; can't alert when the bot is the thing failing.
- **Separate Python daemon** — rejected. Systemd timer is simpler, no auto-restart logic to maintain.
- **External SaaS uptime monitor** — rejected. Adds a third-party dependency for what is a 50-line script.

## Consequences

- Alert-driven catch of the next two extended drawdowns vs eyeballing the dashboard.
- 5-min granularity is the right cadence (cheap, sub-circuit-trip-detectable).
- `alert_state.json` dedup means no spam, but also means resetting the file is needed after intentional pauses.

## Cross-references

- Vault: `wiki/projects/scrooge-v3-dbb-loser-audit.md`
- Vault: `wiki/postmortems/fixes/scrooge-bug-fix-arc-2026-05-25.md`
- Systemd unit: `~/.config/systemd/user/scrooge-drawdown-alert.timer`
