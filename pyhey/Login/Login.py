from selenium import webdriver

url = ("http://test.www.heygears.com/")

driver = webdriver.Chrome()
driver.get(url)

#使用微博登录（需要后台授权才能登录）

#点击登录按钮
driver.find_element_by_partial_link_text("登录").click()

