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
- Windows scored: 701; excluded: 0
- Fill rate: 16.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 49 of 113 = 43.4% (95% range 34.6% to 52.6%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.60 (balance $7.40 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 49/113 = 43.4%; touch 55/123 = 44.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-08T07:00Z (market 5399661, result up)
Scored: p1 up filled at 25s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 25s@0.24, 26s@0.25, 29s@0.25, 29s@0.25, 85s@0.223773241, 86s@0.22, 95s@0.23, 98s@0.2399999808, 101s@0.23, 104s@0.2299999595, 116s@0.21, 122s@0.15 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.6005710337, 7s@0.6, 8s@0.61, 10s@0.6199999943, 10s@0.6199999907, 13s@0.62, 14s@0.58, 17s@0.5899999145, 17s@0.5999999607, 17s@0.6, 17s@0.59999988, 17s@0.59 ...

### 2026-10-08T08:15Z (market 5401069, result up)
Scored: p1 down filled at 97s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5899997404, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 5s@0.64, 8s@0.64, 8s@0.64, 10s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 43s@0.48, 46s@0.48, 49s@0.46, 97s@0.2399999808, 101s@0.24, 103s@0.25, 106s@0.25, 125s@0.25, 205s@0.2399999693, 206s@0.25, 224s@0.2299999517, 226s@0.25 ...

### 2026-10-08T09:15Z (market 5402424, result down)
Scored: p1 up filled at 50s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 5s@0.4599997976, 5s@0.4599999034, 12s@0.4899998383, 50s@0.23, 51s@0.2199999922, 54s@0.21, 56s@0.21, 57s@0.2199999941, 69s@0.21, 72s@0.2099999895, 78s@0.2099999983 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 15s@0.59, 15s@0.5679242487, 15s@0.55, 15s@0.55, 17s@0.6, 21s@0.6, 21s@0.6, 24s@0.6099999744, 26s@0.62, 27s@0.63, 29s@0.65 ...


_Updated 2026-10-08 10:27Z_
