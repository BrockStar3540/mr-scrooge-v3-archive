# NZD_USD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,453**  (W=937 / L=516)  -  WR: **64.5%**

## Session distribution

- asia: n=439  W=277/L=162  WR=63.1%
- ny_mid: n=352  W=218/L=134  WR=61.9%
- ny_close: n=258  W=171/L=87  WR=66.3%
- ny_open: n=231  W=154/L=77  WR=66.7%
- london: n=68  W=49/L=19  WR=72.1%
- london_open: n=46  W=27/L=19  WR=58.7%
- off_hours: n=43  W=28/L=15  WR=65.1%
- asia_late: n=16  W=13/L=3  WR=81.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=131  W=112/L=19  WR=85.5%
- Refine: exclude ZS=ZS3 drops 6/19 losers (32%)
- **Final: n=123  W=110/L=13  WR=89.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W02.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=127  W=116/L=11  WR=91.3%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude BBP=BBP3 drops 3/15 losers (20%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when middle of band

### W04.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude BBP=BBP3 drops 3/15 losers (20%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when middle of band

### W05.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude BBP=BBP3 drops 3/15 losers (20%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when middle of band

### W06.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H60=H60c drops 12/15 losers (80%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W07.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H60=H60c drops 12/15 losers (80%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W08.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H60=H60c drops 12/15 losers (80%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W09.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude H60=H60c drops 8/11 losers (73%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W10.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude H60=H60c drops 8/11 losers (73%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 neutral

### W11.  `H60=H60c AND T4=T4a AND RSI=RSI2`
- Raw: n=106  W=97/L=9  WR=91.5%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_open

### W12.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude H60=H60c drops 7/10 losers (70%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF60 neutral

### W13.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude BBP=BBP3 drops 3/11 losers (27%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when middle of band

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude BBP=BBP3 drops 3/11 losers (27%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when middle of band

### W15.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude BBP=BBP3 drops 3/11 losers (27%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when middle of band

### W16.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude BBP=BBP3 drops 3/11 losers (27%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when middle of band

### W17.  `T4=T4a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude H60=H60c drops 7/10 losers (70%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF60 neutral

### W18.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude H60=H60c drops 7/10 losers (70%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF60 neutral

### W19.  `H20=H20a AND H60=H60c AND T4=T4a`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS2 drops 9/12 losers (75%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W20.  `H60=H60c AND T1=T1a AND T4=T4a`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS2 drops 9/12 losers (75%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W21.  `H60=H60c AND T4=T4a AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS2 drops 9/12 losers (75%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W22.  `H20=H20a AND H60=H60c AND T1=T1a AND T4=T4a`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS2 drops 9/12 losers (75%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W23.  `H20=H20a AND H60=H60c AND T4=T4a AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS2 drops 9/12 losers (75%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W24.  `H60=H60c AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS2 drops 9/12 losers (75%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W25.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60c drops 9/12 losers (75%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF60 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=84  W=26/L=58  WR=31.0%
- Sharpen: sharpest is RSI=RSI2 (50/58 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L02.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=84  W=26/L=58  WR=31.0%
- Sharpen: sharpest is RSI=RSI2 (50/58 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L03.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=84  W=26/L=58  WR=31.0%
- Sharpen: sharpest is RSI=RSI2 (50/58 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L04.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is T4=T4c (50/50 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L05.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is T4=T4c (50/50 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L06.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is T4=T4c (50/50 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T4=T4c (44/44 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T4=T4c (44/44 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T4=T4c (44/44 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T4=T4c (44/44 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T4=T4c (44/44 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4a (32/41 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4a (32/41 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4a (32/41 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L15.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=66  W=12/L=54  WR=18.2%
- Sharpen: sharpest is BBP=BBP2 (38/54 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L16.  `H20=H20e AND H60=H60c AND T4=T4c`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is RSI=RSI2 (42/43 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L17.  `H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is RSI=RSI2 (42/43 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L18.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is RSI=RSI2 (42/43 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L19.  `H20=H20e AND H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is RSI=RSI2 (42/43 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20e AND H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is RSI=RSI2 (42/43 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L21.  `H60=H60c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is RSI=RSI2 (42/43 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L22.  `T1=T1c AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (36/40 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  ONLY when RSI 30-40 weak

### L23.  `ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (36/40 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=ny_open  •  ONLY when RSI 30-40 weak

### L24.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (36/40 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  ONLY when RSI 30-40 weak

### L25.  `T1=T1c AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (36/40 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(46/37) | H60a(37/47) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
