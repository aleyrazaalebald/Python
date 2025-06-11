import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock price App
         
Shown are the Stock closing price and volume of Google!
""")

tickerSymbol = 'GOOGL'

# get data for this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical price for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2010-5-31')

#open High Low Close   Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)