import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ke.ncbagroup.com/forex-rates/"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find_all("th", {"scope":"col"})[0:3]

head = []
for i in table:
    title = i.text
    head.append(title)
print(head)

df = pd.DataFrame(columns = head)
print(df)