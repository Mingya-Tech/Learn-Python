import requests
from bs4 import BeautifulSoup

def download_page(url):
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
   r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
   return r.text