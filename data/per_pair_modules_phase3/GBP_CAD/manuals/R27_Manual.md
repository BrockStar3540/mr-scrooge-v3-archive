# GBP_CAD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,569**  (W=975 / L=594)  -  WR: **62.1%**

## Session distribution

- asia: n=803  W=513/L=290  WR=63.9%
- ny_close: n=337  W=203/L=134  WR=60.2%
- off_hours: n=173  W=102/L=71  WR=59.0%
- london_open: n=72  W=42/L=30  WR=58.3%
- ny_mid: n=53  W=34/L=19  WR=64.2%
- london: n=52  W=29/L=23  WR=55.8%
- ny_open: n=41  W=26/L=15  WR=63.4%
- asia_late: n=38  W=26/L=12  WR=68.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND RSI=RSI1`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when HTF60 strongly against

### W02.  `H20=H20e AND T4=T4a AND RSI=RSI1`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when HTF60 strongly against

### W03.  `H20=H20e AND RSI=RSI1 AND direction_exec=short`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 20-30 oversold  •  AVOID when HTF60 strongly against

### W04.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when HTF60 strongly against

### W05.  `H20=H20e AND T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when HTF60 strongly against

### W06.  `H20=H20e AND T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60e drops 9/13 losers (69%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when HTF60 strongly against

### W07.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude BBP=BBP0 drops 8/9 losers (89%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W08.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=asia drops 6/8 losers (75%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia

### W09.  `H60=H60a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W10.  `H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/6 losers (33%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when strategy=charlie_pullback_continuation_v2

### W11.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 30-40 weak

### W12.  `H20=H20a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 30-40 weak

### W13.  `H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/6 losers (33%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when strategy=charlie_pullback_continuation_v2

### W14.  `H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/6 losers (33%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third  •  AVOID when strategy=charlie_pullback_continuation_v2

### W15.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/6 losers (33%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when strategy=charlie_pullback_continuation_v2

### W16.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/6 losers (33%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when strategy=charlie_pullback_continuation_v2

### W17.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/6 losers (33%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when strategy=charlie_pullback_continuation_v2

### W18.  `H20=H20e AND T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=63/L=4  WR=94.0%
- Refine: exclude H60=H60e drops 4/4 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF60 strongly against

### W19.  `H20=H20e AND T4=T4a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=63/L=4  WR=94.0%
- Refine: exclude H60=H60e drops 4/4 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF60 strongly against

### W20.  `H20=H20e AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=63/L=4  WR=94.0%
- Refine: exclude H60=H60e drops 4/4 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when HTF60 strongly against

### W21.  `H60=H60a AND T4=T4a AND BBP=BBP1`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 30-40 weak

### W22.  `H60=H60a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; just touched lower band  •  AVOID when RSI 30-40 weak

### W23.  `H60=H60a AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W24.  `H60=H60a AND T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 30-40 weak

### W25.  `H60=H60a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=165  W=60/L=105  WR=36.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold

### L02.  `T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=165  W=60/L=105  WR=36.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold

### L03.  `T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=165  W=60/L=105  WR=36.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=165  W=60/L=105  WR=36.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is H20=H20a (32/75 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 aligned WITH trade

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is H20=H20a (32/75 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 aligned WITH trade

### L07.  `H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is H20=H20a (32/75 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is H20=H20a (32/75 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 aligned WITH trade

### L09.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is H20=H20a (32/75 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 aligned WITH trade

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is H20=H20a (32/75 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is ZS=ZS1 (32/74 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=118  W=46/L=72  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (32/72 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is H20=H20a (34/62 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L14.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is H20=H20a (34/62 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L15.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is H20=H20a (34/62 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is H20=H20a (34/62 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L17.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is H20=H20a (34/62 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L18.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is H20=H20a (34/62 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L19.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (32/57 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L20.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (32/57 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L21.  `H60=H60e AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is H20=H20e (35/57 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 strongly against

### L22.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (32/57 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L23.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is BBP=BBP2 (34/55 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when lower third

### L24.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is BBP=BBP2 (34/55 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when lower third

### L25.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is BBP=BBP2 (34/55 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(47/30) | H60e(31/48) |
| T1 | — | — |
| T4 | T4a(56/44) | T4c(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/46) | long(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
