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

- Verdict: **NOT ENOUGH DATA**
- Windows scored: 209; excluded: 0
- Fill rate: 21.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 19 of 44 = 43.2% (95% range 29.7% to 57.8%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-7.05 (balance $12.95 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 19/44 = 43.2%; touch 22/48 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-03T01:15Z (market 5195896, result down)
Scored: p1 down filled at 75s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5799999882, 12s@0.63, 12s@0.63, 12s@0.6199999587, 12s@0.59, 21s@0.6599999938, 23s@0.6645972152, 24s@0.6799998912, 32s@0.6799999767, 44s@0.7099999992, 44s@0.699999993, 45s@0.7099998509 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 74s@0.25, 75s@0.2299999517, 80s@0.21, 80s@0.2, 80s@0.219999978, 87s@0.22, 87s@0.22, 93s@0.229999994, 96s@0.23, 119s@0.2, 122s@0.2099999983, 134s@0.19 ...

### 2026-10-03T03:15Z (market 5196890, result up)
Scored: p1 down filled at 62s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 5s@0.5199999792, 5s@0.5199999792, 6s@0.5199999792, 6s@0.52, 6s@0.5199999792, 6s@0.5199999684, 6s@0.52, 8s@0.52, 8s@0.5299999868, 9s@0.5299998463, 11s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.47, 3s@0.481731891, 5s@0.4899998383, 8s@0.48, 9s@0.48, 20s@0.48, 27s@0.4799998464, 32s@0.4799999616, 62s@0.1799999969, 63s@0.18, 65s@0.16, 71s@0.1399999934 ...

### 2026-10-03T04:15Z (market 5197194, result down)
Scored: p1 up filled at 72s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5099999946, 8s@0.5, 8s@0.51, 72s@0.22, 72s@0.22, 72s@0.22, 72s@0.22, 72s@0.2266666667, 74s@0.22, 74s@0.22, 77s@0.16, 81s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.4899999491, 18s@0.5199999971, 18s@0.5199998921, 18s@0.5199999929, 18s@0.5088953328, 24s@0.5299999587, 33s@0.5299999229, 38s@0.5299998463, 39s@0.53, 41s@0.57, 41s@0.56, 41s@0.5495833333 ...


_Updated 2026-10-03 05:30Z_
