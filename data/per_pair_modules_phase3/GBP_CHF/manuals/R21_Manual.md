# GBP_CHF — R21 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,664**  (W=1,708 / L=956)  -  WR: **64.1%**

## Session distribution

- london_open: n=644  W=431/L=213  WR=66.9%
- asia: n=483  W=313/L=170  WR=64.8%
- ny_mid: n=417  W=272/L=145  WR=65.2%
- london: n=379  W=240/L=139  WR=63.3%
- ny_open: n=376  W=227/L=149  WR=60.4%
- ny_close: n=168  W=103/L=65  WR=61.3%
- asia_late: n=138  W=84/L=54  WR=60.9%
- off_hours: n=59  W=38/L=21  WR=64.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=162  W=139/L=23  WR=85.8%
- Refine: exclude ZS=ZS1 drops 15/23 losers (65%)
- **Final: n=132  W=124/L=8  WR=93.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W02.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude BBP=BBP1 drops 13/16 losers (81%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W03.  `T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude BBP=BBP0 drops 7/17 losers (41%)
- **Final: n=116  W=106/L=10  WR=91.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when deep below lower band

### W04.  `H20=H20e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=114  W=102/L=12  WR=89.5%
- Refine: exclude T1=T1c drops 10/12 losers (83%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

### W05.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude BBP=BBP1 drops 12/15 losers (80%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W06.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude H20=H20a drops 11/16 losers (69%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude BBP=BBP0 drops 7/11 losers (64%)
- **Final: n=95  W=91/L=4  WR=95.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when deep below lower band

### W08.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude H20=H20c drops 8/13 losers (62%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 neutral

### W09.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20a drops 9/14 losers (64%)
- **Final: n=51  W=46/L=5  WR=90.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=92  W=86/L=6  WR=93.5%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W11.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20c drops 10/12 losers (83%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when HTF20 neutral

### W12.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T4=T4c drops 11/11 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend AGAINST trade

### W13.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude ZS=ZS1 drops 9/11 losers (82%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `T1=T1a AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20e drops 7/11 losers (64%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W15.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude session_bucket=asia drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W16.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude BBP=BBP2 drops 8/11 losers (73%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W17.  `T1=T1a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H60=H60c drops 7/11 losers (64%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when HTF60 neutral

### W18.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W19.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W20.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=70/L=5  WR=93.3%
- Refine: exclude ZS=ZS1 drops 4/5 losers (80%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W22.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W23.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP1 drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched lower band

### W24.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude direction_exec=long drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_open  •  AVOID when long

### W25.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude T4=T4a drops 8/11 losers (73%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: LONG**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=137  W=53/L=84  WR=38.7%
- Sharpen: sharpest is RSI=RSI4 (62/84 of losers there)
- **Sharp: n=86  W=24/L=62  WR=27.9%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L02.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=39/L=68  WR=36.4%
- Sharpen: sharpest is H20=H20a (37/68 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=100  W=29/L=71  WR=29.0%
- Sharpen: sharpest is ZS=ZS4 (31/71 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +1 to +2 overbought

### L04.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is RSI=RSI4 (37/55 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L05.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (13/55 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when session=asia

### L06.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=88  W=24/L=64  WR=27.3%
- Sharpen: sharpest is T4=T4a (31/64 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when 4h trend WITH trade

### L07.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=86  W=24/L=62  WR=27.9%
- Sharpen: sharpest is ZS=ZS4 (23/62 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +1 to +2 overbought

### L08.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H20=H20e (20/52 of losers there)
- **Sharp: n=26  W=6/L=20  WR=23.1%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L09.  `H20=H20e AND direction_exec=short AND session_bucket=london`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (20/50 of losers there)
- **Sharp: n=26  W=6/L=20  WR=23.1%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is ZS=ZS4 (16/43 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +1 to +2 overbought

### L11.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is RSI=RSI4 (39/44 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L12.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H60=H60a (10/41 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L13.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is H20=H20d (20/43 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 mildly against

### L14.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is H20=H20d (20/42 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  ONLY when HTF20 mildly against

### L15.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is direction_exec=long (21/41 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when long

### L16.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (16/41 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  ONLY when RSI 50-60 upper neutral

### L17.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is H60=H60e (12/43 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L18.  `T1=T1a AND T4=T4a AND BBP=BBP3`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (12/40 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band  •  ONLY when session=asia

### L19.  `T1=T1a AND T4=T4a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (12/40 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=asia

### L20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H60=H60d (18/40 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L21.  `BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is H20=H20a (19/39 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: LONG**  •  upper third; session=asia  •  ONLY when HTF20 aligned WITH trade

### L22.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=61  W=20/L=41  WR=32.8%
- Sharpen: sharpest is H20=H20e (16/41 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L23.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=61  W=20/L=41  WR=32.8%
- Sharpen: sharpest is H20=H20e (16/41 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L24.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is T4=T4a (33/40 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L25.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is session_bucket=london (11/40 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(36/30) | H60a(30/36) |
| T1 | — | — |
| T4 | T4c(53/46) | T4a(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
