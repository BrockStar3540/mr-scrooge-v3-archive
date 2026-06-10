# Scrooge / MLs / Backtester — Location Index (2026-06-10)

Four homes: **EC2** = the live bot. **Mini/Alien Drive** = the lab + backtester + corpora.
**Dropbox** = per-session work history. **Vault (EC2)** = the wiki knowledge base.
**MBP** = dev clones.

---

## 1. EC2 — THE LIVE BOT  (`ssh ubuntu@[REDACTED-IP]:~/mr-scrooge-v3`, git `main`)

### `src/scrooge_v3/` — bot source
- **`core/`** (19) — the runtime. `runtime.py` (conductor), `scan_coordinator.py` (candidate gen → LightGBM p_win re-rank → best pick), `scan_pipeline.py`, `execution_coordinator.py` (order place + sizing), `position_coordinator.py` (applies exit decisions), `position_pipeline.py`, `state_controller.py`/`state.py` (→ `state.json`), `strategy_router.py`, `bootstrap.py` (wires gates/strats), `runtime_context.py` (ctx: features, known_trade_ids), `types.py` (TradeCandidate/GateResult/GateMode), `trade_geometry.py`, `config.py`.
- **`gates/`** (36) — the entry funnel. **`pipeline.py`** (gate runner), **`pip_eater_gate.py`** ← THE EV gate (playbook cells, align_score, amp bucket, ADR gate, **htf-misalign gate**, pair_blocklist), **`htf_trend_filter.py`** (daily directional bias, observe mode), `cooldown.py`, `debounce.py`, `expiry_backoff.py`, `feature_quality_floor.py`, `spread.py`, `daily_circuit.py`. Rest are legacy/shadow (matrix_*, regime_*, entry_filter_*, box_v3_shadow, ml_strategy_filter…).
- **`management/`** (9) — exits. **`green_exit.py`** ← THE exit manager: TP ladder (+12/+20/+30), 4h→**2h stale-green harvest**, **ATR-collapse** dead-zone exit, **exit-brain** TAKE/RIDE (`rem_mfe`).
- **`features/`** (16) — feature math. **`matrix_features.py`** ← the 14-factor signature + htf (the file we unfroze), `atr.py`, `bollinger.py`, `ema.py`, `rsi.py`, `technical_regime_53.py`, `zone_detector.py`, `range_builder.py`.
- **`advisors/`** — **`lightgbm_shadow.py`** (the v0 p_win scorer load+predict), `branch_router.py`, and **`ml_observer/`** (live self-training shadow ML: `observer.py`, `trainer.py`, `features.py`, `per_pair_modules.py`, `shadow.py`, `oanda_poll.py`).
- **`strategies/`** (15) — the signal generators (alpha/bravo/charlie/delta/echo + the cut families).
- **`execution/`** (6) — `position_tracker.py`, `sizing.py` (risk-cap), order exec.
- **`market/`** (7) — `oanda_adapter.py` (broker API).
- **`services/`** — **`state_recovery.py`** (vanished-trade reconcile → cooldown/blacklist; the daily-delta mis-classification lives here), `config_watcher.py`, `dashboard_bridge.py`.
- **`risk/`** — `cooldown_tracker.py` (cooldowns/blacklist/circuit in-memory).
- **`telemetry/`** (12) — `execution_audit.py`, order-attribution.  **`classifiers/`**, `context/`, `dashboard/`.

### `data/` — live data + the MODELS
- **`playbook_ev_pairaware.csv`** ← THE EV cells: `pair,strategy,direction,align,tier,bucket,n,ev_pips,amp_factor,floor,adr_gated`. The gate's keep/drop source (now direction-keyed).
- **`lab_training/v0/`** ← **LightGBM p_win GATE SCORER**: `model.txt`, `feature_meta.json` (18 feat incl direction_exec), `train_report.json`.
- **`exit-model/`** ← **EXIT BRAIN**: `exit_model.xgb`/`.pkl` (rem_mfe predictor), `exit_model_meta.json`, `exit_ml_corpus.parquet`.
- **`ml-observer/`** ← **live SHADOW ML**: `model.xgb` (advisory, self-trains), `observer-state.json`, `scans.jsonl`+`outcomes.jsonl` (train stream), `actions/account/bot-logs.jsonl`, `shadow-*.json`. (flushed 2026-06-09).
- **`per_pair_modules_phase3/`** ← 27 per-pair regime modules: `regime_centroids.csv`, `regime_session_wl_grid.csv`, `strategies.json`, `lib/build_pair_module.py`.
- **`lab_matrix/`** — **`factor_buckets.py`** ← THE bucketizer (H20/H60/T1/T4 + amp), `factor_catalog.py`, `optimized_matrix.csv` (research matrix, has direction).
- **state** — `state.json`, `cooldowns.json`, `zone_blacklist.json`, `daily_circuit.json`, `positions.json`, `limit_expiry_tracker.json`, `harvest-order-ledger.json`.
- `corpus_8yr.parquet` (repo root) — the validated 4-pair factor corpus (transferred for analysis).

### other
- **`config/default.json`** ← THE live config (gates, strategies.{}.enabled, green_exit, pip_eater spreads + pair_blocklist).
- **`docs/`** — `LIVE_SYSTEM_SPEC.md`, `BLUEPRINT.md`, `EXECUTION_PHYSICS.md`, `TRADE_PHYSICS_FIRST_PRINCIPLES.md`, + dated fixes: HTF_FREEZE / DIRECTION_KEY / ATR_COLLAPSE / HTF_MISALIGN / SPLICE_USDJPY.
- `logs/scrooge_v3.log*` (rotated), `backtests/run_backtest.py` (+ candle caches), `research/`, `scripts/`, `deploy/mr-scrooge-v3.service`.

---

## 2. Mini / Alien Drive — THE LAB + BACKTESTER  (`/Volumes/Alien Device/`, via EC2→Mini hop)

### `mr-scrooge-v3/research/replay_lab/` ← THE BACKTESTER
- **`cache/`** — 380 price-history parquets (M5/M1/D per pair) = the replay data source for ALL backtests.
- **`backtesting_py/`** — the backtesting.py engine.
- **`results/`** — outputs: **`backfill_8yr_6pair/`** (the running 6-pair backfill → `features_*.jsonl` + `trades_*.csv`), `backfill_7yr_4pair/`, `uncovered_8yr_4pair/`, + many `sweep_*`/`spec_sweep_*`/dated dirs.

### `mr-scrooge-v3/ml-lab/` ← THE ML LAB
- **`scripts/`** — `run_backfill_7yr.py` (backfill engine), **`assemble_extended_corpus.py`** (bucketize→corpus), **`score_extended.py`** (net_ladder + alignv), **`green_exit_bt.py`** (exit-ladder backtest), `lab_miner.py`, `lab_train.py` (train v0 + exit models), `regime_gate.py`, `run_uncovered_sweep.py`.
- `scored_corpus.parquet`, `cells_align4.csv`, `cell_ev_by_align.csv`, `ranker_histgbm_v1.pkl`, `findings.md`.

### `scrooge-research/` ← ARCHIVES
- **`archived_cleanup_2026-05-29/per_pair_lab/`** ← the 6mo dated trades **with MFE/MAE** (used for the runner-profile + give-back analysis). Also `archived_2026-05-28/`, `trade_logs/`, `outputs/`, `supplement_box_dbb/`.

### Mini `~/` ← THE PIPELINE TOOLS (run the lab→cells flow)
- **backfill**: `run_backfill_6pair.py` (currently running), `run_backfill_7yr.py`, `run_uncovered_8yr.py`.
- **build chain**: `assemble_extended_corpus.py` → `score_extended.py` → `buildcorpus.py` (→ corpus_8yr) / `build_pairaware.py` (→ playbook cells) / `exit_corpus.py` (→ exit corpus). **`build_ujp.sh`** (USD_JPY cell-build), **`test_pair.sh`** / `show_ujp.sh` (per-pair viability), `build_unc_cells.py`.
- **corpora**: `corpus_8yr.parquet`, **`scored_7yr.parquet`** (scored: net_ladder + alignv + 14 buckets — `build_pairaware`'s input), `exit_ml_corpus.parquet`, `uncovered_scored.parquet`.
- **analysis/patch** (many): `oos_wf.py`/`oos_sk.py`, `mfe_*`, `pwin8yr.py`, `tf2*.py`, `flip_test.py`, `exit_resim.py`, `patch_*` (live hotfixes), `vault-*.py` (vault tooling), `wait*.sh` (job pollers).
- **`~/scrooge_lab_code/`** — `factor_buckets.py` (the lab bucketizer the assembler imports) + `src`, `research`.

---

## 3. Dropbox — SESSION WORK HISTORY  (`LLM Sessions/Claude Sessions/Scrooge/`)
Per-session FINDINGS.md + scripts + artifacts:
- `2026-06-01_*` (per-pair-redesign, fx-edge-research [26-source], matrix-honest-consolidation [→ sig_corpus_phase3], bandit-walkforward)
- `2026-06-02_factor-wiring-fix` · `2026-06-03_bot-backtest` + `_align4-dialin` (the pair cuts) · `2026-06-04_green-exit-ladder` + `_ml-lab-build-spec`
- **`2026-06-09_htf-fix-and-factor-buckets`** ← today: all the fix scripts, the USD_JPY cells, the matrices, the splice + index docs.

---

## 4. Vault (EC2 `/data/obsidian-vault/wiki/systems/`) — THE KNOWLEDGE BASE
- **Hubs**: **`cockpit.md`** (routing HUD — read first), `quick-status.md`, `service-health-dashboard.md`, `schema/discovery.md`, `openclaw-agent-registry.md`.
- **Architecture**: `mr-scrooge-architecture.md`, `mr-scrooge-v3-scoring-system.md`, `-data-assets.md`, `system/bots/mr-scrooge.md`.
- **ML lab**: `ml-lab-build-spec.md`, `ml-lab-findings.md`, `ml-lab-wiring-proposal.md`, `exit-model-integration-spec.md`.
- **Recent fixes**: `htf-freeze-fix`, `direction-key-fix`, `atr-collapse-exit`, `htf-misalign-gate` (2026-06-09/10).
- **History/forensics** (~60): `scrooge-evolution-timeline.md` + `-index.md`, `scrooge-replay-lab.md`, `scrooge-bug-catalog.md`, `scrooge-dead-ends-graveyard.md`, `scrooge-frozen-constraints.md`, `scrooge-management-bug-atlas-v0/v1`, `scrooge-winner-clusters-v0/1/2`, the box/dbb/factor/regime research pages, `scrooge-v1-exec-summary-feb-2026.md`.
- **Accounts**: `registry/accounts/oanda.md`, `dropbox.md`.

---

## 5. MBP (`/Users/brock-mini-mac/`) — DEV CLONES
- `mr-scrooge-v3/` (local repo clone), `scrooge-mllab/`, `scrooge_strategy_drafts/`, `tmp/scrooge-*` (audit worktrees). Dropbox is mounted here (`Library/CloudStorage/Dropbox*`).

---

## The data lineage (how a cell is born)
`replay_lab/cache` (price) + strategies → **`run_backfill_*.py`** → `trades_*.csv` → **`assemble_extended_corpus.py`** (factor_buckets) → corpus → **`score_extended.py`** (net_ladder + alignv) → **`scored_7yr.parquet`** → **`build_pairaware.py`** → **`playbook_ev_pairaware.csv`** (+ `buildcorpus.py` → `corpus_8yr` → `lab_train.py` → `lab_training/v0/model.txt`). The live bot reads the playbook + the models; the **ml-observer** shadows it live.
