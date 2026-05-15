# Trading Project

## Alpaca Paper Account
- Endpoint: `https://paper-api.alpaca.markets/v2`
- Account number: `PA32WPDTE1UV`
- Mode: **paper trading** (no real money)
- Credentials stored in `config.json`

## Files
| File | Purpose |
|------|---------|
| `config.json` | Alpaca API credentials |
| `trade.py` | Python helper — account info, positions, orders, place_order() |
| `orders.log` | Manual log of placed orders |
| `CLAUDE.md` | This file — project context for Claude |

## Usage
```bash
pip install requests
python trade.py
```

To place an order, uncomment the `place_order` call in `trade.py` or call the function directly.
