# NZD_USD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,646**  (W=1,687 / L=959)  -  WR: **63.8%**

## Session distribution

- asia: n=963  W=633/L=330  WR=65.7%
- ny_close: n=625  W=377/L=248  WR=60.3%
- london_open: n=255  W=165/L=90  WR=64.7%
- london: n=249  W=154/L=95  WR=61.8%
- ny_open: n=223  W=139/L=84  WR=62.3%
- asia_late: n=176  W=124/L=52  WR=70.5%
- off_hours: n=112  W=65/L=47  WR=58.0%
- ny_mid: n=43  W=30/L=13  WR=69.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude BBP=BBP5 drops 7/17 losers (41%)
- **Final: n=99  W=89/L=10  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when just touched upper band

### W02.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 10/15 losers (67%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W03.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude H20=H20c drops 4/9 losers (44%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF20 neutral

### W04.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude strategy_id=BR2_vcb_short drops 4/10 losers (40%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when strategy=BR2_vcb_short

### W05.  `H20=H20a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=77  W=75/L=2  WR=97.4%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when upper third

### W06.  `H20=H20a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude BBP=BBP4 drops 7/8 losers (88%)
- **Final: n=62  W=61/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia_late  •  AVOID when upper third

### W07.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude BBP=BBP2 drops 4/8 losers (50%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W08.  `H60=H60e AND T4=T4a AND session_bucket=asia_late`
- Raw: n=76  W=74/L=2  WR=97.4%
- Refine: exclude H20=H20e drops 2/2 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia_late  •  AVOID when HTF20 strongly against

### W09.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude BBP=BBP4 drops 6/10 losers (60%)
- **Final: n=44  W=40/L=4  WR=90.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when upper third

### W10.  `H20=H20e AND H60=H60d AND T1=T1a`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude T4=T4a drops 5/11 losers (45%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

### W11.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude T4=T4c drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W12.  `H20=H20e AND H60=H60d AND T1=T1a AND T4=T4c`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude session_bucket=ny_open drops 5/6 losers (83%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W13.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude T1=T1c drops 7/8 losers (88%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W14.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude H60=H60e drops 7/9 losers (78%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF60 strongly against

### W15.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude H60=H60e drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF60 strongly against

### W16.  `H60=H60e AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia_late  •  AVOID when 4h trend AGAINST trade

### W17.  `T4=T4a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=64  W=63/L=1  WR=98.4%
- Refine: no further refinement
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia_late

### W18.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W19.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 3/9 losers (33%)
- **Final: n=57  W=51/L=6  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W20.  `T1=T1c AND T4=T4a AND session_bucket=asia_late`
- Raw: n=63  W=62/L=1  WR=98.4%
- Refine: no further refinement
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia_late

### W21.  `T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=63  W=62/L=1  WR=98.4%
- Refine: no further refinement
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia_late

### W22.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W23.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=50  W=46/L=4  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=asia  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=61  W=60/L=1  WR=98.4%
- Refine: no further refinement
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia_late

### W25.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (45/68 of losers there)
- **Sharp: n=64  W=19/L=45  WR=29.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L02.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is direction_exec=long (32/67 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when long

### L03.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=74  W=28/L=46  WR=37.8%
- Sharpen: sharpest is T1=T1a (30/46 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L04.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T4=T4a (41/44 of losers there)
- **Sharp: n=55  W=14/L=41  WR=25.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L05.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is H20=H20e (10/47 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when HTF20 strongly against

### L06.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is RSI=RSI3 (32/45 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L07.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (14/42 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L08.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (11/39 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_open

### L09.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=64  W=19/L=45  WR=29.7%
- Sharpen: sharpest is direction_exec=short (22/45 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when short

### L10.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=24/L=38  WR=38.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L11.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is T1=T1a (25/39 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L12.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is BBP=BBP1 (26/38 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L13.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is T1=T1a (28/39 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend WITH trade

### L14.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_open (10/37 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L15.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is ZS=ZS0 (15/35 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L16.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is H20=H20e (20/35 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L17.  `H20=H20e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=56  W=17/L=39  WR=30.4%
- Sharpen: sharpest is ZS=ZS0 (21/39 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  HTF20 strongly against; deep below lower band  •  ONLY when zscore <-3 extreme

### L18.  `T1=T1c AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=56  W=18/L=38  WR=32.1%
- Sharpen: sharpest is RSI=RSI3 (11/38 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=55  W=13/L=42  WR=23.6%
- Sharpen: sharpest is T4=T4c (14/42 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is T1=T1c (20/39 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L21.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H20=H20e (22/35 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when HTF20 strongly against

### L22.  `H20=H20a AND H60=H60b AND T1=T1c AND T4=T4a`
- Raw: n=54  W=17/L=37  WR=31.5%
- Sharpen: sharpest is session_bucket=asia (19/37 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L23.  `T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H60=H60a (23/33 of losers there)
- **Sharp: n=33  W=10/L=23  WR=30.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band  •  ONLY when HTF60 aligned WITH trade

### L24.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H60=H60a (23/33 of losers there)
- **Sharp: n=33  W=10/L=23  WR=30.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L25.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is H20=H20e (19/35 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/38) | H20e(38/47) |
| H60 | — | — |
| T1 | T1c(53/45) | T1a(46/54) |
| T4 | T4a(56/47) | T4c(44/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
