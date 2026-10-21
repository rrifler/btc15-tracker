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
- Windows scored: 1981; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.7% of scored windows had a fill (197 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 189/410 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-21T12:30Z (market 5968826, result down)
Scored: p1 up filled at 26s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799999616, 3s@0.49, 26s@0.2299999693, 26s@0.22, 26s@0.22, 27s@0.2299999864, 27s@0.23, 27s@0.2299999993, 29s@0.24, 29s@0.23, 30s@0.2199999879, 33s@0.2299999993 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.5299999868, 3s@0.52, 5s@0.54, 5s@0.53, 6s@0.5699999914, 6s@0.57, 6s@0.5490519811, 6s@0.54, 8s@0.57, 11s@0.59, 15s@0.64 ...

### 2026-10-21T13:00Z (market 5969281, result up)
Scored: p1 down filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 15s@0.549999945, 15s@0.53, 15s@0.52, 17s@0.549999945, 17s@0.55, 17s@0.55, 18s@0.56, 21s@0.56, 23s@0.58, 23s@0.54, 23s@0.55, 24s@0.54 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.48, 5s@0.5, 6s@0.5, 6s@0.5, 9s@0.4899999968, 20s@0.4599999986, 20s@0.450464843, 21s@0.45, 21s@0.4699999936, 21s@0.4699999936, 21s@0.4599999986, 23s@0.46 ...

### 2026-10-21T13:30Z (market 5969368, result down)
Scored: p1 up filled at 15s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 15s@0.2, 15s@0.2, 15s@0.2099999895, 15s@0.2099999989, 15s@0.2099999995, 17s@0.19, 17s@0.21, 17s@0.2099999997, 17s@0.22, 17s@0.2, 20s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099998543, 3s@0.5099999675, 5s@0.55, 5s@0.59, 5s@0.58, 5s@0.55, 5s@0.5799999348, 5s@0.55, 5s@0.5799999318, 5s@0.58, 5s@0.55, 5s@0.5499999998 ...

### 2026-10-21T14:00Z (market 5969709, result up)
Scored: p1 up filled at 63s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 62s@0.25, 63s@0.24, 65s@0.25, 65s@0.25, 69s@0.25, 108s@0.25, 116s@0.2497053163, 119s@0.2399999808, 122s@0.21, 129s@0.2, 135s@0.2099999895, 135s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.61, 3s@0.5999999698, 3s@0.6, 8s@0.5999999988, 8s@0.6083210325, 9s@0.59999997, 15s@0.5999999991, 18s@0.5799999768, 21s@0.5666666667, 23s@0.59, 26s@0.61, 27s@0.6099998597 ...


_Updated 2026-10-21 18:41Z_
