import requests 
import pandas as pd
from bs4 import BeautifulSoup

url = "https://beautyclick.co.ke/?utm_source=Google+Ads&utm_medium=CPC&utm_campaign=Google+Ads_+Competitor+Keywords+ad&utm_id=Competitor+Campaign_Anniversary&gclid=CjwKCAiAqY6tBhAtEiwAHeRopRdBb2VRqhAXZ1V5IokUjXaD8gkqUI4efMoPyljb9XRp5wyBOlRlqhoCg9sQAvD_BwE"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

descs = soup.find_all("a",{"class":"cd chp"})
item_desc = []
for desc in descs:
 item = desc.text
 item_desc.append(item)
 print(item_desc)

prices = soup.find_all("span",{"class":"price"})
price_list = []
for i in prices:
 price = i.text
 price_list.append(i.text)
 print(price_list)

df = pd.DataFrame({"Item Desc": item_desc, "Item Price": price_list})
print(df)

df.to_csv("product_details.csv")