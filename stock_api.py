# stock_api.py: interface for retrieving stock data 
# (minute granularity via yfinance)

import yfinance as yf

class StockAPI:
    """An interface for accessing stock data"""

    def get_stock_history(self, ticker):
        s = yf.Ticker(ticker)
        return s.history(period="max")

if __name__ == "__main__":
    sapi = StockAPI()
    print(sapi.get_stock_history("MSFT"))
