# USD_CHF — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,659**  (W=1,054 / L=605)  -  WR: **63.5%**

## Session distribution

- asia: n=456  W=298/L=158  WR=65.4%
- ny_mid: n=367  W=225/L=142  WR=61.3%
- ny_close: n=287  W=186/L=101  WR=64.8%
- ny_open: n=182  W=115/L=67  WR=63.2%
- london_open: n=160  W=100/L=60  WR=62.5%
- off_hours: n=84  W=52/L=32  WR=61.9%
- london: n=80  W=55/L=25  WR=68.8%
- asia_late: n=43  W=23/L=20  WR=53.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=139  W=130/L=9  WR=93.5%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when HTF60 strongly against

### W02.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=112  W=108/L=4  WR=96.4%
- Refine: exclude RSI=RSI0 drops 3/4 losers (75%)
- **Final: n=75  W=74/L=1  WR=98.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W03.  `H20=H20e AND H60=H60a AND RSI=RSI1`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 6/15 losers (40%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_open

### W04.  `H20=H20e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude H60=H60e drops 10/11 losers (91%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=asia  •  AVOID when HTF60 strongly against

### W05.  `H20=H20e AND H60=H60a AND session_bucket=asia`
- Raw: n=101  W=98/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W06.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W07.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  AVOID when RSI<20 extreme oversold

### W08.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W09.  `H20=H20e AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W10.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W11.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W12.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W13.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude RSI=RSI0 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W14.  `H20=H20e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude H60=H60e drops 7/8 losers (88%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W15.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude H60=H60e drops 7/8 losers (88%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W16.  `H20=H20a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W17.  `H60=H60a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W18.  `T1=T1a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W19.  `T4=T4a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W20.  `RSI=RSI0 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: SHORT**  •  RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W21.  `H20=H20a AND H60=H60a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W22.  `H20=H20a AND T1=T1a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W23.  `H20=H20a AND T4=T4a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W24.  `H20=H20a AND RSI=RSI0 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

### W25.  `H60=H60a AND T1=T1a AND RSI=RSI0 AND session_bucket=ny_close`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude ZS=ZS0 drops 5/11 losers (45%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold; session=ny_close  •  AVOID when zscore <-3 extreme

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L02.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L03.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L04.  `BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: LONG**  •  lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L05.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L06.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L07.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L09.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L10.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_close (29/61 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_close

### L11.  `H20=H20a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=91  W=17/L=74  WR=18.7%
- Sharpen: sharpest is H60=H60e (38/74 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF60 strongly against

### L12.  `H60=H60e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L13.  `T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L14.  `T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L15.  `RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L17.  `H60=H60e AND T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L18.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L19.  `H60=H60e AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L20.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L21.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L22.  `T1=T1c AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L23.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L24.  `T4=T4c AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L25.  `BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_close (23/53 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(53/47) | H20a(46/53) |
| H60 | H60a(46/40) | H60e(42/48) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
