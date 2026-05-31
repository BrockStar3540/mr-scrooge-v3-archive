# GBP_JPY — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,970**  (W=1,692 / L=1,278)  -  WR: **57.0%**

## Session distribution

- ny_mid: n=716  W=389/L=327  WR=54.3%
- london_open: n=677  W=411/L=266  WR=60.7%
- ny_open: n=612  W=352/L=260  WR=57.5%
- asia: n=531  W=290/L=241  WR=54.6%
- london: n=305  W=172/L=133  WR=56.4%
- asia_late: n=74  W=43/L=31  WR=58.1%
- ny_close: n=54  W=34/L=20  WR=63.0%
- off_hours: n=1  W=1/L=0  WR=100.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude BBP=BBP5 drops 7/10 losers (70%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W02.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude BBP=BBP5 drops 7/10 losers (70%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W03.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude session_bucket=asia_late drops 2/6 losers (33%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia_late

### W04.  `H20=H20a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude T4=T4c drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude T4=T4c drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60e AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude session_bucket=london drops 8/9 losers (89%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=london

### W07.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude session_bucket=london drops 8/9 losers (89%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=london

### W08.  `H60=H60e AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude session_bucket=london drops 8/9 losers (89%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=london

### W09.  `H20=H20a AND T4=T4c AND BBP=BBP3 AND direction_exec=long`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=london_open drops 7/8 losers (88%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; middle of band  •  AVOID when session=london_open

### W10.  `H60=H60a AND T4=T4c AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; middle of band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W11.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=63  W=61/L=2  WR=96.8%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W12.  `H20=H20e AND H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 3/5 losers (60%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when strategy=alpha_pullback_v2

### W13.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 3/5 losers (60%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when strategy=alpha_pullback_v2

### W14.  `T1=T1a AND BBP=BBP3 AND session_bucket=ny_mid`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; session=ny_mid  •  AVOID when 4h trend WITH trade

### W15.  `T1=T1a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when 4h trend WITH trade

### W16.  `T4=T4a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude direction_exec=short drops 7/9 losers (78%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when short

### W17.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=56  W=54/L=2  WR=96.4%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W19.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=56  W=54/L=2  WR=96.4%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W21.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=54  W=52/L=2  WR=96.3%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W22.  `T4=T4a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=54  W=52/L=2  WR=96.3%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W23.  `T1=T1a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=54  W=51/L=3  WR=94.4%
- Refine: exclude session_bucket=ny_mid drops 2/3 losers (67%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W24.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=54  W=49/L=5  WR=90.7%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W25.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=54  W=49/L=5  WR=90.7%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=344  W=132/L=212  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_open (66/212 of losers there)
- **Sharp: n=81  W=15/L=66  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L02.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=344  W=132/L=212  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_open (66/212 of losers there)
- **Sharp: n=81  W=15/L=66  WR=18.5%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when session=ny_open

### L03.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=344  W=132/L=212  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_open (66/212 of losers there)
- **Sharp: n=81  W=15/L=66  WR=18.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=317  W=121/L=196  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=317  W=121/L=196  WR=38.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L05.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=317  W=121/L=196  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=317  W=121/L=196  WR=38.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=317  W=121/L=196  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=317  W=121/L=196  WR=38.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L07.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=279  W=96/L=183  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=279  W=96/L=183  WR=34.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L08.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=279  W=96/L=183  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=279  W=96/L=183  WR=34.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L09.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=279  W=96/L=183  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=279  W=96/L=183  WR=34.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=248  W=96/L=152  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=248  W=96/L=152  WR=38.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L11.  `T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=216  W=86/L=130  WR=39.8%
- Sharpen: sharpest is session_bucket=asia (52/130 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third  •  ONLY when session=asia

### L12.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=206  W=78/L=128  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=206  W=78/L=128  WR=37.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid

### L13.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=206  W=78/L=128  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=206  W=78/L=128  WR=37.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid

### L14.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=206  W=78/L=128  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=206  W=78/L=128  WR=37.9%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid

### L15.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=206  W=78/L=128  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=206  W=78/L=128  WR=37.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid

### L16.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=206  W=78/L=128  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=206  W=78/L=128  WR=37.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid

### L17.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=206  W=78/L=128  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=206  W=78/L=128  WR=37.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid

### L18.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=201  W=73/L=128  WR=36.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=201  W=73/L=128  WR=36.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L19.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=201  W=73/L=128  WR=36.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=201  W=73/L=128  WR=36.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L20.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=201  W=73/L=128  WR=36.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=201  W=73/L=128  WR=36.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L21.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=200  W=78/L=122  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (66/122 of losers there)
- **Sharp: n=81  W=15/L=66  WR=18.5%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=162  W=61/L=101  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=162  W=61/L=101  WR=37.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=ny_mid

### L23.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=162  W=61/L=101  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=162  W=61/L=101  WR=37.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid

### L24.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=162  W=61/L=101  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=162  W=61/L=101  WR=37.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid

### L25.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (31/97 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(41/47) |
| H60 | H60a(50/41) | H60e(43/50) |
| T1 | T1a(56/41) | T1c(44/59) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/44) | short(45/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
