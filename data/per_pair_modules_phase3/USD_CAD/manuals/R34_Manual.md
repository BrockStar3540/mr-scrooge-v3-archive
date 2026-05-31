# USD_CAD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,022**  (W=1,311 / L=711)  -  WR: **64.8%**

## Session distribution

- ny_mid: n=558  W=353/L=205  WR=63.3%
- ny_open: n=524  W=342/L=182  WR=65.3%
- london: n=245  W=162/L=83  WR=66.1%
- ny_close: n=242  W=157/L=85  WR=64.9%
- asia: n=200  W=134/L=66  WR=67.0%
- london_open: n=197  W=129/L=68  WR=65.5%
- off_hours: n=45  W=30/L=15  WR=66.7%
- asia_late: n=11  W=4/L=7  WR=36.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=172  W=149/L=23  WR=86.6%
- Refine: exclude session_bucket=london drops 11/23 losers (48%)
- **Final: n=161  W=149/L=12  WR=92.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W02.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=172  W=149/L=23  WR=86.6%
- Refine: exclude session_bucket=london drops 11/23 losers (48%)
- **Final: n=161  W=149/L=12  WR=92.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W03.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=172  W=149/L=23  WR=86.6%
- Refine: exclude session_bucket=london drops 11/23 losers (48%)
- **Final: n=161  W=149/L=12  WR=92.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W04.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=160  W=138/L=22  WR=86.2%
- Refine: exclude BBP=BBP2 drops 10/22 losers (45%)
- **Final: n=135  W=123/L=12  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when lower third

### W05.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=160  W=138/L=22  WR=86.2%
- Refine: exclude BBP=BBP2 drops 10/22 losers (45%)
- **Final: n=135  W=123/L=12  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W06.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=158  W=138/L=20  WR=87.3%
- Refine: exclude BBP=BBP2 drops 10/20 losers (50%)
- **Final: n=133  W=123/L=10  WR=92.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  AVOID when lower third

### W07.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=158  W=138/L=20  WR=87.3%
- Refine: exclude BBP=BBP2 drops 10/20 losers (50%)
- **Final: n=133  W=123/L=10  WR=92.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W08.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=156  W=136/L=20  WR=87.2%
- Refine: exclude BBP=BBP2 drops 10/20 losers (50%)
- **Final: n=131  W=121/L=10  WR=92.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when lower third

### W09.  `H20=H20e AND H60=H60a AND RSI=RSI5`
- Raw: n=152  W=131/L=21  WR=86.2%
- Refine: exclude T1=T1a drops 12/21 losers (57%)
- **Final: n=110  W=101/L=9  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when 1h trend WITH trade

### W10.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 13/17 losers (76%)
- **Final: n=100  W=96/L=4  WR=96.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W11.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=110  W=101/L=9  WR=91.8%
- Refine: exclude BBP=BBP2 drops 6/9 losers (67%)
- **Final: n=104  W=101/L=3  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W12.  `H20=H20e AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=110  W=101/L=9  WR=91.8%
- Refine: exclude BBP=BBP2 drops 6/9 losers (67%)
- **Final: n=104  W=101/L=3  WR=97.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when lower third

### W13.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude T1=T1c drops 8/10 losers (80%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W14.  `H60=H60a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude T1=T1c drops 6/7 losers (86%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W15.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude T1=T1c drops 6/7 losers (86%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

### W16.  `H60=H60a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude T1=T1c drops 12/12 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W17.  `H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude BBP=BBP5 drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W18.  `H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude BBP=BBP5 drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W19.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude BBP=BBP5 drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W20.  `H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=london drops 3/6 losers (50%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W21.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=london drops 3/6 losers (50%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W22.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=london drops 3/6 losers (50%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W23.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60b drops 8/12 losers (67%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W24.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60b drops 8/12 losers (67%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W25.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60b drops 8/12 losers (67%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=122  W=45/L=77  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/77 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L02.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=122  W=45/L=77  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/77 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L03.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=122  W=45/L=77  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/77 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L04.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI4 (52/67 of losers there)
- **Sharp: n=73  W=21/L=52  WR=28.8%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20a AND H60=H60e AND T1=T1a`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (44/61 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20a AND H60=H60e AND RSI=RSI5`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is T1=T1a (44/61 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L07.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (44/61 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is H60=H60e (25/59 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L09.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is H60=H60e (25/59 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L10.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is RSI=RSI5 (44/60 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is RSI=RSI5 (44/60 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20a AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is RSI=RSI5 (44/59 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  ONLY when RSI 60-70 strong

### L13.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=90  W=33/L=57  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_open (25/57 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L14.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=82  W=26/L=56  WR=31.7%
- Sharpen: sharpest is session_bucket=london_open (14/56 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L15.  `H60=H60e AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=73  W=21/L=52  WR=28.8%
- Sharpen: sharpest is session_bucket=london_open (12/52 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L16.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=73  W=21/L=52  WR=28.8%
- Sharpen: sharpest is session_bucket=london_open (12/52 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L17.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is T1=T1c (25/49 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L18.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is H20=H20a (23/43 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L19.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H20=H20a (21/43 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20a (21/41 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is RSI=RSI5 (22/37 of losers there)
- **Sharp: n=31  W=9/L=22  WR=29.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is BBP=BBP4 (26/44 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when upper third

### L23.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is BBP=BBP4 (26/44 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when upper third

### L24.  `H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=57  W=16/L=41  WR=28.1%
- Sharpen: sharpest is T4=T4a (10/41 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is ZS=ZS5 (15/37 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(49/31) | H60e(32/47) |
| T1 | — | — |
| T4 | T4a(56/43) | T4c(44/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
