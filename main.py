# import requests
# from pybit.unified_trading import HTTP
# import os
# response = requests.get('https://ipinfo.io')

# if response.status_code == 200:
#   print(response.text)
# else:
#   print('Error occurred:', response.status_code)


# PROXY_URL = os.environ['proxy_url']

# os.environ['HTTP_PROXY'] = PROXY_URL
# os.environ['HTTPS_PROXY'] = PROXY_URL


# API_KEY = os.environ['api_key']
# API_SECRET = os.environ['api_secret']
# session = HTTP(
#     testnet=True,
#     api_key=API_KEY,
#     api_secret=API_SECRET,
# )

# def get_balance():
#     try:
#         resp = session.get_wallet_balance(accountType="UNIFIED", coin="USDT")['result']['list'][0]['coin'][0]['walletBalance']
#         resp = float(resp)
#         return resp
#     except Exception as err:
#         print(err)

# print(f'Your balance: {get_balance()} USDT')


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.google.com')
time.sleep(3)
print(driver.title)
driver.quit()




