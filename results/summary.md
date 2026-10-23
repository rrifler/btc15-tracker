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
- Windows scored: 2145; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (236 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 207/452 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-23T05:30Z (market 6036539, result up)
Scored: p1 down filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 21s@0.49, 21s@0.45, 21s@0.45, 23s@0.5, 29s@0.5399999568, 38s@0.54, 54s@0.57, 63s@0.68, 63s@0.5999999803, 63s@0.68, 63s@0.6, 63s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.61, 14s@0.5799999724, 14s@0.57, 14s@0.6099998727, 23s@0.46, 81s@0.25, 89s@0.24, 93s@0.22, 113s@0.21, 119s@0.2, 123s@0.16, 123s@0.16 ...

### 2026-10-23T06:00Z (market 6036872, result up)
Scored: p1 up filled at 56s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 56s@0.24, 65s@0.22, 65s@0.2, 66s@0.21, 68s@0.2, 69s@0.2, 75s@0.23, 78s@0.209999995, 81s@0.2099999627, 81s@0.2099999895, 81s@0.2099999937, 84s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6020634921, 2s@0.63, 3s@0.63, 3s@0.6299998362, 5s@0.63, 8s@0.5799998764, 8s@0.58, 9s@0.5699998617, 23s@0.6199999797, 23s@0.6199999797, 27s@0.63, 27s@0.62 ...

### 2026-10-23T06:30Z (market 6037061, result up)
Scored: p1 down filled at 87s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5799999768, 3s@0.58, 5s@0.559999776, 6s@0.5728394751, 15s@0.6019372632, 15s@0.6, 17s@0.66, 17s@0.6299999845, 18s@0.66, 18s@0.66, 18s@0.66, 18s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 53s@0.25, 62s@0.25, 63s@0.25, 72s@0.25, 87s@0.25, 87s@0.23, 114s@0.25, 114s@0.25, 119s@0.25, 120s@0.25, 297s@0.45 ...

### 2026-10-23T07:15Z (market 6037415, result down)
Scored: p1 up filled at 47s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4799998464, 6s@0.4799998464, 47s@0.2299999517, 51s@0.22, 66s@0.219999978, 68s@0.219999978, 68s@0.219999978, 68s@0.219999978, 68s@0.219999978, 68s@0.219999978, 71s@0.17, 77s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5099999776, 5s@0.5199999792, 6s@0.5235283606, 14s@0.59999988, 21s@0.6, 29s@0.59, 30s@0.6499999025, 32s@0.6499999935, 33s@0.67, 36s@0.7, 36s@0.7, 36s@0.7 ...

### 2026-10-23T07:30Z (market 6037568, result down)
Scored: p1 down filled at 105s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.46, 47s@0.5799999448, 47s@0.55, 47s@0.55, 47s@0.5, 47s@0.5, 47s@0.49, 47s@0.5, 47s@0.5, 47s@0.5, 47s@0.5, 47s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5099999776, 2s@0.5099999776, 3s@0.519999984, 5s@0.52, 5s@0.54, 5s@0.52, 6s@0.57, 8s@0.5699999886, 9s@0.5699999886, 12s@0.5699999967, 23s@0.53, 24s@0.54 ...


_Updated 2026-10-23 11:38Z_
