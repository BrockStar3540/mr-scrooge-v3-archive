# EUR_NZD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,623**  (W=2,211 / L=1,412)  -  WR: **61.0%**

## Session distribution

- asia: n=1257  W=769/L=488  WR=61.2%
- london_open: n=663  W=409/L=254  WR=61.7%
- ny_mid: n=527  W=329/L=198  WR=62.4%
- ny_open: n=397  W=261/L=136  WR=65.7%
- ny_close: n=331  W=189/L=142  WR=57.1%
- asia_late: n=248  W=140/L=108  WR=56.5%
- london: n=123  W=74/L=49  WR=60.2%
- off_hours: n=77  W=40/L=37  WR=51.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=221  W=193/L=28  WR=87.3%
- Refine: exclude H20=H20a drops 22/28 losers (79%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=221  W=193/L=28  WR=87.3%
- Refine: exclude H20=H20a drops 22/28 losers (79%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=221  W=193/L=28  WR=87.3%
- Refine: exclude H20=H20a drops 22/28 losers (79%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=221  W=193/L=28  WR=87.3%
- Refine: exclude H20=H20a drops 22/28 losers (79%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W05.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H20=H20a drops 16/21 losers (76%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W06.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H20=H20a drops 16/21 losers (76%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W07.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H20=H20a drops 16/21 losers (76%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H20=H20a drops 16/21 losers (76%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H20=H20a drops 16/21 losers (76%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H20=H20a drops 16/21 losers (76%)
- **Final: n=99  W=94/L=5  WR=94.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W12.  `H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W13.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W14.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W15.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W16.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W17.  `H20=H20a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W18.  `T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W19.  `T4=T4a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W20.  `RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W21.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W22.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W23.  `H20=H20a AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

### W25.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS0 drops 4/15 losers (27%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when zscore <-3 extreme

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: sharpest is H20=H20d (27/108 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 mildly against

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: sharpest is H20=H20d (27/108 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 mildly against

### L03.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: sharpest is H20=H20d (27/108 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 mildly against

### L04.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: sharpest is H20=H20d (27/108 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 mildly against

### L05.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is H20=H20d (22/78 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L06.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is H20=H20d (22/78 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L07.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is H20=H20d (22/78 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is H20=H20d (22/78 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L09.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is H20=H20d (22/78 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L10.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is H20=H20d (22/78 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L11.  `H20=H20e AND H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=111  W=39/L=72  WR=35.1%
- Sharpen: sharpest is session_bucket=asia (57/72 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=asia

### L12.  `H20=H20e AND H60=H60e AND BBP=BBP0`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS0 (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band  •  ONLY when zscore <-3 extreme

### L13.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP0`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS0 (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L14.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS0 (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L15.  `H20=H20e AND H60=H60e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS0 (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band  •  ONLY when zscore <-3 extreme

### L16.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS0 (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L17.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS0 (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L18.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is H20=H20e (57/66 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF20 strongly against

### L19.  `H20=H20e AND H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is session_bucket=asia (54/69 of losers there)
- **Sharp: n=77  W=23/L=54  WR=29.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when session=asia

### L20.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is session_bucket=asia (54/69 of losers there)
- **Sharp: n=77  W=23/L=54  WR=29.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  ONLY when session=asia

### L21.  `H20=H20e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=41/L=67  WR=38.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=asia

### L22.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=41/L=67  WR=38.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia

### L23.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=41/L=67  WR=38.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia

### L24.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=41/L=67  WR=38.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia

### L25.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=41/L=67  WR=38.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/29) | H20e(30/45) |
| H60 | H60a(40/32) | H60e(34/44) |
| T1 | T1a(56/43) | T1c(44/57) |
| T4 | T4a(55/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(57/42) | long(43/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
