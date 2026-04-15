# Trading Session Log Index

> Master index for per-session dev logs. Session-specific lessons, spread behavior, pair availability, and performance patterns.
>
> Format: `[DATE] [SESSION] — one-line summary -> logs/sessions/SESSION.md`

---

## Session Windows (UTC)

| Session | Open UTC | Close UTC | Primary Pairs |
|---------|----------|-----------|---------------|
| Sydney | 21:00 | 06:00 | AUD, NZD crosses |
| Tokyo | 00:00 | 09:00 | JPY crosses |
| London | 07:00 | 16:00 | EUR, GBP majors + crosses |
| New York | 13:00 | 22:00 | USD majors + crosses |

---

## Session Findings

- `[2026-03-31] [Sydney]` — Spread spikes common on Sunday open. 2-scan consistency gate prevents false blocks -> [logs/sessions/sydney.md](sessions/sydney.md)
- `[2026-03-31] [Tokyo]` — Thin session: probation pairs suppressed in balanced mode. Off-peak 50% size reduction -> [logs/sessions/tokyo.md](sessions/tokyo.md)
- `[2026-04-09] [London]` — Liquid session. Tight spreads. Baseline for spread spike detection (4x London = spike) -> [logs/sessions/london.md](sessions/london.md)
- `[2026-04-09] [New York]` — Overlap with London = peak liquidity. Most trade volume here -> [logs/sessions/new_york.md](sessions/new_york.md)
