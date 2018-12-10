
import re
import requests
# python的第三方拓展包，解析url

url = "https://www.qiushibaike.com"  # url目的地址

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)' "
                         "' AppleWebKit/537.36 (HTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

r = requests.get(url,headers=headers)

# print(ret)
ret = r.content.decode()

# 正则表达式，提取网页想要的内容
content_list = re.findall('<div class="content">.*?<span>(.*?)</span>', ret,re.S)


# 利用正则从网页源代码把满足的内容提取出来（寻找所要内容的规律，）
print(content_list)

print(len(content_list))  # len = 多少条数据

# 把段子排版打印
for content in content_list:
    print(content)
    # 打开qiubai.txt文件， W/a:没有的话，新建一个,并命名字符格式
    with open("qiubai.txt", "a", encoding="utf-8") as f:
        # 替换br字符串，把br替换为|\n 换行
        content = re.sub('<br/>|\n',' ', content)
        #content = re.sub('<br/>''_', content)
        # '+n'每次取得一行文字就换行
        f.write(content)

        # 图片保存方法
        # content_list = re.findall('<div class="content">.*?<span>(.*?)</span>', ret, re.S)
