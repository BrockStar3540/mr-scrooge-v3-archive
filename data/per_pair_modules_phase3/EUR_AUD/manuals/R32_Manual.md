# EUR_AUD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,768**  (W=2,349 / L=1,419)  -  WR: **62.3%**

## Session distribution

- asia: n=1291  W=826/L=465  WR=64.0%
- ny_close: n=531  W=319/L=212  WR=60.1%
- london: n=448  W=285/L=163  WR=63.6%
- ny_open: n=408  W=253/L=155  WR=62.0%
- ny_mid: n=404  W=238/L=166  WR=58.9%
- london_open: n=348  W=220/L=128  WR=63.2%
- asia_late: n=188  W=125/L=63  WR=66.5%
- off_hours: n=150  W=83/L=67  WR=55.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude T4=T4c drops 9/18 losers (50%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W02.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude T4=T4c drops 9/18 losers (50%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W03.  `H60=H60a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude T4=T4c drops 9/18 losers (50%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude T4=T4c drops 9/18 losers (50%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude T4=T4c drops 9/18 losers (50%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND T1=T1a AND BBP=BBP6`
- Raw: n=123  W=108/L=15  WR=87.8%
- Refine: exclude H60=H60e drops 6/15 losers (40%)
- **Final: n=108  W=99/L=9  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when HTF60 strongly against

### W07.  `T1=T1a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude session_bucket=asia_late drops 9/16 losers (56%)
- **Final: n=102  W=95/L=7  WR=93.1%**
- **Dir: SHORT**  •  1h trend WITH trade; deep above upper band  •  AVOID when session=asia_late

### W08.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W09.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W10.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W11.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W12.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 aligned WITH trade

### W13.  `T1=T1c AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=108  W=95/L=13  WR=88.0%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude BBP=BBP1 drops 3/9 losers (33%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W15.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude BBP=BBP1 drops 3/9 losers (33%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W16.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude H60=H60e drops 4/13 losers (31%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when HTF60 strongly against

### W17.  `H20=H20a AND T4=T4c AND BBP=BBP6`
- Raw: n=101  W=90/L=11  WR=89.1%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=86  W=81/L=5  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF60 strongly against

### W18.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude ZS=ZS6 drops 2/12 losers (17%)
- **Final: n=97  W=87/L=10  WR=89.7%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_open  •  AVOID when zscore >+3 extreme

### W19.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W20.  `H20=H20a AND T1=T1a AND T4=T4c AND BBP=BBP6`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF60 strongly against

### W21.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude ZS=ZS6 drops 2/12 losers (17%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when zscore >+3 extreme

### W22.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude ZS=ZS6 drops 2/12 losers (17%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when zscore >+3 extreme

### W23.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude ZS=ZS6 drops 2/12 losers (17%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when zscore >+3 extreme

### W24.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude ZS=ZS6 drops 2/12 losers (17%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when zscore >+3 extreme

### W25.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude ZS=ZS6 drops 2/12 losers (17%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when zscore >+3 extreme

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=156  W=62/L=94  WR=39.7%
- Sharpen: sharpest is BBP=BBP3 (64/94 of losers there)
- **Sharp: n=95  W=31/L=64  WR=32.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L02.  `H20=H20e AND H60=H60e AND BBP=BBP6`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is T4=T4a (51/73 of losers there)
- **Sharp: n=60  W=9/L=51  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is T4=T4a (51/73 of losers there)
- **Sharp: n=60  W=9/L=51  WR=15.0%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is T4=T4a (51/73 of losers there)
- **Sharp: n=60  W=9/L=51  WR=15.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  ONLY when 4h trend WITH trade

### L05.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND direction_exec=long`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is RSI=RSI3 (40/73 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band  •  ONLY when RSI 40-50 lower neutral

### L06.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is H20=H20e (54/71 of losers there)
- **Sharp: n=63  W=9/L=54  WR=14.3%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=114  W=40/L=74  WR=35.1%
- Sharpen: sharpest is T4=T4a (54/74 of losers there)
- **Sharp: n=63  W=9/L=54  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L08.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is BBP=BBP3 (44/73 of losers there)
- **Sharp: n=61  W=17/L=44  WR=27.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L09.  `H20=H20e AND H60=H60e AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is T4=T4c (60/68 of losers there)
- **Sharp: n=88  W=28/L=60  WR=31.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20e AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is T4=T4c (60/68 of losers there)
- **Sharp: n=88  W=28/L=60  WR=31.8%**
- **Dir: LONG**  •  HTF20 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is BBP=BBP3 (41/69 of losers there)
- **Sharp: n=58  W=17/L=41  WR=29.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L12.  `H60=H60e AND T1=T1a AND T4=T4c AND BBP=BBP3`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is RSI=RSI3 (38/68 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; middle of band  •  ONLY when RSI 40-50 lower neutral

### L13.  `H20=H20e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is T1=T1c (53/65 of losers there)
- **Sharp: n=72  W=19/L=53  WR=26.4%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third  •  ONLY when 1h trend AGAINST trade

### L14.  `H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is H20=H20e (21/63 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L15.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is T4=T4a (50/63 of losers there)
- **Sharp: n=59  W=9/L=50  WR=15.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is T4=T4a (50/63 of losers there)
- **Sharp: n=59  W=9/L=50  WR=15.3%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is H20=H20e (21/63 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L18.  `H20=H20e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is H60=H60e (63/63 of losers there)
- **Sharp: n=80  W=17/L=63  WR=21.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london  •  ONLY when HTF60 strongly against

### L19.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (17/61 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `T4=T4c AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=97  W=31/L=66  WR=32.0%
- Sharpen: sharpest is T1=T1a (40/66 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; middle of band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L21.  `T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is T1=T1a (32/59 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L22.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is T1=T1a (32/59 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L23.  `H60=H60e AND T4=T4c AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is T1=T1a (38/64 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L24.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=94  W=32/L=62  WR=34.0%
- Sharpen: sharpest is BBP=BBP6 (40/62 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L25.  `H20=H20e AND H60=H60a AND session_bucket=ny_close`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is T1=T1c (49/61 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(52/45) | H20e(45/52) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
