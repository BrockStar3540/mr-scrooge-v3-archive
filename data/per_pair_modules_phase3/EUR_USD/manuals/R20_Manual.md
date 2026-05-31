# EUR_USD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,967**  (W=1,913 / L=1,054)  -  WR: **64.5%**

## Session distribution

- london_open: n=755  W=496/L=259  WR=65.7%
- ny_mid: n=673  W=442/L=231  WR=65.7%
- ny_open: n=497  W=303/L=194  WR=61.0%
- london: n=330  W=211/L=119  WR=63.9%
- ny_close: n=329  W=209/L=120  WR=63.5%
- asia: n=282  W=187/L=95  WR=66.3%
- asia_late: n=100  W=65/L=35  WR=65.0%
- off_hours: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=221  W=188/L=33  WR=85.1%
- Refine: exclude session_bucket=london_open drops 25/33 losers (76%)
- **Final: n=127  W=119/L=8  WR=93.7%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W02.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=182  W=160/L=22  WR=87.9%
- Refine: exclude H60=H60a drops 18/22 losers (82%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF60 aligned WITH trade

### W03.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=178  W=157/L=21  WR=88.2%
- Refine: exclude H60=H60a drops 18/21 losers (86%)
- **Final: n=100  W=97/L=3  WR=97.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF60 aligned WITH trade

### W04.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=151  W=142/L=9  WR=94.0%
- Refine: exclude T4=T4a drops 8/9 losers (89%)
- **Final: n=81  W=80/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W05.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=147  W=125/L=22  WR=85.0%
- Refine: exclude H60=H60e drops 9/22 losers (41%)
- **Final: n=122  W=109/L=13  WR=89.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 strongly against

### W06.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude T1=T1a drops 12/21 losers (57%)
- **Final: n=130  W=121/L=9  WR=93.1%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W07.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=144  W=128/L=16  WR=88.9%
- Refine: exclude session_bucket=london_open drops 13/16 losers (81%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W08.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=140  W=122/L=18  WR=87.1%
- Refine: exclude H60=H60a drops 10/18 losers (56%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W09.  `H20=H20d AND T1=T1c AND direction_exec=short`
- Raw: n=135  W=118/L=17  WR=87.4%
- Refine: exclude H60=H60e drops 15/17 losers (88%)
- **Final: n=80  W=78/L=2  WR=97.5%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade  •  AVOID when HTF60 strongly against

### W10.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=130  W=121/L=9  WR=93.1%
- Refine: exclude T4=T4a drops 8/9 losers (89%)
- **Final: n=78  W=77/L=1  WR=98.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W11.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude H20=H20e drops 11/18 losers (61%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  AVOID when HTF20 strongly against

### W12.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=122  W=107/L=15  WR=87.7%
- Refine: exclude session_bucket=asia drops 5/15 losers (33%)
- **Final: n=111  W=101/L=10  WR=91.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

### W13.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude session_bucket=london_open drops 12/15 losers (80%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=london_open

### W14.  `T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude ZS=ZS2 drops 8/18 losers (44%)
- **Final: n=98  W=88/L=10  WR=89.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W15.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=118  W=112/L=6  WR=94.9%
- Refine: exclude H60=H60d drops 5/6 losers (83%)
- **Final: n=96  W=95/L=1  WR=99.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W16.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H60=H60b drops 7/17 losers (41%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  AVOID when HTF60 slightly aligned

### W17.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude T1=T1a drops 11/17 losers (65%)
- **Final: n=101  W=95/L=6  WR=94.1%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W18.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 5/15 losers (33%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W19.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude T1=T1c drops 10/15 losers (67%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W20.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=108  W=98/L=10  WR=90.7%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=103  W=96/L=7  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W21.  `H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=107  W=103/L=4  WR=96.3%
- Refine: exclude session_bucket=ny_open drops 3/4 losers (75%)
- **Final: n=90  W=89/L=1  WR=98.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=ny_open

### W22.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=102  W=96/L=6  WR=94.1%
- Refine: exclude session_bucket=london_open drops 6/6 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W23.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude ZS=ZS4 drops 4/11 losers (36%)
- **Final: n=83  W=76/L=7  WR=91.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W24.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=93  W=89/L=4  WR=95.7%
- Refine: exclude session_bucket=ny_open drops 3/4 losers (75%)
- **Final: n=90  W=89/L=1  WR=98.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W25.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude session_bucket=london_open drops 8/12 losers (67%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is H60=H60a (43/83 of losers there)
- **Sharp: n=57  W=14/L=43  WR=24.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L02.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=115  W=44/L=71  WR=38.3%
- Sharpen: sharpest is T4=T4c (54/71 of losers there)
- **Sharp: n=80  W=26/L=54  WR=32.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L03.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is RSI=RSI4 (38/69 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L04.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is RSI=RSI4 (33/63 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L05.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=96  W=28/L=68  WR=29.2%
- Sharpen: sharpest is T4=T4a (38/68 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L06.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is session_bucket=london (17/59 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when session=london

### L07.  `H20=H20e AND H60=H60a AND session_bucket=london_open`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is T1=T1c (39/57 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london_open  •  ONLY when 1h trend AGAINST trade

### L08.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is session_bucket=london_open (13/57 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L09.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is session_bucket=london (17/54 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when session=london

### L10.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is RSI=RSI3 (43/53 of losers there)
- **Sharp: n=57  W=14/L=43  WR=24.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L11.  `H20=H20e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=83  W=29/L=54  WR=34.9%
- Sharpen: sharpest is direction_exec=long (29/54 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when long

### L12.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=81  W=25/L=56  WR=30.9%
- Sharpen: sharpest is T4=T4a (33/56 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20e AND T4=T4c AND BBP=BBP5`
- Raw: n=81  W=31/L=50  WR=38.3%
- Sharpen: sharpest is T1=T1c (34/50 of losers there)
- **Sharp: n=48  W=14/L=34  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=81  W=31/L=50  WR=38.3%
- Sharpen: sharpest is T1=T1c (34/50 of losers there)
- **Sharp: n=48  W=14/L=34  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=26/L=54  WR=32.5%
- Sharpen: sharpest is BBP=BBP0 (18/54 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L16.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is RSI=RSI4 (30/53 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L17.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is H20=H20e (35/49 of losers there)
- **Sharp: n=50  W=15/L=35  WR=30.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L18.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=76  W=25/L=51  WR=32.9%
- Sharpen: sharpest is T1=T1c (27/51 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20e AND T1=T1c AND BBP=BBP5`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is session_bucket=london_open (19/50 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=london_open

### L20.  `H20=H20e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is session_bucket=london_open (19/50 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L21.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is T4=T4a (30/49 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L22.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is session_bucket=london (15/46 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L23.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=71  W=19/L=52  WR=26.8%
- Sharpen: sharpest is RSI=RSI3 (15/52 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L24.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is direction_exec=long (43/43 of losers there)
- **Sharp: n=57  W=14/L=43  WR=24.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when long

### L25.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=69  W=26/L=43  WR=37.7%
- Sharpen: sharpest is H60=H60b (16/43 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(9/4) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(58/45) | long(42/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
