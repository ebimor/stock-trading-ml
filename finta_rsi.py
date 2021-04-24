import pandas as pd
from finta import TA
import matplotlib.pyplot as plt
import mplfinance as mpf




data = pd.read_csv("SPY_daily_finata.csv", header=0, index_col="Date", parse_dates=True)
#ohlc.columns = ["Date", "open", "high", "low", "close", "volume"]
data = data.iloc[::-1]

data['RSI']= TA.RSI(data)
data.to_csv('withRSI.csv')


#ohlc_plot = pd.concat([bbands.BB_UPPER, bbands.BB_LOWER], axis=1)

apd = mpf.make_addplot(data['RSI'].tail(300), color='g',panel=2)

mpf.plot(data.tail(300), type='candle', style='charles',
        title='SPY',
        ylabel='Price (USD)',
        ylabel_lower='Volume',
        volume=True,
        figscale=1.5,
        addplot=apd
        )
