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
- Windows scored: 1648; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.7% of scored windows had a fill (118 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 145/324 = 44.8%. The verdict uses strict.

## Spot-checked windows

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

### 2026-10-18T04:30Z (market 5795426, result down)
Scored: p1 up filled at 75s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998383, 65s@0.25, 75s@0.24, 83s@0.24, 84s@0.24, 84s@0.25, 84s@0.24, 102s@0.21, 107s@0.219999978, 113s@0.21, 113s@0.21, 113s@0.1899999928 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.52, 5s@0.5199999898, 15s@0.5199999055, 17s@0.61, 17s@0.6, 17s@0.6, 17s@0.5899999725, 17s@0.59, 17s@0.59, 17s@0.59, 17s@0.5899999839, 17s@0.5899999546 ...

### 2026-10-18T04:45Z (market 5795592, result down)
Scored: p1 down filled at 86s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5699999886, 9s@0.6, 17s@0.58, 27s@0.59, 36s@0.6, 38s@0.61, 39s@0.61, 39s@0.61, 39s@0.62, 41s@0.66, 41s@0.6315789474, 47s@0.67 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 86s@0.24, 86s@0.25, 141s@0.25, 141s@0.25, 255s@0.4655126792, 255s@0.46, 257s@0.5, 257s@0.48, 275s@0.5199999972, 288s@0.51, 291s@0.52, 291s@0.52 ...


_Updated 2026-10-18 07:34Z_
