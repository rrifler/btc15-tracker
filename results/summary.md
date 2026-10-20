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
- Windows scored: 1849; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.6% of scored windows had a fill (169 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 171/379 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-20T03:15Z (market 5912486, result down)
Scored: p1 up filled at 110s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 96s@0.25, 107s@0.25, 110s@0.22, 111s@0.25, 126s@0.25, 176s@0.25, 179s@0.23, 195s@0.2299999517, 195s@0.2299999517, 198s@0.23, 198s@0.25, 198s@0.240625 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5899998137, 8s@0.6, 8s@0.59999988, 24s@0.6405796796, 24s@0.62, 45s@0.649999971, 51s@0.56, 57s@0.58, 57s@0.57, 57s@0.58, 66s@0.6899999606, 66s@0.69 ...

### 2026-10-20T05:45Z (market 5915434, result down)
Scored: p1 down filled at 33s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.54, 3s@0.5899997155, 3s@0.5899999145, 3s@0.56, 3s@0.56, 6s@0.6, 9s@0.6543676395, 12s@0.66, 15s@0.7, 15s@0.7, 21s@0.7399999896, 21s@0.72 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 24s@0.25, 33s@0.24, 36s@0.24, 36s@0.2399999981, 36s@0.24, 36s@0.24, 38s@0.2399999981, 39s@0.25, 48s@0.2199999974, 50s@0.2099999958, 60s@0.16, 62s@0.16 ...

### 2026-10-20T06:30Z (market 5916596, result up)
Scored: p1 down filled at 56s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.64, 4s@0.6, 4s@0.59, 4s@0.59, 4s@0.59, 5s@0.6518, 5s@0.64, 5s@0.65, 5s@0.64, 7s@0.67, 7s@0.6599997888, 7s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 50s@0.25, 50s@0.25, 50s@0.25, 56s@0.24, 65s@0.21, 68s@0.21, 86s@0.21, 88s@0.21, 89s@0.21, 91s@0.18, 97s@0.18, 97s@0.19 ...

### 2026-10-20T07:15Z (market 5917234, result down)
Scored: p1 up filled at 95s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 95s@0.2, 98s@0.19, 106s@0.1799999998, 106s@0.179999997, 115s@0.1722692308, 115s@0.1699999983, 116s@0.19, 125s@0.17, 128s@0.1799999967, 133s@0.18, 133s@0.18, 133s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5899998466, 5s@0.59, 5s@0.5923390422, 5s@0.59, 8s@0.59999994, 11s@0.599999985, 29s@0.61, 32s@0.6128058361, 34s@0.63, 49s@0.64, 49s@0.63, 49s@0.63 ...

### 2026-10-20T07:30Z (market 5917395, result down)
Scored: p1 up filled at 59s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.51, 2s@0.51, 2s@0.51, 4s@0.51, 4s@0.5099999516, 5s@0.5199999792, 7s@0.5299999587, 7s@0.5213431, 16s@0.5199999982, 17s@0.5, 17s@0.51, 25s@0.51 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 4s@0.5, 14s@0.4899999998, 17s@0.5, 17s@0.5, 17s@0.5, 17s@0.5, 17s@0.5, 17s@0.5, 17s@0.5, 17s@0.5, 19s@0.51 ...


_Updated 2026-10-20 09:37Z_
