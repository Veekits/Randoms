import requests
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
search.send_keys('Datajobs')
search.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, """/html/body/div[5]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3""").click()
time.sleep(3)

search1 = driver.find_element(By.XPATH, """/html/body/div[2]/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[1]/div/div/span/input""")
search1.send_keys('Data Science')
time.sleep(3)
search2 = driver.find_element(By.XPATH, """/html/body/div[2]/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div/div/span/input""")
search2.send_keys('Remote')
time.sleep(3)
driver.find_element(By.XPATH, """/html/body/div[2]/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[2]/button""").click()

html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")
jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')
print(jobs)

