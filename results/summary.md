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
- Windows scored: 2383; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (282 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 230/504 = 45.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-25T18:00Z (market 6145046, result down)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 8s@0.4599999833, 12s@0.47, 14s@0.49, 14s@0.4899999531, 14s@0.4899999531, 21s@0.47, 69s@0.5332309322, 71s@0.8799999909, 71s@0.61, 71s@0.8015607007, 71s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5199999659, 6s@0.53, 8s@0.55, 8s@0.54, 8s@0.55, 9s@0.55, 20s@0.53, 21s@0.5599999382, 21s@0.5499999241, 21s@0.55, 21s@0.55, 21s@0.54 ...

### 2026-10-25T19:30Z (market 6152764, result up)
Scored: p1 down filled at 83s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5599999955, 3s@0.6, 3s@0.6, 3s@0.59999988, 3s@0.6, 5s@0.6, 6s@0.6, 6s@0.6, 6s@0.6, 8s@0.6, 11s@0.599999976, 14s@0.603818 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 81s@0.25, 83s@0.24, 86s@0.24, 87s@0.24, 90s@0.24, 92s@0.24, 92s@0.24, 92s@0.2399999852, 92s@0.24, 92s@0.25, 93s@0.25, 155s@0.24 ...

### 2026-10-25T20:30Z (market 6155455, result down)
Scored: p1 up filled at 45s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999739, 5s@0.4725, 5s@0.4599999879, 5s@0.46, 8s@0.48, 8s@0.48, 18s@0.45, 18s@0.45, 20s@0.4877231256, 20s@0.45, 20s@0.4799999804, 20s@0.4877231256 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.5299999868, 14s@0.5299999587, 18s@0.56, 18s@0.56, 18s@0.5599998767, 18s@0.56, 18s@0.56, 18s@0.56, 18s@0.5599998767, 18s@0.5599999988, 18s@0.56, 18s@0.5599999969 ...

### 2026-10-25T21:00Z (market 6157418, result up)
Scored: p1 down filled at 62s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6199999864, 3s@0.61, 3s@0.6199998946, 6s@0.62, 8s@0.62, 9s@0.6199999994, 20s@0.58, 23s@0.5664688114, 23s@0.5993250166, 23s@0.58, 23s@0.5699999628, 23s@0.5738875306 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 21s@0.45, 21s@0.45, 23s@0.45, 23s@0.4599999957, 23s@0.4811234011, 23s@0.4599999387, 23s@0.46, 23s@0.46, 23s@0.4599999864, 23s@0.4599999879, 23s@0.46, 23s@0.4599999557 ...

### 2026-10-25T21:45Z (market 6159101, result down)
Scored: p1 up filled at 36s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 36s@0.229999999, 39s@0.2, 39s@0.2299999961, 39s@0.2299999983, 44s@0.2, 45s@0.2, 45s@0.2, 45s@0.2, 50s@0.2, 57s@0.2, 69s@0.16, 89s@0.1699999983 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.609999986, 0s@0.6099999961, 3s@0.6, 5s@0.61, 5s@0.6099999488, 5s@0.5699999483, 5s@0.6, 5s@0.6, 5s@0.6, 5s@0.59, 5s@0.59, 6s@0.61 ...


_Updated 2026-10-25 23:29Z_
