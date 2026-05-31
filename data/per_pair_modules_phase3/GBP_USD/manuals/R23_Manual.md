# GBP_USD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,664**  (W=2,230 / L=1,434)  -  WR: **60.9%**

## Session distribution

- ny_mid: n=1086  W=666/L=420  WR=61.3%
- london_open: n=734  W=458/L=276  WR=62.4%
- ny_open: n=689  W=410/L=279  WR=59.5%
- ny_close: n=460  W=297/L=163  WR=64.6%
- london: n=365  W=193/L=172  WR=52.9%
- asia: n=233  W=144/L=89  WR=61.8%
- asia_late: n=79  W=50/L=29  WR=63.3%
- off_hours: n=18  W=12/L=6  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude H20=H20e drops 14/25 losers (56%)
- **Final: n=144  W=133/L=11  WR=92.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W02.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude H20=H20e drops 14/24 losers (58%)
- **Final: n=137  W=127/L=10  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W03.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=129  W=120/L=9  WR=93.0%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W04.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=126  W=111/L=15  WR=88.1%
- Refine: exclude T1=T1a drops 14/15 losers (93%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W05.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=120  W=111/L=9  WR=92.5%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W06.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude direction_exec=long drops 16/17 losers (94%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when long

### W07.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=110  W=106/L=4  WR=96.4%
- Refine: exclude session_bucket=ny_open drops 3/4 losers (75%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W08.  `BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=110  W=106/L=4  WR=96.4%
- Refine: exclude session_bucket=ny_open drops 3/4 losers (75%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W09.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude T1=T1a drops 9/10 losers (90%)
- **Final: n=76  W=75/L=1  WR=98.7%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W10.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude T1=T1a drops 9/10 losers (90%)
- **Final: n=76  W=75/L=1  WR=98.7%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W11.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude H60=H60b drops 7/10 losers (70%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 slightly aligned

### W12.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=101  W=97/L=4  WR=96.0%
- Refine: exclude session_bucket=ny_open drops 3/4 losers (75%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W13.  `H20=H20e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude ZS=ZS6 drops 7/15 losers (47%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when zscore >+3 extreme

### W14.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude direction_exec=long drops 9/10 losers (90%)
- **Final: n=85  W=84/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when long

### W15.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude direction_exec=long drops 9/10 losers (90%)
- **Final: n=85  W=84/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when long

### W16.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude ZS=ZS6 drops 7/14 losers (50%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when zscore >+3 extreme

### W17.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=99  W=90/L=9  WR=90.9%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=86  W=86/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 strongly against

### W18.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=90/L=9  WR=90.9%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=86  W=86/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 strongly against

### W19.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude BBP=BBP4 drops 10/11 losers (91%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W20.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought

### W21.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude H60=H60b drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when HTF60 slightly aligned

### W22.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude ZS=ZS6 drops 7/12 losers (58%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  AVOID when zscore >+3 extreme

### W23.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude H60=H60b drops 7/9 losers (78%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 slightly aligned

### W24.  `H60=H60a AND T1=T1a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=london drops 7/13 losers (54%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=london

### W25.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=london drops 7/13 losers (54%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=268  W=106/L=162  WR=39.6%
- Sharpen: sharpest is H60=H60e (82/162 of losers there)
- **Sharp: n=118  W=36/L=82  WR=30.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L02.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=247  W=94/L=153  WR=38.1%
- Sharpen: sharpest is H60=H60e (79/153 of losers there)
- **Sharp: n=111  W=32/L=79  WR=28.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L03.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_open (39/105 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L04.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=149  W=50/L=99  WR=33.6%
- Sharpen: sharpest is session_bucket=ny_open (39/99 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is T4=T4a (53/88 of losers there)
- **Sharp: n=69  W=16/L=53  WR=23.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=141  W=46/L=95  WR=32.6%
- Sharpen: sharpest is T4=T4a (53/95 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=141  W=46/L=95  WR=32.6%
- Sharpen: sharpest is T4=T4a (53/95 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is BBP=BBP3 (54/84 of losers there)
- **Sharp: n=79  W=25/L=54  WR=31.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when middle of band

### L09.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=133  W=50/L=83  WR=37.6%
- Sharpen: sharpest is H20=H20a (27/83 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L10.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=132  W=47/L=85  WR=35.6%
- Sharpen: sharpest is ZS=ZS5 (32/85 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=131  W=51/L=80  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_close (16/80 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L12.  `T1=T1c AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=131  W=51/L=80  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_close (16/80 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L13.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=130  W=46/L=84  WR=35.4%
- Sharpen: sharpest is H20=H20e (26/84 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=127  W=48/L=79  WR=37.8%
- Sharpen: sharpest is H60=H60b (17/79 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  ONLY when HTF60 slightly aligned

### L15.  `RSI=RSI5 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is T4=T4a (51/79 of losers there)
- **Sharp: n=74  W=23/L=51  WR=31.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1c AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is H20=H20a (47/76 of losers there)
- **Sharp: n=68  W=21/L=47  WR=30.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when HTF20 aligned WITH trade

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is H60=H60e (53/78 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L18.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=121  W=41/L=80  WR=33.9%
- Sharpen: sharpest is session_bucket=ny_mid (53/80 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L19.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is H20=H20a (24/74 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=118  W=36/L=82  WR=30.5%
- Sharpen: sharpest is H20=H20e (53/82 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L21.  `T1=T1c AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is T4=T4a (51/73 of losers there)
- **Sharp: n=74  W=23/L=51  WR=31.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L22.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is RSI=RSI5 (53/71 of losers there)
- **Sharp: n=69  W=16/L=53  WR=23.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L23.  `T1=T1c AND T4=T4a AND BBP=BBP3`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is H60=H60a (29/73 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; middle of band  •  ONLY when HTF60 aligned WITH trade

### L24.  `T1=T1c AND T4=T4a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is H60=H60a (29/73 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  ONLY when HTF60 aligned WITH trade

### L25.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=113  W=37/L=76  WR=32.7%
- Sharpen: sharpest is H60=H60d (34/76 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when HTF60 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/44) | T1c(47/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
