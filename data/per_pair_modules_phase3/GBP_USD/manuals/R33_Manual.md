# GBP_USD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,032**  (W=1,753 / L=1,279)  -  WR: **57.8%**

## Session distribution

- ny_mid: n=1372  W=817/L=555  WR=59.5%
- ny_open: n=621  W=320/L=301  WR=51.5%
- london_open: n=376  W=220/L=156  WR=58.5%
- ny_close: n=303  W=182/L=121  WR=60.1%
- london: n=214  W=132/L=82  WR=61.7%
- asia: n=70  W=42/L=28  WR=60.0%
- asia_late: n=40  W=21/L=19  WR=52.5%
- off_hours: n=36  W=19/L=17  WR=52.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude RSI=RSI3 drops 19/19 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W02.  `T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude T4=T4c drops 13/13 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

### W03.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude RSI=RSI4 drops 11/11 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W04.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 aligned WITH trade

### W05.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=86  W=77/L=9  WR=89.5%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND H60=H60d AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude BBP=BBP4 drops 3/9 losers (33%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; session=ny_mid  •  AVOID when upper third

### W07.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60d drops 9/9 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when HTF60 mildly against

### W08.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60d drops 9/9 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF60 mildly against

### W09.  `H20=H20a AND T4=T4a AND RSI=RSI2`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W10.  `H60=H60b AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W11.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude T1=T1c drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W12.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude H20=H20e drops 2/4 losers (50%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W14.  `H60=H60a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude H20=H20d drops 4/8 losers (50%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 mildly against

### W15.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude H20=H20d drops 4/8 losers (50%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 mildly against

### W16.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak

### W17.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak

### W18.  `H20=H20a AND H60=H60a AND RSI=RSI2`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W19.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W21.  `T4=T4a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 6/10 losers (60%)
- **Final: n=41  W=37/L=4  WR=90.2%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W22.  `H60=H60d AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP2 drops 4/10 losers (40%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: ?**  •  HTF60 mildly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when lower third

### W23.  `H60=H60d AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP2 drops 4/10 losers (40%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when lower third

### W24.  `H60=H60d AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP2 drops 4/10 losers (40%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when lower third

### W25.  `H20=H20a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=ny_open  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=236  W=83/L=153  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (43/153 of losers there)
- **Sharp: n=43  W=0/L=43  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L02.  `T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=197  W=78/L=119  WR=39.6%
- Sharpen: sharpest is H20=H20e (53/119 of losers there)
- **Sharp: n=70  W=17/L=53  WR=24.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=180  W=67/L=113  WR=37.2%
- Sharpen: sharpest is BBP=BBP6 (24/113 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L04.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=177  W=68/L=109  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (28/109 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  ONLY when session=london_open

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=173  W=57/L=116  WR=32.9%
- Sharpen: sharpest is BBP=BBP2 (44/116 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L06.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=172  W=68/L=104  WR=39.5%
- Sharpen: sharpest is ZS=ZS2 (40/104 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L07.  `H60=H60b AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=161  W=59/L=102  WR=36.6%
- Sharpen: sharpest is BBP=BBP4 (39/102 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF60 slightly aligned; session=ny_mid  •  ONLY when upper third

### L08.  `H20=H20e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=152  W=43/L=109  WR=28.3%
- Sharpen: sharpest is H60=H60e (75/109 of losers there)
- **Sharp: n=87  W=12/L=75  WR=13.8%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_open  •  ONLY when HTF60 strongly against

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=148  W=54/L=94  WR=36.5%
- Sharpen: sharpest is BBP=BBP2 (39/94 of losers there)
- **Sharp: n=50  W=11/L=39  WR=22.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L10.  `H60=H60b AND BBP=BBP4 AND direction_exec=long`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_mid (39/85 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF60 slightly aligned; upper third  •  ONLY when session=ny_mid

### L11.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is H20=H20d (40/84 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF20 mildly against

### L12.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: sharpest is BBP=BBP2 (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L13.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=134  W=38/L=96  WR=28.4%
- Sharpen: sharpest is direction_exec=long (75/96 of losers there)
- **Sharp: n=87  W=12/L=75  WR=13.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when long

### L14.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=133  W=35/L=98  WR=26.3%
- Sharpen: sharpest is RSI=RSI2 (36/98 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L15.  `H20=H20e AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=131  W=52/L=79  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (22/79 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L16.  `BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: sharpest is H60=H60a (17/82 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L17.  `BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: sharpest is H60=H60a (17/82 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is direction_exec=long (69/77 of losers there)
- **Sharp: n=94  W=25/L=69  WR=26.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when long

### L19.  `H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is T1=T1c (44/84 of losers there)
- **Sharp: n=47  W=3/L=44  WR=6.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when 1h trend AGAINST trade

### L20.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: sharpest is H20=H20d (40/81 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF20 mildly against

### L21.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=124  W=33/L=91  WR=26.6%
- Sharpen: sharpest is direction_exec=long (62/91 of losers there)
- **Sharp: n=66  W=4/L=62  WR=6.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when long

### L22.  `H20=H20e AND H60=H60b AND session_bucket=ny_mid`
- Raw: n=124  W=42/L=82  WR=33.9%
- Sharpen: sharpest is BBP=BBP4 (31/82 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; session=ny_mid  •  ONLY when upper third

### L23.  `H20=H20e AND H60=H60b AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=124  W=42/L=82  WR=33.9%
- Sharpen: sharpest is BBP=BBP4 (31/82 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; session=ny_mid  •  ONLY when upper third

### L24.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=123  W=41/L=82  WR=33.3%
- Sharpen: sharpest is H20=H20c (17/82 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 neutral

### L25.  `H20=H20e AND H60=H60b AND BBP=BBP4`
- Raw: n=123  W=46/L=77  WR=37.4%
- Sharpen: sharpest is session_bucket=ny_mid (31/77 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; upper third  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/39) | H20e(38/47) |
| H60 | H60a(37/28) | H60e(28/36) |
| T1 | T1a(56/45) | T1c(44/55) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | ny_open(18/24) |

*Read: `bucket(winner%/loser%)`.*
