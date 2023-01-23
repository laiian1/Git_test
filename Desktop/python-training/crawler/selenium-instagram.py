# 爬取ig關鍵字圖片
from itertools import count
from webbrowser import BaseBrowser, Chrome
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
path="/Users/ianlai/Desktop/python-training/crawler/chromedriver"
driver=webdriver.Chrome(path)
driver.get("https://www.instagram.com")

username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
username.clear()
password.clear()
username.send_keys('ian890924')
password.send_keys('ian241312@')
login.click()
search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    )
search.clear()
keyword= "2km2km"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    )
# media_url=[]
# if (Soup.find('//*[@id="react-root"]/section/main')!= None):
#     button = 1
#     while(button != None):
#         soup = Soup(driver.page_source,"lxml")
#         time.sleep(1)
#         img_frame = soup.find_all(class_="FFVAD")
#         vid_frame = soup.find_all(class_="_97aPb")
#         for i in img_frame:
#             try:
#                 new_img = i.img.get('src')
#                 if (new_img != None) & (new_img not in media_url):
#                     media_url.append(new_img)
#                     count += 1
#             except:
#                 pass
#         for j in vid_frame:
#             try:
#                 new_vid = j.video.get("src")
#                 if (new_vid != None) & (new_vid not in media_url):
#                     media_url.append(new_vid)
#                     count += 1
#             except:
#                 pass
#         try:
#             WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_6CZji')))
#             button = driver.find_elements_by_class_name('_97aPb')[0]
#             button.click()
#         except:
#             button = None
# else: # 如果有沒有下一頁(單張圖片或影片)
#     # 取得網頁元素框架
#     soup = Soup(driver.page_source,"lxml")
#     img_frame = soup.find(class_="FFVAD")
#     vid_frame = soup.find(class_="_97aPb")
#     # 取得圖片連結
#     try:
#         new_img = img_frame.img.get('src')
#         if (new_img != None):
#             media_url.append(new_img)
#             count += 1
#     except:
#         pass
#     # 取得影片連結
#     try:
#         new_vid = vid_frame.video.get('src')
#         if (new_vid != None):
#             media_url.append(new_vid)
#             count += 1
#     except:
#         pass

for i in range(42):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
imgs=driver.find_elements_by_class_name("FFVAD")
videos=driver.find_element_by_class_name("fXIG0")

path = os.path.join(keyword)
os.mkdir(path)
count = 0
for img in imgs:
    save_as=os.path.join(path,keyword+str(count)+"jpg.")
    print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"),save_as)
    count+=1
driver.quit()
for video in videos:
    save_as=os.path.join(path,keyword+str(count)+"mp4.")
    print(img.get_attribute("src"))
    wget.download(video.get_attribute("src"),save_as)
    count+=1
driver.quit()