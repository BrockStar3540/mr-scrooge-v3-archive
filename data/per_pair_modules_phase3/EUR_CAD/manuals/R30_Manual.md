# EUR_CAD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,338**  (W=844 / L=494)  -  WR: **63.1%**

## Session distribution

- ny_mid: n=762  W=487/L=275  WR=63.9%
- ny_open: n=235  W=149/L=86  WR=63.4%
- london_open: n=222  W=140/L=82  WR=63.1%
- london: n=79  W=45/L=34  WR=57.0%
- ny_close: n=39  W=23/L=16  WR=59.0%
- asia: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W02.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W03.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W05.  `T1=T1a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W06.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W07.  `H60=H60a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W09.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W10.  `H60=H60a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W11.  `H60=H60e AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude T1=T1b drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  AVOID when 1h trend flat

### W12.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude T1=T1b drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when 1h trend flat

### W13.  `H60=H60e AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude T1=T1b drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  AVOID when 1h trend flat

### W14.  `H20=H20b AND T1=T1a AND ZS=ZS3`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude RSI=RSI3 drops 4/7 losers (57%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 40-50 lower neutral

### W15.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude H20=H20b drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W16.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude H20=H20b drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W17.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude H20=H20b drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W18.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude H20=H20b drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W19.  `BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude H20=H20b drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W20.  `T1=T1a AND RSI=RSI2 AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude H60=H60b drops 2/5 losers (40%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W21.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude H60=H60b drops 2/5 losers (40%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W22.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude H60=H60b drops 2/5 losers (40%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W23.  `H60=H60e AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H20=H20a drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W24.  `T1=T1c AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H20=H20a drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W25.  `ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude H20=H20a drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=193  W=72/L=121  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=193  W=72/L=121  WR=37.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_mid

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=193  W=72/L=121  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=193  W=72/L=121  WR=37.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_mid

### L03.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=193  W=72/L=121  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=193  W=72/L=121  WR=37.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_mid

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=176  W=64/L=112  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=176  W=64/L=112  WR=36.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid

### L05.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is T4=T4c (57/58 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=84  W=29/L=55  WR=34.5%
- Sharpen: sharpest is T4=T4c (54/55 of losers there)
- **Sharp: n=76  W=22/L=54  WR=28.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20d AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is RSI=RSI2 (43/51 of losers there)
- **Sharp: n=58  W=15/L=43  WR=25.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; session=ny_mid  •  ONLY when RSI 30-40 weak

### L08.  `H20=H20d AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is RSI=RSI2 (43/51 of losers there)
- **Sharp: n=58  W=15/L=43  WR=25.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L09.  `H20=H20d AND H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is RSI=RSI2 (43/51 of losers there)
- **Sharp: n=58  W=15/L=43  WR=25.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L10.  `H20=H20d AND H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is RSI=RSI2 (43/51 of losers there)
- **Sharp: n=58  W=15/L=43  WR=25.9%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; session=ny_mid  •  ONLY when RSI 30-40 weak

### L11.  `T1=T1c AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is RSI=RSI2 (26/40 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_mid  •  ONLY when RSI 30-40 weak

### L12.  `T1=T1c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (26/43 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L13.  `T4=T4c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (26/43 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L14.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (26/43 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L15.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (26/43 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L16.  `T1=T1c AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (26/43 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L17.  `T4=T4c AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (26/43 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L18.  `T1=T1c AND T4=T4c AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (26/39 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_mid  •  ONLY when RSI 30-40 weak

### L19.  `T1=T1c AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (26/39 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_mid  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20d AND H60=H60e AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=58  W=15/L=43  WR=25.9%
- Sharpen: sharpest is ZS=ZS3 (9/43 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 30-40 weak; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L21.  `H20=H20b AND T1=T1c AND RSI=RSI2`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L22.  `H20=H20b AND T4=T4c AND RSI=RSI2`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L23.  `H20=H20b AND RSI=RSI2 AND direction_exec=long`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 30-40 weak  •  ONLY when deep below lower band

### L24.  `H20=H20b AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L25.  `H20=H20b AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(45/38) | H60e(40/47) |
| T1 | T1a(54/41) | T1c(44/58) |
| T4 | T4a(56/43) | T4c(44/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/45) | long(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
