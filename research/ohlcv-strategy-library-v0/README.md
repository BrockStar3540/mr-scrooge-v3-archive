# OHLCV Strategy Library v0

Executable harness for Brock's explicit OHLCV formula library.

It computes M5 indicators, applies the 53-regime classifier, emits edge-triggered strategy entries, and screens outcomes with bid/ask-aware forward windows. Full trade logs are generated locally on EC2 and intentionally ignored by git.

Run on EC2:

```bash
cd /home/ubuntu/mr-scrooge-v3
~/mr_burns_env/bin/python3 -u research/ohlcv-strategy-library-v0/backtest_ohlcv_strategy_library_v0.py --scope smoke
~/mr_burns_env/bin/python3 -u research/ohlcv-strategy-library-v0/backtest_ohlcv_strategy_library_v0.py --scope all
```

v0 uses conservative path-agnostic screening: if TP and stop are both touched inside the forward window, the trade is scored as a stop. Survivors should get exact path replay next.
