import requests
from bs4 import BeautifulSoup

url ="https://beautyclick.co.ke/?utm_source=Google+Ads&utm_medium=CPC&utm_campaign=Google+Ads_+Competitor+Keywords+ad&utm_id=Competitor+Campaign_Anniversary&gclid=CjwKCAiAqY6tBhAtEiwAHeRopRdBb2VRqhAXZ1V5IokUjXaD8gkqUI4efMoPyljb9XRp5wyBOlRlqhoCg9sQAvD_BwE"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

boxes = soup.find_all("div",{"class":"product-inner pr"})
print(boxes)

box = soup.find_all("div",{"class":"product-inner pr"})[3]
print(box)

name = box.find("a", {"class":"cd chp"}).text
print(name)

price = box.find("span", {"class":"price"}).text
print(price)