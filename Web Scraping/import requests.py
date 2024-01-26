import requests
import pandas as pd 
from bs4 import BeautifulSoup

url = "https://moneycontrol.com"

r = requests.get(url)
print(r)