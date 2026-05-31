# GBP_CHF — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,429**  (W=865 / L=564)  -  WR: **60.5%**

## Session distribution

- ny_mid: n=555  W=330/L=225  WR=59.5%
- ny_open: n=290  W=178/L=112  WR=61.4%
- ny_close: n=236  W=164/L=72  WR=69.5%
- london_open: n=185  W=114/L=71  WR=61.6%
- london: n=112  W=53/L=59  WR=47.3%
- off_hours: n=30  W=18/L=12  WR=60.0%
- asia: n=21  W=8/L=13  WR=38.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=122  W=105/L=17  WR=86.1%
- Refine: exclude H20=H20e drops 8/17 losers (47%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W02.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 9/12 losers (75%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W03.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 9/12 losers (75%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W04.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 9/12 losers (75%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W05.  `H20=H20e AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W06.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W07.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W08.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W09.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W10.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W11.  `T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude ZS=ZS5 drops 6/10 losers (60%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W12.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W13.  `T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W14.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W15.  `H20=H20a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H60=H60a drops 5/7 losers (71%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W16.  `T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=60  W=53/L=7  WR=88.3%
- Refine: exclude H60=H60a drops 5/7 losers (71%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=60  W=53/L=7  WR=88.3%
- Refine: exclude H60=H60a drops 5/7 losers (71%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20e AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=47  W=42/L=5  WR=89.4%**
- **Dir: ?**  •  HTF20 strongly against; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W19.  `H20=H20a AND T1=T1c AND RSI=RSI4`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 2/4 losers (50%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when strategy=alpha_pullback_v2

### W20.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 mildly against

### W21.  `T4=T4a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 mildly against

### W22.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude ZS=ZS5 drops 5/7 losers (71%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W23.  `H20=H20a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=55  W=52/L=3  WR=94.5%
- Refine: exclude ZS=ZS3 drops 3/3 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=55  W=52/L=3  WR=94.5%
- Refine: exclude ZS=ZS3 drops 3/3 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=55  W=52/L=3  WR=94.5%
- Refine: exclude ZS=ZS3 drops 3/3 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND T4=T4c`
- Raw: n=126  W=50/L=76  WR=39.7%
- Sharpen: sharpest is RSI=RSI4 (32/76 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L02.  `H20=H20a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 mildly against

### L03.  `H20=H20a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L04.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L05.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L06.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L07.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 mildly against

### L08.  `H20=H20a AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L09.  `H20=H20a AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L10.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 mildly against

### L11.  `H20=H20a AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L12.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L13.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L14.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60d (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 mildly against

### L15.  `H20=H20a AND T4=T4c AND ZS=ZS4`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is H60=H60d (15/47 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L16.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is H60=H60d (15/47 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L17.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is H60=H60d (15/47 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L18.  `H20=H20a AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is H60=H60d (15/47 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L19.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=68  W=22/L=46  WR=32.4%
- Sharpen: sharpest is H20=H20e (21/46 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L20.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is ZS=ZS6 (23/40 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L21.  `H20=H20a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H60=H60d (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L22.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H60=H60d (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L23.  `T4=T4c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H60=H60d (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L24.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H60=H60d (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L25.  `H20=H20a AND T1=T1c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H60=H60d (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(54/47) | T1a(46/53) |
| T4 | T4a(56/45) | T4c(44/55) |
| BBP | — | — |
| RSI | RSI5(49/42) | — |
| ZS | — | ZS6(5/10) |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | ny_close(19/13) | — |

*Read: `bucket(winner%/loser%)`.*
