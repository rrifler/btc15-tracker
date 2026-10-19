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
- Windows scored: 1801; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.3% of scored windows had a fill (156 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 163/366 = 44.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-19T15:30Z (market 5887802, result down)
Scored: p1 up filled at 53s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 53s@0.22, 60s@0.24, 60s@0.24, 62s@0.24, 81s@0.19, 84s@0.19, 84s@0.19, 86s@0.1899999962, 87s@0.1931330472, 92s@0.1899999962, 96s@0.1740718834 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.54, 0s@0.54, 3s@0.5499998382, 3s@0.549999945, 5s@0.55, 9s@0.5699999886, 14s@0.5799999448, 14s@0.5799999992, 20s@0.59, 26s@0.6, 30s@0.64, 30s@0.66 ...

### 2026-10-19T17:30Z (market 5895415, result down)
Scored: p1 up filled at 114s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 114s@0.23, 116s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 120s@0.1943823501 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6199998512, 5s@0.62, 5s@0.619999916, 11s@0.66, 15s@0.69, 15s@0.68, 15s@0.67, 17s@0.7199999424, 17s@0.7, 20s@0.7299998102, 24s@0.72, 36s@0.729999975 ...

### 2026-10-19T17:45Z (market 5896551, result down)
Scored: p1 up filled at 26s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4599999965, 26s@0.2299999517, 27s@0.23, 29s@0.25, 29s@0.2299999895, 29s@0.24, 81s@0.2, 90s@0.2099999895, 95s@0.19, 96s@0.21, 96s@0.2217857105, 96s@0.2397114567 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6, 2s@0.55, 3s@0.6, 3s@0.6099999736, 5s@0.67, 6s@0.67, 8s@0.6899999586, 11s@0.7399999871, 17s@0.74, 18s@0.74, 18s@0.75, 20s@0.76 ...

### 2026-10-19T18:00Z (market 5897933, result up)
Scored: p1 down filled at 98s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.49, 3s@0.5013333333, 3s@0.51, 3s@0.5, 3s@0.5, 5s@0.5699999556, 6s@0.57, 6s@0.57, 8s@0.5799999312, 8s@0.57, 9s@0.5799999719, 9s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 98s@0.24, 98s@0.19, 98s@0.2399999992, 105s@0.16, 105s@0.16, 110s@0.12, 111s@0.1317647053, 111s@0.1399999994, 113s@0.1099999962, 116s@0.1, 117s@0.13, 122s@0.13 ...

### 2026-10-19T18:30Z (market 5900104, result up)
Scored: p1 down filled at 87s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6, 0s@0.6, 3s@0.629999995, 3s@0.6299999685, 5s@0.64, 5s@0.629999995, 6s@0.6299999084, 8s@0.63, 8s@0.63, 8s@0.63, 8s@0.6299998362, 11s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 69s@0.25, 75s@0.25, 87s@0.21, 89s@0.2223076923, 93s@0.23, 95s@0.23, 96s@0.25, 96s@0.25, 96s@0.25, 96s@0.25, 96s@0.25, 96s@0.25 ...


_Updated 2026-10-19 21:35Z_
