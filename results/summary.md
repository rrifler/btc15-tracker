# BTC 15-min strategy tracker: FAIL

Data source: INTL_PROXY. INTL_PROXY means trades from the international exchange, used because the US gateway publishes no public trade history.
Real money needs PASS in both the backtest and the live paper run, with the live hit rate within 8 points of the backtest.

## Backtest

- Verdict: **FAIL**
- Windows scored: 700; excluded: 0
- Fill rate: 16.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 52 of 118 = 44.1% (95% range 35.4% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.35 (balance $7.65 from $20)
- Longest losing streak: 9
- Strict vs touch: strict 52/118 = 44.1%; touch 67/136 = 49.3%. The verdict uses strict.

## Live paper run

- Verdict: **FAIL**
- Windows scored: 1513; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (91 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 132/294 = 44.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-16T17:15Z (market 5746288, result down)
Scored: p1 up filled at 87s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5799999768, 3s@0.59999988, 3s@0.6, 6s@0.5599999517, 6s@0.559999832, 6s@0.559999776, 9s@0.5599999642, 11s@0.5499999918, 12s@0.5, 12s@0.5, 12s@0.5099999956, 12s@0.5245173913 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 11s@0.4602083314, 11s@0.4699999361, 11s@0.4699999962, 11s@0.47, 11s@0.469999906, 11s@0.47, 11s@0.45, 11s@0.45, 11s@0.45, 12s@0.48, 12s@0.51 ...


_Updated 2026-10-16 21:33Z_
