# GBP_AUD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,366**  (W=2,048 / L=1,318)  -  WR: **60.8%**

## Session distribution

- asia: n=1230  W=767/L=463  WR=62.4%
- ny_mid: n=631  W=369/L=262  WR=58.5%
- ny_close: n=586  W=361/L=225  WR=61.6%
- ny_open: n=279  W=166/L=113  WR=59.5%
- london: n=214  W=127/L=87  WR=59.3%
- london_open: n=201  W=123/L=78  WR=61.2%
- asia_late: n=127  W=71/L=56  WR=55.9%
- off_hours: n=98  W=64/L=34  WR=65.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude H60=H60e drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W02.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H60=H60e drops 10/14 losers (71%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W03.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude session_bucket=ny_open drops 8/15 losers (53%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W04.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude session_bucket=ny_open drops 8/15 losers (53%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W05.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude session_bucket=ny_open drops 8/15 losers (53%)
- **Final: n=101  W=94/L=7  WR=93.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W06.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=102  W=96/L=6  WR=94.1%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W07.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=102  W=96/L=6  WR=94.1%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W08.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=90  W=86/L=4  WR=95.6%
- Refine: exclude session_bucket=ny_mid drops 3/4 losers (75%)
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W09.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=90  W=86/L=4  WR=95.6%
- Refine: exclude session_bucket=ny_mid drops 3/4 losers (75%)
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W10.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H60=H60e drops 11/13 losers (85%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W11.  `H20=H20e AND T4=T4a AND BBP=BBP2`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude session_bucket=asia drops 10/12 losers (83%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=asia

### W12.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude session_bucket=asia drops 10/12 losers (83%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=asia

### W13.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude session_bucket=asia drops 10/12 losers (83%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=asia

### W14.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude T1=T1a drops 5/7 losers (71%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W15.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude T1=T1a drops 5/7 losers (71%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W16.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude T1=T1a drops 5/7 losers (71%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W17.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/8 losers (25%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W18.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/7 losers (29%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W19.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/7 losers (29%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W20.  `H20=H20a AND T1=T1c AND BBP=BBP6`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 11/11 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=ny_close

### W21.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP6`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 11/11 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=ny_close

### W22.  `H20=H20a AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 11/11 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W23.  `H20=H20a AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 11/11 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=ny_close

### W24.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 10/12 losers (83%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=asia

### W25.  `H60=H60e AND T1=T1a AND BBP=BBP1`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude RSI=RSI4 drops 11/11 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=219  W=81/L=138  WR=37.0%
- Sharpen: sharpest is T4=T4c (61/138 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=219  W=81/L=138  WR=37.0%
- Sharpen: sharpest is T4=T4c (61/138 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L03.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=199  W=73/L=126  WR=36.7%
- Sharpen: sharpest is T4=T4c (49/126 of losers there)
- **Sharp: n=63  W=14/L=49  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L04.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=199  W=73/L=126  WR=36.7%
- Sharpen: sharpest is T4=T4c (49/126 of losers there)
- **Sharp: n=63  W=14/L=49  WR=22.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L05.  `H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=172  W=66/L=106  WR=38.4%
- Sharpen: sharpest is RSI=RSI4 (44/106 of losers there)
- **Sharp: n=61  W=17/L=44  WR=27.9%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L06.  `BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=172  W=66/L=106  WR=38.4%
- Sharpen: sharpest is RSI=RSI4 (44/106 of losers there)
- **Sharp: n=61  W=17/L=44  WR=27.9%**
- **Dir: LONG**  •  upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L07.  `H60=H60e AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=172  W=66/L=106  WR=38.4%
- Sharpen: sharpest is RSI=RSI4 (44/106 of losers there)
- **Sharp: n=61  W=17/L=44  WR=27.9%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L08.  `T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (43/105 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L09.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (43/105 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (43/105 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `H60=H60e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia

### L12.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia

### L13.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=asia

### L14.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia

### L15.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia

### L16.  `T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=57/L=89  WR=39.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia

### L17.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=57/L=89  WR=39.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=asia

### L18.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=57/L=89  WR=39.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia

### L19.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=57/L=89  WR=39.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia

### L20.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is session_bucket=asia_late (21/82 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=asia_late

### L21.  `H20=H20d AND H60=H60e AND RSI=RSI4`
- Raw: n=128  W=48/L=80  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=48/L=80  WR=37.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral

### L22.  `H20=H20d AND RSI=RSI4 AND direction_exec=long`
- Raw: n=128  W=48/L=80  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=48/L=80  WR=37.5%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 50-60 upper neutral

### L23.  `H20=H20d AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=128  W=48/L=80  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=48/L=80  WR=37.5%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral

### L24.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=45/L=78  WR=36.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=asia

### L25.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=45/L=78  WR=36.6%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(29/35) |
| H60 | H60a(55/47) | H60e(45/53) |
| T1 | T1c(55/46) | T1a(45/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/47) | long(45/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
