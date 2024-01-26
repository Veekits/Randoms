from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/Vee/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/section[1]/div/div[1]/div/div/div/div[2]/button").click()
time.sleep(2)

driver.find_element(By.XPATH, """//*[@id="__next"]/div[2]/div[1]/section/div/div[2]/div[1]/div/ul/li[5]/a""").click()