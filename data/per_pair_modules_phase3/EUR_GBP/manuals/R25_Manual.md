# EUR_GBP — R25 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,316**  (W=1,499 / L=817)  -  WR: **64.7%**

## Session distribution

- asia: n=464  W=288/L=176  WR=62.1%
- london_open: n=446  W=296/L=150  WR=66.4%
- ny_close: n=386  W=258/L=128  WR=66.8%
- london: n=333  W=218/L=115  WR=65.5%
- ny_open: n=250  W=158/L=92  WR=63.2%
- ny_mid: n=212  W=138/L=74  WR=65.1%
- asia_late: n=160  W=103/L=57  WR=64.4%
- off_hours: n=65  W=40/L=25  WR=61.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=126  W=111/L=15  WR=88.1%
- Refine: exclude T1=T1c drops 11/15 losers (73%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when 1h trend AGAINST trade

### W02.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude H20=H20d drops 6/18 losers (33%)
- **Final: n=108  W=96/L=12  WR=88.9%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W03.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude direction_exec=short drops 12/17 losers (71%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when short

### W04.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude H60=H60e drops 10/15 losers (67%)
- **Final: n=86  W=81/L=5  WR=94.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W05.  `H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_close drops 4/13 losers (31%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W06.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude H20=H20a drops 10/13 losers (77%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 aligned WITH trade

### W07.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude RSI=RSI3 drops 11/13 losers (85%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W08.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=88  W=81/L=7  WR=92.0%
- Refine: exclude BBP=BBP3 drops 4/7 losers (57%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  AVOID when middle of band

### W09.  `H20=H20b AND H60=H60a AND RSI=RSI3`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude T4=T4a drops 11/12 losers (92%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20e AND H60=H60b AND direction_exec=short`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude BBP=BBP0 drops 5/10 losers (50%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned  •  AVOID when deep below lower band

### W11.  `H20=H20b AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude direction_exec=short drops 8/10 losers (80%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when short

### W12.  `H20=H20b AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude T4=T4a drops 11/12 losers (92%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W13.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H20=H20a drops 6/11 losers (55%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude H60=H60e drops 5/9 losers (56%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; deep above upper band  •  AVOID when HTF60 strongly against

### W15.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude session_bucket=asia drops 3/9 losers (33%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W16.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W17.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H60=H60e drops 5/10 losers (50%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W18.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude session_bucket=london_open drops 3/4 losers (75%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london_open

### W19.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W20.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H20=H20a drops 5/10 losers (50%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W21.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude H60=H60a drops 3/5 losers (60%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W22.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude session_bucket=london_open drops 3/4 losers (75%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london_open

### W23.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude H60=H60e drops 5/8 losers (62%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W24.  `H20=H20b AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude direction_exec=short drops 5/9 losers (56%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when short

### W25.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude H20=H20e drops 4/8 losers (50%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: SHORT**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is session_bucket=asia (17/58 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=asia

### L02.  `H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: sharpest is RSI=RSI4 (37/52 of losers there)
- **Sharp: n=50  W=13/L=37  WR=26.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L03.  `H20=H20d AND H60=H60e AND direction_exec=long`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is T1=T1c (29/52 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is H60=H60b (16/46 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L05.  `H20=H20a AND T1=T1c AND ZS=ZS5`
- Raw: n=75  W=27/L=48  WR=36.0%
- Sharpen: sharpest is H60=H60d (17/48 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 mildly against

### L06.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H20=H20a (25/47 of losers there)
- **Sharp: n=33  W=8/L=25  WR=24.2%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L07.  `H20=H20a AND H60=H60d AND direction_exec=long`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is BBP=BBP6 (13/50 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  ONLY when deep above upper band

### L08.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is direction_exec=short (7/42 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when short

### L09.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is BBP=BBP4 (12/42 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when upper third

### L10.  `H20=H20d AND T4=T4c AND BBP=BBP4`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is T1=T1a (25/40 of losers there)
- **Sharp: n=36  W=11/L=25  WR=30.6%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; upper third  •  ONLY when 1h trend WITH trade

### L11.  `H20=H20d AND T1=T1a AND RSI=RSI4`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is direction_exec=short (22/42 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when short

### L12.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (10/38 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L13.  `H20=H20d AND H60=H60e AND T4=T4c`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is T1=T1c (21/39 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L14.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=56  W=13/L=43  WR=23.2%
- Sharpen: sharpest is RSI=RSI4 (33/43 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20d AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=56  W=15/L=41  WR=26.8%
- Sharpen: sharpest is direction_exec=short (22/41 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when short

### L16.  `T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is H20=H20a (22/35 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L17.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is T1=T1c (22/35 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L18.  `H20=H20a AND T1=T1c AND BBP=BBP6`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is H60=H60d (15/39 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  ONLY when HTF60 mildly against

### L19.  `H20=H20d AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is T1=T1c (20/33 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L20.  `H20=H20a AND H60=H60d AND RSI=RSI3 AND direction_exec=long`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is session_bucket=asia_late (10/33 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 40-50 lower neutral  •  ONLY when session=asia_late

### L21.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=54  W=21/L=33  WR=38.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia

### L22.  `H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=53  W=14/L=39  WR=26.4%
- Sharpen: sharpest is T1=T1a (15/39 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend WITH trade

### L23.  `H20=H20d AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is BBP=BBP6 (6/34 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L24.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is H20=H20a (17/34 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 aligned WITH trade

### L25.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is direction_exec=short (8/32 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when short

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(37/26), H20b(20/15) | H20a(26/39) |
| H60 | H60a(32/25) | H60e(27/32) |
| T1 | — | — |
| T4 | T4a(53/48) | T4c(46/51) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
