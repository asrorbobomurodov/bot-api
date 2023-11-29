from settings import TOKEN
import requests
from pprint import pprint

url = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(url)
if response.status_code == 200:
    pprint(response.json())