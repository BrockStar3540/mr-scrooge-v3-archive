# EUR_USD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,117**  (W=2,008 / L=1,109)  -  WR: **64.4%**

## Session distribution

- ny_mid: n=990  W=631/L=359  WR=63.7%
- london_open: n=770  W=502/L=268  WR=65.2%
- asia: n=471  W=295/L=176  WR=62.6%
- ny_open: n=325  W=196/L=129  WR=60.3%
- london: n=219  W=145/L=74  WR=66.2%
- ny_close: n=211  W=143/L=68  WR=67.8%
- off_hours: n=83  W=61/L=22  WR=73.5%
- asia_late: n=48  W=35/L=13  WR=72.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=196  W=171/L=25  WR=87.2%
- Refine: exclude ZS=ZS3 drops 11/25 losers (44%)
- **Final: n=148  W=134/L=14  WR=90.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W02.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=139  W=123/L=16  WR=88.5%
- Refine: exclude H60=H60e drops 16/16 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W03.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=136  W=117/L=19  WR=86.0%
- Refine: exclude T1=T1a drops 13/19 losers (68%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W04.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude T1=T1c drops 15/17 losers (88%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W05.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=121  W=109/L=12  WR=90.1%
- Refine: exclude ZS=ZS3 drops 6/12 losers (50%)
- **Final: n=113  W=107/L=6  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude T1=T1a drops 11/17 losers (65%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude T4=T4c drops 11/17 losers (65%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude T4=T4a drops 13/15 losers (87%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20a AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude T4=T4a drops 13/15 losers (87%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude ZS=ZS5 drops 17/17 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

### W11.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=113  W=107/L=6  WR=94.7%
- Refine: exclude direction_exec=long drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when long

### W12.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude ZS=ZS5 drops 15/15 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

### W13.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude H60=H60e drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W14.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=96  W=90/L=6  WR=93.8%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude ZS=ZS5 drops 7/8 losers (88%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W17.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W18.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude T1=T1a drops 9/10 losers (90%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W20.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W21.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W22.  `H20=H20a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS2 drops 3/8 losers (38%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=london  •  AVOID when zscore -2 to -1 oversold

### W23.  `T4=T4c AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=74  W=72/L=2  WR=97.3%
- Refine: exclude H20=H20b drops 2/2 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore >+3 extreme  •  AVOID when HTF20 slightly aligned

### W24.  `H20=H20a AND T4=T4c AND BBP=BBP3`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; middle of band  •  AVOID when session=ny_mid

### W25.  `H20=H20a AND T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=145  W=49/L=96  WR=33.8%
- Sharpen: sharpest is T1=T1a (54/96 of losers there)
- **Sharp: n=67  W=13/L=54  WR=19.4%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L02.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is T4=T4a (27/87 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L03.  `T1=T1a AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_mid (18/63 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L04.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is T4=T4a (27/61 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L05.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=95  W=27/L=68  WR=28.4%
- Sharpen: sharpest is H20=H20a (36/68 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L06.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=81  W=27/L=54  WR=33.3%
- Sharpen: sharpest is T1=T1a (23/54 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when 1h trend WITH trade

### L07.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is RSI=RSI5 (47/49 of losers there)
- **Sharp: n=64  W=17/L=47  WR=26.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L08.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=77  W=22/L=55  WR=28.6%
- Sharpen: sharpest is T1=T1a (54/55 of losers there)
- **Sharp: n=67  W=13/L=54  WR=19.4%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L09.  `T4=T4c AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=75  W=23/L=52  WR=30.7%
- Sharpen: sharpest is H20=H20a (16/52 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L10.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=75  W=23/L=52  WR=30.7%
- Sharpen: sharpest is H20=H20a (16/52 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (13/46 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=asia

### L12.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (13/46 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L13.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (24/44 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (24/44 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L15.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (24/44 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L16.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is H60=H60a (24/42 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L17.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is RSI=RSI5 (29/45 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L18.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is H60=H60e (29/45 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when HTF60 strongly against

### L19.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is ZS=ZS6 (24/41 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when zscore >+3 extreme

### L20.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=67  W=13/L=54  WR=19.4%
- Sharpen: sharpest is H60=H60a (20/54 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L21.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is H60=H60e (19/41 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF60 strongly against

### L22.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=64  W=17/L=47  WR=26.6%
- Sharpen: sharpest is H60=H60a (20/47 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L23.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=64  W=20/L=44  WR=31.2%
- Sharpen: sharpest is T4=T4a (17/44 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L24.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (37/39 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60a (20/38 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
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
