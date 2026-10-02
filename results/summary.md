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
- Windows scored: 137; excluded: 0
- Fill rate: 21.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 11 of 29 = 37.9% (95% range 22.7% to 56.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.75 (balance $13.25 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 11/29 = 37.9%; touch 14/32 = 43.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-02T06:15Z (market 5171299, result up)
Scored: p1 down filled at 74s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 2s@0.48, 3s@0.45, 5s@0.469999969, 5s@0.4699999727, 5s@0.469999906, 5s@0.469999906, 5s@0.469999906, 5s@0.47, 5s@0.47, 6s@0.4699999944, 6s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.54, 5s@0.5399999568, 6s@0.5399999568, 6s@0.54, 8s@0.5199999792, 15s@0.5199999803, 15s@0.5199999692, 17s@0.5399999821, 17s@0.5399999887, 17s@0.5382754602, 17s@0.5199999889, 17s@0.5199999768 ...

### 2026-10-02T07:45Z (market 5172362, result up)
Scored: p1 down filled at 50s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.49, 3s@0.5099999304, 3s@0.51, 3s@0.5099998215, 3s@0.51, 3s@0.5099999966, 3s@0.5099999481, 3s@0.509999987, 3s@0.5099998215, 3s@0.51, 3s@0.4966887417, 5s@0.51 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 9s@0.5, 14s@0.5, 15s@0.5, 15s@0.5, 15s@0.5, 15s@0.49, 50s@0.2, 50s@0.2, 50s@0.2, 51s@0.21, 51s@0.2 ...

### 2026-10-02T08:15Z (market 5172529, result up)
Scored: p1 down filled at 81s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 12s@0.5133480361, 14s@0.5399999568, 14s@0.54, 14s@0.5199999992, 14s@0.52, 29s@0.5, 45s@0.5, 47s@0.5058333333, 50s@0.5479166667, 51s@0.5699999886, 53s@0.5799999947 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999857, 3s@0.5099998215, 3s@0.5, 5s@0.5099998215, 5s@0.5099998215, 5s@0.5099999829, 5s@0.5099998215, 8s@0.5099999551, 8s@0.51, 9s@0.5099999841, 9s@0.5099999984, 11s@0.5099998215 ...

### 2026-10-02T09:30Z (market 5172885, result up)
Scored: p1 down filled at 81s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.658, 3s@0.68, 6s@0.62, 8s@0.6199998512, 8s@0.63, 11s@0.6199998784, 11s@0.6, 14s@0.63, 14s@0.62, 14s@0.63, 14s@0.61, 14s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 81s@0.2399999808, 105s@0.1, 105s@0.1, 110s@0.1, 110s@0.11, 111s@0.1, 113s@0.1099999951, 117s@0.1, 122s@0.1, 128s@0.0899999928, 132s@0.1, 132s@0.1 ...


_Updated 2026-10-02 11:23Z_
