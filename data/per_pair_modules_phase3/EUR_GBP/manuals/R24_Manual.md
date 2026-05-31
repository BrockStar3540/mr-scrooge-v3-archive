# EUR_GBP — R24 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **994**  (W=666 / L=328)  -  WR: **67.0%**

## Session distribution

- london_open: n=322  W=216/L=106  WR=67.1%
- ny_mid: n=238  W=163/L=75  WR=68.5%
- ny_open: n=123  W=79/L=44  WR=64.2%
- asia: n=108  W=71/L=37  WR=65.7%
- london: n=102  W=76/L=26  WR=74.5%
- ny_close: n=59  W=31/L=28  WR=52.5%
- off_hours: n=36  W=25/L=11  WR=69.4%
- asia_late: n=6  W=5/L=1  WR=83.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude H20=H20e drops 6/18 losers (33%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W02.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude session_bucket=london_open drops 9/17 losers (53%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london_open

### W03.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H60=H60a drops 15/17 losers (88%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W04.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=london_open drops 9/15 losers (60%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london_open

### W05.  `T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude direction_exec=long drops 13/15 losers (87%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when long

### W06.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london_open  •  AVOID when 4h trend WITH trade

### W07.  `T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=ny_mid drops 7/12 losers (58%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W08.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude H60=H60e drops 9/12 losers (75%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W09.  `H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20e drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third  •  AVOID when HTF20 strongly against

### W10.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude T1=T1a drops 6/12 losers (50%)
- **Final: n=53  W=47/L=6  WR=88.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W11.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude T1=T1a drops 6/12 losers (50%)
- **Final: n=53  W=47/L=6  WR=88.7%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W12.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=london_open drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W13.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=london_open drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W14.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude direction_exec=long drops 7/11 losers (64%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when long

### W15.  `H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude RSI=RSI4 drops 8/11 losers (73%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W16.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=73  W=71/L=2  WR=97.3%
- Refine: exclude BBP=BBP2 drops 2/2 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when lower third

### W17.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude RSI=RSI5 drops 8/10 losers (80%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 60-70 strong

### W18.  `T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude H20=H20e drops 3/9 losers (33%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W19.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude H20=H20e drops 3/9 losers (33%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W20.  `T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20e drops 3/9 losers (33%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W21.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20e drops 3/9 losers (33%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W22.  `T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude T4=T4c drops 7/9 losers (78%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third  •  AVOID when 4h trend AGAINST trade

### W23.  `H20=H20a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=62  W=57/L=5  WR=91.9%
- Refine: exclude session_bucket=london_open drops 3/5 losers (60%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third  •  AVOID when session=london_open

### W24.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude RSI=RSI5 drops 8/9 losers (89%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when RSI 60-70 strong

### W25.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T4=T4a (22/45 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L02.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is T4=T4a (30/43 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london_open  •  ONLY when 4h trend WITH trade

### L03.  `T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is direction_exec=long (30/41 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when long

### L04.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is RSI=RSI3 (22/38 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L05.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is H60=H60a (8/36 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L06.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is T4=T4a (23/36 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 4h trend WITH trade

### L07.  `H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=54  W=18/L=36  WR=33.3%
- Sharpen: sharpest is T1=T1a (27/36 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend WITH trade

### L08.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is session_bucket=london_open (12/29 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when session=london_open

### L09.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is H20=H20e (13/27 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L10.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=40  W=16/L=24  WR=40.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia

### L11.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=39  W=13/L=26  WR=33.3%
- Sharpen: sharpest is H20=H20e (14/26 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L12.  `T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is session_bucket=london_open (12/25 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L13.  `H20=H20e AND T4=T4a AND RSI=RSI3`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is direction_exec=long (22/24 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when long

### L14.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=38  W=11/L=27  WR=28.9%
- Sharpen: sharpest is RSI=RSI3 (19/27 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L15.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=37  W=13/L=24  WR=35.1%
- Sharpen: sharpest is H20=H20e (13/24 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L16.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=36  W=9/L=27  WR=25.0%
- Sharpen: sharpest is H20=H20e (7/27 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L17.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=35  W=5/L=30  WR=14.3%
- Sharpen: sharpest is ZS=ZS5 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=35  W=11/L=24  WR=31.4%
- Sharpen: sharpest is T4=T4a (14/24 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L19.  `BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=35  W=12/L=23  WR=34.3%
- Sharpen: sharpest is T4=T4a (12/23 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: LONG**  •  upper third; session=london_open  •  ONLY when 4h trend WITH trade

### L20.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (12/21 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L21.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=34  W=10/L=24  WR=29.4%
- Sharpen: sharpest is direction_exec=long (23/24 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when long

### L22.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=34  W=11/L=23  WR=32.4%
- Sharpen: sharpest is T4=T4a (13/23 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L23.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is session_bucket=london_open (9/21 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L24.  `H20=H20e AND H60=H60e AND BBP=BBP4`
- Raw: n=32  W=12/L=20  WR=37.5%
- Sharpen: sharpest is strategy_id=BR2_vcb_long (3/20 of losers there)
- **Sharp: n=3  W=0/L=3  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third  •  ONLY when strategy=BR2_vcb_long

### L25.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=32  W=12/L=20  WR=37.5%
- Sharpen: sharpest is strategy_id=BR2_vcb_long (3/20 of losers there)
- **Sharp: n=3  W=0/L=3  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; upper third  •  ONLY when strategy=BR2_vcb_long

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(33/26) | H20e(24/34) |
| H60 | H60a(38/27) | H60e(27/39) |
| T1 | — | — |
| T4 | T4c(53/43) | T4a(46/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(62/40) | long(38/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
