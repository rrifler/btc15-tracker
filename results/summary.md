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
- Windows scored: 1596; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.4% of scored windows had a fill (104 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 139/308 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-17T15:30Z (market 5776464, result down)
Scored: p1 down filled at 95s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.54, 5s@0.53, 5s@0.53, 5s@0.5299999868, 11s@0.55, 12s@0.6093333333, 12s@0.6199999714, 12s@0.5805405405, 17s@0.61, 20s@0.6, 26s@0.63425, 26s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 3s@0.4599999034, 5s@0.46, 5s@0.48, 8s@0.46, 95s@0.24, 95s@0.24, 96s@0.2399999987, 96s@0.24, 96s@0.2399999987, 99s@0.24, 105s@0.2199999941 ...

### 2026-10-17T16:00Z (market 5777095, result up)
Scored: p1 down filled at 21s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.58, 3s@0.4799999904, 3s@0.48, 3s@0.5299998341, 3s@0.49, 3s@0.49, 3s@0.4799998464, 3s@0.48, 5s@0.53, 5s@0.58, 5s@0.48, 5s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 3s@0.5381188119, 3s@0.477772564, 3s@0.5, 3s@0.52, 3s@0.46, 3s@0.46, 3s@0.51, 3s@0.46, 3s@0.4599999948, 3s@0.46, 3s@0.4599999912 ...

### 2026-10-17T16:15Z (market 5777927, result down)
Scored: p1 up filled at 33s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 33s@0.24, 35s@0.2299999943, 38s@0.2299999993, 41s@0.21, 44s@0.2099999695, 47s@0.21, 53s@0.2099999983, 71s@0.2, 86s@0.19, 86s@0.19, 86s@0.19, 86s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.57, 2s@0.57, 3s@0.6, 3s@0.6, 5s@0.64, 5s@0.6, 6s@0.66, 6s@0.6513547292, 6s@0.640072, 6s@0.64, 6s@0.6499999515, 9s@0.7199999853 ...

### 2026-10-17T16:30Z (market 5778062, result down)
Scored: p1 up filled at 66s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5613145913, 3s@0.5499997609, 5s@0.5499999753, 6s@0.47, 8s@0.47, 8s@0.4699999796, 66s@0.24, 84s@0.229999984, 89s@0.21, 90s@0.2299999969, 95s@0.22, 96s@0.2299999977 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999034, 3s@0.45, 5s@0.46, 5s@0.46, 5s@0.46, 6s@0.5399999542, 6s@0.5399999534, 6s@0.5399999542, 6s@0.53, 6s@0.52, 6s@0.47, 6s@0.49 ...


_Updated 2026-10-17 18:34Z_
