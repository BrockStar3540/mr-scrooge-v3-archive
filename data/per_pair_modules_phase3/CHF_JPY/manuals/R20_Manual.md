# CHF_JPY — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,148**  (W=3,729 / L=2,419)  -  WR: **60.7%**

## Session distribution

- asia: n=1883  W=1140/L=743  WR=60.5%
- london_open: n=1317  W=774/L=543  WR=58.8%
- ny_open: n=1038  W=660/L=378  WR=63.6%
- ny_mid: n=850  W=529/L=321  WR=62.2%
- london: n=403  W=246/L=157  WR=61.0%
- ny_close: n=250  W=154/L=96  WR=61.6%
- off_hours: n=204  W=100/L=104  WR=49.0%
- asia_late: n=203  W=126/L=77  WR=62.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude T1=T1c drops 12/18 losers (67%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20e AND H60=H60e AND RSI=RSI2`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  AVOID when session=asia

### W03.  `H20=H20e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak  •  AVOID when session=asia

### W04.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  AVOID when session=asia

### W05.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude ZS=ZS1 drops 11/14 losers (79%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W06.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude ZS=ZS1 drops 11/14 losers (79%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude T1=T1c drops 7/13 losers (54%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W08.  `T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude T1=T1c drops 7/13 losers (54%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W09.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude T1=T1c drops 7/13 losers (54%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W10.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude BBP=BBP1 drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W11.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude BBP=BBP1 drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W12.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude BBP=BBP1 drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W13.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude BBP=BBP1 drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W14.  `H20=H20e AND H60=H60e AND BBP=BBP6`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T4=T4c drops 13/13 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T4=T4c drops 13/13 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T4=T4c drops 13/13 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude BBP=BBP1 drops 5/9 losers (56%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W18.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=88  W=82/L=6  WR=93.2%
- Refine: exclude BBP=BBP1 drops 5/6 losers (83%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W19.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=88  W=82/L=6  WR=93.2%
- Refine: exclude BBP=BBP1 drops 5/6 losers (83%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W20.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=88  W=82/L=6  WR=93.2%
- Refine: exclude BBP=BBP1 drops 5/6 losers (83%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W21.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W22.  `T1=T1a AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W23.  `H20=H20e AND T1=T1a AND RSI=RSI2`
- Raw: n=81  W=77/L=4  WR=95.1%
- Refine: exclude ZS=ZS1 drops 4/4 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W24.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI2`
- Raw: n=81  W=77/L=4  WR=95.1%
- Refine: exclude ZS=ZS1 drops 4/4 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W25.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=81  W=77/L=4  WR=95.1%
- Refine: exclude ZS=ZS1 drops 4/4 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=163  W=65/L=98  WR=39.9%
- Sharpen: sharpest is ZS=ZS1 (18/98 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=64/L=96  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open

### L03.  `H20=H20a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is T4=T4a (79/88 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND H60=H60e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is T1=T1c (26/88 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is T1=T1c (26/88 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: SHORT**  •  HTF20 strongly against; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L06.  `T4=T4c AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=143  W=55/L=88  WR=38.5%
- Sharpen: sharpest is RSI=RSI2 (20/88 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=london_open  •  ONLY when RSI 30-40 weak

### L07.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=143  W=55/L=88  WR=38.5%
- Sharpen: sharpest is RSI=RSI2 (20/88 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=london_open  •  ONLY when RSI 30-40 weak

### L08.  `H20=H20a AND T4=T4a AND session_bucket=london`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is RSI=RSI3 (79/88 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L09.  `T4=T4a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=139  W=43/L=96  WR=30.9%
- Sharpen: sharpest is H60=H60a (60/96 of losers there)
- **Sharp: n=79  W=19/L=60  WR=24.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is T4=T4a (60/78 of losers there)
- **Sharp: n=79  W=19/L=60  WR=24.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when 4h trend WITH trade

### L11.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is T4=T4a (60/78 of losers there)
- **Sharp: n=79  W=19/L=60  WR=24.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  ONLY when 4h trend WITH trade

### L12.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is T4=T4a (60/78 of losers there)
- **Sharp: n=79  W=19/L=60  WR=24.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND T1=T1a AND T4=T4c AND BBP=BBP1`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (20/73 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=london_open

### L14.  `T1=T1a AND T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (20/73 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=london_open

### L15.  `H20=H20e AND BBP=BBP4 AND ZS=ZS3`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (22/71 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L16.  `H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is H20=H20a (29/67 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L17.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is H20=H20a (29/67 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L18.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is T4=T4c (33/67 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is H20=H20a (29/67 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L20.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=108  W=29/L=79  WR=26.9%
- Sharpen: sharpest is ZS=ZS2 (29/79 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when zscore -2 to -1 oversold

### L21.  `H20=H20e AND T1=T1a AND RSI=RSI4`
- Raw: n=104  W=32/L=72  WR=30.8%
- Sharpen: sharpest is BBP=BBP5 (19/72 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when just touched upper band

### L22.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=100  W=28/L=72  WR=28.0%
- Sharpen: sharpest is session_bucket=ny_close (17/72 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L23.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=100  W=28/L=72  WR=28.0%
- Sharpen: sharpest is session_bucket=ny_close (17/72 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L24.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=97  W=28/L=69  WR=28.9%
- Sharpen: sharpest is BBP=BBP5 (19/69 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when just touched upper band

### L25.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=97  W=28/L=69  WR=28.9%
- Sharpen: sharpest is BBP=BBP5 (19/69 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when just touched upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
