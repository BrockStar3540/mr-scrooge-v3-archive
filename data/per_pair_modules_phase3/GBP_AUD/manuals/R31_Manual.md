# GBP_AUD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **6,810**  (W=3,889 / L=2,921)  -  WR: **57.1%**

## Session distribution

- asia: n=2185  W=1233/L=952  WR=56.4%
- ny_close: n=1260  W=779/L=481  WR=61.8%
- ny_mid: n=1213  W=669/L=544  WR=55.2%
- london_open: n=708  W=383/L=325  WR=54.1%
- ny_open: n=617  W=357/L=260  WR=57.9%
- london: n=486  W=279/L=207  WR=57.4%
- off_hours: n=197  W=109/L=88  WR=55.3%
- asia_late: n=144  W=80/L=64  WR=55.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W02.  `H60=H60e AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W03.  `T1=T1c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W04.  `T4=T4c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W05.  `ZS=ZS1 AND direction_exec=long AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W06.  `H20=H20e AND H60=H60e AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W07.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W08.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W09.  `H20=H20e AND ZS=ZS1 AND direction_exec=long AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W10.  `H60=H60e AND T1=T1c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W11.  `H60=H60e AND T4=T4c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W12.  `H60=H60e AND ZS=ZS1 AND direction_exec=long AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W13.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W14.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W15.  `T4=T4c AND ZS=ZS1 AND direction_exec=long AND session_bucket=london`
- Raw: n=51  W=48/L=3  WR=94.1%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W16.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=london`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W17.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=london`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W18.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=london`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W19.  `T4=T4a AND RSI=RSI3 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude H20=H20e drops 3/3 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W20.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=london`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W21.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long AND session_bucket=london`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold; session=london  •  AVOID when just touched lower band

### W22.  `T4=T4a AND BBP=BBP1 AND session_bucket=ny_open`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 2/6 losers (33%)
- **Final: n=35  W=31/L=4  WR=88.6%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; session=ny_open  •  AVOID when strategy=BR2_vcb_short

### W23.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 2/6 losers (33%)
- **Final: n=35  W=31/L=4  WR=88.6%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when strategy=BR2_vcb_short

### W24.  `H20=H20a AND RSI=RSI1 AND ZS=ZS0`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude H60=H60e drops 3/3 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore <-3 extreme  •  AVOID when HTF60 strongly against

### W25.  `H60=H60a AND RSI=RSI1 AND ZS=ZS0`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude H20=H20e drops 3/3 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore <-3 extreme  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=310  W=124/L=186  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (54/186 of losers there)
- **Sharp: n=59  W=5/L=54  WR=8.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when deep below lower band

### L02.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=310  W=124/L=186  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (54/186 of losers there)
- **Sharp: n=59  W=5/L=54  WR=8.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when deep below lower band

### L03.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=310  W=124/L=186  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (54/186 of losers there)
- **Sharp: n=59  W=5/L=54  WR=8.5%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  ONLY when deep below lower band

### L04.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=310  W=124/L=186  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (54/186 of losers there)
- **Sharp: n=59  W=5/L=54  WR=8.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when deep below lower band

### L05.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=310  W=124/L=186  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (54/186 of losers there)
- **Sharp: n=59  W=5/L=54  WR=8.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when deep below lower band

### L06.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=310  W=124/L=186  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (54/186 of losers there)
- **Sharp: n=59  W=5/L=54  WR=8.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when deep below lower band

### L07.  `H60=H60e AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 20-30 oversold

### L08.  `T1=T1c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 20-30 oversold

### L09.  `T4=T4c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold

### L10.  `BBP=BBP1 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: LONG**  •  just touched lower band; RSI 20-30 oversold

### L11.  `H60=H60e AND T1=T1c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band; RSI 20-30 oversold

### L12.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold

### L13.  `H60=H60e AND BBP=BBP1 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold

### L14.  `H60=H60e AND BBP=BBP1 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: LONG**  •  HTF60 strongly against; just touched lower band; RSI 20-30 oversold

### L15.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold

### L16.  `T1=T1c AND BBP=BBP1 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold

### L17.  `T1=T1c AND BBP=BBP1 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band; RSI 20-30 oversold

### L18.  `T4=T4c AND BBP=BBP1 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold

### L19.  `T4=T4c AND BBP=BBP1 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold

### L20.  `BBP=BBP1 AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=56/L=91  WR=38.1%**
- **Dir: LONG**  •  just touched lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold

### L21.  `H60=H60e AND RSI=RSI1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is H20=H20a (14/86 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L22.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is H20=H20a (14/86 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L23.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is H20=H20a (14/86 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L24.  `RSI=RSI1 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is H20=H20a (14/86 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L25.  `H20=H20e AND T4=T4a AND ZS=ZS2`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/87 of losers there)
- **Sharp: n=43  W=11/L=32  WR=25.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/45) | H20e(46/53) |
| H60 | H60a(52/46) | H60e(48/54) |
| T1 | — | — |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/46) | long(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
