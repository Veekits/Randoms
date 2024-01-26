from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/Vee/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/")
time.sleep(2)

search = driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/div/textarea""")
search.send_keys("jumia")
search.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, """/html/body/div[5]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3""" ).click()