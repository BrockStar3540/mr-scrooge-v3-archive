# CHF_JPY — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,539**  (W=3,339 / L=2,200)  -  WR: **60.3%**

## Session distribution

- asia: n=1641  W=1003/L=638  WR=61.1%
- london_open: n=1288  W=764/L=524  WR=59.3%
- london: n=597  W=372/L=225  WR=62.3%
- ny_mid: n=542  W=327/L=215  WR=60.3%
- ny_open: n=536  W=334/L=202  WR=62.3%
- ny_close: n=358  W=205/L=153  WR=57.3%
- asia_late: n=294  W=160/L=134  WR=54.4%
- off_hours: n=283  W=174/L=109  WR=61.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=170  W=145/L=25  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 12/25 losers (48%)
- **Final: n=152  W=139/L=13  WR=91.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W02.  `T1=T1a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=139  W=123/L=16  WR=88.5%
- Refine: exclude session_bucket=london drops 8/16 losers (50%)
- **Final: n=124  W=116/L=8  WR=93.5%**
- **Dir: LONG**  •  1h trend WITH trade; deep below lower band  •  AVOID when session=london

### W03.  `H60=H60a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=134  W=119/L=15  WR=88.8%
- Refine: exclude session_bucket=london drops 8/15 losers (53%)
- **Final: n=119  W=112/L=7  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band  •  AVOID when session=london

### W04.  `T1=T1c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude T4=T4c drops 14/14 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london  •  AVOID when 4h trend AGAINST trade

### W05.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london`
- Raw: n=131  W=119/L=12  WR=90.8%
- Refine: exclude H20=H20e drops 8/12 losers (67%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=london  •  AVOID when HTF20 strongly against

### W06.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude BBP=BBP1 drops 14/16 losers (88%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W07.  `H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude session_bucket=london drops 8/15 losers (53%)
- **Final: n=115  W=108/L=7  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when session=london

### W08.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude session_bucket=london drops 8/15 losers (53%)
- **Final: n=115  W=108/L=7  WR=93.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when session=london

### W09.  `T4=T4a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude BBP=BBP1 drops 14/16 losers (88%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W10.  `H20=H20d AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=122  W=107/L=15  WR=87.7%
- Refine: exclude T4=T4a drops 13/15 losers (87%)
- **Final: n=82  W=80/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude BBP=BBP1 drops 14/16 losers (88%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W12.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude BBP=BBP1 drops 14/16 losers (88%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W13.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude BBP=BBP1 drops 14/16 losers (88%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W14.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude BBP=BBP1 drops 14/16 losers (88%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W15.  `T1=T1a AND BBP=BBP0 AND RSI=RSI4`
- Raw: n=115  W=106/L=9  WR=92.2%
- Refine: exclude ZS=ZS0 drops 6/9 losers (67%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when zscore <-3 extreme

### W16.  `BBP=BBP0 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=115  W=106/L=9  WR=92.2%
- Refine: exclude ZS=ZS0 drops 6/9 losers (67%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: LONG**  •  deep below lower band; RSI 50-60 upper neutral  •  AVOID when zscore <-3 extreme

### W17.  `T1=T1a AND BBP=BBP0 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=115  W=106/L=9  WR=92.2%
- Refine: exclude ZS=ZS0 drops 6/9 losers (67%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: LONG**  •  1h trend WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when zscore <-3 extreme

### W18.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude BBP=BBP1 drops 14/16 losers (88%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W19.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude T4=T4c drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=london  •  AVOID when 4h trend AGAINST trade

### W20.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude T4=T4c drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=london  •  AVOID when 4h trend AGAINST trade

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude H20=H20e drops 8/14 losers (57%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=london  •  AVOID when HTF20 strongly against

### W22.  `H60=H60a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude T4=T4c drops 8/14 losers (57%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W23.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude T4=T4c drops 8/14 losers (57%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W24.  `H60=H60a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude T4=T4c drops 8/14 losers (57%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60a AND BBP=BBP0 AND RSI=RSI4`
- Raw: n=106  W=98/L=8  WR=92.5%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 4/8 losers (50%)
- **Final: n=95  W=91/L=4  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when strategy=delta_tag_and_go_v2

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=235  W=86/L=149  WR=36.6%
- Sharpen: sharpest is T1=T1c (67/149 of losers there)
- **Sharp: n=79  W=12/L=67  WR=15.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L02.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=170  W=67/L=103  WR=39.4%
- Sharpen: sharpest is H20=H20e (50/103 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L03.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=166  W=50/L=116  WR=30.1%
- Sharpen: sharpest is T1=T1c (67/116 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L04.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=166  W=50/L=116  WR=30.1%
- Sharpen: sharpest is T1=T1c (67/116 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=166  W=58/L=108  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (21/108 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L06.  `H60=H60a AND T4=T4a AND BBP=BBP5`
- Raw: n=166  W=64/L=102  WR=38.6%
- Sharpen: sharpest is H20=H20e (25/102 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when HTF20 strongly against

### L07.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=166  W=64/L=102  WR=38.6%
- Sharpen: sharpest is H20=H20e (25/102 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L08.  `T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=162  W=60/L=102  WR=37.0%
- Sharpen: sharpest is H20=H20e (25/102 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band  •  ONLY when HTF20 strongly against

### L09.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=162  W=60/L=102  WR=37.0%
- Sharpen: sharpest is H20=H20e (25/102 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L10.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is H20=H20e (25/102 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when HTF20 strongly against

### L11.  `T1=T1c AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=150  W=56/L=94  WR=37.3%
- Sharpen: sharpest is H20=H20e (48/94 of losers there)
- **Sharp: n=52  W=4/L=48  WR=7.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -1 to +1 neutral; session=london_open  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: sharpest is T1=T1c (65/84 of losers there)
- **Sharp: n=86  W=21/L=65  WR=24.4%**
- **Dir: ?**  •  HTF60 strongly against; zscore -1 to +1 neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

### L13.  `H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=135  W=47/L=88  WR=34.8%
- Sharpen: sharpest is BBP=BBP0 (52/88 of losers there)
- **Sharp: n=63  W=11/L=52  WR=17.5%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L14.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=134  W=47/L=87  WR=35.1%
- Sharpen: sharpest is BBP=BBP5 (67/87 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L15.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is RSI=RSI5 (20/78 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is RSI=RSI5 (20/78 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L17.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is T1=T1c (69/79 of losers there)
- **Sharp: n=95  W=26/L=69  WR=27.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is BBP=BBP6 (50/78 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L19.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP4 (39/77 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when upper third

### L20.  `T1=T1c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=125  W=47/L=78  WR=37.6%
- Sharpen: sharpest is BBP=BBP0 (54/78 of losers there)
- **Sharp: n=65  W=11/L=54  WR=16.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L21.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=123  W=41/L=82  WR=33.3%
- Sharpen: sharpest is BBP=BBP0 (46/82 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L22.  `T1=T1c AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=122  W=42/L=80  WR=34.4%
- Sharpen: sharpest is H20=H20e (42/80 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=london_open  •  ONLY when HTF20 strongly against

### L23.  `H60=H60e AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP0 (42/72 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L24.  `H60=H60e AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is BBP=BBP0 (42/72 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L25.  `H20=H20b AND H60=H60a AND ZS=ZS4`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is T4=T4a (54/71 of losers there)
- **Sharp: n=73  W=19/L=54  WR=26.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

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
