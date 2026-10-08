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
- Windows scored: 717; excluded: 0
- Fill rate: 16.5% of scored windows had a fill (0 too small)
- Fills that reached 45c: 52 of 118 = 44.1% (95% range 35.4% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.50 (balance $7.50 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 52/118 = 44.1%; touch 58/128 = 45.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-08T08:15Z (market 5401069, result up)
Scored: p1 down filled at 97s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5899997404, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 8s@0.64, 8s@0.64, 10s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 43s@0.48, 46s@0.48, 49s@0.46, 97s@0.2399999808, 101s@0.24, 103s@0.25, 106s@0.25, 125s@0.25, 205s@0.2399999693, 206s@0.25, 224s@0.2299999517, 226s@0.25 ...

### 2026-10-08T09:15Z (market 5402424, result down)
Scored: p1 up filled at 50s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 5s@0.4599997976, 5s@0.4599999034, 12s@0.4899998383, 50s@0.23, 51s@0.2199999922, 54s@0.21, 56s@0.21, 57s@0.2199999941, 69s@0.21, 72s@0.2099999895, 78s@0.2099999983 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 15s@0.59, 15s@0.5679242487, 15s@0.55, 15s@0.55, 17s@0.6, 21s@0.6, 21s@0.6, 24s@0.6099999744, 26s@0.62, 27s@0.63, 29s@0.65 ...

### 2026-10-08T10:15Z (market 5403318, result down)
Scored: p1 up filled at 72s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.46, 6s@0.46, 72s@0.24, 72s@0.2299999993, 72s@0.23, 146s@0.24242, 146s@0.25, 159s@0.24, 161s@0.24, 161s@0.24, 162s@0.23, 162s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.54, 11s@0.5599999328, 11s@0.56, 12s@0.5799999768, 12s@0.58, 12s@0.58, 12s@0.58, 14s@0.58, 21s@0.6099999488, 21s@0.6099999831, 21s@0.6, 29s@0.6099999116 ...

### 2026-10-08T11:00Z (market 5403725, result down)
Scored: p1 up filled at 114s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 2s@0.46, 11s@0.45, 15s@0.5, 114s@0.24, 117s@0.2399999925, 120s@0.23, 128s@0.16, 129s@0.17, 129s@0.17, 129s@0.17, 129s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5799999368, 8s@0.5699999214, 12s@0.5, 12s@0.5599999898, 14s@0.5, 17s@0.5506512935, 17s@0.549999956, 17s@0.5099999776, 20s@0.5699999918, 27s@0.6, 27s@0.5899999543, 30s@0.5999999862 ...

### 2026-10-08T11:15Z (market 5403842, result up)
Scored: p1 up filled at 75s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 3s@0.47, 3s@0.469999906, 3s@0.491331484, 3s@0.47, 3s@0.47, 3s@0.4899999899, 3s@0.5, 3s@0.5, 3s@0.52, 8s@0.46, 8s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4899999944, 2s@0.49, 2s@0.49, 3s@0.509999966, 3s@0.5199999406, 3s@0.5199999792, 3s@0.494838831, 3s@0.4899999944, 3s@0.5, 5s@0.5399999771, 6s@0.5399999869, 6s@0.55 ...


_Updated 2026-10-08 14:28Z_
