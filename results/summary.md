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

- Verdict: **NOT ENOUGH DATA**
- Windows scored: 324; excluded: 0
- Fill rate: 17.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 25 of 55 = 45.5% (95% range 33.0% to 58.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-7.15 (balance $12.85 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 25/55 = 45.5%; touch 28/59 = 47.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-04T07:30Z (market 5227628, result down)
Scored: p1 up filled at 64s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 64s@0.24, 65s@0.24, 68s@0.2399999808, 77s@0.2399999923, 95s@0.2399999998, 98s@0.2399999998, 116s@0.24, 116s@0.24, 116s@0.2399999868, 116s@0.2322580405, 142s@0.2, 155s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.585, 4s@0.59025, 5s@0.5899998466, 23s@0.62, 23s@0.58, 25s@0.6799999952, 25s@0.68, 25s@0.6599999745, 25s@0.68, 25s@0.65, 25s@0.66, 26s@0.68 ...

### 2026-10-04T07:45Z (market 5227757, result up)
Scored: p1 down filled at 73s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.53, 4s@0.5832921383, 4s@0.5799999439, 4s@0.57, 4s@0.55, 4s@0.5699999886, 5s@0.59, 7s@0.6199999953, 7s@0.62, 8s@0.62, 8s@0.6199998512, 13s@0.6199999295 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5, 2s@0.46, 4s@0.4599997976, 4s@0.459999989, 53s@0.25, 55s@0.25, 73s@0.2115384615, 73s@0.21, 73s@0.2296173026, 137s@0.25, 146s@0.2399999923, 151s@0.2399999923 ...

### 2026-10-04T08:00Z (market 5227918, result up)
Scored: p1 down filled at 94s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.47, 2s@0.47, 2s@0.4777279753, 2s@0.469999998, 2s@0.5, 2s@0.47, 2s@0.47, 2s@0.5, 2s@0.47, 2s@0.469999998, 2s@0.47, 2s@0.469999998 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 8s@0.45, 8s@0.45, 8s@0.45, 11s@0.45, 11s@0.45, 11s@0.45, 14s@0.47, 14s@0.45, 43s@0.48, 43s@0.48, 94s@0.22 ...

### 2026-10-04T08:30Z (market 5228009, result down)
Scored: p1 up filled at 28s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 28s@0.22, 28s@0.22, 34s@0.2, 34s@0.2, 35s@0.229999987, 35s@0.2, 35s@0.2, 35s@0.2, 37s@0.2287457108, 38s@0.234056144, 40s@0.2399999998, 49s@0.15 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.61, 5s@0.6099997255, 5s@0.61, 5s@0.6099997255, 5s@0.609999986, 7s@0.5999999607, 7s@0.61, 7s@0.61, 7s@0.6, 7s@0.6099998597, 8s@0.6, 8s@0.6 ...

### 2026-10-04T10:15Z (market 5228536, result up)
Scored: p1 down filled at 37s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.65, 2s@0.65, 2s@0.6478187898, 2s@0.67, 4s@0.65, 4s@0.66, 4s@0.65, 5s@0.7299998102, 5s@0.72, 7s@0.73, 8s@0.74, 35s@0.73 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 37s@0.2399999808, 38s@0.2399999808, 40s@0.2399999981, 49s@0.2099999716, 50s@0.219999978, 50s@0.2199999863, 55s@0.2199999974, 58s@0.239999966, 58s@0.2399999631, 58s@0.2295867769, 58s@0.22, 59s@0.25 ...


_Updated 2026-10-04 12:19Z_
