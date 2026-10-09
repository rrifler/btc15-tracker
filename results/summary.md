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
- Windows scored: 845; excluded: 0
- Fill rate: 16.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 68 of 143 = 47.6% (95% range 39.5% to 55.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.55 (balance $8.45 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 68/143 = 47.6%; touch 75/156 = 48.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T16:00Z (market 5432939, result up)
Scored: p1 up filled at 63s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 63s@0.22, 63s@0.21, 65s@0.22, 65s@0.22, 66s@0.22, 66s@0.22, 66s@0.22, 68s@0.22, 69s@0.23, 69s@0.23, 69s@0.22, 71s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.51, 5s@0.65, 5s@0.65, 9s@0.6599999859, 11s@0.6599999958, 12s@0.6599999534, 17s@0.6899999606, 30s@0.72, 30s@0.69, 32s@0.7199999844, 32s@0.7199999942, 33s@0.7099999949 ...

### 2026-10-09T16:15Z (market 5432984, result down)
Scored: p1 down filled at 89s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5099999516, 4s@0.559999776, 4s@0.56, 9s@0.6, 13s@0.61, 15s@0.57, 15s@0.6099999985, 16s@0.5799999768, 16s@0.58, 24s@0.6159573782, 28s@0.64, 37s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998683, 4s@0.45, 6s@0.45, 89s@0.2399999808, 90s@0.25, 90s@0.24, 104s@0.24, 108s@0.23, 147s@0.25, 147s@0.2442996743, 228s@0.45, 239s@0.47 ...

### 2026-10-09T16:45Z (market 5433727, result up)
Scored: p1 down filled at 76s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5699999436, 4s@0.56, 4s@0.5599999851, 4s@0.5599999517, 4s@0.5699999886, 4s@0.5699999886, 7s@0.56, 8s@0.56, 11s@0.5699999886, 14s@0.5699999731, 26s@0.58, 28s@0.6199998512 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.45, 71s@0.25, 76s@0.21, 76s@0.2, 76s@0.2099999895, 77s@0.2233333333, 80s@0.25, 85s@0.2299999782, 91s@0.2099999838, 92s@0.18, 100s@0.2, 103s@0.25 ...

### 2026-10-09T17:30Z (market 5435273, result up)
Scored: p1 up filled at 100s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.48, 4s@0.5, 5s@0.51, 5s@0.5, 7s@0.4899999334, 17s@0.51, 17s@0.5199999792, 35s@0.4599999814, 95s@0.25, 100s@0.23, 101s@0.25, 101s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5, 20s@0.48, 20s@0.46, 26s@0.48, 28s@0.49, 28s@0.51, 35s@0.549999945, 37s@0.6, 47s@0.63, 47s@0.6294444444, 47s@0.6099998597, 47s@0.62 ...

### 2026-10-09T17:45Z (market 5435833, result up)
Scored: p1 up filled at 53s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.46, 53s@0.2387395611, 115s@0.5345939729, 115s@0.4954285714, 115s@0.4899999183, 115s@0.4899999491, 116s@0.4899999743, 116s@0.4899999491, 116s@0.4899998383, 116s@0.49, 116s@0.5, 116s@0.4899999412 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.549999945, 8s@0.5733422939, 10s@0.61, 10s@0.6098006928, 10s@0.592, 11s@0.6099999748, 25s@0.59, 29s@0.6299998362, 31s@0.6099998597, 31s@0.6099999934, 31s@0.6099998597, 31s@0.609999986 ...


_Updated 2026-10-09 22:24Z_
