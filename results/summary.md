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
- Windows scored: 437; excluded: 0
- Fill rate: 17.6% of scored windows had a fill (0 too small)
- Fills that reached 45c: 35 of 77 = 45.5% (95% range 34.8% to 56.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-9.15 (balance $10.85 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 35/77 = 45.5%; touch 40/83 = 48.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-05T10:30Z (market 5275569, result down)
Scored: p1 up filled at 94s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 70s@0.25, 94s@0.229999994, 95s@0.2299999517, 106s@0.229999994, 107s@0.24, 107s@0.2299999983, 109s@0.2399999808, 110s@0.2399999808, 116s@0.2, 116s@0.2, 118s@0.1899999962, 118s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.62, 4s@0.65, 5s@0.6666666667, 11s@0.68, 11s@0.68, 11s@0.68, 13s@0.6899999917, 13s@0.69, 14s@0.69, 16s@0.69, 26s@0.63, 26s@0.6299999758 ...

### 2026-10-05T10:45Z (market 5275969, result up)
Scored: p1 down filled at 107s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 11s@0.52, 11s@0.5099999608, 13s@0.5199999792, 14s@0.5199999792, 16s@0.54, 22s@0.54, 23s@0.55, 25s@0.5499999987, 38s@0.58, 38s@0.57, 38s@0.57, 40s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.54, 5s@0.53, 7s@0.58, 8s@0.5899999827, 11s@0.4899999584, 14s@0.47, 16s@0.47, 19s@0.47, 20s@0.4599997976, 23s@0.46, 25s@0.46, 26s@0.47 ...

### 2026-10-05T13:00Z (market 5279802, result up)
Scored: p1 down filled at 68s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.52, 1s@0.52, 2s@0.52, 5s@0.53, 5s@0.5599999328, 5s@0.559999776, 5s@0.53, 5s@0.5226829268, 7s@0.55, 7s@0.5499999807, 7s@0.5396247423, 7s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.46, 5s@0.501, 5s@0.532, 5s@0.47, 5s@0.4676142089, 5s@0.4799998464, 5s@0.4799998464, 7s@0.4599999387, 7s@0.46, 64s@0.25, 67s@0.25, 68s@0.2099999895 ...

### 2026-10-05T13:30Z (market 5280605, result down)
Scored: p1 up filled at 43s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.535221237, 2s@0.5399999933, 2s@0.54, 4s@0.54, 4s@0.54, 17s@0.45, 20s@0.47, 43s@0.2142651435, 44s@0.2299999987, 44s@0.2299999983, 44s@0.2299999958, 44s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 5s@0.59, 5s@0.53, 5s@0.5899999672, 5s@0.5299999607, 5s@0.58, 5s@0.57, 5s@0.5299999943, 5s@0.53, 5s@0.5299999868, 5s@0.5299999943, 5s@0.53 ...

### 2026-10-05T14:30Z (market 5282353, result down)
Scored: p1 up filled at 19s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.47, 19s@0.25, 19s@0.24, 20s@0.25, 20s@0.25, 20s@0.25, 22s@0.25, 32s@0.25, 34s@0.229999987, 35s@0.23, 38s@0.25, 38s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.6, 4s@0.5709677189, 5s@0.59999988, 5s@0.6, 7s@0.6, 7s@0.6, 7s@0.6099999831, 7s@0.59999994, 8s@0.62, 10s@0.66, 10s@0.65, 10s@0.63 ...


_Updated 2026-10-05 16:26Z_
