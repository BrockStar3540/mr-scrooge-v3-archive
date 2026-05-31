# EUR_GBP — R31 Manual

## Regime centroid (locked factors)

- **BB = BB0**  (very narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **954**  (W=612 / L=342)  -  WR: **64.2%**

## Session distribution

- asia: n=373  W=241/L=132  WR=64.6%
- ny_close: n=217  W=137/L=80  WR=63.1%
- off_hours: n=78  W=46/L=32  WR=59.0%
- london_open: n=66  W=42/L=24  WR=63.6%
- london: n=63  W=44/L=19  WR=69.8%
- ny_mid: n=55  W=34/L=21  WR=61.8%
- ny_open: n=52  W=36/L=16  WR=69.2%
- asia_late: n=50  W=32/L=18  WR=64.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60d drops 8/13 losers (62%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF60 mildly against

### W02.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude BBP=BBP5 drops 9/12 losers (75%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W03.  `ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude BBP=BBP5 drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W04.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=62/L=5  WR=92.5%
- Refine: exclude BBP=BBP2 drops 3/5 losers (60%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W06.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude T1=T1c drops 3/3 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W07.  `BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; session=asia  •  AVOID when 4h trend AGAINST trade

### W08.  `T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude H60=H60a drops 5/7 losers (71%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 aligned WITH trade

### W09.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W10.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude BBP=BBP5 drops 5/5 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W13.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=53  W=51/L=2  WR=96.2%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W14.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude ZS=ZS1 drops 5/6 losers (83%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W15.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 5/7 losers (71%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W16.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude H60=H60d drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 mildly against

### W17.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=48  W=45/L=3  WR=93.8%
- Refine: exclude T1=T1c drops 3/3 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W18.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude ZS=ZS5 drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W19.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W20.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W22.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W23.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude H60=H60a drops 5/7 losers (71%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 aligned WITH trade

### W24.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=47  W=43/L=4  WR=91.5%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=46  W=43/L=3  WR=93.5%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is H60=H60a (31/50 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L02.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is direction_exec=short (31/41 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when short

### L03.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60e (25/38 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L04.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is BBP=BBP6 (23/33 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L05.  `T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is T1=T1c (21/31 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=49  W=17/L=32  WR=34.7%
- Sharpen: sharpest is H60=H60e (25/32 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L07.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=49  W=17/L=32  WR=34.7%
- Sharpen: sharpest is H60=H60e (25/32 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L08.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=49  W=17/L=32  WR=34.7%
- Sharpen: sharpest is H60=H60e (25/32 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L09.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=46  W=13/L=33  WR=28.3%
- Sharpen: sharpest is H20=H20c (11/33 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 neutral

### L10.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=44  W=15/L=29  WR=34.1%
- Sharpen: sharpest is RSI=RSI4 (23/29 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is BBP=BBP6 (20/27 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L12.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is BBP=BBP6 (10/27 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L13.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=41  W=10/L=31  WR=24.4%
- Sharpen: sharpest is H20=H20a (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 aligned WITH trade

### L14.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is T1=T1c (18/24 of losers there)
- **Sharp: n=24  W=6/L=18  WR=25.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L15.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is H60=H60a (11/28 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is session_bucket=off_hours (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=off_hours

### L17.  `H60=H60d AND T1=T1a AND RSI=RSI3`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is direction_exec=long (13/24 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when long

### L18.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is H60=H60a (20/23 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L19.  `H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=37  W=14/L=23  WR=37.8%
- Sharpen: sharpest is RSI=RSI3 (9/23 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L20.  `H20=H20d AND T4=T4c AND session_bucket=ny_close`
- Raw: n=36  W=12/L=24  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (17/24 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L21.  `T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is H20=H20d (17/23 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF20 mildly against

### L22.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is H60=H60c (5/23 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 neutral

### L23.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=35  W=11/L=24  WR=31.4%
- Sharpen: sharpest is session_bucket=asia (10/24 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L24.  `T1=T1c AND T4=T4c AND ZS=ZS3`
- Raw: n=35  W=12/L=23  WR=34.3%
- Sharpen: sharpest is RSI=RSI3 (15/23 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L25.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=35  W=13/L=22  WR=37.1%
- Sharpen: sharpest is H60=H60c (5/22 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(52/45) | T1a(47/54) |
| T4 | T4a(57/43) | T4c(43/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
