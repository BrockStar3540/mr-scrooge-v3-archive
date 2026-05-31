# EUR_CHF — R34 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **285**  (W=181 / L=104)  -  WR: **63.5%**

## Session distribution

- ny_close: n=153  W=95/L=58  WR=62.1%
- asia: n=75  W=49/L=26  WR=65.3%
- london: n=17  W=12/L=5  WR=70.6%
- asia_late: n=12  W=8/L=4  WR=66.7%
- london_open: n=12  W=8/L=4  WR=66.7%
- off_hours: n=10  W=4/L=6  WR=40.0%
- ny_open: n=6  W=5/L=1  WR=83.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W03.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=50  W=50/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade

### W05.  `H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=50  W=50/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade

### W06.  `T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=50  W=50/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade

### W07.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=50  W=50/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade

### W08.  `H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=40  W=40/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close

### W09.  `T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=40  W=40/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_close

### W10.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=40  W=40/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close

### W11.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=40  W=40/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close

### W12.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=40  W=40/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close

### W13.  `H60=H60a AND T1=T1c AND ZS=ZS3`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W16.  `T1=T1c AND T4=T4c AND ZS=ZS3`
- Raw: n=35  W=30/L=5  WR=85.7%
- Refine: exclude direction_exec=long drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when long

### W17.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=32  W=29/L=3  WR=90.6%
- Refine: exclude direction_exec=long drops 3/3 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when long

### W18.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=32  W=29/L=3  WR=90.6%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W19.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=30  W=30/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade

### W20.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=30  W=30/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade

### W21.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=30  W=30/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade

### W22.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=30  W=30/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade

### W23.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=30  W=30/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade

### W24.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=30  W=30/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade

### W25.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=30  W=30/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L02.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L03.  `H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L04.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L07.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=42  W=10/L=32  WR=23.8%
- Sharpen: sharpest is H60=H60e (20/32 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 strongly against

### L08.  `H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is T4=T4a (20/25 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L09.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is T4=T4a (20/25 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is T4=T4a (20/25 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L11.  `H20=H20a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=34  W=10/L=24  WR=29.4%
- Sharpen: sharpest is H60=H60e (12/24 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when HTF60 strongly against

### L12.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=34  W=10/L=24  WR=29.4%
- Sharpen: sharpest is H60=H60e (12/24 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 strongly against

### L13.  `H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=32  W=12/L=20  WR=37.5%
- Sharpen: sharpest is T4=T4a (13/20 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; upper third  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60e AND ZS=ZS3 AND direction_exec=long`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is T4=T4a (11/19 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(51/36) | H20a(33/47) |
| H60 | H60a(58/25) | H60e(24/58) |
| T1 | T1c(61/46) | T1a(39/54) |
| T4 | T4c(67/38) | T4a(33/62) |
| BBP | BBP2(35/27) | BBP4(25/31) |
| RSI | — | — |
| ZS | ZS2(27/18) | — |
| strategy_id | — | — |
| direction_exec | short(60/35) | long(40/65) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
