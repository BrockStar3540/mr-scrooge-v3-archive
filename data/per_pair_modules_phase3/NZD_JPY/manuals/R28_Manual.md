# NZD_JPY — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,315**  (W=2,010 / L=1,305)  -  WR: **60.6%**

## Session distribution

- asia: n=950  W=570/L=380  WR=60.0%
- ny_mid: n=915  W=559/L=356  WR=61.1%
- london_open: n=530  W=321/L=209  WR=60.6%
- ny_open: n=328  W=195/L=133  WR=59.5%
- ny_close: n=310  W=192/L=118  WR=61.9%
- asia_late: n=167  W=104/L=63  WR=62.3%
- london: n=69  W=42/L=27  WR=60.9%
- off_hours: n=46  W=27/L=19  WR=58.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=129  W=114/L=15  WR=88.4%
- Refine: exclude H20=H20c drops 6/15 losers (40%)
- **Final: n=110  W=101/L=9  WR=91.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 neutral

### W02.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude H20=H20c drops 6/15 losers (40%)
- **Final: n=108  W=99/L=9  WR=91.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 neutral

### W03.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=116  W=103/L=13  WR=88.8%
- Refine: exclude ZS=ZS4 drops 8/13 losers (62%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W04.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=114  W=101/L=13  WR=88.6%
- Refine: exclude ZS=ZS4 drops 8/13 losers (62%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W05.  `T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude BBP=BBP3 drops 6/10 losers (60%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia  •  AVOID when middle of band

### W06.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude BBP=BBP3 drops 6/10 losers (60%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when middle of band

### W07.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude session_bucket=ny_mid drops 9/14 losers (64%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W08.  `H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W09.  `H60=H60e AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W10.  `H60=H60a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude H20=H20e drops 4/11 losers (36%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W11.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude RSI=RSI4 drops 4/8 losers (50%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W12.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=92  W=84/L=8  WR=91.3%
- Refine: exclude RSI=RSI4 drops 4/8 losers (50%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W13.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W14.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20e drops 4/9 losers (44%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W15.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=75  W=73/L=2  WR=97.3%
- Refine: exclude BBP=BBP1 drops 2/2 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W16.  `H20=H20c AND H60=H60a AND session_bucket=asia`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude BBP=BBP4 drops 4/7 losers (57%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  AVOID when upper third

### W17.  `H20=H20c AND direction_exec=long AND session_bucket=asia`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude BBP=BBP4 drops 4/7 losers (57%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 neutral; session=asia  •  AVOID when upper third

### W18.  `H20=H20c AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude BBP=BBP4 drops 4/7 losers (57%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  AVOID when upper third

### W19.  `T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 40-50 lower neutral

### W20.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 40-50 lower neutral

### W21.  `T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=ny_mid drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W22.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=ny_mid drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W23.  `T4=T4a AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/9 losers (89%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W24.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 8/8 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W25.  `H60=H60a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude RSI=RSI2 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; session=asia  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=199  W=71/L=128  WR=35.7%
- Sharpen: sharpest is BBP=BBP0 (51/128 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L02.  `H20=H20e AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=136  W=44/L=92  WR=32.4%
- Sharpen: sharpest is T4=T4c (19/92 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L03.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=134  W=45/L=89  WR=33.6%
- Sharpen: sharpest is T4=T4c (22/89 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is T1=T1a (76/78 of losers there)
- **Sharp: n=111  W=35/L=76  WR=31.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L05.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is T1=T1a (76/78 of losers there)
- **Sharp: n=111  W=35/L=76  WR=31.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L06.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (26/81 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L07.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (26/81 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L08.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=49/L=77  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral

### L09.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is H60=H60e (76/76 of losers there)
- **Sharp: n=111  W=35/L=76  WR=31.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when HTF60 strongly against

### L10.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is H60=H60e (76/76 of losers there)
- **Sharp: n=111  W=35/L=76  WR=31.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when HTF60 strongly against

### L11.  `H60=H60e AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP3 (26/74 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  ONLY when middle of band

### L12.  `T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP3 (26/74 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when middle of band

### L13.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP3 (26/74 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london_open  •  ONLY when middle of band

### L14.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP3 (26/74 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when middle of band

### L15.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP3 (26/74 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  ONLY when middle of band

### L16.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP3 (26/74 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when middle of band

### L17.  `H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=119  W=40/L=79  WR=33.6%
- Sharpen: sharpest is session_bucket=london_open (28/79 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L18.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is H20=H20e (25/70 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L19.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is H20=H20e (25/70 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L20.  `H20=H20e AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=113  W=37/L=76  WR=32.7%
- Sharpen: sharpest is T4=T4c (14/76 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=112  W=37/L=75  WR=33.0%
- Sharpen: sharpest is T4=T4c (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20e AND T1=T1a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=112  W=39/L=73  WR=34.8%
- Sharpen: sharpest is session_bucket=london_open (13/73 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L23.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=111  W=35/L=76  WR=31.5%
- Sharpen: sharpest is ZS=ZS1 (19/76 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=109  W=36/L=73  WR=33.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=109  W=36/L=73  WR=33.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L25.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=109  W=36/L=73  WR=33.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=109  W=36/L=73  WR=33.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(52/45) | T4c(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
