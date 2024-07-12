import requests

response = requests.get('https://ipinfo.io')

if response.status_code == 200:
  print(response.text)
else:
  print('Error occurred:', response.status_code)
