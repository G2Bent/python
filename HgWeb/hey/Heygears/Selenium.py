# -*- coding:utf-8 -*-
#Selenium调用，最好采用原本的模式，不要做任意改动，所有的改动在excel数据层改动
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class hg_selenium():
    #读取selenium的diver
    def __init__(self,driver):
        self.driver = driver

    #打开浏览器
    def open_url(self,url):
        self.driver.get(url)

    #浏览器最大化
    def hg_maximize_window(self):
        self.driver.maximize_window()

    #单个元素定位
    def hg_find_element(self,element_str):
        e = element_str.split(',')
        method,element = e[0],e[1]
        if method == 'xpath':
            element_tuple =(By.XPATH,element)
        elif method == 'css':
            element_tuple =(By.CSS_SELECTOR,element)
        elif method == 'text':
            element_tuple =(By.LINK_TEXT,element)
        elif method == 'partial_text':
            element_tuple =(By.PARTIAL_LINK_TEXT,element)
        elif method == 'tag_name':
            element_tuple =(By.TAG_NAME,element)
        elif method == 'name':
            element_tuple =(By.NAME,element)
        elif method == 'class_name':
            element_tuple =(By.CLASS_NAME,element)
        elif method == 'id':
            element_tuple =(By.ID,element)
        else: raise AttributeError
        try:
            WebDriverWait(self.driver,timeout=10,poll_frequency=0.5,ignored_exceptions=None).\
                until(ES.presence_of_element_located(element_tuple),message=str(element_tuple)+'：元素无法被找到！')
            return self.driver.find_element(*element_tuple)
        except TimeoutError as e:
            print (e)

    #定位多个元素
    def hg_find_elements(self,element_str):
        e = element_str.split(',')
        method, element = e[0], e[1]
        if method == 'xpath':
            element_tuple = (By.XPATH, element)
        elif method == 'css':
            element_tuple = (By.CSS_SELECTOR, element)
        elif method == 'text':
            element_tuple = (By.LINK_TEXT, element)
        elif method == 'partial_text':
            element_tuple = (By.PARTIAL_LINK_TEXT, element)
        elif method == 'tag_name':
            element_tuple = (By.TAG_NAME, element)
        elif method == 'name':
            element_tuple = (By.NAME, element)
        elif method == 'class_name':
            element_tuple = (By.CLASS_NAME, element)
        elif method == 'id':
            element_tuple = (By.ID, element)
        else:
            raise AttributeError
        try:
            WebDriverWait(self.driver,timeout=10,poll_frequency=0.5,ignored_exceptions=None).\
                until(ES.presence_of_element_located(element_tuple),message=str(element_tuple)+':元素无法被找到！')
            return self.driver.find_elements(*element_tuple)
        except TimeoutError as e:
            print (e)

    #获取当前页面的url
    def hg_current_url(self):
        return self.driver.current_url

    #获取页面标签属性
    def hg_get_attribute(self,element,attribute_name):
        attribute_value = self.hg_find_element(element).get_attribute(attribute_name)
        if attribute_value == None:
            raise AttributeError
        else:
            return attribute_value

    #获取文本信息
    def hg_text(self,element):
        time.sleep(1)
        return self.hg_find_element(element).text

    #隐形等待
    def hg_wait(self,time):
        '''
        hg_find_element定位元素的时候，设置了显示等待，不能与隐式等待同时使用
        如果要使用隐式等待，则设置的time的时间必须大于显式等待的时间！
        '''
        self.driver.implicitly_wait(time)

    #截图
    def hg_save_screenshot(self,file_url):
        '''仅支持截取当前页面，不能截图全图'''
        self.driver.save_screenshot(file_url)

    #清除事件
    def hg_clear(self,element):
        self.hg_find_element(element).clear()

    #send_keys事件
    def hg_send(self,element,send_values):
        self.hg_find_element(element).send_keys(send_values)

    #鼠标单击事件
    def hg_click(self,element):
        self.hg_find_element(element).click()

    #鼠标双击事件
    def hg_double_click(self,element):
        ActionChains(self.driver).double_click(self.hg_find_element(element)).perform()

    #鼠标右键操作
    def hg_context_click(self,element):
        ActionChains(self.driver).context_click(self.hg_find_element(element)).perform()

    #鼠标悬停
    def hg_move_to_element(self,element):
        ActionChains(self.driver).move_to_element(self.hg_find_element(element)).perform()

    #鼠标拖放
    def hg_drag_and_drop(self,start_element,end_element):
        start = self.hg_find_element(start_element)
        end = self.hg_find_element(end_element)
        ActionChains(self.driver).drag_and_drop(start,end).perform()

    #iframe嵌入
    def hg_iframe(self,element):
        self.driver.switch_to_frame(self.hg_find_element(element))

    #键盘事件 -- 删除事件
    def hg_keys_delete(self,element):
        self.hg_find_element(element).send_keys(Keys.BACK_SPACE)

    #运行js脚本
    def hg_run_js(self,js):
        self.driver.execute_script(js)

    #获取网页的cookie
    def hg_get_cookie(self):
        cookies = self.driver.get_cookies()
        return cookies

    #向网页添加cookie，并刷新页面
    def hg_add_cookie(self,name,value):
        self.driver.add_cookie({
            'name':name,'value':value
        })
        self.driver.refresh()
        time.sleep(1)

    #浏览器前进操作
    def hg_forward(self):
        self.driver.forward()
        time.sleep(2)

    #浏览器后退操作
    def hg_back(self):
        self.driver.back()
        time.sleep(2)