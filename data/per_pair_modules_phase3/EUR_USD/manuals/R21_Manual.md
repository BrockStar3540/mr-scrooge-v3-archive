# EUR_USD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,942**  (W=1,216 / L=726)  -  WR: **62.6%**

## Session distribution

- ny_close: n=639  W=394/L=245  WR=61.7%
- asia: n=568  W=366/L=202  WR=64.4%
- ny_mid: n=326  W=196/L=130  WR=60.1%
- ny_open: n=131  W=86/L=45  WR=65.6%
- london: n=112  W=73/L=39  WR=65.2%
- london_open: n=72  W=46/L=26  WR=63.9%
- asia_late: n=48  W=26/L=22  WR=54.2%
- off_hours: n=46  W=29/L=17  WR=63.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=207  W=177/L=30  WR=85.5%
- Refine: exclude RSI=RSI3 drops 17/30 losers (57%)
- **Final: n=160  W=147/L=13  WR=91.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W02.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude ZS=ZS2 drops 14/26 losers (54%)
- **Final: n=135  W=123/L=12  WR=91.1%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  AVOID when zscore -2 to -1 oversold

### W03.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=181  W=155/L=26  WR=85.6%
- Refine: exclude ZS=ZS4 drops 20/26 losers (77%)
- **Final: n=103  W=97/L=6  WR=94.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W04.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=170  W=150/L=20  WR=88.2%
- Refine: exclude RSI=RSI3 drops 20/20 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  AVOID when RSI 40-50 lower neutral

### W05.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=162  W=141/L=21  WR=87.0%
- Refine: exclude RSI=RSI3 drops 8/21 losers (38%)
- **Final: n=146  W=133/L=13  WR=91.1%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W06.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=162  W=139/L=23  WR=85.8%
- Refine: exclude ZS=ZS2 drops 15/23 losers (65%)
- **Final: n=102  W=94/L=8  WR=92.2%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -2 to -1 oversold

### W07.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=161  W=141/L=20  WR=87.6%
- Refine: exclude RSI=RSI3 drops 7/20 losers (35%)
- **Final: n=146  W=133/L=13  WR=91.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W08.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=154  W=138/L=16  WR=89.6%
- Refine: exclude RSI=RSI3 drops 16/16 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20e AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=144  W=128/L=16  WR=88.9%
- Refine: exclude BBP=BBP1 drops 5/16 losers (31%)
- **Final: n=133  W=122/L=11  WR=91.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=ny_close  •  AVOID when just touched lower band

### W10.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=141  W=125/L=16  WR=88.7%
- Refine: exclude RSI=RSI3 drops 16/16 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W11.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=135  W=121/L=14  WR=89.6%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W12.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=135  W=119/L=16  WR=88.1%
- Refine: exclude ZS=ZS4 drops 12/16 losers (75%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W13.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=131  W=112/L=19  WR=85.5%
- Refine: exclude ZS=ZS1 drops 9/19 losers (47%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `H20=H20e AND H60=H60a AND session_bucket=ny_close`
- Raw: n=128  W=112/L=16  WR=87.5%
- Refine: exclude T4=T4c drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=128  W=112/L=16  WR=87.5%
- Refine: exclude T4=T4c drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 9/18 losers (50%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W17.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude BBP=BBP1 drops 5/17 losers (29%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when just touched lower band

### W18.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude BBP=BBP1 drops 5/16 losers (31%)
- **Final: n=107  W=96/L=11  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when just touched lower band

### W19.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude BBP=BBP2 drops 11/16 losers (69%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when lower third

### W20.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/13 losers (62%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W21.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude H60=H60e drops 12/12 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W22.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T1=T1c drops 6/12 losers (50%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W23.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W24.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude H20=H20a drops 12/14 losers (86%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W25.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude RSI=RSI3 drops 13/13 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND direction_exec=long`
- Raw: n=175  W=67/L=108  WR=38.3%
- Sharpen: sharpest is ZS=ZS3 (31/108 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L02.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=157  W=59/L=98  WR=37.6%
- Sharpen: sharpest is BBP=BBP0 (27/98 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  ONLY when deep below lower band

### L03.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=156  W=51/L=105  WR=32.7%
- Sharpen: sharpest is RSI=RSI2 (16/105 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L04.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=146  W=55/L=91  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (36/91 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20a AND T1=T1a AND RSI=RSI4`
- Raw: n=143  W=53/L=90  WR=37.1%
- Sharpen: sharpest is ZS=ZS5 (29/90 of losers there)
- **Sharp: n=30  W=1/L=29  WR=3.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=139  W=55/L=84  WR=39.6%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close

### L07.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=131  W=51/L=80  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=131  W=51/L=80  WR=38.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close

### L08.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=130  W=43/L=87  WR=33.1%
- Sharpen: sharpest is BBP=BBP0 (18/87 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when deep below lower band

### L09.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=129  W=41/L=88  WR=31.8%
- Sharpen: sharpest is RSI=RSI4 (25/88 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when RSI 50-60 upper neutral

### L10.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=122  W=44/L=78  WR=36.1%
- Sharpen: sharpest is RSI=RSI4 (31/78 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=121  W=43/L=78  WR=35.5%
- Sharpen: sharpest is ZS=ZS5 (29/78 of losers there)
- **Sharp: n=30  W=1/L=29  WR=3.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20a AND T1=T1c AND ZS=ZS3`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is direction_exec=long (31/75 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when long

### L13.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=113  W=40/L=73  WR=35.4%
- Sharpen: sharpest is ZS=ZS3 (12/73 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L14.  `H60=H60e AND T1=T1c AND ZS=ZS3`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_close (25/68 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L15.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=110  W=39/L=71  WR=35.5%
- Sharpen: sharpest is ZS=ZS5 (20/71 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=110  W=39/L=71  WR=35.5%
- Sharpen: sharpest is ZS=ZS5 (20/71 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=107  W=39/L=68  WR=36.4%
- Sharpen: sharpest is H20=H20a (15/68 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L18.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is ZS=ZS4 (29/67 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L19.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=106  W=29/L=77  WR=27.4%
- Sharpen: sharpest is RSI=RSI4 (25/77 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L20.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=104  W=32/L=72  WR=30.8%
- Sharpen: sharpest is T1=T1a (36/72 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L21.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is ZS=ZS4 (29/64 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L22.  `H20=H20a AND H60=H60e AND RSI=RSI3`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=40/L=63  WR=38.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral

### L23.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=40/L=63  WR=38.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral

### L24.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is ZS=ZS4 (29/63 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L25.  `H20=H20a AND H60=H60e AND session_bucket=ny_close`
- Raw: n=102  W=37/L=65  WR=36.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=37/L=65  WR=36.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(60/36) | H20a(37/60) |
| H60 | — | H60e(37/44) |
| T1 | T1a(57/42) | T1c(41/57) |
| T4 | T4c(61/38) | T4a(39/62) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
