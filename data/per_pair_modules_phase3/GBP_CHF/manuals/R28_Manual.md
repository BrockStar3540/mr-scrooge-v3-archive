# GBP_CHF — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,630**  (W=1,671 / L=959)  -  WR: **63.5%**

## Session distribution

- london_open: n=777  W=495/L=282  WR=63.7%
- ny_open: n=391  W=260/L=131  WR=66.5%
- ny_mid: n=352  W=221/L=131  WR=62.8%
- london: n=350  W=215/L=135  WR=61.4%
- asia: n=309  W=191/L=118  WR=61.8%
- ny_close: n=248  W=165/L=83  WR=66.5%
- asia_late: n=133  W=86/L=47  WR=64.7%
- off_hours: n=70  W=38/L=32  WR=54.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude H20=H20c drops 6/15 losers (40%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when HTF20 neutral

### W02.  `ZS=ZS1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude H20=H20c drops 6/15 losers (40%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when HTF20 neutral

### W03.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude H20=H20c drops 6/15 losers (40%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when HTF20 neutral

### W04.  `H20=H20b AND direction_exec=short AND session_bucket=london_open`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude H60=H60e drops 11/14 losers (79%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; session=london_open  •  AVOID when HTF60 strongly against

### W05.  `H20=H20b AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude H60=H60e drops 11/14 losers (79%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W06.  `H60=H60e AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude BBP=BBP0 drops 8/11 losers (73%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=london_open  •  AVOID when deep below lower band

### W07.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20c drops 5/13 losers (38%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when HTF20 neutral

### W08.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20c drops 5/13 losers (38%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when HTF20 neutral

### W09.  `H20=H20e AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 30-40 weak

### W10.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when RSI 30-40 weak

### W11.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W12.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W13.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when lower third

### W14.  `H20=H20b AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W15.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 strongly against

### W16.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H60=H60e drops 8/11 losers (73%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 strongly against

### W17.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 30-40 weak

### W19.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP0 drops 8/8 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; session=london_open  •  AVOID when deep below lower band

### W20.  `T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 mildly against

### W21.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H20=H20d drops 3/9 losers (33%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 mildly against

### W22.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=71  W=67/L=4  WR=94.4%
- Refine: exclude ZS=ZS2 drops 4/4 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -2 to -1 oversold

### W23.  `T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude H20=H20d drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 mildly against

### W24.  `ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude H20=H20d drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 mildly against

### W25.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude H20=H20d drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is H20=H20e (22/75 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L02.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is H20=H20e (22/75 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L03.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is H20=H20e (22/75 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L04.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is H60=H60e (36/70 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L05.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=110  W=40/L=70  WR=36.4%
- Sharpen: sharpest is H20=H20a (31/70 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L06.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=108  W=33/L=75  WR=30.6%
- Sharpen: sharpest is H60=H60e (41/75 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L07.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=103  W=33/L=70  WR=32.0%
- Sharpen: sharpest is H60=H60e (36/70 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L08.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=98  W=28/L=70  WR=28.6%
- Sharpen: sharpest is H60=H60e (41/70 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L09.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H60=H60e (36/65 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L10.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (26/55 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L11.  `H20=H20e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (26/55 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_open  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (26/55 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L13.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (26/55 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L14.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (26/55 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L15.  `H60=H60e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (41/52 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (41/52 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (36/47 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (36/47 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (36/47 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H20=H20a AND T1=T1c AND session_bucket=london`
- Raw: n=74  W=24/L=50  WR=32.4%
- Sharpen: sharpest is H60=H60a (20/50 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when HTF60 aligned WITH trade

### L21.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=74  W=24/L=50  WR=32.4%
- Sharpen: sharpest is H60=H60a (20/50 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=74  W=24/L=50  WR=32.4%
- Sharpen: sharpest is H60=H60a (20/50 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when HTF60 aligned WITH trade

### L23.  `T4=T4c AND BBP=BBP0 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is T1=T1c (43/43 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20d AND direction_exec=long AND session_bucket=london_open`
- Raw: n=69  W=21/L=48  WR=30.4%
- Sharpen: sharpest is RSI=RSI1 (31/48 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; session=london_open  •  ONLY when RSI 20-30 oversold

### L25.  `H20=H20d AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=69  W=21/L=48  WR=30.4%
- Sharpen: sharpest is RSI=RSI1 (31/48 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 20-30 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(40/35) | H60a(32/38) |
| T1 | T1a(52/44) | T1c(48/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/44) | long(48/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
