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
- Windows scored: 2169; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (240 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 210/457 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-23T12:00Z (market 6040799, result down)
Scored: p1 up filled at 98s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 3s@0.4899999839, 3s@0.49, 5s@0.5499999718, 5s@0.5499999696, 5s@0.55, 5s@0.55, 5s@0.5499999549, 5s@0.5499999214, 5s@0.5299999419, 6s@0.54, 6s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.469999906, 3s@0.5299998463, 3s@0.53, 3s@0.53, 3s@0.5199999927, 3s@0.5, 3s@0.52, 5s@0.46, 5s@0.46, 5s@0.5, 6s@0.47, 6s@0.4699999395 ...

### 2026-10-23T13:30Z (market 6042317, result up)
Scored: p1 down filled at 45s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.47, 9s@0.5, 9s@0.4615904426, 9s@0.46, 9s@0.46, 9s@0.46, 9s@0.46, 9s@0.45, 12s@0.58, 12s@0.59, 12s@0.5899999725, 14s@0.5899999871 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5607476615, 2s@0.55, 3s@0.5699999214, 6s@0.57, 9s@0.56, 45s@0.25, 45s@0.24, 45s@0.24, 56s@0.25, 57s@0.2399999808, 57s@0.24, 63s@0.22 ...

### 2026-10-23T14:15Z (market 6043553, result down)
Scored: p1 up filled at 95s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 17s@0.59, 36s@0.46, 36s@0.4599999951, 38s@0.46, 38s@0.4599997976, 39s@0.4799999687, 39s@0.47, 41s@0.48, 41s@0.4799999687, 42s@0.4799998464, 44s@0.48, 44s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 23s@0.45, 24s@0.4699999944, 24s@0.4699999888, 26s@0.47, 29s@0.48, 30s@0.54, 30s@0.5, 30s@0.5, 30s@0.48, 30s@0.49, 30s@0.48, 30s@0.48 ...

### 2026-10-23T16:30Z (market 6051433, result up)
Scored: p1 down filled at 48s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.469999906, 3s@0.469999906, 5s@0.4928450974, 6s@0.5099999776, 8s@0.5075, 17s@0.5499999995, 21s@0.5399999568, 29s@0.5788422854, 32s@0.5999999724, 32s@0.6, 33s@0.62, 38s@0.6899999912 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.49, 5s@0.5399999568, 6s@0.52, 15s@0.46, 17s@0.47, 17s@0.47, 26s@0.46, 48s@0.21, 60s@0.1699999995, 65s@0.16, 69s@0.15, 71s@0.17 ...


_Updated 2026-10-23 17:35Z_
