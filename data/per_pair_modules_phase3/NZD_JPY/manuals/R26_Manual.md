# NZD_JPY — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,916**  (W=2,535 / L=1,381)  -  WR: **64.7%**

## Session distribution

- asia: n=1227  W=803/L=424  WR=65.4%
- ny_mid: n=527  W=338/L=189  WR=64.1%
- ny_open: n=472  W=308/L=164  WR=65.3%
- ny_close: n=464  W=294/L=170  WR=63.4%
- london_open: n=414  W=262/L=152  WR=63.3%
- london: n=351  W=233/L=118  WR=66.4%
- asia_late: n=342  W=218/L=124  WR=63.7%
- off_hours: n=119  W=79/L=40  WR=66.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=246  W=212/L=34  WR=86.2%
- Refine: exclude H60=H60a drops 13/34 losers (38%)
- **Final: n=216  W=195/L=21  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W02.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=192  W=166/L=26  WR=86.5%
- Refine: exclude T4=T4c drops 8/26 losers (31%)
- **Final: n=180  W=162/L=18  WR=90.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W03.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=192  W=166/L=26  WR=86.5%
- Refine: exclude T4=T4c drops 8/26 losers (31%)
- **Final: n=180  W=162/L=18  WR=90.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=180  W=162/L=18  WR=90.0%
- Refine: exclude H60=H60a drops 9/18 losers (50%)
- **Final: n=158  W=149/L=9  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W05.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=180  W=162/L=18  WR=90.0%
- Refine: exclude H60=H60a drops 9/18 losers (50%)
- **Final: n=158  W=149/L=9  WR=94.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W06.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=162  W=138/L=24  WR=85.2%
- Refine: exclude T1=T1a drops 16/24 losers (67%)
- **Final: n=117  W=109/L=8  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=117  W=109/L=8  WR=93.2%
- Refine: exclude ZS=ZS3 drops 8/8 losers (100%)
- **Final: n=94  W=94/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=109/L=8  WR=93.2%
- Refine: exclude ZS=ZS3 drops 8/8 losers (100%)
- **Final: n=94  W=94/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W09.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W10.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W11.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W12.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude RSI=RSI2 drops 7/10 losers (70%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; session=asia  •  AVOID when RSI 30-40 weak

### W13.  `T1=T1a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 strongly against

### W14.  `ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 strongly against

### W15.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 strongly against

### W16.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 strongly against

### W17.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 strongly against

### W18.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude RSI=RSI2 drops 6/9 losers (67%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W19.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude RSI=RSI2 drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W20.  `H20=H20a AND H60=H60c AND T1=T1a`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T4=T4c drops 8/12 losers (67%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20a AND H60=H60c AND direction_exec=short`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T4=T4c drops 8/12 losers (67%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral  •  AVOID when 4h trend AGAINST trade

### W22.  `H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T4=T4c drops 8/12 losers (67%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade  •  AVOID when 4h trend AGAINST trade

### W23.  `H20=H20a AND H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T4=T4c drops 8/12 losers (67%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when 4h trend AGAINST trade

### W24.  `H60=H60d AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 mildly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W25.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude RSI=RSI1 drops 7/14 losers (50%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when RSI 20-30 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=137  W=47/L=90  WR=34.3%
- Sharpen: sharpest is H60=H60c (42/90 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 neutral

### L02.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=137  W=47/L=90  WR=34.3%
- Sharpen: sharpest is H60=H60c (42/90 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 neutral

### L03.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is T1=T1c (44/61 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when 1h trend AGAINST trade

### L04.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=93  W=32/L=61  WR=34.4%
- Sharpen: sharpest is H20=H20e (26/61 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L05.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=84  W=26/L=58  WR=31.0%
- Sharpen: sharpest is ZS=ZS2 (26/58 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L06.  `H20=H20e AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=83  W=32/L=51  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### L07.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI2`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS1 (18/52 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS1 (18/52 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=76  W=25/L=51  WR=32.9%
- Sharpen: sharpest is H60=H60a (28/51 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_mid (16/49 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L11.  `H20=H20c AND H60=H60a AND T1=T1c`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (22/47 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L12.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (22/47 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  ONLY when session=ny_mid

### L13.  `H20=H20c AND T1=T1c AND direction_exec=long`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (22/47 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L14.  `H20=H20c AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (22/47 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L15.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is ZS=ZS3 (13/47 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L16.  `H20=H20e AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is T4=T4c (31/48 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND H60=H60c AND T1=T1c`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (45/45 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20e AND H60=H60c AND direction_exec=long`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (45/45 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (45/45 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20e AND H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (45/45 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=70  W=21/L=49  WR=30.0%
- Sharpen: sharpest is H60=H60a (26/49 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 aligned WITH trade

### L22.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=69  W=26/L=43  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (25/43 of losers there)
- **Sharp: n=33  W=8/L=25  WR=24.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L23.  `T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is H60=H60b (15/43 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when HTF60 slightly aligned

### L24.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is H60=H60b (15/43 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  lower third; session=ny_mid  •  ONLY when HTF60 slightly aligned

### L25.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is H60=H60b (15/43 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | T4a(53/47) | T4c(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
