import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ke.ncbagroup.com/forex-rates/"
headers = {'server': 'nginx', 'date': 'Fri, 19 Jan 2024 06:56:29 GMT', 'content-type': 'text/html; charset=UTF-8', 'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', 'last-modified': 'Fri, 19 Jan 2024 06:38:06 GMT', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'x-frame-options': 'SAMEORIGIN', 'x-content-type-options': 'nosniff', 'x-xss-protection': '1; mode=block', 'set-cookie': 'Path=/; HttpOnly; Secure', 'access-control-allow-origin': 'staging.ncbagroup.com', 'content-encoding': 'gzip'}
r = requests.get(url, headers=headers)
#print(r)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"class":"table table-bordered"})
print(table)