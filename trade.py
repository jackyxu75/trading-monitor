import json
import requests

with open("config.json") as f:
    cfg = json.load(f)["alpaca"]

BASE_URL = cfg["endpoint"]
HEADERS = {
    "APCA-API-KEY-ID": cfg["api_key"],
    "APCA-API-SECRET-KEY": cfg["api_secret"],
    "Content-Type": "application/json",
}


def get_account():
    r = requests.get(f"{BASE_URL}/account", headers=HEADERS)
    r.raise_for_status()
    return r.json()


def get_positions():
    r = requests.get(f"{BASE_URL}/positions", headers=HEADERS)
    r.raise_for_status()
    return r.json()


def get_orders(status="all", limit=20):
    r = requests.get(f"{BASE_URL}/orders", headers=HEADERS, params={"status": status, "limit": limit})
    r.raise_for_status()
    return r.json()


def place_order(symbol: str, qty: int, side: str = "buy", order_type: str = "market", tif: str = "day"):
    payload = {
        "symbol": symbol,
        "qty": str(qty),
        "side": side,
        "type": order_type,
        "time_in_force": tif,
    }
    r = requests.post(f"{BASE_URL}/orders", headers=HEADERS, json=payload)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    account = get_account()
    print(f"Account: {account['account_number']}  |  Cash: ${account['cash']}  |  Portfolio: ${account['portfolio_value']}")

    # Example: buy 1 share of NVDA
    # order = place_order("NVDA", 1, side="buy")
    # print(f"Order placed: {order['id']}  status={order['status']}")
