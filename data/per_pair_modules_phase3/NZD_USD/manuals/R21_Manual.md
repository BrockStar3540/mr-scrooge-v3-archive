# NZD_USD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,583**  (W=1,012 / L=571)  -  WR: **63.9%**

## Session distribution

- ny_close: n=388  W=245/L=143  WR=63.1%
- asia: n=379  W=239/L=140  WR=63.1%
- ny_open: n=262  W=171/L=91  WR=65.3%
- london_open: n=175  W=111/L=64  WR=63.4%
- ny_mid: n=171  W=116/L=55  WR=67.8%
- london: n=128  W=79/L=49  WR=61.7%
- asia_late: n=45  W=28/L=17  WR=62.2%
- off_hours: n=35  W=23/L=12  WR=65.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND RSI=RSI5`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude H60=H60e drops 12/19 losers (63%)
- **Final: n=111  W=104/L=7  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W02.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=142  W=123/L=19  WR=86.6%
- Refine: exclude ZS=ZS3 drops 13/19 losers (68%)
- **Final: n=111  W=105/L=6  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude T4=T4c drops 8/16 losers (50%)
- **Final: n=85  W=77/L=8  WR=90.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude ZS=ZS3 drops 8/11 losers (73%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude ZS=ZS3 drops 8/11 losers (73%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude ZS=ZS3 drops 8/11 losers (73%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude ZS=ZS3 drops 8/11 losers (73%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=123  W=112/L=11  WR=91.1%
- Refine: exclude ZS=ZS3 drops 8/11 losers (73%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W09.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude H60=H60e drops 10/17 losers (59%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W10.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude H60=H60e drops 10/17 losers (59%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W11.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude H20=H20e drops 11/13 losers (85%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W12.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude H20=H20e drops 11/13 losers (85%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=107  W=100/L=7  WR=93.5%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=107  W=100/L=7  WR=93.5%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=107  W=100/L=7  WR=93.5%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude H20=H20e drops 11/13 losers (85%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W17.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude H20=H20e drops 11/13 losers (85%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W18.  `H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: no further refinement
- **Final: n=101  W=87/L=14  WR=86.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third

### W19.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: no further refinement
- **Final: n=101  W=87/L=14  WR=86.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third

### W20.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude RSI=RSI4 drops 11/11 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W21.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W22.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W23.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude H20=H20e drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W24.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude H20=H20e drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W25.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is ZS=ZS4 (25/61 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS4 (20/59 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L03.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS4 (20/59 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L04.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS4 (20/59 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L05.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS4 (20/59 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS4 (20/59 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L07.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (10/52 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L08.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=75  W=23/L=52  WR=30.7%
- Sharpen: sharpest is ZS=ZS4 (20/52 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L09.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=75  W=23/L=52  WR=30.7%
- Sharpen: sharpest is ZS=ZS4 (20/52 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L10.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=75  W=23/L=52  WR=30.7%
- Sharpen: sharpest is ZS=ZS4 (20/52 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L11.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is H60=H60a (15/50 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L12.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is H60=H60e (43/45 of losers there)
- **Sharp: n=61  W=18/L=43  WR=29.5%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L13.  `H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H20=H20a (32/48 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H20=H20a (32/48 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 aligned WITH trade

### L15.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is RSI=RSI5 (30/44 of losers there)
- **Sharp: n=41  W=11/L=30  WR=26.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L16.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is H60=H60e (42/44 of losers there)
- **Sharp: n=58  W=16/L=42  WR=27.6%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is H60=H60e (42/44 of losers there)
- **Sharp: n=58  W=16/L=42  WR=27.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L18.  `H20=H20a AND T1=T1c AND BBP=BBP2`
- Raw: n=70  W=22/L=48  WR=31.4%
- Sharpen: sharpest is session_bucket=london_open (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when session=london_open

### L19.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=70  W=23/L=47  WR=32.9%
- Sharpen: sharpest is H60=H60a (12/47 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is H60=H60a (11/46 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L21.  `T4=T4c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is ZS=ZS3 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L22.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is H20=H20e (20/44 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L23.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=66  W=21/L=45  WR=31.8%
- Sharpen: sharpest is BBP=BBP6 (15/45 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L24.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=64  W=19/L=45  WR=29.7%
- Sharpen: sharpest is session_bucket=ny_open (8/45 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L25.  `H60=H60e AND T1=T1c AND ZS=ZS2`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is H20=H20a (25/41 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(54/45) | H20e(45/54) |
| H60 | H60a(51/42) | H60e(41/49) |
| T1 | T1a(58/41) | T1c(42/59) |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/46) | short(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
