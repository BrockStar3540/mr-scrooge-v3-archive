# GBP_CHF — R30 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,508**  (W=1,000 / L=508)  -  WR: **66.3%**

## Session distribution

- asia: n=899  W=604/L=295  WR=67.2%
- ny_close: n=321  W=207/L=114  WR=64.5%
- asia_late: n=143  W=96/L=47  WR=67.1%
- off_hours: n=86  W=57/L=29  WR=66.3%
- london_open: n=32  W=19/L=13  WR=59.4%
- ny_open: n=13  W=9/L=4  WR=69.2%
- london: n=9  W=6/L=3  WR=66.7%
- ny_mid: n=5  W=2/L=3  WR=40.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=162  W=140/L=22  WR=86.4%
- Refine: exclude H20=H20a drops 11/22 losers (50%)
- **Final: n=134  W=123/L=11  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=162  W=140/L=22  WR=86.4%
- Refine: exclude H20=H20a drops 11/22 losers (50%)
- **Final: n=134  W=123/L=11  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF20 aligned WITH trade

### W03.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 6/18 losers (33%)
- **Final: n=112  W=100/L=12  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  AVOID when strategy=RG1_range_bound_scalp_long

### W04.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude RSI=RSI3 drops 17/19 losers (89%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude T4=T4a drops 8/17 losers (47%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude T4=T4a drops 8/17 losers (47%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W07.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude T4=T4a drops 8/17 losers (47%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W08.  `H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=118  W=106/L=12  WR=89.8%
- Refine: exclude H20=H20a drops 6/12 losers (50%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=99  W=90/L=9  WR=90.9%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=ny_close

### W10.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=99  W=90/L=9  WR=90.9%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=ny_close

### W11.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 5/13 losers (38%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak; session=asia  •  AVOID when strategy=RG1_range_bound_scalp_long

### W12.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude ZS=ZS2 drops 11/11 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W13.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 4/13 losers (31%)
- **Final: n=77  W=68/L=9  WR=88.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when strategy=RG1_range_bound_scalp_long

### W14.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI2`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude ZS=ZS4 drops 3/12 losers (25%)
- **Final: n=79  W=70/L=9  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude ZS=ZS4 drops 3/12 losers (25%)
- **Final: n=79  W=70/L=9  WR=88.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when zscore +1 to +2 overbought

### W16.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude ZS=ZS2 drops 11/11 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W17.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude H20=H20a drops 6/8 losers (75%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20d drops 7/12 losers (58%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 mildly against

### W19.  `T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 6/12 losers (50%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W20.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 6/12 losers (50%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W21.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 6/12 losers (50%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W22.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude H20=H20a drops 6/8 losers (75%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W23.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude ZS=ZS4 drops 3/9 losers (33%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore +1 to +2 overbought

### W24.  `H20=H20c AND T4=T4c AND direction_exec=long`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude BBP=BBP3 drops 3/5 losers (60%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade  •  AVOID when middle of band

### W25.  `H20=H20a AND H60=H60d AND direction_exec=long`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude T4=T4a drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is H20=H20d (11/71 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 mildly against

### L02.  `H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is H20=H20a (14/59 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20e AND H60=H60e AND RSI=RSI2`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is BBP=BBP0 (16/56 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  ONLY when deep below lower band

### L04.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is BBP=BBP0 (11/46 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L05.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is BBP=BBP0 (11/46 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L06.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=69  W=22/L=47  WR=31.9%
- Sharpen: sharpest is ZS=ZS1 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=69  W=22/L=47  WR=31.9%
- Sharpen: sharpest is ZS=ZS1 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=68  W=26/L=42  WR=38.2%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 30-40 weak

### L09.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is BBP=BBP0 (13/42 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when deep below lower band

### L10.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is BBP=BBP0 (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when deep below lower band

### L11.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is ZS=ZS3 (13/37 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L12.  `H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is H20=H20e (12/40 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L13.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is H20=H20e (12/40 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  ONLY when HTF20 strongly against

### L14.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is H20=H20e (12/40 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L15.  `H60=H60e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=56  W=17/L=39  WR=30.4%
- Sharpen: sharpest is H20=H20d (7/39 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 mildly against

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (13/35 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L17.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (13/33 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when deep below lower band

### L18.  `H60=H60e AND T1=T1a AND ZS=ZS3`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (20/31 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when session=asia

### L19.  `H20=H20c AND H60=H60a AND RSI=RSI3`
- Raw: n=50  W=14/L=36  WR=28.0%
- Sharpen: sharpest is ZS=ZS1 (18/36 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H60=H60e AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is T1=T1a (20/32 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore -1 to +1 neutral; session=asia  •  ONLY when 1h trend WITH trade

### L21.  `H60=H60e AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (26/31 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; session=asia  •  ONLY when RSI 30-40 weak

### L22.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is H20=H20c (15/29 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 neutral

### L23.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=46  W=12/L=34  WR=26.1%
- Sharpen: sharpest is BBP=BBP1 (11/34 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  ONLY when just touched lower band

### L24.  `H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=46  W=14/L=32  WR=30.4%
- Sharpen: sharpest is BBP=BBP4 (10/32 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when upper third

### L25.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=46  W=14/L=32  WR=30.4%
- Sharpen: sharpest is BBP=BBP1 (11/32 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when just touched lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(34/39) |
| H60 | H60a(45/31) | H60e(29/47) |
| T1 | — | — |
| T4 | T4c(55/47) | T4a(45/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/50) | short(45/50) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
