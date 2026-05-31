# NZD_JPY — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,805**  (W=1,767 / L=1,038)  -  WR: **63.0%**

## Session distribution

- asia: n=981  W=622/L=359  WR=63.4%
- london: n=459  W=299/L=160  WR=65.1%
- ny_close: n=382  W=243/L=139  WR=63.6%
- london_open: n=322  W=194/L=128  WR=60.2%
- ny_open: n=316  W=194/L=122  WR=61.4%
- asia_late: n=136  W=88/L=48  WR=64.7%
- off_hours: n=108  W=67/L=41  WR=62.0%
- ny_mid: n=101  W=60/L=41  WR=59.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=177  W=152/L=25  WR=85.9%
- Refine: exclude T4=T4a drops 18/25 losers (72%)
- **Final: n=103  W=96/L=7  WR=93.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend WITH trade

### W02.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=157  W=136/L=21  WR=86.6%
- Refine: exclude session_bucket=london_open drops 7/21 losers (33%)
- **Final: n=150  W=136/L=14  WR=90.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W03.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=149  W=128/L=21  WR=85.9%
- Refine: exclude session_bucket=london_open drops 7/21 losers (33%)
- **Final: n=142  W=128/L=14  WR=90.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W04.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=139  W=119/L=20  WR=85.6%
- Refine: exclude session_bucket=ny_open drops 15/20 losers (75%)
- **Final: n=109  W=104/L=5  WR=95.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W05.  `H20=H20a AND T4=T4c AND session_bucket=london`
- Raw: n=131  W=121/L=10  WR=92.4%
- Refine: exclude RSI=RSI3 drops 5/10 losers (50%)
- **Final: n=110  W=105/L=5  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W06.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=london`
- Raw: n=131  W=121/L=10  WR=92.4%
- Refine: exclude RSI=RSI3 drops 5/10 losers (50%)
- **Final: n=110  W=105/L=5  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W07.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=131  W=121/L=10  WR=92.4%
- Refine: exclude RSI=RSI3 drops 5/10 losers (50%)
- **Final: n=110  W=105/L=5  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W08.  `H20=H20a AND BBP=BBP4 AND session_bucket=london`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude T4=T4a drops 13/16 losers (81%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=london`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude T4=T4a drops 13/16 losers (81%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=london  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude T4=T4a drops 13/16 losers (81%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; session=london  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20a AND ZS=ZS4 AND session_bucket=london`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND session_bucket=london`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=london  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when 4h trend WITH trade

### W15.  `T1=T1c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude T4=T4a drops 9/15 losers (60%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude BBP=BBP5 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W17.  `H20=H20a AND T4=T4c AND RSI=RSI5`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude BBP=BBP5 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W18.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude BBP=BBP5 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W19.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude BBP=BBP5 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W20.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude BBP=BBP5 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W21.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude BBP=BBP5 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W22.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude BBP=BBP5 drops 10/13 losers (77%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W23.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude BBP=BBP5 drops 10/13 losers (77%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W24.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude BBP=BBP5 drops 10/13 losers (77%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W25.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude BBP=BBP5 drops 10/13 losers (77%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=179  W=71/L=108  WR=39.7%
- Sharpen: sharpest is T4=T4a (41/108 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L02.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=179  W=71/L=108  WR=39.7%
- Sharpen: sharpest is T4=T4a (41/108 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND H60=H60e AND session_bucket=london`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is T4=T4a (72/90 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND direction_exec=short AND session_bucket=london`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is T4=T4a (72/90 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is T4=T4a (72/90 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  ONLY when 4h trend WITH trade

### L06.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=148  W=49/L=99  WR=33.1%
- Sharpen: sharpest is T4=T4a (63/99 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L07.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=139  W=48/L=91  WR=34.5%
- Sharpen: sharpest is RSI=RSI5 (41/91 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L08.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=133  W=41/L=92  WR=30.8%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L09.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=133  W=41/L=92  WR=30.8%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L10.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=133  W=41/L=92  WR=30.8%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L11.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=133  W=41/L=92  WR=30.8%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L12.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=128  W=36/L=92  WR=28.1%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L13.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=128  W=36/L=92  WR=28.1%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L14.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=128  W=36/L=92  WR=28.1%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=london

### L15.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=128  W=36/L=92  WR=28.1%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=128  W=36/L=92  WR=28.1%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L17.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=128  W=36/L=92  WR=28.1%
- Sharpen: sharpest is session_bucket=london (42/92 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L18.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=127  W=43/L=84  WR=33.9%
- Sharpen: sharpest is session_bucket=london (25/84 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L19.  `H60=H60e AND T4=T4a AND session_bucket=london`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is RSI=RSI5 (42/83 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london  •  ONLY when RSI 60-70 strong

### L20.  `T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is RSI=RSI5 (42/83 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is RSI=RSI5 (42/83 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=london  •  ONLY when RSI 60-70 strong

### L22.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is T4=T4a (41/80 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L23.  `H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=118  W=37/L=81  WR=31.4%
- Sharpen: sharpest is session_bucket=london (25/81 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L24.  `H60=H60e AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=118  W=37/L=81  WR=31.4%
- Sharpen: sharpest is session_bucket=london (25/81 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L25.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is ZS=ZS5 (30/64 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/29), H20b(11/5) | H20e(30/39), H20d(6/12) |
| H60 | — | — |
| T1 | T1c(54/47) | T1a(46/53) |
| T4 | T4c(53/46) | T4a(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
