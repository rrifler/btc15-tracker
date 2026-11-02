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
- Windows scored: 3069; excluded: 14 (trades_truncated: 3, no_trades: 2, market_not_found: 9)
- Fill rate: 19.1% of scored windows had a fill (411 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 296/654 = 45.3%. The verdict uses strict.

## Spot-checked windows

### 2026-11-02T10:00Z (market 6514295, result down)
Scored: p1 up filled at 64s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799999616, 4s@0.48, 4s@0.4799999919, 7s@0.4799999616, 7s@0.47995, 9s@0.4799999962, 9s@0.4799999616, 12s@0.47, 13s@0.46, 63s@0.25, 63s@0.25, 64s@0.2399999808 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5199999843, 12s@0.5399999682, 12s@0.5299999956, 21s@0.5299999587, 21s@0.53, 22s@0.62, 22s@0.55, 24s@0.66, 24s@0.6199999774, 24s@0.6199999575, 24s@0.63, 24s@0.63 ...

### 2026-11-02T11:45Z (market 6518856, result down)
Scored: p1 up filled at 111s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 111s@0.2399999808, 112s@0.2399999808, 117s@0.24, 118s@0.23, 145s@0.1903715029, 147s@0.2, 147s@0.2, 150s@0.1899999962, 150s@0.19, 154s@0.16, 160s@0.13, 162s@0.13 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999886, 7s@0.59999988, 9s@0.6, 10s@0.5999999104, 12s@0.61, 12s@0.61, 12s@0.6099999322, 12s@0.6, 18s@0.6199999815, 21s@0.6199998472, 24s@0.6199998946, 24s@0.62 ...

### 2026-11-02T12:30Z (market 6522291, result down)
Scored: p1 up filled at 106s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.46, 6s@0.46, 6s@0.4599999034, 7s@0.46, 7s@0.46, 7s@0.46, 9s@0.4599997976, 10s@0.4599999387, 13s@0.46, 25s@0.45, 28s@0.47, 28s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.5499999954, 10s@0.5499999807, 13s@0.5499999945, 15s@0.57, 15s@0.549999945, 15s@0.5699999886, 31s@0.4599999034, 39s@0.46, 46s@0.5099998215, 48s@0.5799999768, 48s@0.5799999768, 48s@0.56 ...


_Updated 2026-11-02 15:39Z_
