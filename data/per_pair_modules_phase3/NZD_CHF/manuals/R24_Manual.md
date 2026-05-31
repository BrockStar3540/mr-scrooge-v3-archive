# NZD_CHF — R24 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,480**  (W=1,620 / L=860)  -  WR: **65.3%**

## Session distribution

- asia: n=610  W=412/L=198  WR=67.5%
- london_open: n=478  W=311/L=167  WR=65.1%
- ny_open: n=341  W=223/L=118  WR=65.4%
- ny_close: n=286  W=177/L=109  WR=61.9%
- london: n=280  W=186/L=94  WR=66.4%
- ny_mid: n=256  W=167/L=89  WR=65.2%
- asia_late: n=119  W=76/L=43  WR=63.9%
- off_hours: n=110  W=68/L=42  WR=61.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=143  W=123/L=20  WR=86.0%
- Refine: exclude T4=T4a drops 9/20 losers (45%)
- **Final: n=108  W=97/L=11  WR=89.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W02.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=139  W=120/L=19  WR=86.3%
- Refine: exclude ZS=ZS2 drops 8/19 losers (42%)
- **Final: n=117  W=106/L=11  WR=90.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W03.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude RSI=RSI4 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W04.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude H20=H20b drops 6/11 losers (55%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF20 slightly aligned

### W05.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude ZS=ZS4 drops 6/11 losers (55%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W06.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI2 drops 14/14 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W07.  `H60=H60c AND T4=T4c AND BBP=BBP4`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; upper third  •  AVOID when session=asia

### W08.  `H60=H60c AND T4=T4c AND ZS=ZS4`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W09.  `H60=H60c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia

### W10.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4a drops 8/12 losers (67%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend WITH trade

### W11.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude H60=H60e drops 10/11 losers (91%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W12.  `H60=H60c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI4 drops 4/10 losers (40%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude ZS=ZS2 drops 5/9 losers (56%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W14.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H60=H60b drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when HTF60 slightly aligned

### W15.  `H20=H20e AND H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude session_bucket=ny_mid drops 2/6 losers (33%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W16.  `H20=H20d AND BBP=BBP4 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude T1=T1a drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: SHORT**  •  HTF20 mildly against; upper third  •  AVOID when 1h trend WITH trade

### W17.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H60=H60b drops 6/9 losers (67%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W18.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude T4=T4a drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=68  W=66/L=2  WR=97.1%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 2/2 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when strategy=TF2_pullback_EMA20_long

### W20.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=68  W=66/L=2  WR=97.1%
- Refine: exclude ZS=ZS2 drops 2/2 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W21.  `H60=H60b AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude direction_exec=long drops 9/9 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when long

### W22.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=67  W=62/L=5  WR=92.5%
- Refine: exclude session_bucket=asia drops 4/5 losers (80%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W23.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H60=H60d drops 4/7 losers (57%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: SHORT**  •  upper third; session=ny_open  •  AVOID when HTF60 mildly against

### W24.  `H20=H20d AND ZS=ZS4 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude T1=T1a drops 7/9 losers (78%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20d AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude T1=T1a drops 7/9 losers (78%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  HTF20 mildly against; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is H20=H20e (29/63 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L02.  `H60=H60c AND T1=T1a AND T4=T4a`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is H20=H20a (20/60 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20e AND T1=T1c AND BBP=BBP4`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (19/57 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when session=ny_open

### L04.  `H60=H60c AND T4=T4a AND direction_exec=short`
- Raw: n=89  W=28/L=61  WR=31.5%
- Sharpen: sharpest is BBP=BBP2 (25/61 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when lower third

### L05.  `H20=H20a AND H60=H60c AND T4=T4a`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is direction_exec=short (36/47 of losers there)
- **Sharp: n=50  W=14/L=36  WR=28.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend WITH trade  •  ONLY when short

### L06.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=72  W=21/L=51  WR=29.2%
- Sharpen: sharpest is H20=H20e (28/51 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L07.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is H60=H60e (15/45 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L08.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_open (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_open

### L09.  `H20=H20e AND H60=H60b AND RSI=RSI4 AND direction_exec=long`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_open (15/41 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; RSI 50-60 upper neutral  •  ONLY when session=ny_open

### L10.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=65  W=21/L=44  WR=32.3%
- Sharpen: sharpest is direction_exec=short (21/44 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when short

### L11.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is direction_exec=short (29/41 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when short

### L12.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_open (19/38 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when session=ny_open

### L13.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_open (15/39 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L14.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is T4=T4c (28/37 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60b AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is BBP=BBP0 (14/36 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is T4=T4c (27/36 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_open (16/35 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L18.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is direction_exec=short (28/37 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when short

### L19.  `H60=H60b AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_open (11/34 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: LONG**  •  HTF60 slightly aligned; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_open

### L20.  `H60=H60b AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_open (11/34 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L21.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is H60=H60d (11/34 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF60 mildly against

### L22.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H60=H60a (11/32 of losers there)
- **Sharp: n=14  W=3/L=11  WR=21.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=16/L=36  WR=30.8%
- Sharpen: sharpest is RSI=RSI4 (21/36 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when RSI 50-60 upper neutral

### L24.  `H60=H60c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is T4=T4a (25/34 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: SHORT**  •  HTF60 neutral; lower third  •  ONLY when 4h trend WITH trade

### L25.  `H60=H60c AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is RSI=RSI2 (19/33 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(55/47) | T1a(45/52) |
| T4 | T4c(57/44) | T4a(43/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
