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
- Windows scored: 445; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (0 too small)
- Fills that reached 45c: 35 of 78 = 44.9% (95% range 34.3% to 55.9%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-9.65 (balance $10.35 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 35/78 = 44.9%; touch 40/85 = 47.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-05T13:00Z (market 5279802, result up)
Scored: p1 down filled at 68s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.52, 1s@0.52, 2s@0.52, 5s@0.53, 5s@0.5599999328, 5s@0.559999776, 5s@0.53, 5s@0.5226829268, 7s@0.55, 7s@0.5499999807, 7s@0.5396247423, 7s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.46, 5s@0.501, 5s@0.532, 5s@0.47, 5s@0.4676142089, 5s@0.4799998464, 5s@0.4799998464, 7s@0.4599999387, 7s@0.46, 64s@0.25, 67s@0.25, 68s@0.2099999895 ...

### 2026-10-05T13:30Z (market 5280605, result down)
Scored: p1 up filled at 43s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.535221237, 2s@0.5399999933, 2s@0.54, 4s@0.54, 4s@0.54, 17s@0.45, 20s@0.47, 43s@0.2142651435, 44s@0.2299999987, 44s@0.2299999983, 44s@0.2299999958, 44s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 5s@0.59, 5s@0.53, 5s@0.5899999672, 5s@0.5299999607, 5s@0.58, 5s@0.57, 5s@0.5299999943, 5s@0.53, 5s@0.5299999868, 5s@0.5299999943, 5s@0.53 ...

### 2026-10-05T14:30Z (market 5282353, result down)
Scored: p1 up filled at 19s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.47, 19s@0.25, 19s@0.24, 20s@0.25, 20s@0.25, 20s@0.25, 22s@0.25, 32s@0.25, 34s@0.229999987, 35s@0.23, 38s@0.25, 38s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.6, 4s@0.5709677189, 5s@0.59999988, 5s@0.6, 7s@0.6, 7s@0.6, 7s@0.6099999831, 7s@0.59999994, 8s@0.62, 10s@0.66, 10s@0.65, 10s@0.63 ...

### 2026-10-05T14:45Z (market 5284086, result down)
Scored: p1 up filled at 47s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4599999965, 4s@0.4599999879, 4s@0.46, 4s@0.45, 4s@0.45, 4s@0.47, 5s@0.46, 5s@0.46, 5s@0.46, 5s@0.4599997976, 5s@0.46, 7s@0.4599999563 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 4s@0.549999945, 4s@0.5599999642, 5s@0.549999945, 7s@0.549999945, 8s@0.5399999985, 8s@0.54, 10s@0.55, 10s@0.55, 10s@0.55, 10s@0.55, 10s@0.54053764 ...

### 2026-10-05T17:15Z (market 5291212, result up)
Scored: p1 down filled at 112s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 2s@0.575, 4s@0.549999945, 4s@0.56, 5s@0.549999945, 5s@0.55, 11s@0.5499999966, 17s@0.58, 19s@0.62, 19s@0.63, 19s@0.62, 19s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4599997976, 4s@0.4599999034, 4s@0.469999998, 14s@0.459999988, 79s@0.25, 112s@0.24, 113s@0.25, 115s@0.25, 115s@0.25, 128s@0.22, 143s@0.21, 143s@0.2099999983 ...


_Updated 2026-10-05 18:29Z_
