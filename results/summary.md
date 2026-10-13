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
- Windows scored: 1145; excluded: 0
- Fill rate: 16.7% of scored windows had a fill (17 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 96/211 = 45.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-12T19:00Z (market 5578878, result down)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.56, 5s@0.6, 5s@0.5973333333, 5s@0.6499999594, 6s@0.652520346, 6s@0.64, 6s@0.5599999851, 8s@0.6699998822, 9s@0.6699999971, 11s@0.7299998102, 11s@0.72, 11s@0.6999999754 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.25, 32s@0.25, 72s@0.21, 78s@0.21, 86s@0.2099999969, 89s@0.21, 108s@0.2, 110s@0.17, 114s@0.14, 114s@0.15, 114s@0.16, 114s@0.16 ...

### 2026-10-12T20:15Z (market 5583075, result up)
Scored: p1 down filled at 110s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 41s@0.45, 41s@0.45, 41s@0.45, 42s@0.45, 42s@0.45, 42s@0.45, 44s@0.47, 44s@0.460432, 45s@0.469999906, 59s@0.45, 62s@0.4599999669, 72s@0.4741911583 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.63, 0s@0.64, 3s@0.64, 3s@0.649999805, 3s@0.6499999025, 5s@0.64, 8s@0.64, 14s@0.6299998362, 17s@0.6299998362, 20s@0.6299999685, 23s@0.65, 24s@0.6403846154 ...

### 2026-10-12T21:45Z (market 5587973, result down)
Scored: p1 up filled at 23s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 23s@0.25, 23s@0.24, 23s@0.25, 23s@0.25, 24s@0.25, 24s@0.2414516129, 26s@0.24, 27s@0.25, 27s@0.25, 27s@0.2199999974, 29s@0.2099999938, 29s@0.2099999895 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.63, 5s@0.63, 5s@0.6299999477, 5s@0.629999995, 6s@0.641509434, 9s@0.6499999943, 11s@0.6599999969, 15s@0.68, 15s@0.6799999985, 17s@0.7099999909, 17s@0.71, 17s@0.7099998967 ...

### 2026-10-12T22:30Z (market 5589620, result up)
Scored: p1 down filled at 102s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.62, 3s@0.59999988, 6s@0.62, 11s@0.63875, 11s@0.62, 12s@0.649999805, 15s@0.66, 17s@0.67, 26s@0.63, 36s@0.63, 36s@0.5821585714, 36s@0.5906697924 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 102s@0.25, 102s@0.2399999808, 105s@0.25, 105s@0.25, 110s@0.2399999808, 111s@0.24, 128s@0.25, 131s@0.2299999517, 131s@0.229999987, 134s@0.2099999895, 137s@0.219999978, 153s@0.25 ...

### 2026-10-13T00:45Z (market 5591686, result down)
Scored: p1 up filled at 111s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 104s@0.25, 111s@0.23, 113s@0.24, 117s@0.23, 117s@0.23, 119s@0.2399999923, 120s@0.25, 125s@0.22, 125s@0.23, 126s@0.2299999914, 128s@0.2299999993, 132s@0.1899999962 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6, 0s@0.6100569527, 3s@0.56, 3s@0.5599999869, 5s@0.66, 5s@0.65, 5s@0.62, 8s@0.6599999969, 8s@0.6710476653, 8s@0.6599999448, 8s@0.6599999921, 8s@0.66 ...


_Updated 2026-10-13 01:27Z_
