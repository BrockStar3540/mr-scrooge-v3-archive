# EUR_CHF — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **961**  (W=630 / L=331)  -  WR: **65.6%**

## Session distribution

- london_open: n=262  W=172/L=90  WR=65.6%
- asia: n=247  W=160/L=87  WR=64.8%
- ny_mid: n=216  W=146/L=70  WR=67.6%
- london: n=93  W=61/L=32  WR=65.6%
- ny_open: n=61  W=37/L=24  WR=60.7%
- ny_close: n=42  W=29/L=13  WR=69.0%
- asia_late: n=25  W=16/L=9  WR=64.0%
- off_hours: n=15  W=9/L=6  WR=60.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND direction_exec=short AND session_bucket=london`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude H60=H60c drops 4/7 losers (57%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london  •  AVOID when HTF60 neutral

### W02.  `H20=H20a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W03.  `H20=H20a AND T4=T4a AND session_bucket=london`
- Raw: n=45  W=39/L=6  WR=86.7%
- Refine: exclude H60=H60c drops 4/6 losers (67%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF60 neutral

### W04.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=45  W=39/L=6  WR=86.7%
- Refine: exclude H60=H60c drops 4/6 losers (67%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF60 neutral

### W05.  `T4=T4a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude H60=H60a drops 3/3 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF60 aligned WITH trade

### W06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W07.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak  •  AVOID when session=asia

### W08.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W09.  `H20=H20a AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W10.  `T1=T1a AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W11.  `H20=H20a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=london  •  AVOID when 1h trend WITH trade

### W12.  `T4=T4a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when 1h trend WITH trade

### W13.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when 1h trend WITH trade

### W15.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=london  •  AVOID when 1h trend WITH trade

### W16.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude T1=T1a drops 2/2 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when 1h trend WITH trade

### W17.  `H60=H60a AND T4=T4a AND session_bucket=london`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when 1h trend WITH trade

### W18.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when lower third

### W20.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W21.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when lower third

### W22.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude session_bucket=asia drops 3/3 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W23.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude session_bucket=asia drops 3/3 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W24.  `T4=T4a AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude session_bucket=asia drops 3/3 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W25.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=36  W=33/L=3  WR=91.7%
- Refine: exclude T1=T1a drops 3/3 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is H20=H20a (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is T1=T1a (6/27 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L03.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is T1=T1a (6/27 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L04.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is T1=T1a (6/24 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L05.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is T4=T4c (5/21 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; session=london_open  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60a AND BBP=BBP2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is T4=T4c (5/21 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; session=london_open  •  ONLY when 4h trend AGAINST trade

### L07.  `T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is T1=T1a (11/21 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london  •  ONLY when 1h trend WITH trade

### L08.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=32  W=12/L=20  WR=37.5%
- Sharpen: sharpest is ZS=ZS3 (6/20 of losers there)
- **Sharp: n=7  W=1/L=6  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when zscore -1 to +1 neutral

### L09.  `T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (11/19 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L10.  `T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (11/19 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L11.  `ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (11/19 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L12.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (11/19 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L13.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (11/19 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L14.  `T4=T4c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (11/19 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(49/44), H20b(7/2) | H20d(2/8), H20e(41/47) |
| H60 | — | — |
| T1 | T1c(54/48) | T1a(46/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | RSI3(26/21) | RSI1(11/17) |
| ZS | — | ZS1(15/21) |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
