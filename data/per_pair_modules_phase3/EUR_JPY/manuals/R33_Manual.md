# EUR_JPY — R33 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,932**  (W=1,854 / L=1,078)  -  WR: **63.2%**

## Session distribution

- asia: n=1132  W=733/L=399  WR=64.8%
- ny_close: n=493  W=315/L=178  WR=63.9%
- london: n=290  W=176/L=114  WR=60.7%
- ny_open: n=272  W=167/L=105  WR=61.4%
- asia_late: n=203  W=124/L=79  WR=61.1%
- london_open: n=199  W=121/L=78  WR=60.8%
- ny_mid: n=185  W=117/L=68  WR=63.2%
- off_hours: n=158  W=101/L=57  WR=63.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=162  W=141/L=21  WR=87.0%
- Refine: exclude session_bucket=london_open drops 7/21 losers (33%)
- **Final: n=155  W=141/L=14  WR=91.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W02.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude session_bucket=london_open drops 7/20 losers (35%)
- **Final: n=137  W=124/L=13  WR=90.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W03.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=london_open drops 7/18 losers (39%)
- **Final: n=121  W=110/L=11  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W04.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude T4=T4c drops 9/13 losers (69%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  AVOID when 4h trend AGAINST trade

### W05.  `T1=T1c AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude H60=H60a drops 14/16 losers (88%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; session=asia  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20e AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude H60=H60e drops 8/13 losers (62%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF60 strongly against

### W07.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude ZS=ZS3 drops 4/15 losers (27%)
- **Final: n=91  W=80/L=11  WR=87.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude BBP=BBP4 drops 5/13 losers (38%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W09.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude BBP=BBP4 drops 5/13 losers (38%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W10.  `H20=H20e AND T1=T1a AND session_bucket=london`
- Raw: n=98  W=90/L=8  WR=91.8%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude RSI=RSI2 drops 7/12 losers (58%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: LONG**  •  HTF20 strongly against; deep below lower band  •  AVOID when RSI 30-40 weak

### W12.  `H20=H20e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude RSI=RSI2 drops 7/12 losers (58%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W13.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude RSI=RSI2 drops 7/12 losers (58%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W14.  `H60=H60c AND T4=T4a AND session_bucket=asia`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W15.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=89  W=83/L=6  WR=93.3%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20e AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude RSI=RSI2 drops 7/12 losers (58%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W17.  `T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=88  W=80/L=8  WR=90.9%
- Refine: exclude H20=H20c drops 7/8 losers (88%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W18.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=88  W=80/L=8  WR=90.9%
- Refine: exclude H20=H20c drops 7/8 losers (88%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W19.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=88  W=80/L=8  WR=90.9%
- Refine: exclude H20=H20c drops 7/8 losers (88%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when HTF20 neutral

### W20.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=87  W=81/L=6  WR=93.1%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W21.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=87  W=81/L=6  WR=93.1%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20e AND H60=H60e AND session_bucket=london`
- Raw: n=85  W=79/L=6  WR=92.9%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=85  W=79/L=6  WR=92.9%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20e AND T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4a drops 7/12 losers (58%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=83  W=77/L=6  WR=92.8%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (25/76 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L02.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (25/76 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when upper third

### L03.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=117  W=38/L=79  WR=32.5%
- Sharpen: sharpest is session_bucket=london (33/79 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london

### L04.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is H20=H20a (34/71 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L05.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is H20=H20a (44/69 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L06.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is RSI=RSI4 (30/63 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L07.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=96  W=37/L=59  WR=38.5%
- Sharpen: sharpest is H20=H20a (29/59 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L08.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=93  W=30/L=63  WR=32.3%
- Sharpen: sharpest is RSI=RSI4 (26/63 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L09.  `T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=92  W=27/L=65  WR=29.3%
- Sharpen: sharpest is RSI=RSI2 (54/65 of losers there)
- **Sharp: n=68  W=14/L=54  WR=20.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L10.  `H20=H20a AND T1=T1c AND session_bucket=london`
- Raw: n=85  W=24/L=61  WR=28.2%
- Sharpen: sharpest is RSI=RSI2 (45/61 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L11.  `T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=83  W=29/L=54  WR=34.9%
- Sharpen: sharpest is session_bucket=london_open (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when session=london_open

### L12.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=82  W=23/L=59  WR=28.0%
- Sharpen: sharpest is H20=H20a (34/59 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L13.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is direction_exec=long (12/58 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when long

### L14.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is BBP=BBP2 (29/50 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when lower third

### L15.  `H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=76  W=20/L=56  WR=26.3%
- Sharpen: sharpest is RSI=RSI2 (45/56 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=76  W=20/L=56  WR=26.3%
- Sharpen: sharpest is RSI=RSI4 (26/56 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L17.  `H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=74  W=19/L=55  WR=25.7%
- Sharpen: sharpest is RSI=RSI2 (45/55 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L18.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=74  W=19/L=55  WR=25.7%
- Sharpen: sharpest is RSI=RSI2 (45/55 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L19.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=73  W=20/L=53  WR=27.4%
- Sharpen: sharpest is RSI=RSI2 (45/53 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=73  W=20/L=53  WR=27.4%
- Sharpen: sharpest is RSI=RSI2 (45/53 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when RSI 30-40 weak

### L21.  `T4=T4c AND RSI=RSI2 AND session_bucket=london`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H20=H20a (41/48 of losers there)
- **Sharp: n=45  W=4/L=41  WR=8.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london  •  ONLY when HTF20 aligned WITH trade

### L22.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is RSI=RSI2 (19/48 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is RSI=RSI3 (34/46 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L24.  `H20=H20a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is RSI=RSI3 (34/46 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L25.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is RSI=RSI2 (19/47 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | T4c(53/46) | T4a(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
