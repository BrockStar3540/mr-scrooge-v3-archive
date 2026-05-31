# GBP_CAD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,847**  (W=3,730 / L=2,117)  -  WR: **63.8%**

## Session distribution

- asia: n=2329  W=1497/L=832  WR=64.3%
- ny_close: n=1345  W=864/L=481  WR=64.2%
- london: n=480  W=304/L=176  WR=63.3%
- off_hours: n=479  W=285/L=194  WR=59.5%
- london_open: n=447  W=294/L=153  WR=65.8%
- asia_late: n=339  W=221/L=118  WR=65.2%
- ny_open: n=309  W=179/L=130  WR=57.9%
- ny_mid: n=119  W=86/L=33  WR=72.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=197  W=171/L=26  WR=86.8%
- Refine: exclude session_bucket=asia drops 17/26 losers (65%)
- **Final: n=135  W=126/L=9  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

### W02.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=191  W=173/L=18  WR=90.6%
- Refine: exclude ZS=ZS3 drops 8/18 losers (44%)
- **Final: n=156  W=146/L=10  WR=93.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=187  W=162/L=25  WR=86.6%
- Refine: exclude session_bucket=asia drops 17/25 losers (68%)
- **Final: n=125  W=117/L=8  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W04.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=182  W=155/L=27  WR=85.2%
- Refine: exclude session_bucket=asia drops 19/27 losers (70%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when session=asia

### W05.  `H20=H20a AND H60=H60c AND RSI=RSI3`
- Raw: n=171  W=146/L=25  WR=85.4%
- Refine: exclude T4=T4c drops 19/25 losers (76%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=170  W=145/L=25  WR=85.3%
- Refine: exclude session_bucket=asia drops 18/25 losers (72%)
- **Final: n=104  W=97/L=7  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W07.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=150  W=131/L=19  WR=87.3%
- Refine: exclude H60=H60a drops 16/19 losers (84%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W08.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 8/20 losers (40%)
- **Final: n=131  W=119/L=12  WR=90.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W09.  `H20=H20c AND H60=H60e AND session_bucket=ny_close`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude BBP=BBP4 drops 17/18 losers (94%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=ny_close  •  AVOID when upper third

### W10.  `H20=H20c AND H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude BBP=BBP4 drops 17/18 losers (94%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; session=ny_close  •  AVOID when upper third

### W11.  `H20=H20c AND T1=T1a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude H60=H60a drops 9/17 losers (53%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W12.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude H60=H60e drops 12/19 losers (63%)
- **Final: n=100  W=93/L=7  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W13.  `H20=H20c AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=126  W=115/L=11  WR=91.3%
- Refine: exclude BBP=BBP4 drops 9/11 losers (82%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade; session=ny_close  •  AVOID when upper third

### W14.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=123  W=108/L=15  WR=87.8%
- Refine: exclude ZS=ZS4 drops 8/15 losers (53%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W15.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude H60=H60c drops 6/17 losers (35%)
- **Final: n=114  W=103/L=11  WR=90.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 neutral

### W16.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude H20=H20c drops 9/17 losers (53%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=ny_close  •  AVOID when HTF20 neutral

### W17.  `H20=H20c AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=116  W=103/L=13  WR=88.8%
- Refine: exclude BBP=BBP4 drops 9/13 losers (69%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W18.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude BBP=BBP4 drops 6/11 losers (55%)
- **Final: n=109  W=104/L=5  WR=95.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W19.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude H60=H60c drops 9/17 losers (53%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 neutral

### W20.  `H20=H20d AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP4 drops 9/15 losers (60%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W21.  `H20=H20d AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP4 drops 9/15 losers (60%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W22.  `H20=H20c AND BBP=BBP5 AND direction_exec=long`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude T1=T1a drops 15/15 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; just touched upper band  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude RSI=RSI3 drops 10/15 losers (67%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W24.  `H20=H20c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude T1=T1a drops 15/15 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W25.  `H60=H60b AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude ZS=ZS3 drops 9/15 losers (60%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=280  W=111/L=169  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (109/169 of losers there)
- **Sharp: n=150  W=41/L=109  WR=27.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L02.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=163  W=57/L=106  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_close (41/106 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L03.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=152  W=54/L=98  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_close (39/98 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L04.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=150  W=41/L=109  WR=27.3%
- Sharpen: sharpest is H20=H20a (31/109 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L05.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=146  W=54/L=92  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (38/92 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when session=ny_close

### L06.  `H20=H20c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=144  W=57/L=87  WR=39.6%
- Sharpen: sharpest is direction_exec=short (68/87 of losers there)
- **Sharp: n=102  W=34/L=68  WR=33.3%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; session=ny_close  •  ONLY when short

### L07.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=136  W=45/L=91  WR=33.1%
- Sharpen: sharpest is H20=H20a (21/91 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60e AND T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_close (37/84 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L09.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (49/80 of losers there)
- **Sharp: n=54  W=5/L=49  WR=9.3%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L10.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is H60=H60e (39/75 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L11.  `H20=H20e AND H60=H60c AND RSI=RSI3`
- Raw: n=124  W=43/L=81  WR=34.7%
- Sharpen: sharpest is T4=T4c (52/81 of losers there)
- **Sharp: n=70  W=18/L=52  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20c AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is T4=T4a (64/73 of losers there)
- **Sharp: n=88  W=24/L=64  WR=27.3%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20c AND H60=H60a AND session_bucket=ny_close`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is T1=T1c (60/73 of losers there)
- **Sharp: n=84  W=24/L=60  WR=28.6%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20c AND H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is T1=T1c (60/73 of losers there)
- **Sharp: n=84  W=24/L=60  WR=28.6%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is RSI=RSI5 (12/72 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60d AND T4=T4c AND RSI=RSI4`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is T1=T1a (37/75 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L17.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=110  W=38/L=72  WR=34.5%
- Sharpen: sharpest is T4=T4a (60/72 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_open  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=109  W=39/L=70  WR=35.8%
- Sharpen: sharpest is RSI=RSI4 (51/70 of losers there)
- **Sharp: n=70  W=19/L=51  WR=27.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L19.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=108  W=37/L=71  WR=34.3%
- Sharpen: sharpest is direction_exec=short (60/71 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when short

### L20.  `H60=H60c AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=106  W=40/L=66  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (29/66 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L21.  `H20=H20c AND T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=105  W=38/L=67  WR=36.2%
- Sharpen: sharpest is H60=H60a (51/67 of losers there)
- **Sharp: n=67  W=16/L=51  WR=23.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is T4=T4a (41/64 of losers there)
- **Sharp: n=60  W=19/L=41  WR=31.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4a (39/63 of losers there)
- **Sharp: n=53  W=14/L=39  WR=26.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L24.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=104  W=40/L=64  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia

### L25.  `H20=H20c AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=102  W=34/L=68  WR=33.3%
- Sharpen: sharpest is T1=T1c (64/68 of losers there)
- **Sharp: n=88  W=24/L=64  WR=27.3%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(23/30) |
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
