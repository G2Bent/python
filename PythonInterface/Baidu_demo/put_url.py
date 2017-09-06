import re
import requests

#获取网页内容
r = requests.get("http://test.www.him3d.cn")
data = r.text

#利用正则表达式查找所有链接
link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
for url in link_list:
    print(url)