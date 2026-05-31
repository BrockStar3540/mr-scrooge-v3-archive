# GBP_CHF — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,057**  (W=1,306 / L=751)  -  WR: **63.5%**

## Session distribution

- london_open: n=765  W=490/L=275  WR=64.1%
- ny_mid: n=465  W=299/L=166  WR=64.3%
- london: n=304  W=181/L=123  WR=59.5%
- ny_open: n=218  W=141/L=77  WR=64.7%
- asia: n=187  W=126/L=61  WR=67.4%
- ny_close: n=72  W=43/L=29  WR=59.7%
- asia_late: n=31  W=16/L=15  WR=51.6%
- off_hours: n=15  W=10/L=5  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=152  W=130/L=22  WR=85.5%
- Refine: exclude H20=H20a drops 10/22 losers (45%)
- **Final: n=105  W=93/L=12  WR=88.6%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=141  W=120/L=21  WR=85.1%
- Refine: no further refinement
- **Final: n=141  W=120/L=21  WR=85.1%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### W03.  `H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude H20=H20e drops 6/13 losers (46%)
- **Final: n=123  W=116/L=7  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF20 strongly against

### W04.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude session_bucket=london drops 7/16 losers (44%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W05.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude T1=T1c drops 14/14 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W06.  `H20=H20a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude T1=T1c drops 16/16 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W07.  `T4=T4a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 8/15 losers (53%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W08.  `H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=98  W=91/L=7  WR=92.9%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade  •  AVOID when HTF20 strongly against

### W09.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H20=H20e drops 6/12 losers (50%)
- **Final: n=81  W=75/L=6  WR=92.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF20 strongly against

### W10.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W11.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude BBP=BBP0 drops 5/13 losers (38%)
- **Final: n=84  W=76/L=8  WR=90.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W12.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W13.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T1=T1a drops 10/13 losers (77%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W14.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=91  W=86/L=5  WR=94.5%
- Refine: exclude ZS=ZS4 drops 2/5 losers (40%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W15.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude ZS=ZS2 drops 10/12 losers (83%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  AVOID when zscore -2 to -1 oversold

### W16.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude session_bucket=ny_mid drops 8/8 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W17.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude BBP=BBP4 drops 7/12 losers (58%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W18.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=84  W=79/L=5  WR=94.0%
- Refine: exclude H20=H20e drops 4/5 losers (80%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W19.  `H60=H60e AND T4=T4a AND BBP=BBP0`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20c drops 7/7 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when HTF20 neutral

### W20.  `RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=83  W=77/L=6  WR=92.8%
- Refine: exclude H60=H60c drops 4/6 losers (67%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 neutral

### W21.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude session_bucket=ny_mid drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W22.  `T1=T1a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W23.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP2 drops 10/12 losers (83%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W24.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude T1=T1c drops 10/10 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when 1h trend AGAINST trade

### W25.  `H60=H60e AND T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=147  W=51/L=96  WR=34.7%
- Sharpen: sharpest is direction_exec=short (61/96 of losers there)
- **Sharp: n=85  W=24/L=61  WR=28.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when short

### L02.  `H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is H20=H20c (22/92 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when HTF20 neutral

### L03.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is direction_exec=short (55/86 of losers there)
- **Sharp: n=75  W=20/L=55  WR=26.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when short

### L04.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is direction_exec=short (55/86 of losers there)
- **Sharp: n=75  W=20/L=55  WR=26.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when short

### L05.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=114  W=42/L=72  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (28/72 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L06.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=102  W=29/L=73  WR=28.4%
- Sharpen: sharpest is RSI=RSI3 (51/73 of losers there)
- **Sharp: n=62  W=11/L=51  WR=17.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L07.  `H20=H20c AND H60=H60a AND RSI=RSI3`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is direction_exec=short (27/62 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when short

### L08.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=97  W=33/L=64  WR=34.0%
- Sharpen: sharpest is RSI=RSI3 (37/64 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=95  W=33/L=62  WR=34.7%
- Sharpen: sharpest is RSI=RSI3 (35/62 of losers there)
- **Sharp: n=46  W=11/L=35  WR=23.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L10.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is BBP=BBP0 (35/57 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L11.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is BBP=BBP0 (26/59 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L12.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is direction_exec=short (40/56 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when short

### L13.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is T4=T4c (40/53 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20e AND H60=H60a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is BBP=BBP0 (27/53 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L15.  `H60=H60a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is direction_exec=long (37/59 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when long

### L16.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=85  W=24/L=61  WR=28.2%
- Sharpen: sharpest is H20=H20c (20/61 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 neutral

### L17.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is direction_exec=short (35/57 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when short

### L18.  `H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is RSI=RSI3 (35/53 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is T4=T4c (19/49 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20a AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is T4=T4c (19/49 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=79  W=23/L=56  WR=29.1%
- Sharpen: sharpest is session_bucket=london_open (15/56 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L22.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=79  W=30/L=49  WR=38.0%
- Sharpen: sharpest is direction_exec=short (43/49 of losers there)
- **Sharp: n=64  W=21/L=43  WR=32.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when short

### L23.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=78  W=25/L=53  WR=32.1%
- Sharpen: sharpest is session_bucket=london (27/53 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london

### L24.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=77  W=26/L=51  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=77  W=26/L=51  WR=33.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 40-50 lower neutral

### L25.  `H20=H20e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (28/49 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(8/1) | H20d(2/8) |
| H60 | H60e(49/30) | H60a(31/50) |
| T1 | — | — |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/48) | short(45/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
