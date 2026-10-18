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
- Windows scored: 1640; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.7% of scored windows had a fill (117 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 144/322 = 44.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-17T23:30Z (market 5791109, result up)
Scored: p1 up filled at 59s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999034, 5s@0.46, 6s@0.46, 6s@0.46, 6s@0.46, 59s@0.21, 60s@0.2190236142, 65s@0.2299999658, 65s@0.23, 65s@0.23, 68s@0.2299999993, 71s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.549999945, 6s@0.5549727273, 9s@0.59, 9s@0.5899999988, 11s@0.6499999654, 11s@0.6185714286, 11s@0.6499999838, 12s@0.6590666667, 12s@0.6499999618, 15s@0.66, 20s@0.67, 27s@0.6699999823 ...

### 2026-10-18T00:00Z (market 5791445, result down)
Scored: p1 up filled at 75s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.49, 5s@0.48, 5s@0.48, 6s@0.48, 75s@0.22, 75s@0.22, 75s@0.25, 77s@0.22, 81s@0.23, 86s@0.24, 92s@0.2399999808, 101s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5299998463, 6s@0.5179166667, 6s@0.51, 9s@0.518167, 9s@0.51, 14s@0.5099999137, 17s@0.52, 17s@0.55, 18s@0.6481481481, 20s@0.6499999814, 20s@0.65, 21s@0.6699999721 ...

### 2026-10-18T02:00Z (market 5792444, result up)
Scored: p1 down filled at 119s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.48, 3s@0.56, 3s@0.56, 27s@0.48, 41s@0.57, 41s@0.57, 41s@0.57, 42s@0.6, 42s@0.5999999769, 42s@0.6, 44s@0.61, 44s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 8s@0.45, 8s@0.45, 9s@0.47, 9s@0.4699999612, 9s@0.459999988, 14s@0.48, 15s@0.48, 15s@0.48, 17s@0.4936530324, 21s@0.5215857141, 21s@0.519999946 ...

### 2026-10-18T03:15Z (market 5793553, result down)
Scored: p1 up filled at 98s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.46, 15s@0.48, 15s@0.48, 15s@0.47, 15s@0.45, 15s@0.47, 15s@0.45, 15s@0.4799999687, 15s@0.48, 15s@0.47, 15s@0.47, 15s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.53, 0s@0.52, 0s@0.5199999792, 3s@0.5958515031, 3s@0.59999988, 3s@0.566287971, 3s@0.5516950041, 5s@0.5899999321, 5s@0.5899998466, 5s@0.5899998466, 5s@0.5999998957, 6s@0.6099999843 ...

### 2026-10-18T04:00Z (market 5794673, result down)
Scored: p1 up filled at 108s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.4518149209, 108s@0.24, 108s@0.2328, 114s@0.2399999977, 122s@0.2299999993, 125s@0.23, 129s@0.24, 129s@0.25, 186s@0.25, 186s@0.25, 216s@0.2399999965, 218s@0.2299999903 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5699999756, 3s@0.5699999886, 3s@0.5834449901, 5s@0.56, 5s@0.5599999328, 9s@0.559999832, 21s@0.6, 35s@0.57, 45s@0.62, 45s@0.6, 47s@0.64, 47s@0.64 ...


_Updated 2026-10-18 05:33Z_
