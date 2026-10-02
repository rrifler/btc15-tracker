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
- Windows scored: 181; excluded: 0
- Fill rate: 22.7% of scored windows had a fill (0 too small)
- Fills that reached 45c: 18 of 41 = 43.9% (95% range 29.9% to 59.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.45 (balance $13.55 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 18/41 = 43.9%; touch 21/45 = 46.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-02T16:00Z (market 5180137, result down)
Scored: p1 down filled at 84s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5870646699, 3s@0.5863354036, 5s@0.6199998946, 6s@0.6299998362, 6s@0.6299998362, 8s@0.6299998518, 9s@0.63, 9s@0.63, 9s@0.63, 9s@0.63, 9s@0.629999995, 9s@0.6299998362 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 84s@0.25, 84s@0.23, 84s@0.23, 87s@0.229999994, 90s@0.22, 102s@0.2299999782, 104s@0.2099999895, 110s@0.2, 111s@0.1899999962, 113s@0.1799999856, 114s@0.1699999983, 114s@0.17 ...

### 2026-10-02T16:45Z (market 5181880, result down)
Scored: p1 down filled at 68s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5835164835, 5s@0.59999988, 5s@0.599999988, 5s@0.6, 6s@0.6299998362, 6s@0.6211267418, 6s@0.6299998362, 6s@0.6, 6s@0.6, 8s@0.6599998059, 8s@0.6299998362, 8s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 68s@0.23999997, 68s@0.23, 69s@0.2399999808, 69s@0.2399999946, 69s@0.2399999831, 71s@0.21, 72s@0.21, 72s@0.21, 75s@0.2, 75s@0.21, 75s@0.21, 75s@0.2 ...

### 2026-10-02T17:00Z (market 5183381, result down)
Scored: p1 down filled at 110s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6199998512, 3s@0.5599999955, 3s@0.56, 3s@0.5599999955, 3s@0.5599999382, 5s@0.5599999328, 6s@0.5699999852, 6s@0.5699999214, 6s@0.5599998682, 6s@0.5699999852, 6s@0.5699999886, 6s@0.5699999886 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.5, 30s@0.509999846, 30s@0.51, 30s@0.5099998215, 30s@0.5, 30s@0.5, 35s@0.45, 35s@0.5, 35s@0.5, 35s@0.5, 38s@0.45, 42s@0.45 ...

### 2026-10-02T17:15Z (market 5183587, result down)
Scored: p1 up filled at 53s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 3s@0.54, 3s@0.5704099822, 3s@0.52, 3s@0.8, 3s@0.5299999942, 5s@0.5382473601, 15s@0.4699999863, 17s@0.4599999653, 17s@0.4599999971, 32s@0.45, 39s@0.4756815395 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.48, 2s@0.46, 2s@0.4543690504, 3s@0.5899999725, 3s@0.46, 3s@0.55, 3s@0.5, 3s@0.5, 3s@0.4599999929, 3s@0.4599999922, 3s@0.5, 3s@0.49 ...

### 2026-10-02T18:15Z (market 5187216, result down)
Scored: p1 up filled at 74s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 5s@0.5199999992, 5s@0.52, 6s@0.5299999868, 8s@0.5299999747, 8s@0.51, 14s@0.48, 17s@0.4899999984, 17s@0.4851484889, 32s@0.4799998464, 33s@0.48, 33s@0.4799998464 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.5, 3s@0.5, 5s@0.49, 6s@0.5299999868, 6s@0.52, 6s@0.51, 11s@0.5, 12s@0.5278353469, 15s@0.5299999685, 18s@0.52, 23s@0.5213114737 ...


_Updated 2026-10-02 22:22Z_
