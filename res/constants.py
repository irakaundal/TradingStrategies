from res import id as id
import os


# url
url = {
    id.price_action: 'https://api.bitfinex.com/v2/candles/trade:{}:t{}{}/hist?sort=1',
}

# strategy wise
three_black_crow = {
    id.window_size: 14,
    id.wick_percentage: 0.5
}

double_top_double_bottom = {
    id.window_size: 14,
}

# database
database = {
    id.db_url: os.getenv('database'),
}

coinbase = [
    "TRX_USD",
    "BTC_USD",
    "ETH_USD",
    "XRP_USD",
    "ETH_BTC",
    "XRP_BTC",
    "TRX_BTC"

            ]



