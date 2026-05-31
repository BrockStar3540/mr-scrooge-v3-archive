# AUD_JPY — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,865**  (W=1,186 / L=679)  -  WR: **63.6%**

## Session distribution

- asia: n=632  W=400/L=232  WR=63.3%
- london_open: n=406  W=262/L=144  WR=64.5%
- ny_mid: n=288  W=178/L=110  WR=61.8%
- ny_open: n=146  W=95/L=51  WR=65.1%
- off_hours: n=143  W=83/L=60  WR=58.0%
- asia_late: n=124  W=83/L=41  WR=66.9%
- london: n=92  W=62/L=30  WR=67.4%
- ny_close: n=34  W=23/L=11  WR=67.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=165  W=145/L=20  WR=87.9%
- Refine: exclude ZS=ZS1 drops 9/20 losers (45%)
- **Final: n=141  W=130/L=11  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -3 to -2 deep oversold

### W02.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=165  W=145/L=20  WR=87.9%
- Refine: exclude ZS=ZS1 drops 9/20 losers (45%)
- **Final: n=141  W=130/L=11  WR=92.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -3 to -2 deep oversold

### W03.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=127  W=114/L=13  WR=89.8%
- Refine: exclude H20=H20e drops 8/13 losers (62%)
- **Final: n=119  W=114/L=5  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 strongly against

### W04.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=127  W=114/L=13  WR=89.8%
- Refine: exclude H20=H20e drops 8/13 losers (62%)
- **Final: n=119  W=114/L=5  WR=95.8%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  AVOID when HTF20 strongly against

### W05.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=127  W=114/L=13  WR=89.8%
- Refine: exclude H20=H20e drops 8/13 losers (62%)
- **Final: n=119  W=114/L=5  WR=95.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 strongly against

### W06.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude H60=H60e drops 12/16 losers (75%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W07.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=92  W=90/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W08.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=92  W=90/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W09.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=92  W=90/L=2  WR=97.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W10.  `H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W11.  `T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W12.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W13.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W14.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W15.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude ZS=ZS3 drops 6/16 losers (38%)
- **Final: n=88  W=78/L=10  WR=88.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude ZS=ZS3 drops 6/16 losers (38%)
- **Final: n=88  W=78/L=10  WR=88.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W17.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude ZS=ZS3 drops 6/16 losers (38%)
- **Final: n=88  W=78/L=10  WR=88.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=london drops 4/10 losers (40%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W19.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=london drops 4/10 losers (40%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W20.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=london drops 4/10 losers (40%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W21.  `H20=H20a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1c drops 9/12 losers (75%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

### W22.  `H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1c drops 9/12 losers (75%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

### W23.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1c drops 9/12 losers (75%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

### W24.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1c drops 9/12 losers (75%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

### W25.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude T1=T1c drops 9/12 losers (75%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=239  W=95/L=144  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (50/144 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L02.  `T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=239  W=95/L=144  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (50/144 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L03.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=239  W=95/L=144  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (50/144 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L04.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=162  W=58/L=104  WR=35.8%
- Sharpen: sharpest is session_bucket=off_hours (41/104 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=off_hours

### L05.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=147  W=55/L=92  WR=37.4%
- Sharpen: sharpest is session_bucket=off_hours (31/92 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=off_hours

### L06.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=147  W=55/L=92  WR=37.4%
- Sharpen: sharpest is session_bucket=off_hours (31/92 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=off_hours

### L07.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=147  W=55/L=92  WR=37.4%
- Sharpen: sharpest is session_bucket=off_hours (31/92 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=off_hours

### L08.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is RSI=RSI3 (39/81 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=127  W=39/L=88  WR=30.7%
- Sharpen: sharpest is session_bucket=off_hours (31/88 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=off_hours

### L10.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=127  W=39/L=88  WR=30.7%
- Sharpen: sharpest is session_bucket=off_hours (31/88 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=off_hours

### L11.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is T1=T1c (50/65 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L12.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is T1=T1c (50/65 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L13.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is T1=T1c (50/65 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L14.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (54/58 of losers there)
- **Sharp: n=75  W=21/L=54  WR=28.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L15.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (54/58 of losers there)
- **Sharp: n=75  W=21/L=54  WR=28.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (54/58 of losers there)
- **Sharp: n=75  W=21/L=54  WR=28.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L17.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (39/62 of losers there)
- **Sharp: n=50  W=11/L=39  WR=22.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L18.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (39/62 of losers there)
- **Sharp: n=50  W=11/L=39  WR=22.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L19.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=93  W=31/L=62  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (39/62 of losers there)
- **Sharp: n=50  W=11/L=39  WR=22.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L20.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=93  W=35/L=58  WR=37.6%
- Sharpen: sharpest is BBP=BBP1 (34/58 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L21.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=92  W=34/L=58  WR=37.0%
- Sharpen: sharpest is RSI=RSI4 (35/58 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L22.  `H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is session_bucket=off_hours (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=off_hours

### L23.  `T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is session_bucket=off_hours (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=off_hours

### L24.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is session_bucket=off_hours (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=off_hours

### L25.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is session_bucket=off_hours (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=off_hours

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(54/37) | H20e(36/53) |
| H60 | H60a(60/40) | H60e(40/60) |
| T1 | T1a(56/42) | T1c(44/58) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(60/40) | short(40/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
