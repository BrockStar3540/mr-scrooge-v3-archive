# EUR_USD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **963**  (W=609 / L=354)  -  WR: **63.2%**

## Session distribution

- london_open: n=255  W=165/L=90  WR=64.7%
- ny_open: n=185  W=124/L=61  WR=67.0%
- asia: n=143  W=84/L=59  WR=58.7%
- ny_mid: n=137  W=87/L=50  WR=63.5%
- london: n=124  W=75/L=49  WR=60.5%
- ny_close: n=67  W=40/L=27  WR=59.7%
- asia_late: n=52  W=34/L=18  WR=65.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude BBP=BBP2 drops 8/9 losers (89%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W02.  `H20=H20a AND T1=T1c AND direction_exec=long`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude BBP=BBP2 drops 8/9 losers (89%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when lower third

### W03.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude BBP=BBP2 drops 8/9 losers (89%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W04.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude BBP=BBP2 drops 8/9 losers (89%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W05.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W06.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W07.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W08.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W09.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W10.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=77  W=72/L=5  WR=93.5%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W11.  `H20=H20a AND T1=T1c AND RSI=RSI2`
- Raw: n=68  W=63/L=5  WR=92.6%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=london

### W12.  `H20=H20a AND T4=T4c AND RSI=RSI2`
- Raw: n=68  W=63/L=5  WR=92.6%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=london

### W13.  `H20=H20a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=68  W=63/L=5  WR=92.6%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W14.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=68  W=63/L=5  WR=92.6%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=london

### W15.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=68  W=63/L=5  WR=92.6%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=london

### W16.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=68  W=63/L=5  WR=92.6%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=london

### W17.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=asia

### W18.  `H20=H20a AND H60=H60a AND T4=T4c`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W19.  `H20=H20a AND H60=H60a AND direction_exec=long`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  AVOID when session=asia

### W20.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=london drops 5/8 losers (62%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W21.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W22.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=asia

### W23.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W24.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W25.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=86  W=31/L=55  WR=36.0%
- Sharpen: sharpest is H20=H20e (31/55 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: sharpest is H20=H20e (31/52 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: sharpest is H20=H20e (31/52 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade  •  ONLY when HTF20 strongly against

### L04.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: sharpest is H20=H20e (31/52 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L05.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is RSI=RSI1 (18/36 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L06.  `H20=H20e AND T1=T1a AND direction_exec=short`
- Raw: n=54  W=10/L=44  WR=18.5%
- Sharpen: sharpest is ZS=ZS1 (19/44 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=52  W=8/L=44  WR=15.4%
- Sharpen: sharpest is ZS=ZS1 (19/44 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=52  W=8/L=44  WR=15.4%
- Sharpen: sharpest is ZS=ZS1 (19/44 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=52  W=8/L=44  WR=15.4%
- Sharpen: sharpest is ZS=ZS1 (19/44 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is H20=H20e (20/31 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is H20=H20e (20/31 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is H20=H20e (20/31 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  ONLY when HTF20 strongly against

### L13.  `H20=H20e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L14.  `H60=H60e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L15.  `T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L16.  `T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L17.  `RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L18.  `H20=H20e AND H60=H60e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L19.  `H20=H20e AND T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L20.  `H20=H20e AND T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L21.  `H20=H20e AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L22.  `H20=H20e AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L23.  `H60=H60e AND T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L24.  `H60=H60e AND T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

### L25.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/30 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/38) | H20e(41/53) |
| H60 | H60a(54/43) | H60e(44/56) |
| T1 | T1c(56/47) | T1a(44/53) |
| T4 | T4c(58/47) | T4a(42/53) |
| BBP | — | — |
| RSI | RSI2(39/33) | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/47) | short(42/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
