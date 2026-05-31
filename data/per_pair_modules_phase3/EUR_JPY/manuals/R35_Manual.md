# EUR_JPY — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,848**  (W=2,374 / L=1,474)  -  WR: **61.7%**

## Session distribution

- london_open: n=1181  W=725/L=456  WR=61.4%
- asia: n=905  W=560/L=345  WR=61.9%
- ny_mid: n=740  W=458/L=282  WR=61.9%
- ny_close: n=326  W=206/L=120  WR=63.2%
- ny_open: n=297  W=186/L=111  WR=62.6%
- london: n=208  W=130/L=78  WR=62.5%
- asia_late: n=113  W=69/L=44  WR=61.1%
- off_hours: n=78  W=40/L=38  WR=51.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=207  W=177/L=30  WR=85.5%
- Refine: exclude session_bucket=london_open drops 23/30 losers (77%)
- **Final: n=138  W=131/L=7  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W02.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=176  W=155/L=21  WR=88.1%
- Refine: exclude session_bucket=london_open drops 14/21 losers (67%)
- **Final: n=130  W=123/L=7  WR=94.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W03.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=170  W=153/L=17  WR=90.0%
- Refine: exclude T1=T1a drops 10/17 losers (59%)
- **Final: n=136  W=129/L=7  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W04.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=159  W=141/L=18  WR=88.7%
- Refine: exclude H60=H60a drops 10/18 losers (56%)
- **Final: n=147  W=139/L=8  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W05.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=148  W=133/L=15  WR=89.9%
- Refine: exclude session_bucket=london_open drops 15/15 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W06.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=148  W=133/L=15  WR=89.9%
- Refine: exclude session_bucket=london_open drops 15/15 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W07.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=143  W=125/L=18  WR=87.4%
- Refine: exclude T1=T1a drops 10/18 losers (56%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W08.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP5`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude RSI=RSI5 drops 19/19 losers (100%)
- **Final: n=91  W=91/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  AVOID when RSI 60-70 strong

### W09.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=119  W=111/L=8  WR=93.3%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=93  W=93/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W10.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=117  W=109/L=8  WR=93.2%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=91  W=91/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W11.  `H20=H20e AND T1=T1c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=110  W=103/L=7  WR=93.6%
- Refine: exclude H60=H60a drops 7/7 losers (100%)
- **Final: n=101  W=101/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W12.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude BBP=BBP3 drops 8/14 losers (57%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when middle of band

### W13.  `T1=T1a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 4/14 losers (29%)
- **Final: n=86  W=76/L=10  WR=88.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W14.  `RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 4/14 losers (29%)
- **Final: n=86  W=76/L=10  WR=88.4%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W15.  `T1=T1a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 4/14 losers (29%)
- **Final: n=86  W=76/L=10  WR=88.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W16.  `T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude H60=H60a drops 5/8 losers (62%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W18.  `T4=T4c AND BBP=BBP2 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude T1=T1a drops 7/10 losers (70%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W19.  `T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI5 drops 9/11 losers (82%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 60-70 strong

### W20.  `H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=82  W=81/L=1  WR=98.8%
- Refine: no further refinement
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold

### W21.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=82  W=81/L=1  WR=98.8%
- Refine: no further refinement
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold

### W22.  `T4=T4c AND RSI=RSI4 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude T1=T1a drops 7/8 losers (88%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold; session=asia  •  AVOID when 1h trend WITH trade

### W23.  `T4=T4a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude RSI=RSI5 drops 9/9 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; session=asia  •  AVOID when RSI 60-70 strong

### W24.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude RSI=RSI5 drops 9/9 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 60-70 strong

### W25.  `T1=T1a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI4 drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (22/90 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L02.  `H20=H20a AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is BBP=BBP5 (49/87 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L03.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=121  W=41/L=80  WR=33.9%
- Sharpen: sharpest is session_bucket=ny_close (13/80 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L04.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is BBP=BBP5 (46/75 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L05.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (22/71 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L06.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=101  W=36/L=65  WR=35.6%
- Sharpen: sharpest is ZS=ZS6 (28/65 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore >+3 extreme

### L07.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is RSI=RSI4 (48/61 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L08.  `H20=H20a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is T1=T1a (49/63 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band  •  ONLY when 1h trend WITH trade

### L09.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is T1=T1a (49/63 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is BBP=BBP5 (38/58 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L11.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (13/62 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L12.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (13/62 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L13.  `H20=H20a AND H60=H60a AND BBP=BBP5`
- Raw: n=92  W=32/L=60  WR=34.8%
- Sharpen: sharpest is T1=T1a (46/60 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band  •  ONLY when 1h trend WITH trade

### L14.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=92  W=32/L=60  WR=34.8%
- Sharpen: sharpest is T1=T1a (46/60 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L15.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=92  W=32/L=60  WR=34.8%
- Sharpen: sharpest is T1=T1a (46/60 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band  •  ONLY when 1h trend WITH trade

### L16.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is ZS=ZS6 (23/57 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore >+3 extreme

### L17.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=90  W=33/L=57  WR=36.7%
- Sharpen: sharpest is BBP=BBP6 (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

### L18.  `H20=H20a AND T4=T4a AND BBP=BBP5`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is T1=T1a (42/56 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when 1h trend WITH trade

### L19.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is T1=T1a (42/56 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L20.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is H60=H60a (27/56 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L21.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is RSI=RSI4 (48/53 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L22.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is RSI=RSI4 (48/53 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L23.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is T1=T1a (38/52 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when 1h trend WITH trade

### L24.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP5`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is T1=T1a (36/50 of losers there)
- **Sharp: n=50  W=14/L=36  WR=28.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when 1h trend WITH trade

### L25.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=81  W=31/L=50  WR=38.3%
- Sharpen: sharpest is T1=T1a (26/50 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=asia  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
