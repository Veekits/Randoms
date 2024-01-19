import requests
from bs4 import BeautifulSoup

url = "https://ke.ncbagroup.com/forex-rates/"
headers = {'server': 'nginx', 'date': 'Fri, 19 Jan 2024 06:56:29 GMT', 'content-type': 'text/html; charset=UTF-8', 'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', 'last-modified': 'Fri, 19 Jan 2024 06:38:06 GMT', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'x-frame-options': 'SAMEORIGIN', 'x-content-type-options': 'nosniff', 'x-xss-protection': '1; mode=block', 'set-cookie': 'Path=/; HttpOnly; Secure', 'access-control-allow-origin': 'staging.ncbagroup.com', 'content-encoding': 'gzip'}

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", {"class": "table table-bordered"})
    
    if table:
        print(table)
    else:
        print("Table not found in the HTML content.")

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")

# Uncomment the line below to print the entire HTML content
# print(r.text)
