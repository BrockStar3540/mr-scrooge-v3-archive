# EUR_CHF — R31 Manual

## Regime centroid (locked factors)

- **BB = BB0**  (very narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **898**  (W=582 / L=316)  -  WR: **64.8%**

## Session distribution

- asia: n=380  W=250/L=130  WR=65.8%
- london_open: n=112  W=67/L=45  WR=59.8%
- ny_close: n=110  W=70/L=40  WR=63.6%
- asia_late: n=107  W=64/L=43  WR=59.8%
- ny_open: n=86  W=56/L=30  WR=65.1%
- london: n=45  W=32/L=13  WR=71.1%
- off_hours: n=41  W=31/L=10  WR=75.6%
- ny_mid: n=17  W=12/L=5  WR=70.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude T1=T1c drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W03.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W04.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H60=H60a drops 5/7 losers (71%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 aligned WITH trade

### W05.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=58  W=54/L=4  WR=93.1%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W07.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude H60=H60a drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W08.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=52  W=52/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade

### W09.  `H20=H20a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W10.  `H20=H20a AND H60=H60d AND direction_exec=long`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20a AND H60=H60a AND T4=T4c`
- Raw: n=48  W=43/L=5  WR=89.6%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W12.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=48  W=43/L=5  WR=89.6%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W13.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude T4=T4c drops 6/7 losers (86%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=47  W=43/L=4  WR=91.5%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude direction_exec=short drops 4/5 losers (80%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when short

### W16.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude H60=H60a drops 5/5 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20a AND H60=H60a AND session_bucket=ny_close`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W18.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W19.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W20.  `H60=H60e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=46  W=40/L=6  WR=87.0%
- Refine: exclude H60=H60d drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W22.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=46  W=40/L=6  WR=87.0%
- Refine: exclude H60=H60b drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 slightly aligned

### W23.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=45  W=42/L=3  WR=93.3%
- Refine: exclude H60=H60d drops 2/3 losers (67%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 mildly against

### W24.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=45  W=40/L=5  WR=88.9%
- Refine: exclude H60=H60d drops 3/5 losers (60%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF60 mildly against

### W25.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=43  W=38/L=5  WR=88.4%
- Refine: exclude T1=T1c drops 5/5 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=70  W=21/L=49  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (20/49 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L02.  `H20=H20e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is H60=H60b (20/44 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is H20=H20a (24/42 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L04.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=57  W=18/L=39  WR=31.6%
- Sharpen: sharpest is session_bucket=asia (16/39 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L05.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is H60=H60e (23/36 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=53  W=14/L=39  WR=26.4%
- Sharpen: sharpest is H60=H60b (23/39 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when HTF60 slightly aligned

### L07.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=50  W=17/L=33  WR=34.0%
- Sharpen: sharpest is ZS=ZS5 (8/33 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is T1=T1a (15/31 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=46  W=13/L=33  WR=28.3%
- Sharpen: sharpest is T4=T4c (28/33 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is ZS=ZS5 (9/31 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is H60=H60e (17/29 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L12.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is T1=T1a (14/29 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L13.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=45  W=15/L=30  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (8/30 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is direction_exec=short (28/28 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when short

### L15.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is T1=T1a (23/27 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when 1h trend WITH trade

### L16.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is T1=T1a (23/27 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when 1h trend WITH trade

### L17.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=43  W=14/L=29  WR=32.6%
- Sharpen: sharpest is session_bucket=asia_late (6/29 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L18.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=43  W=14/L=29  WR=32.6%
- Sharpen: sharpest is session_bucket=asia_late (6/29 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L19.  `T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is RSI=RSI4 (24/27 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L20.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is RSI=RSI4 (24/27 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L21.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is H60=H60b (15/31 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 slightly aligned

### L22.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is T4=T4c (20/28 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when 4h trend AGAINST trade

### L23.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=39  W=12/L=27  WR=30.8%
- Sharpen: sharpest is direction_exec=short (15/27 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when short

### L24.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is H20=H20e (15/24 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L25.  `H60=H60e AND ZS=ZS3 AND direction_exec=long`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is BBP=BBP3 (15/25 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -1 to +1 neutral  •  ONLY when middle of band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/29), H20d(11/4) | H20e(31/49), H20b(4/9) |
| H60 | H60a(38/28) | H60e(28/35) |
| T1 | — | — |
| T4 | T4a(57/44) | T4c(43/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
