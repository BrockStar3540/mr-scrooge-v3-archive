# NZD_CHF — R25 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **832**  (W=516 / L=316)  -  WR: **62.0%**

## Session distribution

- ny_mid: n=250  W=159/L=91  WR=63.6%
- asia: n=196  W=123/L=73  WR=62.8%
- ny_close: n=119  W=74/L=45  WR=62.2%
- london_open: n=112  W=68/L=44  WR=60.7%
- ny_open: n=76  W=44/L=32  WR=57.9%
- london: n=62  W=36/L=26  WR=58.1%
- off_hours: n=17  W=12/L=5  WR=70.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND BBP=BBP2`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=ny_close drops 4/8 losers (50%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  AVOID when session=ny_close

### W02.  `H20=H20e AND H60=H60e AND ZS=ZS2`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 4/8 losers (50%)
- **Final: n=45  W=41/L=4  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W03.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 4/8 losers (50%)
- **Final: n=45  W=41/L=4  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W04.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=ny_close

### W05.  `H20=H20e AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=50  W=48/L=2  WR=96.0%
- Refine: exclude H60=H60e drops 2/2 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF60 strongly against

### W06.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=49  W=43/L=6  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W07.  `H20=H20e AND T4=T4c AND RSI=RSI1`
- Raw: n=48  W=43/L=5  WR=89.6%
- Refine: exclude BBP=BBP1 drops 3/5 losers (60%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when just touched lower band

### W08.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude BBP=BBP1 drops 4/6 losers (67%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when just touched lower band

### W09.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=33  W=31/L=2  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  AVOID when session=ny_close

### W10.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=33  W=31/L=2  WR=93.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  AVOID when session=ny_close

### W11.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=46  W=40/L=6  WR=87.0%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; RSI 30-40 weak  •  AVOID when session=ny_close

### W12.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=45  W=39/L=6  WR=86.7%
- Refine: exclude H60=H60a drops 4/6 losers (67%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF60 aligned WITH trade

### W13.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=44  W=40/L=4  WR=90.9%
- Refine: exclude BBP=BBP1 drops 3/4 losers (75%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  AVOID when just touched lower band

### W14.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20a AND H60=H60a AND T4=T4c`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude BBP=BBP2 drops 3/6 losers (50%)
- **Final: n=38  W=35/L=3  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W16.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS2`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=29  W=27/L=2  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W17.  `H20=H20e AND H60=H60e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=29  W=27/L=2  WR=93.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W18.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude session_bucket=ny_close drops 4/6 losers (67%)
- **Final: n=26  W=24/L=2  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W19.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude BBP=BBP4 drops 2/4 losers (50%)
- **Final: n=35  W=33/L=2  WR=94.3%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when upper third

### W20.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude BBP=BBP4 drops 2/4 losers (50%)
- **Final: n=35  W=33/L=2  WR=94.3%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when upper third

### W21.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude BBP=BBP4 drops 2/4 losers (50%)
- **Final: n=35  W=33/L=2  WR=94.3%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when upper third

### W22.  `H20=H20e AND H60=H60e AND ZS=ZS3`
- Raw: n=39  W=34/L=5  WR=87.2%
- Refine: exclude T4=T4a drops 4/5 losers (80%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W23.  `H60=H60e AND T4=T4c AND ZS=ZS3`
- Raw: n=39  W=34/L=5  WR=87.2%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W24.  `H20=H20e AND T1=T1a AND BBP=BBP0`
- Raw: n=38  W=35/L=3  WR=92.1%
- Refine: exclude RSI=RSI2 drops 3/3 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W25.  `H20=H20e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=38  W=35/L=3  WR=92.1%
- Refine: exclude RSI=RSI2 drops 3/3 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; deep below lower band  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is BBP=BBP0 (16/44 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L02.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is BBP=BBP0 (16/44 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when deep below lower band

### L03.  `H20=H20a AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is BBP=BBP0 (16/44 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L04.  `H20=H20a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is BBP=BBP0 (12/39 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L05.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is BBP=BBP0 (7/37 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_mid  •  ONLY when deep below lower band

### L06.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is BBP=BBP0 (14/36 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L07.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is BBP=BBP0 (14/36 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L08.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is BBP=BBP0 (14/36 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L09.  `H20=H20b AND H60=H60c AND RSI=RSI2`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is ZS=ZS1 (13/29 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 neutral; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=46  W=14/L=32  WR=30.4%
- Sharpen: sharpest is H20=H20a (13/32 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20a AND T4=T4a AND BBP=BBP2`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is RSI=RSI1 (6/29 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L12.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (19/27 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L13.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (19/27 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (19/27 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L15.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (19/27 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (19/27 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L17.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is T4=T4a (10/27 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND H60=H60a AND BBP=BBP2`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI1 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L19.  `H20=H20a AND T4=T4a AND ZS=ZS2`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is RSI=RSI1 (6/26 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L20.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is RSI=RSI1 (6/26 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L21.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=40  W=13/L=27  WR=32.5%
- Sharpen: sharpest is H20=H20a (13/27 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L22.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=40  W=13/L=27  WR=32.5%
- Sharpen: sharpest is H20=H20a (13/27 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=40  W=13/L=27  WR=32.5%
- Sharpen: sharpest is H20=H20a (13/27 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L24.  `H20=H20a AND H60=H60a AND ZS=ZS2`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is RSI=RSI1 (6/25 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L25.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is RSI=RSI1 (6/25 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 20-30 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(47/32) | H20a(34/46) |
| H60 | H60d(7/2) | — |
| T1 | T1c(56/45) | T1a(44/55) |
| T4 | T4c(59/41) | T4a(41/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/45) | short(44/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
