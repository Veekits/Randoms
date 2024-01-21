import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ke.ncbagroup.com/forex-rates/"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find_all("th", {"scope":"col"})[1:4]

head = []
for i in table:
    title = i.text
    head.append(title)
print(head)

df = pd.DataFrame(columns=head)

rows = soup.find_all("tbody") 
print(rows)

data = []
for row in rows:
    td_elements = row.find_all("td")
    filtered_data = [td.text for td in td_elements if not td.find("div", class_="currency-flag")]
    reshaped_data = [filtered_data[i:i + len(head)] for i in range(0, len(filtered_data), len(head))]
    data.extend(reshaped_data)
df = pd.DataFrame(data, columns=head)
print(df)
df.to_csv("forex_exchange_ncba.csv")

