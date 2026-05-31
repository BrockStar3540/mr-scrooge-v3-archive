# NZD_CHF — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **763**  (W=490 / L=273)  -  WR: **64.2%**

## Session distribution

- ny_mid: n=205  W=128/L=77  WR=62.4%
- london_open: n=193  W=126/L=67  WR=65.3%
- asia: n=164  W=108/L=56  WR=65.9%
- ny_close: n=54  W=34/L=20  WR=63.0%
- off_hours: n=53  W=34/L=19  WR=64.2%
- ny_open: n=46  W=30/L=16  WR=65.2%
- london: n=29  W=18/L=11  WR=62.1%
- asia_late: n=19  W=12/L=7  WR=63.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND direction_exec=short`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude session_bucket=london_open drops 7/9 losers (78%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  AVOID when session=london_open

### W02.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude direction_exec=long drops 9/14 losers (64%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when long

### W03.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=97  W=90/L=7  WR=92.8%
- Refine: exclude ZS=ZS2 drops 4/7 losers (57%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W04.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=asia drops 8/13 losers (62%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia

### W05.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude session_bucket=asia drops 7/11 losers (64%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude session_bucket=asia drops 7/11 losers (64%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W07.  `H20=H20a AND T1=T1a AND BBP=BBP4`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude H60=H60a drops 9/11 losers (82%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF60 aligned WITH trade

### W08.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=92  W=84/L=8  WR=91.3%
- Refine: exclude ZS=ZS2 drops 3/8 losers (38%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W09.  `H20=H20a AND T1=T1a AND ZS=ZS4`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/9 losers (33%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when strategy=delta_tag_and_go_v2

### W10.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/9 losers (33%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when strategy=delta_tag_and_go_v2

### W11.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=asia drops 6/12 losers (50%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W12.  `T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude direction_exec=long drops 10/13 losers (77%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when long

### W13.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude session_bucket=london_open drops 6/7 losers (86%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london_open

### W14.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude ZS=ZS2 drops 4/6 losers (67%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W15.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude direction_exec=long drops 7/11 losers (64%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when long

### W16.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude direction_exec=short drops 4/7 losers (57%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when short

### W17.  `T4=T4c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude H60=H60a drops 6/8 losers (75%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/6 losers (50%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when strategy=delta_tag_and_go_v2

### W19.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia

### W20.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude H60=H60a drops 5/5 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W21.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 6/8 losers (75%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W22.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=71  W=66/L=5  WR=93.0%
- Refine: exclude H60=H60a drops 5/5 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W23.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude ZS=ZS2 drops 4/6 losers (67%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W24.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude BBP=BBP4 drops 4/7 losers (57%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when upper third

### W25.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude ZS=ZS2 drops 4/6 losers (67%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is direction_exec=long (44/66 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when long

### L02.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=104  W=32/L=72  WR=30.8%
- Sharpen: sharpest is H20=H20e (46/72 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L03.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is session_bucket=london_open (38/60 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L04.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is T1=T1c (46/57 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND T1=T1c AND RSI=RSI4`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is ZS=ZS4 (38/53 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L06.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: sharpest is T1=T1c (44/52 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when 1h trend AGAINST trade

### L07.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=81  W=32/L=49  WR=39.5%
- Sharpen: sharpest is H20=H20e (32/49 of losers there)
- **Sharp: n=43  W=11/L=32  WR=25.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L08.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=78  W=23/L=55  WR=29.5%
- Sharpen: sharpest is H20=H20e (38/55 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L09.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is ZS=ZS4 (32/45 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L10.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H20=H20e (32/47 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L11.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H20=H20e (32/47 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=18/L=54  WR=25.0%
- Sharpen: sharpest is H20=H20e (38/54 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L13.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=18/L=54  WR=25.0%
- Sharpen: sharpest is H20=H20e (38/54 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L14.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=72  W=19/L=53  WR=26.4%
- Sharpen: sharpest is T1=T1c (33/53 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=71  W=22/L=49  WR=31.0%
- Sharpen: sharpest is H60=H60c (13/49 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L16.  `H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=69  W=26/L=43  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (33/43 of losers there)
- **Sharp: n=47  W=14/L=33  WR=29.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L17.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is RSI=RSI4 (23/41 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=66  W=19/L=47  WR=28.8%
- Sharpen: sharpest is direction_exec=long (33/47 of losers there)
- **Sharp: n=40  W=7/L=33  WR=17.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when long

### L19.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=64  W=14/L=50  WR=21.9%
- Sharpen: sharpest is ZS=ZS4 (16/50 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L20.  `T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is T4=T4a (22/40 of losers there)
- **Sharp: n=29  W=7/L=22  WR=24.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third  •  ONLY when 4h trend WITH trade

### L21.  `T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is session_bucket=london_open (25/41 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L22.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is session_bucket=london_open (25/41 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is session_bucket=ny_mid (22/42 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L24.  `H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is T4=T4a (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is T4=T4a (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(55/33) | H20e(36/56), H20b(0/6) |
| H60 | — | — |
| T1 | T1a(62/40) | T1c(38/60) |
| T4 | T4c(56/47) | T4a(44/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | ZS4(29/34) |
| strategy_id | — | — |
| direction_exec | short(56/43) | long(44/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
