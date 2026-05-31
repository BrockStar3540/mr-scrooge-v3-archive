# AUD_USD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,383**  (W=859 / L=524)  -  WR: **62.1%**

## Session distribution

- ny_mid: n=456  W=289/L=167  WR=63.4%
- asia: n=304  W=185/L=119  WR=60.9%
- london_open: n=187  W=110/L=77  WR=58.8%
- ny_open: n=162  W=99/L=63  WR=61.1%
- ny_close: n=124  W=74/L=50  WR=59.7%
- london: n=88  W=58/L=30  WR=65.9%
- asia_late: n=32  W=24/L=8  WR=75.0%
- off_hours: n=30  W=20/L=10  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W02.  `T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 9/13 losers (69%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W03.  `H20=H20e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W04.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W05.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W06.  `H20=H20e AND T1=T1c AND BBP=BBP2`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=77  W=70/L=7  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  AVOID when session=ny_open

### W07.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 4/9 losers (44%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  AVOID when session=ny_open

### W08.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W10.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP4 drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when upper third

### W12.  `H20=H20e AND T4=T4a AND BBP=BBP2`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=ny_open

### W13.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=ny_open

### W14.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=ny_open

### W15.  `T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 aligned WITH trade

### W16.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude BBP=BBP4 drops 3/8 losers (38%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W17.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W18.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W19.  `H20=H20e AND T4=T4a AND ZS=ZS2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W20.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W21.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W22.  `H20=H20e AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W23.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W24.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (9/55 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L02.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is T1=T1c (29/58 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L03.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is T4=T4c (29/47 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (9/46 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is RSI=RSI2 (13/43 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L06.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is T1=T1c (29/49 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L07.  `H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4c (22/41 of losers there)
- **Sharp: n=31  W=9/L=22  WR=29.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  ONLY when 4h trend AGAINST trade

### L08.  `H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_mid (20/40 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L09.  `H20=H20e AND H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is T4=T4c (25/38 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L10.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (13/39 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L11.  `H20=H20e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is T4=T4c (35/41 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=59  W=12/L=47  WR=20.3%
- Sharpen: sharpest is T1=T1c (21/47 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L13.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is T4=T4c (29/39 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is T4=T4c (29/39 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is T4=T4c (29/39 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=57  W=16/L=41  WR=28.1%
- Sharpen: sharpest is T1=T1c (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L17.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=57  W=16/L=41  WR=28.1%
- Sharpen: sharpest is T1=T1c (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L18.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=57  W=16/L=41  WR=28.1%
- Sharpen: sharpest is T1=T1c (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is T1=T1a (20/34 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when 1h trend WITH trade

### L20.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is T1=T1a (20/34 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is T1=T1a (20/34 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when 1h trend WITH trade

### L22.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H20=H20a (12/33 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: sharpest is BBP=BBP0 (10/37 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when deep below lower band

### L24.  `T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=52  W=15/L=37  WR=28.8%
- Sharpen: sharpest is RSI=RSI2 (21/37 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L25.  `T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=52  W=15/L=37  WR=28.8%
- Sharpen: sharpest is RSI=RSI2 (21/37 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(55/45) | H60a(41/51) |
| T1 | — | — |
| T4 | T4a(59/43) | T4c(41/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
