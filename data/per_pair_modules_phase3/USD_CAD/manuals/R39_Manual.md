# USD_CAD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,183**  (W=2,043 / L=1,140)  -  WR: **64.2%**

## Session distribution

- london_open: n=817  W=533/L=284  WR=65.2%
- london: n=620  W=394/L=226  WR=63.5%
- ny_open: n=470  W=293/L=177  WR=62.3%
- ny_close: n=455  W=295/L=160  WR=64.8%
- asia: n=356  W=231/L=125  WR=64.9%
- ny_mid: n=236  W=150/L=86  WR=63.6%
- asia_late: n=130  W=82/L=48  WR=63.1%
- off_hours: n=99  W=65/L=34  WR=65.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=205  W=176/L=29  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 11/29 losers (38%)
- **Final: n=168  W=150/L=18  WR=89.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_close

### W02.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=165  W=145/L=20  WR=87.9%
- Refine: exclude ZS=ZS3 drops 9/20 losers (45%)
- **Final: n=135  W=124/L=11  WR=91.9%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude RSI=RSI3 drops 9/19 losers (47%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W04.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude H20=H20a drops 14/21 losers (67%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W05.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=138  W=124/L=14  WR=89.9%
- Refine: exclude T1=T1a drops 11/14 losers (79%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend WITH trade

### W06.  `H20=H20e AND H60=H60a AND session_bucket=london_open`
- Raw: n=126  W=112/L=14  WR=88.9%
- Refine: exclude RSI=RSI3 drops 12/14 losers (86%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W07.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude session_bucket=asia drops 6/18 losers (33%)
- **Final: n=119  W=107/L=12  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W08.  `H20=H20e AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude session_bucket=off_hours drops 6/18 losers (33%)
- **Final: n=117  W=105/L=12  WR=89.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W09.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude session_bucket=off_hours drops 6/18 losers (33%)
- **Final: n=116  W=104/L=12  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W10.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude H20=H20a drops 8/16 losers (50%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H20=H20c drops 8/17 losers (47%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 neutral

### W12.  `H60=H60b AND T4=T4a AND RSI=RSI4`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude T1=T1c drops 10/13 losers (77%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W13.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude H20=H20c drops 5/11 losers (45%)
- **Final: n=91  W=85/L=6  WR=93.4%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W14.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=asia drops 8/16 losers (50%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W15.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=103  W=95/L=8  WR=92.2%
- Refine: exclude direction_exec=long drops 4/8 losers (50%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when long

### W16.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20a drops 7/12 losers (58%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20c drops 8/15 losers (53%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 neutral

### W18.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20a drops 8/15 losers (53%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W19.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20a drops 8/15 losers (53%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W20.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=98  W=91/L=7  WR=92.9%
- Refine: exclude T1=T1a drops 6/7 losers (86%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend WITH trade

### W21.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=81  W=75/L=6  WR=92.6%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude RSI=RSI4 drops 11/12 losers (92%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 50-60 upper neutral

### W23.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H60=H60e drops 13/14 losers (93%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF60 strongly against

### W24.  `H60=H60b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude session_bucket=asia_late drops 4/9 losers (44%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=asia_late

### W25.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20c AND H60=H60a AND direction_exec=short`
- Raw: n=170  W=68/L=102  WR=40.0%
- Sharpen: sharpest is T1=T1a (40/102 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade  •  ONLY when 1h trend WITH trade

### L02.  `H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is ZS=ZS4 (23/70 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L03.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is H60=H60e (19/66 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 strongly against

### L04.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=105  W=36/L=69  WR=34.3%
- Sharpen: sharpest is ZS=ZS4 (27/69 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +1 to +2 overbought

### L05.  `H60=H60d AND T4=T4c AND RSI=RSI4`
- Raw: n=96  W=35/L=61  WR=36.5%
- Sharpen: sharpest is T1=T1c (26/61 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20a AND H60=H60e AND session_bucket=london_open`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is RSI=RSI4 (34/58 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L07.  `T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=95  W=36/L=59  WR=37.9%
- Sharpen: sharpest is H20=H20a (35/59 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is T4=T4c (29/60 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  HTF60 strongly against; deep above upper band  •  ONLY when 4h trend AGAINST trade

### L09.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is T4=T4c (29/60 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20a AND T4=T4c AND session_bucket=london_open`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is RSI=RSI4 (37/52 of losers there)
- **Sharp: n=50  W=13/L=37  WR=26.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L11.  `T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is H60=H60e (29/48 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when HTF60 strongly against

### L12.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is T4=T4c (26/49 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L13.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is H60=H60e (31/45 of losers there)
- **Sharp: n=42  W=11/L=31  WR=26.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF60 strongly against

### L14.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=72  W=27/L=45  WR=37.5%
- Sharpen: sharpest is BBP=BBP5 (11/45 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when just touched upper band

### L15.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is RSI=RSI4 (29/45 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is RSI=RSI4 (27/43 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L17.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=68  W=17/L=51  WR=25.0%
- Sharpen: sharpest is H20=H20e (33/51 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L18.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=67  W=21/L=46  WR=31.3%
- Sharpen: sharpest is H60=H60e (22/46 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF60 strongly against

### L19.  `H20=H20c AND H60=H60a AND T4=T4a`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is RSI=RSI4 (23/43 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L20.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is RSI=RSI4 (23/43 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L21.  `H20=H20c AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is RSI=RSI4 (23/43 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L22.  `H60=H60e AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is T4=T4c (17/41 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when 4h trend AGAINST trade

### L23.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=66  W=18/L=48  WR=27.3%
- Sharpen: sharpest is ZS=ZS5 (13/48 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is T4=T4a (28/41 of losers there)
- **Sharp: n=39  W=11/L=28  WR=28.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is ZS=ZS4 (18/40 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(38/30) | H20a(34/40) |
| H60 | — | H60d(5/11) |
| T1 | — | — |
| T4 | T4a(57/45) | T4c(43/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
