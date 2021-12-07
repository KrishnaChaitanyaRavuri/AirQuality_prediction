import pandas
import requests
import csv
import time
from lxml import  html
url='http://www.tianqihoubao.com/aqi/beijing.html'
session = requests.Session()
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
resp = session.get(url,headers=headers,timeout=10)
res=resp.text
paste=html.etree.HTML(res)

url_list = paste.xpath('//div[@class="box p"]//a/@href')
for url in url_list:
   url = 'http://www.tianqihoubao.com' + url
   data = pandas.read_html(url, header=0, encoding='gbk')[0]
   time.sleep(1)
   data.to_csv("Tianjing Air Quality.csv", mode='a', header=False)
