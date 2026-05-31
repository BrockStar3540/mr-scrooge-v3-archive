# GBP_CAD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,125**  (W=1,890 / L=1,235)  -  WR: **60.5%**

## Session distribution

- ny_mid: n=914  W=545/L=369  WR=59.6%
- ny_open: n=555  W=317/L=238  WR=57.1%
- ny_close: n=475  W=292/L=183  WR=61.5%
- london_open: n=409  W=253/L=156  WR=61.9%
- asia: n=336  W=211/L=125  WR=62.8%
- london: n=268  W=165/L=103  WR=61.6%
- off_hours: n=99  W=61/L=38  WR=61.6%
- asia_late: n=69  W=46/L=23  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude T1=T1a drops 7/11 losers (64%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when 1h trend WITH trade

### W02.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=100  W=97/L=3  WR=97.0%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W03.  `H60=H60c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=88  W=85/L=3  WR=96.6%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; session=ny_close  •  AVOID when lower third

### W04.  `H20=H20a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=81  W=78/L=3  WR=96.3%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=81  W=78/L=3  WR=96.3%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude T1=T1a drops 7/8 losers (88%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude T1=T1a drops 7/8 losers (88%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 1h trend WITH trade

### W08.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP5 drops 8/11 losers (73%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  AVOID when just touched upper band

### W09.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude BBP=BBP5 drops 8/11 losers (73%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when just touched upper band

### W10.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H20=H20c drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W11.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H20=H20c drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W12.  `H60=H60c AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=79  W=77/L=2  WR=97.5%
- Refine: exclude BBP=BBP2 drops 2/2 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when lower third

### W13.  `H20=H20a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=79  W=76/L=3  WR=96.2%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W14.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude H60=H60e drops 2/2 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  AVOID when HTF60 strongly against

### W15.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude H60=H60e drops 2/2 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W16.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H60=H60a drops 9/9 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W17.  `T4=T4c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W18.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=74  W=74/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band

### W19.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude H20=H20d drops 3/4 losers (75%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when HTF20 mildly against

### W20.  `H60=H60a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude H20=H20d drops 3/4 losers (75%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 mildly against

### W21.  `H60=H60c AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 6/9 losers (67%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W22.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude H20=H20d drops 3/7 losers (43%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 mildly against

### W23.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude session_bucket=ny_mid drops 9/9 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_mid

### W24.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W25.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude session_bucket=ny_mid drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=147  W=52/L=95  WR=35.4%
- Sharpen: sharpest is BBP=BBP4 (39/95 of losers there)
- **Sharp: n=40  W=1/L=39  WR=2.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when upper third

### L02.  `H60=H60c AND T1=T1c AND T4=T4a`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is BBP=BBP4 (31/86 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when upper third

### L03.  `H60=H60c AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is BBP=BBP4 (31/86 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L04.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=129  W=41/L=88  WR=31.8%
- Sharpen: sharpest is direction_exec=short (39/88 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when short

### L05.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=120  W=44/L=76  WR=36.7%
- Sharpen: sharpest is BBP=BBP4 (39/76 of losers there)
- **Sharp: n=40  W=1/L=39  WR=2.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L06.  `H20=H20b AND T4=T4c AND direction_exec=long`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (12/72 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L07.  `H20=H20b AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (12/72 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L08.  `T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=108  W=38/L=70  WR=35.2%
- Sharpen: sharpest is H20=H20e (26/70 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L09.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=107  W=38/L=69  WR=35.5%
- Sharpen: sharpest is H20=H20e (26/69 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L10.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is session_bucket=ny_open (39/67 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_open

### L11.  `H20=H20a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=101  W=31/L=70  WR=30.7%
- Sharpen: sharpest is H60=H60a (39/70 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L12.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=101  W=31/L=70  WR=30.7%
- Sharpen: sharpest is H60=H60a (39/70 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L13.  `T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is H20=H20e (24/65 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is H20=H20e (24/65 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L15.  `T4=T4c AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_long (16/65 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=ny_mid  •  ONLY when strategy=TF2_pullback_EMA20_long

### L16.  `T1=T1c AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is H20=H20e (24/64 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L17.  `H20=H20c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_open (23/61 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_open

### L18.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=94  W=30/L=64  WR=31.9%
- Sharpen: sharpest is H20=H20e (26/64 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L19.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=92  W=30/L=62  WR=32.6%
- Sharpen: sharpest is ZS=ZS4 (19/62 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L20.  `H20=H20e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=88  W=31/L=57  WR=35.2%
- Sharpen: sharpest is session_bucket=ny_mid (38/57 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: LONG**  •  HTF20 strongly against; upper third  •  ONLY when session=ny_mid

### L21.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_open (39/54 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L22.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=86  W=27/L=59  WR=31.4%
- Sharpen: sharpest is H20=H20e (24/59 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L23.  `H60=H60e AND T4=T4c AND BBP=BBP4`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is H20=H20e (20/56 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L24.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H60=H60c (23/51 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF60 neutral

### L25.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=84  W=22/L=62  WR=26.2%
- Sharpen: sharpest is ZS=ZS4 (19/62 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

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
| direction_exec | short(54/48) | long(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
