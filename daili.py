
import requests
from lxml import etree

# 抓取的网页地址

url = 'http://www.xicidaili.com'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)' "
                         "' AppleWebKit/537.36 (HTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
                         "Accept-Encoding: gzip, deflate"
                        "Accept - Language""zh - CN, zh;q = 0.9, zh - TW;q = 0.8, en;q = 0.7"
           }
response = requests.get(url=url,headers=headers,timeout=3)
        #正则表达式提取
        #content_list = re.findall('<div class="content">.*?<span>(.*?)</span>', ret,re.S)
         #print(content_linst)

# xpath 爬虫方法
res_xpath = etree.HTML(response.text)
for node in res_xpath.xpath('//table[@id="ip_list"]//tr')[1:]:
    print(node.xpath('./td[2]/text()')[0]+":"+node.xpath('./td[3]/text()')[0])

    # 使用爬取下来的IP地址
    # proxies = {'https':'116.7.176.170:8118'}
