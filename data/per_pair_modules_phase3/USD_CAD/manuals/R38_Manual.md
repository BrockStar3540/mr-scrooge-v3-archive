# USD_CAD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,864**  (W=1,175 / L=689)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=993  W=629/L=364  WR=63.3%
- ny_open: n=287  W=172/L=115  WR=59.9%
- ny_close: n=238  W=148/L=90  WR=62.2%
- london_open: n=124  W=85/L=39  WR=68.5%
- asia: n=113  W=74/L=39  WR=65.5%
- london: n=54  W=29/L=25  WR=53.7%
- off_hours: n=38  W=26/L=12  WR=68.4%
- asia_late: n=17  W=12/L=5  WR=70.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=170  W=152/L=18  WR=89.4%
- Refine: exclude session_bucket=ny_mid drops 14/18 losers (78%)
- **Final: n=102  W=98/L=4  WR=96.1%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W02.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=150  W=137/L=13  WR=91.3%
- Refine: exclude session_bucket=ny_mid drops 11/13 losers (85%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W03.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=150  W=137/L=13  WR=91.3%
- Refine: exclude session_bucket=ny_mid drops 11/13 losers (85%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W04.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=137  W=120/L=17  WR=87.6%
- Refine: exclude session_bucket=ny_mid drops 13/17 losers (76%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W05.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 13/17 losers (76%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H20=H20e drops 16/18 losers (89%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W07.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H20=H20e drops 16/18 losers (89%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W08.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H20=H20e drops 16/18 losers (89%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W09.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude session_bucket=ny_mid drops 10/12 losers (83%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W10.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude session_bucket=ny_mid drops 10/12 losers (83%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W11.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude T4=T4a drops 12/16 losers (75%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20b AND T1=T1a AND RSI=RSI5`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP6 drops 3/3 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W13.  `H20=H20b AND T4=T4a AND RSI=RSI5`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP6 drops 3/3 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W14.  `H20=H20b AND RSI=RSI5 AND direction_exec=long`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP6 drops 3/3 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong  •  AVOID when deep above upper band

### W15.  `H20=H20b AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP6 drops 3/3 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W16.  `H20=H20b AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP6 drops 3/3 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W17.  `H20=H20b AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude BBP=BBP6 drops 3/3 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W18.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W19.  `H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W20.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W21.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W23.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +2 to +3 deep overbought

### W24.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W25.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS5 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +2 to +3 deep overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=143  W=43/L=100  WR=30.1%
- Sharpen: sharpest is RSI=RSI5 (45/100 of losers there)
- **Sharp: n=46  W=1/L=45  WR=2.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L02.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: sharpest is RSI=RSI5 (36/85 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L03.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=116  W=40/L=76  WR=34.5%
- Sharpen: sharpest is RSI=RSI5 (36/76 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L04.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=104  W=27/L=77  WR=26.0%
- Sharpen: sharpest is H60=H60a (21/77 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T1=T1c (36/60 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L06.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is H20=H20e (43/55 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is H60=H60e (45/54 of losers there)
- **Sharp: n=61  W=16/L=45  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L08.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is H60=H60e (45/54 of losers there)
- **Sharp: n=61  W=16/L=45  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L09.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=88  W=20/L=68  WR=22.7%
- Sharpen: sharpest is T1=T1c (19/68 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L10.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=88  W=20/L=68  WR=22.7%
- Sharpen: sharpest is T1=T1c (19/68 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L11.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=87  W=27/L=60  WR=31.0%
- Sharpen: sharpest is H20=H20b (28/60 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L12.  `H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=86  W=22/L=64  WR=25.6%
- Sharpen: sharpest is RSI=RSI5 (45/64 of losers there)
- **Sharp: n=46  W=1/L=45  WR=2.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=85  W=27/L=58  WR=31.8%
- Sharpen: sharpest is H20=H20b (28/58 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L14.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=83  W=20/L=63  WR=24.1%
- Sharpen: sharpest is RSI=RSI5 (45/63 of losers there)
- **Sharp: n=46  W=1/L=45  WR=2.2%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=83  W=20/L=63  WR=24.1%
- Sharpen: sharpest is RSI=RSI5 (45/63 of losers there)
- **Sharp: n=46  W=1/L=45  WR=2.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L16.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is H60=H60e (24/53 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L17.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is H60=H60e (24/53 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L18.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is H60=H60e (24/53 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS4`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (30/50 of losers there)
- **Sharp: n=41  W=11/L=30  WR=26.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L20.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=80  W=20/L=60  WR=25.0%
- Sharpen: sharpest is RSI=RSI5 (45/60 of losers there)
- **Sharp: n=46  W=1/L=45  WR=2.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=80  W=20/L=60  WR=25.0%
- Sharpen: sharpest is RSI=RSI5 (45/60 of losers there)
- **Sharp: n=46  W=1/L=45  WR=2.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is ZS=ZS4 (45/50 of losers there)
- **Sharp: n=61  W=16/L=45  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L23.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=79  W=28/L=51  WR=35.4%
- Sharpen: sharpest is ZS=ZS5 (11/51 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is H20=H20e (30/48 of losers there)
- **Sharp: n=40  W=10/L=30  WR=25.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L25.  `H60=H60e AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=77  W=27/L=50  WR=35.1%
- Sharpen: sharpest is H20=H20e (36/50 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(37/28) | H20e(29/36), H20d(10/17) |
| H60 | H60a(46/37) | H60e(34/42) |
| T1 | T1a(55/45) | T1c(44/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
