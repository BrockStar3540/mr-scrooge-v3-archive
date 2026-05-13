# LLM Textbook Trade Lab v0

This lab tests Brock's idea: use an LLM as a trade designer / chart-reader, then reverse-engineer winning historical chart trades into deterministic microstrategies.

Files:
- `generate_contexts_fast.py` — creates blind historical chart contexts from M5 data.
- `contexts/` — 12 blind pre-decision chart dossiers.
- `trade_plans_v0.jsonl` — Codex-designed blind TAKE/SKIP plans.
- `score_trade_plans.py` — bid/ask forward scorer for the blind plans.
- `textbook_trade_scores.csv` — blind batch scoring; 6 TAKEs, 6 stops.
- `winner_seed_events.csv` — known clean raw-M5 winners used for reverse engineering.
- `textbook_winner_reverse_engineering_v0.md` — first three drafted textbook techniques.

Key lesson:
Random textbook-looking contexts are not enough. Winner-first reverse engineering is the useful workflow.
