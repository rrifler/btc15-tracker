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
- Windows scored: 2724; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.3% of scored windows had a fill (351 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 269/583 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-29T10:45Z (market 6338502, result up)
Scored: p1 down filled at 92s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.58, 2s@0.6, 2s@0.5899999725, 4s@0.63, 4s@0.63, 4s@0.63, 4s@0.63, 14s@0.649999805, 17s@0.6499999935, 25s@0.65, 26s@0.6599999842, 29s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 92s@0.2199999974, 92s@0.21, 92s@0.2199999901, 94s@0.2199999972, 95s@0.229999998, 95s@0.22, 97s@0.2199999974, 100s@0.2, 103s@0.19, 104s@0.2, 112s@0.219999978, 112s@0.219999978 ...

### 2026-10-29T12:30Z (market 6340254, result up)
Scored: p1 down filled at 25s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5099998215, 5s@0.5, 5s@0.55, 7s@0.5599999969, 10s@0.5246382031, 10s@0.4778916667, 10s@0.49, 10s@0.4899999824, 10s@0.5, 11s@0.6799998912, 11s@0.6, 11s@0.5999999597 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 2s@0.48, 4s@0.51, 4s@0.5, 5s@0.459999994, 5s@0.46, 7s@0.45, 7s@0.46, 8s@0.54, 8s@0.5299999896, 8s@0.5, 8s@0.5 ...

### 2026-10-29T13:00Z (market 6341672, result up)
Scored: p1 down filled at 79s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.56, 4s@0.5599999815, 4s@0.5599999815, 4s@0.56, 4s@0.56, 4s@0.55, 4s@0.55, 10s@0.64, 17s@0.6599999897, 17s@0.66, 19s@0.6799999921, 19s@0.6799999921 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 71s@0.25, 73s@0.25, 79s@0.2, 80s@0.1899999962, 80s@0.19, 80s@0.18, 82s@0.19, 85s@0.1899999962, 88s@0.2, 89s@0.2, 91s@0.23, 92s@0.2399999923 ...

### 2026-10-29T13:15Z (market 6341812, result up)
Scored: p1 down filled at 115s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4799998464, 8s@0.49, 26s@0.51, 40s@0.5, 43s@0.5099999215, 56s@0.5999999902, 56s@0.6, 59s@0.55, 61s@0.549999945, 62s@0.5299999607, 64s@0.5376051935, 64s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5399999568, 8s@0.49, 8s@0.51, 8s@0.5099999688, 11s@0.48, 13s@0.49, 14s@0.5, 16s@0.5, 23s@0.5199999792, 23s@0.53, 29s@0.5, 37s@0.48 ...

### 2026-10-29T13:30Z (market 6342869, result down)
Scored: p1 up filled at 118s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.4899999944, 2s@0.5, 4s@0.5, 5s@0.5099998215, 5s@0.51, 5s@0.5099999776, 5s@0.5099998215, 8s@0.5099998215, 10s@0.51, 10s@0.51, 11s@0.5399999992, 11s@0.54 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5199999792, 8s@0.5, 8s@0.5, 10s@0.5, 10s@0.5, 14s@0.47, 14s@0.47, 20s@0.4799999262, 22s@0.495049505, 22s@0.48375, 22s@0.4899999824, 28s@0.48 ...


_Updated 2026-10-29 16:02Z_
