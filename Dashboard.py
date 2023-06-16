import pprint
import streamlit as st
import time
from datetime import datetime
import pandas as pd
import numpy as np
#import yfinance as yf
import pytz
import ccxt
import mplfinance
import plotly.graph_objects as go

st.set_page_config(
                    page_title="Live Stock Chart",
                    page_icon="🧊",
                    layout="wide",
                    )

#current_time  =  datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
current_time = datetime.now(pytz.timezone("America/New_York")).strftime("%Y-%m-%d %H:%M:%S")

st.title("Real Time Crypto Currency Dashboard")
st.subheader(f"Current Time:{current_time}/Timezone:America/New_York")



symbol = ["AAPL","MSFT","TSLA","ADBE","META","UBER"]
interval = ["1m","5m","15m","1h","4h","1d","1w"]
period = ["1d","1w","1mo","6mo","1y","5y"]

placeholder = st.empty

def get_data():
    global symbol, interval, period
    symbol = st.sidebar.selectbox("SYMBOL",symbol)
    interval = st.sidebar.selectbox("INTERVAL",interval)
    period = st.sidebar.selectbox("PERIOD",period)
    
    data = yf.download(symbol,interval,period)
    data = pd.DataFrame(data)
    st.write(data)

get_data()
"""
def binance():
    client = ccxt.binanceusdm({
                                "apiKey": "xBPLNbrLuBqVmYriXB2lVFWa7XEPfUIOyo1Sjvft21SmfZMRUxDz2BcXNFGXGxOw",
                                "secret": "W4Pv0VODKY6eT4p4wW7QwW30yXm2ziu7IYQH19M2U9NkmOH7ZBscNi4yLUhAlSFr",
                                'options': {'adjustForTimeDifference': True}
                                 })
    return client

client = binance()
#coins = list(client.symbols)
coins = list(("BTCUSDT","ETHUSDT","CRVUSDT"))

## Top Level Filter
coins = st.sidebar.selectbox("Select the Stock",coins)
timeframe = st.sidebar.selectbox("Select the Interval",["1m","3m","5m","15m","30m","1h","4h","12h","1d","3d","1w"])

limit  =  100
#st.write(f"You Selected {stock}")
#df = yf.download(tickers=str(stock),interval=str(interval),period=str(period))
def get_data():

    data = pd.DataFrame(client.fetch_ohlcv(symbol=coins,timeframe=timeframe,limit=limit), columns=["timestamp","open","high","low","close","volume"])
    data["timestamp"] = pd.to_datetime(data["timestamp"],unit="ms")


    return data

## Creating a single element container
placeholder = st.empty()

#for seconds in range(200):
while True:

    with placeholder.container():
        data = get_data()
        m1,m2,m3,m4 = st.columns(4)
        m1.metric(label=str(coins),value=data["close"].iloc[-1],delta=str(round(data["close"].iloc[-1] - data["close"].iloc[-2],2)))
        m2.metric(label=str(coins), value=data["close"].iloc[-1],
                       delta=str(round(data["close"].iloc[-1] - data["close"].iloc[-2], 2)))
        m3.metric(label=str(coins), value=data["close"].iloc[-1],
                       delta=str(round(data["close"].iloc[-1] - data["close"].iloc[-2], 2)))

        fig = go.Figure(data = [go.Candlestick(x = data["timestamp"],
                                               open = data["open"],
                                               high = data["high"],
                                               low = data["low"],
                                               close = data["close"],
                                               name=coins)])
        #fig.update_xaxes(type = "TimeStamp")
        #fig.update_layout(height = 60)


        st.plotly_chart(fig,use_container_width=True)
        st.write(data)

"""



