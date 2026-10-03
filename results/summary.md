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
- Windows scored: 189; excluded: 0
- Fill rate: 21.7% of scored windows had a fill (0 too small)
- Fills that reached 45c: 18 of 41 = 43.9% (95% range 29.9% to 59.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.45 (balance $13.55 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 18/41 = 43.9%; touch 21/45 = 46.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-02T18:15Z (market 5187216, result down)
Scored: p1 up filled at 74s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 5s@0.5199999992, 5s@0.52, 6s@0.5299999868, 8s@0.5299999747, 8s@0.51, 14s@0.48, 17s@0.4899999984, 17s@0.4851484889, 32s@0.4799998464, 33s@0.48, 33s@0.4799998464 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.5, 3s@0.5, 5s@0.49, 6s@0.5299999868, 6s@0.52, 6s@0.51, 11s@0.5, 12s@0.5278353469, 15s@0.5299999685, 18s@0.52, 23s@0.5213114737 ...

### 2026-10-02T19:15Z (market 5190984, result up)
Scored: p1 up filled at 89s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.517412932, 3s@0.5099999949, 3s@0.5199999792, 3s@0.51, 5s@0.5299998463, 5s@0.5299998463, 5s@0.5299999868, 6s@0.5299998463, 8s@0.5099998215, 8s@0.5099999442, 8s@0.53, 8s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.5, 3s@0.5, 5s@0.4799999616, 8s@0.48, 9s@0.5, 11s@0.46, 23s@0.48, 23s@0.46, 24s@0.48, 26s@0.4799998464, 26s@0.469999906 ...

### 2026-10-02T20:00Z (market 5191991, result up)
Scored: p1 down filled at 98s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.56, 3s@0.5375609756, 5s@0.5699999998, 5s@0.57, 5s@0.56, 5s@0.57, 5s@0.57, 5s@0.57, 5s@0.57, 6s@0.57, 6s@0.57, 11s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4925, 2s@0.5, 3s@0.47, 3s@0.47, 98s@0.2399999808, 101s@0.2399999923, 107s@0.24, 128s@0.23, 128s@0.22, 152s@0.23, 158s@0.25, 281s@0.24 ...

### 2026-10-02T20:45Z (market 5192816, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 5s@0.5299999797, 5s@0.5399999568, 5s@0.5399999568, 5s@0.5299999868, 5s@0.5299998463, 6s@0.5399999568, 8s@0.539999811, 8s@0.54, 11s@0.54, 12s@0.54, 12s@0.54 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4799998464, 6s@0.4699999674, 6s@0.46, 6s@0.4699999674, 8s@0.4699999674, 8s@0.4699999674, 9s@0.4699999674, 29s@0.45, 30s@0.4799998464, 38s@0.4799999616, 44s@0.48, 44s@0.48 ...


_Updated 2026-10-03 00:30Z_
