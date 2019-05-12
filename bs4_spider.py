import requests
from bs4 import BeautifulSoup

# 定义要爬取的目标网站的地址
url = "https://nba.hupu.com/"
# 调用 requests 库中的 get() 函数，从目标地址中获取 Response
page = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'})

# （可选）打印出 Response 中的网页内容（content）
# print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
# 打印出结果
print(soup.find_all(class_="item-list news-item"))