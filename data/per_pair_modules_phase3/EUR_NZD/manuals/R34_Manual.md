# EUR_NZD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,750**  (W=2,197 / L=1,553)  -  WR: **58.6%**

## Session distribution

- asia: n=1594  W=943/L=651  WR=59.2%
- ny_close: n=807  W=478/L=329  WR=59.2%
- ny_open: n=476  W=285/L=191  WR=59.9%
- london: n=294  W=157/L=137  WR=53.4%
- off_hours: n=184  W=99/L=85  WR=53.8%
- asia_late: n=183  W=110/L=73  WR=60.1%
- london_open: n=158  W=91/L=67  WR=57.6%
- ny_mid: n=54  W=34/L=20  WR=63.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=110  W=98/L=12  WR=89.1%
- Refine: exclude session_bucket=ny_close drops 9/12 losers (75%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W02.  `H20=H20a AND T1=T1a AND ZS=ZS3`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude session_bucket=ny_close drops 9/14 losers (64%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W03.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude session_bucket=ny_close drops 9/12 losers (75%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W04.  `H20=H20a AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=96  W=87/L=9  WR=90.6%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W05.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude session_bucket=ny_close drops 9/11 losers (82%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W06.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60a drops 7/13 losers (54%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 aligned WITH trade

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude ZS=ZS4 drops 9/9 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude ZS=ZS4 drops 9/9 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W09.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=asia

### W10.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude ZS=ZS4 drops 9/9 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W11.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude T4=T4c drops 7/7 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W12.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_open  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND H60=H60e AND session_bucket=ny_open`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude BBP=BBP6 drops 8/11 losers (73%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_open  •  AVOID when deep above upper band

### W14.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 strongly against

### W15.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 strongly against

### W16.  `H20=H20a AND T1=T1a AND BBP=BBP3`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude direction_exec=short drops 4/7 losers (57%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; middle of band  •  AVOID when short

### W17.  `H20=H20a AND T1=T1a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude direction_exec=short drops 4/7 losers (57%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when short

### W18.  `H20=H20a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/5 losers (40%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; middle of band  •  AVOID when strategy=bravo_failed_momentum

### W19.  `H20=H20a AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/5 losers (40%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when strategy=bravo_failed_momentum

### W20.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude T4=T4c drops 7/7 losers (100%)
- **Final: n=17  W=17/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20a AND T1=T1a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=67  W=64/L=3  WR=95.5%
- Refine: exclude session_bucket=ny_close drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; middle of band  •  AVOID when session=ny_close

### W22.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude T4=T4c drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W23.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF20 strongly against

### W24.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; session=ny_open  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=597  W=235/L=362  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=597  W=235/L=362  WR=39.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L02.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=505  W=201/L=304  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=505  W=201/L=304  WR=39.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third

### L03.  `T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=499  W=196/L=303  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=499  W=196/L=303  WR=39.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought

### L04.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=499  W=196/L=303  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=499  W=196/L=303  WR=39.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L05.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=463  W=180/L=283  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=463  W=180/L=283  WR=38.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L06.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=463  W=180/L=283  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=463  W=180/L=283  WR=38.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L07.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=455  W=180/L=275  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=455  W=180/L=275  WR=39.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L08.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=423  W=163/L=260  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=423  W=163/L=260  WR=38.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong

### L09.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=421  W=161/L=260  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=421  W=161/L=260  WR=38.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L10.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=421  W=161/L=260  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=421  W=161/L=260  WR=38.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong

### L11.  `H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=408  W=156/L=252  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=408  W=156/L=252  WR=38.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L12.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=408  W=156/L=252  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=408  W=156/L=252  WR=38.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L13.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=408  W=156/L=252  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=408  W=156/L=252  WR=38.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L14.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=364  W=140/L=224  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=364  W=140/L=224  WR=38.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L15.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=261  W=102/L=159  WR=39.1%
- Sharpen: sharpest is ZS=ZS5 (38/159 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=258  W=98/L=160  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=258  W=98/L=160  WR=38.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong

### L17.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=258  W=98/L=160  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=258  W=98/L=160  WR=38.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought

### L19.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=245  W=96/L=149  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=96/L=149  WR=39.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought

### L20.  `H20=H20e AND H60=H60a AND RSI=RSI5`
- Raw: n=225  W=82/L=143  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_close (56/143 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L21.  `H20=H20a AND T4=T4c AND BBP=BBP4`
- Raw: n=219  W=86/L=133  WR=39.3%
- Sharpen: sharpest is session_bucket=off_hours (25/133 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=off_hours

### L22.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=218  W=84/L=134  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (32/134 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=218  W=84/L=134  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (32/134 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=218  W=84/L=134  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (32/134 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=218  W=84/L=134  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (32/134 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/39) | — |
| H60 | H60e(52/41) | H60a(42/52) |
| T1 | T1a(56/44) | T1c(44/56) |
| T4 | T4a(59/40) | T4c(40/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/45) | short(45/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
