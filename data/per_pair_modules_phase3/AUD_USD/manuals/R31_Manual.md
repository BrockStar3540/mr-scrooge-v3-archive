# AUD_USD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,181**  (W=1,394 / L=787)  -  WR: **63.9%**

## Session distribution

- ny_mid: n=718  W=461/L=257  WR=64.2%
- london_open: n=468  W=297/L=171  WR=63.5%
- asia: n=466  W=288/L=178  WR=61.8%
- ny_open: n=294  W=190/L=104  WR=64.6%
- london: n=73  W=52/L=21  WR=71.2%
- ny_close: n=59  W=35/L=24  WR=59.3%
- asia_late: n=55  W=38/L=17  WR=69.1%
- off_hours: n=48  W=33/L=15  WR=68.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=139  W=119/L=20  WR=85.6%
- Refine: exclude T4=T4c drops 20/20 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W02.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=131  W=112/L=19  WR=85.5%
- Refine: exclude H20=H20c drops 7/19 losers (37%)
- **Final: n=114  W=102/L=12  WR=89.5%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W03.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=122  W=109/L=13  WR=89.3%
- Refine: exclude T4=T4c drops 13/13 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W04.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude T4=T4c drops 15/15 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20e AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=114  W=102/L=12  WR=89.5%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude T4=T4c drops 15/15 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W07.  `H20=H20a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W13.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 8/12 losers (67%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when session=ny_mid

### W15.  `T4=T4c AND BBP=BBP6 AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude RSI=RSI5 drops 7/11 losers (64%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; session=ny_mid  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20c AND T1=T1c AND ZS=ZS5`
- Raw: n=61  W=58/L=3  WR=95.1%
- Refine: exclude direction_exec=long drops 3/3 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when long

### W17.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=58  W=56/L=2  WR=96.6%
- Refine: exclude ZS=ZS4 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W18.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=58  W=56/L=2  WR=96.6%
- Refine: exclude ZS=ZS4 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W19.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=58  W=56/L=2  WR=96.6%
- Refine: exclude ZS=ZS4 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W20.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=58  W=56/L=2  WR=96.6%
- Refine: exclude ZS=ZS4 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W21.  `T1=T1c AND BBP=BBP5 AND session_bucket=ny_open`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude direction_exec=long drops 3/8 losers (38%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; session=ny_open  •  AVOID when long

### W22.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude direction_exec=long drops 3/8 losers (38%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought; session=ny_open  •  AVOID when long

### W23.  `H20=H20c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W24.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude RSI=RSI4 drops 5/7 losers (71%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W25.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude RSI=RSI4 drops 5/7 losers (71%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is H20=H20a (59/64 of losers there)
- **Sharp: n=80  W=21/L=59  WR=26.2%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=97  W=32/L=65  WR=33.0%
- Sharpen: sharpest is ZS=ZS5 (20/65 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is H20=H20a (57/62 of losers there)
- **Sharp: n=77  W=20/L=57  WR=26.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L04.  `H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=93  W=27/L=66  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (20/66 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=93  W=27/L=66  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (20/66 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=93  W=27/L=66  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (20/66 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is ZS=ZS5 (20/65 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is ZS=ZS5 (20/65 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=90  W=23/L=67  WR=25.6%
- Sharpen: sharpest is H20=H20b (13/67 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 slightly aligned

### L10.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=82  W=27/L=55  WR=32.9%
- Sharpen: sharpest is H20=H20a (55/55 of losers there)
- **Sharp: n=76  W=21/L=55  WR=27.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=80  W=21/L=59  WR=26.2%
- Sharpen: sharpest is T4=T4c (15/59 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=80  W=26/L=54  WR=32.5%
- Sharpen: sharpest is H20=H20a (54/54 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L13.  `H20=H20a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=77  W=20/L=57  WR=26.0%
- Sharpen: sharpest is T4=T4c (15/57 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=77  W=23/L=54  WR=29.9%
- Sharpen: sharpest is BBP=BBP5 (14/54 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L15.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=77  W=23/L=54  WR=29.9%
- Sharpen: sharpest is BBP=BBP5 (14/54 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=77  W=23/L=54  WR=29.9%
- Sharpen: sharpest is BBP=BBP5 (14/54 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L17.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=23/L=54  WR=29.9%
- Sharpen: sharpest is BBP=BBP5 (14/54 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L18.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=77  W=23/L=54  WR=29.9%
- Sharpen: sharpest is BBP=BBP5 (14/54 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L19.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=23/L=54  WR=29.9%
- Sharpen: sharpest is BBP=BBP5 (14/54 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=22/L=53  WR=29.3%
- Sharpen: sharpest is BBP=BBP5 (14/53 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L21.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=22/L=53  WR=29.3%
- Sharpen: sharpest is BBP=BBP5 (14/53 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when just touched upper band

### L22.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=62  W=17/L=45  WR=27.4%
- Sharpen: sharpest is T1=T1a (45/45 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L23.  `H20=H20e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=57  W=18/L=39  WR=31.6%
- Sharpen: sharpest is session_bucket=asia (16/39 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L24.  `H60=H60e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=57  W=18/L=39  WR=31.6%
- Sharpen: sharpest is session_bucket=asia (16/39 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L25.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=57  W=18/L=39  WR=31.6%
- Sharpen: sharpest is session_bucket=asia (16/39 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(57/48) | T1a(43/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
