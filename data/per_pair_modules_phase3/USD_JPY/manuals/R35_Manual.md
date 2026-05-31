# USD_JPY — R35 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,137**  (W=2,591 / L=1,546)  -  WR: **62.6%**

## Session distribution

- asia: n=1371  W=853/L=518  WR=62.2%
- london_open: n=924  W=588/L=336  WR=63.6%
- ny_open: n=459  W=294/L=165  WR=64.1%
- london: n=431  W=266/L=165  WR=61.7%
- asia_late: n=387  W=245/L=142  WR=63.3%
- ny_close: n=284  W=173/L=111  WR=60.9%
- ny_mid: n=175  W=111/L=64  WR=63.4%
- off_hours: n=106  W=61/L=45  WR=57.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND session_bucket=london_open`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude ZS=ZS4 drops 9/16 losers (56%)
- **Final: n=77  W=70/L=7  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W02.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude H60=H60e drops 6/16 losers (38%)
- **Final: n=96  W=86/L=10  WR=89.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when HTF60 strongly against

### W03.  `T1=T1a AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude T4=T4c drops 6/16 losers (38%)
- **Final: n=94  W=84/L=10  WR=89.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W04.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude T4=T4c drops 5/15 losers (33%)
- **Final: n=94  W=84/L=10  WR=89.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W05.  `BBP=BBP0 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 5/15 losers (33%)
- **Final: n=94  W=84/L=10  WR=89.4%**
- **Dir: LONG**  •  deep below lower band; RSI 50-60 upper neutral  •  AVOID when strategy=echo_box_fade_v2

### W06.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude session_bucket=london_open drops 8/15 losers (53%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W07.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T4=T4c drops 4/12 losers (33%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W08.  `H60=H60a AND BBP=BBP0 AND RSI=RSI4`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 5/15 losers (33%)
- **Final: n=88  W=78/L=10  WR=88.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when strategy=echo_box_fade_v2

### W09.  `H60=H60a AND BBP=BBP0 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 5/15 losers (33%)
- **Final: n=88  W=78/L=10  WR=88.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when strategy=echo_box_fade_v2

### W10.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20b drops 4/14 losers (29%)
- **Final: n=89  W=79/L=10  WR=88.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W11.  `T1=T1a AND BBP=BBP0 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude H20=H20c drops 6/12 losers (50%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  1h trend WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W12.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W13.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND RSI=RSI4`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude H20=H20c drops 6/12 losers (50%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W14.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=asia

### W15.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=asia

### W16.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=asia

### W17.  `T4=T4a AND BBP=BBP6 AND session_bucket=ny_open`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; session=ny_open  •  AVOID when HTF20 mildly against

### W18.  `H60=H60a AND T4=T4a AND BBP=BBP3 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI5 drops 6/11 losers (55%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; middle of band; session=asia  •  AVOID when RSI 60-70 strong

### W19.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude strategy_id=CP2_squeeze_momentum_long drops 2/10 losers (20%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when strategy=CP2_squeeze_momentum_long

### W20.  `BBP=BBP4 AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude strategy_id=CP2_squeeze_momentum_long drops 2/10 losers (20%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when strategy=CP2_squeeze_momentum_long

### W21.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude strategy_id=CP2_squeeze_momentum_long drops 2/10 losers (20%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when strategy=CP2_squeeze_momentum_long

### W22.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20b drops 3/11 losers (27%)
- **Final: n=73  W=65/L=8  WR=89.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W23.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP4 drops 7/11 losers (64%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when upper third

### W24.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS4 drops 8/11 losers (73%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W25.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude ZS=ZS4 drops 8/11 losers (73%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +1 to +2 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=191  W=76/L=115  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=191  W=76/L=115  WR=39.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=181  W=71/L=110  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=181  W=71/L=110  WR=39.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L03.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=145  W=56/L=89  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=145  W=56/L=89  WR=38.6%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L04.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=136  W=53/L=83  WR=39.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral

### L05.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is ZS=ZS2 (61/82 of losers there)
- **Sharp: n=91  W=30/L=61  WR=33.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is ZS=ZS2 (57/76 of losers there)
- **Sharp: n=83  W=26/L=57  WR=31.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L07.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is BBP=BBP5 (21/76 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when just touched upper band

### L08.  `T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is session_bucket=asia_late (11/71 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=asia_late

### L09.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is session_bucket=asia_late (11/71 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=asia_late

### L10.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=110  W=43/L=67  WR=39.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral

### L11.  `H20=H20a AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=39/L=66  WR=37.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; session=asia

### L12.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=39/L=66  WR=37.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia

### L13.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is H20=H20c (19/64 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when HTF20 neutral

### L14.  `H60=H60e AND T1=T1c AND ZS=ZS2`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=asia_late (11/67 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=asia_late

### L15.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=asia_late (11/67 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=asia_late

### L16.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=asia_late (11/67 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=asia_late

### L17.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H20=H20a (43/64 of losers there)
- **Sharp: n=58  W=15/L=43  WR=25.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L18.  `T1=T1c AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=101  W=40/L=61  WR=39.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold

### L19.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=101  W=40/L=61  WR=39.6%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold

### L20.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=96  W=29/L=67  WR=30.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=96  W=29/L=67  WR=30.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open

### L21.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (41/65 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=37/L=56  WR=39.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 50-60 upper neutral

### L23.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=91  W=30/L=61  WR=33.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=30/L=61  WR=33.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L24.  `H20=H20c AND H60=H60a AND ZS=ZS5`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is session_bucket=london_open (21/56 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L25.  `H20=H20c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is session_bucket=london_open (21/56 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/48) | T1c(47/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
