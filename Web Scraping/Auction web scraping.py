import requests
import pandas as pd 
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"class": "ih-td-tab auction-tbl"})
print(table)

titles = []
headers = table.find_all("th")
for header in headers:
    i = header.text
    titles.append(i)
print(titles)

df = pd.DataFrame(columns = titles)
print(df)

body = table.find_all("tr")

for i in body[1:]:
    first_td = i.find_all("td")[0].find("div",{"class":"ih-pt-ic"}).text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0, first_td)
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv("auction_stats_2024-01.csv")

