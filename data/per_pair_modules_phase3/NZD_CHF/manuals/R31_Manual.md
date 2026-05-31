# NZD_CHF — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,404**  (W=921 / L=483)  -  WR: **65.6%**

## Session distribution

- asia: n=551  W=376/L=175  WR=68.2%
- ny_close: n=279  W=171/L=108  WR=61.3%
- london_open: n=129  W=88/L=41  WR=68.2%
- ny_mid: n=121  W=76/L=45  WR=62.8%
- ny_open: n=116  W=82/L=34  WR=70.7%
- london: n=89  W=55/L=34  WR=61.8%
- asia_late: n=61  W=36/L=25  WR=59.0%
- off_hours: n=58  W=37/L=21  WR=63.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=143  W=122/L=21  WR=85.3%
- Refine: exclude ZS=ZS3 drops 11/21 losers (52%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W02.  `H20=H20e AND H60=H60e AND ZS=ZS1`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP0 drops 9/13 losers (69%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W03.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=83  W=76/L=7  WR=91.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W04.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude session_bucket=ny_mid drops 4/10 losers (40%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W05.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude session_bucket=ny_mid drops 4/10 losers (40%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W06.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude BBP=BBP0 drops 7/11 losers (64%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W07.  `H20=H20e AND H60=H60a AND session_bucket=asia`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude ZS=ZS4 drops 5/11 losers (45%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP0 drops 10/12 losers (83%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W09.  `H20=H20e AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP0 drops 10/12 losers (83%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W10.  `H20=H20e AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T4=T4c drops 6/9 losers (67%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP4 drops 5/9 losers (56%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  AVOID when upper third

### W12.  `H20=H20a AND H60=H60c AND T1=T1a`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when session=asia

### W13.  `H20=H20a AND H60=H60c AND direction_exec=short`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral  •  AVOID when session=asia

### W14.  `H20=H20a AND H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when session=asia

### W15.  `H20=H20e AND H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude ZS=ZS4 drops 4/10 losers (40%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when zscore +1 to +2 overbought

### W16.  `H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=london drops 4/10 losers (40%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W17.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=66  W=60/L=6  WR=90.9%
- Refine: exclude T4=T4c drops 5/6 losers (83%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND H60=H60e AND BBP=BBP1`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude session_bucket=asia drops 3/4 losers (75%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  AVOID when session=asia

### W19.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude session_bucket=asia drops 3/4 losers (75%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W20.  `H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude RSI=RSI1 drops 3/9 losers (33%)
- **Final: n=56  W=50/L=6  WR=89.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  AVOID when RSI 20-30 oversold

### W21.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude BBP=BBP4 drops 5/9 losers (56%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when upper third

### W22.  `H60=H60e AND T4=T4a AND ZS=ZS2`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude RSI=RSI1 drops 3/8 losers (38%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 20-30 oversold

### W23.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude RSI=RSI1 drops 3/8 losers (38%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 20-30 oversold

### W24.  `H20=H20a AND H60=H60c AND T4=T4a`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude RSI=RSI2 drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W25.  `H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude session_bucket=london drops 4/8 losers (50%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND ZS=ZS1`
- Raw: n=79  W=30/L=49  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_close (15/49 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L02.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_close (15/49 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L03.  `H20=H20e AND H60=H60c AND T1=T1c`
- Raw: n=57  W=14/L=43  WR=24.6%
- Sharpen: sharpest is session_bucket=ny_close (27/43 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L04.  `H20=H20e AND H60=H60c AND direction_exec=long`
- Raw: n=57  W=14/L=43  WR=24.6%
- Sharpen: sharpest is session_bucket=ny_close (27/43 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral  •  ONLY when session=ny_close

### L05.  `H20=H20e AND H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=57  W=14/L=43  WR=24.6%
- Sharpen: sharpest is session_bucket=ny_close (27/43 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L06.  `H20=H20a AND H60=H60a AND session_bucket=ny_close`
- Raw: n=55  W=17/L=38  WR=30.9%
- Sharpen: sharpest is T4=T4c (15/38 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L07.  `H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is RSI=RSI2 (30/30 of losers there)
- **Sharp: n=41  W=11/L=30  WR=26.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L08.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is RSI=RSI2 (30/30 of losers there)
- **Sharp: n=41  W=11/L=30  WR=26.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L09.  `H20=H20e AND H60=H60c AND T4=T4c`
- Raw: n=46  W=13/L=33  WR=28.3%
- Sharpen: sharpest is RSI=RSI1 (19/33 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L10.  `H20=H20e AND H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=46  W=13/L=33  WR=28.3%
- Sharpen: sharpest is RSI=RSI1 (19/33 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L11.  `H20=H20e AND H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=46  W=13/L=33  WR=28.3%
- Sharpen: sharpest is RSI=RSI1 (19/33 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L12.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is T4=T4c (15/28 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L13.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=44  W=13/L=31  WR=29.5%
- Sharpen: sharpest is session_bucket=ny_mid (12/31 of losers there)
- **Sharp: n=15  W=3/L=12  WR=20.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=ny_mid

### L14.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L15.  `H20=H20c AND T1=T1c AND direction_exec=long`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=asia

### L16.  `H20=H20c AND T4=T4c AND direction_exec=long`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when session=asia

### L17.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L18.  `H20=H20a AND H60=H60a AND BBP=BBP1`
- Raw: n=43  W=13/L=30  WR=30.2%
- Sharpen: sharpest is session_bucket=ny_close (14/30 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band  •  ONLY when session=ny_close

### L19.  `H20=H20a AND H60=H60a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=43  W=13/L=30  WR=30.2%
- Sharpen: sharpest is session_bucket=ny_close (14/30 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L20.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=asia

### L21.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L22.  `H20=H20c AND H60=H60e AND direction_exec=long`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against  •  ONLY when session=asia

### L23.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L24.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=asia

### L25.  `H20=H20c AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (18/28 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(42/31) | H20a(33/42) |
| H60 | H60e(41/32) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | RSI2(68/62) | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
