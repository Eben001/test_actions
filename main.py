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
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv
import os
import re
   


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))

handle = 'virtuosoltd'
url = f'https://www.instagram.com/{handle}'
driver.get(url)
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//h2[@class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]'))
    )
except:
    pass
finally:
    soup =  BeautifulSoup(driver.page_source, 'lxml')

try:
    account_handle = soup.find('h2', class_='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj').text.strip()
except: 
    account_handle = ''
       
try:
    category = soup.find('div', class_='_ap3a _aaco _aacu _aacy _aad6 _aade').text.strip()
except: 
    category = 'cound't find the category'
  


print(account_handle)
print(category)
