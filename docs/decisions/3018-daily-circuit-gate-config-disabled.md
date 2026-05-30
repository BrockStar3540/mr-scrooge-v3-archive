# 3018. DailyCircuitGate config-disabled — alerting carries the safety

**Status:** Accepted
**Date:** 2026-05-28
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

The `DailyCircuitGate` was hard-coded into `register_many` and emitting FAILED log lines on every scan even after `enabled=false` in config. During the $5,350 losing-streak recovery, the gate was tripped at day-start and the trip state persisted across reboots, leaving the bot frozen even after the underlying issue was fixed.

Meanwhile the Telegram drawdown alerter (ADR 3007) had been live for weeks providing equivalent protection out-of-band.

## Decision

Honor `gates.daily_circuit.enabled=false` in config: when disabled, `DailyCircuitGate` is not registered into the pipeline at all (vs. previously being registered and stuck in observe mode spamming FAILED lines).

Set `enabled=false` in `config/default.json`. Drawdown alerter carries the safety net.

## Alternatives considered

- **Fix the trip-state-persists-across-reboots bug instead of disabling** — partially separate fix landed earlier (the 2026-04-28 daily circuit roll fix, commit 5db12f1); but the gate's value-add over the alerter is marginal once alerting is reliable.
- **Keep registered in observe mode** — rejected. Was spamming FAILED log lines that confused live debugging.
- **Remove the class entirely** — rejected. Config-flippable revival is cheap; deleting means a code restore to bring it back.

## Consequences

- No more daily-circuit FAILED noise in journal.
- Drawdown protection now solely on the Telegram alerter; if the alerter fails, we lose this layer.
- Boot log emits `[BOOT] DailyCircuitGate DISABLED via config` to confirm intentional state.

## Cross-references

- Tasks #24 (clear trip + disable), #28 (lack-of-trades diagnosis)
- Commit: `5db12f1` (earlier daily circuit roll fix), bootstrap.py registration changes 2026-05-28
- ADR 3007 (drawdown alerter)
