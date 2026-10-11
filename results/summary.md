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
- Windows scored: 1037; excluded: 0
- Fill rate: 16.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 75 of 168 = 44.6% (95% range 37.3% to 52.2%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-14.65 (balance $5.35 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 75/168 = 44.6%; touch 83/182 = 45.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-11T16:00Z (market 5506811, result down)
Scored: p1 up filled at 88s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 4s@0.47, 4s@0.47, 4s@0.46, 4s@0.46, 4s@0.45, 4s@0.45, 4s@0.45, 6s@0.5091137009, 6s@0.5, 6s@0.4873086667, 6s@0.4903913883 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999873, 4s@0.549999945, 4s@0.549999945, 4s@0.55, 4s@0.5599999328, 7s@0.5, 7s@0.4832347035, 7s@0.5, 7s@0.4699999953, 9s@0.4699999896, 9s@0.46, 9s@0.46 ...

### 2026-10-11T17:00Z (market 5509704, result down)
Scored: p1 up filled at 37s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 33s@0.25, 37s@0.24, 40s@0.2399999979, 40s@0.24, 42s@0.25, 46s@0.239999962, 48s@0.239999962, 49s@0.24, 49s@0.24, 49s@0.2399999921, 51s@0.2099999996, 51s@0.2099999987 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 3s@0.5899999145, 3s@0.5899999201, 4s@0.6, 4s@0.5952380952, 7s@0.61, 10s@0.6142857143, 10s@0.64, 10s@0.63, 12s@0.629999995, 12s@0.64125, 13s@0.66 ...

### 2026-10-11T17:15Z (market 5510312, result up)
Scored: p1 down filled at 105s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 4s@0.55, 9s@0.5619263416, 13s@0.52, 13s@0.52, 16s@0.52, 18s@0.52, 18s@0.53, 18s@0.5299999868, 18s@0.5299999587, 21s@0.5479166667, 22s@0.5725957416 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.4899999824, 105s@0.2399999726, 106s@0.24, 106s@0.24, 108s@0.23, 109s@0.24, 112s@0.25, 112s@0.25, 112s@0.25, 112s@0.25, 132s@0.21, 136s@0.2178217628 ...

### 2026-10-11T18:45Z (market 5516333, result down)
Scored: p1 up filled at 43s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 43s@0.19, 43s@0.19, 45s@0.1899999962, 46s@0.16, 46s@0.16, 46s@0.16, 46s@0.16, 46s@0.16, 48s@0.16, 48s@0.16, 49s@0.12, 49s@0.15 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.648, 0s@0.6299999969, 0s@0.63, 3s@0.6699999667, 3s@0.6699999848, 3s@0.6699999976, 6s@0.6699999196, 6s@0.659999991, 7s@0.67, 7s@0.6699999483, 7s@0.6699999823, 7s@0.6699999951 ...

### 2026-10-11T21:15Z (market 5522576, result down)
Scored: p1 up filled at 8s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.45, 4s@0.469999906, 4s@0.47, 4s@0.469999906, 4s@0.469999906, 8s@0.22, 8s@0.2199999844, 8s@0.22, 8s@0.2199999976, 8s@0.22, 8s@0.2199999974 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4913232007, 2s@0.549999945, 2s@0.49, 2s@0.4899999944, 4s@0.62, 4s@0.64, 4s@0.63, 4s@0.6299999496, 4s@0.6299999592, 4s@0.64, 5s@0.7, 5s@0.71 ...


_Updated 2026-10-11 22:24Z_
