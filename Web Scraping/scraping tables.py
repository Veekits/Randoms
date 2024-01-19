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

print(titles)

df = pd.DataFrame(columns = titles)
print(df)