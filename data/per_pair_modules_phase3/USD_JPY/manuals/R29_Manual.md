# USD_JPY — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,102**  (W=1,298 / L=804)  -  WR: **61.8%**

## Session distribution

- asia: n=1015  W=626/L=389  WR=61.7%
- ny_close: n=389  W=242/L=147  WR=62.2%
- london: n=197  W=117/L=80  WR=59.4%
- ny_open: n=193  W=112/L=81  WR=58.0%
- off_hours: n=158  W=99/L=59  WR=62.7%
- asia_late: n=104  W=71/L=33  WR=68.3%
- ny_mid: n=24  W=15/L=9  WR=62.5%
- london_open: n=22  W=16/L=6  WR=72.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/13 losers (62%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W02.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/13 losers (62%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W03.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/13 losers (62%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W04.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/13 losers (62%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W05.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/13 losers (62%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W06.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/13 losers (62%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W07.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude BBP=BBP4 drops 8/11 losers (73%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W08.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude BBP=BBP4 drops 8/11 losers (73%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W09.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude BBP=BBP4 drops 8/11 losers (73%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W10.  `H20=H20c AND T4=T4a AND BBP=BBP2`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude session_bucket=london drops 8/11 losers (73%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; lower third  •  AVOID when session=london

### W11.  `T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude H20=H20c drops 9/10 losers (90%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W12.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude H20=H20c drops 9/10 losers (90%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W13.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude H20=H20c drops 9/10 losers (90%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W14.  `H20=H20c AND T4=T4a AND ZS=ZS2`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude session_bucket=london drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W15.  `H60=H60e AND RSI=RSI2 AND session_bucket=london`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20c drops 9/10 losers (90%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W16.  `H20=H20c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude session_bucket=london drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london

### W17.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20c drops 9/10 losers (90%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W18.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20c drops 9/10 losers (90%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W19.  `H20=H20e AND H60=H60e AND session_bucket=london`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  AVOID when lower third

### W20.  `H20=H20e AND T1=T1a AND session_bucket=london`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W21.  `H20=H20e AND direction_exec=short AND session_bucket=london`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london  •  AVOID when lower third

### W22.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W23.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  AVOID when lower third

### W24.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W25.  `H60=H60a AND T1=T1c AND session_bucket=asia_late`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H20=H20c drops 5/9 losers (56%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia_late  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=219  W=81/L=138  WR=37.0%
- Sharpen: sharpest is BBP=BBP0 (39/138 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=170  W=63/L=107  WR=37.1%
- Sharpen: sharpest is BBP=BBP0 (24/107 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L03.  `T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=170  W=63/L=107  WR=37.1%
- Sharpen: sharpest is BBP=BBP0 (24/107 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=170  W=63/L=107  WR=37.1%
- Sharpen: sharpest is BBP=BBP0 (24/107 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L05.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (15/91 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L06.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (15/91 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L07.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (15/91 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L08.  `H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=133  W=48/L=85  WR=36.1%
- Sharpen: sharpest is ZS=ZS2 (54/85 of losers there)
- **Sharp: n=76  W=22/L=54  WR=28.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -2 to -1 oversold

### L09.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=133  W=48/L=85  WR=36.1%
- Sharpen: sharpest is ZS=ZS2 (54/85 of losers there)
- **Sharp: n=76  W=22/L=54  WR=28.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -2 to -1 oversold

### L10.  `H60=H60a AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=133  W=48/L=85  WR=36.1%
- Sharpen: sharpest is ZS=ZS2 (54/85 of losers there)
- **Sharp: n=76  W=22/L=54  WR=28.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -2 to -1 oversold

### L11.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=128  W=37/L=91  WR=28.9%
- Sharpen: sharpest is BBP=BBP0 (39/91 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when deep below lower band

### L12.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=128  W=37/L=91  WR=28.9%
- Sharpen: sharpest is BBP=BBP0 (39/91 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when deep below lower band

### L13.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=128  W=37/L=91  WR=28.9%
- Sharpen: sharpest is BBP=BBP0 (39/91 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when deep below lower band

### L14.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=106  W=40/L=66  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (40/66 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=asia

### L15.  `BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=106  W=40/L=66  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (40/66 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: LONG**  •  lower third; RSI 20-30 oversold  •  ONLY when session=asia

### L16.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=106  W=40/L=66  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (40/66 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=asia

### L17.  `H20=H20a AND T1=T1c AND RSI=RSI1`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L18.  `H20=H20a AND T4=T4c AND RSI=RSI1`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L19.  `H20=H20a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L20.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L21.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L22.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L23.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L24.  `H20=H20a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L25.  `H20=H20a AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (15/64 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(41/34) | H20a(34/41) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
