# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
path="/Users/ianlai/Desktop/python-training/crawler/chromedriver"
driver=webdriver.Chrome(path)
driver.get("https://www.dcard.tw/f")
print(driver.title)
driver.quit()