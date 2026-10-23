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
- Windows scored: 2165; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (239 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 210/456 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-23T11:00Z (market 6039176, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5799999768, 11s@0.47, 57s@0.23, 59s@0.23, 59s@0.2299999864, 60s@0.2299999926, 60s@0.2299999914, 65s@0.219999978, 66s@0.22, 66s@0.22, 69s@0.17, 75s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5005555222, 8s@0.51, 8s@0.51, 8s@0.5099999215, 8s@0.5099999378, 9s@0.5699999886, 11s@0.5099999542, 11s@0.4899999412, 12s@0.5099999949, 14s@0.51, 20s@0.6034734282, 20s@0.5901638925 ...

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


_Updated 2026-10-23 16:40Z_
