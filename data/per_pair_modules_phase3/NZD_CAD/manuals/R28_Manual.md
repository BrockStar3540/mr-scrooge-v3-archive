# NZD_CAD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,800**  (W=1,133 / L=667)  -  WR: **62.9%**

## Session distribution

- asia: n=416  W=270/L=146  WR=64.9%
- london_open: n=303  W=191/L=112  WR=63.0%
- ny_open: n=284  W=171/L=113  WR=60.2%
- ny_mid: n=269  W=160/L=109  WR=59.5%
- london: n=263  W=162/L=101  WR=61.6%
- ny_close: n=133  W=90/L=43  WR=67.7%
- asia_late: n=118  W=82/L=36  WR=69.5%
- off_hours: n=14  W=7/L=7  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=asia drops 10/14 losers (71%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W02.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=asia drops 10/14 losers (71%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W03.  `H20=H20d AND H60=H60a AND T4=T4a`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude direction_exec=long drops 11/14 losers (79%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when long

### W04.  `H60=H60a AND T1=T1c AND BBP=BBP0`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=asia_late drops 3/12 losers (25%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia_late

### W05.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude session_bucket=asia drops 6/11 losers (55%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W06.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H60=H60e drops 12/14 losers (86%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  AVOID when HTF60 strongly against

### W07.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude session_bucket=asia_late drops 3/12 losers (25%)
- **Final: n=84  W=75/L=9  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia_late

### W08.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=asia drops 6/9 losers (67%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W09.  `T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H20=H20e drops 9/12 losers (75%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third  •  AVOID when HTF20 strongly against

### W10.  `H20=H20d AND H60=H60a AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude T4=T4c drops 9/12 losers (75%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade  •  AVOID when 4h trend AGAINST trade

### W11.  `T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 strongly against

### W12.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H20=H20e drops 8/11 losers (73%)
- **Final: n=37  W=34/L=3  WR=91.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W13.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=asia drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W14.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude session_bucket=ny_mid drops 4/9 losers (44%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_mid

### W15.  `T4=T4c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude H60=H60e drops 7/9 losers (78%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when HTF60 strongly against

### W16.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=asia drops 4/9 losers (44%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W17.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS0 drops 3/10 losers (30%)
- **Final: n=64  W=57/L=7  WR=89.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when zscore <-3 extreme

### W18.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W19.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude H60=H60e drops 3/8 losers (38%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W20.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; session=asia  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when lower third

### W22.  `H20=H20d AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when lower third

### W23.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude BBP=BBP0 drops 7/8 losers (88%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when deep below lower band

### W24.  `H20=H20e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude T1=T1a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20e AND T1=T1c AND BBP=BBP0`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND ZS=ZS2`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=41/L=64  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold

### L02.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=41/L=64  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold

### L03.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=97  W=37/L=60  WR=38.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold

### L04.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=87  W=28/L=59  WR=32.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third

### L05.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is T4=T4c (30/53 of losers there)
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (41/50 of losers there)
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L07.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is H20=H20a (21/48 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L08.  `H20=H20e AND T4=T4c AND ZS=ZS2`
- Raw: n=79  W=26/L=53  WR=32.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=79  W=26/L=53  WR=32.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L09.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=79  W=26/L=53  WR=32.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=79  W=26/L=53  WR=32.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L10.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is BBP=BBP1 (8/46 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when just touched lower band

### L11.  `H20=H20e AND H60=H60a AND BBP=BBP2`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is T4=T4c (19/44 of losers there)
- **Sharp: n=25  W=6/L=19  WR=24.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20c AND T1=T1c AND T4=T4a`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (17/44 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london_open

### L13.  `H20=H20c AND T1=T1c AND direction_exec=long`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (17/44 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=london_open

### L14.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (17/44 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  ONLY when session=london_open

### L15.  `H20=H20c AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (17/44 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london_open

### L16.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/42 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=london_open

### L17.  `H20=H20c AND H60=H60e AND T4=T4a`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/42 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=london_open

### L18.  `H20=H20c AND H60=H60e AND direction_exec=long`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/42 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against  •  ONLY when session=london_open

### L19.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/42 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london_open

### L20.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/42 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=london_open

### L21.  `H20=H20c AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/42 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=london_open

### L22.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is session_bucket=london_open (13/45 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=london_open

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=67  W=19/L=48  WR=28.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=67  W=19/L=48  WR=28.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral

### L24.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is session_bucket=london_open (13/43 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L25.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is H60=H60e (12/42 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(54/43) | H60e(41/52) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
