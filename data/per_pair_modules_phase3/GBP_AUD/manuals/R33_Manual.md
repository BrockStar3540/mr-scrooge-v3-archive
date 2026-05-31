# GBP_AUD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,859**  (W=2,336 / L=1,523)  -  WR: **60.5%**

## Session distribution

- asia: n=1587  W=983/L=604  WR=61.9%
- ny_close: n=827  W=491/L=336  WR=59.4%
- london_open: n=307  W=177/L=130  WR=57.7%
- london: n=294  W=171/L=123  WR=58.2%
- ny_open: n=275  W=179/L=96  WR=65.1%
- off_hours: n=267  W=144/L=123  WR=53.9%
- asia_late: n=197  W=120/L=77  WR=60.9%
- ny_mid: n=105  W=71/L=34  WR=67.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude session_bucket=asia drops 11/16 losers (69%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W02.  `H60=H60e AND BBP=BBP4 AND session_bucket=london`
- Raw: n=117  W=111/L=6  WR=94.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W03.  `T1=T1a AND BBP=BBP4 AND session_bucket=london`
- Raw: n=117  W=111/L=6  WR=94.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W04.  `BBP=BBP4 AND direction_exec=long AND session_bucket=london`
- Raw: n=117  W=111/L=6  WR=94.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  upper third; session=london  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=london`
- Raw: n=117  W=111/L=6  WR=94.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W06.  `H60=H60e AND BBP=BBP4 AND direction_exec=long AND session_bucket=london`
- Raw: n=117  W=111/L=6  WR=94.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W07.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london`
- Raw: n=117  W=111/L=6  WR=94.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W08.  `H60=H60e AND T4=T4c AND ZS=ZS3`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W09.  `T4=T4c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W10.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W11.  `H60=H60e AND T4=T4c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W12.  `T1=T1a AND T4=T4c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W13.  `H60=H60e AND ZS=ZS4 AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W14.  `T1=T1a AND ZS=ZS4 AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W15.  `ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W16.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W17.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W18.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W19.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W20.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W21.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=london`
- Raw: n=112  W=106/L=6  WR=94.6%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W22.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=asia drops 11/15 losers (73%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W23.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS3`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude session_bucket=asia drops 11/12 losers (92%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W24.  `H20=H20e AND T4=T4c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude session_bucket=asia drops 11/12 losers (92%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W25.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london`
- Raw: n=92  W=86/L=6  WR=93.5%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=london  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=351  W=140/L=211  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (132/211 of losers there)
- **Sharp: n=197  W=65/L=132  WR=33.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L02.  `T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=351  W=140/L=211  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (132/211 of losers there)
- **Sharp: n=197  W=65/L=132  WR=33.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L03.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=351  W=140/L=211  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (132/211 of losers there)
- **Sharp: n=197  W=65/L=132  WR=33.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L04.  `T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=275  W=101/L=174  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (30/174 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=275  W=101/L=174  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (30/174 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=275  W=101/L=174  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (30/174 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=220  W=71/L=149  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (29/149 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=220  W=71/L=149  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (29/149 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=220  W=71/L=149  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (29/149 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=218  W=82/L=136  WR=37.6%
- Sharpen: sharpest is H60=H60e (132/136 of losers there)
- **Sharp: n=197  W=65/L=132  WR=33.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L11.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=218  W=85/L=133  WR=39.0%
- Sharpen: sharpest is H60=H60e (131/133 of losers there)
- **Sharp: n=195  W=64/L=131  WR=32.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L12.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=197  W=65/L=132  WR=33.0%
- Sharpen: sharpest is ZS=ZS5 (26/132 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=197  W=65/L=132  WR=33.0%
- Sharpen: sharpest is ZS=ZS5 (26/132 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=195  W=64/L=131  WR=32.8%
- Sharpen: sharpest is ZS=ZS5 (29/131 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=195  W=64/L=131  WR=32.8%
- Sharpen: sharpest is ZS=ZS5 (29/131 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=172  W=58/L=114  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (26/114 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H60=H60e AND T1=T1a AND BBP=BBP6`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (42/84 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when session=asia

### L18.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (42/84 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when session=asia

### L19.  `H60=H60e AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (42/84 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band  •  ONLY when session=asia

### L20.  `H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=136  W=38/L=98  WR=27.9%
- Sharpen: sharpest is BBP=BBP4 (78/98 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when upper third

### L21.  `H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=136  W=38/L=98  WR=27.9%
- Sharpen: sharpest is BBP=BBP4 (78/98 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london  •  ONLY when upper third

### L22.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=136  W=38/L=98  WR=27.9%
- Sharpen: sharpest is BBP=BBP4 (78/98 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  ONLY when upper third

### L23.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=136  W=38/L=98  WR=27.9%
- Sharpen: sharpest is BBP=BBP4 (78/98 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when upper third

### L24.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=134  W=49/L=85  WR=36.6%
- Sharpen: sharpest is ZS=ZS4 (28/85 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L25.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is RSI=RSI4 (33/78 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

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
