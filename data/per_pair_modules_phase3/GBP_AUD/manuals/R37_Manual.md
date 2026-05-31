# GBP_AUD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,911**  (W=2,350 / L=1,561)  -  WR: **60.1%**

## Session distribution

- asia: n=1192  W=723/L=469  WR=60.7%
- london_open: n=616  W=357/L=259  WR=58.0%
- ny_close: n=500  W=304/L=196  WR=60.8%
- ny_open: n=445  W=277/L=168  WR=62.2%
- london: n=422  W=264/L=158  WR=62.6%
- ny_mid: n=330  W=193/L=137  WR=58.5%
- asia_late: n=329  W=195/L=134  WR=59.3%
- off_hours: n=77  W=37/L=40  WR=48.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND ZS=ZS4 AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20d drops 5/17 losers (29%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W02.  `ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20d drops 5/17 losers (29%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W03.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20d drops 5/17 losers (29%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W04.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20d drops 5/17 losers (29%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W05.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20d drops 5/17 losers (29%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W06.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=122  W=108/L=14  WR=88.5%
- Refine: exclude H20=H20e drops 5/14 losers (36%)
- **Final: n=106  W=97/L=9  WR=91.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W07.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=london`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude H20=H20d drops 5/17 losers (29%)
- **Final: n=107  W=95/L=12  WR=88.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W08.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude H20=H20d drops 5/17 losers (29%)
- **Final: n=107  W=95/L=12  WR=88.8%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W09.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude H20=H20e drops 5/11 losers (45%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W10.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude H20=H20e drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W11.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude H20=H20e drops 7/13 losers (54%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W12.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude RSI=RSI5 drops 9/14 losers (64%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W13.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude T1=T1a drops 6/9 losers (67%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude RSI=RSI5 drops 9/12 losers (75%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W15.  `H20=H20a AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude RSI=RSI5 drops 9/12 losers (75%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W16.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude H20=H20e drops 8/11 losers (73%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF20 strongly against

### W17.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude RSI=RSI5 drops 7/9 losers (78%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W18.  `H60=H60a AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; zscore >+3 extreme  •  AVOID when session=ny_close

### W19.  `H60=H60a AND ZS=ZS6 AND direction_exec=short`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore >+3 extreme  •  AVOID when session=ny_close

### W20.  `BBP=BBP6 AND ZS=ZS6 AND direction_exec=short`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore >+3 extreme  •  AVOID when session=ny_close

### W21.  `H60=H60a AND BBP=BBP6 AND ZS=ZS6 AND direction_exec=short`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band; zscore >+3 extreme  •  AVOID when session=ny_close

### W22.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=london`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H20=H20d drops 5/11 losers (45%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W23.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W24.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W25.  `H20=H20a AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=273  W=107/L=166  WR=39.2%
- Sharpen: sharpest is BBP=BBP4 (79/166 of losers there)
- **Sharp: n=98  W=19/L=79  WR=19.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L02.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=252  W=90/L=162  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=252  W=90/L=162  WR=35.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong

### L03.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=252  W=90/L=162  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=252  W=90/L=162  WR=35.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong

### L04.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=252  W=90/L=162  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=252  W=90/L=162  WR=35.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong

### L05.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=252  W=90/L=162  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=252  W=90/L=162  WR=35.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong

### L06.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=252  W=90/L=162  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=252  W=90/L=162  WR=35.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong

### L07.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=252  W=90/L=162  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=252  W=90/L=162  WR=35.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong

### L08.  `H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=217  W=86/L=131  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (44/131 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L09.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=217  W=86/L=131  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (44/131 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L10.  `H60=H60a AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=217  W=86/L=131  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (44/131 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L11.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=190  W=72/L=118  WR=37.9%
- Sharpen: sharpest is session_bucket=london_open (45/118 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L12.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=189  W=72/L=117  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (44/117 of losers there)
- **Sharp: n=49  W=5/L=44  WR=10.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L13.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=189  W=72/L=117  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (44/117 of losers there)
- **Sharp: n=49  W=5/L=44  WR=10.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L14.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (52/111 of losers there)
- **Sharp: n=68  W=16/L=52  WR=23.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (52/111 of losers there)
- **Sharp: n=68  W=16/L=52  WR=23.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (52/111 of losers there)
- **Sharp: n=68  W=16/L=52  WR=23.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=170  W=64/L=106  WR=37.6%
- Sharpen: sharpest is BBP=BBP4 (65/106 of losers there)
- **Sharp: n=78  W=13/L=65  WR=16.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L18.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (56/96 of losers there)
- **Sharp: n=69  W=13/L=56  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L19.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (56/96 of losers there)
- **Sharp: n=69  W=13/L=56  WR=18.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L20.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=148  W=54/L=94  WR=36.5%
- Sharpen: sharpest is T4=T4c (61/94 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L21.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=148  W=57/L=91  WR=38.5%
- Sharpen: sharpest is H60=H60e (52/91 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L22.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=146  W=45/L=101  WR=30.8%
- Sharpen: sharpest is T4=T4c (52/101 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L23.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=146  W=45/L=101  WR=30.8%
- Sharpen: sharpest is T4=T4c (52/101 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L24.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=146  W=45/L=101  WR=30.8%
- Sharpen: sharpest is T4=T4c (52/101 of losers there)
- **Sharp: n=64  W=12/L=52  WR=18.8%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L25.  `T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=144  W=50/L=94  WR=34.7%
- Sharpen: sharpest is RSI=RSI4 (79/94 of losers there)
- **Sharp: n=98  W=19/L=79  WR=19.4%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
