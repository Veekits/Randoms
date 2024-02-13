from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/Vee/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/")
time.sleep(2)

search = driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys('Datajobs.com')
search.send_keys(Keys.ENTER)
time.sleep(5)

driver.find_element(By.XPATH, """/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/span/a/h3""").click()
time.sleep(3)

search1 = driver.find_element(By.XPATH, """/html/body/div[2]/div[7]/div/div/form/div[2]/input""")
search1.send_keys('Data Science')
time.sleep(3)
search2 = driver.find_element(By.XPATH, """/html/body/div[2]/div[7]/div/div/form/div[3]/input""")
search2.send_keys('Remote')
search2.send_keys(Keys.ENTER)

html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")
job_listings = soup.find_all('div', {"style" : "display:table-cell; width:520px;"})

for job_listing in job_listings:
    # Extract hyperlink
    hyperlink = job_listing.find('a')['href'] if job_listing.find('a') else ""

    # Extract job title
    job_title = job_listing.find('strong').text.strip() if job_listing.find('strong') else ""

    # Extract location
    location = job_listing.find('span', {"style": "font-size:14px; text-transform:capitalize;"}).text.strip() if job_listing.find('span') else ""

    # Extract company or institution
    company = job_listing.find('span', {"style": "font-size:14px; text-transform:capitalize;"}).text.strip() if job_listing.find('span') else ""

    # Print or store the extracted information
    print("Hyperlink:", hyperlink)
    print("Job Title:", job_title)
    print("Location:", location)
    print("Company:", company)
    print("\n")


