# AUD_CHF — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,659**  (W=1,099 / L=560)  -  WR: **66.2%**

## Session distribution

- asia: n=583  W=398/L=185  WR=68.3%
- ny_close: n=297  W=193/L=104  WR=65.0%
- london: n=169  W=113/L=56  WR=66.9%
- ny_mid: n=145  W=92/L=53  WR=63.4%
- london_open: n=127  W=78/L=49  WR=61.4%
- ny_open: n=124  W=88/L=36  WR=71.0%
- off_hours: n=111  W=69/L=42  WR=62.2%
- asia_late: n=103  W=68/L=35  WR=66.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W02.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W03.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  AVOID when middle of band

### W04.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W05.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W06.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when middle of band

### W07.  `H60=H60e AND BBP=BBP4 AND session_bucket=london`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude RSI=RSI6 drops 4/7 losers (57%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=london  •  AVOID when RSI 70-80 overbought

### W08.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude RSI=RSI6 drops 4/7 losers (57%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=london  •  AVOID when RSI 70-80 overbought

### W09.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude RSI=RSI6 drops 4/7 losers (57%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=london  •  AVOID when RSI 70-80 overbought

### W10.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude RSI=RSI6 drops 4/7 losers (57%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=london  •  AVOID when RSI 70-80 overbought

### W11.  `H20=H20d AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude BBP=BBP4 drops 6/7 losers (86%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 mildly against; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W12.  `H60=H60e AND ZS=ZS4 AND session_bucket=london`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI6 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london  •  AVOID when RSI 70-80 overbought

### W13.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND session_bucket=london`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI6 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=london  •  AVOID when RSI 70-80 overbought

### W14.  `H60=H60e AND T4=T4c AND ZS=ZS4 AND session_bucket=london`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI6 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=london  •  AVOID when RSI 70-80 overbought

### W15.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI6 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=london  •  AVOID when RSI 70-80 overbought

### W16.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=london`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI6 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london  •  AVOID when RSI 70-80 overbought

### W17.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W18.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W19.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W20.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W21.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W22.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W23.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude H60=H60a drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W24.  `H20=H20c AND T1=T1a AND direction_exec=long`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude H60=H60a drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W25.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude H60=H60a drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is H20=H20a (19/36 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20a (17/34 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20a (17/34 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L04.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20a (17/34 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L05.  `T1=T1a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20a (24/32 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L06.  `T4=T4a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20a (24/32 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L07.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20a (24/32 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20a (24/32 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20a (24/32 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L10.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20a (24/32 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=45  W=12/L=33  WR=26.7%
- Sharpen: sharpest is ZS=ZS5 (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=45  W=12/L=33  WR=26.7%
- Sharpen: sharpest is ZS=ZS5 (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=45  W=12/L=33  WR=26.7%
- Sharpen: sharpest is ZS=ZS5 (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H60=H60a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=44  W=13/L=31  WR=29.5%
- Sharpen: sharpest is ZS=ZS5 (8/31 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=44  W=13/L=31  WR=29.5%
- Sharpen: sharpest is ZS=ZS5 (8/31 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=44  W=13/L=31  WR=29.5%
- Sharpen: sharpest is ZS=ZS5 (8/31 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=44  W=13/L=31  WR=29.5%
- Sharpen: sharpest is ZS=ZS5 (8/31 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is session_bucket=london_open (8/27 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L19.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is session_bucket=london_open (8/27 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=london_open

### L20.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is session_bucket=london_open (8/27 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L21.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: sharpest is ZS=ZS5 (14/31 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: sharpest is ZS=ZS5 (14/31 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: sharpest is ZS=ZS5 (14/31 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=41  W=12/L=29  WR=29.3%
- Sharpen: sharpest is H60=H60b (13/29 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when HTF60 slightly aligned

### L25.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=41  W=12/L=29  WR=29.3%
- Sharpen: sharpest is H60=H60b (13/29 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(37/29), H20d(17/11) | H20a(30/38), H20b(10/17) |
| H60 | H60e(52/39) | H60a(39/51) |
| T1 | T1c(57/44) | T1a(43/56) |
| T4 | T4c(57/44) | T4a(43/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(57/45) | long(43/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
