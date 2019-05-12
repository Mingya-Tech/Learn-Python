# 参考资料：
# requests中文文档：https://2.python-requests.org//zh_CN/latest/user/quickstart.html
# BeautifulSoup4中文文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
import requests
from bs4 import BeautifulSoup

# 定义要爬取的目标网站的地址
url = "https://nba.hupu.com/"
# 调用 requests 库中的 get() 函数，从目标地址中获取 Response
page = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'})

# （可选）打印出 Response 中的网页文档内容
# print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
# 打印出结果
print(soup.find_all(class_="item-list news-item"))