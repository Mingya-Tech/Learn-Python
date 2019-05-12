# 获取豆瓣
import requests
from lxml import html

url = 'https://movie.douban.com/'  # 需要爬数据的网址
page = requests.Session().get(url)  # 调用requests包中的方法获取网址对应的页面

tree = html.fromstring( page.text )  # 解析网页
result = tree.xpath('//td[@class="title"]//a/text()')  # 获取需要的数据

# 打印出结果
print(result)

#关于//td[@class="title"//a/text
#//td相当于大目录
#[@class="title"]相当于小目录
#//a相当于最小的目录
#/text相当于文字内容
#<td class="title"><a onclick="moreurl(this, {from:'mv_rk'})" href="https://movie.douban.com/subject/30170448/">何以为家</a></td>
