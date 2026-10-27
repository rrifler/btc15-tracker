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
- Windows scored: 2572; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (318 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 255/548 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-27T17:00Z (market 6257163, result down)
Scored: p1 up filled at 117s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 20s@0.45, 21s@0.45, 21s@0.45, 24s@0.46, 24s@0.4599999115, 26s@0.4737292213, 35s@0.4799998464, 35s@0.4799999683, 36s@0.46, 117s@0.2299999982, 125s@0.24875, 128s@0.2399999992 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999718, 5s@0.52, 5s@0.5199999567, 6s@0.5199999942, 8s@0.5199999927, 8s@0.52, 9s@0.52, 9s@0.5199999802, 9s@0.5199999941, 9s@0.52, 11s@0.55, 11s@0.53 ...

### 2026-10-27T18:00Z (market 6258896, result up)
Scored: p1 up filled at 87s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.4540858059, 11s@0.4699999896, 12s@0.47, 14s@0.5, 20s@0.5424299773, 20s@0.54, 21s@0.5499999928, 21s@0.55, 23s@0.55, 30s@0.48, 66s@0.25, 87s@0.2399999808 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.56, 2s@0.54, 6s@0.59, 6s@0.6, 8s@0.57, 8s@0.54, 9s@0.54, 12s@0.53, 15s@0.5, 17s@0.49, 27s@0.45, 29s@0.52 ...

### 2026-10-27T19:00Z (market 6261685, result up)
Scored: p1 down filled at 44s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4799999694, 8s@0.4799999679, 12s@0.48, 14s@0.4799999694, 21s@0.51, 21s@0.4869928175, 24s@0.5399999992, 26s@0.54, 27s@0.6299999909, 27s@0.64, 29s@0.64, 30s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.53, 6s@0.53, 6s@0.53, 11s@0.5299998463, 11s@0.5299998463, 17s@0.5299999587, 21s@0.4599999669, 23s@0.469999906, 44s@0.2399999808, 44s@0.25, 60s@0.2099999895, 95s@0.2299999979 ...

### 2026-10-27T21:30Z (market 6267596, result up)
Scored: p1 down filled at 83s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.54, 8s@0.5499998965, 9s@0.55, 9s@0.5499999928, 12s@0.55, 21s@0.55, 23s@0.549999945, 23s@0.5499999325, 35s@0.5299998463, 39s@0.5399999966, 39s@0.54, 39s@0.5399999604 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.47, 3s@0.4699999968, 5s@0.46, 8s@0.459999988, 32s@0.4689655172, 72s@0.25, 83s@0.2, 89s@0.2, 92s@0.18, 93s@0.15, 98s@0.1199999914, 98s@0.15 ...

### 2026-10-27T22:15Z (market 6276022, result up)
Scored: p1 down filled at 78s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.47, 21s@0.4799999846, 24s@0.4799999687, 26s@0.4799999616, 32s@0.4799999262, 35s@0.52, 35s@0.52, 35s@0.5099999215, 35s@0.49, 39s@0.5199999792, 42s@0.5499999862, 42s@0.5237231109 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5199999742, 15s@0.52, 17s@0.53, 18s@0.54, 18s@0.5399999792, 18s@0.52, 32s@0.5299999868, 42s@0.4799999984, 78s@0.229999994, 78s@0.24, 84s@0.24, 84s@0.24 ...


_Updated 2026-10-27 22:39Z_
