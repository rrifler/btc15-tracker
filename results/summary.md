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
- Windows scored: 1109; excluded: 0
- Fill rate: 16.7% of scored windows had a fill (11 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 89/201 = 44.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-12T10:15Z (market 5546516, result down)
Scored: p1 up filled at 117s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5199999406, 5s@0.46, 81s@0.25, 81s@0.25, 108s@0.25, 117s@0.24, 152s@0.23, 152s@0.23, 158s@0.22, 159s@0.229999994, 159s@0.22, 182s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.49, 2s@0.4907513148, 2s@0.4899999944, 12s@0.5899999288, 12s@0.5899999725, 12s@0.56, 12s@0.557826087, 15s@0.5699999886, 18s@0.6099999955, 18s@0.6, 18s@0.6, 18s@0.6 ...

### 2026-10-12T10:45Z (market 5547474, result down)
Scored: p1 down filled at 105s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.549999945, 2s@0.5499999904, 2s@0.549999945, 8s@0.5299999399, 12s@0.5299999989, 20s@0.5899999458, 20s@0.56, 20s@0.59, 24s@0.5899999725, 26s@0.5899999725, 32s@0.5899999725, 35s@0.5899999918 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4699999944, 3s@0.4739214823, 6s@0.4699999988, 8s@0.48, 105s@0.24, 108s@0.19, 110s@0.2, 116s@0.2, 116s@0.1930406852, 117s@0.2099999895, 120s@0.19, 122s@0.2 ...

### 2026-10-12T12:15Z (market 5554148, result down)
Scored: p1 up filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 5s@0.47, 5s@0.48, 5s@0.4705882353, 89s@0.23, 89s@0.24, 90s@0.23, 93s@0.2399999808, 105s@0.24, 153s@0.23, 186s@0.23, 194s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5039849624, 2s@0.5, 5s@0.549999945, 9s@0.6099999322, 9s@0.6099999962, 21s@0.6099999116, 24s@0.6261538462, 26s@0.6699999863, 26s@0.66, 26s@0.6699999984, 26s@0.64, 26s@0.64 ...

### 2026-10-12T12:45Z (market 5557504, result down)
Scored: p1 down filled at 75s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.59, 3s@0.59, 3s@0.5899999145, 3s@0.5899999458, 3s@0.5699999873, 3s@0.5899999954, 3s@0.5838058098, 5s@0.59, 5s@0.59, 6s@0.59, 6s@0.5899999841, 6s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 75s@0.25, 75s@0.24, 77s@0.25, 132s@0.23, 137s@0.2099999983, 147s@0.2099999895, 147s@0.21, 149s@0.2099999983, 149s@0.2099999895, 162s@0.19, 203s@0.16, 204s@0.16 ...

### 2026-10-12T14:45Z (market 5562096, result down)
Scored: p1 up filled at 104s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.48, 6s@0.5, 6s@0.4867249351, 9s@0.5, 9s@0.5, 11s@0.48, 11s@0.49, 14s@0.48, 21s@0.4599999387, 96s@0.25, 99s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4899999799, 2s@0.5, 3s@0.53, 3s@0.53, 6s@0.51, 12s@0.53, 17s@0.5299998463, 21s@0.5899999725, 21s@0.5609957239, 21s@0.5499999693, 21s@0.54, 23s@0.59 ...


_Updated 2026-10-12 16:27Z_
