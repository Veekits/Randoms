from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/Vee/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/")
time.sleep(2)

search = driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/div/textarea""")
time.sleep(2)
search.send_keys("twitter login")
search.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, """/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/span/a/h3""").click()
time.sleep(2)

name_1 = driver.find_element(By.XPATH, """/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]""")
name_1.send_keys("Superselenium")
time.sleep(2)

driver.find_element(By.XPATH, """/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div""").click()
