# workhorse for running analysis and connecting to other modules, making trades, etc.
from stock_api import StockAPI

class Workhorse:
    def __init__(self):
        self.sapi = StockAPI()


    def analyze(self):
        return self.sapi.get_stock_history("MSFT")


if __name__ == "__main__":
    w = Workhorse()
    print(w.analyze())
