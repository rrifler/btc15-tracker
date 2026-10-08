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
- Windows scored: 673; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 46 of 110 = 41.8% (95% range 33.0% to 51.2%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-13.20 (balance $6.80 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 46/110 = 41.8%; touch 52/120 = 43.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-07T22:00Z (market 5392657, result up)
Scored: p1 down filled at 90s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 4s@0.5299998463, 4s@0.53, 4s@0.5299999868, 6s@0.5299999868, 6s@0.529999959, 6s@0.5299999763, 6s@0.5299999399, 7s@0.53, 7s@0.5299999868, 9s@0.53, 9s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799998464, 3s@0.47, 3s@0.4602011385, 3s@0.4599999992, 3s@0.46, 3s@0.4596489217, 3s@0.45, 4s@0.4799998551, 4s@0.4799998464, 4s@0.4799998464, 4s@0.4799998551, 4s@0.4799998551 ...

### 2026-10-07T22:45Z (market 5393003, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 53s@0.25, 68s@0.24, 70s@0.2462503645, 116s@0.25, 118s@0.23, 121s@0.2, 143s@0.2026903115, 160s@0.2, 161s@0.2, 164s@0.2128653905, 169s@0.23, 172s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5731225251, 5s@0.6, 5s@0.5899999145, 5s@0.5899997404, 10s@0.6, 10s@0.6, 11s@0.6, 14s@0.6099999892, 26s@0.61, 31s@0.65, 31s@0.61, 31s@0.649999997 ...

### 2026-10-07T23:15Z (market 5393448, result up)
Scored: p1 down filled at 67s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5199999792, 4s@0.52, 4s@0.5199999792, 5s@0.5199999792, 8s@0.52, 11s@0.58, 11s@0.56, 11s@0.5199999792, 13s@0.5899997404, 16s@0.5899999688, 20s@0.6, 20s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.48, 4s@0.49, 5s@0.4899999635, 5s@0.4899998383, 5s@0.4899998383, 7s@0.4899999714, 7s@0.49, 8s@0.49, 10s@0.4899999854, 67s@0.2019230668, 68s@0.21, 77s@0.2 ...

### 2026-10-08T00:00Z (market 5394282, result down)
Scored: p1 up filled at 115s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.46, 2s@0.46, 31s@0.45, 34s@0.52, 115s@0.24, 115s@0.25, 115s@0.24, 116s@0.24, 116s@0.25, 119s@0.23, 134s@0.21, 136s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5699999886, 7s@0.5699999983, 16s@0.5899999458, 17s@0.6, 17s@0.5982737978, 19s@0.61, 22s@0.61, 23s@0.6099998597, 35s@0.51, 35s@0.49, 35s@0.4899999706, 37s@0.56 ...

### 2026-10-08T02:15Z (market 5395211, result up)
Scored: p1 down filled at 82s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.6, 5s@0.5799999936, 5s@0.5799999768, 5s@0.5799999768, 7s@0.599999988, 10s@0.5899999866, 11s@0.5899999894, 13s@0.55, 16s@0.549999945, 19s@0.549999945, 20s@0.5199999792, 35s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.450728, 19s@0.46, 23s@0.469999906, 28s@0.4599999034, 82s@0.2299999517, 82s@0.2299999693, 101s@0.22, 103s@0.2399999852, 106s@0.25, 112s@0.2399999808, 113s@0.25, 133s@0.4599999829 ...


_Updated 2026-10-08 03:26Z_
