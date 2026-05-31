# USD_CHF — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,837**  (W=1,175 / L=662)  -  WR: **64.0%**

## Session distribution

- ny_mid: n=709  W=453/L=256  WR=63.9%
- london_open: n=407  W=262/L=145  WR=64.4%
- ny_open: n=192  W=130/L=62  WR=67.7%
- asia: n=176  W=112/L=64  WR=63.6%
- ny_close: n=169  W=103/L=66  WR=60.9%
- london: n=117  W=72/L=45  WR=61.5%
- off_hours: n=55  W=35/L=20  WR=63.6%
- asia_late: n=12  W=8/L=4  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND T4=T4c`
- Raw: n=146  W=132/L=14  WR=90.4%
- Refine: exclude direction_exec=long drops 13/14 losers (93%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when long

### W02.  `H20=H20e AND T4=T4c AND ZS=ZS2`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude H60=H60b drops 9/15 losers (60%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W03.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude H60=H60b drops 9/15 losers (60%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W04.  `T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 12/14 losers (86%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W05.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude BBP=BBP3 drops 9/9 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when middle of band

### W06.  `H60=H60e AND T4=T4c AND RSI=RSI4`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude H20=H20c drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W07.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude RSI=RSI3 drops 12/12 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W08.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W09.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude RSI=RSI3 drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W10.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude RSI=RSI3 drops 9/9 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W11.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude RSI=RSI4 drops 6/9 losers (67%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 50-60 upper neutral

### W12.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T4=T4a drops 8/10 losers (80%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W13.  `T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=78  W=72/L=6  WR=92.3%
- Refine: exclude ZS=ZS0 drops 4/6 losers (67%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore <-3 extreme

### W14.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude RSI=RSI4 drops 6/8 losers (75%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W15.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude H60=H60d drops 6/9 losers (67%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W16.  `T4=T4c AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude T1=T1c drops 6/7 losers (86%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  4h trend AGAINST trade; middle of band; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

### W17.  `T4=T4c AND BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude T1=T1c drops 6/7 losers (86%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  4h trend AGAINST trade; middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 1h trend AGAINST trade

### W18.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H60=H60d drops 6/9 losers (67%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W19.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W20.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H20=H20a drops 6/10 losers (60%)
- **Final: n=50  W=46/L=4  WR=92.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W21.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H60=H60a drops 7/11 losers (64%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when HTF60 aligned WITH trade

### W22.  `T1=T1a AND T4=T4c AND BBP=BBP3`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band  •  AVOID when session=ny_mid

### W23.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W24.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS0 drops 4/9 losers (44%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  AVOID when zscore <-3 extreme

### W25.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=70  W=69/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is direction_exec=long (40/70 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when long

### L02.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is ZS=ZS2 (37/56 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L03.  `T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is T4=T4a (24/50 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L04.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is T1=T1a (37/46 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L05.  `T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=75  W=27/L=48  WR=36.0%
- Sharpen: sharpest is session_bucket=asia (18/48 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when session=asia

### L06.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is ZS=ZS1 (23/45 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=69  W=22/L=47  WR=31.9%
- Sharpen: sharpest is BBP=BBP2 (29/47 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when lower third

### L08.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is T4=T4a (37/47 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L09.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is T4=T4a (24/45 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is H20=H20a (14/44 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (20/39 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=63  W=18/L=45  WR=28.6%
- Sharpen: sharpest is T4=T4a (37/45 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=62  W=17/L=45  WR=27.4%
- Sharpen: sharpest is RSI=RSI3 (37/45 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L14.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=60  W=15/L=45  WR=25.0%
- Sharpen: sharpest is RSI=RSI3 (37/45 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L15.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is RSI=RSI4 (26/37 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L16.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is H20=H20a (21/37 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L17.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is H20=H20a (21/37 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L18.  `H60=H60a AND T1=T1a AND ZS=ZS1`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is T4=T4a (20/37 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is T4=T4a (20/37 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L20.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is T4=T4a (20/37 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L21.  `T4=T4a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=55  W=15/L=40  WR=27.3%
- Sharpen: sharpest is T1=T1c (19/40 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L22.  `T4=T4a AND BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=55  W=15/L=40  WR=27.3%
- Sharpen: sharpest is T1=T1c (19/40 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 1h trend AGAINST trade

### L23.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is T1=T1c (17/33 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L24.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is H20=H20a (18/33 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L25.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is H60=H60a (10/38 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(38/31) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(55/43) | T4a(45/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
