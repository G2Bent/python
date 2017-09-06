#get请求返回信息
import requests

url_one = "http://www.baidu.com/s?wd=python"
response_message = requests.get(url_one)

print(response_message.status_code)#打印相应结果状态码
#print(response_message.text)#打印响应结果
print(response_message.url)#打印请求的url

if "python" in response_message.text:
    print("success")
if 200 == response_message.status_code:
    print("你真棒")
assert (response_message.status_code,200)

