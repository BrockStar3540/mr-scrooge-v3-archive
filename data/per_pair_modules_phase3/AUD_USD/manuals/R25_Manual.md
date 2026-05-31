# AUD_USD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,843**  (W=1,146 / L=697)  -  WR: **62.2%**

## Session distribution

- asia: n=421  W=268/L=153  WR=63.7%
- london_open: n=416  W=255/L=161  WR=61.3%
- ny_mid: n=327  W=213/L=114  WR=65.1%
- london: n=242  W=160/L=82  WR=66.1%
- ny_open: n=186  W=99/L=87  WR=53.2%
- ny_close: n=150  W=92/L=58  WR=61.3%
- asia_late: n=92  W=53/L=39  WR=57.6%
- off_hours: n=9  W=6/L=3  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude ZS=ZS3 drops 7/12 losers (58%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  AVOID when zscore -1 to +1 neutral

### W02.  `H20=H20c AND T1=T1c AND direction_exec=long`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W03.  `H20=H20c AND H60=H60a AND T1=T1c`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude T4=T4a drops 6/7 losers (86%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  AVOID when 4h trend WITH trade

### W05.  `H20=H20c AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W06.  `H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when 1h trend WITH trade

### W07.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london  •  AVOID when 1h trend WITH trade

### W08.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when 1h trend WITH trade

### W09.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W10.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI4 drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  AVOID when 4h trend WITH trade

### W15.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude RSI=RSI4 drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W16.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude RSI=RSI4 drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W17.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude RSI=RSI4 drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W18.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 mildly against

### W19.  `T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 mildly against

### W20.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 mildly against

### W21.  `H60=H60a AND T1=T1a AND session_bucket=london`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/8 losers (25%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when strategy=delta_tag_and_go_v2

### W22.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/8 losers (25%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when strategy=delta_tag_and_go_v2

### W23.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/8 losers (25%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when strategy=delta_tag_and_go_v2

### W24.  `T4=T4a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H60=H60e drops 3/9 losers (33%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when HTF60 strongly against

### W25.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (15/59 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L02.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (15/59 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L03.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (15/59 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L04.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (18/46 of losers there)
- **Sharp: n=23  W=5/L=18  WR=21.7%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  ONLY when session=london_open

### L05.  `H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=67  W=19/L=48  WR=28.4%
- Sharpen: sharpest is RSI=RSI3 (26/48 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L06.  `T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is T4=T4c (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=60  W=20/L=40  WR=33.3%
- Sharpen: sharpest is session_bucket=london_open (17/40 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  ONLY when session=london_open

### L08.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is T4=T4a (19/36 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L09.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI5 (27/41 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20c AND H60=H60e AND T1=T1a`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is session_bucket=london_open (16/39 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  ONLY when session=london_open

### L11.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is H20=H20c (15/39 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 neutral

### L12.  `H20=H20c AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=59  W=20/L=39  WR=33.9%
- Sharpen: sharpest is session_bucket=london_open (16/39 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  ONLY when session=london_open

### L13.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=58  W=15/L=43  WR=25.9%
- Sharpen: sharpest is BBP=BBP0 (12/43 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  ONLY when deep below lower band

### L14.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is T4=T4a (19/36 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L15.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is T4=T4a (19/36 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L16.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is T4=T4a (19/36 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20a AND H60=H60a AND session_bucket=ny_close`
- Raw: n=56  W=14/L=42  WR=25.0%
- Sharpen: sharpest is T4=T4a (27/42 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=56  W=14/L=42  WR=25.0%
- Sharpen: sharpest is T4=T4a (27/42 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L19.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is T4=T4c (23/39 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london_open  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60e AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is T4=T4c (22/38 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is T4=T4c (22/38 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=54  W=19/L=35  WR=35.2%
- Sharpen: sharpest is BBP=BBP5 (10/35 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when just touched upper band

### L23.  `H60=H60e AND RSI=RSI4 AND session_bucket=london`
- Raw: n=54  W=19/L=35  WR=35.2%
- Sharpen: sharpest is BBP=BBP4 (20/35 of losers there)
- **Sharp: n=26  W=6/L=20  WR=23.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london  •  ONLY when upper third

### L24.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=54  W=19/L=35  WR=35.2%
- Sharpen: sharpest is BBP=BBP5 (10/35 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when just touched upper band

### L25.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=54  W=19/L=35  WR=35.2%
- Sharpen: sharpest is BBP=BBP4 (20/35 of losers there)
- **Sharp: n=26  W=6/L=20  WR=23.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(55/47) | T1c(45/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
