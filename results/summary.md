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
- Windows scored: 197; excluded: 0
- Fill rate: 21.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 19 of 42 = 45.2% (95% range 31.2% to 60.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.05 (balance $13.95 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 19/42 = 45.2%; touch 22/46 = 47.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-02T20:00Z (market 5191991, result up)
Scored: p1 down filled at 98s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.56, 3s@0.5375609756, 5s@0.5699999998, 5s@0.57, 5s@0.56, 5s@0.57, 5s@0.57, 5s@0.57, 5s@0.57, 6s@0.57, 6s@0.57, 11s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4925, 2s@0.5, 3s@0.47, 3s@0.47, 98s@0.2399999808, 101s@0.2399999923, 107s@0.24, 128s@0.23, 128s@0.22, 152s@0.23, 158s@0.25, 281s@0.24 ...

### 2026-10-02T20:45Z (market 5192816, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 5s@0.5299999797, 5s@0.5399999568, 5s@0.5399999568, 5s@0.5299999868, 5s@0.5299998463, 6s@0.5399999568, 8s@0.539999811, 8s@0.54, 11s@0.54, 12s@0.54, 12s@0.54 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4799998464, 6s@0.4699999674, 6s@0.46, 6s@0.4699999674, 8s@0.4699999674, 8s@0.4699999674, 9s@0.4699999674, 29s@0.45, 30s@0.4799998464, 38s@0.4799999616, 44s@0.48, 44s@0.48 ...

### 2026-10-03T01:15Z (market 5195896, result down)
Scored: p1 down filled at 75s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5799999882, 12s@0.63, 12s@0.63, 12s@0.6199999587, 12s@0.59, 21s@0.6599999938, 23s@0.6645972152, 24s@0.6799998912, 32s@0.6799999767, 44s@0.7099999992, 44s@0.699999993, 45s@0.7099998509 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 74s@0.25, 75s@0.2299999517, 80s@0.21, 80s@0.2, 80s@0.219999978, 87s@0.22, 87s@0.22, 93s@0.229999994, 96s@0.23, 119s@0.2, 122s@0.2099999983, 134s@0.19 ...


_Updated 2026-10-03 02:24Z_
