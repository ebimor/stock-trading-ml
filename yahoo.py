import yfinance as yf

msft = yf.Ticker("^GSPC")
# get historical market data
hist = msft.history(period="20y")
