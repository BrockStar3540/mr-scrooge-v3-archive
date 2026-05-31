# CAD_JPY — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,847**  (W=1,163 / L=684)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=754  W=465/L=289  WR=61.7%
- london_open: n=423  W=281/L=142  WR=66.4%
- asia: n=314  W=201/L=113  WR=64.0%
- london: n=127  W=70/L=57  WR=55.1%
- ny_open: n=89  W=53/L=36  WR=59.6%
- ny_close: n=81  W=54/L=27  WR=66.7%
- asia_late: n=39  W=25/L=14  WR=64.1%
- off_hours: n=20  W=14/L=6  WR=70.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude H20=H20a drops 21/23 losers (91%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude H20=H20a drops 21/23 losers (91%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W03.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude H20=H20a drops 21/23 losers (91%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude H20=H20a drops 21/23 losers (91%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude H20=H20a drops 21/23 losers (91%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W06.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude H20=H20a drops 21/23 losers (91%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W07.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: exclude H20=H20a drops 24/24 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W08.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=168  W=147/L=21  WR=87.5%
- Refine: exclude H20=H20a drops 21/21 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=168  W=147/L=21  WR=87.5%
- Refine: exclude H20=H20a drops 21/21 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=168  W=147/L=21  WR=87.5%
- Refine: exclude H20=H20a drops 21/21 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W12.  `T1=T1a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W13.  `T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W14.  `RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W15.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W16.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W17.  `H60=H60a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W18.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W19.  `T1=T1a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W20.  `T4=T4a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude BBP=BBP6 drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W21.  `H20=H20a AND H60=H60a AND BBP=BBP5`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI7 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band  •  AVOID when RSI>80 extreme overbought

### W22.  `H20=H20a AND T1=T1a AND BBP=BBP5`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI7 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band  •  AVOID when RSI>80 extreme overbought

### W23.  `H20=H20a AND T4=T4a AND BBP=BBP5`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI7 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when RSI>80 extreme overbought

### W24.  `H20=H20a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI7 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band  •  AVOID when RSI>80 extreme overbought

### W25.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP5`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI7 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; just touched upper band  •  AVOID when RSI>80 extreme overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is H20=H20a (40/109 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is H20=H20a (40/109 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L03.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is H20=H20a (40/109 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is H20=H20a (40/109 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L05.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is H20=H20a (40/109 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L06.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is H20=H20a (40/109 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L07.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=172  W=64/L=108  WR=37.2%
- Sharpen: sharpest is H20=H20a (37/108 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is H20=H20a (37/106 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is H20=H20a (37/106 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L10.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is H20=H20a (37/106 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60e AND T1=T1c AND BBP=BBP5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

### L12.  `H60=H60e AND T4=T4c AND BBP=BBP5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

### L13.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L14.  `H60=H60e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band  •  ONLY when RSI 70-80 overbought

### L15.  `T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

### L16.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L17.  `T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

### L18.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L19.  `T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

### L20.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L21.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

### L22.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L23.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

### L24.  `H60=H60e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L25.  `H60=H60e AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is RSI=RSI6 (45/61 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(49/43) | H20e(44/52) |
| H60 | H60a(52/45) | H60e(48/55) |
| T1 | T1a(52/45) | T1c(48/55) |
| T4 | T4a(55/42) | T4c(45/58) |
| BBP | — | — |
| RSI | RSI5(52/45) | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/45) | short(48/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
