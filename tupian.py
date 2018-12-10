# Python3.4以上环境
# Requests模块
# lxml模块

# 1. 分析网页

# 面向对象 --》 集成封装

import requests
from lxml import etree


class Spider(object):
    def __init__(self):
        self.url = "http://www.mmjpg.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "http://www.mmjpg.com/"
        }

    def start_requests(self):
        # 2. 获取网页整体数据 Requests
        for i in range(1, 104):
            print("正在爬取%d页.....!!!!" % i)
            if i == 1:
                response = requests.get(self.url)
                html = etree.HTML(response.content.decode())
                self.xpath_data(html)
            else:
                response = requests.get(self.url + "/home/" + str(i))
                html = etree.HTML(response.content.decode())
                self.xpath_data(html)

    def xpath_data(self, html):
        # 3. 抽取我们想要的数据 lxml
        src_list = html.xpath('//div[@class="pic"]/ul/li/a/img/@src')
        alt_list = html.xpath('//div[@class="pic"]/ul/li/a/img/@alt')
        for src, alt in zip(src_list, alt_list):
            response = requests.get(src, headers=self.headers)
            file_name = alt + ".jpg"
            print("正在抓取" + file_name)
            # 4. 保存数据 jpg,png
            try:
                with open(file_name, "wb") as f:
                    f.write(response.content)
            except:
                print("保存图片失败！....")


spider = Spider()
spider.start_requests()
