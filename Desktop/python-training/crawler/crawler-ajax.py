# 抓取 Medium.com 的文章資料
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
url="https://medium.com/_/api/home-feed"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 根據觀察，取得的資料是 JSON 格式

# 解析 JSON 格式的資料，取得每篇文章標題
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data) # 把原始 JSON 資料解析成字典/列表的表示形式
print(data)
# 取得 JSON 資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])
