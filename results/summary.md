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
- Windows scored: 1310; excluded: 0
- Fill rate: 17.4% of scored windows had a fill (54 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 116/253 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-14T12:30Z (market 5647869, result down)
Scored: p1 up filled at 8s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.51, 0s@0.5199999358, 3s@0.55, 3s@0.67, 3s@0.53, 3s@0.55, 3s@0.5299999998, 3s@0.53, 6s@0.62, 6s@0.53, 6s@0.62, 8s@0.2399999928 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4849794923, 6s@0.77, 6s@0.55, 6s@0.7326583333, 6s@0.76, 6s@0.606, 6s@0.7493333333, 8s@0.7633333333, 8s@0.55, 8s@0.6638, 8s@0.76, 9s@0.7831106002 ...

### 2026-10-14T13:30Z (market 5648814, result up)
Scored: p1 down filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.554, 5s@0.54, 5s@0.54, 6s@0.54, 6s@0.55, 6s@0.54, 8s@0.54, 8s@0.54, 9s@0.5499999943, 9s@0.5499999214, 9s@0.5499999214, 15s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.45, 2s@0.4599999992, 2s@0.4502101584, 2s@0.4599999992, 3s@0.46, 5s@0.47, 5s@0.47, 5s@0.4699999899, 6s@0.4599999987, 6s@0.4599999687, 8s@0.4599999801, 12s@0.45 ...

### 2026-10-14T15:15Z (market 5651007, result up)
Scored: p1 down filled at 46s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.549999945, 4s@0.55, 7s@0.5399999568, 7s@0.54, 7s@0.54, 10s@0.5399999773, 10s@0.54, 12s@0.54, 12s@0.5499999325, 15s@0.55, 19s@0.559999776, 21s@0.5607917931 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.47, 4s@0.4621972111, 4s@0.4599999828, 4s@0.4599999914, 6s@0.4699999962, 6s@0.469999998, 15s@0.46, 15s@0.46, 15s@0.4599999878, 16s@0.45, 46s@0.23, 46s@0.2299999914 ...

### 2026-10-14T17:30Z (market 5662896, result down)
Scored: p1 down filled at 36s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.575, 4s@0.61, 6s@0.67, 6s@0.6699999818, 6s@0.6699999926, 6s@0.63, 6s@0.62, 7s@0.6775137753, 7s@0.6699999823, 7s@0.67, 7s@0.67, 10s@0.6999999606 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 36s@0.2099999895, 36s@0.21, 42s@0.2099999895, 43s@0.23, 43s@0.22, 43s@0.21, 43s@0.2099999895, 45s@0.25, 45s@0.25, 45s@0.2303999705, 49s@0.22, 51s@0.24 ...


_Updated 2026-10-14 18:43Z_
