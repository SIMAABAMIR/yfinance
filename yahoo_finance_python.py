import requests
import json
from requests.exceptions import HTTPError

try:
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

    # MSFT for Microsoft
    ticker = input("Please enter ticker symbol to know it's last closing price :\n")


    querystring = {"symbol":ticker,"region":"US"}

    headers = {
        'x-rapidapi-key': "266c9b736dmsh35b2cf8ed6a3bd3p104e9cjsnf33eb85d2073",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # Use the json module to load response into a dictionary.
    response_dict = json.loads(response.text)

    print ('Regular Market Price for {} : ${}'.format(ticker.upper(),response_dict['price']['regularMarketPrice']['fmt']))

    print ('Regular Market Previous Price for {} : ${}'.format(ticker.upper(),response_dict['price']['regularMarketPreviousClose']['fmt']))

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Please check ticker - {ticker.upper()} / Other error occurred: {err}')
