import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    product_names = [i.text for i in soup.find_all("h3", {"class": "name"})]
    product_prices = [i.text for i in soup.find_all("div", {"class": "prc"})]

    return product_names, product_prices

def scrape_jumia_catalog(base_url):
    all_product_names = []
    all_product_prices = []

    while True:
        product_names, product_prices = scrape_page(base_url)

        all_product_names.extend(product_names)
        all_product_prices.extend(product_prices)

        next_page_link = soup.find("div", {"class": "pg-w -ptm -pbxl"}).find("a", {"aria-label": "Next Page"})
        if not next_page_link:
            break

        next_page_url = "https://www.jumia.co.ke/" + next_page_link.get("href")
        base_url = next_page_url

    df = pd.DataFrame({"Product Name": all_product_names, "Product Price": all_product_prices})
    return df

url = "https://www.jumia.co.ke/catalog/?q=garnier"

# Scrape the Jumia catalog from multiple pages
result_df = scrape_jumia_catalog(url)

# Print or save the result DataFrame
print(result_df)
