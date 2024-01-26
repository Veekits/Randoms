import requests
import pandas as pd
from bs4 import BeautifulSoup

product_names = []
product_prices = []

url = "https://www.jumia.co.ke/catalog/?q=garnier"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

for i in range(0,7):
    np = soup.find("div", {"class":"pg-w -ptm -pbxl"}).find("a", {"aria-label":"Next Page"}).get("href")
    cnp = "https://www.jumia.co.ke/"+np

    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    name = soup.find_all("h3",{"class":"name"})

    for i in name:
        product_name = i.text
        product_names.append(product_name)

    price = soup.find_all("div",{"class":"prc"})
    for i in price:
        product_price = i.text
        product_prices.append(product_price)

df = pd.DataFrame({"Product Name":product_names, "Product Price":product_prices})
print(df)
 
df.to_csv("Jumia Products.csv")
