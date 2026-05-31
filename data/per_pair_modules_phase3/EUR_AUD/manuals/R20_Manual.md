# EUR_AUD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,550**  (W=2,176 / L=1,374)  -  WR: **61.3%**

## Session distribution

- asia: n=960  W=592/L=368  WR=61.7%
- london_open: n=860  W=544/L=316  WR=63.3%
- ny_open: n=450  W=276/L=174  WR=61.3%
- london: n=449  W=252/L=197  WR=56.1%
- ny_mid: n=339  W=199/L=140  WR=58.7%
- ny_close: n=285  W=179/L=106  WR=62.8%
- asia_late: n=175  W=111/L=64  WR=63.4%
- off_hours: n=32  W=23/L=9  WR=71.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude session_bucket=off_hours drops 3/20 losers (15%)
- **Final: n=143  W=126/L=17  WR=88.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W02.  `T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude T4=T4c drops 16/21 losers (76%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band  •  AVOID when 4h trend AGAINST trade

### W03.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude T4=T4c drops 16/21 losers (76%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W04.  `T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude ZS=ZS3 drops 5/18 losers (28%)
- **Final: n=128  W=115/L=13  WR=89.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=london drops 6/18 losers (33%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=london

### W06.  `H60=H60a AND T1=T1c AND BBP=BBP5`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude T4=T4c drops 13/18 losers (72%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  AVOID when 4h trend AGAINST trade

### W07.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude T4=T4c drops 13/18 losers (72%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W08.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude T4=T4c drops 13/18 losers (72%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  AVOID when 4h trend AGAINST trade

### W09.  `T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude H60=H60a drops 8/13 losers (62%)
- **Final: n=86  W=81/L=5  WR=94.2%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W10.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude H60=H60a drops 8/13 losers (62%)
- **Final: n=86  W=81/L=5  WR=94.2%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W11.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude T4=T4c drops 13/18 losers (72%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W12.  `H20=H20e AND H60=H60a AND ZS=ZS5`
- Raw: n=122  W=107/L=15  WR=87.7%
- Refine: exclude session_bucket=london drops 10/15 losers (67%)
- **Final: n=106  W=101/L=5  WR=95.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W13.  `H20=H20e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=122  W=107/L=15  WR=87.7%
- Refine: exclude session_bucket=london drops 10/15 losers (67%)
- **Final: n=106  W=101/L=5  WR=95.3%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W14.  `H20=H20e AND H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=122  W=107/L=15  WR=87.7%
- Refine: exclude session_bucket=london drops 10/15 losers (67%)
- **Final: n=106  W=101/L=5  WR=95.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W15.  `H60=H60e AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W16.  `ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W17.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W18.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W19.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W20.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 8/17 losers (47%)
- **Final: n=95  W=86/L=9  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W21.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 8/17 losers (47%)
- **Final: n=95  W=86/L=9  WR=90.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W22.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude RSI=RSI4 drops 14/14 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W23.  `T4=T4a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude RSI=RSI4 drops 14/14 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20e AND T4=T4c AND BBP=BBP6`
- Raw: n=108  W=100/L=8  WR=92.6%
- Refine: exclude ZS=ZS6 drops 4/8 losers (50%)
- **Final: n=102  W=98/L=4  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when zscore >+3 extreme

### W25.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=102  W=98/L=4  WR=96.1%
- Refine: exclude session_bucket=london drops 4/4 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND ZS=ZS4`
- Raw: n=214  W=81/L=133  WR=37.9%
- Sharpen: sharpest is session_bucket=london (39/133 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=london

### L02.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=214  W=81/L=133  WR=37.9%
- Sharpen: sharpest is session_bucket=london (39/133 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=london

### L03.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=197  W=73/L=124  WR=37.1%
- Sharpen: sharpest is H60=H60a (39/124 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L04.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=155  W=60/L=95  WR=38.7%
- Sharpen: sharpest is H60=H60a (63/95 of losers there)
- **Sharp: n=85  W=22/L=63  WR=25.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L05.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=142  W=43/L=99  WR=30.3%
- Sharpen: sharpest is T4=T4c (52/99 of losers there)
- **Sharp: n=57  W=5/L=52  WR=8.8%**
- **Dir: LONG**  •  just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L06.  `H20=H20a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=140  W=51/L=89  WR=36.4%
- Sharpen: sharpest is T4=T4a (50/89 of losers there)
- **Sharp: n=66  W=16/L=50  WR=24.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=139  W=49/L=90  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/90 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=139  W=49/L=90  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/90 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L09.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=139  W=49/L=90  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/90 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L10.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: sharpest is H60=H60e (29/85 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L11.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=136  W=48/L=88  WR=35.3%
- Sharpen: sharpest is direction_exec=long (73/88 of losers there)
- **Sharp: n=96  W=23/L=73  WR=24.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when long

### L12.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=136  W=48/L=88  WR=35.3%
- Sharpen: sharpest is direction_exec=long (73/88 of losers there)
- **Sharp: n=96  W=23/L=73  WR=24.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when long

### L13.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=133  W=43/L=90  WR=32.3%
- Sharpen: sharpest is T4=T4c (46/90 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  just touched upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L14.  `BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=133  W=43/L=90  WR=32.3%
- Sharpen: sharpest is T4=T4c (46/90 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=131  W=43/L=88  WR=32.8%
- Sharpen: sharpest is T4=T4c (52/88 of losers there)
- **Sharp: n=57  W=5/L=52  WR=8.8%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L16.  `H60=H60e AND BBP=BBP5 AND direction_exec=long`
- Raw: n=131  W=43/L=88  WR=32.8%
- Sharpen: sharpest is T4=T4c (52/88 of losers there)
- **Sharp: n=57  W=5/L=52  WR=8.8%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band  •  ONLY when 4h trend AGAINST trade

### L17.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=131  W=43/L=88  WR=32.8%
- Sharpen: sharpest is T4=T4c (52/88 of losers there)
- **Sharp: n=57  W=5/L=52  WR=8.8%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20e AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=129  W=48/L=81  WR=37.2%
- Sharpen: sharpest is RSI=RSI3 (40/81 of losers there)
- **Sharp: n=41  W=1/L=40  WR=2.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=127  W=47/L=80  WR=37.0%
- Sharpen: sharpest is T4=T4a (52/80 of losers there)
- **Sharp: n=73  W=21/L=52  WR=28.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is session_bucket=london (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; upper third  •  ONLY when session=london

### L21.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=125  W=43/L=82  WR=34.4%
- Sharpen: sharpest is T4=T4c (46/82 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=125  W=43/L=82  WR=34.4%
- Sharpen: sharpest is T4=T4c (46/82 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=125  W=43/L=82  WR=34.4%
- Sharpen: sharpest is T4=T4c (46/82 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20a AND T1=T1c AND BBP=BBP6`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is T4=T4a (43/76 of losers there)
- **Sharp: n=57  W=14/L=43  WR=24.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP6`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is T4=T4a (42/75 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(54/47) | T1a(46/53) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
