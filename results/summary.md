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
- Windows scored: 1636; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.7% of scored windows had a fill (115 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 143/320 = 44.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-17T22:00Z (market 5789685, result up)
Scored: p1 down filled at 29s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.56, 3s@0.59, 3s@0.59, 6s@0.64, 8s@0.61, 8s@0.61, 8s@0.61, 9s@0.64, 12s@0.6799999861, 12s@0.66, 12s@0.6599999892, 17s@0.7099999732 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.25, 29s@0.24, 29s@0.24, 29s@0.24, 29s@0.2, 29s@0.2, 29s@0.2, 42s@0.2299999517, 44s@0.2, 47s@0.19, 48s@0.2016992679, 48s@0.1899999992 ...

### 2026-10-17T22:15Z (market 5789842, result down)
Scored: p1 up filled at 119s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4563636364, 93s@0.25, 119s@0.24, 119s@0.24, 119s@0.24, 120s@0.25, 120s@0.25, 120s@0.23, 215s@0.23375, 216s@0.2, 240s@0.1799999856, 254s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.54, 0s@0.54, 0s@0.54, 2s@0.54, 3s@0.55, 3s@0.55, 3s@0.549999945, 3s@0.55, 3s@0.5499999933, 3s@0.55, 5s@0.56, 5s@0.56 ...

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


_Updated 2026-10-18 04:34Z_
