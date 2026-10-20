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
- Windows scored: 1904; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (183 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 178/394 = 45.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-20T17:00Z (market 5931608, result down)
Scored: p1 up filled at 116s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 21s@0.46, 21s@0.45455, 116s@0.24, 119s@0.24, 119s@0.24, 119s@0.24, 125s@0.25, 125s@0.25, 282s@0.4699999773, 288s@0.47, 311s@0.469999906, 321s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.559999776, 3s@0.5499999783, 5s@0.56, 9s@0.5899999145, 11s@0.5899999712, 12s@0.5899999712, 15s@0.5899999841, 17s@0.589999941, 27s@0.5699999886, 33s@0.5599999805, 65s@0.61, 65s@0.5999999754 ...

### 2026-10-20T21:15Z (market 5940366, result up)
Scored: p1 down filled at 45s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5799999768, 3s@0.5799999768, 6s@0.59, 6s@0.59, 6s@0.59, 6s@0.58, 8s@0.59, 8s@0.585746, 8s@0.59, 9s@0.5599999851, 11s@0.559999776, 17s@0.54 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.45, 9s@0.45, 11s@0.45, 14s@0.4679166667, 15s@0.47, 20s@0.4599999034, 20s@0.46, 26s@0.46, 32s@0.46, 45s@0.2, 45s@0.2, 47s@0.19 ...

### 2026-10-20T23:00Z (market 5950902, result down)
Scored: p1 up filled at 86s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999387, 3s@0.469999906, 5s@0.459999996, 86s@0.24, 87s@0.25, 90s@0.25, 162s@0.25, 162s@0.25, 162s@0.25, 162s@0.25, 165s@0.2299999993, 168s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5355371759, 5s@0.5499998396, 5s@0.5499999018, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55, 8s@0.55, 8s@0.55, 8s@0.55, 8s@0.55 ...


_Updated 2026-10-20 23:32Z_
