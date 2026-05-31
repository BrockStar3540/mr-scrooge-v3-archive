# NZD_USD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,235**  (W=781 / L=454)  -  WR: **63.2%**

## Session distribution

- asia: n=404  W=268/L=136  WR=66.3%
- ny_close: n=261  W=161/L=100  WR=61.7%
- london_open: n=156  W=101/L=55  WR=64.7%
- london: n=120  W=64/L=56  WR=53.3%
- ny_mid: n=110  W=69/L=41  WR=62.7%
- ny_open: n=67  W=45/L=22  WR=67.2%
- asia_late: n=62  W=37/L=25  WR=59.7%
- off_hours: n=55  W=36/L=19  WR=65.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: no further refinement
- **Final: n=82  W=70/L=12  WR=85.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; RSI 20-30 oversold

### W02.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: no further refinement
- **Final: n=82  W=70/L=12  WR=85.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; RSI 20-30 oversold

### W03.  `H20=H20a AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: no further refinement
- **Final: n=82  W=70/L=12  WR=85.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; RSI 20-30 oversold

### W04.  `H20=H20a AND H60=H60e AND T1=T1a`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=london drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=london

### W05.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=london drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when session=london

### W06.  `H20=H20a AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=london drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=london

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: no further refinement
- **Final: n=79  W=68/L=11  WR=86.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: no further refinement
- **Final: n=79  W=68/L=11  WR=86.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold

### W09.  `H20=H20a AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: no further refinement
- **Final: n=79  W=68/L=11  WR=86.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold

### W10.  `H20=H20e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude BBP=BBP0 drops 7/7 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when deep below lower band

### W11.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude BBP=BBP0 drops 7/7 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  AVOID when deep below lower band

### W12.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude BBP=BBP0 drops 7/7 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when deep below lower band

### W13.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude BBP=BBP1 drops 8/10 losers (80%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when just touched lower band

### W14.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude H60=H60a drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W15.  `H20=H20a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W16.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=asia drops 6/9 losers (67%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=asia

### W17.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=59  W=54/L=5  WR=91.5%
- Refine: exclude H20=H20c drops 3/5 losers (60%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF20 neutral

### W18.  `H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=56  W=53/L=3  WR=94.6%
- Refine: exclude H20=H20a drops 3/3 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=56  W=53/L=3  WR=94.6%
- Refine: exclude H20=H20a drops 3/3 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=56  W=53/L=3  WR=94.6%
- Refine: exclude H20=H20a drops 3/3 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=50  W=48/L=2  WR=96.0%
- Refine: exclude H60=H60a drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W22.  `T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=50  W=48/L=2  WR=96.0%
- Refine: exclude H60=H60a drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W23.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=50  W=48/L=2  WR=96.0%
- Refine: exclude H60=H60a drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W24.  `H60=H60e AND T4=T4a AND RSI=RSI1`
- Raw: n=49  W=43/L=6  WR=87.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=asia

### W25.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=49  W=43/L=6  WR=87.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is session_bucket=ny_close (31/85 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_close

### L02.  `BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is session_bucket=ny_close (31/85 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  lower third; RSI 20-30 oversold  •  ONLY when session=ny_close

### L03.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is session_bucket=ny_close (31/85 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_close

### L04.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=118  W=32/L=86  WR=27.1%
- Sharpen: sharpest is session_bucket=ny_close (31/86 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_close

### L05.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=117  W=32/L=85  WR=27.4%
- Sharpen: sharpest is session_bucket=ny_close (31/85 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_close

### L06.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=117  W=32/L=85  WR=27.4%
- Sharpen: sharpest is session_bucket=ny_close (31/85 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_close

### L07.  `H20=H20e AND T1=T1c AND RSI=RSI1`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (27/70 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_close

### L08.  `H20=H20e AND T4=T4c AND RSI=RSI1`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (27/70 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_close

### L09.  `H20=H20e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (27/70 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold  •  ONLY when session=ny_close

### L10.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (27/70 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_close

### L11.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (27/70 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_close

### L12.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (27/70 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_close

### L13.  `T1=T1c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L14.  `T4=T4c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L15.  `RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L16.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L17.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L18.  `T1=T1c AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L19.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L20.  `T4=T4c AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L21.  `BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is session_bucket=ny_close (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: LONG**  •  lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L22.  `T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=110  W=37/L=73  WR=33.6%
- Sharpen: sharpest is H60=H60a (28/73 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is H60=H60b (18/63 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 slightly aligned

### L24.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=97  W=32/L=65  WR=33.0%
- Sharpen: sharpest is H60=H60b (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 slightly aligned

### L25.  `H20=H20e AND direction_exec=long AND session_bucket=asia`
- Raw: n=97  W=32/L=65  WR=33.0%
- Sharpen: sharpest is H60=H60b (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=asia  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/39) | H20e(41/53) |
| H60 | H60e(40/35) | H60b(2/8) |
| T1 | T1a(59/38) | T1c(41/62) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | RSI1(35/40) |
| ZS | — | ZS2(34/39) |
| strategy_id | — | — |
| direction_exec | short(59/38) | long(41/62) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
