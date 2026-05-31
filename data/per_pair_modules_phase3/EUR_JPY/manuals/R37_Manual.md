# EUR_JPY — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,848**  (W=3,006 / L=1,842)  -  WR: **62.0%**

## Session distribution

- asia: n=2073  W=1293/L=780  WR=62.4%
- ny_close: n=859  W=512/L=347  WR=59.6%
- london: n=601  W=391/L=210  WR=65.1%
- ny_open: n=499  W=311/L=188  WR=62.3%
- off_hours: n=255  W=134/L=121  WR=52.5%
- ny_mid: n=203  W=132/L=71  WR=65.0%
- asia_late: n=187  W=124/L=63  WR=66.3%
- london_open: n=171  W=109/L=62  WR=63.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=142  W=123/L=19  WR=86.6%
- Refine: exclude session_bucket=ny_open drops 9/19 losers (47%)
- **Final: n=122  W=112/L=10  WR=91.8%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W02.  `H20=H20a AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=138  W=118/L=20  WR=85.5%
- Refine: exclude RSI=RSI3 drops 10/20 losers (50%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when RSI 40-50 lower neutral

### W03.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=136  W=117/L=19  WR=86.0%
- Refine: exclude BBP=BBP2 drops 9/19 losers (47%)
- **Final: n=116  W=106/L=10  WR=91.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_open  •  AVOID when lower third

### W04.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude T1=T1c drops 8/18 losers (44%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 1h trend AGAINST trade

### W05.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude BBP=BBP2 drops 9/16 losers (56%)
- **Final: n=105  W=98/L=7  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when lower third

### W06.  `H60=H60b AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude BBP=BBP6 drops 15/17 losers (88%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W07.  `H60=H60b AND ZS=ZS5 AND direction_exec=long`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20c drops 7/17 losers (41%)
- **Final: n=110  W=100/L=10  WR=90.9%**
- **Dir: LONG**  •  HTF60 slightly aligned; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W08.  `H60=H60b AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude BBP=BBP6 drops 14/16 losers (88%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W09.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude BBP=BBP2 drops 9/16 losers (56%)
- **Final: n=103  W=96/L=7  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when lower third

### W10.  `H20=H20e AND H60=H60b AND ZS=ZS5`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude BBP=BBP6 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W11.  `H60=H60b AND T4=T4c AND ZS=ZS5`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude BBP=BBP6 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W12.  `H20=H20e AND H60=H60b AND T4=T4c AND ZS=ZS5`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude BBP=BBP6 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W13.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=ny_open drops 7/15 losers (47%)
- **Final: n=99  W=91/L=8  WR=91.9%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W14.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=ny_open drops 7/15 losers (47%)
- **Final: n=99  W=91/L=8  WR=91.9%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W15.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude session_bucket=ny_close drops 6/11 losers (55%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W16.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W17.  `H60=H60b AND T1=T1a AND ZS=ZS5`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude H20=H20c drops 6/14 losers (43%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W18.  `H20=H20e AND H60=H60b AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude BBP=BBP6 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W19.  `H60=H60b AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude BBP=BBP6 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W20.  `H20=H20e AND H60=H60b AND ZS=ZS5 AND direction_exec=long`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude BBP=BBP6 drops 8/10 losers (80%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W21.  `H60=H60b AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude BBP=BBP6 drops 8/10 losers (80%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W22.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude BBP=BBP2 drops 9/10 losers (90%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when lower third

### W23.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude BBP=BBP2 drops 9/10 losers (90%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when lower third

### W24.  `BBP=BBP5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T1=T1c drops 9/13 losers (69%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  just touched upper band; session=asia  •  AVOID when 1h trend AGAINST trade

### W25.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T1=T1c drops 9/13 losers (69%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=202  W=80/L=122  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (30/122 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L02.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=177  W=63/L=114  WR=35.6%
- Sharpen: sharpest is session_bucket=ny_open (29/114 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L03.  `T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=150  W=57/L=93  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (43/93 of losers there)
- **Sharp: n=46  W=3/L=43  WR=6.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L04.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=150  W=57/L=93  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (43/93 of losers there)
- **Sharp: n=46  W=3/L=43  WR=6.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L05.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H20=H20e (50/80 of losers there)
- **Sharp: n=66  W=16/L=50  WR=24.2%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L06.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=128  W=49/L=79  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_open (20/79 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L07.  `BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is T4=T4a (54/72 of losers there)
- **Sharp: n=82  W=28/L=54  WR=34.1%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L08.  `BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is T4=T4a (54/72 of losers there)
- **Sharp: n=82  W=28/L=54  WR=34.1%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L09.  `H60=H60e AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (43/73 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L10.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=115  W=45/L=70  WR=39.1%
- Sharpen: sharpest is H20=H20a (59/70 of losers there)
- **Sharp: n=85  W=26/L=59  WR=30.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20d AND T4=T4c AND direction_exec=short`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is H60=H60c (42/69 of losers there)
- **Sharp: n=51  W=9/L=42  WR=17.6%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade  •  ONLY when HTF60 neutral

### L12.  `H60=H60e AND T1=T1c AND BBP=BBP5`
- Raw: n=112  W=41/L=71  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (43/71 of losers there)
- **Sharp: n=46  W=3/L=43  WR=6.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L13.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=112  W=41/L=71  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (43/71 of losers there)
- **Sharp: n=46  W=3/L=43  WR=6.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L14.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=110  W=40/L=70  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (20/70 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L15.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (43/69 of losers there)
- **Sharp: n=46  W=3/L=43  WR=6.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=asia

### L16.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is ZS=ZS4 (26/67 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L17.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_open (20/66 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_open

### L18.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=106  W=32/L=74  WR=30.2%
- Sharpen: sharpest is T1=T1c (68/74 of losers there)
- **Sharp: n=89  W=21/L=68  WR=23.6%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L19.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (20/64 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=asia

### L20.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is H20=H20a (53/65 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L21.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is T1=T1c (52/64 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L22.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H20=H20a (55/64 of losers there)
- **Sharp: n=75  W=20/L=55  WR=26.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L23.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is session_bucket=asia (31/62 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L24.  `H20=H20e AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI4 (50/62 of losers there)
- **Sharp: n=66  W=16/L=50  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=101  W=29/L=72  WR=28.7%
- Sharpen: sharpest is T4=T4c (36/72 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(45/35) | H60e(34/43) |
| T1 | T1a(54/45) | T1c(46/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/44) | short(42/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
