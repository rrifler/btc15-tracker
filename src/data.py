"""Public Polymarket data: Gamma (market lookup) and Data API (trades). No keys needed."""
import json
import time

import requests

GAMMA = "https://gamma-api.polymarket.com/events"
DATA = "https://data-api.polymarket.com/trades"
UA = {"User-Agent": "btc15-tracker/1.0"}


def _get(url, params, tries=5):
    last = None
    for i in range(tries):
        try:
            r = requests.get(url, params=params, headers=UA, timeout=30)
            if r.status_code == 429:
                time.sleep(2 * (i + 1))
                continue
            if r.status_code == 400:
                return None, 400
            r.raise_for_status()
            return r.json(), r.status_code
        except requests.RequestException as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET {url} failed after {tries} tries: {last}")


def slug_for(window_start):
    return f"btc-updown-15m-{window_start}"


def get_market(window_start):
    """Return dict(market_id, condition_id, up_token, down_token, result) or None if not found.

    result is "up", "down", or None when the market is not settled yet.
    """
    data, _ = _get(GAMMA, {"slug": slug_for(window_start)})
    if not data:
        return None
    m = data[0]["markets"][0]
    outcomes = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    tokens = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    prices = json.loads(m["outcomePrices"]) if isinstance(m["outcomePrices"], str) else m["outcomePrices"]
    idx = {o.lower(): i for i, o in enumerate(outcomes)}
    result = None
    if m.get("closed"):
        up_p, down_p = float(prices[idx["up"]]), float(prices[idx["down"]])
        if up_p == 1.0 and down_p == 0.0:
            result = "up"
        elif down_p == 1.0 and up_p == 0.0:
            result = "down"
    return {
        "market_id": m["id"],
        "condition_id": m["conditionId"],
        "up_token": tokens[idx["up"]],
        "down_token": tokens[idx["down"]],
        "result": result,
    }


def get_trades(condition_id, page=1000, max_offset=9000):
    """All trades for a market. Returns (trades, truncated).

    truncated is True when paging hit the cap or the API refused a deeper page, so the
    list may be incomplete.
    """
    out, offset = [], 0
    while True:
        rows, status = _get(DATA, {"market": condition_id, "limit": page, "offset": offset})
        if status == 400:
            return out, True
        out.extend(rows)
        if len(rows) < page:
            return out, False
        offset += page
        if offset > max_offset:
            return out, True


def split_trades(trades, up_token, down_token):
    up, down = [], []
    for t in trades:
        row = {"timestamp": int(t["timestamp"]), "price": float(t["price"]), "size": float(t["size"]),
               "side": t["side"]}
        if t["asset"] == up_token:
            up.append(row)
        elif t["asset"] == down_token:
            down.append(row)
    up.sort(key=lambda t: t["timestamp"])
    down.sort(key=lambda t: t["timestamp"])
    return up, down
