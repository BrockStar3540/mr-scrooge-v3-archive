# EUR_GBP — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,037**  (W=668 / L=369)  -  WR: **64.4%**

## Session distribution

- asia: n=373  W=237/L=136  WR=63.5%
- ny_close: n=172  W=115/L=57  WR=66.9%
- london_open: n=143  W=88/L=55  WR=61.5%
- asia_late: n=124  W=91/L=33  WR=73.4%
- london: n=85  W=53/L=32  WR=62.4%
- off_hours: n=64  W=32/L=32  WR=50.0%
- ny_open: n=51  W=33/L=18  WR=64.7%
- ny_mid: n=25  W=19/L=6  WR=76.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W02.  `H20=H20d AND T4=T4c AND ZS=ZS5`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude H60=H60a drops 7/8 losers (88%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W03.  `H20=H20d AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude H60=H60a drops 7/8 losers (88%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W04.  `H20=H20d AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude H60=H60a drops 7/8 losers (88%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W05.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  AVOID when HTF20 strongly against

### W06.  `T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third  •  AVOID when HTF20 strongly against

### W07.  `T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third  •  AVOID when HTF20 strongly against

### W08.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  AVOID when HTF20 strongly against

### W09.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W10.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W11.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W12.  `T4=T4c AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W13.  `H20=H20a AND T4=T4c AND RSI=RSI5`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W16.  `H20=H20d AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade

### W18.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade

### W19.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade

### W20.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade

### W21.  `H20=H20d AND H60=H60e AND RSI=RSI5`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20d AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude H60=H60a drops 7/8 losers (88%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 mildly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W23.  `H20=H20d AND H60=H60e AND T1=T1c`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when 4h trend WITH trade

### W24.  `H20=H20d AND H60=H60e AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20d AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H60=H60a (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L02.  `H20=H20b AND T4=T4a AND direction_exec=long`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H60=H60a (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L03.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H60=H60a (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L04.  `H20=H20b AND T4=T4a AND RSI=RSI5`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is H60=H60a (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L05.  `H20=H20b AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is H60=H60a (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L06.  `H20=H20b AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is H60=H60a (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L07.  `H20=H20b AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L08.  `T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is H60=H60e (21/42 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L09.  `T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is H60=H60e (21/42 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L10.  `T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is H60=H60e (21/42 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L11.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is H60=H60e (21/42 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L12.  `T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=54  W=14/L=40  WR=25.9%
- Sharpen: sharpest is H60=H60a (18/40 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L13.  `H20=H20b AND T4=T4a AND ZS=ZS5`
- Raw: n=52  W=16/L=36  WR=30.8%
- Sharpen: sharpest is H60=H60a (10/36 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L14.  `H20=H20b AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=52  W=16/L=36  WR=30.8%
- Sharpen: sharpest is H60=H60a (10/36 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L15.  `H20=H20b AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=52  W=16/L=36  WR=30.8%
- Sharpen: sharpest is H60=H60a (10/36 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20b AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=49  W=13/L=36  WR=26.5%
- Sharpen: sharpest is H60=H60b (14/36 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L17.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is ZS=ZS5 (18/31 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20b AND T4=T4a AND session_bucket=asia`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is H60=H60a (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L19.  `H20=H20b AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is H60=H60a (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20b AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is H60=H60a (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L21.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is H60=H60a (8/30 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L22.  `T4=T4a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is H60=H60a (8/30 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20b AND T1=T1a AND BBP=BBP5`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (17/26 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; just touched upper band  •  ONLY when session=asia

### L24.  `H20=H20b AND BBP=BBP5 AND direction_exec=long`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (17/26 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; just touched upper band  •  ONLY when session=asia

### L25.  `H20=H20b AND T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (17/26 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(31/25) | H20b(24/32) |
| H60 | H60a(35/29) | — |
| T1 | T1c(59/45) | T1a(41/55) |
| T4 | T4c(66/40) | T4a(34/60) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(61/43) | long(39/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
