# NZD_CAD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,183**  (W=1,330 / L=853)  -  WR: **60.9%**

## Session distribution

- asia: n=597  W=349/L=248  WR=58.5%
- ny_mid: n=450  W=286/L=164  WR=63.6%
- ny_close: n=433  W=268/L=165  WR=61.9%
- ny_open: n=276  W=157/L=119  WR=56.9%
- london_open: n=157  W=102/L=55  WR=65.0%
- london: n=123  W=77/L=46  WR=62.6%
- off_hours: n=106  W=66/L=40  WR=62.3%
- asia_late: n=41  W=25/L=16  WR=61.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=159  W=139/L=20  WR=87.4%
- Refine: exclude T4=T4c drops 13/20 losers (65%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W02.  `H20=H20e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=159  W=139/L=20  WR=87.4%
- Refine: exclude T4=T4c drops 13/20 losers (65%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W03.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=159  W=139/L=20  WR=87.4%
- Refine: exclude T4=T4c drops 13/20 losers (65%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20e AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=159  W=139/L=20  WR=87.4%
- Refine: exclude T4=T4c drops 13/20 losers (65%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=159  W=139/L=20  WR=87.4%
- Refine: exclude T4=T4c drops 13/20 losers (65%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=114  W=103/L=11  WR=90.4%
- Refine: exclude session_bucket=ny_close drops 11/11 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W07.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H60=H60b drops 5/16 losers (31%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W08.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude H60=H60b drops 4/15 losers (27%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W09.  `H20=H20e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude ZS=ZS4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W10.  `H20=H20e AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude ZS=ZS4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude ZS=ZS4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W12.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude ZS=ZS4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W13.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 strongly against

### W14.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF20 strongly against

### W15.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: no further refinement
- **Final: n=84  W=73/L=11  WR=86.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong; session=ny_close

### W16.  `H20=H20b AND H60=H60a AND BBP=BBP5`
- Raw: n=83  W=80/L=3  WR=96.4%
- Refine: exclude session_bucket=ny_open drops 3/3 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; just touched upper band  •  AVOID when session=ny_open

### W17.  `H20=H20b AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=83  W=80/L=3  WR=96.4%
- Refine: exclude session_bucket=ny_open drops 3/3 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W18.  `H20=H20b AND H60=H60a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=83  W=80/L=3  WR=96.4%
- Refine: exclude session_bucket=ny_open drops 3/3 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W19.  `H60=H60a AND T4=T4a AND BBP=BBP5`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI6 drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when RSI 70-80 overbought

### W20.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI6 drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when RSI 70-80 overbought

### W21.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI6 drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 70-80 overbought

### W22.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI6 drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when RSI 70-80 overbought

### W23.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20b drops 11/12 losers (92%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W24.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W25.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude ZS=ZS4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (60/128 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L02.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (60/128 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L03.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (60/128 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L04.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=175  W=57/L=118  WR=32.6%
- Sharpen: sharpest is RSI=RSI5 (35/118 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=175  W=57/L=118  WR=32.6%
- Sharpen: sharpest is RSI=RSI5 (35/118 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L06.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=175  W=57/L=118  WR=32.6%
- Sharpen: sharpest is RSI=RSI5 (35/118 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20a AND H60=H60e AND RSI=RSI5`
- Raw: n=167  W=60/L=107  WR=35.9%
- Sharpen: sharpest is T4=T4c (63/107 of losers there)
- **Sharp: n=87  W=24/L=63  WR=27.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20a AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=167  W=60/L=107  WR=35.9%
- Sharpen: sharpest is T4=T4c (63/107 of losers there)
- **Sharp: n=87  W=24/L=63  WR=27.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=167  W=60/L=107  WR=35.9%
- Sharpen: sharpest is T4=T4c (63/107 of losers there)
- **Sharp: n=87  W=24/L=63  WR=27.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20d AND H60=H60e AND RSI=RSI6`
- Raw: n=165  W=61/L=104  WR=37.0%
- Sharpen: sharpest is ZS=ZS5 (48/104 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H20=H20d AND T1=T1c AND RSI=RSI6`
- Raw: n=163  W=62/L=101  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (48/101 of losers there)
- **Sharp: n=68  W=20/L=48  WR=29.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20d AND T4=T4c AND RSI=RSI6`
- Raw: n=163  W=62/L=101  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (48/101 of losers there)
- **Sharp: n=68  W=20/L=48  WR=29.4%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H20=H20d AND RSI=RSI6 AND direction_exec=short`
- Raw: n=163  W=62/L=101  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (48/101 of losers there)
- **Sharp: n=68  W=20/L=48  WR=29.4%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20d AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=163  W=62/L=101  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (48/101 of losers there)
- **Sharp: n=68  W=20/L=48  WR=29.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20d AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=163  W=62/L=101  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (48/101 of losers there)
- **Sharp: n=68  W=20/L=48  WR=29.4%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20d AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=163  W=62/L=101  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (48/101 of losers there)
- **Sharp: n=68  W=20/L=48  WR=29.4%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=159  W=60/L=99  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (78/99 of losers there)
- **Sharp: n=112  W=34/L=78  WR=30.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=156  W=59/L=97  WR=37.8%
- Sharpen: sharpest is T4=T4c (60/97 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L19.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is ZS=ZS5 (71/92 of losers there)
- **Sharp: n=105  W=34/L=71  WR=32.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is ZS=ZS5 (71/92 of losers there)
- **Sharp: n=105  W=34/L=71  WR=32.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is ZS=ZS5 (71/92 of losers there)
- **Sharp: n=105  W=34/L=71  WR=32.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20d AND H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=151  W=57/L=94  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (48/94 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20d AND H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=151  W=57/L=94  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (48/94 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20d AND H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=151  W=57/L=94  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (48/94 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=145  W=44/L=101  WR=30.3%
- Sharpen: sharpest is RSI=RSI5 (18/101 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(31/23), H20b(26/20) | H20a(23/31), H20d(20/26) |
| H60 | H60a(53/40) | H60e(40/54) |
| T1 | T1a(58/38) | T1c(42/62) |
| T4 | T4a(57/41) | T4c(43/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/38) | short(42/62) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
