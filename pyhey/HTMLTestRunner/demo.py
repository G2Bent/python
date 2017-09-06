from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# 引入HTMLTestRunner包
from HTMLTestRunner import HTMLTestRunner


class Baidu(unittest.TestCase):
    # 初始化设置
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 百度搜索用例
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium Webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    # coding=utf-8      #防止中文乱码
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    # 加载键盘使用的模块
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    from selenium.common.exceptions import NoSuchElementException

    # 加载unittest模块
    import unittest
    import time
    import re
    # 加载HTMLTestRunner，用于生成HTMLreuslt
    import HTMLTestRunner


    class BaiduYun(unittest.TestCase):
        def setUp(self):
            self.browser = webdriver.Chrome()
            self.browser.implicitly_wait(30)
            self.base_url = "http://yun.baidu.com"
            self.verficationErrors = []
            self.accept_next_alert = True

        def Login(self):
            browser = self.browser
            browser.get(self.base_url + '/')
            u"""百度云登录"""
            browser.find_element_by_name("userName").clear()
            username = browser.find_element_by_name("userName")
            username.send_keys("alu***")
            username.send_keys(Keys.TAB)
            time.sleep(2)
            password = browser.find_element_by_name("password")
            password.send_keys("***")
            password.send_keys(Keys.ENTER)
            time.sleep(3)
            browser.close()

        def Register(self):
            browser = self.browser
            browser.get(self.base_url + '/')
            u"""立即注册百度账号"""
            browser.find_element_by_class_name("link-create").click()
            time.sleep(2)
            browser.close()

        def Link(self):
            browser = self.browser
            browser.get(self.base_url + '/')
            u"""会员中心"""
            browser.find_element_by_link_text("会员中心").click()
            time.sleep(2)
            browser.close()

        def tearDown(self):
            self.browser.quit()
            self.assertEqual([], self.verficationErrors)


    if __name__ == "__main__":
        # unittest.main()
        testunit = unittest.TestSuite()
        # 将测试用例加入到测试容器中
        testunit.addTest(BaiduYun("Login"))
        testunit.addTest(BaiduYun("Register"))
        testunit.addTest(BaiduYun("Link"))
        # 获取当前时间，这样便于下面的使用。
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # 打开一个文件，将result写入此file中
        fp = open("result" + now + ".html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
        runner.run(testunit)
        fp.close()