# NZD_CAD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,584**  (W=1,037 / L=547)  -  WR: **65.5%**

## Session distribution

- asia: n=528  W=353/L=175  WR=66.9%
- ny_open: n=315  W=206/L=109  WR=65.4%
- london_open: n=267  W=168/L=99  WR=62.9%
- ny_close: n=192  W=123/L=69  WR=64.1%
- ny_mid: n=136  W=87/L=49  WR=64.0%
- london: n=111  W=75/L=36  WR=67.6%
- off_hours: n=23  W=17/L=6  WR=73.9%
- asia_late: n=12  W=8/L=4  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=96  W=86/L=10  WR=89.6%
- Refine: exclude H20=H20e drops 6/10 losers (60%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 strongly against

### W02.  `T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20d drops 7/14 losers (50%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 mildly against

### W03.  `T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20e drops 9/13 losers (69%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 strongly against

### W04.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude H20=H20e drops 5/9 losers (56%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 strongly against

### W05.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_mid

### W06.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/10 losers (30%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W07.  `H20=H20b AND H60=H60e AND RSI=RSI3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP6 drops 3/8 losers (38%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when deep above upper band

### W08.  `H20=H20b AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP6 drops 3/8 losers (38%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep above upper band

### W09.  `H20=H20b AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP6 drops 3/8 losers (38%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when deep above upper band

### W10.  `H20=H20d AND T4=T4a AND RSI=RSI2`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_close

### W11.  `H20=H20d AND RSI=RSI2 AND direction_exec=short`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 30-40 weak  •  AVOID when session=ny_close

### W12.  `H20=H20d AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_close

### W13.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20a drops 4/10 losers (40%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  AVOID when session=london_open

### W15.  `H60=H60e AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 5/10 losers (50%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W16.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=65  W=60/L=5  WR=92.3%
- Refine: exclude H20=H20d drops 2/5 losers (40%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 mildly against

### W17.  `H20=H20b AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude BBP=BBP6 drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep above upper band

### W18.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude ZS=ZS1 drops 6/9 losers (67%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude ZS=ZS1 drops 6/9 losers (67%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude ZS=ZS1 drops 6/9 losers (67%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude BBP=BBP1 drops 6/6 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when just touched lower band

### W22.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude BBP=BBP1 drops 6/6 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when just touched lower band

### W23.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/7 losers (43%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when strategy=BR2_vcb_short

### W24.  `H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude BBP=BBP2 drops 5/8 losers (62%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when lower third

### W25.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude BBP=BBP2 drops 5/8 losers (62%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (15/32 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L02.  `H20=H20b AND T4=T4c AND RSI=RSI2`
- Raw: n=50  W=15/L=35  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (22/35 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L03.  `H20=H20b AND RSI=RSI2 AND direction_exec=long`
- Raw: n=50  W=15/L=35  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (22/35 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 30-40 weak  •  ONLY when session=asia

### L04.  `H20=H20b AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=50  W=15/L=35  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (22/35 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L05.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=47  W=12/L=35  WR=25.5%
- Sharpen: sharpest is session_bucket=ny_close (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L06.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=47  W=12/L=35  WR=25.5%
- Sharpen: sharpest is session_bucket=ny_close (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L07.  `T1=T1c AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (9/29 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L08.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (9/29 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L09.  `H20=H20e AND T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is BBP=BBP0 (14/28 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L10.  `H20=H20e AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is BBP=BBP0 (14/28 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L11.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is H60=H60e (9/27 of losers there)
- **Sharp: n=11  W=2/L=9  WR=18.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF60 strongly against

### L12.  `T1=T1c AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (9/27 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L13.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=44  W=10/L=34  WR=22.7%
- Sharpen: sharpest is ZS=ZS2 (21/34 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -2 to -1 oversold

### L14.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=44  W=11/L=33  WR=25.0%
- Sharpen: sharpest is session_bucket=ny_close (16/33 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L15.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is H20=H20e (15/27 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is H20=H20e (15/27 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF60 strongly against; session=london_open  •  ONLY when HTF20 strongly against

### L17.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is H20=H20e (15/27 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L18.  `H20=H20b AND T1=T1c AND RSI=RSI2`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (15/28 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L19.  `H20=H20b AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (15/28 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L20.  `H20=H20b AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (15/28 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L21.  `T4=T4c AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=london_open (9/25 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L22.  `H60=H60b AND T1=T1a AND direction_exec=short`
- Raw: n=40  W=11/L=29  WR=27.5%
- Sharpen: sharpest is session_bucket=ny_open (19/29 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade  •  ONLY when session=ny_open

### L23.  `H20=H20d AND H60=H60a AND RSI=RSI3`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (14/28 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L24.  `H20=H20d AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (14/28 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L25.  `H20=H20d AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=40  W=12/L=28  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (14/28 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(45/35), H60d(11/5) | H60a(37/45), H60b(6/11) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
