import requests
from bs4 import BeautifulSoup

url = 'https://datajobs.com'

r = requests.get(url)
print(r)