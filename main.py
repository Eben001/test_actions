import requests
from requests.auth import HTTPProxyAuth
from pybit.unified_trading import HTTP
from google.colab import userdata
import os


response = requests.get('https://ipinfo.io')

if response.status_code == 200:
  print(response.text)
else:
  print('Error occurred:', response.status_code)


PROXY = os.environ['proxy']

os.environ['HTTP_PROXY'] = PROXY
os.environ['HTTPS_PROXY'] = PROXY


API_KEY = os.environ['api_key']
API_SECRET = os.environ['api_secret']
session = HTTP(
    testnet=True,
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def get_balance():
    try:
        resp = session.get_wallet_balance(accountType="UNIFIED", coin="USDT")['result']['list'][0]['coin'][0]['walletBalance']
        resp = float(resp)
        return resp
    except Exception as err:
        print(err)

print(f'Your balance: {get_balance()} USDT')





