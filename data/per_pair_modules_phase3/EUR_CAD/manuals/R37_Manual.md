# EUR_CAD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,607**  (W=1,651 / L=956)  -  WR: **63.3%**

## Session distribution

- ny_close: n=898  W=542/L=356  WR=60.4%
- asia: n=871  W=574/L=297  WR=65.9%
- off_hours: n=217  W=142/L=75  WR=65.4%
- london: n=172  W=110/L=62  WR=64.0%
- ny_mid: n=152  W=100/L=52  WR=65.8%
- london_open: n=118  W=73/L=45  WR=61.9%
- ny_open: n=115  W=69/L=46  WR=60.0%
- asia_late: n=64  W=41/L=23  WR=64.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=ny_close drops 13/17 losers (76%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W02.  `H60=H60e AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=114  W=102/L=12  WR=89.5%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=off_hours  •  AVOID when 1h trend WITH trade

### W03.  `H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude direction_exec=long drops 7/16 losers (44%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when long

### W04.  `T4=T4a AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W05.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=100  W=88/L=12  WR=88.0%
- Refine: exclude RSI=RSI5 drops 10/12 losers (83%)
- **Final: n=90  W=88/L=2  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W06.  `T4=T4a AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=88  W=87/L=1  WR=98.9%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W07.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=96  W=87/L=9  WR=90.6%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude RSI=RSI5 drops 10/12 losers (83%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W09.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude T4=T4c drops 13/14 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W10.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=90  W=87/L=3  WR=96.7%
- Refine: exclude H20=H20e drops 2/3 losers (67%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W11.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20b drops 8/9 losers (89%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W12.  `H20=H20a AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude RSI=RSI5 drops 10/12 losers (83%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W13.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude H20=H20b drops 8/9 losers (89%)
- **Final: n=78  W=77/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W14.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude RSI=RSI5 drops 10/13 losers (77%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W15.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude H20=H20b drops 7/8 losers (88%)
- **Final: n=76  W=75/L=1  WR=98.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W16.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude session_bucket=off_hours drops 6/10 losers (60%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral  •  AVOID when session=off_hours

### W17.  `T4=T4c AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/11 losers (64%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=off_hours  •  AVOID when upper third

### W18.  `H20=H20a AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude RSI=RSI5 drops 10/12 losers (83%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W19.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude H20=H20b drops 7/8 losers (88%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W20.  `H20=H20c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude session_bucket=asia drops 5/6 losers (83%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF20 neutral; RSI 50-60 upper neutral  •  AVOID when session=asia

### W21.  `H20=H20c AND T1=T1a AND RSI=RSI4`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W22.  `H20=H20c AND T4=T4c AND RSI=RSI4`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W23.  `H20=H20c AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W24.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=80  W=77/L=3  WR=96.2%
- Refine: exclude H20=H20e drops 2/3 losers (67%)
- **Final: n=76  W=75/L=1  WR=98.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND T4=T4a AND ZS=ZS2`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 3/12 losers (25%)
- **Final: n=77  W=68/L=9  WR=88.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=106  W=32/L=74  WR=30.2%
- Sharpen: sharpest is session_bucket=ny_close (32/74 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L02.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is T1=T1a (57/57 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L03.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is direction_exec=long (29/53 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when long

### L04.  `H20=H20a AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=85  W=33/L=52  WR=38.8%
- Sharpen: sharpest is session_bucket=london (13/52 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=london

### L05.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=81  W=32/L=49  WR=39.5%
- Sharpen: sharpest is direction_exec=long (26/49 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when long

### L06.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=81  W=32/L=49  WR=39.5%
- Sharpen: sharpest is direction_exec=long (26/49 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when long

### L07.  `H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=80  W=26/L=54  WR=32.5%
- Sharpen: sharpest is H20=H20e (41/54 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade  •  ONLY when HTF20 strongly against

### L08.  `H60=H60a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=77  W=24/L=53  WR=31.2%
- Sharpen: sharpest is H20=H20c (27/53 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=off_hours  •  ONLY when HTF20 neutral

### L09.  `H60=H60b AND T1=T1a AND T4=T4c`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is BBP=BBP6 (8/47 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when deep above upper band

### L10.  `H60=H60b AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is BBP=BBP6 (8/47 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when deep above upper band

### L11.  `H20=H20e AND H60=H60d AND direction_exec=short`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is T4=T4a (21/50 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against  •  ONLY when 4h trend WITH trade

### L12.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is H20=H20d (8/46 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 mildly against

### L13.  `H20=H20e AND T1=T1a AND BBP=BBP6`
- Raw: n=71  W=14/L=57  WR=19.7%
- Sharpen: sharpest is session_bucket=ny_close (32/57 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when session=ny_close

### L14.  `H20=H20e AND T1=T1a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=71  W=14/L=57  WR=19.7%
- Sharpen: sharpest is session_bucket=ny_close (32/57 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L15.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=71  W=16/L=55  WR=22.5%
- Sharpen: sharpest is H60=H60e (47/55 of losers there)
- **Sharp: n=51  W=4/L=47  WR=7.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L16.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=70  W=18/L=52  WR=25.7%
- Sharpen: sharpest is direction_exec=long (47/52 of losers there)
- **Sharp: n=51  W=4/L=47  WR=7.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when long

### L17.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is session_bucket=london (9/41 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=london

### L18.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is session_bucket=ny_close (16/41 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L19.  `H60=H60e AND T1=T1a AND BBP=BBP6`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_close (17/38 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when session=ny_close

### L20.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_close (17/38 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when session=ny_close

### L21.  `H60=H60e AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_close (17/38 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when session=ny_close

### L22.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=61  W=19/L=42  WR=31.1%
- Sharpen: sharpest is H60=H60d (27/42 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  ONLY when HTF60 mildly against

### L23.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_mid (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=ny_mid

### L24.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_mid (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=ny_mid

### L25.  `H20=H20c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=60  W=17/L=43  WR=28.3%
- Sharpen: sharpest is session_bucket=off_hours (22/43 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 50-60 upper neutral  •  ONLY when session=off_hours

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(54/47) | T1a(46/53) |
| T4 | T4a(53/48) | T4c(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/44) | short(47/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
