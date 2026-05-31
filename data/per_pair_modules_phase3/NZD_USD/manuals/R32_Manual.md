# NZD_USD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,048**  (W=1,328 / L=720)  -  WR: **64.8%**

## Session distribution

- asia: n=1018  W=669/L=349  WR=65.7%
- ny_close: n=299  W=189/L=110  WR=63.2%
- london: n=240  W=163/L=77  WR=67.9%
- london_open: n=180  W=118/L=62  WR=65.6%
- ny_open: n=135  W=89/L=46  WR=65.9%
- asia_late: n=70  W=42/L=28  WR=60.0%
- off_hours: n=55  W=37/L=18  WR=67.3%
- ny_mid: n=51  W=21/L=30  WR=41.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=143  W=123/L=20  WR=86.0%
- Refine: exclude H60=H60a drops 10/20 losers (50%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W02.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude H60=H60a drops 10/20 losers (50%)
- **Final: n=99  W=89/L=10  WR=89.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W03.  `H20=H20a AND H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude T4=T4c drops 14/18 losers (78%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20d AND H60=H60a AND T1=T1a`
- Raw: n=118  W=104/L=14  WR=88.1%
- Refine: exclude session_bucket=london drops 6/14 losers (43%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london

### W05.  `H20=H20d AND H60=H60a AND direction_exec=short`
- Raw: n=118  W=104/L=14  WR=88.1%
- Refine: exclude session_bucket=london drops 6/14 losers (43%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade  •  AVOID when session=london

### W06.  `H20=H20d AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=118  W=104/L=14  WR=88.1%
- Refine: exclude session_bucket=london drops 6/14 losers (43%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london

### W07.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude RSI=RSI3 drops 11/14 losers (79%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W08.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W09.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude RSI=RSI3 drops 14/15 losers (93%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W10.  `H20=H20d AND H60=H60a AND T4=T4a`
- Raw: n=102  W=94/L=8  WR=92.2%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=80  W=78/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W11.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude BBP=BBP4 drops 5/9 losers (56%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when upper third

### W12.  `H20=H20d AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W13.  `H20=H20d AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W14.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude RSI=RSI3 drops 9/10 losers (90%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W15.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude BBP=BBP4 drops 6/11 losers (55%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when upper third

### W16.  `H20=H20d AND T4=T4a AND RSI=RSI2`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H60=H60b drops 11/14 losers (79%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF60 slightly aligned

### W17.  `H20=H20d AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H60=H60b drops 11/14 losers (79%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF60 slightly aligned

### W18.  `H20=H20d AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H60=H60b drops 11/14 losers (79%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF60 slightly aligned

### W19.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude RSI=RSI3 drops 8/9 losers (89%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20d AND H60=H60a AND RSI=RSI2`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W21.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude H60=H60e drops 5/10 losers (50%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 strongly against

### W22.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude BBP=BBP4 drops 5/9 losers (56%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when upper third

### W23.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude BBP=BBP4 drops 5/9 losers (56%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when upper third

### W24.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 aligned WITH trade

### W25.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude T1=T1c drops 8/11 losers (73%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is T4=T4c (31/57 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_close (23/49 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L03.  `H20=H20b AND H60=H60e AND T1=T1c`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is T4=T4c (35/49 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20b AND H60=H60e AND direction_exec=long`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is T4=T4c (35/49 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20b AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is T4=T4c (35/49 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is H20=H20e (31/47 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF20 strongly against

### L07.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (21/43 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L08.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is RSI=RSI3 (22/43 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20b AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (22/40 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L10.  `H60=H60e AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L11.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L12.  `H20=H20b AND H60=H60e AND RSI=RSI2`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is T4=T4c (30/39 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20b AND H60=H60e AND BBP=BBP2`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_close (22/37 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; lower third  •  ONLY when session=ny_close

### L14.  `H20=H20b AND T4=T4c AND RSI=RSI2`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: sharpest is H60=H60e (30/37 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L15.  `H20=H20b AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: sharpest is H60=H60e (30/37 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L16.  `H20=H20b AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: sharpest is H60=H60e (30/37 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L17.  `H20=H20b AND H60=H60e AND ZS=ZS2`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_close (22/36 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L18.  `H20=H20b AND H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_close (22/36 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L19.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is H20=H20a (17/34 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L20.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is H20=H20e (17/32 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=51  W=15/L=36  WR=29.4%
- Sharpen: sharpest is RSI=RSI3 (22/36 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L22.  `H60=H60e AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=51  W=15/L=36  WR=29.4%
- Sharpen: sharpest is RSI=RSI3 (22/36 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L23.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is ZS=ZS1 (13/33 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H20=H20b AND H60=H60e AND T4=T4c`
- Raw: n=50  W=11/L=39  WR=22.0%
- Sharpen: sharpest is session_bucket=asia (17/39 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L25.  `H20=H20b AND H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is T4=T4c (30/31 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(12/4) | H20b(4/11) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(57/46) | T4c(43/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
