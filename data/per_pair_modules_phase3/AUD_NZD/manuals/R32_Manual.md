# AUD_NZD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,642**  (W=1,676 / L=966)  -  WR: **63.4%**

## Session distribution

- asia: n=1235  W=786/L=449  WR=63.6%
- ny_mid: n=570  W=357/L=213  WR=62.6%
- london_open: n=315  W=197/L=118  WR=62.5%
- off_hours: n=242  W=152/L=90  WR=62.8%
- london: n=149  W=95/L=54  WR=63.8%
- ny_open: n=74  W=48/L=26  WR=64.9%
- asia_late: n=39  W=27/L=12  WR=69.2%
- ny_close: n=18  W=14/L=4  WR=77.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=273  W=235/L=38  WR=86.1%
- Refine: exclude T1=T1c drops 19/38 losers (50%)
- **Final: n=194  W=175/L=19  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=235  W=201/L=34  WR=85.5%
- Refine: exclude T1=T1c drops 15/34 losers (44%)
- **Final: n=182  W=163/L=19  WR=89.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W03.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=235  W=201/L=34  WR=85.5%
- Refine: exclude T1=T1c drops 15/34 losers (44%)
- **Final: n=182  W=163/L=19  WR=89.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W04.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=206  W=177/L=29  WR=85.9%
- Refine: no further refinement
- **Final: n=206  W=177/L=29  WR=85.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia

### W05.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=206  W=177/L=29  WR=85.9%
- Refine: no further refinement
- **Final: n=206  W=177/L=29  WR=85.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia

### W06.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=170  W=151/L=19  WR=88.8%
- Refine: exclude session_bucket=london_open drops 7/19 losers (37%)
- **Final: n=157  W=145/L=12  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W07.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude T1=T1c drops 13/21 losers (62%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W08.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=139  W=120/L=19  WR=86.3%
- Refine: exclude T4=T4a drops 12/19 losers (63%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=129  W=112/L=17  WR=86.8%
- Refine: exclude T1=T1c drops 13/17 losers (76%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W10.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude RSI=RSI5 drops 11/15 losers (73%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 60-70 strong

### W11.  `H20=H20d AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=118  W=106/L=12  WR=89.8%
- Refine: exclude T1=T1a drops 9/12 losers (75%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 mildly against; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W12.  `H60=H60a AND T1=T1c AND ZS=ZS2`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude RSI=RSI3 drops 16/17 losers (94%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W13.  `T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude RSI=RSI3 drops 16/17 losers (94%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W14.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude RSI=RSI3 drops 16/17 losers (94%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W15.  `H60=H60a AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude RSI=RSI3 drops 16/17 losers (94%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W16.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude RSI=RSI3 drops 16/17 losers (94%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W17.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H60=H60a drops 6/15 losers (40%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W18.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H60=H60a drops 6/15 losers (40%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20a AND T1=T1c AND ZS=ZS2`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude RSI=RSI3 drops 15/16 losers (94%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W20.  `H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W21.  `T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude RSI=RSI3 drops 15/16 losers (94%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W24.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W25.  `H20=H20a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T4=T4a drops 10/15 losers (67%)
- **Final: n=51  W=46/L=5  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=198  W=74/L=124  WR=37.4%
- Sharpen: sharpest is T1=T1c (53/124 of losers there)
- **Sharp: n=71  W=18/L=53  WR=25.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L02.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=194  W=74/L=120  WR=38.1%
- Sharpen: sharpest is T1=T1c (77/120 of losers there)
- **Sharp: n=112  W=35/L=77  WR=31.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L03.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is T1=T1c (50/121 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is T1=T1c (50/121 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=191  W=75/L=116  WR=39.3%
- Sharpen: sharpest is T1=T1c (61/116 of losers there)
- **Sharp: n=81  W=20/L=61  WR=24.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=172  W=68/L=104  WR=39.5%
- Sharpen: sharpest is T1=T1c (72/104 of losers there)
- **Sharp: n=107  W=35/L=72  WR=32.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L07.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=172  W=68/L=104  WR=39.5%
- Sharpen: sharpest is T1=T1c (72/104 of losers there)
- **Sharp: n=107  W=35/L=72  WR=32.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L08.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=168  W=66/L=102  WR=39.3%
- Sharpen: sharpest is T1=T1c (58/102 of losers there)
- **Sharp: n=75  W=17/L=58  WR=22.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L09.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=168  W=66/L=102  WR=39.3%
- Sharpen: sharpest is T1=T1c (58/102 of losers there)
- **Sharp: n=75  W=17/L=58  WR=22.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L10.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=163  W=57/L=106  WR=35.0%
- Sharpen: sharpest is RSI=RSI4 (61/106 of losers there)
- **Sharp: n=81  W=20/L=61  WR=24.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=157  W=54/L=103  WR=34.4%
- Sharpen: sharpest is RSI=RSI4 (58/103 of losers there)
- **Sharp: n=75  W=17/L=58  WR=22.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=157  W=54/L=103  WR=34.4%
- Sharpen: sharpest is RSI=RSI4 (58/103 of losers there)
- **Sharp: n=75  W=17/L=58  WR=22.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L13.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is T1=T1c (28/87 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L14.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is T1=T1c (28/87 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is T1=T1c (28/87 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L16.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=134  W=46/L=88  WR=34.3%
- Sharpen: sharpest is T1=T1c (29/88 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L17.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=123  W=43/L=80  WR=35.0%
- Sharpen: sharpest is T1=T1c (24/80 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L18.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=123  W=43/L=80  WR=35.0%
- Sharpen: sharpest is T1=T1c (24/80 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L19.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=119  W=45/L=74  WR=37.8%
- Sharpen: sharpest is ZS=ZS6 (22/74 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore >+3 extreme

### L20.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=112  W=35/L=77  WR=31.2%
- Sharpen: sharpest is session_bucket=asia (38/77 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L21.  `H20=H20e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=94  W=25/L=69  WR=26.6%
- Sharpen: sharpest is session_bucket=off_hours (14/69 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=off_hours

### L22.  `H20=H20b AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is T4=T4a (30/56 of losers there)
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L23.  `H60=H60e AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20b (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L24.  `BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20b (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L25.  `H60=H60e AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20b (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/28) | H20e(28/42) |
| H60 | H60a(54/45) | H60e(46/55) |
| T1 | — | — |
| T4 | T4c(56/44) | T4a(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/45) | short(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
