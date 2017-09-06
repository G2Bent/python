#打印URL
from selenium import webdriver
import time

browser = webdriver.Chrome()

url = "http://www.baidu.com"
#通过get方法获取当前URL打印
print("现在url是：",url)
browser.get(url)
time.sleep(2)

browser.find_element_by_id("kw").send_keys("seekeke")
browser.find_element_by_id("su").click()
text1 = browser.find_element_by_id("cp").text
print(text1)
print(browser.get_cookies())
time.sleep(3)

browser.quit()