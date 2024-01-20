import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.centralbank.go.ke/rates/forex-exchange-rates/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"id":"table_1"})

head1 = table.find_all("th")[0:5]

titles = []
for i in head1:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns = titles)

rows = table.find_all("tr")

for i in rows[2:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row
    
df.to_csv("forex_exchange_cbk.csv")