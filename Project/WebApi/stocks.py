import yfinance as yf


class Stock:
    def __init__(self, symbol: str):
        self.stock = yf.Ticker(symbol.upper())
