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
- Windows scored: 2293; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.0% of scored windows had a fill (261 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 222/483 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-24T20:00Z (market 6094772, result up)
Scored: p1 down filled at 83s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.56, 6s@0.5599999923, 6s@0.56, 8s@0.55, 8s@0.593997599, 8s@0.58, 8s@0.6199999369, 9s@0.6631972789, 9s@0.6699999941, 9s@0.6599999822, 9s@0.6107462468, 11s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.47, 27s@0.48, 35s@0.45, 83s@0.2, 86s@0.1899999962, 89s@0.17, 93s@0.2, 95s@0.19, 98s@0.13, 104s@0.109999989, 104s@0.1, 105s@0.1 ...

### 2026-10-24T21:15Z (market 6096506, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 3s@0.539999964, 6s@0.54, 9s@0.54, 11s@0.54, 12s@0.54, 12s@0.54, 15s@0.5099999975, 15s@0.51, 15s@0.51, 18s@0.4899998383, 29s@0.4899999684 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 15s@0.5, 15s@0.47, 15s@0.51, 15s@0.51, 15s@0.5, 15s@0.5, 15s@0.5, 15s@0.4799999687, 15s@0.5, 15s@0.48, 15s@0.5, 15s@0.5 ...

### 2026-10-24T23:30Z (market 6100216, result up)
Scored: p1 down filled at 75s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 2s@0.45, 3s@0.46, 3s@0.46, 3s@0.4558950007, 8s@0.4699999944, 12s@0.48, 14s@0.48, 27s@0.4799999616, 42s@0.49, 42s@0.4899999984, 44s@0.5399999963 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 3s@0.54, 3s@0.54, 3s@0.5399999473, 5s@0.5399999881, 5s@0.5399999881, 5s@0.5399999881, 5s@0.54, 5s@0.54, 5s@0.5399999568, 5s@0.5399999568, 6s@0.54 ...

### 2026-10-25T00:00Z (market 6101125, result down)
Scored: p1 up filled at 74s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 3s@0.45, 3s@0.45, 74s@0.22875, 74s@0.22, 75s@0.219999978, 75s@0.219999978, 90s@0.219999978, 107s@0.21, 108s@0.21, 111s@0.2142775047, 119s@0.2199999901 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5699999886, 3s@0.5599998805, 5s@0.5653662328, 5s@0.559999832, 5s@0.56, 6s@0.6099999927, 6s@0.6099999927, 6s@0.5949429787, 6s@0.61, 6s@0.599999994, 6s@0.59, 8s@0.61 ...


_Updated 2026-10-25 00:43Z_
