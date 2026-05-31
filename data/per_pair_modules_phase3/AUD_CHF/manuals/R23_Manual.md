# AUD_CHF — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,956**  (W=1,250 / L=706)  -  WR: **63.9%**

## Session distribution

- asia: n=844  W=542/L=302  WR=64.2%
- ny_close: n=275  W=176/L=99  WR=64.0%
- london_open: n=232  W=138/L=94  WR=59.5%
- london: n=213  W=131/L=82  WR=61.5%
- ny_mid: n=122  W=79/L=43  WR=64.8%
- ny_open: n=118  W=82/L=36  WR=69.5%
- asia_late: n=94  W=62/L=32  WR=66.0%
- off_hours: n=58  W=40/L=18  WR=69.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude session_bucket=london_open drops 4/15 losers (27%)
- **Final: n=99  W=88/L=11  WR=88.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W02.  `H20=H20e AND H60=H60e AND BBP=BBP1`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 5/13 losers (38%)
- **Final: n=72  W=64/L=8  WR=88.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  AVOID when RSI 50-60 upper neutral

### W03.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 5/13 losers (38%)
- **Final: n=72  W=64/L=8  WR=88.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 50-60 upper neutral

### W04.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND direction_exec=short`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 5/13 losers (38%)
- **Final: n=72  W=64/L=8  WR=88.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  AVOID when RSI 50-60 upper neutral

### W05.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude session_bucket=ny_close drops 3/11 losers (27%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W06.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude session_bucket=ny_close drops 3/11 losers (27%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W07.  `H60=H60e AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W08.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude RSI=RSI4 drops 6/12 losers (50%)
- **Final: n=58  W=52/L=6  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 50-60 upper neutral

### W09.  `H60=H60e AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W10.  `H60=H60e AND BBP=BBP1 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=asia drops 8/12 losers (67%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W11.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI4 drops 5/11 losers (45%)
- **Final: n=58  W=52/L=6  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 2/9 losers (22%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W13.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 3/11 losers (27%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W14.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude session_bucket=london_open drops 3/9 losers (33%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W15.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 4/10 losers (40%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W17.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=london_open drops 3/9 losers (33%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W18.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude session_bucket=asia_late drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W19.  `H20=H20b AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; session=asia  •  AVOID when 4h trend WITH trade

### W20.  `H20=H20b AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 slightly aligned; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20b AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20a AND H60=H60b AND direction_exec=long`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude session_bucket=london_open drops 4/5 losers (80%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 slightly aligned  •  AVOID when session=london_open

### W23.  `H20=H20b AND T1=T1c AND BBP=BBP4`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude T4=T4a drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; upper third  •  AVOID when 4h trend WITH trade

### W24.  `H20=H20b AND T1=T1c AND ZS=ZS4`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude T4=T4a drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20b AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude T4=T4a drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=90  W=33/L=57  WR=36.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=90  W=33/L=57  WR=36.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral

### L02.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=90  W=33/L=57  WR=36.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=90  W=33/L=57  WR=36.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral

### L03.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is RSI=RSI3 (31/46 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L04.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is RSI=RSI3 (31/46 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L05.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T4=T4c (28/45 of losers there)
- **Sharp: n=40  W=12/L=28  WR=30.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L06.  `H20=H20d AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (7/44 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

### L07.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is T4=T4a (19/46 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: sharpest is ZS=ZS5 (22/43 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is T4=T4c (28/42 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is T4=T4c (28/39 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is T4=T4c (28/39 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND H60=H60e AND BBP=BBP5`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is T4=T4c (28/37 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is T4=T4c (28/37 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is T4=T4c (28/37 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band  •  ONLY when 4h trend AGAINST trade

### L15.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is T4=T4c (24/36 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is T4=T4c (24/36 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (26/35 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L18.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is T4=T4a (24/35 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london  •  ONLY when 4h trend WITH trade

### L19.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is session_bucket=asia (24/34 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L20.  `H20=H20d AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: sharpest is RSI=RSI3 (8/37 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: ?**  •  HTF20 mildly against; upper third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20d AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: sharpest is RSI=RSI3 (8/37 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: ?**  •  HTF20 mildly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 40-50 lower neutral

### L22.  `H20=H20d AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: sharpest is RSI=RSI3 (8/37 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: ?**  •  HTF20 mildly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 40-50 lower neutral

### L23.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is T4=T4c (24/33 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20e AND H60=H60d AND direction_exec=short`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: sharpest is BBP=BBP2 (15/35 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against  •  ONLY when lower third

### L25.  `H60=H60e AND RSI=RSI4 AND session_bucket=london`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is T4=T4a (23/32 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(44/39) | — |
| T1 | T1c(54/46) | T1a(45/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
