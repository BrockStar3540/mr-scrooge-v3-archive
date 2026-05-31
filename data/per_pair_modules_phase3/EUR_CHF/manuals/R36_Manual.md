# EUR_CHF — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **874**  (W=565 / L=309)  -  WR: **64.6%**

## Session distribution

- ny_mid: n=291  W=187/L=104  WR=64.3%
- london_open: n=220  W=139/L=81  WR=63.2%
- ny_open: n=114  W=67/L=47  WR=58.8%
- asia: n=103  W=71/L=32  WR=68.9%
- london: n=60  W=44/L=16  WR=73.3%
- ny_close: n=54  W=35/L=19  WR=64.8%
- off_hours: n=32  W=22/L=10  WR=68.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60c AND T1=T1a AND T4=T4c`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 6/10 losers (60%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W02.  `H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude ZS=ZS5 drops 4/9 losers (44%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore +2 to +3 deep overbought

### W03.  `T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20a drops 5/9 losers (56%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude ZS=ZS5 drops 4/9 losers (44%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore +2 to +3 deep overbought

### W05.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20a drops 5/9 losers (56%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60c AND T4=T4c AND RSI=RSI4`
- Raw: n=59  W=56/L=3  WR=94.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when just touched lower band

### W07.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude session_bucket=ny_open drops 6/8 losers (75%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W08.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  AVOID when 4h trend AGAINST trade

### W09.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W10.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude H20=H20a drops 5/8 losers (62%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W11.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude H20=H20a drops 5/8 losers (62%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W13.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W14.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W15.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude H20=H20e drops 5/7 losers (71%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 strongly against

### W16.  `H60=H60c AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when just touched lower band

### W17.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=49  W=43/L=6  WR=87.8%
- Refine: exclude H60=H60a drops 3/6 losers (50%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 aligned WITH trade

### W18.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W20.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W21.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W22.  `T1=T1a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=47  W=45/L=2  WR=95.7%
- Refine: exclude H20=H20d drops 2/2 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 mildly against

### W23.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=47  W=45/L=2  WR=95.7%
- Refine: exclude H20=H20d drops 2/2 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 mildly against

### W24.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 2/5 losers (40%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W25.  `H20=H20b AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=44  W=41/L=3  WR=93.2%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF20 slightly aligned; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is T4=T4a (18/26 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L02.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (12/25 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L03.  `H60=H60c AND T4=T4a AND RSI=RSI4`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is H20=H20e (10/31 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L04.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=39  W=13/L=26  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (13/26 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L05.  `T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=38  W=12/L=26  WR=31.6%
- Sharpen: sharpest is H20=H20e (15/26 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (9/23 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L07.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (9/23 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L08.  `H60=H60c AND T4=T4a AND direction_exec=long`
- Raw: n=33  W=8/L=25  WR=24.2%
- Sharpen: sharpest is ZS=ZS5 (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60c AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=33  W=8/L=25  WR=24.2%
- Sharpen: sharpest is H20=H20e (10/25 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L10.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is T4=T4c (9/21 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is T4=T4c (9/21 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is T4=T4c (9/21 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is H20=H20e (15/19 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is H20=H20e (15/19 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L15.  `T1=T1c AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=30  W=8/L=22  WR=26.7%
- Sharpen: sharpest is T4=T4c (13/22 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L16.  `H60=H60c AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=30  W=8/L=22  WR=26.7%
- Sharpen: sharpest is ZS=ZS5 (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=30  W=8/L=22  WR=26.7%
- Sharpen: sharpest is T4=T4c (13/22 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20a AND T4=T4a AND ZS=ZS6`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (12/18 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore >+3 extreme  •  ONLY when RSI 50-60 upper neutral

### L19.  `H20=H20a AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (12/18 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore >+3 extreme  •  ONLY when RSI 50-60 upper neutral

### L20.  `T4=T4a AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (12/18 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore >+3 extreme  •  ONLY when RSI 50-60 upper neutral

### L21.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (12/18 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore >+3 extreme  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(35/26) | H20a(30/39) |
| H60 | H60e(41/35) | H60a(33/40) |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | T4c(55/41) | T4a(44/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/48) | short(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
