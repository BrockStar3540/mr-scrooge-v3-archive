# NZD_JPY — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,821**  (W=1,141 / L=680)  -  WR: **62.7%**

## Session distribution

- asia: n=797  W=494/L=303  WR=62.0%
- ny_close: n=353  W=223/L=130  WR=63.2%
- london_open: n=185  W=121/L=64  WR=65.4%
- off_hours: n=154  W=97/L=57  WR=63.0%
- london: n=132  W=84/L=48  WR=63.6%
- ny_open: n=93  W=53/L=40  WR=57.0%
- asia_late: n=63  W=41/L=22  WR=65.1%
- ny_mid: n=44  W=28/L=16  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=79  W=74/L=5  WR=93.7%
- Refine: exclude H60=H60d drops 5/5 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W02.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude H60=H60d drops 5/7 losers (71%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W03.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=70  W=65/L=5  WR=92.9%
- Refine: exclude H60=H60d drops 5/5 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W04.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=68  W=68/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral

### W05.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=68  W=68/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral

### W06.  `H20=H20a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude T1=T1c drops 5/7 losers (71%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W07.  `T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=63  W=60/L=3  WR=95.2%
- Refine: exclude BBP=BBP0 drops 3/3 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W08.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  AVOID when HTF20 slightly aligned

### W09.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 slightly aligned

### W10.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=59  W=59/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral

### W11.  `BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=59  W=54/L=5  WR=91.5%
- Refine: exclude H60=H60d drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W12.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude T4=T4c drops 4/6 losers (67%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W13.  `T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude H60=H60e drops 6/8 losers (75%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W14.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude ZS=ZS3 drops 5/6 losers (83%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude RSI=RSI3 drops 2/4 losers (50%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W16.  `H20=H20a AND T1=T1a AND ZS=ZS1`
- Raw: n=53  W=51/L=2  WR=96.2%
- Refine: exclude BBP=BBP0 drops 2/2 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W17.  `H20=H20a AND T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=53  W=51/L=2  WR=96.2%
- Refine: exclude BBP=BBP0 drops 2/2 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W18.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=53  W=49/L=4  WR=92.5%
- Refine: exclude RSI=RSI3 drops 2/4 losers (50%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude T1=T1c drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20a AND H60=H60a AND ZS=ZS1`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude T1=T1c drops 5/7 losers (71%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W21.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude T1=T1c drops 5/7 losers (71%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W22.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude H60=H60d drops 5/7 losers (71%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W23.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude session_bucket=ny_open drops 3/5 losers (60%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W24.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=49  W=47/L=2  WR=95.9%
- Refine: exclude BBP=BBP0 drops 2/2 losers (100%)
- **Final: n=15  W=15/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W25.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude RSI=RSI3 drops 2/4 losers (50%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is H20=H20b (23/49 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF20 slightly aligned

### L02.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (36/45 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L03.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is T4=T4c (32/46 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L04.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20b (23/41 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF20 slightly aligned

### L05.  `H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (31/39 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L06.  `T4=T4a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is H20=H20b (23/36 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF20 slightly aligned

### L07.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (20/36 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 60-70 strong

### L08.  `RSI=RSI4 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is ZS=ZS5 (18/36 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=off_hours  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND T1=T1c AND ZS=ZS2`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20e AND T4=T4c AND ZS=ZS2`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20e AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is RSI=RSI4 (29/37 of losers there)
- **Sharp: n=30  W=1/L=29  WR=3.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L16.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is RSI=RSI4 (29/37 of losers there)
- **Sharp: n=30  W=1/L=29  WR=3.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L17.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is H60=H60a (29/36 of losers there)
- **Sharp: n=30  W=1/L=29  WR=3.3%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L18.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is ZS=ZS5 (16/34 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (16/34 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20b AND H60=H60a AND RSI=RSI5`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L21.  `H20=H20b AND T1=T1a AND RSI=RSI5`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L22.  `H20=H20b AND T4=T4a AND RSI=RSI5`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L23.  `H20=H20b AND RSI=RSI5 AND direction_exec=long`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong  •  ONLY when session=asia

### L24.  `T4=T4a AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is BBP=BBP6 (11/32 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when deep above upper band

### L25.  `H20=H20b AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/37) | H20e(31/41) |
| H60 | H60a(51/44) | H60e(39/48) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/48) | short(45/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
