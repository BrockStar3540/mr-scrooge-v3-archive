# GBP_AUD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,652**  (W=1,630 / L=1,022)  -  WR: **61.5%**

## Session distribution

- asia: n=1376  W=868/L=508  WR=63.1%
- ny_close: n=569  W=338/L=231  WR=59.4%
- off_hours: n=326  W=188/L=138  WR=57.7%
- london: n=130  W=83/L=47  WR=63.8%
- asia_late: n=93  W=55/L=38  WR=59.1%
- ny_open: n=76  W=44/L=32  WR=57.9%
- london_open: n=54  W=35/L=19  WR=64.8%
- ny_mid: n=28  W=19/L=9  WR=67.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND T4=T4a AND session_bucket=asia`
- Raw: n=171  W=150/L=21  WR=87.7%
- Refine: exclude RSI=RSI4 drops 12/21 losers (57%)
- **Final: n=153  W=144/L=9  WR=94.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W02.  `H20=H20d AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=165  W=144/L=21  WR=87.3%
- Refine: exclude RSI=RSI4 drops 12/21 losers (57%)
- **Final: n=151  W=142/L=9  WR=94.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W03.  `T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=146  W=131/L=15  WR=89.7%
- Refine: exclude H20=H20e drops 11/15 losers (73%)
- **Final: n=103  W=99/L=4  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 strongly against

### W04.  `H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=143  W=127/L=16  WR=88.8%
- Refine: exclude H20=H20e drops 11/16 losers (69%)
- **Final: n=103  W=98/L=5  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W05.  `RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=143  W=127/L=16  WR=88.8%
- Refine: exclude H20=H20e drops 11/16 losers (69%)
- **Final: n=103  W=98/L=5  WR=95.1%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W06.  `H60=H60a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=143  W=127/L=16  WR=88.8%
- Refine: exclude H20=H20e drops 11/16 losers (69%)
- **Final: n=103  W=98/L=5  WR=95.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W07.  `T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=141  W=129/L=12  WR=91.5%
- Refine: exclude H20=H20e drops 7/12 losers (58%)
- **Final: n=105  W=100/L=5  WR=95.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W08.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=135  W=124/L=11  WR=91.9%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W09.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=135  W=124/L=11  WR=91.9%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W10.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude H20=H20e drops 11/16 losers (69%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W11.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude H20=H20e drops 11/16 losers (69%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W13.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude RSI=RSI4 drops 10/15 losers (67%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W14.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude RSI=RSI4 drops 10/15 losers (67%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W15.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude H60=H60a drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 aligned WITH trade

### W16.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude BBP=BBP0 drops 12/16 losers (75%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W17.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude BBP=BBP0 drops 12/16 losers (75%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W18.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude BBP=BBP0 drops 12/16 losers (75%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W19.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude H20=H20d drops 11/16 losers (69%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W20.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude BBP=BBP0 drops 12/14 losers (86%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W21.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude BBP=BBP0 drops 12/14 losers (86%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude BBP=BBP0 drops 12/16 losers (75%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W23.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude BBP=BBP0 drops 12/16 losers (75%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude BBP=BBP0 drops 12/14 losers (86%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W25.  `H60=H60e AND T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude RSI=RSI4 drops 9/9 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=224  W=85/L=139  WR=37.9%
- Sharpen: sharpest is session_bucket=asia (77/139 of losers there)
- **Sharp: n=101  W=24/L=77  WR=23.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L02.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=224  W=85/L=139  WR=37.9%
- Sharpen: sharpest is session_bucket=asia (77/139 of losers there)
- **Sharp: n=101  W=24/L=77  WR=23.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L03.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=224  W=85/L=139  WR=37.9%
- Sharpen: sharpest is session_bucket=asia (77/139 of losers there)
- **Sharp: n=101  W=24/L=77  WR=23.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (66/128 of losers there)
- **Sharp: n=87  W=21/L=66  WR=24.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L05.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (66/128 of losers there)
- **Sharp: n=87  W=21/L=66  WR=24.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (66/128 of losers there)
- **Sharp: n=87  W=21/L=66  WR=24.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L07.  `H20=H20e AND H60=H60e AND RSI=RSI2`
- Raw: n=138  W=42/L=96  WR=30.4%
- Sharpen: sharpest is BBP=BBP1 (30/96 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  ONLY when just touched lower band

### L08.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=138  W=42/L=96  WR=30.4%
- Sharpen: sharpest is BBP=BBP1 (30/96 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when just touched lower band

### L09.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=138  W=42/L=96  WR=30.4%
- Sharpen: sharpest is session_bucket=asia (72/96 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L10.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=138  W=42/L=96  WR=30.4%
- Sharpen: sharpest is BBP=BBP1 (30/96 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  ONLY when just touched lower band

### L11.  `T1=T1a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=138  W=52/L=86  WR=37.7%
- Sharpen: sharpest is H60=H60a (48/86 of losers there)
- **Sharp: n=61  W=13/L=48  WR=21.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF60 aligned WITH trade

### L12.  `H20=H20b AND T1=T1c AND session_bucket=asia`
- Raw: n=137  W=51/L=86  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (40/86 of losers there)
- **Sharp: n=46  W=6/L=40  WR=13.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI2`
- Raw: n=134  W=37/L=97  WR=27.6%
- Sharpen: sharpest is BBP=BBP1 (30/97 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L14.  `H20=H20b AND T4=T4c AND session_bucket=asia`
- Raw: n=134  W=44/L=90  WR=32.8%
- Sharpen: sharpest is ZS=ZS5 (40/90 of losers there)
- **Sharp: n=46  W=6/L=40  WR=13.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=129  W=37/L=92  WR=28.7%
- Sharpen: sharpest is BBP=BBP1 (30/92 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=129  W=37/L=92  WR=28.7%
- Sharpen: sharpest is BBP=BBP1 (30/92 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L17.  `H20=H20b AND H60=H60e AND direction_exec=long`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is BBP=BBP4 (22/77 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against  •  ONLY when upper third

### L18.  `H20=H20b AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=126  W=42/L=84  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (40/84 of losers there)
- **Sharp: n=46  W=6/L=40  WR=13.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=124  W=36/L=88  WR=29.0%
- Sharpen: sharpest is T4=T4c (72/88 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=124  W=39/L=85  WR=31.5%
- Sharpen: sharpest is ZS=ZS1 (36/85 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=124  W=39/L=85  WR=31.5%
- Sharpen: sharpest is ZS=ZS1 (36/85 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=124  W=39/L=85  WR=31.5%
- Sharpen: sharpest is ZS=ZS1 (36/85 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=123  W=44/L=79  WR=35.8%
- Sharpen: sharpest is T1=T1c (72/79 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=120  W=43/L=77  WR=35.8%
- Sharpen: sharpest is RSI=RSI3 (36/77 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=115  W=34/L=81  WR=29.6%
- Sharpen: sharpest is ZS=ZS1 (36/81 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(41/30), H20d(18/11) | H20e(30/41), H20b(10/17) |
| H60 | H60a(53/48) | H60e(47/52) |
| T1 | T1a(55/49) | T1c(45/51) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/48) | long(47/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
