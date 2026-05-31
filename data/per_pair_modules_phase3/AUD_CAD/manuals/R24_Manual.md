# AUD_CAD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,991**  (W=1,917 / L=1,074)  -  WR: **64.1%**

## Session distribution

- asia: n=743  W=474/L=269  WR=63.8%
- ny_mid: n=594  W=382/L=212  WR=64.3%
- london_open: n=528  W=338/L=190  WR=64.0%
- ny_open: n=337  W=209/L=128  WR=62.0%
- ny_close: n=311  W=201/L=110  WR=64.6%
- london: n=283  W=186/L=97  WR=65.7%
- asia_late: n=129  W=84/L=45  WR=65.1%
- off_hours: n=66  W=43/L=23  WR=65.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=133  W=118/L=15  WR=88.7%
- Refine: exclude strategy_id=bravo_failed_momentum drops 6/15 losers (40%)
- **Final: n=124  W=115/L=9  WR=92.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  AVOID when strategy=bravo_failed_momentum

### W02.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=129  W=112/L=17  WR=86.8%
- Refine: exclude H20=H20a drops 15/17 losers (88%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=128  W=109/L=19  WR=85.2%
- Refine: exclude session_bucket=asia drops 9/19 losers (47%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

### W04.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=124  W=110/L=14  WR=88.7%
- Refine: exclude strategy_id=bravo_failed_momentum drops 5/14 losers (36%)
- **Final: n=118  W=109/L=9  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; lower third  •  AVOID when strategy=bravo_failed_momentum

### W05.  `H20=H20c AND T1=T1c AND T4=T4a`
- Raw: n=121  W=108/L=13  WR=89.3%
- Refine: exclude BBP=BBP0 drops 5/13 losers (38%)
- **Final: n=116  W=108/L=8  WR=93.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when deep below lower band

### W06.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude session_bucket=asia drops 8/16 losers (50%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W07.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude H20=H20a drops 5/15 losers (33%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/9 losers (44%)
- **Final: n=103  W=98/L=5  WR=95.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when strategy=bravo_failed_momentum

### W09.  `H60=H60e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude H20=H20a drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude H20=H20a drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/9 losers (44%)
- **Final: n=97  W=92/L=5  WR=94.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when strategy=bravo_failed_momentum

### W12.  `H20=H20e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W13.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude RSI=RSI4 drops 6/13 losers (46%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W14.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude strategy_id=bravo_failed_momentum drops 5/13 losers (38%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; lower third  •  AVOID when strategy=bravo_failed_momentum

### W15.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=87  W=77/L=10  WR=88.5%
- Refine: exclude BBP=BBP0 drops 6/10 losers (60%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when deep below lower band

### W16.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W17.  `H20=H20e AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W18.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 5/10 losers (50%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=ny_open

### W19.  `T4=T4a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude H20=H20d drops 5/12 losers (42%)
- **Final: n=71  W=64/L=7  WR=90.1%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 mildly against

### W20.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude H20=H20d drops 5/12 losers (42%)
- **Final: n=71  W=64/L=7  WR=90.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 mildly against

### W21.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W22.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W23.  `H20=H20c AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude BBP=BBP0 drops 5/9 losers (56%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when deep below lower band

### W24.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H20=H20a drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 aligned WITH trade

### W25.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H20=H20a drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is H20=H20c (16/82 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 neutral

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is H20=H20c (17/75 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 neutral

### L03.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=116  W=44/L=72  WR=37.9%
- Sharpen: sharpest is ZS=ZS2 (63/72 of losers there)
- **Sharp: n=94  W=31/L=63  WR=33.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L04.  `H60=H60e AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=111  W=42/L=69  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=42/L=69  WR=37.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; lower third

### L05.  `T1=T1a AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=94  W=31/L=63  WR=33.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=94  W=31/L=63  WR=33.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L06.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=92  W=31/L=61  WR=33.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=92  W=31/L=61  WR=33.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L07.  `H20=H20c AND T1=T1a AND T4=T4c`
- Raw: n=86  W=27/L=59  WR=31.4%
- Sharpen: sharpest is RSI=RSI4 (29/59 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L08.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20a (39/50 of losers there)
- **Sharp: n=54  W=15/L=39  WR=27.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is H20=H20c (13/50 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 neutral

### L10.  `H60=H60a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is H20=H20a (39/48 of losers there)
- **Sharp: n=54  W=15/L=39  WR=27.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is H20=H20a (39/48 of losers there)
- **Sharp: n=54  W=15/L=39  WR=27.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 aligned WITH trade

### L12.  `T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is H20=H20a (31/42 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L13.  `H20=H20b AND H60=H60e AND T1=T1a`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is ZS=ZS1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H20=H20b AND T1=T1a AND direction_exec=short`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is ZS=ZS1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H20=H20b AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is ZS=ZS1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H20=H20b AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is ZS=ZS1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20b AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is ZS=ZS1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is H60=H60a (15/42 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L19.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is H20=H20a (31/42 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 aligned WITH trade

### L20.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_mid (14/40 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L21.  `H20=H20c AND T4=T4c AND direction_exec=long`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (16/39 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L22.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is H20=H20c (13/43 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 neutral

### L23.  `H60=H60a AND T4=T4c AND session_bucket=london`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is H20=H20a (31/40 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L24.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is H20=H20a (31/40 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L25.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20b (12/41 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(58/42) | T4c(42/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
