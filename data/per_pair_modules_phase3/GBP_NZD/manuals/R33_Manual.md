# GBP_NZD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,778**  (W=2,970 / L=1,808)  -  WR: **62.2%**

## Session distribution

- asia: n=2051  W=1290/L=761  WR=62.9%
- london_open: n=717  W=451/L=266  WR=62.9%
- london: n=558  W=340/L=218  WR=60.9%
- ny_open: n=400  W=239/L=161  WR=59.8%
- ny_close: n=364  W=229/L=135  WR=62.9%
- ny_mid: n=352  W=221/L=131  WR=62.8%
- asia_late: n=228  W=139/L=89  WR=61.0%
- off_hours: n=108  W=61/L=47  WR=56.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=174  W=151/L=23  WR=86.8%
- Refine: exclude H20=H20e drops 14/23 losers (61%)
- **Final: n=115  W=106/L=9  WR=92.2%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W02.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude H20=H20e drops 11/18 losers (61%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W03.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude H20=H20e drops 11/18 losers (61%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W04.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude session_bucket=london drops 9/19 losers (47%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london

### W05.  `T4=T4a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; session=asia  •  AVOID when HTF20 aligned WITH trade

### W06.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=102  W=91/L=11  WR=89.2%
- Refine: exclude H20=H20e drops 8/11 losers (73%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W08.  `H20=H20d AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude BBP=BBP2 drops 11/12 losers (92%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W09.  `H20=H20d AND T1=T1a AND RSI=RSI3`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude BBP=BBP2 drops 11/13 losers (85%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W10.  `H20=H20d AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=93  W=86/L=7  WR=92.5%
- Refine: exclude BBP=BBP2 drops 6/7 losers (86%)
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W11.  `RSI=RSI4 AND strategy_id=TF2_pullback_EMA20_short AND direction_exec=long`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude T1=T1c drops 7/10 losers (70%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; strategy=TF2_pullback_EMA20_short  •  AVOID when 1h trend AGAINST trade

### W12.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W13.  `T4=T4a AND BBP=BBP5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched upper band; session=asia  •  AVOID when HTF20 aligned WITH trade

### W14.  `T4=T4a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude T1=T1c drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W15.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W16.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W17.  `H20=H20a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude direction_exec=short drops 10/12 losers (83%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when short

### W18.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude direction_exec=short drops 10/12 losers (83%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when short

### W19.  `H60=H60d AND T1=T1c AND BBP=BBP4`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W20.  `T1=T1a AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H20=H20e drops 5/6 losers (83%)
- **Final: n=62  W=61/L=1  WR=98.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W21.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude ZS=ZS4 drops 8/11 losers (73%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W22.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude BBP=BBP6 drops 4/11 losers (36%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when deep above upper band

### W23.  `H60=H60d AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude session_bucket=ny_close drops 3/7 losers (43%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; upper third  •  AVOID when session=ny_close

### W24.  `T4=T4c AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20e drops 10/11 losers (91%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF20 strongly against

### W25.  `H20=H20d AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude BBP=BBP2 drops 7/7 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND ZS=ZS4`
- Raw: n=217  W=85/L=132  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=217  W=85/L=132  WR=39.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought

### L02.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=217  W=85/L=132  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=217  W=85/L=132  WR=39.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought

### L03.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=213  W=83/L=130  WR=39.0%
- Sharpen: sharpest is BBP=BBP3 (32/130 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london_open  •  ONLY when middle of band

### L04.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=155  W=60/L=95  WR=38.7%
- Sharpen: sharpest is BBP=BBP3 (21/95 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when middle of band

### L05.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=153  W=55/L=98  WR=35.9%
- Sharpen: sharpest is H60=H60e (64/98 of losers there)
- **Sharp: n=80  W=16/L=64  WR=20.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=152  W=55/L=97  WR=36.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=152  W=55/L=97  WR=36.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought

### L07.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=146  W=51/L=95  WR=34.9%
- Sharpen: sharpest is H20=H20b (16/95 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L08.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=127  W=47/L=80  WR=37.0%
- Sharpen: sharpest is H20=H20a (64/80 of losers there)
- **Sharp: n=80  W=16/L=64  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=127  W=48/L=79  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=127  W=48/L=79  WR=37.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open

### L10.  `H20=H20a AND H60=H60e AND T4=T4a AND ZS=ZS3`
- Raw: n=125  W=43/L=82  WR=34.4%
- Sharpen: sharpest is direction_exec=short (47/82 of losers there)
- **Sharp: n=61  W=14/L=47  WR=23.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when short

### L11.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: sharpest is H20=H20b (15/81 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L12.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: sharpest is H20=H20b (15/81 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L13.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is ZS=ZS3 (31/80 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L14.  `H20=H20e AND H60=H60a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=125  W=48/L=77  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (26/77 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L15.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is T4=T4a (39/72 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20a AND H60=H60e AND ZS=ZS3 AND direction_exec=short`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is RSI=RSI4 (64/69 of losers there)
- **Sharp: n=80  W=16/L=64  WR=20.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L17.  `H20=H20e AND T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: sharpest is T4=T4c (34/68 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is H60=H60e (45/69 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L19.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is session_bucket=asia (34/69 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when session=asia

### L20.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is H60=H60e (21/64 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L21.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is direction_exec=short (33/63 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when short

### L22.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (22/62 of losers there)
- **Sharp: n=29  W=7/L=22  WR=24.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=102  W=28/L=74  WR=27.5%
- Sharpen: sharpest is T1=T1a (25/74 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L24.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (33/67 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=asia

### L25.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is ZS=ZS1 (21/65 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

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
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
