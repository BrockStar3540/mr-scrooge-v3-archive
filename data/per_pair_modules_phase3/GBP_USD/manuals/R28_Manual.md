# GBP_USD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,037**  (W=1,953 / L=1,084)  -  WR: **64.3%**

## Session distribution

- london_open: n=946  W=596/L=350  WR=63.0%
- asia: n=623  W=385/L=238  WR=61.8%
- london: n=557  W=386/L=171  WR=69.3%
- ny_open: n=449  W=283/L=166  WR=63.0%
- asia_late: n=236  W=152/L=84  WR=64.4%
- ny_mid: n=207  W=140/L=67  WR=67.6%
- ny_close: n=19  W=11/L=8  WR=57.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=128  W=112/L=16  WR=87.5%
- Refine: exclude RSI=RSI2 drops 8/16 losers (50%)
- **Final: n=120  W=112/L=8  WR=93.3%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W02.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude RSI=RSI2 drops 8/17 losers (47%)
- **Final: n=116  W=107/L=9  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W03.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude ZS=ZS1 drops 8/16 losers (50%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W04.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude RSI=RSI2 drops 8/16 losers (50%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W05.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude H60=H60e drops 13/14 losers (93%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=london_open  •  AVOID when HTF60 strongly against

### W06.  `T1=T1c AND ZS=ZS2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude H60=H60e drops 13/14 losers (93%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W07.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=london`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude BBP=BBP3 drops 4/11 losers (36%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=london  •  AVOID when middle of band

### W08.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude H60=H60b drops 5/7 losers (71%)
- **Final: n=86  W=84/L=2  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 slightly aligned

### W10.  `H60=H60e AND T4=T4a AND BBP=BBP0`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude session_bucket=london_open drops 9/11 losers (82%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when session=london_open

### W11.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=86  W=77/L=9  WR=89.5%
- Refine: exclude H60=H60b drops 7/9 losers (78%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 slightly aligned

### W12.  `T4=T4a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude H60=H60e drops 6/12 losers (50%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  AVOID when HTF60 strongly against

### W13.  `T4=T4a AND BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude H60=H60e drops 6/12 losers (50%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W14.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude H60=H60e drops 6/7 losers (86%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 strongly against

### W15.  `H60=H60e AND ZS=ZS5 AND session_bucket=london`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude RSI=RSI4 drops 7/12 losers (58%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=london  •  AVOID when RSI 50-60 upper neutral

### W16.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude BBP=BBP2 drops 9/10 losers (90%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when lower third

### W17.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude H20=H20b drops 3/6 losers (50%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 slightly aligned

### W18.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude H60=H60e drops 6/7 losers (86%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W19.  `T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia_late  •  AVOID when 1h trend WITH trade

### W20.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W21.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=73  W=72/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold

### W22.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude RSI=RSI2 drops 8/10 losers (80%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_open drops 5/10 losers (50%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W24.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude RSI=RSI6 drops 3/7 losers (43%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when RSI 70-80 overbought

### W25.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude session_bucket=asia drops 4/7 losers (57%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is T4=T4c (45/83 of losers there)
- **Sharp: n=56  W=11/L=45  WR=19.6%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is BBP=BBP2 (33/78 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when lower third

### L03.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is H60=H60e (34/73 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L04.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is H60=H60e (34/73 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L05.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (25/69 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L06.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (33/68 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L07.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=104  W=35/L=69  WR=33.7%
- Sharpen: sharpest is session_bucket=asia (20/69 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L08.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is T1=T1c (56/64 of losers there)
- **Sharp: n=76  W=20/L=56  WR=26.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L09.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=100  W=36/L=64  WR=36.0%
- Sharpen: sharpest is H60=H60e (36/64 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: LONG**  •  deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L10.  `T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is ZS=ZS5 (19/65 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is H60=H60e (29/64 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L12.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is H20=H20e (26/62 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L13.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=33/L=62  WR=34.7%
- Sharpen: sharpest is ZS=ZS2 (24/62 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L14.  `H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is T1=T1a (40/60 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third  •  ONLY when 1h trend WITH trade

### L15.  `H60=H60e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=92  W=33/L=59  WR=35.9%
- Sharpen: sharpest is T1=T1a (39/59 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L16.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=92  W=33/L=59  WR=35.9%
- Sharpen: sharpest is T1=T1a (39/59 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L17.  `T1=T1a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=88  W=29/L=59  WR=33.0%
- Sharpen: sharpest is RSI=RSI3 (33/59 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L18.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=88  W=31/L=57  WR=35.2%
- Sharpen: sharpest is H60=H60e (28/57 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=87  W=29/L=58  WR=33.3%
- Sharpen: sharpest is T1=T1a (38/58 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when 1h trend WITH trade

### L20.  `H20=H20e AND H60=H60e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is T1=T1a (38/58 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=81  W=27/L=54  WR=33.3%
- Sharpen: sharpest is H60=H60e (27/54 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L22.  `H60=H60e AND T1=T1a AND ZS=ZS2`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (34/48 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L23.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (34/48 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L24.  `T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=79  W=28/L=51  WR=35.4%
- Sharpen: sharpest is H60=H60b (14/51 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when HTF60 slightly aligned

### L25.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is direction_exec=short (48/50 of losers there)
- **Sharp: n=67  W=19/L=48  WR=28.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when short

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(49/42) | H20e(42/51) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(54/48) | T4c(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
