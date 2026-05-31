# EUR_CHF — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,767**  (W=1,173 / L=594)  -  WR: **66.4%**

## Session distribution

- ny_mid: n=751  W=502/L=249  WR=66.8%
- london_open: n=408  W=255/L=153  WR=62.5%
- ny_open: n=334  W=234/L=100  WR=70.1%
- london: n=112  W=72/L=40  WR=64.3%
- asia: n=74  W=47/L=27  WR=63.5%
- ny_close: n=70  W=52/L=18  WR=74.3%
- off_hours: n=18  W=11/L=7  WR=61.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=136  W=116/L=20  WR=85.3%
- Refine: exclude ZS=ZS4 drops 12/20 losers (60%)
- **Final: n=81  W=73/L=8  WR=90.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W02.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude T1=T1a drops 17/18 losers (94%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when 1h trend WITH trade

### W03.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude T4=T4c drops 10/14 losers (71%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W04.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude ZS=ZS3 drops 6/14 losers (43%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T4=T4c drops 12/13 losers (92%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20b AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude RSI=RSI4 drops 6/7 losers (86%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W07.  `H60=H60b AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H20=H20d drops 7/10 losers (70%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 mildly against

### W08.  `H20=H20b AND H60=H60c AND direction_exec=long`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 neutral  •  AVOID when upper third

### W09.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W10.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20b drops 4/8 losers (50%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W11.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H20=H20d drops 5/10 losers (50%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 mildly against

### W12.  `H60=H60b AND T4=T4a AND direction_exec=short`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when 1h trend WITH trade

### W13.  `H60=H60b AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  HTF60 slightly aligned; session=ny_mid  •  AVOID when HTF20 mildly against

### W14.  `H60=H60b AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 mildly against

### W15.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude BBP=BBP4 drops 7/9 losers (78%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when upper third

### W16.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude BBP=BBP1 drops 8/10 losers (80%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched lower band

### W17.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=66  W=61/L=5  WR=92.4%
- Refine: exclude ZS=ZS5 drops 5/5 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

### W18.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude direction_exec=long drops 3/7 losers (43%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when long

### W19.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude T1=T1c drops 5/9 losers (56%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W20.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude ZS=ZS5 drops 7/8 losers (88%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

### W21.  `H20=H20a AND H60=H60e AND RSI=RSI4`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=50  W=46/L=4  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=50  W=46/L=4  WR=92.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude BBP=BBP4 drops 3/7 losers (43%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF60 neutral; RSI 40-50 lower neutral  •  AVOID when upper third

### W24.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when upper third

### W25.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=62  W=57/L=5  WR=91.9%
- Refine: exclude ZS=ZS5 drops 5/5 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is T4=T4c (34/53 of losers there)
- **Sharp: n=47  W=13/L=34  WR=27.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L02.  `H20=H20b AND T1=T1c AND T4=T4a`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H60=H60d (27/51 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 mildly against

### L03.  `H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is H20=H20e (36/40 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when HTF20 strongly against

### L04.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is H20=H20e (35/39 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when HTF20 strongly against

### L05.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=59  W=17/L=42  WR=28.8%
- Sharpen: sharpest is T4=T4a (21/42 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=55  W=17/L=38  WR=30.9%
- Sharpen: sharpest is T4=T4a (18/38 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when 4h trend WITH trade

### L07.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is T4=T4c (13/33 of losers there)
- **Sharp: n=17  W=4/L=13  WR=23.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L08.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is T4=T4a (23/33 of losers there)
- **Sharp: n=33  W=10/L=23  WR=30.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L09.  `H20=H20d AND H60=H60c AND direction_exec=short`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is T1=T1c (19/36 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 neutral  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H20=H20a (27/32 of losers there)
- **Sharp: n=40  W=13/L=27  WR=32.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: sharpest is BBP=BBP5 (11/35 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when just touched upper band

### L12.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is T4=T4c (13/32 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is ZS=ZS2 (13/32 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L14.  `H20=H20b AND H60=H60e AND T4=T4a`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (15/30 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_mid

### L15.  `H20=H20b AND H60=H60e AND direction_exec=long`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (15/30 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against  •  ONLY when session=ny_mid

### L16.  `H20=H20b AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (15/30 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_mid

### L17.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=48  W=12/L=36  WR=25.0%
- Sharpen: sharpest is T4=T4a (18/36 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when 4h trend WITH trade

### L18.  `H60=H60a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is T4=T4a (20/30 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is T4=T4a (20/30 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20e AND H60=H60a AND RSI=RSI4`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is BBP=BBP5 (11/29 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when just touched upper band

### L21.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is BBP=BBP5 (11/29 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when just touched upper band

### L22.  `H60=H60a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is T4=T4a (19/29 of losers there)
- **Sharp: n=26  W=7/L=19  WR=26.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L23.  `H60=H60c AND T4=T4c AND direction_exec=short`
- Raw: n=45  W=16/L=29  WR=35.6%
- Sharpen: sharpest is T1=T1c (21/29 of losers there)
- **Sharp: n=28  W=7/L=21  WR=25.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L24.  `ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is T4=T4a (17/27 of losers there)
- **Sharp: n=25  W=8/L=17  WR=32.0%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L25.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is T4=T4a (17/27 of losers there)
- **Sharp: n=25  W=8/L=17  WR=32.0%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60b(12/6), H60e(37/31) | H60a(31/39) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/48) | short(47/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
