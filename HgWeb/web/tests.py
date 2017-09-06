from django.test import TestCase
from selenium import webdriver
import time
# Create your tests here.

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(5)


driver.quit()