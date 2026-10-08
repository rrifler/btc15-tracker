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
- Windows scored: 733; excluded: 0
- Fill rate: 16.4% of scored windows had a fill (0 too small)
- Fills that reached 45c: 53 of 120 = 44.2% (95% range 35.6% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.55 (balance $7.45 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 53/120 = 44.2%; touch 59/130 = 45.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-08T12:45Z (market 5404621, result down)
Scored: p1 up filled at 107s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 107s@0.23, 107s@0.23, 108s@0.23, 113s@0.2, 114s@0.2, 116s@0.2099999983, 116s@0.2, 117s@0.2, 119s@0.1799999856, 120s@0.19, 128s@0.229999987, 128s@0.229999987 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.558574609, 2s@0.5899999942, 2s@0.57, 3s@0.6, 3s@0.6, 6s@0.6, 9s@0.6, 9s@0.5999999607, 9s@0.6, 9s@0.5999999877, 11s@0.5999999862, 14s@0.61 ...

### 2026-10-08T13:45Z (market 5405405, result up)
Scored: p1 up filled at 48s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5199999874, 3s@0.46, 3s@0.4599997976, 3s@0.46, 3s@0.46, 3s@0.5, 3s@0.5, 5s@0.4599999849, 5s@0.469999906, 5s@0.46, 5s@0.47, 5s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.49, 2s@0.49, 3s@0.4924829299, 3s@0.4899999944, 3s@0.49, 3s@0.51, 5s@0.55, 6s@0.5399999804, 6s@0.5399999887, 8s@0.5399999568, 8s@0.54, 8s@0.55 ...

### 2026-10-08T15:15Z (market 5406435, result down)
Scored: p1 up filled at 117s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 5s@0.45, 5s@0.45, 6s@0.46, 6s@0.45, 11s@0.45, 69s@0.48, 69s@0.4599999269, 72s@0.5, 75s@0.4699999944, 80s@0.4799999846, 83s@0.4799999899 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 3s@0.565, 5s@0.56, 6s@0.5599999328, 8s@0.56, 8s@0.5599999686, 9s@0.5699999735, 9s@0.5699999731, 11s@0.559999776, 14s@0.57, 14s@0.5699999214, 17s@0.61 ...

### 2026-10-08T16:30Z (market 5407708, result down)
Scored: p1 up filled at 99s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.48, 6s@0.45, 6s@0.45, 8s@0.45, 8s@0.45, 9s@0.48, 29s@0.4599999269, 29s@0.4599999269, 30s@0.46, 32s@0.5, 32s@0.4699999422, 33s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.549999945, 6s@0.55, 6s@0.53, 11s@0.5299999512, 11s@0.5299999959, 12s@0.53, 14s@0.56, 14s@0.5699999443, 14s@0.56, 14s@0.54, 15s@0.58, 15s@0.5799999383 ...


_Updated 2026-10-08 18:28Z_
