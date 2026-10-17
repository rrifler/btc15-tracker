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
- Windows scored: 1560; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.4% of scored windows had a fill (98 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 136/302 = 45.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-17T03:00Z (market 5765954, result down)
Scored: p1 up filled at 11s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 11s@0.2399999862, 11s@0.2399999808, 17s@0.25, 108s@0.24, 126s@0.25, 134s@0.25, 180s@0.2, 183s@0.18, 183s@0.18, 194s@0.17, 198s@0.15, 204s@0.1685254024 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5099999215, 2s@0.68, 3s@0.6899999685, 3s@0.6899999586, 3s@0.69, 3s@0.6899999586, 3s@0.6899999685, 3s@0.6899999573, 3s@0.6899999685, 5s@0.6899999391, 5s@0.69, 6s@0.6899999391 ...

### 2026-10-17T05:00Z (market 5767371, result up)
Scored: p1 down filled at 74s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5399998832, 5s@0.54, 11s@0.56, 13s@0.56, 14s@0.649999985, 14s@0.65, 14s@0.6499999618, 14s@0.65, 14s@0.58, 14s@0.6499999923, 14s@0.57, 14s@0.5966666667 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4599997976, 2s@0.4599997976, 2s@0.469999906, 7s@0.4699999944, 8s@0.4699999988, 8s@0.47, 74s@0.2399999995, 79s@0.2099999834, 79s@0.21, 80s@0.2186842105, 80s@0.21, 83s@0.2058823511 ...

### 2026-10-17T07:30Z (market 5769569, result up)
Scored: p1 down filled at 45s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5399999978, 9s@0.5399999568, 14s@0.5799999567, 14s@0.58, 14s@0.54, 14s@0.54, 14s@0.54, 15s@0.58, 17s@0.57, 23s@0.549999945, 23s@0.5499999505, 27s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4699999556, 3s@0.46, 3s@0.4599997976, 3s@0.47, 5s@0.4699999796, 5s@0.469999906, 5s@0.47, 5s@0.47, 5s@0.47, 5s@0.47, 6s@0.47, 6s@0.47 ...


_Updated 2026-10-17 09:32Z_
