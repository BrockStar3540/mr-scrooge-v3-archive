# NZD_USD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **771**  (W=498 / L=273)  -  WR: **64.6%**

## Session distribution

- asia: n=285  W=183/L=102  WR=64.2%
- london_open: n=150  W=96/L=54  WR=64.0%
- london: n=133  W=93/L=40  WR=69.9%
- asia_late: n=65  W=43/L=22  WR=66.2%
- ny_close: n=60  W=33/L=27  WR=55.0%
- ny_open: n=38  W=25/L=13  WR=65.8%
- off_hours: n=24  W=16/L=8  WR=66.7%
- ny_mid: n=16  W=9/L=7  WR=56.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude ZS=ZS3 drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W02.  `H20=H20a AND H60=H60e AND session_bucket=asia`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude BBP=BBP4 drops 7/8 losers (88%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=asia  •  AVOID when upper third

### W03.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude ZS=ZS3 drops 7/9 losers (78%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude BBP=BBP4 drops 7/11 losers (64%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia  •  AVOID when upper third

### W05.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when HTF20 slightly aligned

### W06.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude T4=T4c drops 10/10 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W07.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude BBP=BBP4 drops 7/8 losers (88%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when upper third

### W08.  `H20=H20a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude T4=T4a drops 5/5 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude BBP=BBP4 drops 7/7 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=asia  •  AVOID when upper third

### W10.  `T1=T1c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  AVOID when HTF60 aligned WITH trade

### W11.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=57  W=56/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=asia

### W12.  `H20=H20a AND T1=T1c AND session_bucket=london`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london  •  AVOID when 4h trend WITH trade

### W13.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W14.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=54  W=50/L=4  WR=92.6%
- Refine: exclude BBP=BBP4 drops 4/4 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  AVOID when upper third

### W15.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude BBP=BBP3 drops 5/6 losers (83%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when middle of band

### W16.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=53  W=51/L=2  WR=96.2%
- Refine: exclude strategy_id=charlie_compression_breakout drops 2/2 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when strategy=charlie_compression_breakout

### W17.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20a AND T4=T4c AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP5 drops 3/3 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when just touched upper band

### W19.  `T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W20.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W21.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W22.  `T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=50  W=46/L=4  WR=92.0%
- Refine: exclude H20=H20b drops 4/4 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when HTF20 slightly aligned

### W24.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W25.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is H20=H20d (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 mildly against

### L02.  `H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is T4=T4a (21/38 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is T1=T1a (17/31 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L04.  `H60=H60d AND T1=T1c AND T4=T4a`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H20=H20e (12/28 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L05.  `H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H20=H20e (12/28 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L06.  `H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H20=H20e (12/28 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L07.  `H60=H60d AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H20=H20e (12/28 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L08.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=45  W=9/L=36  WR=20.0%
- Sharpen: sharpest is direction_exec=short (21/36 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when short

### L09.  `H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is T4=T4c (21/26 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is T4=T4c (18/25 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when 4h trend AGAINST trade

### L11.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is H60=H60a (15/24 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L12.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=38  W=9/L=29  WR=23.7%
- Sharpen: sharpest is direction_exec=short (18/29 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when short

### L13.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=38  W=12/L=26  WR=31.6%
- Sharpen: sharpest is H60=H60d (10/26 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L14.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=38  W=12/L=26  WR=31.6%
- Sharpen: sharpest is H60=H60d (10/26 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=38  W=12/L=26  WR=31.6%
- Sharpen: sharpest is H60=H60d (10/26 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L16.  `H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=36  W=7/L=29  WR=19.4%
- Sharpen: sharpest is H20=H20d (8/29 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when HTF20 mildly against

### L17.  `T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=34  W=8/L=26  WR=23.5%
- Sharpen: sharpest is T1=T1a (16/26 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when 1h trend WITH trade

### L18.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is H60=H60a (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L19.  `T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is H20=H20e (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 strongly against

### L20.  `T1=T1a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=33  W=13/L=20  WR=39.4%
- Sharpen: sharpest is T4=T4a (16/20 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L21.  `ZS=ZS5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=33  W=13/L=20  WR=39.4%
- Sharpen: sharpest is T4=T4a (16/20 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L22.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=33  W=13/L=20  WR=39.4%
- Sharpen: sharpest is T4=T4a (16/20 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L23.  `T1=T1a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=32  W=12/L=20  WR=37.5%
- Sharpen: sharpest is H20=H20e (18/20 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london  •  ONLY when HTF20 strongly against

### L24.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=31  W=7/L=24  WR=22.6%
- Sharpen: sharpest is H20=H20d (10/24 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia  •  ONLY when HTF20 mildly against

### L25.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is H60=H60d (6/21 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when HTF60 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/32) | H20e(32/42), H20d(7/15) |
| H60 | H60e(45/30) | H60a(33/44), H60d(7/12) |
| T1 | — | — |
| T4 | T4c(58/41) | T4a(42/59) |
| BBP | — | BBP3(12/18) |
| RSI | — | — |
| ZS | — | ZS3(18/26) |
| strategy_id | — | — |
| direction_exec | long(58/46) | short(42/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
