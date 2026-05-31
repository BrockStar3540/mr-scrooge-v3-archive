# NZD_CHF — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **781**  (W=545 / L=236)  -  WR: **69.8%**

## Session distribution

- asia: n=327  W=227/L=100  WR=69.4%
- london_open: n=144  W=100/L=44  WR=69.4%
- london: n=89  W=65/L=24  WR=73.0%
- ny_close: n=76  W=56/L=20  WR=73.7%
- ny_open: n=50  W=32/L=18  WR=64.0%
- asia_late: n=43  W=27/L=16  WR=62.8%
- ny_mid: n=34  W=25/L=9  WR=73.5%
- off_hours: n=18  W=13/L=5  WR=72.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=116  W=107/L=9  WR=92.2%
- Refine: exclude H60=H60e drops 4/9 losers (44%)
- **Final: n=101  W=96/L=5  WR=95.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 strongly against

### W02.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude H60=H60e drops 8/13 losers (62%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W03.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude H60=H60e drops 9/12 losers (75%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W04.  `H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=98  W=92/L=6  WR=93.9%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=96  W=87/L=9  WR=90.6%
- Refine: exclude H20=H20a drops 7/9 losers (78%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude ZS=ZS1 drops 8/10 losers (80%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W08.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=90  W=86/L=4  WR=95.6%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W09.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W10.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=83  W=77/L=6  WR=92.8%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend WITH trade

### W11.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=80  W=80/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia

### W12.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=80  W=75/L=5  WR=93.8%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF20 strongly against

### W13.  `H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=79  W=77/L=2  WR=97.5%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude session_bucket=london drops 3/5 losers (60%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W16.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=75  W=72/L=3  WR=96.0%
- Refine: exclude H60=H60d drops 3/3 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 mildly against

### W17.  `H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 aligned WITH trade

### W18.  `H20=H20e AND H60=H60a AND RSI=RSI3`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude T1=T1c drops 5/7 losers (71%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

### W19.  `T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude T1=T1a drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W20.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude session_bucket=off_hours drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when session=off_hours

### W22.  `H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude session_bucket=london drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third  •  AVOID when session=london

### W24.  `H20=H20a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude H60=H60e drops 4/10 losers (40%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W25.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=68  W=64/L=4  WR=94.1%
- Refine: exclude ZS=ZS1 drops 3/4 losers (75%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  AVOID when zscore -3 to -2 deep oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=60  W=16/L=44  WR=26.7%
- Sharpen: sharpest is H60=H60e (24/44 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

### L02.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=55  W=18/L=37  WR=32.7%
- Sharpen: sharpest is T4=T4a (20/37 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (20/33 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L04.  `H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=16/L=34  WR=32.0%
- Sharpen: sharpest is T4=T4a (15/34 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=asia  •  ONLY when 4h trend WITH trade

### L05.  `H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20b (12/32 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L06.  `H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (24/30 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L07.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is RSI=RSI3 (21/30 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L08.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (25/30 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is direction_exec=short (20/26 of losers there)
- **Sharp: n=26  W=6/L=20  WR=23.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when short

### L10.  `H60=H60b AND T4=T4a AND direction_exec=short`
- Raw: n=41  W=8/L=33  WR=19.5%
- Sharpen: sharpest is BBP=BBP6 (11/33 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when deep above upper band

### L11.  `H20=H20b AND T4=T4a AND RSI=RSI3`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is T1=T1a (25/28 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L12.  `H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is T4=T4a (24/28 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is session_bucket=asia (15/25 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=asia

### L14.  `H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is T4=T4a (17/25 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20b AND T1=T1a AND direction_exec=long`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is session_bucket=asia (17/24 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade  •  ONLY when session=asia

### L16.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=37  W=5/L=32  WR=13.5%
- Sharpen: sharpest is H60=H60e (18/32 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

### L17.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=37  W=12/L=25  WR=32.4%
- Sharpen: sharpest is session_bucket=asia (15/25 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L18.  `H60=H60e AND T1=T1a AND ZS=ZS4`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is T4=T4a (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is T4=T4a (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L20.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=34  W=2/L=32  WR=5.9%
- Sharpen: sharpest is RSI=RSI3 (24/32 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20b AND T1=T1a AND RSI=RSI3`
- Raw: n=33  W=5/L=28  WR=15.2%
- Sharpen: sharpest is session_bucket=asia (17/28 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L22.  `H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is H20=H20b (15/21 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade  •  ONLY when HTF20 slightly aligned

### L23.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is H20=H20a (12/21 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L24.  `H20=H20b AND T4=T4a AND session_bucket=asia`
- Raw: n=32  W=10/L=22  WR=31.2%
- Sharpen: sharpest is T1=T1a (18/22 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L25.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=32  W=10/L=22  WR=31.2%
- Sharpen: sharpest is H60=H60e (9/22 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(36/28), H20d(16/10) | H20b(8/20) |
| H60 | H60a(52/20), H60d(11/5) | H60e(24/51), H60b(3/14) |
| T1 | T1c(54/45) | T1a(44/53) |
| T4 | T4c(58/40) | T4a(42/60) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(51/44) | short(49/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
