# EUR_JPY — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,575**  (W=1,653 / L=922)  -  WR: **64.2%**

## Session distribution

- asia: n=872  W=564/L=308  WR=64.7%
- london_open: n=578  W=367/L=211  WR=63.5%
- asia_late: n=267  W=172/L=95  WR=64.4%
- london: n=241  W=168/L=73  WR=69.7%
- ny_close: n=230  W=142/L=88  WR=61.7%
- ny_open: n=188  W=110/L=78  WR=58.5%
- ny_mid: n=166  W=113/L=53  WR=68.1%
- off_hours: n=33  W=17/L=16  WR=51.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=263  W=224/L=39  WR=85.2%
- Refine: exclude BBP=BBP6 drops 26/39 losers (67%)
- **Final: n=150  W=137/L=13  WR=91.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W02.  `H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=199  W=172/L=27  WR=86.4%
- Refine: exclude ZS=ZS3 drops 13/27 losers (48%)
- **Final: n=170  W=156/L=14  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=199  W=172/L=27  WR=86.4%
- Refine: exclude ZS=ZS3 drops 13/27 losers (48%)
- **Final: n=170  W=156/L=14  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=186  W=168/L=18  WR=90.3%
- Refine: exclude RSI=RSI4 drops 13/18 losers (72%)
- **Final: n=146  W=141/L=5  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W05.  `H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=182  W=159/L=23  WR=87.4%
- Refine: exclude T4=T4c drops 18/23 losers (78%)
- **Final: n=131  W=126/L=5  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=182  W=159/L=23  WR=87.4%
- Refine: exclude T4=T4c drops 18/23 losers (78%)
- **Final: n=131  W=126/L=5  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend AGAINST trade

### W07.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=182  W=159/L=23  WR=87.4%
- Refine: exclude T4=T4c drops 18/23 losers (78%)
- **Final: n=131  W=126/L=5  WR=96.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=181  W=155/L=26  WR=85.6%
- Refine: exclude session_bucket=london drops 9/26 losers (35%)
- **Final: n=154  W=137/L=17  WR=89.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W09.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=172  W=154/L=18  WR=89.5%
- Refine: exclude session_bucket=london drops 9/18 losers (50%)
- **Final: n=147  W=138/L=9  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W10.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude H60=H60c drops 19/24 losers (79%)
- **Final: n=131  W=126/L=5  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF60 neutral

### W11.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude H60=H60c drops 19/24 losers (79%)
- **Final: n=131  W=126/L=5  WR=96.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF60 neutral

### W12.  `T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=150  W=137/L=13  WR=91.3%
- Refine: exclude H60=H60b drops 5/13 losers (38%)
- **Final: n=145  W=137/L=8  WR=94.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W13.  `T4=T4a AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=150  W=137/L=13  WR=91.3%
- Refine: exclude H60=H60b drops 5/13 losers (38%)
- **Final: n=145  W=137/L=8  WR=94.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W14.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=141  W=121/L=20  WR=85.8%
- Refine: exclude ZS=ZS3 drops 11/20 losers (55%)
- **Final: n=118  W=109/L=9  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=137  W=117/L=20  WR=85.4%
- Refine: exclude T4=T4c drops 16/20 losers (80%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=137  W=117/L=20  WR=85.4%
- Refine: exclude T4=T4c drops 16/20 losers (80%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W17.  `T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude BBP=BBP6 drops 12/14 losers (86%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when deep above upper band

### W18.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=132  W=118/L=14  WR=89.4%
- Refine: exclude BBP=BBP6 drops 12/14 losers (86%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when deep above upper band

### W19.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=131  W=126/L=5  WR=96.2%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 2/5 losers (40%)
- **Final: n=120  W=117/L=3  WR=97.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when strategy=alpha_breakout_retest_v2

### W20.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude session_bucket=london drops 6/18 losers (33%)
- **Final: n=117  W=105/L=12  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when session=london

### W21.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude H60=H60c drops 15/18 losers (83%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF60 neutral

### W22.  `H20=H20a AND T1=T1a AND session_bucket=london`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude ZS=ZS5 drops 9/13 losers (69%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when zscore +2 to +3 deep overbought

### W23.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude ZS=ZS5 drops 9/13 losers (69%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  AVOID when zscore +2 to +3 deep overbought

### W24.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude ZS=ZS5 drops 9/13 losers (69%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when zscore +2 to +3 deep overbought

### W25.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=114  W=101/L=13  WR=88.6%
- Refine: exclude H60=H60b drops 5/13 losers (38%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=364  W=140/L=224  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (69/224 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=364  W=140/L=224  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (69/224 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L03.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=352  W=135/L=217  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (69/217 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L04.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=203  W=78/L=125  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (40/125 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L05.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=169  W=65/L=104  WR=38.5%
- Sharpen: sharpest is H60=H60e (89/104 of losers there)
- **Sharp: n=117  W=28/L=89  WR=23.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF60 strongly against

### L06.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=169  W=65/L=104  WR=38.5%
- Sharpen: sharpest is H60=H60e (89/104 of losers there)
- **Sharp: n=117  W=28/L=89  WR=23.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF60 strongly against

### L07.  `T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=162  W=60/L=102  WR=37.0%
- Sharpen: sharpest is H60=H60e (69/102 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF60 strongly against

### L08.  `H20=H20a AND H60=H60e AND RSI=RSI5`
- Raw: n=161  W=62/L=99  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (29/99 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=london_open

### L09.  `H20=H20a AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=161  W=62/L=99  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (29/99 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L10.  `H20=H20a AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=161  W=62/L=99  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (29/99 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L11.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=161  W=62/L=99  WR=38.5%
- Sharpen: sharpest is session_bucket=london_open (29/99 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=london_open

### L12.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=158  W=61/L=97  WR=38.6%
- Sharpen: sharpest is H20=H20a (37/97 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L13.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=155  W=56/L=99  WR=36.1%
- Sharpen: sharpest is RSI=RSI6 (25/99 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L14.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=155  W=56/L=99  WR=36.1%
- Sharpen: sharpest is RSI=RSI6 (25/99 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L15.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=155  W=56/L=99  WR=36.1%
- Sharpen: sharpest is RSI=RSI6 (25/99 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L16.  `H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=131  W=46/L=85  WR=35.1%
- Sharpen: sharpest is T4=T4c (69/85 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend AGAINST trade

### L17.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=131  W=46/L=85  WR=35.1%
- Sharpen: sharpest is T4=T4c (69/85 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend AGAINST trade

### L18.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=131  W=46/L=85  WR=35.1%
- Sharpen: sharpest is T4=T4c (69/85 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=128  W=42/L=86  WR=32.8%
- Sharpen: sharpest is BBP=BBP5 (47/86 of losers there)
- **Sharp: n=60  W=13/L=47  WR=21.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L20.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=125  W=36/L=89  WR=28.8%
- Sharpen: sharpest is RSI=RSI5 (69/89 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=125  W=36/L=89  WR=28.8%
- Sharpen: sharpest is RSI=RSI5 (69/89 of losers there)
- **Sharp: n=72  W=3/L=69  WR=4.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L22.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=124  W=35/L=89  WR=28.2%
- Sharpen: sharpest is session_bucket=london_open (46/89 of losers there)
- **Sharp: n=49  W=3/L=46  WR=6.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=120  W=46/L=74  WR=38.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 60-70 strong

### L24.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (55/72 of losers there)
- **Sharp: n=79  W=24/L=55  WR=30.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L25.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (55/72 of losers there)
- **Sharp: n=79  W=24/L=55  WR=30.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(49/35) | H60e(36/50) |
| T1 | T1a(57/41) | T1c(42/58) |
| T4 | T4a(64/37) | T4c(36/63) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/42) | short(43/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
