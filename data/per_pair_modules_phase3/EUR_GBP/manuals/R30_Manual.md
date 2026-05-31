# EUR_GBP — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **590**  (W=378 / L=212)  -  WR: **64.1%**

## Session distribution

- ny_mid: n=207  W=132/L=75  WR=63.8%
- ny_open: n=99  W=60/L=39  WR=60.6%
- london: n=98  W=59/L=39  WR=60.2%
- london_open: n=84  W=55/L=29  WR=65.5%
- asia: n=60  W=43/L=17  WR=71.7%
- ny_close: n=24  W=16/L=8  WR=66.7%
- off_hours: n=18  W=13/L=5  WR=72.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20c drops 5/10 losers (50%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 neutral

### W02.  `T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude session_bucket=ny_close drops 2/7 losers (29%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W03.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude session_bucket=ny_close drops 2/7 losers (29%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W04.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 3/9 losers (33%)
- **Final: n=53  W=47/L=6  WR=88.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when strategy=alpha_breakout_retest_v2

### W05.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 6/8 losers (75%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W06.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 6/8 losers (75%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W07.  `H20=H20c AND H60=H60a AND T4=T4c`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude T1=T1c drops 8/8 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when 1h trend AGAINST trade

### W08.  `T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=53  W=47/L=6  WR=88.7%
- Refine: exclude session_bucket=ny_close drops 2/6 losers (33%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W09.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=53  W=47/L=6  WR=88.7%
- Refine: exclude session_bucket=ny_close drops 2/6 losers (33%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W10.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude ZS=ZS3 drops 4/5 losers (80%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20c AND T1=T1a AND RSI=RSI4`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W12.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=46  W=45/L=1  WR=97.8%
- Refine: no further refinement
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### W13.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=46  W=45/L=1  WR=97.8%
- Refine: no further refinement
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### W14.  `T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=45  W=40/L=5  WR=88.9%
- Refine: exclude H20=H20b drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when HTF20 slightly aligned

### W15.  `H20=H20c AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=43  W=43/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=ny_mid

### W16.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=43  W=38/L=5  WR=88.4%
- Refine: exclude session_bucket=ny_close drops 2/5 losers (40%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W17.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude T4=T4a drops 4/5 losers (80%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W18.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude RSI=RSI2 drops 2/2 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W19.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude RSI=RSI2 drops 2/2 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W20.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=41  W=39/L=2  WR=95.1%
- Refine: exclude RSI=RSI2 drops 2/2 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=41  W=37/L=4  WR=90.2%
- Refine: exclude T4=T4a drops 4/4 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 4h trend WITH trade

### W22.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 2/4 losers (50%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when strategy=echo_box_fade_v2

### W23.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W24.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude ZS=ZS3 drops 4/4 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=38  W=34/L=4  WR=89.5%
- Refine: exclude H60=H60a drops 4/4 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND RSI=RSI3`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is session_bucket=london (19/31 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L02.  `H20=H20a AND T4=T4a AND RSI=RSI3`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is session_bucket=london (21/30 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L03.  `T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is H60=H60e (22/32 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L04.  `T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is H20=H20c (11/27 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L05.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is H20=H20c (11/27 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L06.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=43  W=13/L=30  WR=30.2%
- Sharpen: sharpest is T1=T1a (19/30 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when 1h trend WITH trade

### L07.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is H20=H20c (15/28 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 neutral

### L08.  `T1=T1c AND T4=T4a AND session_bucket=london`
- Raw: n=41  W=9/L=32  WR=22.0%
- Sharpen: sharpest is H20=H20a (19/32 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L09.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI3 (11/30 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L10.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI3 (11/30 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L11.  `T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is RSI=RSI3 (17/28 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L12.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_open (14/25 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L13.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is H20=H20d (7/23 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L14.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is H20=H20d (7/23 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L15.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=37  W=12/L=25  WR=32.4%
- Sharpen: sharpest is H20=H20a (17/25 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=37  W=12/L=25  WR=32.4%
- Sharpen: sharpest is H20=H20a (17/25 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L17.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is ZS=ZS2 (23/23 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L18.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=35  W=12/L=23  WR=34.3%
- Sharpen: sharpest is T4=T4a (8/23 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L19.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=35  W=12/L=23  WR=34.3%
- Sharpen: sharpest is H60=H60e (18/23 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L20.  `T1=T1c AND BBP=BBP2 AND session_bucket=london`
- Raw: n=35  W=13/L=22  WR=37.1%
- Sharpen: sharpest is H20=H20a (16/22 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=london  •  ONLY when HTF20 aligned WITH trade

### L21.  `T1=T1c AND ZS=ZS2 AND session_bucket=london`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is H20=H20a (16/21 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=london  •  ONLY when HTF20 aligned WITH trade

### L22.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is H20=H20a (13/21 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is H20=H20a (16/21 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=london  •  ONLY when HTF20 aligned WITH trade

### L24.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is H20=H20a (13/21 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L25.  `H20=H20a AND T4=T4a AND BBP=BBP2`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is ZS=ZS2 (22/22 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when zscore -2 to -1 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(12/17) |
| H60 | H60e(39/32) | H60a(33/40) |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | T4c(53/41) | T4a(47/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/46) | short(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
