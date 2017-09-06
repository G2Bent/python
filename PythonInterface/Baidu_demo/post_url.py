import requests
import json
#url_post = "http://www.baidu.com/s?wd=python"将这段代码拆分
url_post = "http://www.baidu.com/s"
data = {'wd':'python'}
file = {'file':open('report.txt','rb')}
respone_message = requests.post(url=url_post,data=data,files = file)
r = requests.get("http://www.baidu.com/s")
print(respone_message.status_code)
#print(respone_message.text)
print(respone_message.json)
print(respone_message.cookies)
print(respone_message.headers)
print(r.json())
