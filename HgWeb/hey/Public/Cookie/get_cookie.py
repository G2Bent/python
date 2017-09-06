from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os

driver = webdriver.Chrome()
driver.get('http://test.ucenter.heygears.com/')


driver.find_element(By.XPATH,'//*[@id="third_sign_in"]/li[2]/a').click()

while True:
    driver.find_element(By.XPATH,'//*[@id="userId"]').clear()
    driver.find_element(By.XPATH,'//*[@id="userId"]').send_keys('18520118360')
    driver.find_element(By.XPATH,'//*[@id="passwd"]').clear()
    driver.find_element(By.XPATH,'//*[@id="passwd"]').send_keys('13713546892')
    driver.find_element(By.XPATH,'//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
    login_class = driver.find_element(By.XPATH,'//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').get_attribute('class')
    if login_class == 'WB_btn_loginIng formbtn_01':
        break
time.sleep(10)
cookies = driver.get_cookies()
for cookie in cookies:
    if cookie['name'] == 'hg_unionid':
        path = os.getcwd()+'\HeyGearsCookie.txt'
        with open(path,'w') as f:
            f.write(cookie['name']+'\n')
            f.write(cookie['value']+'\n')
driver.quit()

