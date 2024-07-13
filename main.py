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



def extract_links(text):
    urls = re.findall(r'(https?://\S+)', text)
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)  # Regex for emails
    at_words = re.findall(r'\B@\w+', text)  # \B ensures that @ is not preceded by a word character
    return urls + emails + at_words


def extract_date(alt_text):   
    date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{2}, \d{4}\b'
    match = re.search(date_pattern, alt_text)
    
    if match:
        return match.group(0)
    
    return None
    


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))

handle = 'burrenfarmexperience'
url = f'https://www.instagram.com/{handle}'
driver.get(url)
try:
    WebDriverWait(driver, 20).until(
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
    account_name_span = soup.find('span', class_='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')
    account_name = account_name_span.text.strip()
except:
    account_name = ''

try:
    body = soup.body

    target_text = "This account is private"

    # Check if the target text is present in the body content
    if body and target_text.lower() in body.get_text().lower():
        account_visibility = "Private"
    else:
        account_visibility = "Public"
except:
    account_visibility = "Public" 
    
try:
    post_count = soup.find('li', class_='xl565be x1m39q7l x1uw6ca5 x2pgyrj').find('span', class_='html-span').get_text()
except: 
    post_count = ''
          
try:
    followers_count = soup.find('li', class_='xl565be x1m39q7l x1uw6ca5 x2pgyrj').find_next_sibling().find('span', class_='_ac2a')['title']
except: 
    followers_count = ''

try:
    following_count = soup.find('li', class_='xl565be x1m39q7l x1uw6ca5 x2pgyrj').find_next_sibling().find_next_sibling().find('span', class_='_ac2a').get_text()
except:
    try:
      following_count = soup.find('li', class_='xl565be x1m39q7l x1uw6ca5 x2pgyrj').find_next_sibling().find_next_sibling().find('span', class_='_ac2a')['title']
    except: 
      following_count = '' 


try:
    button = driver.find_element(By.XPATH, "//div[@role='button' and @aria-disabled='false']//span[contains(text(), 'more')]")
    button.click()
except: 
    pass

try:
    soup =  BeautifulSoup(driver.page_source, 'lxml')

    bio_span = soup.find('span', class_='_ap3a _aaco _aacu _aacx _aad7 _aade')
    bio_text = bio_span.get_text()
except: 
    bio_text  = ''

try:
    bio_span = soup.find('span', class_='_ap3a _aaco _aacu _aacx _aad7 _aade')
    bio_text = bio_span.get_text()
    bio_links = extract_links(bio_text)
    bio_links_str = ',\n'.join(bio_links)

except: 
    bio_links_str = ''

        
try:
    multiple_links_button = driver.find_element(By.XPATH, "//div[@class='_ap3a _aaco _aacw _aacz _aada _aade']")
    multiple_links_button.click()
    soup = BeautifulSoup(driver.page_source, 'lxml')

    multiple_links_section = soup.find('div', class_='x78zum5 xdt5ytf xl56j7k')
    external_urls = [link.get('href') for link in multiple_links_section.find_all('a') if link.get('href')]
    separator = ' | '  
    external_urls_str = separator.join(external_urls)

    close_button = driver.find_element(By.XPATH, '//div[@aria-label="Close"]')
    close_button.click()
except: 
    try:
        single_link_section = soup.find('div', class_='x6ikm8r x10wlt62')
        external_urls_str = single_link_section.find('a')['href']
    except: 
        external_urls_str = ''
 
            
try:
    category = soup.find('div', class_='_ap3a _aaco _aacu _aacy _aad6 _aade').text.strip()
except: 
    category = ''
  
try:
    profile_photo = soup.find('meta', {'property':'og:image'})['content']

except: 
    profile_photo = ""

try:
    # Find all single boxes and put them in a list
    all_single_boxes = soup.find_all('div', class_='x1lliihq x1n2onr6 xh8yej3 x4gyw5p x2pgyrj x56m6dy x1ntc13c xn45foy x9i3mqj')

    # Remove any single box that has an svg tag with the attribute aria-label="Pinned post icon"
    filtered_boxes = [box for box in all_single_boxes if not box.find('svg', {'aria-label': 'Pinned post icon'})]

    if not filtered_boxes:
        raise ValueError("No valid single boxes found after filtering pinned posts.")

    # Pick the first item in the single boxes list
    first_box = filtered_boxes[0]
    


    # Extract the 'alt' attribute content from the img tag
    img_tag = first_box.find('img')
    if img_tag and 'alt' in img_tag.attrs:
        text_content = img_tag['alt']
    else:
        raise ValueError("No 'alt' attribute found in the img tag.")

    # Pass the text to the extract_date function
    last_post_date = extract_date(text_content)
    if last_post_date is None:
        raise ValueError("Extracted date is None.")

except Exception:
    try:
        # Extract the 'a' tag of the first item in the single boxes list and get the href attribute
        a_tag = first_box.find('a', href=True)
        if a_tag and 'href' in a_tag.attrs:
            post_url = a_tag['href']
            full_link = f'https://www.instagram.com{post_url}'
            driver.get(full_link)
            # print(full_link)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//time[@class='_a9ze _a9zf']"))
            )
           
            last_post_date =  driver.find_element(By.XPATH, "//time[@class='_a9ze _a9zf']").get_attribute('title')
        else:
            print("No 'a' tag with 'href' attribute found.")
    except Exception:
        last_post_date = ''

print(handle)
print( {
"Handle": handle,
"Account Handle": account_handle,
"Account Name": account_name,
"Category": category,
"Profile Photo":profile_photo,
"Account Visibility": account_visibility,
"Bio": bio_text,
"Bio Links": bio_links_str,
"External URLs": external_urls_str,
"Post Count": post_count,
"Followers Count": followers_count,
"Following Count": following_count,
"Last Post Date": last_post_date
})

