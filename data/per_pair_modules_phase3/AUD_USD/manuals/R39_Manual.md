# AUD_USD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,266**  (W=1,429 / L=837)  -  WR: **63.1%**

## Session distribution

- asia: n=780  W=497/L=283  WR=63.7%
- london_open: n=346  W=210/L=136  WR=60.7%
- ny_mid: n=311  W=202/L=109  WR=65.0%
- london: n=245  W=164/L=81  WR=66.9%
- ny_open: n=236  W=137/L=99  WR=58.1%
- ny_close: n=231  W=142/L=89  WR=61.5%
- asia_late: n=111  W=73/L=38  WR=65.8%
- off_hours: n=6  W=4/L=2  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=287  W=245/L=42  WR=85.4%
- Refine: exclude H20=H20e drops 13/42 losers (31%)
- **Final: n=246  W=217/L=29  WR=88.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W02.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=268  W=230/L=38  WR=85.8%
- Refine: exclude T4=T4a drops 16/38 losers (42%)
- **Final: n=229  W=207/L=22  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend WITH trade

### W03.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=268  W=230/L=38  WR=85.8%
- Refine: exclude T4=T4a drops 16/38 losers (42%)
- **Final: n=229  W=207/L=22  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W04.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=268  W=230/L=38  WR=85.8%
- Refine: exclude T4=T4a drops 16/38 losers (42%)
- **Final: n=229  W=207/L=22  WR=90.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend WITH trade

### W05.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=263  W=229/L=34  WR=87.1%
- Refine: exclude H60=H60b drops 12/34 losers (35%)
- **Final: n=229  W=207/L=22  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 slightly aligned

### W06.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=263  W=229/L=34  WR=87.1%
- Refine: exclude H60=H60b drops 12/34 losers (35%)
- **Final: n=229  W=207/L=22  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 slightly aligned

### W07.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=263  W=229/L=34  WR=87.1%
- Refine: exclude H60=H60b drops 12/34 losers (35%)
- **Final: n=229  W=207/L=22  WR=90.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 slightly aligned

### W08.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=229  W=207/L=22  WR=90.4%
- Refine: exclude BBP=BBP2 drops 11/22 losers (50%)
- **Final: n=158  W=147/L=11  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W09.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=176  W=151/L=25  WR=85.8%
- Refine: exclude H60=H60b drops 10/25 losers (40%)
- **Final: n=144  W=129/L=15  WR=89.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W10.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=154  W=135/L=19  WR=87.7%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 4/19 losers (21%)
- **Final: n=146  W=131/L=15  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when strategy=alpha_extended_fade_v2

### W11.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude RSI=RSI2 drops 14/20 losers (70%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  AVOID when RSI 30-40 weak

### W12.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude RSI=RSI2 drops 14/18 losers (78%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when RSI 30-40 weak

### W13.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude RSI=RSI2 drops 14/18 losers (78%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  AVOID when RSI 30-40 weak

### W14.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude RSI=RSI2 drops 14/18 losers (78%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when RSI 30-40 weak

### W15.  `H20=H20a AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H60=H60b drops 5/12 losers (42%)
- **Final: n=83  W=76/L=7  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 slightly aligned

### W16.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude T4=T4a drops 7/14 losers (50%)
- **Final: n=83  W=76/L=7  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W17.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI3 drops 6/13 losers (46%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W18.  `H20=H20a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude T1=T1a drops 11/14 losers (79%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend WITH trade

### W19.  `H60=H60e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude strategy_id=BR5_opening_range_breakout_short drops 2/6 losers (33%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when strategy=BR5_opening_range_breakout_short

### W20.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude strategy_id=BR5_opening_range_breakout_short drops 2/6 losers (33%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london  •  AVOID when strategy=BR5_opening_range_breakout_short

### W21.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude strategy_id=BR5_opening_range_breakout_short drops 2/6 losers (33%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when strategy=BR5_opening_range_breakout_short

### W22.  `H20=H20a AND T4=T4c AND BBP=BBP4`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=london_open drops 5/8 losers (62%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W23.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=london_open drops 5/8 losers (62%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W24.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=london_open drops 5/8 losers (62%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W25.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude session_bucket=london_open drops 5/7 losers (71%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=177  W=60/L=117  WR=33.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia

### L02.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=177  W=60/L=117  WR=33.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia

### L03.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=177  W=60/L=117  WR=33.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia

### L04.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=160  W=54/L=106  WR=33.8%
- Sharpen: sharpest is RSI=RSI3 (27/106 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L05.  `T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is H20=H20e (45/67 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 strongly against

### L06.  `T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is H20=H20e (42/60 of losers there)
- **Sharp: n=60  W=18/L=42  WR=30.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is H60=H60e (34/56 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

### L08.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is H20=H20e (34/56 of losers there)
- **Sharp: n=41  W=7/L=34  WR=17.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 strongly against

### L09.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is H20=H20e (42/53 of losers there)
- **Sharp: n=60  W=18/L=42  WR=30.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 strongly against

### L10.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is H20=H20e (42/53 of losers there)
- **Sharp: n=60  W=18/L=42  WR=30.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 strongly against

### L11.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=79  W=30/L=49  WR=38.0%
- Sharpen: sharpest is H20=H20e (27/49 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is RSI=RSI2 (42/50 of losers there)
- **Sharp: n=51  W=9/L=42  WR=17.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L13.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is RSI=RSI2 (42/50 of losers there)
- **Sharp: n=51  W=9/L=42  WR=17.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L14.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is RSI=RSI2 (42/50 of losers there)
- **Sharp: n=51  W=9/L=42  WR=17.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L15.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is H20=H20e (34/47 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 strongly against

### L16.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is H20=H20e (15/42 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 strongly against

### L17.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (12/41 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L18.  `H60=H60a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20e (15/42 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 strongly against

### L19.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20e (15/42 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 strongly against

### L20.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is H20=H20e (14/41 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is RSI=RSI1 (10/40 of losers there)
- **Sharp: n=12  W=2/L=10  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L22.  `T1=T1a AND T4=T4a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is RSI=RSI3 (17/38 of losers there)
- **Sharp: n=23  W=6/L=17  WR=26.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral; session=asia  •  ONLY when RSI 40-50 lower neutral

### L23.  `T4=T4a AND ZS=ZS3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is RSI=RSI3 (17/38 of losers there)
- **Sharp: n=23  W=6/L=17  WR=26.1%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -1 to +1 neutral; session=asia  •  ONLY when RSI 40-50 lower neutral

### L24.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=62  W=10/L=52  WR=16.1%
- Sharpen: sharpest is BBP=BBP0 (13/52 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when deep below lower band

### L25.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is H20=H20e (14/41 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(52/37) | H20e(35/48) |
| H60 | H60a(49/39) | H60e(41/48) |
| T1 | T1c(56/45) | T1a(44/55) |
| T4 | T4c(53/47) | T4a(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/45) | short(45/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
