"""Polymarket US access. Two clients with the same methods: Live (real orders) and DryRun (logs only).

Docs checked 2026-10-01: https://docs.polymarket.us/api-reference/sdks/python/orders.md
Order prices always refer to the YES side. Up = YES (long). Down = NO (short), so a Down price p
is sent as 1 - p. Quantity is a whole number of contracts.
"""
import datetime as dt
import email.utils
import os

import requests

GATEWAY = "https://gateway.polymarket.us"
BUY, SELL = "buy", "sell"
UP, DOWN = "up", "down"


def window_slug(ws):
    t = dt.datetime.fromtimestamp(ws, dt.timezone.utc)
    return f"cpc-btc-updown-15m-{t:%Y-%m-%d-%H%M}z"


def to_intent(side, action):
    return {
        (UP, BUY): "ORDER_INTENT_BUY_LONG", (UP, SELL): "ORDER_INTENT_SELL_LONG",
        (DOWN, BUY): "ORDER_INTENT_BUY_SHORT", (DOWN, SELL): "ORDER_INTENT_SELL_SHORT",
    }[(side, action)]


def yes_price(side, price):
    """Down orders are quoted on the YES side: a 25c NO price is a 75c YES price."""
    return round(price if side == UP else 1.0 - price, 2)


def settlement(slug):
    """Public settlement value of the YES side: 1.0 if Up won, 0.0 if Down won, None if not settled."""
    r = requests.get(f"{GATEWAY}/v1/markets/{slug}/settlement", timeout=15)
    if r.status_code != 200:
        return None
    m = requests.get(f"{GATEWAY}/v1/market/slug/{slug}", timeout=15).json().get("market", {})
    if m.get("status") != "MARKET_STATUS_RESOLVED":
        return None
    return float(r.json()["settlement"])


def clock_skew_seconds():
    """Local clock minus the gateway's HTTP Date header. Resolution is one second."""
    r = requests.head(f"{GATEWAY}/v1/markets?limit=1", timeout=10)
    server = email.utils.parsedate_to_datetime(r.headers["Date"]).timestamp()
    return dt.datetime.now(dt.timezone.utc).timestamp() - server


class LiveClient:
    def __init__(self, key_id=None, secret=None):
        from polymarket_us import PolymarketUS
        key_id = key_id or os.environ["PM_KEY_ID"]
        secret = secret or os.environ["PM_SECRET"]
        self.c = PolymarketUS(key_id=key_id, secret_key=secret)
        self.mode = "live"

    def balance(self):
        b = self.c.account.balances()
        bal = b["balances"][0] if "balances" in b else b
        return float(bal["buyingPower"])

    def place(self, slug, side, action, price, qty):
        """Post-only limit order, good till cancel. Returns the order id."""
        res = self.c.orders.create({
            "marketSlug": slug, "intent": to_intent(side, action), "type": "ORDER_TYPE_LIMIT",
            "price": {"value": f"{yes_price(side, price):.2f}", "currency": "USD"},
            "quantity": int(qty), "tif": "TIME_IN_FORCE_GOOD_TILL_CANCEL",
            "participateDontInitiate": True,
            "manualOrderIndicator": "MANUAL_ORDER_INDICATOR_AUTOMATIC",
        })
        return res["id"]

    def filled_qty(self, order_id):
        o = self.c.orders.retrieve(order_id)
        o = o.get("order", o)
        return int(float(o.get("cumQuantity", 0))), o.get("state", "")

    def cancel(self, slug, order_id):
        self.c.orders.cancel(order_id, {"marketSlug": slug})

    def cancel_all(self):
        self.c.orders.cancel_all()

    def open_order_count(self):
        return len(self.c.orders.list().get("orders", []))


class DryRunClient:
    """Same interface. Sends nothing. Never reports a fill, so it logs the buy and cancel path only."""

    def __init__(self, balance):
        self.mode = "dry"
        self._balance = float(balance)
        self._n = 0

    def balance(self):
        return self._balance

    def place(self, slug, side, action, price, qty):
        self._n += 1
        return f"dry-{self._n}"

    def filled_qty(self, order_id):
        return 0, "ORDER_STATE_NEW"

    def cancel(self, slug, order_id):
        pass

    def cancel_all(self):
        pass

    def open_order_count(self):
        return 0
