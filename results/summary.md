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
- Windows scored: 849; excluded: 0
- Fill rate: 17.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 68 of 145 = 46.9% (95% range 39.0% to 55.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.05 (balance $7.95 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 68/145 = 46.9%; touch 75/158 = 47.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T17:30Z (market 5435273, result up)
Scored: p1 up filled at 100s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.48, 4s@0.5, 5s@0.51, 5s@0.5, 7s@0.4899999334, 17s@0.51, 17s@0.5199999792, 35s@0.4599999814, 95s@0.25, 100s@0.23, 101s@0.25, 101s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5, 20s@0.48, 20s@0.46, 26s@0.48, 28s@0.49, 28s@0.51, 35s@0.549999945, 37s@0.6, 47s@0.63, 47s@0.6294444444, 47s@0.6099998597, 47s@0.62 ...

### 2026-10-09T17:45Z (market 5435833, result up)
Scored: p1 up filled at 53s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.46, 53s@0.2387395611, 115s@0.5345939729, 115s@0.4954285714, 115s@0.4899999183, 115s@0.4899999491, 116s@0.4899999743, 116s@0.4899999491, 116s@0.4899998383, 116s@0.49, 116s@0.5, 116s@0.4899999412 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.549999945, 8s@0.5733422939, 10s@0.61, 10s@0.6098006928, 10s@0.592, 11s@0.6099999748, 25s@0.59, 29s@0.6299998362, 31s@0.6099998597, 31s@0.6099999934, 31s@0.6099998597, 31s@0.609999986 ...

### 2026-10-09T18:00Z (market 5437274, result down)
Scored: p1 up filled at 88s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.45, 4s@0.45, 88s@0.239999992, 91s@0.24, 94s@0.2466456196, 94s@0.25, 235s@0.25, 259s@0.24, 260s@0.2399999981, 262s@0.219999978, 272s@0.2299999992, 274s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5799999768, 4s@0.5699999886, 5s@0.6199999531, 5s@0.61, 5s@0.61, 5s@0.6099999932, 5s@0.6, 7s@0.62, 10s@0.62, 20s@0.6099998597, 26s@0.5699999886, 29s@0.57 ...

### 2026-10-09T20:00Z (market 5442116, result up)
Scored: p1 down filled at 119s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 4s@0.4899999584, 4s@0.49, 5s@0.51, 5s@0.5, 5s@0.4899998383, 5s@0.5, 5s@0.4899999907, 5s@0.4925967742, 7s@0.5121386462, 7s@0.51, 7s@0.5099999551 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 5s@0.51, 5s@0.52, 7s@0.5, 10s@0.55, 20s@0.5399999568, 22s@0.5399999568, 119s@0.23, 131s@0.22, 131s@0.22, 131s@0.22, 133s@0.23 ...

### 2026-10-09T20:45Z (market 5442570, result up)
Scored: p1 down filled at 80s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 2s@0.56, 2s@0.55, 5s@0.61, 8s@0.6199999864, 11s@0.62, 13s@0.64, 13s@0.65, 13s@0.64, 14s@0.64, 17s@0.6499999805, 20s@0.6599997888 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 80s@0.24, 82s@0.2399999923, 82s@0.24, 83s@0.24, 89s@0.2432895978, 89s@0.24, 97s@0.25, 104s@0.2, 106s@0.2, 106s@0.21, 107s@0.2, 128s@0.1899999962 ...


_Updated 2026-10-09 23:23Z_
