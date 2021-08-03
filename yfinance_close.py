#un-comment the below pip to download yfinance for respective OS
# command to install on linux
#!pip install yfinance --user

# command to install yfinance on windows
# pip install yfinance --user

#import yfinance
import yfinance as yf

"""
Function to take ticker and return it's last closing price
"""
def last_close_price(symbol):
    print(yf.Ticker(symbol).history('1d')['Close'])
    
# MSFT for Microsfot
ticker_symbol = input("Please enter ticker symbol to know it's last closing price :\n")
last_close_price(ticker_symbol)