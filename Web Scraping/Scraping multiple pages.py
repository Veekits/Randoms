import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/catalog/?q=garnier"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "html.parser")

np = soup.find("div", {"class":"pg-w -ptm -pbxl"}).find("a", {"aria-label":"Next Page"}).get("href")
cnp = "https://www.jumia.co.ke/"+np
print(cnp)

product_names = []
product_prices = []

all_product_names = []
all_product_prices = []

def scrape_page(soup):

    name = soup.find_all("h3",{"class":"name"})

    for i in name:
        product_name = i.text
        product_names.append(product_name)
    print(product_names)

    price = soup.find_all("div",{"class":"prc"})

    for i in price:
        product_price = i.text
        product_prices.append(product_price)
    print(product_prices)
    return(product_names, product_prices)

def jumia_catalogue(cnp):


    while True:
        all_product_names.extend(product_names)
        all_product_prices.extend(product_prices)
        if not cnp:
            break
    return(all_product_names, all_product_prices)
df = pd.DataFrame({"Product Name":all_product_names, "Product Price":all_product_prices})
print(df)


