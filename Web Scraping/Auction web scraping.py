import requests
import pandas as pd 
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction"

r = requests.get(url)
print(r)