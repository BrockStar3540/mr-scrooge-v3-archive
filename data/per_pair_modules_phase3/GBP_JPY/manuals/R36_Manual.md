# GBP_JPY — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,801**  (W=2,220 / L=1,581)  -  WR: **58.4%**

## Session distribution

- london_open: n=1252  W=759/L=493  WR=60.6%
- ny_mid: n=978  W=545/L=433  WR=55.7%
- asia: n=899  W=520/L=379  WR=57.8%
- ny_open: n=260  W=163/L=97  WR=62.7%
- london: n=185  W=110/L=75  WR=59.5%
- off_hours: n=87  W=44/L=43  WR=50.6%
- asia_late: n=73  W=45/L=28  WR=61.6%
- ny_close: n=67  W=34/L=33  WR=50.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude T1=T1c drops 15/15 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI5`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W04.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W05.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W06.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W09.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W10.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W11.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W12.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W13.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W14.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W15.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W16.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W17.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W18.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W19.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W20.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W21.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W22.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when 4h trend AGAINST trade

### W23.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when 4h trend AGAINST trade

### W24.  `T1=T1c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20b drops 6/11 losers (55%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 slightly aligned

### W25.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H20=H20b drops 9/10 losers (90%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=241  W=94/L=147  WR=39.0%
- Sharpen: sharpest is ZS=ZS4 (40/147 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L02.  `H20=H20a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=213  W=84/L=129  WR=39.4%
- Sharpen: sharpest is ZS=ZS1 (30/129 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=207  W=78/L=129  WR=37.7%
- Sharpen: sharpest is ZS=ZS1 (30/129 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=207  W=78/L=129  WR=37.7%
- Sharpen: sharpest is ZS=ZS1 (30/129 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=207  W=78/L=129  WR=37.7%
- Sharpen: sharpest is ZS=ZS1 (30/129 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=195  W=73/L=122  WR=37.4%
- Sharpen: sharpest is ZS=ZS1 (30/122 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=150  W=59/L=91  WR=39.3%
- Sharpen: sharpest is RSI=RSI5 (36/91 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L08.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=146  W=58/L=88  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (36/88 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L09.  `T1=T1a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=141  W=54/L=87  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (43/87 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  ONLY when session=asia

### L10.  `T1=T1a AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=141  W=54/L=87  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (43/87 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=asia

### L11.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (58/88 of losers there)
- **Sharp: n=70  W=12/L=58  WR=17.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L12.  `T1=T1a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is session_bucket=asia (37/74 of losers there)
- **Sharp: n=53  W=16/L=37  WR=30.2%**
- **Dir: LONG**  •  1h trend WITH trade; middle of band  •  ONLY when session=asia

### L13.  `T1=T1a AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is session_bucket=asia (37/74 of losers there)
- **Sharp: n=53  W=16/L=37  WR=30.2%**
- **Dir: LONG**  •  1h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=asia

### L14.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=120  W=37/L=83  WR=30.8%
- Sharpen: sharpest is T1=T1c (65/83 of losers there)
- **Sharp: n=81  W=16/L=65  WR=19.8%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60a AND T1=T1a AND BBP=BBP3`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (37/72 of losers there)
- **Sharp: n=53  W=16/L=37  WR=30.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band  •  ONLY when session=asia

### L16.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (37/72 of losers there)
- **Sharp: n=53  W=16/L=37  WR=30.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=asia

### L17.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (37/72 of losers there)
- **Sharp: n=53  W=16/L=37  WR=30.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band  •  ONLY when session=asia

### L18.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=118  W=38/L=80  WR=32.2%
- Sharpen: sharpest is BBP=BBP4 (32/80 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when upper third

### L19.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is T1=T1c (44/71 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L20.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=116  W=33/L=83  WR=28.4%
- Sharpen: sharpest is T1=T1c (65/83 of losers there)
- **Sharp: n=77  W=12/L=65  WR=15.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L21.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=116  W=33/L=83  WR=28.4%
- Sharpen: sharpest is T1=T1c (65/83 of losers there)
- **Sharp: n=77  W=12/L=65  WR=15.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L22.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=115  W=35/L=80  WR=30.4%
- Sharpen: sharpest is H60=H60a (65/80 of losers there)
- **Sharp: n=77  W=12/L=65  WR=15.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is RSI=RSI5 (36/69 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is RSI=RSI5 (36/67 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60e AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is BBP=BBP6 (30/69 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(43/49) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
