import requests
from bs4 import BeautifulSoup
import re

url = "https://beautyclick.co.ke/?utm_source=Google+Ads&utm_medium=CPC&utm_campaign=Google+Ads_+Competitor+Keywords+ad&utm_id=Competitor+Campaign_Anniversary&gclid=CjwKCAiAqY6tBhAtEiwAHeRopRdBb2VRqhAXZ1V5IokUjXaD8gkqUI4efMoPyljb9XRp5wyBOlRlqhoCg9sQAvD_BwE"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
#data = soup.find_all(string = "L'Oreal Paris")
data = soup.find_all(string = re.compile("L'Oreal"))

print(data)