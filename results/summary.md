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
- Windows scored: 517; excluded: 0
- Fill rate: 17.4% of scored windows had a fill (0 too small)
- Fills that reached 45c: 38 of 90 = 42.2% (95% range 32.5% to 52.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.80 (balance $8.20 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 38/90 = 42.2%; touch 43/98 = 43.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-06T06:00Z (market 5316494, result down)
Scored: p1 up filled at 58s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5099998215, 6s@0.4599997976, 6s@0.4899998383, 7s@0.46, 58s@0.24, 61s@0.24, 63s@0.2099999983, 64s@0.19, 64s@0.2, 66s@0.18, 66s@0.18, 66s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 4s@0.5, 4s@0.5, 6s@0.5, 6s@0.51, 6s@0.5, 6s@0.5, 6s@0.5, 10s@0.559999776, 16s@0.56, 22s@0.6, 22s@0.61 ...

### 2026-10-06T06:45Z (market 5316771, result down)
Scored: p1 down filled at 106s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.59, 1s@0.580625, 3s@0.606573031, 4s@0.6199998512, 4s@0.617529819, 9s@0.64, 9s@0.6361538462, 9s@0.6199999958, 18s@0.5799999768, 24s@0.6099998597, 40s@0.6099998597, 57s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 103s@0.25, 106s@0.2399999923, 109s@0.2399999912, 115s@0.239999962, 120s@0.2312781641, 121s@0.2399999808, 138s@0.2399999923, 157s@0.2399999959, 159s@0.2399999808, 160s@0.24, 166s@0.24, 175s@0.24 ...

### 2026-10-06T07:45Z (market 5317613, result up)
Scored: p1 down filled at 106s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.56, 3s@0.56, 4s@0.57, 9s@0.6275098746, 9s@0.63, 9s@0.61, 9s@0.61, 10s@0.6599999534, 10s@0.6499999861, 16s@0.66, 27s@0.6599997888, 30s@0.67 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4554455391, 106s@0.21, 115s@0.1799999949, 124s@0.15, 124s@0.16, 126s@0.16, 127s@0.1699999836, 129s@0.15, 129s@0.1499999925, 132s@0.1499999997, 132s@0.1499999925, 138s@0.1572541578 ...

### 2026-10-06T08:00Z (market 5318206, result up)
Scored: p1 down filled at 109s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4899998383, 4s@0.47, 4s@0.455, 6s@0.528280592, 6s@0.5066248802, 9s@0.5699999214, 10s@0.57, 12s@0.5799999848, 13s@0.58, 15s@0.58, 15s@0.58, 16s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5588235245, 3s@0.57, 4s@0.52, 4s@0.5199999792, 4s@0.54, 6s@0.49, 6s@0.52, 6s@0.49, 40s@0.47, 109s@0.25, 109s@0.24, 115s@0.25 ...

### 2026-10-06T09:15Z (market 5319270, result down)
Scored: p1 down filled at 117s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999776, 4s@0.52, 7s@0.52, 19s@0.5199999792, 19s@0.52, 19s@0.5199999792, 22s@0.54, 22s@0.5379166667, 24s@0.6199998512, 24s@0.6082376632, 24s@0.62, 25s@0.6199999958 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 1s@0.5, 1s@0.5, 4s@0.4799998464, 4s@0.49, 4s@0.4899999584, 6s@0.48, 6s@0.49, 10s@0.4899999824, 18s@0.4899999824, 22s@0.4899999824, 117s@0.2199999998 ...


_Updated 2026-10-06 12:30Z_
