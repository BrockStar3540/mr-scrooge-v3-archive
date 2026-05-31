# CHF_JPY — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,698**  (W=2,925 / L=1,773)  -  WR: **62.3%**

## Session distribution

- asia: n=2200  W=1390/L=810  WR=63.2%
- ny_close: n=924  W=567/L=357  WR=61.4%
- asia_late: n=543  W=353/L=190  WR=65.0%
- london: n=332  W=207/L=125  WR=62.3%
- off_hours: n=289  W=153/L=136  WR=52.9%
- ny_open: n=247  W=155/L=92  WR=62.8%
- london_open: n=152  W=95/L=57  WR=62.5%
- ny_mid: n=11  W=5/L=6  WR=45.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia_late`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude H20=H20d drops 12/17 losers (71%)
- **Final: n=94  W=89/L=5  WR=94.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia_late  •  AVOID when HTF20 mildly against

### W02.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=105  W=96/L=9  WR=91.4%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=off_hours

### W03.  `H60=H60e AND T1=T1c AND session_bucket=off_hours`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude ZS=ZS3 drops 9/15 losers (60%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude ZS=ZS3 drops 9/15 losers (60%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W06.  `H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when 4h trend AGAINST trade

### W07.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia_late`
- Raw: n=79  W=79/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia_late

### W08.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20b AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude BBP=BBP1 drops 4/10 losers (40%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when just touched lower band

### W10.  `H20=H20b AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude BBP=BBP1 drops 4/10 losers (40%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when just touched lower band

### W11.  `H20=H20b AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude BBP=BBP1 drops 4/10 losers (40%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  AVOID when just touched lower band

### W12.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=22  W=21/L=1  WR=95.5%**
- **Dir: LONG**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W13.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W14.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=24  W=23/L=1  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=24  W=23/L=1  WR=95.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20c AND T4=T4a AND RSI=RSI5`
- Raw: n=74  W=69/L=5  WR=93.2%
- Refine: exclude session_bucket=off_hours drops 5/5 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=off_hours

### W17.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=22  W=21/L=1  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W18.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W19.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude H20=H20b drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W20.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF20 strongly against

### W21.  `H20=H20a AND H60=H60e AND session_bucket=off_hours`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=off_hours  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=off_hours  •  AVOID when 4h trend AGAINST trade

### W23.  `H20=H20a AND H60=H60e AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=off_hours  •  AVOID when 4h trend AGAINST trade

### W24.  `H20=H20b AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=65  W=60/L=5  WR=92.3%
- Refine: exclude H60=H60e drops 5/5 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W25.  `H20=H20e AND H60=H60a AND session_bucket=asia_late`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude RSI=RSI4 drops 6/7 losers (86%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=144  W=53/L=91  WR=36.8%
- Sharpen: sharpest is RSI=RSI4 (66/91 of losers there)
- **Sharp: n=91  W=25/L=66  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L02.  `H20=H20a AND H60=H60a AND BBP=BBP5`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (19/81 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band  •  ONLY when RSI 60-70 strong

### L03.  `H20=H20a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (19/81 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band  •  ONLY when RSI 60-70 strong

### L04.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (19/81 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (19/81 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (19/81 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is RSI=RSI5 (38/77 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=126  W=33/L=93  WR=26.2%
- Sharpen: sharpest is H20=H20a (42/93 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=off_hours  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=121  W=43/L=78  WR=35.5%
- Sharpen: sharpest is H20=H20e (49/78 of losers there)
- **Sharp: n=65  W=16/L=49  WR=24.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L10.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=113  W=36/L=77  WR=31.9%
- Sharpen: sharpest is RSI=RSI5 (38/77 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L11.  `H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=113  W=39/L=74  WR=34.5%
- Sharpen: sharpest is RSI=RSI4 (52/74 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L12.  `H60=H60e AND T1=T1c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=112  W=39/L=73  WR=34.8%
- Sharpen: sharpest is RSI=RSI4 (52/73 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20d AND direction_exec=short AND session_bucket=asia`
- Raw: n=108  W=35/L=73  WR=32.4%
- Sharpen: sharpest is RSI=RSI5 (31/73 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: SHORT**  •  HTF20 mildly against; session=asia  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20d AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=108  W=35/L=73  WR=32.4%
- Sharpen: sharpest is RSI=RSI5 (31/73 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is T4=T4c (56/67 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: SHORT**  •  HTF20 neutral; upper third  •  ONLY when 4h trend AGAINST trade

### L16.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=100  W=29/L=71  WR=29.0%
- Sharpen: sharpest is H20=H20e (39/71 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L17.  `T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is ZS=ZS4 (34/71 of losers there)
- **Sharp: n=35  W=1/L=34  WR=2.9%**
- **Dir: LONG**  •  1h trend WITH trade; session=off_hours  •  ONLY when zscore +1 to +2 overbought

### L18.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia_late`
- Raw: n=97  W=30/L=67  WR=30.9%
- Sharpen: sharpest is H20=H20c (27/67 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia_late  •  ONLY when HTF20 neutral

### L19.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=97  W=36/L=61  WR=37.1%
- Sharpen: sharpest is ZS=ZS4 (42/61 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L20.  `H20=H20c AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=97  W=36/L=61  WR=37.1%
- Sharpen: sharpest is ZS=ZS4 (42/61 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L21.  `H20=H20c AND T4=T4c AND BBP=BBP4`
- Raw: n=96  W=31/L=65  WR=32.3%
- Sharpen: sharpest is session_bucket=asia (31/65 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; upper third  •  ONLY when session=asia

### L22.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is H20=H20c (27/62 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L23.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (22/58 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (22/58 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=92  W=31/L=61  WR=33.7%
- Sharpen: sharpest is RSI=RSI5 (38/61 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
