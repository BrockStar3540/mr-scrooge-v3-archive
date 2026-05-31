# EUR_JPY — R23 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,142**  (W=1,928 / L=1,214)  -  WR: **61.4%**

## Session distribution

- asia: n=1228  W=768/L=460  WR=62.5%
- ny_close: n=537  W=335/L=202  WR=62.4%
- ny_mid: n=348  W=209/L=139  WR=60.1%
- ny_open: n=219  W=122/L=97  WR=55.7%
- asia_late: n=218  W=128/L=90  WR=58.7%
- london_open: n=212  W=123/L=89  WR=58.0%
- london: n=209  W=135/L=74  WR=64.6%
- off_hours: n=171  W=108/L=63  WR=63.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=189  W=161/L=28  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 10/28 losers (36%)
- **Final: n=179  W=161/L=18  WR=89.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W02.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: exclude session_bucket=asia_late drops 9/25 losers (36%)
- **Final: n=171  W=155/L=16  WR=90.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia_late

### W03.  `T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=168  W=144/L=24  WR=85.7%
- Refine: exclude session_bucket=asia_late drops 7/24 losers (29%)
- **Final: n=159  W=142/L=17  WR=89.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W04.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude ZS=ZS3 drops 5/12 losers (42%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  AVOID when zscore -1 to +1 neutral

### W06.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude H60=H60b drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when HTF60 slightly aligned

### W07.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W08.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W09.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W10.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude session_bucket=ny_close drops 5/12 losers (42%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W11.  `H60=H60b AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude BBP=BBP3 drops 6/13 losers (46%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 50-60 upper neutral; session=asia  •  AVOID when middle of band

### W12.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude session_bucket=asia drops 4/8 losers (50%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

### W13.  `H20=H20e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude strategy_id=BR2_vcb_long drops 3/7 losers (43%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=BR2_vcb_long

### W14.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude strategy_id=BR2_vcb_long drops 3/7 losers (43%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=BR2_vcb_long

### W15.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=asia drops 4/7 losers (57%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W16.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H20=H20b drops 11/11 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 slightly aligned

### W17.  `H60=H60b AND T1=T1c AND session_bucket=asia`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude RSI=RSI2 drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T1=T1a drops 7/9 losers (78%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W19.  `T4=T4c AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H60=H60b drops 7/11 losers (64%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -1 to +1 neutral; session=asia  •  AVOID when HTF60 slightly aligned

### W20.  `H20=H20e AND H60=H60b AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude T1=T1a drops 8/11 losers (73%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W21.  `H20=H20c AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude T4=T4c drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20c AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude T4=T4c drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W23.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20c drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 neutral

### W24.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude T1=T1a drops 4/6 losers (67%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude RSI=RSI2 drops 8/10 losers (80%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=143  W=54/L=89  WR=37.8%
- Sharpen: sharpest is ZS=ZS3 (28/89 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L02.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=143  W=54/L=89  WR=37.8%
- Sharpen: sharpest is ZS=ZS3 (28/89 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L03.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=114  W=38/L=76  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (39/76 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L04.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=108  W=43/L=65  WR=39.8%
- Sharpen: sharpest is H20=H20e (49/65 of losers there)
- **Sharp: n=66  W=17/L=49  WR=25.8%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is ZS=ZS3 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L06.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=95  W=33/L=62  WR=34.7%
- Sharpen: sharpest is T4=T4a (46/62 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (15/57 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore >+3 extreme

### L08.  `H20=H20e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=92  W=30/L=62  WR=32.6%
- Sharpen: sharpest is RSI=RSI3 (35/62 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (34/57 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L10.  `H20=H20e AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is RSI=RSI3 (35/59 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L11.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is RSI=RSI3 (35/59 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L12.  `T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=88  W=31/L=57  WR=35.2%
- Sharpen: sharpest is direction_exec=short (46/57 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  ONLY when short

### L13.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (28/56 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=asia

### L14.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (28/56 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=asia

### L15.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is ZS=ZS3 (22/53 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L16.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is H60=H60e (45/51 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 strongly against

### L17.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is H20=H20a (17/51 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L18.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is ZS=ZS3 (34/57 of losers there)
- **Sharp: n=41  W=7/L=34  WR=17.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L19.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is ZS=ZS3 (34/57 of losers there)
- **Sharp: n=41  W=7/L=34  WR=17.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L20.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (15/48 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L21.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is BBP=BBP2 (25/48 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when lower third

### L22.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is T4=T4a (37/52 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=77  W=26/L=51  WR=33.8%
- Sharpen: sharpest is T1=T1a (32/51 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=asia  •  ONLY when 1h trend WITH trade

### L24.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is H20=H20e (35/47 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 strongly against

### L25.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is BBP=BBP6 (14/46 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(36/42) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
